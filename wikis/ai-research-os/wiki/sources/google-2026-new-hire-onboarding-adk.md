---
title: "Google ADK New Hire Onboarding Example"
date_created: 2026-05-16
date_modified: 2026-05-16
summary: "The Google ADK new-hire onboarding repo turns the durable-agent architecture into a runnable reference implementation. It uses a coordinator agent, persistent sessions, FastAPI, a "
tags: [google-adk, long-running-agents, human-in-the-loop, state-machines]
type: source
status: final
---

# Google ADK New Hire Onboarding Example

**Type:** repo  
**Date:** 2026-05-15  
**URL:** https://github.com/GoogleCloudPlatform/generative-ai/tree/main/agents/adk/new-hire-onboarding  
**Raw file:** [[../raw/repos/new-hire-onboarding-2026-05-15.md]]

## Summary

The Google ADK new-hire onboarding repo turns the durable-agent architecture into a runnable reference implementation. It uses a coordinator agent, persistent sessions, FastAPI, a React cockpit, and an explicit onboarding state machine to manage a workflow that pauses for signed documents and hardware delivery. The key engineering lesson is that progress is not inferred from chat history or UI optimism; state advances only after backend ADK resume turns complete.

This is especially relevant to Self-OS because many useful automations are long-running operations with human gates: wiki compile PR review, research request fulfillment, supply-chain signal monitoring, and coding-agent handoffs. The repo demonstrates a pattern for combining a human-facing cockpit with backend event resumes and delegated sub-workflows. Rather than asking a model to remember everything, the system stores compact states and artifacts, wakes the agent from verified events, and routes specialist work to narrower components. It is a concrete implementation reference for converting Hermes cron jobs into durable, inspectable operating workflows.

## Key contributions
- The repository implements a state-machine-based onboarding coordinator using Google ADK.
- Human-in-the-loop gates are handled by pause/resume events rather than blocked execution.
- The demo connects durable backend state to a visible HR and employee cockpit.

**Tags:** google-adk, long-running-agents, human-in-the-loop, state-machines
