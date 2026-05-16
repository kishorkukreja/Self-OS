---
title: "Agent Memory"
date_created: 2026-04-27
date_modified: 2026-05-16
summary: "Systems that enable agents to store, retrieve, and learn from historical experiences to improve future reasoning and planning."
tags: ['agent-memory', 'deep-research', 'parametric-memory', 'memory-system']
type: concept
status: draft
confidence: emerging
source_count: 3
---

# Agent Memory

**Agent memory** encompasses both non-parametric (retrieval-based) and parametric (model-weight-based) mechanisms for leveraging historical experience. In deep research agents, memory must capture not only factual results but also process knowledge: how tasks were solved, what strategies succeeded or failed, and how plans were adapted. MIA proposes a Manager-Planner-Executor architecture that explicitly separates episodic memory storage from parametric planning, enabling test-time learning without interrupting inference.

Key dimensions:
- **Non-parametric memory:** Stored trajectories retrieved by similarity, quality, and frequency.
- **Parametric memory:** Knowledge distilled into model weights via reinforcement learning.
- **Bidirectional conversion:** Trajectories are compressed into workflows, which are then used to update the Planner's policy.

_Last updated: 2026-05-09_

## Update — 2026-05-01
Architectures and benchmarks for retaining, retrieving, and evaluating persistent context across agent interactions. New supporting source: [[sources/x-blogs-digest-2026-04-30.md]].

_Last updated: 2026-05-09_

## Update — 2026-05-02

[[sources/x-blogs-digest-2026-05-01.md]] adds LifelongAgentBench as another benchmark focused on whether agents can accumulate and transfer knowledge across interdependent tasks. The reported weakness of naive experience replay reinforces the existing wiki theme that memory systems need retrieval discipline, compression, and task relevance rather than unfiltered transcript replay.

## 2026-05-09 — Dreams and persistent coding-agent context

The Claude Code platform video introduces Dreams memory as a signal that durable memory is becoming a product-level agent capability. For Self-OS, this mirrors the same pattern in raw captures, wiki compaction, and skills: agent systems need a deliberate memory layer that survives sessions without leaking irrelevant context into every task.

**Sources:** [[sources/claire-vo-2026-claude-code-agent-platform.md]]

## 2026-05-09 — Local-first knowledge graph memory

Rowboat adds a concrete reference for local-first agent memory. It stores working context as an Obsidian-compatible Markdown vault with backlinks, then uses that graph of people, projects, decisions, commitments, and topics to generate meeting briefs, emails, documents, plans, and decks. The source reinforces that memory should be inspectable, editable, portable, and tied to action workflows.

**Sources:** [[sources/rowboat-2026-local-first-ai-coworker.md]]

## Evidence from SkillOS: Learning Skill Curation for Self-Evolving Agents (2026-05-13)

- [[sources/skillos-learning-skill-curation-for-self-evolving-agents-2026-05-12.md|SkillOS: Learning Skill Curation for Self-Evolving Agents]] adds another signal for **Agent Memory** in this wiki. The source is useful primarily as retrieval context and should be interpreted alongside earlier evidence before promoting broad claims.

## Evidence from Hermes Agent — Use Case Patterns and Self-OS Strategic Applications (2026-05-13)

- [[sources/hermes-agent-use-case-patterns-and-self-os-strategic-applications-2026-05-13.md|Hermes Agent — Use Case Patterns and Self-OS Strategic Applications]] adds another signal for **Agent Memory** in this wiki. The source is useful primarily as retrieval context and should be interpreted alongside earlier evidence before promoting broad claims.

## Evidence from Hermes Agent — User Stories & Use Cases (2026-05-13)

- [[sources/hermes-agent-user-stories-and-use-cases-2026-05-12.md|Hermes Agent — User Stories & Use Cases]] adds another signal for **Agent Memory** in this wiki. The source is useful primarily as retrieval context and should be interpreted alongside earlier evidence before promoting broad claims.

## Evidence from X/Twitter AI Blogs and Articles — 2026-05-12 (2026-05-13)

- [[sources/x-twitter-ai-blogs-and-articles-2026-05-12-2026-05-12.md|X/Twitter AI Blogs and Articles — 2026-05-12]] adds another signal for **Agent Memory** in this wiki. The source is useful primarily as retrieval context and should be interpreted alongside earlier evidence before promoting broad claims.

## Evidence from Garry Tan: Meta-Meta-Prompting — The Secret to Making AI Agents Work (2026-05-13)

- [[sources/garry-tan-meta-meta-prompting-the-secret-to-making-ai-agents-work-2026-05-12.md|Garry Tan: Meta-Meta-Prompting — The Secret to Making AI Agents Work]] adds another signal for **Agent Memory** in this wiki. The source is useful primarily as retrieval context and should be interpreted alongside earlier evidence before promoting broad claims.

## 2026-05-16 update

The ADK article distinguishes durable workflow state from raw transcript memory, reinforcing compact state over prompt replay. Source: [[sources/google-2026-long-running-agents-adk.md|Agent Memory]].

_Last updated: 2026-05-16_
