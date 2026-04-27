---
title: "SkillClaw — Skill Collective Evolution Framework"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Framework for evolving reusable skills in multi-user OpenClaw-style agent ecosystems by automatically distilling session experience into shared SKILL.md files."
tags: [skill-evolution, multi-agent, llm-agents, openclaw, knowledge-compounding]
type: source
status: final
---

# SkillClaw — Skill Collective Evolution Framework

**Type:** repo
**Date:** 2026-04-12
**URL:** https://github.com/AMAP-ML/SkillClaw
**Raw file:** [[../../raw/repos/skillclaw-2026-04-12.md]]

**Summary:** SkillClaw is a framework for skill collective evolution in multi-user OpenClaw-style agent ecosystems. It automatically distills real-world experience from multiple users and agents into reusable SKILL.md files, sharing them via cloud storage to enable continuous evolution across the entire agent cluster. The system comprises three interchangeable components: a Client Proxy that intercepts agent requests and records session artifacts; a Workflow Evolve Server that runs a fixed three-stage LLM pipeline (Summarise → Aggregate → Execute); and an Agent Evolve Server that uses an autonomous OpenClaw agent to analyse patterns and write evolved skill files. Evaluated on WildClawBench, SkillClaw improves Qwen3-Max performance under limited group interaction without requiring a larger model.

**Key contributions:**
- Automatic skill distillation from real session data in the background
- Three-component architecture (Client Proxy, Workflow Evolve Server, Agent Evolve Server)
- Support for multiple Claw frameworks (CoPaw, IronClaw, PicoClaw, ZeroClaw, NanoClaw, NemoClaw)
- Cloud-backed skill synchronisation via Alibaba OSS, S3, or local filesystem
- WildClawBench evaluation demonstrating experience-driven improvement

**Tags:** skill-evolution, multi-agent, llm-agents, openclaw, knowledge-compounding
