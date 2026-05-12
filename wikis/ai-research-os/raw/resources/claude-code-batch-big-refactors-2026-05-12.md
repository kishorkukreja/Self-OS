---
source: user-pasted-text
date: 2026-05-12
type: resource
tags: [claude-code, batch, big-refactors, git-worktrees, parallel-agents, code-review, night-shift, self-os]
---

# Claude Code `/batch` — speeding up big refactors with parallel agents

## Summary

The pasted note describes Claude Code's `/batch` command as a way to speed up large mechanical refactors by splitting the work across parallel agents. Instead of manually renaming a function across hundreds of files or replacing a dependency everywhere, `/batch` decomposes the task into units, runs each unit in a separate Git worktree, and opens one pull request per agent.

## Source text

> How to speed up big refactors in Claude Code
>
> Renaming a function across 200 files or swapping “axios” for “fetch” everywhere usually eats up an entire afternoon. The “/batch” command fixes this by splitting the workload across parallel agents:
>
> `/batch rename all instances of getUser to fetchUser across the repo`
>
> It breaks the task into 5 to 30 units, presents a plan, and then runs each unit in its own “git worktree” before opening one PR per agent.

## Key points

- Best suited for large, mostly mechanical refactors.
- The command first presents a plan rather than immediately editing.
- Work is split into 5–30 units.
- Each unit runs in its own Git worktree.
- Output is one PR per agent, preserving reviewability.

## Why it matters

This is a practical form of **bounded parallelism**: split a large repo-wide change into reviewable slices while preserving isolation. It avoids one giant unreviewable diff and aligns with the user's preference for GitHub PR review as the best review surface.

## Self-OS implications

- This maps directly to Night Shift coding orchestration.
- Large refactors should be expressed as batch plans with independent worktree units and objective checks.
- Morning review can prioritize PRs by risk: mechanical rename PRs first, behavior-changing PRs last.
- Good candidate for taskOS templates: require scope, unit split, validation command, and rollback plan before launching agents.

## Open questions to verify later

- Confirm exact Claude Code `/batch` syntax and availability in the user's current Claude Code setup.
- Confirm whether `/batch` can be configured for PR count, worktree location, validation command, and review metadata.
