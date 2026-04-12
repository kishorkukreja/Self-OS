---
source: https://github.com/AMAP-ML/SkillClaw
date: 2026-04-12
type: repo
tags: [skill-evolution, multi-agent, llm-agents, openclaw, knowledge-compounding]
status: raw
---

<div align="center">

# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver

[![Paper](https://img.shields.io/badge/Paper-arXiv-b5212f.svg?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2604.08377)

</div>

> SkillClaw is a framework for **skill collective evolution** in multi-user OpenClaw-style agent ecosystems. It automatically distills real-world experience from multiple users and agents into reusable Skills, and shares them via the cloud to enable continuous evolution across the entire agent cluster.

**Easy to install, effortless to use** — just two commands to set up, and supports a wide range of scenarios. Users simply interact with OpenClaw as usual, and skill evolution happens seamlessly in the background — zero extra effort required.

**Broad framework support** — SkillClaw natively integrates with various Claw frameworks, including CoPaw, IronClaw, PicoClaw, ZeroClaw, NanoClaw, and NemoClaw.

**Proven results** — In real-world scenario evaluations on [WildClawBench](https://github.com/InternLM/WildClawBench), SkillClaw significantly improved Qwen3-Max's performance even under limited group interaction and feedback conditions — not by using a bigger model, but by leveraging smarter experience.

---

## Overview

SkillClaw makes LLM agents progressively better by **evolving reusable skills** from real session data and sharing them across a group of agents.

The system has three components:

1. **Client Proxy** — A local API proxy (`/v1/chat/completions`, `/v1/messages`) that intercepts agent requests, records session artifacts, and syncs skills with shared storage.

2. **Workflow Evolve Server** (`evolve_server`) — A fixed 3-stage LLM workflow (Summarize → Aggregate → Execute) that reads session data from shared storage, evolves or creates skills, and writes them back.

3. **Agent Evolve Server** (`agent_evolve_server`) — An autonomous agent-driven alternative to the workflow evolve server. Uses an OpenClaw agent to read sessions, analyze patterns, and directly write evolved skill files with full tool access (read/write/exec).

All three share the same storage layer (Alibaba OSS / S3 / local filesystem) and skill format (`SKILL.md`), so they are fully interchangeable in a deployment.

---

## Quick Start

### Prerequisites

- Python >= 3.10
- An OpenAI-compatible LLM API endpoint

### 1. Install

```bash
# Client / local development
git clone <repo-url> SkillClaw && cd SkillClaw
bash scripts/install_skillclaw.sh
source .venv/bin/activate
```

### 2. Configure & Start the Client Proxy

```bash
export OPENAI_BASE_URL="https://your-api-gateway/v1"
export OPENAI_API_KEY="sk-..."

skillclaw setup
skillclaw start
skillclaw status
```

### 3. Start the Evolve Server

Workflow evolve server:

```bash
skillclaw-evolve-server --port 8787 --interval 300 \
  --storage-backend oss \
  --group-id my-group
```

Agent evolve server:

```bash
skillclaw-agent-evolve-server --port 8787 --interval 300 --no-fresh \
  --storage-backend oss \
  --group-id my-group
```

### 4. Skill Management

```bash
skillclaw skills pull          # download shared skills
skillclaw skills push          # upload local skills
skillclaw skills sync          # bidirectional
skillclaw skills list-remote   # browse shared skills
```

---

## Project Structure

```
SkillClaw/
├── skillclaw/                  # Client proxy, CLI, config, skill sync, experiments
├── evolve_server/              # Workflow evolve server
├── agent_evolve_server/        # OpenClaw-based evolve server
└── scripts/                    # Installers + main public experiment runner
```

## License

See [LICENSE](./LICENSE) for details.
