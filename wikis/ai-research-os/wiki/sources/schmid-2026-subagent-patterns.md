---
title: "Phil Schmid — Four Subagent Patterns in 2026"
date_created: 2026-05-07
date_modified: 2026-05-07
summary: "Article classifying subagent orchestration by lifecycle control: inline tools, fan-out, persistent pools, and teams that communicate directly."
tags: [subagents, multi-agent-systems, agent-orchestration]
type: source
status: final
---

# Phil Schmid — Four Subagent Patterns in 2026

**Type:** article
**Date:** 2026-05-06
**URL/Source:** https://www.philschmid.de/subagent-patterns-2026
**Raw file:** [[../raw/articles/2026-05-06-subagent-patterns-2026.md]]
**Concepts:** [[concepts/subagent-orchestration]], [[concepts/persistent-agent-pools]], [[concepts/multi-agent-teams]]
**Entities:** [[entities/phil-schmid]]

## Summary

Phil Schmid’s article gives a practical taxonomy for how main agents manage other agents. The simplest pattern is an inline tool call, where the main agent invokes a subagent like `read_file` or `run_command` and receives one result. Fan-out separates spawning from collection: the main agent launches multiple independent agents, does other work, and later waits for batched results. Persistent agent pools add stateful workers that can receive follow-up messages, retain context, and be cancelled. The most complex pattern is a team where agents message one another directly and the main agent mostly sets roles, kicks off the planner, and waits for a final report.

The article is useful because it organizes subagents by lifecycle and coordination burden rather than by branding. Inline and fan-out patterns fit self-contained research, code review, file analysis, and test generation. Persistent pools make sense for multi-step workflows that need follow-up or specialist state, but require the supervising agent to track messages, ownership, progress, and shutdown. Teams can keep the main context clean during large tasks, but they introduce risks around deadlocks, conflicting edits, missed completion reports, and routing mistakes. For Hermes and Self-OS, this taxonomy maps directly to decisions about when to use simple `delegate_task`, when to run AFK/Night Shift workers, and where persistent role agents need stronger QA controls.

## Key takeaways

- Subagent architecture should be chosen by lifecycle, follow-up needs, and coordination complexity.
- Fan-out only helps when the main agent can interleave work before collecting results.
- Persistent pools and autonomous teams need stronger state tracking, conflict control, and shutdown rules than inline delegation.

## Compilation notes

Compiled from `raw/articles/2026-05-06-subagent-patterns-2026.md` during the 2026-05-07 wiki compile. The raw capture remains the canonical source for exact excerpts, links, figures, and code.
