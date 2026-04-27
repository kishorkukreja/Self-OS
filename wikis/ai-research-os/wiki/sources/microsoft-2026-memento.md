---
title: "Memento — Extending LLM Output Length via KV Cache Compaction"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Microsoft research project that extends effective LLM output length by splitting chain-of-thought into blocks and summaries, evicting blocks from KV cache after summarisation."
tags: [context-compression, chain-of-thought, kv-cache, long-context, microsoft]
type: source
status: final
---

# Memento — Extending LLM Output Length via KV Cache Compaction

**Type:** repo
**Date:** 2026-04-13
**URL:** https://github.com/microsoft/memento
**Raw file:** [[../../raw/repos/memento-2026-04-13.md]]

**Summary:** Memento is a Microsoft research project that extends the effective output length of large language models by splitting chain-of-thought reasoning into blocks and summaries (mementos). After each reasoning block, the model generates a short summary; the block content is then evicted from the KV cache, allowing the model to continue from the summary with a shorter context. This enables more reasoning steps within a fixed context window. The repository includes a data pipeline that converts raw CoT traces into Memento-formatted training data, and a vLLM overlay adding KV cache block masking for efficient inference.

**Key contributions:**
- Block-and-summary pattern for KV cache compaction during chain-of-thought
- Special token structure for block boundaries and summary delimiters
- Data pipeline for converting CoT traces into SFT training data
- vLLM overlay with block masking for efficient Memento inference
- Enables longer effective output without increasing model context size

**Tags:** context-compression, chain-of-thought, kv-cache, long-context, microsoft
