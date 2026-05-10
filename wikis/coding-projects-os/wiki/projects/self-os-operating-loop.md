---
title: Self Os Operating Loop
date_created: '2026-05-03'
date_modified: 2026-05-10
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
tags: [wiki, maintenance]
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

## Compile update — 2026-05-10: Claude Swarm Multi-Agent Framework

- Raw file: [[../raw/ideas/2026-05-09-claude-swarm-multi-agent-framework.md]]
- Summary: Claude Swarm Multi Agent Framework One line idea Create or adopt a framework for spinning up multiple Claude agents in a swarm style setup, then evaluate how it applies to Self OS / taskOS / Night Shift use cases. Why it might matter This could become a practical orchestration layer for running specialized Claude agents in parallel rather than treating Claude Code as a single autonomous worker. It fits the existing Self OS direction: rigorous multi agent workflows, day/night shifts, separate planner/implementer/reviewer roles, and agent swarms that can attack implementation, research, QA, and synthesis tasks concurrently.

## Compile update — 2026-05-10: Experiment With an Agno Agent Platform Agent

- Raw file: [[../raw/ideas/2026-05-09-experiment-with-agno-agent-platform-agent.md]]
- Summary: Experiment With an Agno Agent Platform Agent One line idea Run a small experiment using the Agno / AgentOS agent platform setup from Ashpreet Bedi’s “How to Build an Agent Platform” blog, then evaluate whether its runtime, traces, evals, scheduler, interfaces, and Claude Code improvement loop are useful for Self OS. Why it might matter The Agno AgentOS template looks like a concrete way to test the “agent platform” architecture rather than only theorizing about it. Self OS already has pieces of this shape — Telegram interface, cron jobs, Git backed memory, Hermes skills, taskOS, Kanban, and Claude/Codex workflows — but it does not yet have a unified app style agent runtime with sessions, traces, eval history, scheduler, and a UI around agents.

## Compile update — 2026-05-10: Idea Inbox Routing Flow

- Raw file: [[../raw/ideas/2026-05-09-idea-inbox-routing-flow.md]]
- Summary: Idea Inbox Routing Flow One line idea Add a lightweight idea inbox to the Self OS wiki so random ideas and daily/weekly brief insights can be captured first, shaped over time, then promoted to taskOS and Hermes Kanban only when implementation ready. Why it might matter The daily and weekly Self OS briefs will surface patterns, questions, and possible actions. Not all of those should immediately become tasks.

## Compile update — 2026-05-10: Coding Projects OS — Idea Inbox

- Raw file: [[../raw/ideas/README.md]]
- Summary: Coding Projects OS — Idea Inbox This folder is the lightweight capture point for raw implementation shaped ideas that are not ready for taskOS or Kanban yet. Use this for: Random project/product/automation ideas captured on the go. Ideas surfaced by the daily Self OS brief or weekly synthesis.

## Compile update — 2026-05-10: Idea Capture Template

- Raw file: [[../raw/ideas/templates/idea.md]]
- Summary: Idea Capture Template Copy this file to: Required frontmatter Body template

## Compile update — 2026-05-10: Self-OS Evening Brief — 2026-05-09

- Raw file: [[../raw/projects/self-os-operating-loop/ops/daily/2026-05-09-evening.md]]
- Summary: Self OS Evening Brief — 2026 05 09 TL;DR repo is clean at collection time; 2 open PR(s); no injected cron failures. Top next move: use the Thinking Loop to turn one recent capture into a connection, synthesis, or safe next action. Changed Since Last Brief Recent commits, last 24h Recent raw/wiki/doc markdown files, last 24h wikis/supply chain os/raw/newsletters/supply chain signals/2026 W19/sources/2026 05 09 sources.md wikis/supply chain os/raw/newsletters/supply chain signals/2026 W19/daily/2026 05 09 daily research.md wikis/ai research os/raw/repos/github trending weekly 2026 05 09.md wikis/ai research os/raw/x blogs/2026 05 09 x blogs digest.md wikis/supply chain os/wiki/sources/supply chain signals 2026 w19 overview.md wikis/supply chain os/wiki/log.md wikis/supply chain os/wiki/sources/supply chain signals 2026 05 04 sources.md wikis/supply chain os/wiki/sources/supply chain signals 2026 05 04 daily research.md wikis/supply chain os/wiki/entities/reuters.md wikis/supply chain os/wiki/entities/new york fed.md wikis/supply chain os/wiki/entities/supply chain signals.md wikis/supply chain os/wiki/entities/flexport.md wikis/supply chain os/wiki/entities/ism.md wikis/supply chain os/wiki/concepts/wafer to rack.md wikis/supply chain os/wiki/concepts/tariffs.md wikis/supply chain os/wiki/concepts/supply chain signals.md wikis/supply chain os/wiki/concepts/procurement.md wikis/supply chain os/wiki/concepts/supply chain pressure.md wikis/supply chain os/wiki/concepts/manufacturing.md wikis/supply chain os/wiki/concepts/inventory.md wikis/supply chain os/wiki/concepts/logistics.md wikis/supply chain os/wiki/concepts/demand pull forward.md wikis/supply chain os/wiki/concepts/manufacturing input cost inflation.md wikis/personal os/wiki/log.md wikis/personal os/wiki/actions/lint report 2026 05 02.md wikis/coding projects os/wiki/log.md wikis/coding projects os/wiki/patterns/daily operating brief.md wikis/coding projects os/wiki/projects/projectsos.md wikis/coding projects os/wiki/projects/self os operating loop.md wikis/ai research os/wiki/sources/text to cad 2026 05 04.md docs/self os operating contract.md Thinking Loop Connections wikis/supply chain os/raw/newsletters/supply chain signals/2026 W19/sources/2026 05 09 sources.md (Supply Chain Signals Sources — 2026 05 09) connects to wikis/supply chain os/raw/newsletters/supply chain signals/2026 W19/sources/2026 05 06 sources.md (Supply Chain Signals Sources — 2026 05 06) via supply, spglobal, chain.

## Compile update — 2026-05-10: Self-OS Weekly Synthesis — 2026-W19

- Raw file: [[../raw/projects/self-os-operating-loop/ops/weekly/2026-W19-review.md]]
- Summary: Self OS Weekly Synthesis — 2026 W19 TL;DR The week’s material clusters around wikis, concepts, chain, supply; convert the strongest recurring theme into an operational loop rather than another passive note. Health: No blocking weekly health issue detected by local collector. Recommended next move: choose one weekly theme and route it into wiki synthesis, skill patch, Kanban/taskOS, or a decision prompt.
