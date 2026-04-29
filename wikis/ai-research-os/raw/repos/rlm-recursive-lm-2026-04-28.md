---
status: processed
---
# Recursive Language Models (RLMs) — alexzhang13/rlm

**URL:** https://github.com/alexzhang13/rlm  
**License:** MIT  
**Maintained by:** Authors from the MIT OASYS lab  
**Stats:** 4k+ stars · 722 forks · 21 contributors · 111 commits · Python 99.7%

**Links:** [Full Paper (arXiv:2512.24601)](https://arxiv.org/abs/2512.24601) · [Blogpost](https://alexzhang13.github.io/blog/2025/rlm/) · [Documentation](https://alexzhang13.github.io/rlm/) · [RLM Minimal](https://github.com/alexzhang13/rlm-minimal)

## What are RLMs?

Recursive Language Models (RLMs) are a **task-agnostic inference paradigm** for handling near-infinite length contexts by enabling the language model to *programmatically* examine, decompose, and **recursively call itself** over its input.

> RLMs replace the canonical `llm.completion(prompt, model)` call with a `rlm.completion(prompt, model)` call. RLMs offload the context as a variable in a REPL environment that the LM can interact with and launch sub-LM calls inside of.

## Quick Setup

```bash
pip install rlms
```

### Minimal Usage (OpenAI / GPT-5-nano)
```python
from rlm import RLM

rlm = RLM(
    backend="openai",
    backend_kwargs={"model_name": "gpt-5-nano"},
    verbose=True,
)

print(rlm.completion("Print me the first 100 powers of two, each on a newline.").response)
```

## REPL Environments

| Type | Environment | Requirements | Notes |
|------|-------------|--------------|-------|
| **Non-isolated** | `local` (default) | None | Same process; minimal security; shares host venv. |
| **Non-isolated** | `ipython` | `pip install 'rlms[ipython]'` | Real IPython session. In-process or subprocess (`ipykernel`) with timeout and namespace isolation. |
| **Non-isolated** | `docker` | Docker installed | `DockerREPL`; default image `python:3.11-slim`; custom images supported. |
| **Isolated** | `modal` | `uv add modal` + `modal setup` | Cloud-based Modal Sandbox. |
| **Isolated** | `prime` | `uv pip install -e ".[prime]"` + `PRIME_API_KEY` | Beta. Prime Intellect Sandboxes. Slow runtimes currently observed. |
| **Isolated** | `daytona`, `e2b` | SDK setup | Cloud-based sandboxes. |

## Model Providers

Supported APIs / routers:
- **Cloud:** OpenAI, Anthropic, OpenRouter, Portkey
- **Local:** vLLM (via OpenAI-compatible client)

## Logging, Trajectory Metadata & Visualization

`RLMChatCompletion` includes a `metadata` field containing the full trajectory (run config + all iterations and sub-calls).

```python
from rlm.logger import RLMLogger

logger = RLMLogger(log_dir="./logs")
rlm = RLM(..., logger=logger)
```

Visualizer: Node.js/shadcn/ui app in `visualizer/` — explore code execution, sub-LM calls, and root-LM calls.

## Latest Release

- **v0.1.1a** (Feb 18, 2026) — Depth > 1 recursive subcalls with limits and cost tracking, compaction with offloaded history, `max_budget` (USD) support and `BudgetExceededError`.

## Research Citation

```bibtex
@misc{zhang2026recursivelanguagemodels,
      title={Recursive Language Models},
      author={Alex L. Zhang and Tim Kraska and Omar Khattab},
      year={2026},
      eprint={2512.24601},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2512.24601},
}
```

## Why It Matters

RLMs are a fundamental rethink of the LLM inference interface—instead of stuffing context into a prompt, the model gets a REPL environment and can recursively call itself. This enables near-infinite context handling and emergent decomposition strategies. Strong research pedigree from MIT OASYS lab (Kraska + Khattab).

## Tags

- recursive-language-models
- mit-oasys
- inference-paradigm
- infinite-context
- repl-environment
- sandbox
- python
- research
