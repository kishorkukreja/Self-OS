---
title: "Claude Swarm Multi-Agent Framework"
date: 2026-05-09
type: idea
status: seed
domain: coding-projects-os
source: telegram
origin_ref: "Voice note from Kishor on 2026-05-09: framework for spinning multi-agents for Claude in a swarm-based setup"
tags: [idea, self-os, claude-code, multi-agent, swarm, agent-orchestration, night-shift]
taskos_path: null
kanban_tasks: []
---

# Claude Swarm Multi-Agent Framework

## One-line idea

Create or adopt a framework for spinning up multiple Claude agents in a swarm-style setup, then evaluate how it applies to Self-OS / taskOS / Night Shift use cases.

## Why it might matter

This could become a practical orchestration layer for running specialized Claude agents in parallel rather than treating Claude Code as a single autonomous worker. It fits the existing Self-OS direction: rigorous multi-agent workflows, day/night shifts, separate planner/implementer/reviewer roles, and agent swarms that can attack implementation, research, QA, and synthesis tasks concurrently.

## Current shape

- What we know:
  - Kishor thinks a Claude swarm-based multi-agent framework is a good idea.
  - The target is a reusable flow/framework for spinning multiple Claude agents.
  - The next step is to capture the idea and later explore use cases.
- What is fuzzy:
  - Whether this should use Claude Code native subagents, parallel Claude Code worktrees, Hermes `delegate_task`, tmux-managed Claude sessions, or an external orchestration framework.
  - Whether this is for coding only, research only, Self-OS operating loops, or a general orchestration primitive.
  - What “swarm” means operationally: peer agents, manager-worker, debate/review loop, blackboard architecture, or task queue fan-out.
- What triggered it:
  - Telegram voice note: “one of the framework for spinning multi-agents for Claude in a swarm-based setup… very good idea… set it up or do something about it… see how it can apply to some of our use cases.”

## Links / evidence

- Related wiki notes:
  - `coding-projects-os` idea inbox for implementation-shaped concepts.
  - Prior captures around parallel Claude Code, AFK agents, day/night shift workflows, and multi-agent review layers.
- Related daily/weekly briefs:
  - Self-OS operating loop and Night Shift briefs may be a future consumer of this framework.
- Related external sources:
  - Claude Code multi-agent / subagent patterns.
  - Parallel Claude Code + git worktree workflows.
  - OpenAI Symphony / Codex orchestration patterns.
  - AgentField / agent-control-plane style architectures.

## Possible implementation shape

- Likely repo/system:
  - `/data/Self-OS` for operating-loop documentation and durable idea capture.
  - `/data/taskOS` if promoted into a buildable backlog item.
  - Potentially a standalone “agent swarm harness” project if it becomes reusable infrastructure.
- Likely files/services:
  - A swarm orchestration spec: roles, routing, lifecycle, safety, and review gates.
  - A small CLI/script to launch N Claude agents against taskOS tasks or project worktrees.
  - A results aggregator that summarizes each agent’s output and pushes follow-up review tasks.
  - Integration hooks for Hermes Kanban and Self-OS daily/night-shift briefs.
- Dependencies:
  - Claude Code CLI / subagents / worktrees.
  - Git worktree isolation and PR-based review.
  - Hermes `delegate_task`, cron, and/or taskOS as orchestration substrate.
- Risks / objections:
  - Swarms can multiply low-quality output unless constrained by tight task specs and review gates.
  - Coordination overhead may exceed value if the setup is too heavy.
  - Parallel agents need strong isolation to avoid clobbering files or generating conflicting changes.
  - Cost/token use can balloon without budgets and max-turn limits.

## Candidate use cases

- Night Shift implementation: planner creates task slices; multiple Claude agents implement independent vertical slices in isolated worktrees; reviewer agents inspect outputs before Kishor sees PRs.
- Wiki/research synthesis: agents split source discovery, extraction, evidence checking, and synthesis.
- Code review swarm: separate agents review for correctness, security, performance, tests, and product alignment.
- Self-OS operations: agents inspect cron health, wiki freshness, PRs, and taskOS backlog, then produce a routed operating brief.
- Experimentation: run multiple approaches to the same task and compare using an evaluator/reviewer layer.

## Promotion checklist

Ready for taskOS when:

- [ ] Desired outcome is clear: adopt existing framework vs build a small Self-OS-specific harness.
- [ ] Initial use case is chosen: Night Shift coding, research/wiki, review swarm, or operating-loop brief.
- [ ] Constraints are known enough: Claude Code vs Hermes-native, worktree isolation, cost controls, permissions.
- [ ] Acceptance criteria can be written.
- [ ] It is worth turning into a durable task/spec.

Ready for Kanban when:

- [ ] taskOS folder exists.
- [ ] Work can be assigned to a profile.
- [ ] Next action is concrete and testable.

## Next question

What is the first concrete use case for the swarm: Night Shift coding, multi-agent code review, wiki/research synthesis, or Self-OS operating-loop intelligence?
