---
title: "Harness vs Warp (Agent Architecture Overview)"
date_created: 2026-05-03
date_modified: 2026-05-03
summary: "Harness vs Warp (Agent Architecture Overview) Capture note: the user supplied the neutral Harness vs Warp summary below and attached the X URL as context/source. Browser extraction of the linked X post surfaced a Google Cloud Tech article a"
tags: [agent-harness, warp, agent-architecture, orchestration, multi-agent-systems, a2a, mcp, google-cloud]
type: source
status: final
---

# Harness vs Warp (Agent Architecture Overview)

**Type:** thread
**Date:** 2026-05-02
**URL/Source:** https://x.com/GoogleCloudTech/status/2047567704807346675
**Raw file:** [[../raw/x-threads/2026-05-02-googlecloudtech-harness-vs-warp-agent-architecture.md]]
**Concepts:** [[concepts/agent-harness]], [[concepts/warp]], [[concepts/agent-architecture]]
**Entities:** [[entities/google-cloud]], [[entities/warp]]

## Summary

Harness vs Warp (Agent Architecture Overview) Capture note: the user supplied the neutral Harness vs Warp summary below and attached the X URL as context/source. Browser extraction of the linked X post surfaced a Google Cloud Tech article about A2A + MCP integration patterns; both are preserved here because they are adjacent concepts in agent architecture and orchestration. User Supplied Wiki Summary Key Concepts Agent harness (e.g. Cursor SDK) A harness is the control layer around an agent: manages the agent loop handles tool execution controls context and memory enables subagents and delegation It turns a model into a fully functioning, programmable agent. Warp (agentic environment + orchestrator) Warp is a terminal based environment with built in agents and orchestration: runs agents locally or in the cloud (via its backend, “Oz”) supports multi agent workflows integrates with codebases and tools provides a UI + execution layer Relationship Between Them A harness and Warp operate at different layers: Harness: Defines how an agent works — loop, tools, reasoning. Warp: Defines how agents are run and coordinated. What Works in Practice You can: build a custom agent using a harness run it independently, locally or as a service invoke it from Warp workflows What Does Not Happen (Currently) Warp does not: act as a neutral host for arbitrary harnesses fully adopt external agent runtimes expose its internal agent loop for replacement Correct Mental Model Harness builds agents. More precisely: Bottom Line Harnesses and Warp are complementary, not interchangeable. Harness: agent construction layer Warp: agent execution + orchestration environment Extracted X / Google Cloud Tech Context Post: Google Cloud Tech, Apr 24 2026 Visible engagement at capture: 17 replies, 91 reposts, 475 likes, 636 bookmarks, 43.6K views The linked X post is a Google Cloud Tech article titled: How A2A and MCP work together: five integration patterns for building multi agent systems The article argues that organizations will not build every agent from scratch. Instead, value comes from discovering and coordinating agents built by different teams, languages, and organizations. It frames A2A as the protocol for agent to agent communication and MCP as the protocol for agent to tool communication. Agent Card Discovery Before an agent can delegate to another agent, it must know that agent exists, what it can do, and how to communicate with it. A2A uses Agent Cards : JSON documents published at well known URLs describing capabilities, authentication requirements, and rate limits. The article compares Agent Cards to OpenAPI specs, but for agent to agent interaction.

## Key takeaways

- runs agents locally or in the cloud (via its backend, “Oz”)
- integrates with codebases and tools
- provides a UI + execution layer
- Harness: Defines how an agent works — loop, tools, reasoning.

## Compilation notes

Compiled from `raw/x-threads/2026-05-02-googlecloudtech-harness-vs-warp-agent-architecture.md` during the 2026-05-03 wiki compile. The raw capture remains the canonical source for exact excerpts, links, and figures.
