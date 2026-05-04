---
title: Self Os Operating Loop
date_created: 2026-05-03
date_modified: '2026-05-04'
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
| 2026-05-03-morning | 2026-05-03 | Self-OS Morning Brief — 2026-05-03 TL;DR - repo is clean at collection time; 1 open PR s ; no injected cron failures. - Top next move: inspect this first manual |
| 2026-05-02-manual | 2026-05-02 | Manual operating brief captured repo state, recent commits/raw changes, and the next move for shaping the Self-OS brief workflow. |

## Open questions
- Whether the manual brief format is useful enough to wrap into a dedicated Hermes skill.
- Which signals should be promoted from raw operational context into daily action routing.

## Links
- Raw brief: [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-02-manual.md]]
