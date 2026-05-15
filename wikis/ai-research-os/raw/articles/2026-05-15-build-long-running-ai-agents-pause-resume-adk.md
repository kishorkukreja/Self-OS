---
source: https://developers.googleblog.com/build-long-running-ai-agents-that-pause-resume-and-never-lose-context-with-adk/
date: 2026-05-15
type: article
tags: [google-adk, long-running-agents, durable-agent-state, event-driven-agents, agent-runtime, agents-cli, multi-agent-orchestration, self-os]
---

# Build Long-running AI Agents That Pause, Resume, and Never Lose Context with ADK

## Summary

This Google Developers Blog article explains how to build long-running AI agents with Google’s Agent Development Kit (ADK). The central claim is that real enterprise workflows do not fit the stateless chatbot pattern: they span days or weeks, wait on human actions or real-world events, and need to survive crashes, cold starts, and scale-to-zero periods. The example is a New Hire Onboarding Coordinator Agent that sends a welcome packet, pauses until paperwork is signed, delegates IT provisioning, pauses again for laptop delivery, and then sends a day-one schedule.

The article’s most important architectural idea is that reliable agents need explicit durable state, event-driven dormancy gates, and multi-agent delegation. Bigger context windows are not the solution to long-running workflows; explicit state and resumable workflow design are.

## Key points

- Stateless chatbots fail when workflows stretch across idle time, human approvals, and external dependencies.
- Replaying entire conversation histories causes prompt pollution, token-cost explosion, and hallucinated reasoning after long pauses.
- Durable agents should persist compact workflow state, not raw chat logs.
- Event-driven resumption is preferable to blocked threads or active polling.
- Multi-agent delegation keeps specialist workflows isolated and prevents coordinator prompts from becoming overloaded.
- The companion repository demonstrates these ideas with a Google ADK new-hire onboarding workflow.

## Architectural thesis

The article argues that long-running agents need a fundamentally different architecture from chatbots:

> The fix isn’t a bigger context window. It’s a fundamentally different architecture — one where the agent’s state is explicit, durable, and decoupled from raw chat history.

The new-hire onboarding example has several real-world discontinuities:

1. HR sends onboarding materials.
2. The system waits while the new hire signs documents.
3. IT provisions accounts and tools.
4. The system waits while hardware is shipped.
5. HR sends a day-one schedule.

A stateless chatbot cannot reliably infer this process state after days of inactivity. A durable agent can resume because it reads the exact persisted state of the workflow.

## Three production patterns

### 1. Durable memory schemas

The agent should store a compact state model that captures the current workflow step, completed gates, outstanding dependencies, and relevant artifacts. This avoids asking the model to reconstruct reality from stale conversational transcripts.

### 2. Event-driven dormancy gates

Long-running workflows should go dormant while waiting on outside events. They should resume from external signals such as a webhook, a user action, or a verified state transition. This is cheaper and safer than polling or keeping a thread blocked.

### 3. Multi-agent delegation

The coordinator should delegate specialized work to sub-agents rather than accumulating every tool and responsibility in one monolithic prompt. In the onboarding example, IT provisioning can be handled as a separate delegated workflow.

## Example workflow

The onboarding agent can:

- send a welcome packet,
- pause for document signatures,
- resume from persisted state,
- delegate IT provisioning,
- pause while hardware ships,
- resume after delivery confirmation,
- and generate a personalized day-one schedule.

The same pattern is applicable to procurement approvals, invoice dispute resolution, compliance audits, sales sequences, vendor onboarding, and any process where much of the elapsed time is waiting for humans or external systems.

## Related project

Companion repository:

```text
https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/new-hire-onboarding
```

The repository includes a FastAPI + React demo UI and an ADK implementation of the onboarding coordinator.

## Why it matters

This article is a useful conceptual reference for **agent operating systems**. It separates agent reliability from chat-memory tricks and defines a more production-grade model: explicit durable state, event-driven wakeups, and scoped delegation. That maps strongly to Self-OS/Hermes workflows, where many tasks are not single-turn interactions but multi-step operating loops with human review gates and delayed external evidence.

## Self-OS / Hermes implications

- Convert recurring workflows into stateful procedures with named phases, not loose prompt chains.
- Persist compact task state in markdown/JSON files where needed: current phase, source evidence, pending external event, last verified artifact, next human decision.
- For scheduled work, distinguish “cron fired” from “workflow state advanced”; a job should only advance after evidence is verified.
- Use Telegram as a reporting surface, but keep the source of truth in durable markdown/git state.
- For wiki research, newsletters, coding-agent handoffs, and PR review, define explicit pause/resume gates and human approval states.
- This supports the existing Self-OS direction: minimal durable operating loop first, dashboard only later if it serves verified state rather than vibes.

## Raw content notes

The article identifies several failure modes of stateless agent design:

- **Prompt context pollution:** irrelevant old chatter, duplicated instructions, and stale tool outputs crowd out the current decision.
- **Token cost explosion:** replaying weeks of conversation history on every turn becomes expensive.
- **Hallucinated reasoning after idle time:** the model may assume approvals happened, documents were signed, or steps were completed when they were not.

It recommends durable session variables and explicit state machines as the correct remedy. The article also references Google’s Agents CLI and Agent Runtime as supporting infrastructure for building, evaluating, and deploying these ADK agents.
