---
title: OpenHarness — Open Agent Harness with Built-in Personal Agent Ohmo
date_created: '2026-05-05'
date_modified: '2026-05-05'
summary: OpenHarness is a broad Python harness for tool use, skills, memory, plugin
  compatibility, permissions, multi-agent coordination, and a personal-agent application
  called Ohmo. Its significance for Self-OS is architectural
tags:
- ai-agents
- agent-harness
- personal-agent
- skills
- memory
- multi-agent
- github-repo
type: source
status: final
tags: [wiki, maintenance]
---

# OpenHarness — Open Agent Harness with Built-in Personal Agent Ohmo

**Type:** repo  
**Date:** 2026-05-04  
**URL:** https://github.com/HKUDS/OpenHarness  
**Raw file:** [[../raw/repos/openharness-2026-05-04.md]]

## Summary
OpenHarness is a broad Python harness for tool use, skills, memory, plugin compatibility, permissions, multi-agent coordination, and a personal-agent application called Ohmo. Its significance for Self-OS is architectural: the project treats the harness as the agent’s operational substrate, providing hands, eyes, memory, safety boundaries, and chat/platform integrations around an LLM. The repository is directly adjacent to Hermes because it combines gateway-style usage, skills, permissions, compression, and memory into one open personal-agent stack. It is a useful comparison point for deciding which capabilities belong in the core harness versus as plugins or wiki-maintained skills.

## Key contributions
- Combines tool calls, skills, plugins, memory, permissions, and platform integrations.
- Provides a personal-agent app, Ohmo, as a concrete harness product.
- Offers a comparison point for Hermes/Self-OS architecture and governance boundaries.

## Linked concepts and entities
- Concepts: [[concepts/agent-harness-engineering]], [[concepts/agent-memory]], [[concepts/agent-skills]]
- Entities: [[entities/openharness]], [[entities/ohmo]]

**Tags:** ai-agents, agent-harness, personal-agent, skills, memory, multi-agent, github-repo
