---
title: "GBrain — Garry Tan's Opinionated Agent Brain"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Open-source agent brain built on Bun with hybrid search, code intelligence, and automatic typed-link extraction, compatible with OpenClaw and Hermes Agent."
tags: [agent-brain, knowledge-engine, search, retrieval, openclaw, hermes-agent, code-intelligence]
type: source
status: final
---

# GBrain — Garry Tan's Opinionated Agent Brain

**Type:** repo
**Date:** 2026-04-26
**URL:** https://github.com/garrytan/gbrain
**Raw file:** [[../../raw/repos/gbrain-2026-04-26.md]]

**Summary:** GBrain is Garry Tan's open-source agent brain built on Bun with a pluggable dual-engine architecture (embedded PGLite or Postgres/Supabase). It stores markdown and code pages as compiled truth plus an append-only timeline, with automatic typed-link extraction (works_at, advises, founded, invested_in, attended, mentions). Search uses a hybrid pipeline fusing pgvector HNSW cosine similarity, chunk-grain tsvector FTS, and Reciprocal Rank Fusion, with source-aware ranking boosting curated originals and damping chat noise. Code intelligence features include tree-sitter chunking for 29 languages, call-graph edge capture, and two-pass structural retrieval. The BrainBench evaluation harness demonstrates strong retrieval performance on a 240-page prose corpus.

**Key contributions:**
- Hybrid search pipeline (pgvector + tsvector + RRF) with source-aware ranking
- Automatic typed-link extraction from unstructured text
- Code intelligence: tree-sitter chunking, call-graph edges, structural retrieval
- Pluggable storage: embedded PGLite or remote Postgres/Supabase
- BrainBench evaluation harness with 145 relational queries

**Tags:** agent-brain, knowledge-engine, search, retrieval, openclaw, hermes-agent, code-intelligence
