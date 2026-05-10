# Hermes Kanban for Self-OS

Created: 2026-05-10

## Setup status

Hermes Kanban is initialized on this machine using the default board from the official Hermes Kanban tutorial.

- Hermes CLI: `Hermes Agent v0.12.0 (2026.4.30)`
- Default board SQLite DB: `~/.hermes/kanban.db`
- Additional named boards, when created: `~/.hermes/kanban/boards/<slug>/kanban.db`
- Default board: `default`
- Current known assignee/profile: `default`

The official tutorial treats `hermes kanban init` as safe/idempotent. On this machine it reports the board at `/root/.hermes/kanban.db` and reminds that the gateway hosts the embedded dispatcher.

## Dashboard

Run interactively:

```bash
hermes dashboard --host 127.0.0.1 --port 9119 --no-open
```

Then open:

```text
http://127.0.0.1:9119
```

Keep it bound to localhost; tunnel it over SSH/Tailscale if accessing remotely.

## Self-OS Day/Night shift mapping

Use Kanban as the persistent routing layer for daily operating work:

1. **Day shift planner** creates small, scoped cards from the daily brief, inbox, and active Self-OS projects.
2. **Research / analysis / writing / ops lanes** can initially all use assignee `default`, with role intent in the title, for example `[research]`, `[analysis]`, `[writer]`, `[ops]`.
3. Add named Hermes profiles later only when separation is useful: different tools, models, working directories, memory, or safety boundaries.
4. **Night shift review** checks completed/blocked cards, unblocks anything needing Kishor input, and converts learnings back into Self-OS notes.
5. For long-running agent experiments, put files under `/data/Self-OS/workspaces/hermes-experiments/<slug>/` and reference that path in the Kanban card. Use Kanban for execution state; use the workspace for `mission.md`, run logs, reviews, and curated artifacts.

Minimal first recurring workflow:

```bash
hermes kanban create "[planner] Prepare tomorrow's Self-OS operating brief" \
  --assignee default \
  --tenant self-os \
  --priority 2 \
  --body "Review today's notes, active projects, and blocked Kanban cards. Produce a concise tomorrow brief with top priorities, waiting-for items, and suggested agent tasks."
```

Watch status:

```bash
hermes kanban stats
hermes kanban list --tenant self-os
```

Dispatcher note: ready tasks are picked up by the Hermes gateway's embedded dispatcher, so keep the gateway running when you want agents to execute queued cards:

```bash
hermes gateway status
hermes gateway start
```
