---
source: https://addyosmani.com/blog/agent-harness-engineering/
date: 2026-04-29
type: article
tags: [agents, harness-engineering, coding-agents, ai-engineering, verification, agentic-workflows]
status: processed
---

# Addy Osmani — Agent Harness Engineering

## Summary
Addy Osmani's “Agent Harness Engineering” argues that a coding agent is the model plus everything built around it: prompts, tools, execution environments, hooks, memory, context policies, subagents, feedback loops, and observability. The central thesis is that many agent failures should not be treated as fixed model limitations; they are often harness gaps that can be ratcheted into durable constraints, tests, hooks, rules, and workflows.

The post is especially relevant for production coding agents because it reframes agent quality as an engineering discipline. Instead of waiting for better models, teams should work backward from desired behaviors, instrument failures, update `AGENTS.md`/`CLAUDE.md`, add blocking hooks, route work through planner/reviewer subagents, and wire typechecks/tests back into the loop.

## Key points
- “Agent = Model + Harness”; if you are not improving the model, you are improving the harness.
- A harness includes system prompts, `CLAUDE.md`, `AGENTS.md`, skill files, tools, MCP servers, sandboxes, filesystem access, orchestration, hooks, middleware, logs, traces, cost, and latency metering.
- Products such as Claude Code, Cursor, Codex, Aider, and Cline are harnesses around models, and the same model can behave very differently depending on the harness.
- The article reframes many failures as configuration/system-design failures: missing conventions, unsafe commands, long-task drift, and false completion claims.
- Harness engineering uses a ratchet: every agent failure should become a rule, hook, test, reviewer check, or environment change that makes the same failure less likely next time.
- Every line in a good `AGENTS.md` should trace back to a specific thing that went wrong.
- Harness components should be justified by desired behavior: if you cannot name the behavior a component produces or prevents, it probably should not be there.
- Filesystem and git are foundational durable-state primitives for coding agents, enabling shared context, rollback, progress tracking, and branch-based experimentation.

## Why it matters
This is directly aligned with rigorous Self-OS/Sandcastle-style agent engineering: agents need structured harnesses, not vibes. The article provides language and patterns for turning agent failures into durable system improvements across planning, execution, review, sandboxing, memory, and verification.

## Raw content
The article defines harness engineering as the discipline of improving the scaffolding around an AI model: prompts, tools, execution environments, hooks, memory, context policies, subagents, feedback loops, and observability. Its core claim is that a coding agent is the model plus everything built around it, and that scaffolding should tighten every time the agent slips.

Viv Trivedy's formulation anchors the post: “Agent = Model + Harness. If you're not the model, you're the harness.” A raw model is not an agent. It becomes an agent when surrounded by infrastructure for state, tool execution, feedback loops, context injection, constraints, recovery paths, observation, and verification. Osmani lists harness pieces including system prompts, `CLAUDE.md`, `AGENTS.md`, skill files, subagent prompts, tools, skills, MCP servers, tool descriptions, filesystem access, sandbox, browser, bundled infrastructure, orchestration logic, subagent spawning, handoffs, model routing, hooks, compaction, continuation, lint checks, logs, traces, cost, and latency metering.

The article emphasizes that products such as Claude Code, Cursor, Codex, Aider, and Cline are all harnesses. Even with the same model, the user experience can be dramatically different because the harness shapes behavior. Simon Willison's simplified definition of an agent as something that “runs tools in a loop to achieve a goal” is used to underline the role of tooling and orchestration.

A major reframe is the “skill issue” argument. When an agent makes a mistake, teams often blame the model and wait for a better one. Harness engineering instead asks what configuration or system-design change would prevent recurrence. If the agent did not know a convention, add it to `AGENTS.md`. If it ran a destructive command, add a blocking hook. If it got lost in a long task, split planning and execution. If it claimed broken code was complete, wire typecheck and test failures back into the loop.

The article's central practice is the ratchet: every mistake becomes a rule. If an agent ships a PR with a commented-out test, potential fixes include adding “never comment out tests” to `AGENTS.md`, adding a pre-commit hook that blocks `.skip(` or `xit(`, and adding a reviewer subagent that flags commented-out tests as blockers. The principle is that every line in a good `AGENTS.md` should be traceable to a specific failure.

Osmani also argues that harness design should work backward from desired behavior. Every harness component should exist to produce or prevent a behavior. If a component cannot be tied to a behavior, it probably should not be there.

The article highlights filesystem and git as durable-state primitives. The filesystem lets an agent read code, data, docs, and intermediate artifacts rather than holding everything in context. It also creates a shared coordination surface for humans and multiple agents. Git adds versioning, rollback, progress tracking, and branch-based experimentation. These primitives become the substrate for reliable coding-agent workflows.
