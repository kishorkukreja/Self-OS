---
source: https://x.com/ashpreetbedi/status/2053885390717890757?utm_source=tldrai
date: 2026-05-13
type: thread
tags: [auto-improving-software, agent-platforms, agno, claude-code, evals, traces, agent-workflows, self-os]
status: processed
---

# Ashpreet Bedi — Auto-Improving Software

## Summary

Ashpreet Bedi describes an agent-platform pattern where coding agents create, improve, extend, hill-climb, and review other agents using a colocated platform stack. The key claim is that auto-improvement becomes practical when agent code, traces, logs, evals, and live runtime all live close enough for a coding agent to run end-to-end loops without crossing multiple disconnected tools.

## Source metadata

- Author: Ashpreet Bedi / `@ashpreetbedi`
- Published: 5:10 PM · May 11, 2026
- Engagement at capture: 6 replies, 45 reposts, 368 likes, 672 bookmarks, 24.1K views
- Linked repo: https://github.com/agno-agi/agent-platform-railway
- Related docs: https://docs.agno.com/

## Core idea

Coding agents have changed how software is built; the next step is coding agents improving the agent platforms they run on. Ashpreet frames the entire agent development lifecycle as five coding-agent prompts:

1. **Create** — scaffold a new agent.
2. **Improve** — harden an existing agent against its own spec.
3. **Extend** — add capabilities to an existing agent.
4. **Hill Climb** — run evals, diagnose failures, and fix what is in scope.
5. **Review** — sweep the repo for drift between docs, code, and config.

The most important loop is **Improve → Hill Climb**, which recursively improves agents with minimal oversight.

## Why the loop works

Ashpreet argues that most software cannot auto-improve because inputs and outputs are scattered across tools, auth systems, and interfaces. His agent platform is intentionally designed for auto-improvement: Claude Code can test an agent, read sessions/traces/logs, decide PASS/FAIL, edit the agent, and run it again.

Three enabling properties:

1. **Every action is exposed as an API** — running an agent, reading a session, and running an eval can all be executed with `curl` or bash.
2. **Data is colocated** — sessions and traces live in Postgres, so a coding agent can trigger a run and inspect outputs without leaving the environment.
3. **Logs over everything** — the platform runs locally on Docker; the coding agent can read live logs and make updates. The test/review loop is about 5 seconds.

## Lifecycle details

### Create an agent

Prompt shape:

```text
Run create-new-agent.md in a new branch.
```

Claude asks what the agent should do and which tools it needs, searches Agno docs via MCP for the right toolkit, generates the agent file, registers it in `app/main.py`, restarts the container, and smoke-tests via `curl`. Simple agents take roughly 5–10 minutes from prompt to working agent.

### Improve an agent

Prompt shape:

```text
Run improve-agent.md on code-search agent.
```

Claude reads the agent's `INSTRUCTIONS`, derives 8–12 probes, runs them against the live container via `curl`, reads responses and tool calls from logs, judges PASS/FAIL against the spec, edits `agents/<slug>.py`, hot-reloads, and reruns failed probes. Iteration is capped at five rounds and stops earlier if everything passes.

Probe types include:

- Golden-path cases.
- Edge cases.
- Tool-selection cases.
- Adversarial cases such as prompt injection, malformed input, and attempts to pull the agent off-purpose.

### Extend an agent

Prompt shape:

```text
Run extend-agent.md on code-search agent.
```

This is a human-guided flow for adding tools, refining prompts, and fixing bugs. Claude uses the Agno docs MCP so toolkit research is grounded in the real API, then makes small verified changes and smoke-tests them.

### Hill Climb

Prompt shape:

```text
Run eval-and-improve.md.
```

Hill Climb runs the eval suite, diagnoses failures, and fixes in-scope issues. Failure categories map to likely fix locations: missing instruction rule, hallucination, wrong tool, or overspecified rubric. The loop reruns only failing cases, then reruns the full suite to catch regressions.

The eval suite is two files:

- `evals/cases.py` — cases with input, rubric, and optional expected tool call.
- Agno's `AgentAsJudgeEval` and `ReliabilityEval`.

### Review

Prompt shape:

```text
Run review-and-improve.md.
```

Claude sweeps the repo for drift between docs, code, and config. Mechanical drift is auto-fixed; larger issues are flagged with recommended next steps. Examples:

- Agent files on disk should be registered in `app/main.py`.
- Env vars read by code should appear in `example.env` and `AGENTS.md`.
- Markdown paths should still exist.
- Scripts should match what docs claim.

## Why agent platforms are a good testbed

Agent platforms are unusually well-suited to recursive improvement because:

- They are greenfield enough to be designed for coding agents from the start.
- The improvement loop is clear: run, read logs, grade response, edit, run again.
- Improvements are measurable and valuable because agent behavior directly improves.
- The platform hosting the loop becomes the first thing the loop improves.

## Self-OS implications

This is highly relevant to Self-OS and Hermes because it describes the missing substrate for reliable agent self-improvement:

- **Colocate code, logs, traces, evals, and docs** so coding agents can inspect cause/effect without tool friction.
- **Expose all key actions as scriptable APIs** (`curl`, CLI, bash), not just UI buttons.
- **Make evals first-class** for each agent/workflow, not an afterthought.
- **Use capped repair loops**: derive probes from the spec, run live checks, patch only in-scope failures, rerun failed cases, then rerun the full suite.
- **Add drift review** as a recurring workflow for docs/config/code alignment.

For Self-OS, this suggests a practical next pattern:

```text
skill/task spec → probes/evals → live run → logs/traces/session readback → patch → rerun → drift review
```

It also reinforces the existing Day/Night Shift model: Day Shift defines specs/evals and reviews drift; Night Shift agents execute bounded improvement loops against those specs.

## Related concepts

- Agent platform architecture.
- Eval-driven agent development.
- Recursive self-improvement loops.
- Colocated traces/logs/runtime as an agent-operable substrate.
- Docs/code/config drift repair.

## Extraction notes

- X/Twitter extraction used browser DOM text because `xurl` is not installed on this machine.
- The source is an X Article, not just a short tweet, so the capture preserves the full article structure and linked implementation repo.
