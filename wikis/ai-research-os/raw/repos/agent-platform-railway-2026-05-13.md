---
source: https://github.com/agno-agi/agent-platform-railway
date: 2026-05-13
type: repo
tags: [agno, agent-platforms, auto-improving-software, railway, claude-code, evals, traces, agent-workflows]
status: processed
---

# agno-agi/agent-platform-railway

## Summary

`agno-agi/agent-platform-railway` is a starter agent platform built with Agno, designed to be built, run, and improved by coding agents. It packages a FastAPI + Agno AgentOS runtime, Postgres/pgvector storage, Docker local setup, Railway deployment, eval workflows, and Claude Code prompt docs for creating, improving, extending, hill-climbing, and reviewing agents.

## Repository metadata

- Repository: `agno-agi/agent-platform-railway`
- Description: Agent platform you build, run, and improve using coding agents.
- License: Apache-2.0
- Public repository
- Capture stats from extraction: 18 stars, 2 forks, 1 watcher
- Languages: Python, Shell, Dockerfile
- Contributor: Ashpreet Bedi / `ashpreetbedi`
- Latest extracted commit: `d494a07` — `chore: update readme` — May 12, 2026

## Platform components

The repository includes:

- FastAPI + Agno AgentOS runtime.
- PostgreSQL + pgvector storage for sessions, memory, knowledge, and traces.
- Coding-agent workflows for agent creation and improvement.
- Local Docker setup and Railway deployment.
- Built-in eval workflow for regression testing.
- Optional Slack interface.
- Support for tools, MCP servers, scheduled tasks, multi-agent teams, and workflows.

## Important folders and files

- `agents/` — agent definitions and reference agents.
- `app/` — FastAPI / AgentOS application code.
- `db/` — database-related code/config.
- `docs/` — coding-agent prompts and workflow docs.
- `evals/` — evaluation cases and runner.
- `scripts/` — deployment and utility scripts.
- `.mcp.json` — MCP configuration.
- `AGENTS.md` — agent-oriented repo guidance.
- `CLAUDE.md` — Claude-specific guidance.
- `compose.yaml` — local Docker Compose setup.
- `example.env` — environment variable template.
- `railway.json` — Railway deployment configuration.

## Core design

The codebase is intentionally structured so a coding agent can understand and improve the whole system because traces, agent code, logs, iteration docs/tools, and config files all live together in one repo.

The five lifecycle workflows are:

1. **Create** — ask questions, scaffold a new agent, register it in `app/main.py`, add quick prompts, restart the container, and smoke-test via `curl`.
2. **Improve** — harden an existing agent by deriving probes from its instructions, running live checks, judging responses, and editing until passing.
3. **Extend** — add tools, refine prompts, or fix bugs using grounded Agno docs through MCP.
4. **Hill Climb** — run evals, diagnose failures, fix in-scope issues, and rerun until green.
5. **Review** — detect and repair drift between docs, code, and config.

## Getting started notes

The extracted README flow starts with Docker:

```bash
git clone https://github.com/agno-agi/agent-platform-railway.git agent-platform
cd agent-platform
cp example.env .env
# set OPENAI_API_KEY
docker compose up -d --build
```

Then confirm AgentOS is running at:

```text
http://localhost:8000/docs
```

The Agno UI can connect through `os.agno.com` by adding a local OS pointed at `http://localhost:8000`.

## Why it matters

This repository is a concrete implementation of Ashpreet Bedi's Auto-Improving Software article. It shows what an agent-operable platform looks like when code, evals, logs, traces, docs, and runtime are deliberately colocated.

## Self-OS implications

- Strong candidate reference architecture for a Self-OS agent-platform experiment.
- The repo's `docs/` prompts may be worth inspecting later as templates for Hermes/taskOS workflows.
- The pattern reinforces that Self-OS should expose scriptable actions and colocate operational evidence with specs/evals.
- A safe experiment should run locally or privately over Tailscale first; do not expose AgentOS publicly without auth controls.

## Related capture

- `wikis/ai-research-os/raw/x-threads/2026-05-13-ashpreetbedi-auto-improving-agent-platform.md`
