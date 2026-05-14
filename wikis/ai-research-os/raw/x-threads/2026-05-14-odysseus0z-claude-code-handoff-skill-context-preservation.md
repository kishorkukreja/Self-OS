---
source: https://x.com/odysseus0z/status/2031850264240800131
date: 2026-05-14
type: thread
tags: [claude-code, agent-memory, context-management, handoff, skills, matt-pocock, coding-agents, self-os]
---

# George / odysseus0z — Claude Code handoff skill for preserving context between sessions

## Source metadata

- Author: George / `@odysseus0z`
- Original post date: 2026-03-11 21:50
- Captured: 2026-05-14
- Source URL: https://x.com/odysseus0z/status/2031850264240800131
- Visible metrics at capture: 22 replies, 66 reposts, 881 likes, ~2.1K bookmarks
- Related repository: https://github.com/mattpocock/skills
- Handoff skill source: https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/handoff/SKILL.md

## User-supplied summary

> How to stop losing context between Claude Code sessions (5K likes)
>
> Every Claude Code session eventually times out, and the next one starts from scratch. Any decisions made, bugs found, or half-finished plans are lost. To fix this, Matt Pocock, an ex-Vercel engineer, created a “/handoff” skill that compresses your current session into a Markdown file so the next agent can start with full context.
>
> To install it, run this in your terminal: `npx skills@latest add mattpocock/skills`.
>
> Select “handoff” from the menu, set Claude Code as your agent, and restart. Before you close a session, run the skill with a quick description of what's next:
>
> `/handoff debug the failing auth tests`
>
> When you start your next session, just load that Markdown file, and Claude will be right back where you left off.

## Canonical handoff skill behavior

From Matt Pocock's `handoff` skill:

```yaml
name: handoff
description: Compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
```

The skill instructs the agent to:

- write a handoff document summarising the current conversation so a fresh agent can continue the work;
- save it to a temporary Markdown file path produced by `mktemp -t handoff-XXXXXX.md`;
- suggest useful skills for the next session;
- avoid duplicating details already captured in PRDs, plans, ADRs, issues, commits, or diffs; and
- tailor the handoff around the user's argument, if one is supplied.

## Why it matters

The operational problem is not just Claude Code session timeout; it is loss of working state. Coding sessions accumulate implicit context that often never reaches durable artifacts:

- decisions made during debugging;
- rejected hypotheses;
- partial plans;
- files already inspected;
- known failing tests;
- next likely actions;
- relevant skills or project conventions.

A short handoff document is a lightweight compaction step that converts ephemeral context into a reviewable Markdown artifact before the agent context window or session lifecycle resets.

## Self-OS / Hermes implications

This pattern maps directly onto Self-OS and Hermes operating-loop needs:

- For long-running wiki compiles, coding-agent work, and research tasks, create a `task-state.md` or handoff artifact before stopping.
- Store durable project handoffs near the work artifact rather than in global memory: e.g. repo plans, taskOS folders, workspace `runs/`, or PR notes.
- Keep persistent memory reserved for stable facts/preferences; use handoff files for transient task state.
- Consider a Hermes analogue to `/handoff` that writes a compact session continuation note with: goal, state, inspected files, decisions, blockers, next command, and recommended skill(s).

## Extraction notes

The public X post itself rendered as a pointer to an X article and visible browser extraction did not expose the full article without login. The capture therefore preserves the user-supplied article summary and verifies the related Matt Pocock repository/skill source separately.
