---
title: "Recursive Language Models (RLMs) — alexzhang13/rlm"
date_created: 2026-04-29
date_modified: 2026-04-29
summary: "Recursive Language Models (RLMs) — alexzhang13/rlm captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabili"
tags: [context-engineering]
type: source
status: final
---

# Recursive Language Models (RLMs) — alexzhang13/rlm

**Type:** repo  
**Date:** 2026-04-28  
**URL:** https://github.com/alexzhang13/rlm  
**Raw file:** [[../../raw/repos/rlm-recursive-lm-2026-04-28.md]]

**Summary:** Recursive Language Models (RLMs) — alexzhang13/rlm captures a repo relevant to AI engineering workflows, agent infrastructure, and knowledge-management practices. The source is useful because it records concrete capabilities, setup details, and design trade-offs that can be compared against the rest of the AI Research OS corpus. Recursive Language Models (RLMs) — alexzhang13/rlm Maintained by: Authors from the MIT OASYS lab Links: Full Paper (arXiv:2512.24601) · Blogpost · Documentation · RLM Minimal Recursive Language Models (RLMs) are a task-agnostic inference paradigm for handling near-infinite length contexts by enabling the language model to programmatically examine, decompose, and recursively call itself over its input. RLMs replace the canonical llm.completion(prompt, model) call with a rlm.completion(prompt, model) call. RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of. Minimal Usage (OpenAI / GPT-5-nano) Non-isolated  local (default)  None  Same process; minimal security; shares host venv. Non-isolated  ipython  pip install 'rlms[ipython]'  Real IPython session. In-process or subprocess (ipykernel) with timeout and namespace isolation. Non-isolated  docker  Docker installed  DockerREPL; default image python:3.11-slim; custom images supported.

**Key contributions:**
- Recursive Language Models (RLMs) — alexzhang13/rlm
- Maintained by: Authors from the MIT OASYS lab
- Stats: 4k+ stars · 722 forks · 21 contributors · 111 commits · Python 99.7%
- Links: Full Paper (arXiv:2512.24601) · Blogpost · Documentation · RLM Minimal
- Minimal Usage (OpenAI / GPT-5-nano)

**Related concepts:** [[concepts/context-engineering]]  
**Primary entity:** [[entities/recursive-language-models]]

**Tags:** context-engineering
