---
title: "Agentic Harness Engineering 2026 05 03"
date_created: 2026-05-04
date_modified: 2026-05-04
summary: "Agentic Harness Engineering Summary Agentic Harness Engineering is an observability-driven framework for automatically evolving the harness around a fixed coding agent: prompts, tools, middleware, skills, sub-agents, and"
tags: [agents, coding-agents, harness-engineering, observability, agent-evaluation, terminal-bench]
type: source
status: final
---

# Agentic Harness Engineering 2026 05 03

**Type:** repo
**Date:** 2026-05-03
**URL/Source:** https://github.com/china-qijizhifeng/agentic-harness-engineering
**Raw file:** [[../raw/repos/agentic-harness-engineering-2026-05-03.md]]
**Concepts:** [[concepts/agents.md]], [[concepts/coding-agents.md]], [[concepts/harness-engineering.md]], [[concepts/observability.md]], [[concepts/agent-evaluation.md]]

## Summary

Agentic Harness Engineering Summary Agentic Harness Engineering is an observability-driven framework for automatically evolving the harness around a fixed coding agent: prompts, tools, middleware, skills, sub-agents, and memory. The repo is tied to arXiv:2604.25850 and reports Terminal-Bench 2 pass@1 improvement from 69.7% to 77.0% over ten evaluate-analyze-improve iterations. Repository metadata - Repository: - Description: Official code for 'Agentic Harness Engineering' arXiv:2604.25850 — observability-driven automatic evolution of coding-agent harnesses concurrent work with meta-harness . Lifts Terminal-Bench 2 pass@1 69.7%→77.0% over 10 iterations, beats Codex/ACE/Training Free GRPO; frozen harness transfers to SWE-bench-verified and 4 other base models. - Default branch: main - Primary language: Python - Languages: - Python: 787723 bytes - Shell: 9006 bytes - Stars: 84 - Forks: 9 - Open issues: 0 - License: MIT - Topics: none listed - Created: 2026-04-23T07:01:18Z - Updated: 2026-05-03T22:52:21Z - Pushed: 2026-05-02T03:51:40Z - Homepage: Key points - Evolves the agent harness around a fixed base model rather than training model weights. - Uses an outer loop of evaluate → analyze → improve . - Treats traces, not aggregate scores, as the unit of optimization. - Decomposes the harness into observable components such as system prompts, tools, middleware, skills, sub-agents, and long-term memory. - Requires evidence-backed edits: failure evidence, root cause, targeted fix, and predicted impact. - Reported benchmark claim: Terminal-Bench 2 pass@1 improves from 69.7% to 77.0% over ten iterations. Why it matters This is directly relevant to Self-OS and agent engineering because it treats the agent harness—not model weights—as the optimization surface. The pattern maps well to Hermes/Self-OS: trace failures, compress them into evidence, propose falsifiable harness edits, and measure task flips across iterations. Top-level files observed - .env.example - .gitignore - LICENSE - README.md - README zh.md - evolve.py - pyproject.toml - trace converter.py Raw README <p align="right" English <a href="README zh.md" 简体中文</a </p Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses <div align="left" <p align="left" <img alt="License: MIT" src=" <img alt="Python" src=" <img alt="Managed with uv" src=" with-uv-261230?logo=python&logoColor=white" </p </div <p align="center" <img src="assets/figures/case study.png" alt="Case Study" width="44%" <img src="assets/figures/training curve.png" alt="Training Curve" width="54%" </p --- 📰 News - 2026-04-30 ✍️ Blog post on Dawning Road English & Chinese

## Key takeaways

- Agentic Harness Engineering Summary Agentic Harness Engineering is an observability-driven framework for automatically evolving the harness around a fixed coding agent: prompts, tools, middleware, skills, sub-agents, and memory.
- The repo is tied to arXiv:2604.25850 and reports Terminal-Bench 2 pass@1 improvement from 69.7% to 77.0% over ten evaluate-analyze-improve iterations.
- Repository metadata - Repository: - Description: Official code for 'Agentic Harness Engineering' arXiv:2604.25850 — observability-driven automatic evolution of coding-agent harnesses concurrent work with meta-harness .
- Lifts Terminal-Bench 2 pass@1 69.7%→77.0% over 10 iterations, beats Codex/ACE/Training Free GRPO; frozen harness transfers to SWE-bench-verified and 4 other base models.

## Compilation notes

Compiled from `raw/repos/agentic-harness-engineering-2026-05-03.md` during the 2026-05-04 wiki compile. The raw capture remains the canonical source for exact excerpts, links, figures, and context.
