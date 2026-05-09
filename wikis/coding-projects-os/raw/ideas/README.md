---
title: "Coding Projects OS — Idea Inbox"
date: 2026-05-09
type: idea-inbox
status: active
---

# Coding Projects OS — Idea Inbox

This folder is the lightweight capture point for raw implementation-shaped ideas that are not ready for taskOS or Kanban yet.

Use this for:

- Random project/product/automation ideas captured on the go.
- Ideas surfaced by the daily Self-OS brief or weekly synthesis.
- Half-formed workflows that need more context before becoming work.
- Repeated patterns that might later become a skill, taskOS task, or Kanban task.

Do **not** use this for:

- External article/repo/video source capture → route to the relevant wiki `raw/articles`, `raw/repos`, etc.
- Fully actionable implementation work → route directly to `/data/taskOS/tasks/<slug>/` and/or Hermes Kanban.
- Personal/finance/health ideas → route to `personal-os` unless explicitly implementation-shaped.
- Supply-chain/newsletter/business ideas → route to `supply-chain-os` unless they are software/automation implementation ideas.

## Lifecycle

1. **Capture** — save a raw idea note here using `templates/idea.md`.
2. **Shape** — daily/weekly briefs may append context, links, objections, and next questions.
3. **Promote to taskOS** — once the idea has a clear outcome, constraints, and acceptance criteria, create `/data/taskOS/tasks/<slug>/README.md` and `docs/idea.md`.
4. **Promote to Kanban** — once the taskOS idea is ready for work, create one or more Hermes Kanban tasks and link the task IDs back into the taskOS note and/or this idea note.
5. **Archive or kill** — if it no longer looks useful, set `status: archived` or `status: killed` and add a short reason.

## Status values

- `seed` — raw capture, not yet evaluated.
- `shaping` — actively gathering context or refining the idea.
- `ready-for-taskos` — clear enough to become a taskOS task folder.
- `promoted-taskos` — taskOS folder exists.
- `promoted-kanban` — Kanban task(s) exist.
- `archived` — kept for reference, not active.
- `killed` — explicitly rejected.
