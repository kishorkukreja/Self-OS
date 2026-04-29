---
title: "AgentField"
date_created: 2026-04-29
date_modified: 2026-04-29
summary: "AgentField captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-of"
tags: [agent-orchestration]
type: source
status: final
---

# AgentField

**Type:** repo  
**Date:** 2026-04-28  
**URL:** https://github.com/Agent-Field/agentfield  
**Raw file:** [[../../raw/repos/agentfield-2026-04-28.md]]

**Summary:** AgentField captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-offs that can be compared against the rest of the AI Research OS corpus. Latest Release: v0.1.71 (Apr 21, 2026); v0.1.72-rc.8 (Apr 28, 2026) AgentField is an open-source control plane that makes AI agents callable by any service—frontends, backends, other agents, cron jobs—just like any other API. You write agent logic in Python, Go, or TypeScript. AgentField turns it into production infrastructure: routing, coordination, memory, async execution, and cryptographic audit trails. Every function becomes a REST endpoint, every agent gets a cryptographic identity, and every decision is traceable. "AI has outgrown chatbots and prompt orchestrators. Backend agents need backend infrastructure." - Reasoners & Skills — @app.reasoner() for AI judgment; @app.skill() for deterministic code. - Structured AI — app.ai(schema=MyModel) returns typed Pydantic/Zod output via LiteLLM (100+ LLMs). - Harness — app.harness("task", provider="claude-code") dispatches multi-turn coding tasks to Claude Code, Codex, Gemini CLI, or OpenCode. - Cross-Agent Calls — app.call("other-agent.func") routes through the control plane with tracing.

**Key contributions:**
- License: Apache 2.0  Stars: 1.5k  Forks: 251  Contributors: 32
- Languages: Go (50.0%), TypeScript (30.1%), Python (18.9%)
- Latest Release: v0.1.71 (Apr 21, 2026); v0.1.72-rc.8 (Apr 28, 2026)
- "AI has outgrown chatbots and prompt orchestrators. Backend agents need backend infrastructure."
- - Reasoners & Skills — @app.reasoner() for AI judgment; @app.skill() for deterministic code.

**Related concepts:** [[concepts/agent-orchestration]]  
**Primary entity:** [[entities/agentfield]]

**Tags:** agent-orchestration
