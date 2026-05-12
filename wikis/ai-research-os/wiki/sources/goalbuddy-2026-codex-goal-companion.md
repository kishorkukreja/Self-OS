---
title: "Goal Buddy — Codex /goal Companion"
date_created: 2026-05-12
date_modified: 2026-05-12
summary: "Goal Buddy documents a local-first companion for Codex `/goal`: it prepares a goal charter, keeps `state.yaml` as the repo-local board, and captures notes/receipts as agents move through Scout, Judge, and Worker roles. The source matters be"
tags: [goalbuddy, codex, goal-command, kanban, coding-agents, local-state, agent-workflows, self-os]
type: source
status: final
---

# Goal Buddy — Codex /goal Companion

**Type:** resource  
**Date:** 2026-05-11  
**URL/Source:** https://goalbuddy.dev/  
**Raw file:** [[../raw/resources/goalbuddy-codex-goal-companion-2026-05-11.md]]  
**Concepts:** [[concepts/local-first-agent-orchestration]], [[concepts/agent-work-receipts]], [[concepts/kanban-agent-workflows]]  
**Entities:** [[entities/goal-buddy]], [[entities/codex]]  

## Summary

Goal Buddy documents a local-first companion for Codex `/goal`: it prepares a goal charter, keeps `state.yaml` as the repo-local board, and captures notes/receipts as agents move through Scout, Judge, and Worker roles. The source matters because it makes agent orchestration concrete at the file-system layer rather than treating a hosted task tracker as the source of truth. Its strongest Self-OS implication is that long-running coding agents need explicit state, handoff receipts, stop conditions, and visible board transitions before they need another SaaS integration. Optional GitHub, Linear, Slack, and project-board bridges are framed as mirrors, while repository files remain authoritative. This matches the Self-OS direction of durable Markdown/Git state, evidence before completion claims, and scoped implementation slices that can be resumed by another agent or by the user later. The source is useful primarily as a compiled signal rather than as a final answer: the raw capture remains the canonical place for exact wording, examples, figures, and links. In the wiki layer it should be read as evidence about recurring operating patterns, decision pressure, and implementation considerations that can be connected to adjacent source summaries without copying the raw text verbatim.

## Key contributions
- Shows how `goal.md`, `state.yaml`, and notes can structure long Codex runs.
- Separates mapping, slice selection, and implementation into Scout/Judge/Worker roles.
- Treats external trackers as mirrors rather than sources of truth.

**Tags:** goalbuddy, codex, goal-command, kanban, coding-agents, local-state, agent-workflows, self-os
