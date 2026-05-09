---
title: "Experiment With an Agno Agent Platform Agent"
date: 2026-05-09
type: idea
status: seed
domain: coding-projects-os
source: telegram
origin_ref: "Conversation note: experiment with an agent from the Agno Agent Platform setup blog"
tags: [idea, self-os, agno, agentos, agent-platform, claude-code, evals, traces, agent-runtime, experiment]
taskos_path: null
kanban_tasks: []
---

# Experiment With an Agno Agent Platform Agent

## One-line idea

Run a small experiment using the Agno / AgentOS agent-platform setup from Ashpreet Bedi’s “How to Build an Agent Platform” blog, then evaluate whether its runtime, traces, evals, scheduler, interfaces, and Claude Code improvement loop are useful for Self-OS.

## Why it might matter

The Agno AgentOS template looks like a concrete way to test the “agent platform” architecture rather than only theorizing about it. Self-OS already has pieces of this shape — Telegram interface, cron jobs, Git-backed memory, Hermes skills, taskOS, Kanban, and Claude/Codex workflows — but it does not yet have a unified app-style agent runtime with sessions, traces, eval history, scheduler, and a UI around agents.

A small experiment could clarify whether Agno should become:

- a useful external runtime for selected Self-OS agents,
- a reference architecture to borrow from,
- a dead end because Hermes already covers the needed platform layer,
- or a bridge for building/hosting specific agents with richer traces and interfaces.

## Current shape

- What we know:
  - The source blog has already been captured in `ai-research-os` as `wikis/ai-research-os/raw/articles/2026-05-09-how-to-build-an-agent-platform.md`.
  - The blog’s core stack is Agno/AgentOS with FastAPI, Postgres, Docker, evals, scheduler, Railway deployment, interfaces, and Claude Code prompts for creating/improving agents.
  - The experiment should be practical and small: create one agent, run it locally, inspect traces/evals, and compare against the current Hermes/Self-OS stack.
- What is fuzzy:
  - Which first agent should be built: wiki search, Self-OS brief assistant, taskOS triage, code search, research scout, or newsletter helper.
  - Whether this should live inside `/data/Self-OS`, `/data/taskOS`, or as a separate disposable experiment repo.
  - Whether Agno complements Hermes or duplicates too much of the existing orchestration layer.
  - How much to integrate with existing credentials/tools versus keeping the experiment sandboxed.
- What triggered it:
  - The Agent Platform article capture and the follow-up idea: “let’s also experiment with agent from agno agent platform setup blog.”

## Links / evidence

- Related raw source:
  - `/data/Self-OS/wikis/ai-research-os/raw/articles/2026-05-09-how-to-build-an-agent-platform.md`
  - Source URL: https://www.ashpreetbedi.com/agent-platform
- Related repo/template from the article:
  - https://github.com/agno-agi/agentos-railway-template
- Related Self-OS concepts:
  - Self-OS operating loop
  - Hermes cron + Telegram control surface
  - taskOS backlog
  - Night Shift / Day Shift workflow
  - Claude Swarm Multi-Agent Framework idea

## Possible implementation shape

- Likely repo/system:
  - Prefer a separate disposable experiment directory first, e.g. `/data/experiments/agno-agent-platform/`, to avoid polluting Self-OS.
  - If useful, promote findings into taskOS and/or a Self-OS architecture note.
- Candidate first agents:
  - **Wiki search / source scout:** searches captured wiki raw files and returns relevant notes.
  - **Self-OS brief explainer:** reads recent brief outputs and explains what changed.
  - **taskOS triage agent:** inspects idea notes and suggests which should become taskOS tasks.
  - **Code search agent:** mirrors the template’s example, useful for testing traces/evals without sensitive scope.
- Experiment steps:
  1. Clone `agno-agi/agentos-railway-template` into a sandbox experiment directory.
  2. Run locally with Docker and Postgres.
  3. Connect the local AgentOS UI if feasible.
  4. Use Claude Code / template docs to create one simple agent.
  5. Add 3–5 eval cases that match the agent’s job.
  6. Inspect traces, sessions, eval history, scheduler, and interface hooks.
  7. Write a short verdict: adopt, borrow patterns, defer, or discard.
- Dependencies:
  - Docker / Docker Compose.
  - OpenAI key or compatible model config for Agno.
  - Claude Code if testing recursive create/improve prompts.
  - Careful secret isolation.
- Risks / objections:
  - Could duplicate Hermes capabilities without adding much value.
  - UI/platform may be overkill if Telegram + Git-backed Markdown remains the preferred Self-OS control surface.
  - Connecting real Self-OS tools too early could create security/permission drift.
  - AgentOS cloud/pro UI may not be necessary for the learning goal.

## Promotion checklist

Ready for taskOS when:

- [ ] First agent use case is chosen.
- [ ] Experiment location is chosen and sandbox boundaries are clear.
- [ ] Success criteria are clear: what would make Agno useful enough to adopt or borrow from?
- [ ] Credentials and permissions are scoped safely.
- [ ] Acceptance criteria can be written.

Ready for Kanban when:

- [ ] taskOS folder exists.
- [ ] Work can be assigned to an implementation/research profile.
- [ ] Next action is concrete and testable: clone template, run locally, create one agent, run evals, write verdict.

## Next question

Which first agent should we use for the Agno experiment: wiki search/source scout, Self-OS brief explainer, taskOS triage, code search, or research scout?
