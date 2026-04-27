---
title: "Multica — Managed Agents Platform"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Open-source managed agents platform that turns coding agents into team members with task assignment, autonomous execution, skill compounding, and unified runtime management."
tags: [managed-agents, multi-agent, claude-code, skill-compounding, open-source, human-ai-teams]
type: source
status: final
---

# Multica — Managed Agents Platform

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/multica-ai/multica
**Raw file:** [[../../raw/repos/multica-2026-04-13.md]]

**Summary:** Multica is an open-source managed agents platform designed to turn coding agents into real teammates. Users assign issues to agents as they would to human colleagues; agents pick up work, write code, report blockers, and update statuses autonomously. The platform manages the full agent lifecycle from task assignment to skill reuse, with support for Claude Code, Codex, OpenClaw, and OpenCode. Architecture comprises a Next.js frontend, Go backend with WebSocket streaming, PostgreSQL with pgvector, and a local agent daemon that auto-detects available CLIs.

**Key contributions:**
- Agent lifecycle management: enqueue, claim, start, complete/fail with real-time streaming
- Reusable skills system where every solution compounds team capabilities
- Unified runtime dashboard for local daemons and cloud instances
- Multi-workspace organisation with workspace-level isolation
- Auto-detection of agent CLIs (claude, codex, openclaw, opencode) on PATH

**Tags:** managed-agents, multi-agent, claude-code, skill-compounding, open-source, human-ai-teams
