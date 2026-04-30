---
title: "Addy Osmani — Agent Harness Engineering"
date_created: 2026-04-30
date_modified: 2026-04-30
summary: "Addy Osmani's “Agent Harness Engineering” argues that a coding agent is the model plus everything built around it: prompts, tools, execution environments, hooks, memory, context policies, subagents, feedback loops, and o"
tags: [agents, harness-engineering, coding-agents, ai-engineering, verification, agentic-workflows]
type: source
status: final
---

# Addy Osmani — Agent Harness Engineering

**Type:** article  
**Date:** 2026-04-29  
**URL:** https://addyosmani.com/blog/agent-harness-engineering/  
**Raw file:** [[../raw/articles/2026-04-29-addy-osmani-agent-harness-engineering.md]]

**Summary:** Addy Osmani's “Agent Harness Engineering” argues that a coding agent is the model plus everything built around it: prompts, tools, execution environments, hooks, memory, context policies, subagents, feedback loops, and observability. The central thesis is that many agent failures should not be treated as fixed model limitations; they are often harness gaps that can be ratcheted into durable constraints, tests, hooks, rules, and workflows.
The post is especially relevant for production coding agents because it reframes agent quality as an engineering discipline. Instead of waiting for better models, teams should work backward from desired behaviors, instrument failures, update AGENTS.md/CLAUDE.md, add blocking hooks, route work through planner/reviewer subagents, and wire typechecks/tests back into the loop.

**Key contributions:**
- “Agent = Model + Harness”; if you are not improving the model, you are improving the harness.
- A harness includes system prompts, CLAUDE.md, AGENTS.md, skill files, tools, MCP servers, sandboxes, filesystem access, orchestration, hooks, middleware, logs, traces, cost, and latency metering.
- Products such as Claude Code, Cursor, Codex, Aider, and Cline are harnesses around models, and the same model can behave very differently depending on the harness.
- The article reframes many failures as configuration/system-design failures: missing conventions, unsafe commands, long-task drift, and false completion claims.
- Harness engineering uses a ratchet: every agent failure should become a rule, hook, test, reviewer check, or environment change that makes the same failure less likely next time.
- Every line in a good AGENTS.md should trace back to a specific thing that went wrong.

**Tags:** agents, harness-engineering, coding-agents, ai-engineering, verification, agentic-workflows
