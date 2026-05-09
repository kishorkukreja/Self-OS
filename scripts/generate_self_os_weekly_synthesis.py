#!/usr/bin/env python3
"""Generate the weekly Self-OS feedback-loop synthesis.

The weekly artifact is saved into the Git-backed Self-OS wiki. It turns a week of
briefs, captures, commits, branches, and optional Hermes cron metadata into a
small operating review: what changed, what patterns are forming, what should be
automated, and what needs Kishor's decision.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Iterable

REPO = Path(__file__).resolve().parents[1]
RAW_ROOT = REPO / "wikis"
DAILY_ROOT = REPO / "wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/daily"
DEFAULT_OUTPUT_ROOT = REPO / "wikis/coding-projects-os/raw/projects/self-os-operating-loop/ops/weekly"
CONTRACT_PATH = REPO / "docs/self-os-operating-contract.md"
GITHUB_PULLS_URL = "https://api.github.com/repos/kishorkukreja/Self-OS/pulls?state=open&per_page=50"


def run(cmd: list[str], cwd: Path = REPO, timeout: int = 45) -> tuple[int, str]:
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
    except Exception as exc:
        return 1, f"ERROR running {' '.join(cmd)}: {exc}"


def utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def week_slug(now: dt.datetime) -> str:
    year, week, _ = now.isocalendar()
    return f"{year}-W{week:02d}"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def bullet(items: Iterable[str], empty: str = "None found.") -> str:
    clean = [item for item in items if item]
    if not clean:
        return f"- {empty}"
    return "\n".join(f"- {item}" for item in clean)


def code_or_none(text: str, empty: str = "None.") -> str:
    if not text.strip():
        return empty
    return "```text\n" + text.strip() + "\n```"


def read_excerpt(path: Path, limit: int = 2400) -> str:
    try:
        return path.read_text(errors="replace")[:limit]
    except Exception:
        return ""


def recent_files(root: Path, since: dt.datetime, limit: int = 80) -> list[Path]:
    if not root.exists():
        return []
    since_ts = since.timestamp()
    rows: list[tuple[float, Path]] = []
    for path in root.rglob("*.md"):
        try:
            mtime = path.stat().st_mtime
        except OSError:
            continue
        if mtime >= since_ts:
            rows.append((mtime, path))
    rows.sort(reverse=True, key=lambda row: row[0])
    return [path for _, path in rows[:limit]]


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


def theme_counts(paths: list[Path], limit: int = 12) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    stop = {
        "raw", "wiki", "source", "sources", "daily", "brief", "weekly", "review",
        "self", "project", "projects", "status", "notes", "system", "markdown",
        "research", "internal", "article", "thread", "video", "repo", "output", "outputs",
        "created", "title", "summary", "date", "tags", "type", "client", "false", "true",
    }
    for path in paths:
        text = read_excerpt(path, 3000).lower()
        for tag in extract_tags(text):
            key = tag.lower().replace("_", "-")
            if key and key not in stop:
                counts[key] = counts.get(key, 0) + 4
        for token in re.findall(r"[a-z][a-z0-9-]{4,}", rel(path).lower() + "\n" + text[:1600]):
            token = token.strip("-")
            if token and token not in stop:
                counts[token] = counts.get(token, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def github_open_prs() -> tuple[list[str], str | None]:
    req = urllib.request.Request(
        GITHUB_PULLS_URL,
        headers={"Accept": "application/vnd.github+json", "User-Agent": "self-os-weekly-synthesis"},
    )
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return [], f"GitHub PR lookup failed: HTTP {exc.code}"
    except Exception as exc:
        return [], f"GitHub PR lookup failed: {exc}"

    rows = []
    for pr in data[:20]:
        number = pr.get("number")
        title = pr.get("title", "Untitled")
        branch = pr.get("head", {}).get("ref", "unknown-branch")
        url = pr.get("html_url", "")
        rows.append(f"#{number} — {title} (`{branch}`) {url}".strip())
    return rows, None


def load_cron_snapshot(path: str | None) -> tuple[list[str], list[str], list[str]]:
    if not path:
        return [], [], ["Cron snapshot not injected."]
    p = Path(path)
    if not p.exists():
        return [], [], [f"Cron snapshot path not found: {p}"]
    try:
        data = json.loads(p.read_text())
    except Exception as exc:
        return [], [], [f"Cron snapshot unreadable: {exc}"]

    jobs = data.get("jobs", []) if isinstance(data, dict) else []
    rows: list[str] = []
    failures: list[str] = []
    successes: list[str] = []
    for job in jobs:
        name = job.get("name", job.get("job_id", "unnamed"))
        status = job.get("last_status") or "never-run"
        enabled = job.get("enabled")
        next_run = job.get("next_run_at") or "n/a"
        row = f"{name}: last `{status}`, enabled `{enabled}`, next `{next_run}`"
        rows.append(row)
        if status == "ok":
            successes.append(row)
        elif status != "never-run":
            failures.append(row)
        if job.get("last_delivery_error"):
            failures.append(f"{name}: delivery error `{job.get('last_delivery_error')}`")
    return rows, successes, failures


def skills_changed(since: dt.datetime) -> list[str]:
    # The skills live outside the repo, but durable skill changes should often be
    # visible as repo docs/notes or recent agent activity. This local heuristic
    # catches explicit mentions in weekly sources without reading Hermes internals.
    paths = recent_files(REPO, since, limit=150)
    rows: list[str] = []
    for path in paths:
        text = read_excerpt(path, 2000).lower()
        if "skill" in text or "skills" in text:
            rows.append(f"`{rel(path)}` mentions skill/workflow changes")
        if len(rows) >= 8:
            break
    return rows


def build_weekly(cron_snapshot: str | None) -> tuple[str, str, Path]:
    now = utc_now()
    since = now - dt.timedelta(days=7)
    slug = week_slug(now)
    out_path = DEFAULT_OUTPUT_ROOT / f"{slug}-review.md"

    branch_rc, branch = run(["git", "branch", "--show-current"])
    status_rc, status = run(["git", "status", "--short"])
    log_rc, log = run(["git", "log", "--oneline", "--since=7 days ago", "--", "."])
    remote_rc, remote_branches = run(["git", "branch", "-r", "--list", "origin/wiki-*"])
    merged_rc, merged = run(["git", "log", "--oneline", "--merges", "--since=7 days ago", "--", "."])

    recent_raw = recent_files(RAW_ROOT, since, limit=80)
    recent_daily = recent_files(DAILY_ROOT, since, limit=14)
    prs, pr_error = github_open_prs()
    cron_rows, cron_successes, cron_failures = load_cron_snapshot(cron_snapshot)
    themes = theme_counts(recent_raw + recent_daily, limit=10)
    skill_rows = skills_changed(since)

    major_changes = []
    if log.strip():
        major_changes.extend(log.splitlines()[:12])
    if recent_raw:
        major_changes.extend(f"Recent capture: `{rel(path)}` — {extract_title(path)}" for path in recent_raw[:10])
    if not major_changes:
        major_changes.append("No major repo commits or raw captures detected in the last 7 days.")

    repeated_themes = [f"{term} ({count})" for term, count in themes]
    emerging_thesis = (
        f"The week’s material clusters around {', '.join(term for term, _ in themes[:4])}; convert the strongest recurring theme into an operational loop rather than another passive note."
        if themes
        else "No strong weekly theme detected by local scan; the next week should improve capture consistency."
    )

    automation_candidates = []
    if themes:
        automation_candidates.append(f"Promote `{themes[0][0]}` into either a wiki synthesis page, skill patch, idea inbox note, taskOS folder, or Kanban task depending on maturity.")
    if cron_failures:
        automation_candidates.append("Fix failing cron jobs before adding new automations.")
    if len(recent_raw) > 10:
        automation_candidates.append("Run or inspect wiki compile output so raw captures do not accumulate without interpretation.")
    automation_candidates.append("Keep the daily Thinking Loop as the control surface; only add dashboards after repeated weekly synthesis proves which signals matter.")

    decisions = [
        "Which weekly theme deserves implementation next rather than further capture?",
        "Which automation should be killed, simplified, or merged because it is not producing useful decisions?",
    ]
    if prs:
        decisions.append("Which open Self-OS PRs should be reviewed, merged, or closed?")
    if cron_failures:
        decisions.append("Should failed cron jobs be paused until fixed, or kept running while debugging?")

    priorities = []
    if themes:
        priorities.append(f"Turn `{themes[0][0]}` into one concrete next action with an owner/path.")
    priorities.append("Continue saving daily briefs and this weekly synthesis back to the Self-OS wiki as the durable record.")
    priorities.append("Route implementation ideas into the idea inbox first; promote to taskOS once shaped, then create Kanban tasks only for execution-ready work.")

    health = []
    if branch_rc != 0 or branch != "master":
        health.append(f"Repo branch is `{branch or 'unknown'}`; expected `master` for direct operating briefs.")
    if status.strip():
        health.append("Working tree has uncommitted changes.")
    if pr_error:
        health.append(pr_error)
    health.extend(cron_failures)
    if not health:
        health.append("No blocking weekly health issue detected by local collector.")

    markdown = f"""---
