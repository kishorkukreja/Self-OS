---
title: "How to Ship with AFK Agents — Day Shift vs Night Shift"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Matt Pocock's day-shift/night-shift model: humans plan and QA during the day; AFK agents implement and review in parallel sandboxes overnight."
tags: [afk-agents, day-shift, night-shift, agent-workflow, sandcastle, planning, review]
type: source
status: final
---

# How to Ship with AFK Agents — Day Shift vs Night Shift

**Type:** article
**Date:** 2026-04-26
**Source:** X/Twitter post by Matt Pocock
**Raw file:** [[../../raw/articles/2026-04-26-mattpocock-afk-agents-day-shift-night-shift.md]]

**Summary:** Matt Pocock describes a proven workflow for shipping software with AFK agents, separating human and machine work into day shift and night shift. The **day shift** handles planning (Grill Me alignment, PRD creation, issue slicing) and QA (branch review, follow-up issue creation, manual PR review). The **night shift** runs a planner agent that identifies unblocked tickets and kicks off multiple sandboxed implementation agents via **Sandcastle**, followed by automated reviewer agents checking alignment to the PRD and code quality. Commits land on branches for human review. Pocock identifies four failure modes for AFK agents: bad original plans, unknown unknowns, AI errors in both review and implementation, and bad codebases with insufficient feedback loops. The night shift's sole purpose is automating review without latency concerns; planning too far ahead without working code is futile. Tools referenced: Sandcastle (sandboxing), Evalite (evaluation), and Software Factory.

**Key contributions:**
- Day shift / night shift separation: planning and QA are human; implementation is automated
- Planner agent orchestrates parallel implementation and review agents
- Automated review checking PRD alignment and code quality before human review
- Four-cause taxonomy for AFK agent failure modes
- Parallel day/night operation: QA feeds back into planning while new implementation runs

**Tags:** afk-agents, day-shift, night-shift, agent-workflow, sandcastle, planning, review
