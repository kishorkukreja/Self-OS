#!/usr/bin/env python3
"""Generate a minimal Self-OS daily operating brief.

This v0 script intentionally uses only local repo state plus optional public
GitHub API calls. It writes a markdown artifact into the Self-OS repo; a Hermes
skill/cron can later send the concise summary to Telegram.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

REPO = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_ROOT = REPO / "wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/daily"
CONTRACT_PATH = REPO / "docs/self-os-operating-contract.md"
RAW_ROOT = REPO / "wikis"
GITHUB_PULLS_URL = "https://api.github.com/repos/kishorkukreja/Self-OS/pulls?state=open&per_page=20"


def run(cmd: list[str], cwd: Path = REPO, timeout: int = 30) -> tuple[int, str]:
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout,
            check=False,
        )
        return proc.returncode, proc.stdout.strip()
    except Exception as exc:  # pragma: no cover - defensive CLI output
        return 1, f"ERROR running {' '.join(cmd)}: {exc}"


def bullet(items: Iterable[str], empty: str = "None found.") -> str:
    clean = [item for item in items if item]
    if not clean:
        return f"- {empty}"
    return "\n".join(f"- {item}" for item in clean)


def code_or_none(text: str, empty: str = "None.") -> str:
    if not text.strip():
        return empty
    return "```text\n" + text.strip() + "\n```"


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def local_date_slug(now: dt.datetime) -> str:
    # The repo convention here only needs a stable calendar date. Keep UTC to
    # avoid depending on host timezone configuration.
    return now.strftime("%Y-%m-%d")


def recent_files(root: Path, since: dt.datetime, limit: int = 25) -> list[Path]:
    if not root.exists():
        return []
    rows: list[tuple[float, Path]] = []
    since_ts = since.timestamp()
    for path in root.rglob("*.md"):
        try:
            mtime = path.stat().st_mtime
        except OSError:
            continue
        if mtime >= since_ts:
            rows.append((mtime, path))
    rows.sort(reverse=True, key=lambda row: row[0])
    return [path for _, path in rows[:limit]]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def github_open_prs() -> tuple[list[str], str | None]:
    req = urllib.request.Request(
        GITHUB_PULLS_URL,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "self-os-brief"},
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return [], f"GitHub PR lookup failed: HTTP {exc.code}"
    except Exception as exc:
        return [], f"GitHub PR lookup failed: {exc}"

    prs = []
    for pr in data[:20]:
        number = pr.get("number")
        title = pr.get("title", "Untitled")
        branch = pr.get("head", {}).get("ref", "unknown-branch")
        url = pr.get("html_url", "")
        prs.append(f"#{number} — {title} (`{branch}`) {url}".strip())
    return prs, None


def load_cron_snapshot(path: str | None) -> tuple[list[str], list[str]]:
    """Load optional Hermes cronjob(action='list') JSON saved by an agent.

    The standalone script cannot call Hermes tools directly, so cron health is
    optional until the Hermes skill wrapper injects a snapshot.
    """
    if not path:
        return [], []
    p = Path(path)
    if not p.exists():
        return [], [f"Cron snapshot path not found: {p}"]
    try:
        data = json.loads(p.read_text())
    except Exception as exc:
        return [], [f"Cron snapshot unreadable: {exc}"]

    jobs = data.get("jobs", []) if isinstance(data, dict) else []
    rows: list[str] = []
    failures: list[str] = []
    for job in jobs:
        name = job.get("name", job.get("job_id", "unnamed"))
        status = job.get("last_status") or "never-run"
        enabled = job.get("enabled")
        next_run = job.get("next_run_at") or "n/a"
        rows.append(f"{name}: last `{status}`, enabled `{enabled}`, next `{next_run}`")
        if status not in {"ok", "never-run"}:
            failures.append(f"{name}: last status `{status}`")
        if job.get("last_delivery_error"):
            failures.append(f"{name}: delivery error `{job.get('last_delivery_error')}`")
    return rows, failures


def pending_requests(limit: int = 20) -> list[str]:
    rows: list[str] = []
    for req_dir in RAW_ROOT.glob("*/raw/requests"):
        for path in sorted(req_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True):
            try:
                text = path.read_text(errors="replace")[:1200]
            except Exception:
                text = ""
            # Treat missing processed/done marker as potentially pending.
            if not re.search(r"(?im)^status:\s*(processed|done|complete|completed)\b", text):
                rows.append(rel(path))
            if len(rows) >= limit:
                return rows
    return rows


def unprocessed_raw_counts() -> list[str]:
    rows: list[str] = []
    for wiki in sorted(RAW_ROOT.glob("*")):
        raw = wiki / "raw"
        if not raw.exists():
            continue
        total = 0
        processed = 0
        for path in raw.rglob("*.md"):
            total += 1
            try:
                head = path.read_text(errors="replace")[:800]
            except Exception:
                head = ""
            if re.search(r"(?im)^status:\s*(processed|done|complete|completed)\b", head):
                processed += 1
        if total:
            rows.append(f"{wiki.name}: {total - processed} likely unprocessed / {total} raw markdown files")
    return rows


def first_line_commit_summary(line: str) -> str:
    return line.strip()


def build_brief(kind: str, cron_snapshot: str | None) -> tuple[str, str, Path]:
    now = utc_now()
    since = now - dt.timedelta(hours=24)
    date_slug = local_date_slug(now)
    out_path = DEFAULT_OUTPUT_ROOT / f"{date_slug}-{kind}.md"

    branch_rc, branch = run(["git", "branch", "--show-current"])
    status_rc, status = run(["git", "status", "--short"])
    log_rc, log = run(["git", "log", "--oneline", "--since=24 hours ago", "--", "."])
    remote_branches_rc, remote_branches = run([
        "git",
        "branch",
        "-r",
        "--list",
        "origin/wiki-*",
    ])

    recent_raw = recent_files(RAW_ROOT, since, limit=30)
    recent_plans = recent_files(REPO / "docs", since, limit=10)
    prs, pr_error = github_open_prs()
    cron_rows, cron_failures = load_cron_snapshot(cron_snapshot)
    pending = pending_requests()
    raw_counts = unprocessed_raw_counts()

    health: list[str] = []
    if branch_rc != 0 or branch != "master":
        health.append(f"Repo branch is `{branch or 'unknown'}`; expected `master` for direct raw ops.")
    if status.strip():
        health.append("Working tree has uncommitted changes.")
    if pr_error:
        health.append(pr_error)
    health.extend(cron_failures)
    if not health:
        health.append("No blocking health issue detected by local collector.")

    review_items: list[str] = []
    if prs:
        review_items.extend(prs[:10])
    if pending:
        review_items.extend(f"Pending request candidate: `{p}`" for p in pending[:10])
    if not prs and pr_error is None:
        review_items.append("No open GitHub PRs returned by public API.")

    safe_actions: list[str] = []
    if recent_raw:
        safe_actions.append("Review whether recent raw captures should wait for tonight's wiki compile or trigger a manual compile PR.")
    if pending:
        safe_actions.append("Poll and fulfill pending wiki research requests using the `wiki-research` workflow.")
    if not CONTRACT_PATH.exists():
        safe_actions.append("Create the Self-OS operating contract.")
    safe_actions.append("Keep daily brief manual until the format proves useful; do not schedule cron yet.")

    top_changed = []
    if log.strip():
        top_changed.extend(first_line_commit_summary(line) for line in log.splitlines()[:5])
    if recent_raw:
        top_changed.extend(f"Recent raw/doc file: `{rel(path)}`" for path in recent_raw[:8])
    if not top_changed:
        top_changed.append("No recent commits or raw files detected in the last 24 hours.")

    tldr_bits = []
    if status.strip():
        tldr_bits.append("repo has uncommitted changes")
    else:
        tldr_bits.append("repo is clean at collection time")
    if prs:
        tldr_bits.append(f"{len(prs)} open PR(s)")
    if pending:
        tldr_bits.append(f"{len(pending)} pending request candidate(s)")
    if cron_failures:
        tldr_bits.append(f"{len(cron_failures)} cron/automation issue(s)")
    else:
        tldr_bits.append("no injected cron failures")

    markdown = f"""---
