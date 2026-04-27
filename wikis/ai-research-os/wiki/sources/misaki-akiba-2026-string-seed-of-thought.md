---
title: "String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "ICLR 2026 paper introducing SSoT, a two-stage prompting method that improves probabilistic instruction following by using random strings as entropy seeds."
tags: [prompting, llm, diversity, probabilistic-instruction-following, generation, iclr-2026]
type: source
status: final
---

# String Seed of Thought: Prompting LLMs for Distribution-Faithful and Diverse Generation

**Type:** paper
**Date:** 2026-04-26
**URL:** https://arxiv.org/abs/2510.21150
**Authors:** Kou Misaki, Takuya Akiba
**Venue:** ICLR 2026
**Raw file:** [[../../raw/papers/2026-04-26-misaki-akiba-string-seed-of-thought.md]]

**Summary:** Misaki and Akiba identify that LLMs struggle with **Probabilistic Instruction Following (PIF)** — tasks requiring the model to select answers from predefined options according to target probabilities. Standard prompting causes bias, diversity collapse, and degraded test-time scaling. Their solution, **String Seed of Thought (SSoT)**, is a remarkably simple two-stage prompt: first instruct the LLM to output a random string to generate entropy, then instruct it to manipulate that string to derive a constrained answer. SSoT approaches ideal pseudo-random performance on PIF benchmarks and generalizes to open-ended tasks via improved response diversity on NoveltyBench.

**Key contributions:**
- Formalizes PIF as a core LLM capability gap with implications for human-behavior simulation, content diversification, and multiplayer games
- SSoT requires no fine-tuning or model changes — purely a prompting strategy
- Demonstrates that diversity preservation and constraint adherence are not mutually exclusive
- Shows benefits extend beyond closed-set PIF to open-ended generation

**Tags:** prompting, llm, diversity, probabilistic-instruction-following, generation, iclr-2026
