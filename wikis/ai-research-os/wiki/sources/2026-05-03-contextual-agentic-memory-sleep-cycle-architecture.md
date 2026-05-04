---
title: "Contextual Agentic Memory Sleep Cycle Architecture"
date_created: 2026-05-04
date_modified: 2026-05-04
summary: "Contextual Agentic Memory — Sleep-Cycle Architecture with Skill Embeddings Context Architecture for agentic memory systems that avoids two failure modes — pure retrieval experience → retrieval, no abstraction and aggress"
tags: [agentic-memory, skill-embeddings, sleep-cycle-architecture, self-improving-agents, adapter-distillation]
type: source
status: final
---

# Contextual Agentic Memory Sleep Cycle Architecture

**Type:** article
**Date:** 2026-05-03
**URL/Source:** user-provided framework
**Raw file:** [[../raw/articles/2026-05-03-contextual-agentic-memory-sleep-cycle-architecture.md]]
**Concepts:** [[concepts/agentic-memory.md]], [[concepts/skill-embeddings.md]], [[concepts/sleep-cycle-architecture.md]], [[concepts/self-improving-agents.md]], [[concepts/adapter-distillation.md]]

## Summary

Contextual Agentic Memory — Sleep-Cycle Architecture with Skill Embeddings Context Architecture for agentic memory systems that avoids two failure modes — pure retrieval experience → retrieval, no abstraction and aggressive weight updates experience → full model update . The missing middle is a promotion ladder that compresses episodes into skills, organizes skills via embeddings, abstracts to meta-skills, and selectively internalizes via small adapters. Skill embeddings are the connective tissue that makes cross-skill learning possible. Decisions/Findings - Core promotion ladder: Raw Episodes → Skill Cards → Skill Embeddings → Skill Graph → Meta-Skills → Distilled Adapters → Merged Adapters → Full Model Consolidation. Nothing jumps directly from episode to weights. - Episode triage gates promotion: importance = novelty × recurrence × success failure signal × user value. Only high-value episodes advance. - Skill cards are the atomic semantic unit — structured YAML with trigger, procedure, failure modes, source episodes. - Skill embeddings are multi-faceted vectors per skill: semantic, procedural, domain, failure mode, tool affinity, adapter affinity, co activation. Without embeddings skills are isolated notes; with them they become comparable and cluster-able. - Skill graph encodes typed relationships: special case of, often used with, conflicts with, implemented by, requires, supersedes. Makes skill relationships machine-navigable. - Meta-skills emerge from embedding clusters — e.g., api rate limit recovery + db lock retry + network retry → adaptive recovery from transient failures. This is the layer between skill cards and adapters. - Cross-adapter learning uses skill clusters to decide consolidation strategy: Option A = adapter router retrieval-like , Option B = merged adapter via distillation, Option C = hyper-adapter generator task → adapter weights . - Distillation trains small adapters/policy heads/routers from episodes + skill cards + meta-skills + adapter traces + human corrections. Base model untouched. - Every promoted artifact requires: version, source episodes, eval score, known risks, rollback path, expiry date. - Safety gates before any promotion: benchmark improvement, regression tests, user preference alignment, conflict scan, rollback path. Open - Skill graph update policy: co-activation edges often used with should update online just counters ; structural edges special case of, supersedes should remain sleep-gated. Decision point before implementation. - Hyper-adapter generator Option C

## Key takeaways

- Contextual Agentic Memory — Sleep-Cycle Architecture with Skill Embeddings Context Architecture for agentic memory systems that avoids two failure modes — pure retrieval experience → retrieval, no abstraction and aggressive weight updates experience → full model update .
- The missing middle is a promotion ladder that compresses episodes into skills, organizes skills via embeddings, abstracts to meta-skills, and selectively internalizes via small adapters.
- Skill embeddings are the connective tissue that makes cross-skill learning possible.
- Decisions/Findings - Core promotion ladder: Raw Episodes → Skill Cards → Skill Embeddings → Skill Graph → Meta-Skills → Distilled Adapters → Merged Adapters → Full Model Consolidation.

## Compilation notes

Compiled from `raw/articles/2026-05-03-contextual-agentic-memory-sleep-cycle-architecture.md` during the 2026-05-04 wiki compile. The raw capture remains the canonical source for exact excerpts, links, figures, and context.
