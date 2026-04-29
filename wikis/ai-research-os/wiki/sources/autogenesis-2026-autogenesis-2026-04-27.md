---
title: "Autogenesis: A Self-Evolving Agent Protocol"
date_created: 2026-04-29
date_modified: 2026-04-29
summary: "Autogenesis: A Self-Evolving Agent Protocol captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, s"
tags: [agent-orchestration]
type: source
status: final
---

# Autogenesis: A Self-Evolving Agent Protocol

**Type:** repo  
**Date:** 2026-04-27  
**URL:** https://arxiv.org/abs/2604.15034  
**Raw file:** [[../../raw/repos/autogenesis-2026-04-27.md]]

**Summary:** Autogenesis: A Self-Evolving Agent Protocol captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-offs that can be compared against the rest of the AI Research OS corpus. Autogenesis: A Self-Evolving Agent Protocol Authors: Wentao Zhang, Zhe Zhao, Haibin Wen, Yingcheng Wu, Ming Yin, Bo An, Mengdi Wang Recent advances in LLM-based agent systems have shown promise in tackling complex, long-horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under-specify cross-entity lifecycle and context management, version tracking, and evolution-safe update interfaces, which encourages monolithic compositions and brittle glue code. We introduce Autogenesis Protocol (AGP), a self-evolution protocol that decouples what evolves from how evolution occurs: - RSPL (Resource Substrate Protocol Layer): Models prompts, agents, tools, environments, and memory as protocol-registered resources with explicit state, lifecycle, and versioned interfaces. - SEPL (Self Evolution Protocol Layer): Specifies a closed-loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback. Building on AGP, we present Autogenesis System (AGS), a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. Evaluated on multiple challenging benchmarks…

**Key contributions:**
- Autogenesis: A Self-Evolving Agent Protocol
- Authors: Wentao Zhang, Zhe Zhao, Haibin Wen, Yingcheng Wu, Ming Yin, Bo An, Mengdi Wang
- We introduce Autogenesis Protocol (AGP), a self-evolution protocol that decouples what evolves from how evolution occurs:
- - RSPL (Resource Substrate Protocol Layer): Models prompts, agents, tools, environments, and memory as protocol-registered resources with explicit state, lifecycle, and versioned interfaces.
- - SEPL (Self Evolution Protocol Layer): Specifies a closed-loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback.

**Related concepts:** [[concepts/agent-orchestration]]  
**Primary entity:** [[entities/autogenesis]]

**Tags:** agent-orchestration
