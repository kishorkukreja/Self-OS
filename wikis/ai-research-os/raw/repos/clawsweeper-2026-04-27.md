---
url: https://github.com/openclaw/clawsweeper
repo: openclaw/clawsweeper
saved: 2026-04-27
source: The Unwind AI newsletter
stars: 1.2k
license: MIT
language: JavaScript (100%)
status: processed
---
# ClawSweeper

**OpenClaw maintenance bot** for `openclaw/openclaw`.

> "ClawSweeper scans all issues and PRs and suggest what we can close, and why. It runs every PR / Issue once a week."

## Overview

- Maintains **one markdown report per open issue/PR**
- Publishes **one durable Codex automated review comment** when useful
- **Only closes items when the evidence is strong**

## Guardrails (Close Criteria)

ClawSweeper may propose closing **only** when an item is clearly one of:

- Implemented on current `main`
- Not reproducible on current `main`
- Better suited for ClawHub skill/plugin work than core
- Duplicate or superseded by a canonical issue/PR
- Concrete but not actionable in this source repo
- Incoherent enough that no action can be taken
- Stale issue older than **60 days** with too little data to verify

**Never auto-close:**
- Maintainer-authored items
- Issues with an open PR referencing them using closing syntax (`Fixes #123`) until that PR merges or closes
- Open issue/PR pairs from the same author (unless paired item is resolved or maintainer asks)

## Architecture

### Scheduler
- **Hot/new + recently active**: hourly (5-minute intake schedule for newest queue edge)
- **PRs and issues < 30 days**: daily after leaving hot window
- **Older inactive issues**: weekly
- **Apply lane**: wakes every 15 minutes; exits quickly when no unchanged high-confidence proposals exist

### Review Lane
- Planner assigns item numbers to shards
- Checks out `openclaw/openclaw` at `main`
- **Codex config**: `gpt-5.5`, high reasoning, fast service tier, **10-minute per-item timeout**
- Generates `items/<number>.md` with decision, evidence, suggested comment, runtime metadata, and GitHub snapshot hash
- High-confidence allowed closes marked as `proposed_close`
- Publishes single **marker-backed Codex review comment**; syncs missing immediately, refreshes stale weekly

### Apply Lane
- Updates the single durable review comment in place
- Closes **only unchanged high-confidence proposals**
- Reuses review comment on close (no duplicate close comment)
- Moves closed reports to `closed/<number>.md`; moves reopened archived reports back to `items/<number>.md` (stale)
- Commits checkpoints and dashboard heartbeats during long runs
- Deterministic write path: checks fresh GitHub snapshot, labels, maintainer-authorship, and unchanged item state immediately before mutation

### Safety Model
- Maintainer-authored items excluded from automated closes
- Protected labels block close proposals
- Open PRs with GitHub closing references block issue closes until resolved
- Open same-author issue/PR pairs block one-sided closes
- Codex runs **without GitHub write tokens**
- CI makes OpenClaw checkout **read-only** for reviews
- Reviews fail if Codex leaves tracked or untracked changes behind
- Snapshot changes block apply unless the only change is the bot’s own review comment

## Dashboard Snapshot (Apr 27, 2026)
- **Open issues**: 3,546
- **Open PRs**: 3,457
- **Total open items**: 7,003
- **Reviewed files**: 6,771
- **Unreviewed open items**: 232
- **Archived closed files**: 13,060
- **Closed by Codex apply** (historical): **10,217**

## Why It Matters

A production-grade example of an AI agent with **conservative, safety-first automation** for repo maintenance. Demonstrates tiered scheduling, review/apply separation, durable comments, and strong guardrails against over-eager closes. Useful reference for anyone building autonomous repo-maintenance or triage bots.
