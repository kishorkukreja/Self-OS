---
source: https://addyosmani.com/blog/long-running-agents/?utm_source=tldrnewsletter
date: 2026-04-29
type: article
tags: [agents, long-running-agents, agent-harnesses, persistent-state, verification, ai-engineering]
---

# Addy Osmani — Long-running Agents

## Summary
Addy Osmani's article frames long-running agents as AI systems that can keep making progress over hours, days, or weeks across many context windows and sandboxes. The core claim is that the hard part is not only model intelligence, but externalized state, recovery, verification, artifacts, and reliable handoffs. The article separates long-running agents into long-horizon reasoning, long-running execution, and persistent agency, then argues that production systems usually need all three.

The article is highly relevant to agentic engineering because it treats agents as operational systems rather than chat sessions. It covers finite context, context rot, lack of persistent state, weak self-verification, the Ralph loop, memory-bank patterns, task ledgers, progress logs, and verifier-driven loops that let agents resume safely rather than repeatedly starting from scratch.

## Key points
- A long-running AI agent can make progress over hours, days, or weeks across context windows and sandboxes, recover from failure, leave structured artifacts, and resume where it left off.
- “Long-running” combines three ideas: long-horizon reasoning, long-running execution, and persistent agency.
- METR's time-horizon framing measures the length of tasks frontier models can complete with 50% reliability; Osmani notes the horizon has been doubling roughly every seven months since 2019.
- The three major walls are finite context, lack of persistent state, and poor self-verification.
- Context windows are not enough; context rot degrades performance before hard limits are reached.
- The Ralph loop externalizes state into files such as `prd.json`, `progress.txt`, and `AGENTS.md`, allowing an amnesiac model to continue via a persistent filesystem.
- Long-running agents need test suites, task ledgers, checkpoints, recovery paths, and external verification rather than asking the model if it is done.

## Why it matters
This directly maps to Self-OS-style agent workflows: day/night shifts, persistent task artifacts, filesystem-backed memory, multiple agent handoffs, and external QA. It is a strong source for designing agent runtimes where progress survives context compaction, crashes, flaky tools, and optimistic self-grading.

## Raw content
Addy Osmani defines a long-running AI agent as a system that can keep making progress over hours, days, or weeks. It does this across many context windows and sandboxes, recovers from failure, leaves structured artifacts behind, and resumes where it left off. The article argues that these agents are the next step beyond chat-window agents. Instead of operating in a single sitting until context or patience runs out, they persist across sessions, sandboxes, failures, and context resets.

The article distinguishes three related concepts. Long-horizon reasoning is the ability to plan and execute many dependent steps. Long-running execution is the harness/runtime capability where the agent process itself runs for hours or days, invoking models thousands of times across coding jobs, research sweeps, or 24/7 monitoring. Persistent agency is the Memory Bank style of agent identity, where memories, user preferences, past context, and operational knowledge outlive any single task. Osmani argues that real production agents usually combine all three: long-horizon reasoning inside long-running execution backed by persistent agency.

The economic delegation point is that short agents handle small tasks such as answering questions, summarizing documents, or fixing small bugs, while long-running agents can own larger units of work: entire features, backlog migrations, overnight research sweeps, and junior-analyst-style tasks. Anthropic examples include Claude Sonnet performing more than 30 hours of autonomous coding in internal tests and a run producing an 11,000-line Slack-style app.

The article identifies three walls that long-running agents hit. First, finite context: even very large context windows eventually fill, and context rot degrades model quality before the limit. Second, no persistent state: fresh sessions start blank unless state is externalized. The article uses Anthropic's analogy of engineers working shifts where each new engineer has no memory of the previous shift. Third, no self-verification: models are optimistic when grading themselves and may claim work is done when it is incomplete.

A key pattern is the Ralph loop, also called the Ralph Wiggum technique. The loop picks the next unfinished task from a list such as `prd.json`, builds a prompt with the task and relevant context, calls the agent, runs tests or checks, appends what happened to `progress.txt`, updates the task list, and repeats. Its core insight is that state lives outside the model context: `prd.json` is the plan, `progress.txt` is lab notes, and `AGENTS.md` is a rolling rulebook. The agent is amnesiac, but the filesystem is not.

The broader lesson is that long-running agent systems need durable state, resumable checkpoints, explicit task ledgers, structured artifacts, external verification, and recovery mechanisms. Asking the model “are you done?” is not enough; test suites, linters, acceptance checks, logs, and human review loops must provide the grounding.
