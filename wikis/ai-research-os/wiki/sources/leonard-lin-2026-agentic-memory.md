---
title: "Agentic Memory Research Collection"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Curated research collection by Leonard Lin summarising 30+ academic papers and production systems on agent memory architectures, with deep-dive analyses and cross-system comparisons."
tags: [agent-memory, research-collection, memory-architectures, persistence]
type: source
status: final
---

# Agentic Memory Research Collection

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/lhl/agentic-memory
**Raw file:** [[../../raw/repos/agentic-memory-lhl-2026-04-13.md]]

**Summary:** This repository is a comprehensive research collection on agent memory architectures, persistence patterns, and output quality maintenance for LLM-based agents. Leonard Lin summarises and analyses over 30 academic papers and production systems—including MemGPT, Mem0, SimpleMem, Zep, Nemori, and Hindsight—alongside community implementations like OpenClaw, Karta, and ClawVault. The collection includes both reference summaries and critical deep-dive analyses that evaluate coherence, evidence quality, and operational risks. Key cross-cutting themes include the importance of phased build order, tiered retrieval strategies, score decay for recency weighting, and the operational simplicity of SQLite over hosted vector databases at current scales.

**Key contributions:**
- Summaries of 30+ papers and systems with structured metadata
- Critical analyses evaluating claims against implementation reality
- Cross-system comparison mapping techniques to memory types
- Identification of universal patterns: recency decay, tiered retrieval, feedback loops
- Security deep dives on memory poisoning attacks (MINJA) and defences

**Tags:** agent-memory, research-collection, memory-architectures, persistence, benchmarks
