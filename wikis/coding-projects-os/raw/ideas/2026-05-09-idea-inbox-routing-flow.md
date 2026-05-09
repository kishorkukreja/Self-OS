---
title: "Idea Inbox Routing Flow"
date: 2026-05-09
type: idea
status: seed
domain: coding-projects-os
source: conversation
origin_ref: "Telegram discussion about adding an idea folder to Self-OS wiki"
tags: [idea, self-os, taskos, kanban, operating-loop]
taskos_path: null
kanban_tasks: []
---

# Idea Inbox Routing Flow

## One-line idea

Add a lightweight idea inbox to the Self-OS wiki so random ideas and daily/weekly brief insights can be captured first, shaped over time, then promoted to taskOS and Hermes Kanban only when implementation-ready.

## Why it might matter

The daily and weekly Self-OS briefs will surface patterns, questions, and possible actions. Not all of those should immediately become tasks. Some need a middle state: captured enough not to lose, but not yet forced into project management.

The idea inbox gives Self-OS a missing stage between **passive knowledge** and **active work**.

## Proposed flow

```text
Telegram / conversation / daily brief / weekly synthesis
  ↓
Self-OS wiki idea inbox
  /data/Self-OS/wikis/coding-projects-os/raw/ideas/YYYY-MM-DD-{slug}.md
  ↓
Shape idea through future briefs, notes, and links
  ↓
When outcome + constraints + acceptance criteria are clear:
  /data/taskOS/tasks/{slug}/README.md
  /data/taskOS/tasks/{slug}/docs/idea.md
  ↓
When ready for execution:
  Hermes Kanban task(s)
  ↓
Implementation / review / done
```

## Routing rules

- If it is just a raw idea, save it to the idea inbox.
- If it is an external source, save it to the relevant wiki source folder instead.
- If it is already implementation-ready, create the taskOS folder directly.
- If it needs active work now, create Kanban tasks after taskOS capture.
- If the daily/weekly brief finds a repeated pattern but the action is unclear, create or update an idea note rather than creating premature Kanban work.

## Promotion checklist

Ready for taskOS when:

- [ ] The desired outcome is clear.
- [ ] There is enough context to write acceptance criteria.
- [ ] The idea is likely to require implementation, research, or multi-step planning.
- [ ] It has survived at least one review, repeated signal, or explicit user request.

Ready for Kanban when:

- [ ] taskOS folder exists.
- [ ] The next action is assignable.
- [ ] The result can be verified.
- [ ] The user either requested execution or the operating loop has enough confidence to recommend it.

## Next question

Should this be supported by a small helper script, e.g. `scripts/capture_idea.py`, so Telegram idea captures use one consistent template?
