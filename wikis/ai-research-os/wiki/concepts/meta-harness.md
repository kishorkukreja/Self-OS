# Meta-Harness

**Definition:** A system where a coding agent autonomously improves LLM evaluation harnesses by reading the full history of prior attempts and proposing targeted modifications — a meta-learning approach with minimal imposed structure.

**Why it matters:** Optimising evaluation harnesses is typically manual and slow. Meta-Harness automates this: the agent reads everything (code, traces, scores), reasons about what failed and why, and proposes harness changes. Full history access (not summaries) is essential — long-horizon credit assignment requires seeing the details.

**Key findings (Yoonho Lee et al., 2026):**
- Agents reading full history (median 82 files/iteration) outperform agents that only see summaries/rewards
- The proposer reasons like a human engineer: forms targeted hypotheses about what failed
- Meta-Harness is itself a harness: a system that optimises other systems
- Benchmarked on TerminalBench-2

**Relevance to Self OS:**
- The principle of full history access applies to wiki-agent-memory: agents need complete session logs, not just summaries, for deep reasoning
- Supersession and retention decay patterns parallel the credit assignment problem

**Related:** [[wiki-agent-memory]], [[knowledge-compounding]]

**Sources:** [[sources/yoonholeee-meta-harness-2026]]

_Last updated: 2026-04-12_
