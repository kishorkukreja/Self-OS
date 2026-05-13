---
source: https://x.com/steipete/status/2053032450138276274
date: 2026-05-12
type: thread
tags: [codex, crabbox, agent-workflows, remote-sandboxes, bug-repair, parallel-agents, verification-loops, self-os]
status: processed
---

# Peter Steinberger — Codex + Crabbox for parallel bug repair

## Summary

Peter Steinberger describes a bug-investigation workflow where Codex recreates the exact buggy state inside an ephemeral Crabbox, verifies the bug, fixes it, and verifies the fix. The value is isolation and parallelism: local machine state cannot pollute the reproduction, and multiple sessions can run at once.

## Extracted post

Author: Peter Steinberger / `@steipete`  
Published: 8:40 AM · May 9, 2026  
Engagement at capture: 106 replies, 178 reposts, 3K likes, 2.8K bookmarks, 315.2K views

> Whenever I investigate a bug, I let codex recreate the exact state in an emphemeral crabbox, verify the bug, fix it, verify the fix.
>
> No messy state because local system might be polluted, and no slowdown because I run 10 sessions in parallel.
>
> crabbox.sh

Note: source spelling says `emphemeral`; likely intended `ephemeral`.

## Why it matters

This is a concrete **iterative repair loop** pattern: reproduce → verify failure → patch → verify success. The important addition is that each loop runs in a clean remote sandbox, so the result is less likely to depend on hidden local state.

## Self-OS implications

- For Night Shift coding, use sandboxed worktrees/remote boxes for bug reproduction rather than trusting local polluted environments.
- Store failure reproduction commands as first-class acceptance criteria before letting an implementation agent patch.
- Parallelize bug fixes only when each agent has an isolated workspace and an objective validation command.
- Pair this with OpenAI's Codex iterative repair cookbook and Crabbox-style remote execution.

## Related captures

- `wikis/ai-research-os/raw/resources/crabbox-remote-agent-workspaces-2026-05-12.md`
- `wikis/ai-research-os/raw/resources/openai-codex-iterative-repair-loops-2026-05-12.md`
