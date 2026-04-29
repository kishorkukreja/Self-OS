---
status: processed
---
# ACE: Agentic Context Engineering

**URL:** https://github.com/ace-agent/ace  
**License:** Apache-2.0  
**Language:** Python 100%  
**Stars:** 1k | **Forks:** 134 | **Contributors:** 5  
**Paper:** [arXiv:2510.04618](https://arxiv.org/abs/2510.04618)

## Overview

ACE (Agentic Context Engineering) is a framework that enables LLMs to **self-improve by treating contexts as evolving playbooks**. It accumulates, refines, and organizes strategies through a modular process of generation, reflection, and curation.

Unlike traditional approaches that suffer from **brevity bias** and **context collapse**, ACE uses structured, incremental updates guided by a grow-and-refine principle to preserve detailed, domain-specific knowledge while remaining scalable.

## Key Features

- **Three-Role Agentic Architecture:** Generator, Reflector, and Curator continuously improve contexts
- **Incremental Delta Updates:** Localized edits preserve prior knowledge while accumulating new insights
- **Self-Supervised Learning:** Adapts without labeled supervision using natural execution feedback
- **High Efficiency:** **86.9% lower adaptation latency** on average vs. existing adaptive methods
- **Cost Effective:** Fewer rollouts and lower dollar costs with higher accuracy

## Performance

ACE achieves average gains of **+10.6% on agent tasks** and **+8.6% on domain-specific benchmarks** across offline and online adaptation.

| Task Category | Dataset | Improvement | Details |
| --- | --- | --- | --- |
| **Agent Tasks** | AppWorld | **+10.6%** | Matches top-ranked production agent (GPT-4.1) on average; surpasses it on harder test-challenge split using a smaller open-source model |
| **Finance** | FiNER + XBRL Formula | **+8.6%** | Domain-specific reasoning with structured information extraction |

### Efficiency Gains
- **Offline (AppWorld):** **-82.3% latency** and **-75.1% rollouts** vs. GEPA
- **Online (FiNER):** **-91.5% latency** and **-83.6% token cost** vs. Dynamic Cheatsheet

## How It Works

1. **Generator:** Produces reasoning trajectories, surfacing effective strategies and recurring pitfalls
2. **Reflector:** Separates evaluation and insight extraction from curation to improve context quality
3. **Curator:** Converts lessons into structured **delta updates** with `helpful`/`harmful` counters, using deterministic merging with de-duplication and pruning

This prevents **context collapse**, where iterative rewriting erodes details over time.

## Quick Start

```bash
git clone https://github.com/ace-agent/ace.git
cd ace

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install ACE and core dependencies
uv sync

# Set up API keys
cp .env.example .env
# Edit .env and set the API key(s) you need
```

### Basic Usage
```python
from ace import ACE
from utils import initialize_clients

api_provider = "sambanova"  # or "together", "openai", "commonstack"

ace_system = ACE(
    api_provider=api_provider,
    generator_model="DeepSeek-V3.1",
    reflector_model="DeepSeek-V3.1",
    curator_model="DeepSeek-V3.1",
    max_tokens=4096
)

config = {
    'num_epochs': 1,
    'max_num_rounds': 3,
    'curator_frequency': 1,
    'eval_steps': 100,
    'online_eval_frequency': 15,
    'save_steps': 50,
    'playbook_token_budget': 80000,
    'task_name': 'your_task',
    'json_mode': False,
    'no_ground_truth': False,
    'save_dir': './results',
    'test_workers': 20,
    'use_bulletpoint_analyzer': False,
    'api_provider': api_provider
}

# Offline adaptation
results = ace_system.run(
    mode='offline',
    train_samples=train_data,
    val_samples=val_data,
    test_samples=test_data,
    data_processor=processor,
    config=config
)

# Online adaptation
results = ace_system.run(
    mode='online',
    test_samples=test_data,
    data_processor=processor,
    config=config
)

# Evaluation only
results = ace_system.run(
    mode='eval_only',
    test_samples=test_data,
    data_processor=processor,
    config=config
)
```

## Finance Domain Example

```bash
# Offline training
uv run python -m eval.finance.run --task_name finer --mode offline --save_path results

# Online training and testing
uv run python -m eval.finance.run --task_name finer --mode online --save_path results

# Evaluation only
uv run python -m eval.finance.run --task_name finer --mode eval_only \
    --initial_playbook_path results/ace_run_TIMESTAMP_finer_offline/best_playbook.txt \
    --save_path test_results
```

## Why It Matters

ACE attacks the "context collapse" problem in agentic systems by treating context as an evolving playbook rather than a static prompt. The three-role architecture (Generator/Reflector/Curator) with delta updates is a principled approach to self-improvement that doesn't require labeled data. Strong research backing with published arXiv paper.

## Tags

- agentic-context-engineering
- self-improvement
- context-management
- playbook-evolution
- python
- research
- appworld
- finance
- sambanova
