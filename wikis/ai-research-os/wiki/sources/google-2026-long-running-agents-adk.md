---
title: "Build Long-running AI Agents That Pause, Resume, and Never Lose Context with ADK"
date_created: 2026-05-16
date_modified: 2026-05-16
summary: "Google’s ADK article reframes production agents as durable workflow coordinators rather than stateless chatbots. Its onboarding example waits across document signing, IT provisioni"
tags: [google-adk, long-running-agents, durable-agent-state, event-driven-agents, self-os]
type: source
status: final
---

# Build Long-running AI Agents That Pause, Resume, and Never Lose Context with ADK

**Type:** article  
**Date:** 2026-05-15  
**URL:** https://developers.googleblog.com/build-long-running-ai-agents-pause-resume-and-never-lose-context-with-adk/  
**Raw file:** [[../raw/articles/2026-05-15-build-long-running-ai-agents-pause-resume-adk.md]]

## Summary

Google’s ADK article reframes production agents as durable workflow coordinators rather than stateless chatbots. Its onboarding example waits across document signing, IT provisioning, hardware delivery, and day-one scheduling, which makes raw transcript replay a poor continuity mechanism. The useful design move is to persist compact workflow state: current phase, completed gates, outstanding dependencies, and artifacts. This reduces prompt pollution and makes resumption auditable after cold starts, crashes, or multi-day delays.

For Self-OS and Hermes, the article is a strong architectural signal. Recurring jobs such as wiki research, newsletter production, operating briefs, and coding-agent handoffs should be modeled as state machines with event-driven wakeups, not as ever-growing prompts. The article also validates scoped delegation: a coordinator can hand IT provisioning or another specialized subtask to a narrower agent, then resume once the sub-workflow reports completion. The practical lesson is that context durability belongs in explicit state and artifacts, while the model handles local reasoning at each transition.

## Key contributions
- Long-running agent reliability depends on explicit durable state rather than bigger context windows.
- Event-driven dormancy gates let workflows sleep until a verified external event arrives.
- Multi-agent delegation keeps specialized work isolated from the coordinator prompt.

**Tags:** google-adk, long-running-agents, durable-agent-state, event-driven-agents, self-os
