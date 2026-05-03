---
title: "X/Twitter AI Blogs and Articles — 2026-05-02"
date_created: 2026-05-03
date_modified: 2026-05-03
summary: "Daily digest of AI/ML articles and blog links discovered via X/Twitter search and web search fallback. Key themes this cycle: agent harness engineering , evaluation cost and redundancy , automated AI research systems , MCP based agent evalu"
tags: [x, twitter, blogs, articles, ai-research, daily-digest]
type: source
status: final
---

# X/Twitter AI Blogs and Articles — 2026-05-02

**Type:** article
**Date:** 2026-05-02
**URL/Source:** X/Twitter daily search
**Raw file:** [[../raw/x-blogs/2026-05-02-x-blogs-digest.md]]
**Concepts:** [[concepts/ai-research-discovery]], [[concepts/ai-research]], [[concepts/agent-harness-engineering]]
**Entities:** [[entities/github]], [[entities/openai]]

## Summary

Daily digest of AI/ML articles and blog links discovered via X/Twitter search and web search fallback. Key themes this cycle: agent harness engineering , evaluation cost and redundancy , automated AI research systems , MCP based agent evaluation frameworks , and lifelong/agent benchmarks . X/Twitter remains a primary discovery vector for long form engineering posts and preprint announcements. Harness engineering: leveraging Codex in an agent first world — OpenAI Engineering Blog URL: https://openai.com/index/harness engineering/ Shared via X: https://x.com/levie/status/2028711992320835686 (and others) Source/domain: openai.com Author: Ryan Lopopolo (OpenAI) Why it matters: One of the most cited engineering posts in the agent discourse; describes a 5 month experiment building a product with ~0 manually written lines of code, using Codex agents end to end. Extracted summary: Team of 3→7 engineers shipped ~1M lines of code via Codex over 5 months; throughput increased as the team grew. Engineering role shifts from writing code to designing environments, specifying intent, and building feedback loops. Agent to agent review loops ("Ralph Wiggum Loop") reduced human QA bottleneck. Emphasizes "application legibility" — UI, logs, metrics must be readable by agents, not just humans. Signals: Repeatedly referenced across X/Twitter; LinkedIn virality; cited by Martin Fowler and LangChain. Harness engineering for coding agent users — Martin Fowler URL: https://martinfowler.com/articles/harness engineering.html Shared via X: https://x.com/GenAI is real/status/2036266930290696599 Source/domain: martinfowler.com Author: Birgitta Böckeler (Thoughtworks) Why it matters: A practitioner oriented deep dive that formalizes "harness engineering" as a bounded context for coding agent users, bridging OpenAI's internal实践 with general software engineering. Extracted summary: Defines agent = model + harness; narrows "harness" for coding agents into feedforward guides (principles, rules, docs) and feedback sensors (static analysis, logs, review agents). Argues for "keep quality left" — harness should self correct before human eyes. Discusses harness templates and the evolving role of the human as steerer, not coder. Signals: High authority domain; 10k+ word long form; shared widely in AI engineering circles on X. AI evals are becoming the new compute bottleneck — Hugging Face Blog URL: https://huggingface.co/blog/evaleval/eval costs bottleneck Shared via X: https://x.com/ philschmid/status/1903376215806816398 (and eval threads) Source/domain: huggingface.co Authors: Avijit Ghosh, Yifan Mai, Georgia Channing, Leshem Choshen, et al. (EvalEval Coalition) Why it matters: Documents a concrete cost inflection point where evaluation now rivals or exceeds training cost for frontier agents; calls for benchmark compression and reliable benchmarking infrastructure. Extracted summary: HAL spent ~$40k running 21,730 agent rollouts across 9 models × 9 benchmarks. Single GAIA run on a frontier model can cost $2,829; Exgentic found 33× cost spread driven by scaffold choice.

## Key takeaways

- Shared via X: https://x.com/levie/status/2028711992320835686 (and others)
- Why it matters: One of the most cited engineering posts in the agent discourse; describes a 5 month experiment building a product with ~0 manually written lines of code, using Codex agents end to end.
- Team of 3→7 engineers shipped ~1M lines of code via Codex over 5 months; throughput increased as the team grew.
- Core insight: humans steer, agents execute. Engineering role shifts from writing code to designing environments, specifying intent, and building feedback loops.

## Compilation notes

Compiled from `raw/x-blogs/2026-05-02-x-blogs-digest.md` during the 2026-05-03 wiki compile. The raw capture remains the canonical source for exact excerpts, links, and figures.
