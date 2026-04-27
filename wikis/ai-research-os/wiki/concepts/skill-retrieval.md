---
title: "Skill Retrieval"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Methods for selecting relevant agent skills from large libraries at inference time, balancing relevance with dependency completeness."
tags: ['skill-retrieval', 'agent-skills', 'graph', 'efficiency']
type: concept
status: draft
confidence: emerging
source_count: 2
---

# Skill Retrieval

**Skill retrieval** is the problem of selecting a compact, executable subset of skills from a large library when an agent receives a task query. Flat approaches (loading the full library) waste context and increase latency, while simple vector retrieval may miss functionally required prerequisites. [[Graph of Skills]] addresses this by constructing a typed skill graph and using reverse-weighted Personalized PageRank to recover dependency-complete bundles.

Key tradeoffs:
- **Relevance vs. sufficiency:** The top-k semantically similar skills may not include necessary prerequisites.
- **Context budget:** Retrieved bundles must fit within the LLM's prompt window.
- **Structural awareness:** Dependency edges between skills encode execution requirements that pure semantic similarity cannot capture.

_Last updated: 2026-04-27_
