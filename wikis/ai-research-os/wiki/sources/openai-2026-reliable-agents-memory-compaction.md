---
title: "OpenAI — Reliable Agents with Memory and Compaction"
date_created: 2026-05-07
date_modified: 2026-05-07
summary: "OpenAI Cookbook example separating compaction for current long-running runs from memory for reusable lessons across future sandbox-agent runs."
tags: [openai-agents-sdk, memory, compaction, reliable-agents]
type: source
status: final
---

# OpenAI — Reliable Agents with Memory and Compaction

**Type:** article
**Date:** 2026-05-06
**URL/Source:** https://developers.openai.com/cookbook/examples/agents_sdk/building_reliable_agents_memory_compaction
**Raw file:** [[../raw/articles/2026-05-06-openai-building-reliable-agents-memory-compaction.md]]
**Concepts:** [[concepts/memory-compaction]], [[concepts/sandbox-agents]], [[concepts/evidence-review-agents]]
**Entities:** [[entities/openai]], [[entities/openai-agents-sdk]]

## Summary

OpenAI’s Cookbook example uses a synthetic compliance investigation to demonstrate a reliability pattern for long-running agents: keep the active run viable with compaction, but store only reusable workflow lessons in memory. The agent works inside a controlled sandbox workspace containing policy documents, exception notes, audit follow-ups, approval records, remediation plans, a manifest, and an output directory. Instead of pasting every document into the prompt, the application gives the agent filesystem and shell tools, a bounded workspace, and a final memo target that remains the human-reviewed source of truth.

The most important distinction is what each persistence layer is allowed to carry. Compaction summarizes the active conversation and working state so the same review can continue after context growth. Memory persists generalized habits such as checking the manifest first, preserving uncertainty, or tracking superseded assumptions; it should not store case-specific investigation conclusions. The notebook disables tracing by default for Zero Data Retention-sensitive environments and sets live model execution off by default, making it inspectable without credentials. For Self-OS, this article reinforces a useful architecture for wiki research, Night Shift agents, QA loops, and daily briefs: raw evidence stays separate, compacted task state is temporary, final artifacts are reviewable, and durable memory is reserved for reusable process lessons.

## Key takeaways

- Compaction and memory solve different problems and should not be merged into one persistence bucket.
- Sandbox manifests let agents work over file workspaces while preserving provenance and output reviewability.
- Final human-reviewed artifacts, not agent memory, should remain the source of truth for case-specific conclusions.

## Compilation notes

Compiled from `raw/articles/2026-05-06-openai-building-reliable-agents-memory-compaction.md` during the 2026-05-07 wiki compile. The raw capture remains the canonical source for exact excerpts, links, figures, and code.
