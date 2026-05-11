---
source: https://goalbuddy.dev/
date: 2026-05-11
type: resource
tags: [goalbuddy, codex, goal-command, kanban, coding-agents, local-state, agent-workflows, self-os]
---

# Goal Buddy — open source Codex /goal companion

## Summary
Goal Buddy is an open-source companion for Codex `/goal`. It prepares a `goal.md` charter for the `/goal` command, keeps `state.yaml` as local truth, and can render a live board so Codex work becomes visible as Scout, Judge, and Worker tasks populate. It also exposes optional extensions for GitHub PR handoffs, GitHub Projects, codebase onboarding maps, CI triage, Linear handoffs, and Slack standup digests.

## Key points
- Install with `npx goalbuddy`; update with `npx goalbuddy update`.
- The starter flow is `npx goalbuddy`, then `$goal-prep`, then `/goal follow docs/goals/<slug>/goal.md`.
- It writes durable project files: `goal.md`, `state.yaml`, and `notes/` receipts.
- The core loop separates work into Scout, Judge, and Worker roles:
  - Scout maps repo facts, constraints, commands, risks, and unknowns.
  - Judge chooses the next bounded implementation slice with files, stop conditions, and acceptance checks.
  - Worker patches, verifies, records receipts, and hands updated state back to `/goal`.
- Goal Buddy keeps repo files authoritative while optional extensions mirror state outward to GitHub, Linear, Slack, etc.

## Why it matters
Goal Buddy is a useful concrete design reference for local-first agent orchestration. The core insight is that a long Codex run needs a goal charter, machine-readable board state, notes/receipts, and verification gates more than it needs a hosted tracker. That aligns with Self-OS/taskOS/Hermes design priorities: repo-centric state, auditable agent progress, explicit work slicing, and receipts before completion claims.

## Self-OS implications
- Goal Buddy's `goal.md` + `state.yaml` + `notes/` shape is worth comparing with Self-OS mission workspaces and taskOS task folders.
- The live board pattern may inform Hermes Kanban: cards should expose state transitions, verification receipts, and the active agent role.
- The Scout/Judge/Worker role split could become a reusable planning/execution/review pattern for Codex/Hermes agent runs.
- Extensions should remain mirrors, not sources of truth — consistent with Self-OS using durable Markdown/Git state first and SaaS integrations second.

## Raw content
Open source Codex /goal companion

# Give /goala best friend.

Goal Buddy prepares a goal.md for the Codex /goal command, keeps state.yaml as local truth, and lets you extend goal state into GitHub, Slack, Linear, and other places when the workflow needs it.

```bash
npx goalbuddy
$goal-prep

Prepared docs/goals/improve-project/
  goal.md
  state.yaml
  notes/

/goal follow goal.md
```

## Compile the board
Turn rough intent into a scoped goal.md, state.yaml, and starter /goal command.

## Keep one truth
Codex reads and updates local state instead of relying on a hosted tracker.

## Extend outward
Optional extensions publish handoffs or mirrors while state.yaml stays primary.

## Watch the board appear while Codex keeps working.
GoalBuddy can open a local live board inside Codex before the task list is finished, so the work becomes visible as Scout, Judge, and Worker tasks populate.

## A bounded loop for long Codex runs.
Goal Buddy separates mapping, decision, and implementation so /goal can continue from explicit state instead of re-inferring the project every turn.

### Scout — Map repo facts
Capture file ownership, commands, constraints, risks, and unknowns before selecting implementation work.

### Judge — Choose the next slice
Convert findings into one task with allowed files, stop conditions, and concrete acceptance checks.

### Worker — Patch and receipt
Implement the slice, record changed files and verification output, then hand updated state back to /goal.

## Repo files stay authoritative.
Goal Buddy writes the goal charter, machine-readable state, and notes into your repository. /goal can resume from those files, and extensions can mirror the state without replacing it.

### goal.md
Human-readable charter for Codex /goal: intent, scope, acceptance criteria, and run instructions.

### state.yaml
Structured board state for active agent, tasks, dependencies, receipts, and verification status.

### notes/
Longer Scout findings, Worker receipts, blocked-task notes, and command output summaries.

## State advances only after evidence.
Each role writes enough information for the next role to continue, and verification gates completion claims.

1. Capture intent
2. Scout constraints
3. Judge the slice
4. Worker patches
5. Verify and update state

## Extension surface
Optional extensions include GitHub PR workflow, GitHub Projects, codebase onboarding, CI failure triage, Linear ticket handoff, and Slack standup digest.
