---
source: https://x.com/tolibear_/status/2053859040556360116
date: 2026-05-11
type: thread
tags: [codex, goalbuddy, kanban, goal-command, coding-agents, agent-workflows, local-state, self-os]
---

# tolibear: Codex /goal now has a native Kanban board

## Summary
Toli announced that Codex `/goal` can now work with a lightweight native Kanban board via Goal Buddy. Starting a `/goal` run can create clickable task cards that move as Codex completes work. The practical install/update path is `npx goalbuddy` or `npx goalbuddy update`, followed by starting the `goal-prep` skill.

## Key points
- Goal Buddy gives Codex `/goal` a visible Kanban-style board for long-running agent work.
- The board uses local project artifacts rather than making a hosted tracker the source of truth.
- The workflow starts with `npx goalbuddy`, then `$goal-prep`, then the generated `/goal follow ...` command.
- This is directly adjacent to Self-OS patterns: goal charters, local state, task receipts, verification gates, and visible progress boards for agent runs.

## Why it matters
This is a concrete example of agent work becoming more inspectable: instead of a coding agent running as an opaque long prompt, it exposes task state as a board and receipt trail. That overlaps strongly with Hermes Kanban, taskOS, mission workspaces, and the Self-OS preference for durable Markdown/local state over SaaS-only trackers.

## Self-OS implications
- Compare Goal Buddy's `goal.md` + `state.yaml` pattern against `/data/taskOS` task folders and Hermes Kanban state.
- Consider whether Hermes mission workspaces should adopt a similar split: human-readable goal charter, machine-readable state, notes/receipts, and visible board.
- The Scout/Judge/Worker split mirrors the Day/Night shift pattern: map constraints, choose a bounded slice, then implement with verification receipts.
- Useful candidate for a future experiment: run `npx goalbuddy` in a sandbox repo, inspect generated files, and decide whether Goal Buddy should become part of the Codex workflow or just inform the Self-OS board/state design.

## Extraction notes
- User asked to try Scrapling/Scraply for the X source.
- Direct Scrapling import was not available in the Hermes Python environment.
- `uv run --with scrapling` also failed because the package import chain required missing dependencies (`curl_cffi`, then `playwright`, then `browserforge`).
- Browser extraction succeeded and recovered the post text. The URL pasted by the user (`https://x.com/shannholmberg/status/2052780393326092407?s=20`) resolved in-browser to a separate Shann article; web search found the matching Goal Buddy post at `https://x.com/tolibear_/status/2053859040556360116`.

## Raw content
toli (@tolibear_)
Codex /goal now has a native Kanban board.

Starting a /goal run now fires up a lightweight Kanban board with clickable cards that move as Codex completes tasks.

npx goalbuddy

Or update with npx goalbuddy update

Start the goal-prep skill

3:25 PM · May 11, 2026 · 58.9K Views
30 replies · 52 reposts · 871 likes · 973 bookmarks


## User-supplied text
```text
Codex /goal now has a native Kanban board.

Starting a /goal run now fires up a lightweight Kanban board with clickable cards that move as Codex completes tasks.

npx goalbuddy

Or update with npx goalbuddy update

Start the goal-prep skill
```