title: Self-OS {kind.title()} Brief — {date_slug}
type: self-os-operating-brief
status: raw
created_at: {now.isoformat()}
brief_kind: {kind}
source: scripts/generate_self_os_brief.py
---

# Self-OS {kind.title()} Brief — {date_slug}

## TL;DR

- {"; ".join(tldr_bits)}.
- Top next move: inspect this first manual brief, then decide whether the brief shape is useful enough to wrap in a Hermes skill.

## Changed Since Last Brief

### Recent commits, last 24h

{code_or_none(log, "No commits in the last 24 hours.")}

### Recent raw/wiki/doc markdown files, last 24h

{bullet([f"`{rel(path)}`" for path in recent_raw + recent_plans], "No recent markdown files detected.")}

## Needs Kishor Review

{bullet(review_items, "No review items detected by local collector.")}

## Safe Agent Actions

{bullet(safe_actions)}

## Decisions Needed

- Is this daily brief shape useful enough to turn into the `self-os-daily-brief` Hermes skill?
- Should the next run include Hermes cron snapshots via skill wrapper, or keep the script local-only for one more iteration?
- Should daily briefs be sent once per day first, before adding morning/evening split?

## Health / Failures

### Git state

- Branch: `{branch or 'unknown'}`
- Working tree: {'dirty' if status.strip() else 'clean'}

