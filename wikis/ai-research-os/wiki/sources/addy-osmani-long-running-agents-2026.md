---
title: "Addy Osmani — Long-running Agents"
date_created: 2026-04-30
date_modified: 2026-04-30
summary: "Addy Osmani's article frames long-running agents as AI systems that can keep making progress over hours, days, or weeks across many context windows and sandboxes. The core claim is that the hard part is not only model in"
tags: [agents, long-running-agents, agent-harnesses, persistent-state, verification, ai-engineering]
type: source
status: final
---

# Addy Osmani — Long-running Agents

**Type:** article  
**Date:** 2026-04-29  
**URL:** https://addyosmani.com/blog/long-running-agents/?utm_source=tldrnewsletter  
**Raw file:** [[../raw/articles/2026-04-29-addy-osmani-long-running-agents.md]]

**Summary:** Addy Osmani's article frames long-running agents as AI systems that can keep making progress over hours, days, or weeks across many context windows and sandboxes. The core claim is that the hard part is not only model intelligence, but externalized state, recovery, verification, artifacts, and reliable handoffs. The article separates long-running agents into long-horizon reasoning, long-running execution, and persistent agency, then argues that production systems usually need all three.
The article is highly relevant to agentic engineering because it treats agents as operational systems rather than chat sessions. It covers finite context, context rot, lack of persistent state, weak self-verification, the Ralph loop, memory-bank patterns, task ledgers, progress logs, and verifier-driven loops that let agents resume safely rather than repeatedly starting from scratch.

**Key contributions:**
- A long-running AI agent can make progress over hours, days, or weeks across context windows and sandboxes, recover from failure, leave structured artifacts, and resume where it left off.
- “Long-running” combines three ideas: long-horizon reasoning, long-running execution, and persistent agency.
- METR's time-horizon framing measures the length of tasks frontier models can complete with 50% reliability; Osmani notes the horizon has been doubling roughly every seven months since 2019.
- The three major walls are finite context, lack of persistent state, and poor self-verification.
- Context windows are not enough; context rot degrades performance before hard limits are reached.
- The Ralph loop externalizes state into files such as prd.json, progress.txt, and AGENTS.md, allowing an amnesiac model to continue via a persistent filesystem.

**Tags:** agents, long-running-agents, agent-harnesses, persistent-state, verification, ai-engineering
