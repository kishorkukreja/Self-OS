---
status: processed
---
     1|---
     2|source: https://github.com/AMAP-ML/SkillClaw
     3|date: 2026-04-12
     4|type: repo
     5|tags: [skill-evolution, multi-agent, llm-agents, openclaw, knowledge-compounding]
     6|status: raw
     7|---
     8|
     9|<div align="center">
    10|
    11|# SkillClaw: Let Skills Evolve Collectively with Agentic Evolver
    12|
    13|[![Paper](https://img.shields.io/badge/Paper-arXiv-b5212f.svg?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2604.08377)
    14|
    15|</div>
    16|
    17|> SkillClaw is a framework for **skill collective evolution** in multi-user OpenClaw-style agent ecosystems. It automatically distills real-world experience from multiple users and agents into reusable Skills, and shares them via the cloud to enable continuous evolution across the entire agent cluster.
    18|
    19|**Easy to install, effortless to use** — just two commands to set up, and supports a wide range of scenarios. Users simply interact with OpenClaw as usual, and skill evolution happens seamlessly in the background — zero extra effort required.
    20|
    21|**Broad framework support** — SkillClaw natively integrates with various Claw frameworks, including CoPaw, IronClaw, PicoClaw, ZeroClaw, NanoClaw, and NemoClaw.
    22|
    23|**Proven results** — In real-world scenario evaluations on [WildClawBench](https://github.com/InternLM/WildClawBench), SkillClaw significantly improved Qwen3-Max's performance even under limited group interaction and feedback conditions — not by using a bigger model, but by leveraging smarter experience.
    24|
    25|---
    26|
    27|## Overview
    28|
    29|SkillClaw makes LLM agents progressively better by **evolving reusable skills** from real session data and sharing them across a group of agents.
    30|
    31|The system has three components:
    32|
    33|1. **Client Proxy** — A local API proxy (`/v1/chat/completions`, `/v1/messages`) that intercepts agent requests, records session artifacts, and syncs skills with shared storage.
    34|
    35|2. **Workflow Evolve Server** (`evolve_server`) — A fixed 3-stage LLM workflow (Summarize → Aggregate → Execute) that reads session data from shared storage, evolves or creates skills, and writes them back.
    36|
    37|3. **Agent Evolve Server** (`agent_evolve_server`) — An autonomous agent-driven alternative to the workflow evolve server. Uses an OpenClaw agent to read sessions, analyze patterns, and directly write evolved skill files with full tool access (read/write/exec).
    38|
    39|All three share the same storage layer (Alibaba OSS / S3 / local filesystem) and skill format (`SKILL.md`), so they are fully interchangeable in a deployment.
    40|
    41|---
    42|
    43|## Quick Start
    44|
    45|### Prerequisites
    46|
    47|- Python >= 3.10
    48|- An OpenAI-compatible LLM API endpoint
    49|
    50|### 1. Install
    51|
    52|```bash
    53|# Client / local development
    54|git clone <repo-url> SkillClaw && cd SkillClaw
    55|bash scripts/install_skillclaw.sh
    56|source .venv/bin/activate
    57|```
    58|
    59|### 2. Configure & Start the Client Proxy
    60|
    61|```bash
    62|export OPENAI_BASE_URL="https://your-api-gateway/v1"
    63|export OPENAI_API_KEY="***"
    64|
    65|skillclaw setup
    66|skillclaw start
    67|skillclaw status
    68|```
    69|
    70|### 3. Start the Evolve Server
    71|
    72|Workflow evolve server:
    73|
    74|```bash
    75|skillclaw-evolve-server --port 8787 --interval 300 \
    76|  --storage-backend oss \
    77|  --group-id my-group
    78|```
    79|
    80|Agent evolve server:
    81|
    82|```bash
    83|skillclaw-agent-evolve-server --port 8787 --interval 300 --no-fresh \
    84|  --storage-backend oss \
    85|  --group-id my-group
    86|```
    87|
    88|### 4. Skill Management
    89|
    90|```bash
    91|skillclaw skills pull          # download shared skills
    92|skillclaw skills push          # upload local skills
    93|skillclaw skills sync          # bidirectional
    94|skillclaw skills list-remote   # browse shared skills
    95|```
    96|
    97|---
    98|
    99|## Project Structure
   100|
   101|```
   102|SkillClaw/
   103|├── skillclaw/                  # Client proxy, CLI, config, skill sync, experiments
   104|├── evolve_server/              # Workflow evolve server
   105|├── agent_evolve_server/        # OpenClaw-based evolve server
   106|└── scripts/                    # Installers + main public experiment runner
   107|```
   108|
   109|## License
   110|
   111|See [LICENSE](./LICENSE) for details.
   112|