title: Self-OS Weekly Synthesis — {slug}
type: self-os-weekly-synthesis
status: raw
created_at: {now.isoformat()}
week: {slug}
source: scripts/generate_self_os_weekly_synthesis.py
---

# Self-OS Weekly Synthesis — {slug}

## TL;DR

- {emerging_thesis}
- Health: {health[0] if health else 'No blocking issue detected.'}
- Recommended next move: choose one weekly theme and route it into wiki synthesis, skill patch, idea inbox, taskOS, Kanban, or a decision prompt.

## Major Changes This Week

{bullet(major_changes, "No major changes detected.")}

### Recent commits, last 7 days

{code_or_none(log, "No commits in the last 7 days.")}

### Merged PRs / merge commits, last 7 days

{code_or_none(merged, "No merge commits detected in the last 7 days.")}

## Repeated Captures / Themes

{bullet(repeated_themes, "No repeated themes detected by local scan.")}

## Feedback Loop Synthesis

- Emerging thesis: {emerging_thesis}
- Contradictions to inspect: look for places where recent captures add information but did not change any workflow, skill, or decision.
- Knowledge gaps: identify missing source classes around the top theme before treating it as a settled thesis.
- One action: promote the top theme into one operational artifact this week.

## Open PRs and Stale Branches

### Open PRs

