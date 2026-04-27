---
title: "Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Preprint introducing GoS, a graph-structured retrieval layer for large skill libraries that uses reverse-weighted Personalized PageRank to recover prerequisite skills missed by flat semantic retrieval."
tags: [agent-skills, skill-retrieval, graph, llm-agents, tool-use, efficiency]
type: source
status: final
---

# Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills

**Type:** paper
**Date:** 2026-04-13
**URL:** https://arxiv.org/abs/2604.05333
**Authors:** Dawei Liu, Zongxia Li, Hongyang Du, Xiyang Wu, Shihang Gui, Yongbei Kuang, Lichao Sun
**Raw file:** [[../../raw/papers/2026-04-13-liu-graph-of-skills.md]]

**Summary:** Liu et al. address the skill retrieval bottleneck in large agent ecosystems. As skill libraries scale to thousands of items, vanilla full-context loading saturates context windows while simple vector retrieval misses functionally necessary prerequisites that are semantically distant. **Graph of Skills (GoS)** constructs a typed directed graph offline from skill packages (dependency, workflow, semantic, and alternative edges), then at inference time retrieves a bounded, dependency-aware bundle via hybrid semantic-lexical seeding and reverse-weighted Personalized PageRank. On SkillsBench and ALFWorld, GoS improves average reward by 43.6% over full-library baselines while reducing input tokens by 37.8%, generalizing across Claude Sonnet, GPT-5.2 Codex, and MiniMax.

**Key contributions:**
- Typed skill graph with four relation types capturing executable structure, not just metadata proximity
- Reverse-aware graph diffusion that recovers prerequisite skills from high-level solver seeds
- Context-budgeted hydration producing compact, execution-complete skill bundles
- Consistent gains across library sizes from 200 to 2,000 skills

**Tags:** agent-skills, skill-retrieval, graph, llm-agents, tool-use, efficiency
