---
title: "SkillClaw: Let Skills Evolve Collectively with Agentic Evolver"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Framework for collective skill evolution in multi-user agent ecosystems, using aggregated session trajectories and an autonomous evolver to refine and create skills continuously."
tags: [skill-evolution, multi-agent, llm-agents, openclaw, knowledge-compounding]
type: source
status: final
---

# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

**Type:** paper
**Date:** 2026-04-12
**URL:** https://arxiv.org/abs/2604.08377
**Authors:** Ziyu Ma, Shidong Yang, Yuxiang Ji, Xucong Wang, Yong Wang, Yiming Hu, Tongwen Huang, Xiangxiang Chu (DreamX Team)
**Raw file:** [[../../raw/papers/2026-04-12-ma-skillclaw.md]]

**Summary:** Ma et al. present **SkillClaw**, a framework that enables skills to evolve collectively across multi-user agent ecosystems. Current agent skills remain static after deployment, forcing users to repeatedly rediscover solutions. SkillClaw aggregates session trajectories from independent agents, groups them by referenced skills, and processes them through an **agentic evolver** that identifies recurring patterns and translates them into skill updates — refining existing skills or creating new ones. Updated skills are validated in idle environments during nighttime and synchronized across all agents. Experiments on WildClawBench over 6 days show consistent gains: Social Interaction improves 11.7%, Search & Retrieval 52%, Creative Synthesis 88.4%, and Safety & Alignment 33.3%. The system is compatible with OpenClaw and variants including CoPaw, IronClaw, and NemoClaw.

**Key contributions:**
- Collective evolution: cross-user knowledge transfer into a shared, continuously improving skill ecosystem
- Fully automatic pipeline from session recording to skill synchronization without user intervention
- Agentic evolver using open-ended reasoning over evidence rather than predefined rules
- Monotonic deployment: only validated improvements are accepted, preventing skill degradation
- Compatible with multiple Claw-style agent systems

**Tags:** skill-evolution, multi-agent, llm-agents, openclaw, knowledge-compounding
