# Meta-Harness: Autonomously Improving LLM Harnesses

**Type:** thread
**Date:** 2026-03-30
**URL:** https://x.com/yoonholeee/status/2038640635482456118
**Raw file:** [[../../raw/x-threads/Thread by @yoonholeee.md]]

**Summary:** Research paper announcement introducing Meta-Harness — a method for autonomously optimising LLM evaluation harnesses on problems humans are actively working on. Uses a coding agent as proposer with full filesystem access to the complete history of prior experience, solving a long-horizon credit-assignment problem. Benchmarked on TerminalBench-2.

**Key contributions:**
- Meta-Harness: an agent-based system for optimising other harnesses end-to-end
- Key finding: unrestricted access to full history outperforms summaries/rewards-only approaches
- Agent reads median 82 files per iteration — full history access is essential for long-horizon reasoning
- New instantiation of classic meta-learning: less imposed structure, more agent autonomy
- Paper: https://arxiv.org/abs/2603.28052

**Tags:** meta-learning, harness-optimization, agent-self-improvement, llm-evaluation, research