{bullet(prs, "No open GitHub PRs returned by public API.")}

### Remote wiki branches

{code_or_none(remote_branches, "No remote wiki branches listed.")}

## Cron Reliability

{bullet(cron_rows, "Cron snapshot not injected. Hermes cron wrapper should pass one for scheduled runs.")}

## Skills Patched or Needing Patches

{bullet(skill_rows, "No explicit skill/workflow change mentions found in this week's repo scan.")}

## Workflows That Should Be Automated Next

{bullet(automation_candidates)}

## Decisions Kishor Should Make

{bullet(decisions)}

## Proposed Next Week Operating Priorities

{bullet(priorities)}

## Health / Failures

### Git state

- Branch: `{branch or 'unknown'}`
- Working tree: {'dirty' if status.strip() else 'clean'}

{code_or_none(status, "Working tree clean.")}

### Detected health notes

{bullet(health)}

## Operating Contract Used

- `{rel(CONTRACT_PATH)}` {'exists' if CONTRACT_PATH.exists() else 'missing'}

## Next Suggested Prompt

```text
Use this weekly synthesis to pick one operational improvement: wiki synthesis, skill patch, idea inbox note, taskOS implementation candidate, Kanban execution task, or decision prompt for Kishor. Do not add a dashboard until the brief loop repeatedly proves the signal.
```
"""

    telegram_summary = "\n".join([
        f"Self-OS Weekly Synthesis — {slug}",
        f"- Theme: {emerging_thesis}",
        f"- Activity: {len(log.splitlines()) if log.strip() else 0} commit(s), {len(recent_raw)} recent raw/wiki file(s), {len(prs)} open PR(s).",
        f"- Cron: {len(cron_successes)} ok / {len(cron_failures)} issue(s) from injected snapshot.",
        f"- Health: {health[0] if health else 'No blocking issue detected.'}",
        "- Suggested next: route the top theme into wiki synthesis, skill patch, idea inbox, taskOS, Kanban, or decision.",
    ])
    return markdown, telegram_summary, out_path


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Generate a Self-OS weekly feedback-loop synthesis")
    parser.add_argument("--cron-snapshot", default=os.environ.get("SELF_OS_CRON_SNAPSHOT"), help="Optional path to cronjob(list) JSON")
    parser.add_argument("--print-telegram-summary", action="store_true", help="Print concise Telegram-ready summary after writing")
    args = parser.parse_args(argv)

    markdown, telegram_summary, out_path = build_weekly(args.cron_snapshot)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(markdown)
    print(out_path)
    if args.print_telegram_summary:
        print("\n--- Telegram summary ---")
        print(telegram_summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
