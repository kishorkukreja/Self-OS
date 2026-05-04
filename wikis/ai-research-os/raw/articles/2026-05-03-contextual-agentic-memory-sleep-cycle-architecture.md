---
source: user-provided framework
date: 2026-05-03
type: article
tags: [agentic-memory, skill-embeddings, sleep-cycle-architecture, self-improving-agents, adapter-distillation]
status: processed
---

# Contextual Agentic Memory — Sleep-Cycle Architecture with Skill Embeddings

## Context

Architecture for agentic memory systems that avoids two failure modes — pure retrieval (experience → retrieval, no abstraction) and aggressive weight updates (experience → full model update). The missing middle is a promotion ladder that compresses episodes into skills, organizes skills via embeddings, abstracts to meta-skills, and selectively internalizes via small adapters. Skill embeddings are the connective tissue that makes cross-skill learning possible.

## Decisions/Findings

- Core promotion ladder: Raw Episodes → Skill Cards → Skill Embeddings → Skill Graph → Meta-Skills → Distilled Adapters → Merged Adapters → Full Model Consolidation. Nothing jumps directly from episode to weights.
- Episode triage gates promotion: importance = novelty × recurrence × success_failure_signal × user_value. Only high-value episodes advance.
- Skill cards are the atomic semantic unit — structured YAML with trigger, procedure, failure_modes, source_episodes.
- Skill embeddings are multi-faceted vectors per skill: semantic, procedural, domain, failure_mode, tool_affinity, adapter_affinity, co_activation. Without embeddings skills are isolated notes; with them they become comparable and cluster-able.
- Skill graph encodes typed relationships: special_case_of, often_used_with, conflicts_with, implemented_by, requires, supersedes. Makes skill relationships machine-navigable.
- Meta-skills emerge from embedding clusters — e.g., api_rate_limit_recovery + db_lock_retry + network_retry → adaptive_recovery_from_transient_failures. This is the layer between skill cards and adapters.
- Cross-adapter learning uses skill clusters to decide consolidation strategy: Option A = adapter router (retrieval-like), Option B = merged adapter via distillation, Option C = hyper-adapter generator (task → adapter weights).
- Distillation trains small adapters/policy heads/routers from episodes + skill cards + meta-skills + adapter traces + human corrections. Base model untouched.
- Every promoted artifact requires: version, source_episodes, eval_score, known_risks, rollback_path, expiry_date.
- Safety gates before any promotion: benchmark improvement, regression tests, user preference alignment, conflict scan, rollback path.

## Open

- Skill graph update policy: co-activation edges (often_used_with) should update online (just counters); structural edges (special_case_of, supersedes) should remain sleep-gated. Decision point before implementation.
- Hyper-adapter generator (Option C) assumes stable task embedding space. Needs degradation path if task distribution shifts — either periodic re-training or fallback to Option A. Not yet specified in architecture.
