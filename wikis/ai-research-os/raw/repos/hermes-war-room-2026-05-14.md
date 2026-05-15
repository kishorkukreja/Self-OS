---
source: https://github.com/Naroh091/hermes-war-room
date: 2026-05-14
type: repo
tags: [hermes, ai-agents, agent-orchestration, kanban, dashboard, agent-platforms, self-os]
status: processed
---

# Naroh091 / hermes-war-room — Orchestration War Room

## Summary

Hermes War Room is a browser dashboard built on top of Hermes Agent’s native multi-profile delegation and kanban systems. It does not replace Hermes orchestration; it acts as a visual UI layer that makes the agent fleet visible, legible, directable, and manageable from one screen instead of multiple terminals and `hermes kanban tail` sessions. The repo is highly relevant to Self-OS because it directly targets the same Hermes primitives already used in the operating loop: profiles, kanban, delegation, worker dispatch, mission threads, and async task tracking.

## Repository metadata

- **Repository:** `Naroh091/hermes-war-room`
- **URL:** https://github.com/Naroh091/hermes-war-room
- **Description:** UI layer for the native Hermes orchestration features
- **Primary language:** Vue
- **Default branch:** `master`
- **Stars:** 191
- **Forks:** 13
- **Open issues:** 3
- **License:** MIT
- **Created:** 2026-05-03
- **Last pushed:** 2026-05-11
- **Latest release surfaced by extraction:** `v1.4.1` on 2026-05-11
- **Topics:** `agent`, `agentic-ai`, `hermes`, `orchestration`

## Key points

- **Thin visual layer over Hermes:** War Room shells out to the Hermes CLI, reads `~/.hermes/kanban.db`, and uses Hermes profiles rather than creating a separate orchestration backend.
- **Main pages:** `/` for live War Room, `/team` for roster/personnel management, and `/missions` for archived mission threads.
- **Mission control:** Chat tab briefs the active orchestrator; Board tab shows active kanban tasks in Todo / Ready / Running / Blocked columns.
- **Operatives floor:** Each Hermes profile is rendered as a workstation with callsign, avatar, color, status pill, and live activity/speech bubble while reasoning or calling tools.
- **Operative drill-down:** Shows the current task, who delegated it, subtasks spawned by that operative, recent tool/reasoning activity, and the read-only mission thread.
- **Team management:** UI can hire, retrain, deactivate, and fire Hermes profiles by editing profile-level filesystem state such as SOUL.md, skills, tools, model, and behaviour rules.
- **ACP integration:** Backend spawns `hermes -p <slug> acp` subprocesses and pools them per profile.
- **Persistence:** War Room-specific state is kept in `data/war-room.db`; Hermes task state remains in the native kanban DB.
- **Auto-nudge loop:** Watches delegated task IDs; when watched tasks become done/blocked, it injects a synthetic system message back into the orchestrator session to summarize results.

## Why it matters

This is a concrete implementation of a **Hermes control room**: not a replacement for the Self-OS operating loop, but a visual cockpit for the same underlying primitives. It is useful as evidence that a dashboard can be valuable when it exposes existing repo/profile/kanban state rather than becoming a duplicate source of truth.

## Self-OS implications

- **Good dashboard shape:** This aligns with the Self-OS rule that Git/markdown/kanban remain durable records while UI is a control surface. War Room reads Hermes state rather than inventing a parallel task system.
- **Useful for Tailscale/private access:** A local browser UI over Hermes fits the existing preference for private control surfaces instead of public URLs.
- **Potential cockpit for Night Shift:** The mission + operative + kanban visualization could help inspect AFK agent work without SSHing into logs.
- **Risk to manage:** The UI has power to mutate profiles/SOUL/tools. If adopted, it needs strict permissions, backup/versioning of profile edits, and review gates before becoming part of the main operating loop.
- **Avoid dashboard gravity:** This should complement Telegram + markdown operating briefs, not replace them. Best initial use would be read-heavy observability, then limited profile/task controls once validated.

## Quickstart surfaced

```bash
mkdir -p ~/hermes-war-room && cd ~/hermes-war-room
curl -L -o hermes-war-room.tar.gz \
  https://github.com/Naroh091/hermes-war-room/releases/latest/download/hermes-war-room.tar.gz

tar xzf hermes-war-room.tar.gz

HERMES_HOME=$HOME/.hermes NITRO_HOST=127.0.0.1 NITRO_PORT=3000 \
  node .output/server/index.mjs
# → http://localhost:3000
```

Development quickstart:

```bash
hermes profile create lider
hermes profile create investigador
hermes profile create legal
hermes gateway start

git clone https://github.com/Naroh091/hermes-war-room.git
cd hermes-war-room
pnpm install
pnpm dev
# → http://localhost:3000
```

## Extraction notes

- User supplied a LinkedIn safety redirect URL; canonical source resolved to `https://github.com/Naroh091/hermes-war-room`.
- `web_extract` captured a rich repository summary.
- GitHub API was used for current metadata.
- Raw README was fetched from `https://raw.githubusercontent.com/Naroh091/hermes-war-room/master/README.md`.

## Raw content excerpt

```markdown
# Orchestration War Room

> A multilingual visual UI for Hermes agentic orchestration/delegation system.

A browser dashboard on top of Hermes Agent's multi-profile delegation and kanban systems. Hermes already gives you everything you need to run a fleet of specialised agents that hand work to each other — the Orchestration War Room just makes that fleet visible, legible, and directable from a single screen instead of a forest of terminal sessions and `hermes kanban tail` invocations.

TL;DR — Hire a leader and a team, brief the leader, watch the team work. The War Room handles all the wiring (kanban delegation, status tracking, notifications) underneath.

## Why does this exist?

Hermes has powerful primitives for multi-agent work:

- Profiles — isolated agent personas with their own SOUL.md, skills, tool permissions, model, and history.
- delegate_task — a synchronous in-process subagent call. Good for small one-shot reasoning fan-outs within a single turn.
- Kanban — a durable SQLite-backed task board where any profile can drop a row and any other profile will pick it up asynchronously, with parent/child dependencies, blocking, comments, and run history.

Both delegation paths work great. They are also invisible from the outside: you talk to one profile in hermes chat, and the rest of the fleet quietly hums along in background processes you can only inspect by SSH-ing into your own machine and grepping logs.

The War Room is the glass on the floor: a real-time dashboard that shows you the whole team, what each operative is currently thinking about, what tasks are in flight, who delegated what to whom, and the final results — all without leaving the browser. It's a thin visualisation + coordination layer; the actual orchestration logic still lives inside Hermes.

## Tech under the hood

- Frontend: Nuxt 4 + Nuxt UI + Tailwind CSS v4.
- Backend: Nuxt Nitro server. Talks to Hermes via Agent Client Protocol by spawning `hermes -p <slug> acp` subprocesses and pooling them per-profile. Reads Hermes kanban DB directly, read-only.
- Persistence: local SQLite `data/war-room.db` for operative customisations, missions, messages, and auto-nudge watch list.
- Live updates: per-mission Server-Sent Events stream; polling for kanban and operatives floor.
```
