---
url: https://arxiv.org/abs/2604.15034
repo: https://github.com/DVampire/Autogenesis
saved: 2026-04-27
paper_title: 'Autogenesis: A Self-Evolving Agent Protocol'
arXiv: 2604.15034 (v2, submitted 16 Apr 2026, revised 21 Apr 2026)
license: CC BY 4.0 (paper) / MIT (repo)
repo_stars: 29
language: Python 99.6%
contributors: Wentao Zhang, Claude, Usman
status: processed
---
# Autogenesis: A Self-Evolving Agent Protocol

## Paper

**Authors:** Wentao Zhang, Zhe Zhao, Haibin Wen, Yingcheng Wu, Ming Yin, Bo An, Mengdi Wang

**Abstract:**
Recent advances in LLM-based agent systems have shown promise in tackling complex, long-horizon tasks. However, existing agent protocols (e.g., A2A and MCP) under-specify cross-entity lifecycle and context management, version tracking, and evolution-safe update interfaces, which encourages monolithic compositions and brittle glue code.

We introduce **Autogenesis Protocol (AGP)**, a self-evolution protocol that decouples *what evolves* from *how evolution occurs*:

- **RSPL (Resource Substrate Protocol Layer):** Models prompts, agents, tools, environments, and memory as protocol-registered resources with explicit state, lifecycle, and versioned interfaces.
- **SEPL (Self Evolution Protocol Layer):** Specifies a closed-loop operator interface for proposing, assessing, and committing improvements with auditable lineage and rollback.

Building on AGP, we present **Autogenesis System (AGS)**, a self-evolving multi-agent system that dynamically instantiates, retrieves, and refines protocol-registered resources during execution. Evaluated on multiple challenging benchmarks requiring long-horizon planning and tool use across heterogeneous resources. Results demonstrate consistent improvements over strong baselines.

## Repository

**GitHub:** [DVampire/Autogenesis](https://github.com/DVampire/Autogenesis)

> **Note:** Codebase is actively undergoing refactoring and optimization. `examples/run_tool_calling_agent.py` is functional; other agents are being progressively stabilized.

### Two-Layer Protocol

| Layer | Name | Purpose |
|-------|------|---------|
| RSPL | Resource Substrate Protocol Layer | Models prompts, agents, tools, environments, memory as protocol-registered resources with explicit state, lifecycle, and versioned interfaces |
| SEPL | Self Evolution Protocol Layer | Closed-loop operator interface to propose, assess, and commit improvements with auditable lineage and rollback |

### Self-Evolution Loop

1. **Act** — Agent produces actions/outputs using LLM + available tools/environments
2. **Observe** — Capture outcomes, traces, intermediate reasoning, environment feedback
3. **Optimize** — Update prompts/solutions/variables using optimizer (reflection or RL-style methods)
4. **Remember** — Persist summaries/insights/records to memory for later steps and sessions

### Core Building Blocks

| Component | Path | Purpose |
|-----------|------|---------|
| Agents | `src/agent/` | Runtime logic for planning, tool-calling, domain agents |
| Tools | `src/tool/` | Callable capabilities exposed to agents |
| Environments | `src/environment/` | Stateful interfaces (filesystem, trading, browser, mobile) |
| Memory | `src/memory/` | Session/event memory for summarization, insights, long-term state |
| Optimizers | `src/optimizer/` | Self-improvement algorithms (reflection, GRPO, Reinforce++) |
| Tracing & Versioning | `src/tracer/`, `src/version/` | Record trajectories, manage iterative artifacts |
| Config System | `configs/`, `src/config/` | MMEngine-style config composition |

### Design Goals

- **Composable** — Add/replace agents, tools, environments, memory, optimizers without rewriting the whole stack
- **Inspectable** — Structured traces and memory events for failure analysis
- **Evolvable** — Explicit optimizers + persistent memory enable iterative refinement vs one-shot inference

### Optional: Run a Tool-Calling Agent

```bash
# Install dependencies (see scripts/INSTALL.md)
cp .env.template .env
# Set environment variables

python examples/run_tool_calling_agent.py --config configs/tool_calling_agent.py
```

### Memory System

Includes a `HeartbeatMemorySystem` (added via PR #1, co-authored by Claude):
- JSONL-backed memory subclass
- Maps Autogenesis ChatEvents to heartbeat's native learning schema (type, key, insight, confidence, source)
- Appends to `learnings.jsonl` without requiring an LLM call
- Entries derived deterministically from EventType and event data

## Citation

```bibtex
@misc{zhang2026autogenesisselfevolvingagentprotocol,
      title={Autogenesis: A Self-Evolving Agent Protocol},
      author={Wentao Zhang and Zhe Zhao and Haibin Wen and Yingcheng Wu and Ming Yin and Bo An and Mengdi Wang},
      year={2026},
      eprint={2604.15034},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2604.15034},
}
```

## Why It Matters

Autogenesis formalizes something many agent systems do ad-hoc: **structured self-evolution**. By decoupling the resource substrate (what exists) from the evolution protocol (how it improves), it provides a principled framework for agents that don't just execute tasks but genuinely improve their own prompts, tools, and workflows over time. The explicit versioning, rollback, and lineage features make it suitable for production systems where uncontrolled evolution is dangerous. Strong relevance for anyone building long-running, self-improving agent infrastructures.

## Related

- A2A and MCP protocols (prior art that AGP extends)
- WUPHF — multi-agent office with shared memory
- ClawSweeper — automated maintenance bot with review/apply lanes
- Hermes Labyrinth — observability for agent crossings
