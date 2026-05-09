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


def read_excerpt(path: Path, limit: int = 1800) -> str:
    try:
        return path.read_text(errors="replace")[:limit]
    except Exception:
        return ""


def extract_title(path: Path, text: str | None = None) -> str:
    text = text if text is not None else read_excerpt(path)
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def extract_tags(text: str) -> list[str]:
    match = re.search(r"(?im)^tags:\s*\[(.*?)\]", text)
    if not match:
        return []
    return [tag.strip().strip("'\"") for tag in match.group(1).split(",") if tag.strip()]


def theme_counts(paths: list[Path], limit: int = 8) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    stop = {
        "raw", "wiki", "source", "sources", "article", "repo", "video", "thread",
        "daily", "brief", "self", "os", "project", "projects", "notes", "system",
        "knowledge", "research", "markdown", "output", "outputs", "internal",
    }
    for path in paths:
        text = read_excerpt(path, 2500).lower()
        for tag in extract_tags(text):
            key = tag.lower().replace("_", "-")
            if key and key not in stop:
                counts[key] = counts.get(key, 0) + 3
        for token in re.findall(r"[a-z][a-z0-9-]{4,}", rel(path).lower() + "\n" + text[:1200]):
            token = token.strip("-")
            if token and token not in stop:
                counts[token] = counts.get(token, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def build_thinking_loop(recent_paths: list[Path], since: dt.datetime) -> tuple[list[str], str, str]:
    """Generate a lightweight feedback loop from recent captures.

    This intentionally stays deterministic and local-only: the scheduled Hermes
    agent can still add judgment in its Telegram response, while the saved wiki
    artifact always contains a durable connection/pattern/question block.
    """
    unique_recent: list[Path] = []
    seen: set[Path] = set()
    for path in recent_paths:
        if path not in seen and path.exists():
            unique_recent.append(path)
            seen.add(path)

    if not unique_recent:
        return (
            ["No fresh captures detected in the last 24 hours, so no new cross-note connections were generated."],
            "No dominant new capture pattern detected today.",
            "What should Self-OS deliberately capture or review next so the feedback loop has better signal tomorrow?",
        )

    recent_themes = theme_counts(unique_recent, limit=5)
    older_candidates: list[Path] = []
    since_ts = since.timestamp()
    for path in RAW_ROOT.rglob("*.md"):
        try:
            if path.stat().st_mtime < since_ts:
                older_candidates.append(path)
        except OSError:
            continue

    connections: list[str] = []
    for recent in unique_recent[:8]:
        recent_text = read_excerpt(recent, 2200)
        recent_title = extract_title(recent, recent_text)
        recent_tags = set(extract_tags(recent_text.lower()))
        recent_tokens = set(token for token, _ in theme_counts([recent], limit=10))
        terms = {t.lower() for t in recent_tags | recent_tokens if len(t) >= 5}
        best: tuple[int, Path] | None = None
        for older in older_candidates[:500]:
            if older == recent:
                continue
            older_blob = (rel(older) + "\n" + read_excerpt(older, 1800)).lower()
            score = sum(1 for term in terms if term in older_blob)
            if score and (best is None or score > best[0]):
                best = (score, older)
        if best:
            older_title = extract_title(best[1])
            shared = ", ".join(list(terms)[:3]) or "shared theme"
            connections.append(
                f"`{rel(recent)}` ({recent_title}) connects to `{rel(best[1])}` ({older_title}) via {shared}."
            )
        if len(connections) >= 3:
            break

    if not connections:
        connections.append("Recent captures did not strongly match older notes by local keyword scan; this is a cue for the next wiki compile/synthesis pass to add better concept links.")

    if recent_themes:
        pattern_terms = ", ".join(term for term, _ in recent_themes[:4])
        pattern = f"Recent captures cluster around: {pattern_terms}."
        question = f"Given today’s {recent_themes[0][0]} signal, what should become an operational workflow rather than another passive note?"
    else:
        pattern = "Recent captures are too sparse or heterogeneous to infer a strong pattern."
        question = "Which recurring Self-OS decision should the next capture/synthesis loop make easier?"
    return connections, pattern, question


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
    thinking_connections, thinking_pattern, thinking_question = build_thinking_loop(recent_raw + recent_plans, since)
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
    safe_actions.append("Use the Thinking Loop below to promote one useful insight into either a wiki synthesis, a skill patch, or a Kanban/taskOS action.")

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
- Top next move: use the Thinking Loop to turn one recent capture into a connection, synthesis, or safe next action.

## Changed Since Last Brief

### Recent commits, last 24h

{code_or_none(log, "No commits in the last 24 hours.")}

### Recent raw/wiki/doc markdown files, last 24h

{bullet([f"`{rel(path)}`" for path in recent_raw + recent_plans], "No recent markdown files detected.")}

## Thinking Loop

### Connections

{bullet(thinking_connections, "No cross-note connections generated.")}

### Pattern

- {thinking_pattern}

### Question

- {thinking_question}

## Needs Kishor Review

{bullet(review_items, "No review items detected by local collector.")}

## Safe Agent Actions

{bullet(safe_actions)}

## Decisions Needed

- Which Thinking Loop item should become an action: passive wiki synthesis, skill patch, Kanban/taskOS task, or decision for Kishor?
- Are any recent captures important enough to compile into canonical wiki concepts before the normal wiki-compile cadence?
- Should any repeated operational failure be promoted into a skill patch today?

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
Use this daily brief's Thinking Loop to choose one action: create a wiki synthesis, patch/create a Hermes skill, create a Kanban/taskOS task, or ask Kishor for a decision.
```
"""

    telegram_summary = "\n".join([
        f"Self-OS {kind.title()} Brief — {date_slug}",
        f"- State: {'dirty working tree' if status.strip() else 'repo clean at collection time'}; {len(prs)} open PR(s); {len(pending)} pending request candidate(s).",
        f"- Recent files detected: {len(recent_raw) + len(recent_plans)} markdown file(s) in last 24h.",
        f"- Thinking Loop: {thinking_pattern}",
        f"- Question: {thinking_question}",
        f"- Health: {health[0] if health else 'No blocking issue detected.'}",
        "- Suggested next: choose one loop item to promote into wiki synthesis, skill patch, Kanban/taskOS task, or decision.",
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