{code_or_none(status, "Working tree clean.")}

### Open wiki branches

{code_or_none(remote_branches, "No remote wiki branches listed.")}

### Cron / automation snapshot

{bullet(cron_rows, "Cron snapshot not injected. Hermes skill wrapper should add this later.")}

### Detected health notes

{bullet(health)}

## Raw Backlog Signal

This is a coarse local scan. It counts raw markdown files that do not appear to have a processed/done status marker in the frontmatter.

{bullet(raw_counts, "No raw markdown files found.")}

## Pending Request Candidates

{bullet([f"`{p}`" for p in pending], "No pending request files found.")}

## Operating Contract Used

- `{rel(CONTRACT_PATH)}` {'exists' if CONTRACT_PATH.exists() else 'missing'}

## Next Suggested Prompt

```text
Use the Self-OS operating contract and this first manual brief to create the self-os-daily-brief Hermes skill, but do not schedule cron yet. Run the skill manually once and compare its Telegram summary against the saved markdown artifact.
```
"""

    telegram_summary = "\n".join([
        f"Self-OS {kind.title()} Brief — {date_slug}",
        f"- State: {'dirty working tree' if status.strip() else 'repo clean at collection time'}; {len(prs)} open PR(s); {len(pending)} pending request candidate(s).",
        f"- Recent files detected: {len(recent_raw) + len(recent_plans)} markdown file(s) in last 24h.",
        f"- Health: {health[0] if health else 'No blocking issue detected.'}",
        "- Suggested next: review this manual brief, then wrap it as `self-os-daily-brief` if useful.",
    ])
    return markdown, telegram_summary, out_path


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Generate a Self-OS daily operating brief")
    parser.add_argument("--kind", default="manual", choices=["manual", "morning", "evening"], help="Brief kind")
    parser.add_argument("--cron-snapshot", default=os.environ.get("SELF_OS_CRON_SNAPSHOT"), help="Optional path to cronjob(list) JSON")
    parser.add_argument("--print-telegram-summary", action="store_true", help="Print concise Telegram-ready summary after writing")
    args = parser.parse_args(argv)

    markdown, telegram_summary, out_path = build_brief(args.kind, args.cron_snapshot)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown)
    print(out_path)
    if args.print_telegram_summary:
        print("\n--- Telegram summary ---")
        print(telegram_summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
