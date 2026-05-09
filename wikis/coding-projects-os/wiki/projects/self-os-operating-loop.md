---
title: Self Os Operating Loop
date_created: '2026-05-03'
date_modified: 2026-05-09
summary: Project memory for the Self-OS operating loop and daily brief workflow.
tags:
- self-os
- operating-loop
- automation
type: project
status: active
project_status: active
tech_stack:
- python
- github-actions
- hermes
---

# Self Os Operating Loop
_Status: active_
_Last session: 2026-05-03_

## What it is

Self-OS operating loop is the automation and workflow layer that turns repository activity, wiki maintenance, cron health, and raw captures into daily operational briefs and next-action guidance.

## Architecture

The current loop is repository-native: raw operational captures are saved under `raw/projects/`, wiki pages compile the durable project memory, and scripts such as `scripts/generate_self_os_brief.py` produce daily briefs from Git, cron, and wiki signals.

## Sessions
| Session ID | Date | What happened |
|------------|------|----------------|
| 2026-05-05-morning | 2026-05-05 | Manual operating brief captured repo state, recent commits/raw changes, and the next move for shaping the Self-OS brief workflow. |
| 2026-05-03-morning | 2026-05-03 | Self-OS Morning Brief — 2026-05-03 TL;DR - repo is clean at collection time; 1 open PR s ; no injected cron failures. - Top next move: inspect this first manual |
| 2026-05-02-manual | 2026-05-02 | Manual operating brief captured repo state, recent commits/raw changes, and the next move for shaping the Self-OS brief workflow. |

## Open questions
- Whether the manual brief format is useful enough to wrap into a dedicated Hermes skill.
- Which signals should be promoted from raw operational context into daily action routing.

## Links
- Raw brief: [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-02-manual.md]]

## Session / operating brief — 2026-05-04 morning

**Source:** [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-04-morning.md]]

**What happened:** The first Self-OS morning brief captured repository state, open PR count, recent commits, branch/worktree health, cron status, and suggested next operating moves. It identified that the repo was clean at collection time, one PR was open, no injected cron failures were present, and the immediate next move was to inspect whether the manual brief format was useful enough to wrap in a Hermes skill.

**Decisions / implications:** This raw operating brief supports the Self-OS operating loop as a recurring project artifact: briefs should summarize system state, surface failures, and propose the next action without becoming a substitute for the canonical raw logs.

**Remaining work:** Decide whether the brief shape should remain a script-only output, become a Hermes skill, or feed a daily project dashboard.

## 2026-05-06 morning brief ingest

The 2026-05-06 morning brief reported a clean repository at collection time, one open wiki-compile PR, no injected cron failures, and a recommended next move to inspect the manual brief before turning the shape into a Hermes skill. It also surfaced raw backlog counts across AI, coding-projects, and supply-chain wikis and pointed to the Self-OS operating contract as the source for the brief generator.

**Raw source:** [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-06-morning.md]]


## Session: 2026-05-07 Morning Brief

**Source:** [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-07-morning.md]]

The first manual Self-OS morning brief reported a clean repository, one open wiki-compile PR, recent raw/wiki changes, and a backlog signal across AI, supply-chain, and coding-project wikis. It recommended reviewing the brief shape before wrapping it in a Hermes skill and surfaced the decision of whether to schedule daily delivery or keep the script manual for one more iteration. The run also established that the brief should include cron snapshots later rather than relying only on local git state.

**Follow-ups:**
- Decide whether the brief format should become a `self-os-daily-brief` Hermes skill.
- Add Hermes cron snapshots to the wrapper before scheduling automated delivery.
- Keep backlog counts coarse unless the compile scanner is reused directly.

_Last updated: 2026-05-09_

## Session: 2026-05-08 Morning Brief

**Source:** [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-08-morning.md]]

The 2026-05-08 morning brief reported a clean repository at collection time, one open wiki-compile PR, recent raw/wiki changes across AI, supply-chain, coding-project, and personal wikis, and no injected cron failures. It recommended inspecting the first manual brief and deciding whether the format should become a `self-os-daily-brief` Hermes skill before scheduling delivery.

**Follow-ups:**
- Decide whether the brief shape is useful enough to turn into a Hermes skill.
- Add Hermes cron snapshots through the skill wrapper rather than keeping the collector local-only.
- Keep the raw backlog signal coarse unless the compile scanner is reused directly.
