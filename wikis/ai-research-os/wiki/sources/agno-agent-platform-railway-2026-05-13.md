---
title: "agno-agi/agent-platform-railway"
date_created: 2026-05-14
date_modified: 2026-05-14
summary: "`agno-agi/agent-platform-railway` is the implementation companion to the auto-improving software pattern. It packages a FastAPI and Agno AgentOS runtime with Postgres/pgvector stat"
tags: [agno, agent-platforms, evals, railway]
type: source
status: final
---

# agno-agi/agent-platform-railway

**Type:** repo
**Date:** 2026-05-13
**URL:** https://github.com/agno-agi/agent-platform-railway
**Raw file:** [[../raw/repos/agent-platform-railway-2026-05-13.md]]

## Summary

`agno-agi/agent-platform-railway` is the implementation companion to the auto-improving software pattern. It packages a FastAPI and Agno AgentOS runtime with Postgres/pgvector state, Docker local development, Railway deployment, eval workflows, and prompt documentation for coding agents. The repository is notable because it is structured for both human deployment and agent modification: the code, docs, MCP configuration, evals, logs, and agent definitions are all visible to a coding agent operating in the repo.

The repository matters less as a finished product than as a reference shape for agent-operable platforms. It shows how creation, improvement, extension, hill climbing, and review can be turned into repeatable prompts and scripts. In Self-OS terms, it is evidence that [[concepts/agent-platforms.md]] are moving toward closed-loop engineering systems: a running agent can be tested via API, its traces inspected, its code modified, and its behavior rechecked inside a single workspace. That has direct implications for future Hermes-style skill curation and evaluation workflows.

## Key contributions
- Provides a concrete FastAPI/Agno/Postgres/Railway stack for building and improving agents with coding agents.
- Includes evals and prompt workflows that operationalize the create/improve/extend/hill-climb/review lifecycle.
- Serves as implementation evidence for auto-improving software and agent-operable platform design.

**Tags:** agno, agent-platforms, evals, railway
