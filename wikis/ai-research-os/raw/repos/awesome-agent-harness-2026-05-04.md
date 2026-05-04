---
source: https://github.com/Picrew/awesome-agent-harness
date: 2026-05-04
type: repo
tags: [agent-harness, awesome-list, ai-agents, evaluation, observability, governance, github-repo]
---

# Awesome Agent Harness — Implementation-First Harness Engineering Catalog

## Summary
Awesome Agent Harness is a curated catalog of agent harness engineering resources, with GitHub projects as the primary focus. It organizes harness architecture, context/state engineering, sandboxing, protocols, evaluation, observability, governance, reference implementations, and readings.

## Repo metadata
- **Repository:** `Picrew/awesome-agent-harness`
- **URL:** https://github.com/Picrew/awesome-agent-harness
- **Description:** An awesome list of Agent Harness engineering resources, including GitHub projects, tools, benchmarks, and practical guides.
- **Primary language:** Python
- **Language breakdown:** Python 100.0%
- **License:** not detected by GitHub API
- **Stars:** 287
- **Forks:** 18
- **Watchers:** 1
- **Open issues:** 2
- **Created:** 2026-03-30T03:14:38Z
- **Updated:** 2026-05-04T21:44:54Z
- **Last pushed:** 2026-04-28T07:37:59Z
- **Default branch:** main
- **Homepage:** none
- **Topics:** agent-harness, context-engineering, harness-engineering
- **Fetched README:** main/README.md

## Key points
- Catalogs more than 160 harness-related resources across nine categories.
- Highlights practical harness engineering blogs from Anthropic, OpenAI, LangChain, Inngest, and others.
- Useful as a discovery map for comparing open-source harnesses, benchmarks, security patterns, and observability tools.

## Why it matters
Useful as a meta-source for Self-OS research: it can seed a broader harness-engineering map and identify tools worth compiling into entities/concepts later.

## Raw content

```markdown
# Awesome Agent Harness

A curated, implementation-first list of **agent harness engineering** resources, with GitHub projects as the primary focus.

- Total entries: **163**
- GitHub entries: **138 (84.7%)**
- GitHub in project categories (excluding readings): **134/134 (100.0%)**
- Categories: **9**
- Last verified: **2026-04-22**
- Language: [English](./README.md) | [中文](./README_zh.md)

<a id="featured-harness-blogs"></a>
## Featured Harness Blogs

- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents): Anthropic's meta-harness architecture for decoupling session logs, harness loops, and sandboxes in long-horizon agents.
- [Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode): Anthropic's write-up on classifier-backed approval delegation for safer high-autonomy coding-agent runs.
- [Harness engineering (OpenAI)](https://openai.com/index/harness-engineering/): Field report on building reliable agent-first software via harness constraints and verification.
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents): Anthropic's practical guidance on when to use workflows vs. autonomous agents and how to structure them.
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents): Best practices for tool interface design so agents call tools safely and reliably.
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): Practical guide to maintaining state, resumability, and reliability over long agent runs.
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps): Follow-up article on improving long-running app generation through harness structure.
- [Improving Deep Agents with harness engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/): Evidence that harness improvements alone can move benchmark performance.
- [Evaluating Deep Agents: Our Learnings](https://blog.langchain.com/evaluating-deep-agents-our-learnings/): LangChain's practical lessons on evaluating stateful and long-horizon agents.
- [Your Agent Needs a Harness, Not a Framework](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework): Argument for reliability-first infrastructure around agents instead of framework-only thinking.

## Contents

- [Category Overview](#category-overview)
- [Featured Harness Blogs](#featured-harness-blogs)
- [Catalog](#catalog)
  - [Harness Architecture & Orchestration](#harness-architecture-orchestration)
  - [Context & Working-State Engineering](#context-working-state-engineering)
  - [Execution Substrates & Sandboxing](#execution-substrates-sandboxing)
  - [Protocols, Tool Interfaces & Agent Contracts](#protocols-tool-interfaces-agent-contracts)
  - [Evaluation Harnesses & Benchmarks](#evaluation-harnesses-benchmarks)
  - [Observability & Reliability Operations](#observability-reliability-operations)
  - [Guardrails, Security & Governance](#guardrails-security-governance)
  - [Reference Harness Implementations](#reference-harness-implementations)
  - [Essential Readings & Ecosystem Maps](#essential-readings-ecosystem-maps)
- [Maintenance Notes](#maintenance-notes)
- [Citation](#citation)

## Category Overview

| Category | Entries |
| --- | ---: |
| Harness Architecture & Orchestration | 20 |
| Context & Working-State Engineering | 9 |
| Execution Substrates & Sandboxing | 16 |
| Protocols, Tool Interfaces & Agent Contracts | 11 |
| Evaluation Harnesses & Benchmarks | 21 |
| Observability & Reliability Operations | 14 |
| Guardrails, Security & Governance | 11 |
| Reference Harness Implementations | 32 |
| Essential Readings & Ecosystem Maps | 29 |

## Catalog

Notes:
- `Stars` are rendered as badges from snapshot values.
- Repository update dates are tracked in `data/projects.yaml` and validation reports.
- Entries are sorted by stars (descending) within each category.

<a id="harness-architecture-orchestration"></a>
### Harness Architecture & Orchestration

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| DeerFlow | [GitHub](https://github.com/bytedance/deer-flow) | [![[b9b78cd49be3bc822a4e8530ebde8829_MD5.svg]]](https://github.com/bytedance/deer-flow) | long-horizon, memory, subagents | Long-horizon super-agent harness integrating memory, tools, subagents, and sandboxes. |
| AutoGen | [GitHub](https://github.com/microsoft/autogen) | [![[7c45895b1c0fc56f56724fe50291f12c_MD5.svg]]](https://github.com/microsoft/autogen) | multi-agent, orchestration, framework | Programming framework for agentic AI with multi-agent interaction and orchestration. |
| Agno | [GitHub](https://github.com/agno-agi/agno) | [![[9003e289e38aa34f3593b75bf6451a83_MD5.svg]]](https://github.com/agno-agi/agno) | scale, runtime, management | Agent software runtime focused on running and managing agentic systems at scale. |
| LangGraph | [GitHub](https://github.com/langchain-ai/langgraph) | [![[1e0c7bec27b66d8a0de0f5c4fa6356d5_MD5.svg]]](https://github.com/langchain-ai/langgraph) | graph, workflow, runtime | Graph-based runtime for resilient stateful agents and deterministic workflow control. |
| Semantic Kernel | [GitHub](https://github.com/microsoft/semantic-kernel) | [![[843daa6d64621a383d21c1383bf25f1a_MD5.svg]]](https://github.com/microsoft/semantic-kernel) | enterprise, orchestration, plugins | Enterprise-grade agentic application framework with orchestration and plugin patterns. |
| OpenAI Agents SDK (Python) | [GitHub](https://github.com/openai/openai-agents-python) | [![[8279f236c3e7e8bd29a84d27bda4a841_MD5.svg]]](https://github.com/openai/openai-agents-python) | sdk, handoff, workflows | Lightweight framework for multi-agent workflows, handoffs, and production patterns. |
| deepagents | [GitHub](https://github.com/langchain-ai/deepagents) | [![[9fb77644ad60cd5640b964861a4c2831_MD5.svg]]](https://github.com/langchain-ai/deepagents) | runtime, orchestration, long-running | Open-source harness for long-running, tool-using agents with planning and subagent patterns. |
| Google ADK (Python) | [GitHub](https://github.com/google/adk-python) | [![[3faab9c76f20f30dbf335c380de729d2_MD5.svg]]](https://github.com/google/adk-python) | toolkit, deployment, evaluation | Code-first toolkit to build, evaluate, and deploy advanced AI agents. |
| PydanticAI | [GitHub](https://github.com/pydantic/pydantic-ai) | [![[b2dbe9863d7963d9681d4d27ee3ffb4b_MD5.svg]]](https://github.com/pydantic/pydantic-ai) | python, typing, schema | Type-safe Python framework for agents with strong schema contracts and tooling. |
| Hive | [GitHub](https://github.com/aden-hive/hive) | [![[8f00bff1c5068e3cf3b146ab7bf6d89e_MD5.svg]]](https://github.com/aden-hive/hive) | harness, orchestration, runtime | Outcome-driven agent runtime harness with explicit control loops and orchestration blocks. |
| Microsoft Agent Framework | [GitHub](https://github.com/microsoft/agent-framework) | [![[db7b82aca78dbff8ce4118653de9d165_MD5.svg]]](https://github.com/microsoft/agent-framework) | multi-agent, workflows, observability | Multi-language framework for building, orchestrating, and deploying AI agents with graph workflows and observability. |
| VoltAgent | [GitHub](https://github.com/VoltAgent/voltagent) | [![[2ed4716a22bf2242d7329ae34c820452_MD5.svg]]](https://github.com/VoltAgent/voltagent) | typescript, platform, runtime | TypeScript agent engineering platform built around open runtime abstractions. |
| mcp-agent | [GitHub](https://github.com/lastmile-ai/mcp-agent) | [![[b604d4c44db544da4493894328f8610f_MD5.svg]]](https://github.com/lastmile-ai/mcp-agent) | mcp, runtime, workflow | Practical agent framework centered on MCP tool ecosystems and workflow composition. |
| Yao | [GitHub](https://github.com/YaoApp/yao) | [![[4d63bba80c7819c9cacc780f52d4f1b9_MD5.svg]]](https://github.com/YaoApp/yao) | single-binary, runtime, autonomous | Single-binary runtime for defining and running autonomous agents. |
| Cloudflare Agents | [GitHub](https://github.com/cloudflare/agents) | [![[d4e06c835016ae4192b236cd145017b3_MD5.svg]]](https://github.com/cloudflare/agents) | platform, deployment, runtime | Platform runtime for building and deploying agents with production infrastructure primitives. |
| Docker Agent | [GitHub](https://github.com/docker/docker-agent) | [![[8000d82702a9f9cd418edbfd2509eb6b_MD5.svg]]](https://github.com/docker/docker-agent) | docker, runtime, container | Agent builder and runtime stack emphasizing container-native execution. |
| NeMo Agent Toolkit | [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | [![[b69f462f78ab8a1a210f4b1395b5de66_MD5.svg]]](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | multi-agent, optimization, toolkit | Open toolkit for connecting and optimizing teams of AI agents. |
| Scion | [GitHub](https://github.com/GoogleCloudPlatform/scion) | [![[fc4b24d33cb1f6b5264bb7d24a69b9a8_MD5.svg]]](https://github.com/GoogleCloudPlatform/scion) | multi-agent, containers, orchestration | Experimental multi-agent orchestration testbed that runs isolated agent harnesses in containers, worktrees, and remote runtimes. |
| deepagentsjs | [GitHub](https://github.com/langchain-ai/deepagentsjs) | [![[874fc06b6ae75e0acfc671868e1f4028_MD5.svg]]](https://github.com/langchain-ai/deepagentsjs) | typescript, langgraph, subagents | TypeScript agent harness with built-in planning, filesystem tools, subagents, and LangGraph-native runtime hooks. |
| hankweave | [GitHub](https://github.com/SouthBridgeAI/hankweave-runtime) | [![[bd2b0243c11a3da812bb91f893b067be_MD5.svg]]](https://github.com/SouthBridgeAI/hankweave-runtime) | long-horizon, runtime, checkpoints | Headless-first long-horizon runtime that orchestrates existing agent harnesses with sentinels, loops, checkpoints, and event journals. |

<a id="context-working-state-engineering"></a>
### Context & Working-State Engineering

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| everything-claude-code | [GitHub](https://github.com/affaan-m/everything-claude-code) | [![[a5266d79383032f345d63c91ae8e5b4e_MD5.svg]]](https://github.com/affaan-m/everything-claude-code) | context, skills, harness-practices | Large open repository of harness practices around memory, skills, and context control for coding agents. |
| claude-mem | [GitHub](https://github.com/thedotmack/claude-mem) | [![[b65710a09c2ba5c5b8600bb4a148c381_MD5.svg]]](https://github.com/thedotmack/claude-mem) | memory, context, session | Plugin-style memory layer that captures session history and reinjects relevant context into future coding runs. |
| planning-with-files | [GitHub](https://github.com/OthmanAdi/planning-with-files) | [![[41f45ae9a74da1aead0bf9c4d020f14b_MD5.svg]]](https://github.com/OthmanAdi/planning-with-files) | planning, skills, persistence | Skill package for persistent file-based planning in coding-agent workflows. |
| Agent Skills for Context Engineering | [GitHub](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | [![[d5771c06022a07589b00e8c2ade6c2e9_MD5.svg]]](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | skills, context, production | Large skill library oriented around context engineering and production agents. |
| Context-Engineering Handbook | [GitHub](https://github.com/davidkimai/Context-Engineering) | [![[cbfd79e2a85d50874216ebebc44fbe6a_MD5.svg]]](https://github.com/davidkimai/Context-Engineering) | context-engineering, handbook, practices | First-principles handbook focused on practical context engineering for agent systems. |
| CCPM | [GitHub](https://github.com/automazeio/ccpm) | [![[28712eb26413da0ed72aea2f5d8a7dfd_MD5.svg]]](https://github.com/automazeio/ccpm) | planning, github-issues, parallel-execution | Spec-driven project-manager skill that turns PRDs and GitHub issues into persistent context and parallel agent execution. |
| Trellis | [GitHub](https://github.com/mindfold-ai/Trellis) | [![[992d85f3fd14817bd703c97637d54961_MD5.svg]]](https://github.com/mindfold-ai/Trellis) | specs, memory, workflow | Multi-platform coding-agent workflow framework with task context, project memory, and spec injection. |
| Awesome Context Engineering | [GitHub](https://github.com/Meirtz/Awesome-Context-Engineering) | [![[d9f515aa24d8758998668c6815b55854_MD5.svg]]](https://github.com/Meirtz/Awesome-Context-Engineering) | awesome-list, context, survey | Survey-style list for context engineering resources and frameworks. |
| context-space | [GitHub](https://github.com/context-space/context-space) | [![[5abc7a339b0a5955f935aa58f08d777b_MD5.svg]]](https://github.com/context-space/context-space) | context, infrastructure, mcp | Infrastructure project focused on context engineering building blocks and MCP-centric integrations. |

<a id="execution-substrates-sandboxing"></a>
### Execution Substrates & Sandboxing

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Daytona | [GitHub](https://github.com/daytonaio/daytona) | [![[01c6a8e4672a2336dbb51021bc2859ec_MD5.svg]]](https://github.com/daytonaio/daytona) | sandbox, execution, infra | Secure and elastic sandbox infrastructure for running AI-generated code with file, Git, LSP, and execution APIs. |
| CUA | [GitHub](https://github.com/trycua/cua) | [![[7d3ef4ca0ef54e85d99bdb3865d6553f_MD5.svg]]](https://github.com/trycua/cua) | computer-use, sandbox, infra | Infrastructure stack for computer-use agents with sandbox, SDK, and benchmark support. |
| E2B | [GitHub](https://github.com/e2b-dev/E2B) | [![[27cfb4bfb7eed3c89ea6d876b1edfbc0_MD5.svg]]](https://github.com/e2b-dev/E2B) | cloud-sandbox, execution, enterprise | Secure cloud environments with real tools for production-grade agent execution. |
| OpenSandbox | [GitHub](https://github.com/alibaba/OpenSandbox) | [![[cd09ce24275a69c2fd63dad465ecfb6d_MD5.svg]]](https://github.com/alibaba/OpenSandbox) | sandbox, security, runtime | Secure and extensible sandbox runtime built for agent workloads. |
| agent-infra sandbox | [GitHub](https://github.com/agent-infra/sandbox) | [![[3348461f052248034c4228303636b5a4_MD5.svg]]](https://github.com/agent-infra/sandbox) | all-in-one, browser, shell | All-in-one sandbox combining browser, shell, files, MCP, and IDE server. |
| Judge0 | [GitHub](https://github.com/judge0/judge0) | [![[8b149f19881fcaaeed8a2111f8e5a8f6_MD5.svg]]](https://github.com/judge0/judge0) | code-execution, sandbox, backend | Scalable sandboxed code execution system usable as an agent execution backend. |
| Agent Sandbox | [GitHub](https://github.com/kubernetes-sigs/agent-sandbox) | [![[8c3c398a50efa33e1914dc66d597353f_MD5.svg]]](https://github.com/kubernetes-sigs/agent-sandbox) | kubernetes, sandbox, stateful | Kubernetes-native sandbox control plane for isolated, stateful agent runtimes with stable identity, persistence, and warm-pool support. |
| stakpak/agent | [GitHub](https://github.com/stakpak/agent) | [![[17fd8a390026d89b195c401b95d8e359_MD5.svg]]](https://github.com/stakpak/agent) | always-on, autonomous, ops | Always-on open agent that runs on your machines with autonomous operational loops. |
| OSS-Fuzz Gen | [GitHub](https://github.com/google/oss-fuzz-gen) | [![[ecc3e090446260f03267808784ea669c_MD5.svg]]](https://github.com/google/oss-fuzz-gen) | fuzzing, security, execution | LLM-powered fuzzing workflows integrated with controlled execution contexts. |
| Tensorlake | [GitHub](https://github.com/tensorlakeai/tensorlake) | [![[707bb5e217d1d6e8e0f569b1535eb69f_MD5.svg]]](https://github.com/tensorlakeai/tensorlake) | microvm, sandbox, orchestration | Serverless runtime for agent sandboxes with MicroVM isolation, snapshots, suspend-resume, and background orchestration. |
| Arrakis | [GitHub](https://github.com/abshkbh/arrakis) | [![[0364af1772ac3dcdaea3fc3ae853da88_MD5.svg]]](https://github.com/abshkbh/arrakis) | sandbox, microvm, snapshots | Self-hosted sandbox substrate with MicroVM isolation, snapshot restore, and REST, SDK, and MCP interfaces for agent code execution and computer use. |
| AgentScope Runtime | [GitHub](https://github.com/agentscope-ai/agentscope-runtime) | [![[4f7e72d9949238502807ca73b0d89700_MD5.svg]]](https://github.com/agentscope-ai/agentscope-runtime) | runtime, sandbox, deployment | Production runtime for agent apps with secure tool sandboxes, deployment APIs, observability, and state services. |
| SWE-ReX | [GitHub](https://github.com/SWE-agent/SWE-ReX) | [![[6dd94141a18c7060cf8f1aedff14af3b_MD5.svg]]](https://github.com/SWE-agent/SWE-ReX) | sandbox, execution, coding-agent | Sandboxed execution infrastructure for AI coding agents at local and cloud scale. |
| sandboxed.sh | [GitHub](https://github.com/Th0rgal/sandboxed.sh) | [![[cff5b8a2709a1260cd1062834ebdc25d_MD5.svg]]](https://github.com/Th0rgal/sandboxed.sh) | self-hosted, isolation, orchestrator | Self-hosted orchestrator running coding agents inside isolated Linux workspaces. |
| Capsule | [GitHub](https://github.com/capsulerun/capsule) | [![[7516dd5bb9201965c235f7ed9bcdd493_MD5.svg]]](https://github.com/capsulerun/capsule) | wasm, sandbox, task-runtime | Durable runtime that coordinates agent tasks inside isolated WebAssembly sandboxes with retries and lifecycle tracking. |
| terminal-bench-env | [GitHub](https://github.com/ucsb-mlsec/terminal-bench-env) | [![[2d073357081a8db7411a569fd3c0ded0_MD5.svg]]](https://github.com/ucsb-mlsec/terminal-bench-env) | terminal, benchmark-env, sandbox | Environment layer for terminal-agent benchmark execution. |

<a id="protocols-tool-interfaces-agent-contracts"></a>
### Protocols, Tool Interfaces & Agent Contracts

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| GitHub Spec Kit | [GitHub](https://github.com/github/spec-kit) | [![[01d8da5b26a666e3a52fdc32abaeaf1c_MD5.svg]]](https://github.com/github/spec-kit) | spec-driven, workflows, tooling | Toolkit for spec-driven development to guide deterministic agent execution. |
| MCP Servers | [GitHub](https://github.com/modelcontextprotocol/servers) | [![[cdcbcdaf0580cb9aa708d93675fc3951_MD5.svg]]](https://github.com/modelcontextprotocol/servers) | mcp, servers, implementations | Official collection of MCP server implementations across tools and domains. |
| AGENTS.md | [GitHub](https://github.com/agentsmd/agents.md) | [![[f3aec5f81373bbef4b1f68940fc06c33_MD5.svg]]](https://github.com/agentsmd/agents.md) | spec, agent-file, instructions | Open format for repository-local instructions that coding agents can follow. |
| Model Context Protocol | [GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol) | [![[118a68ba7433798a950d64dfe43babeb_MD5.svg]]](https://github.com/modelcontextprotocol/modelcontextprotocol) | mcp, protocol, interoperability | Core specification and docs for MCP-based tool and context interoperability. |
| directories (rules and MCP indexes) | [GitHub](https://github.com/leerob/directories) | [![[2624c8ade3bf1214f15c8fd15127304b_MD5.svg]]](https://github.com/leerob/directories) | directories, mcp, rules | Curated directories of agent rules and MCP servers for tool discovery. |
| LangChain MCP Adapters | [GitHub](https://github.com/langchain-ai/langchain-mcp-adapters) | [![[7de9f6352287ff38a8a05b42520b39ee_MD5.svg]]](https://github.com/langchain-ai/langchain-mcp-adapters) | mcp, adapters, integration | Adapters connecting LangChain components with MCP servers. |
| Microsoft MCP Servers | [GitHub](https://github.com/microsoft/mcp) | [![[2345c82548c1bdf07737ac717ab1a7a6_MD5.svg]]](https://github.com/microsoft/mcp) | mcp, enterprise, servers | Microsoft's official MCP server catalog for enterprise data and tools. |
| ACPX | [GitHub](https://github.com/openclaw/acpx) | [![[94efe810c739c27f52ed7c8b9ea1164a_MD5.svg]]](https://github.com/openclaw/acpx) | acp, client, sessions | Headless CLI client for stateful Agent Client Protocol sessions. |
| Microsoft Learn MCP | [GitHub](https://github.com/MicrosoftDocs/mcp) | [![[ed1faf816e500882f9cda7c914b04cb5_MD5.svg]]](https://github.com/MicrosoftDocs/mcp) | mcp, docs, grounding | MCP server and CLI for grounding agents with Microsoft documentation sources. |
| IBM MCP | [GitHub](https://github.com/IBM/mcp) | [![[265a4466caf239f8a34702c2d55a6360_MD5.svg]]](https://github.com/IBM/mcp) | mcp, clients, tooling | IBM collection of MCP servers, clients, and developer tooling. |
| AGENT.md | [GitHub](https://github.com/agentmd/agent.md) | [![[9ddc3abb6e1680d77d959b2fb4824312_MD5.svg]]](https://github.com/agentmd/agent.md) | standard, agent-file, interoperability | Standardized machine-readable file format for agentic coding tools. |

<a id="evaluation-harnesses-benchmarks"></a>
### Evaluation Harnesses & Benchmarks

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Promptfoo | [GitHub](https://github.com/promptfoo/promptfoo) | [![[9b818b1c48e1e6d4bf51aa3212666dde_MD5.svg]]](https://github.com/promptfoo/promptfoo) | eval, red-team, ci | Config-driven prompt/agent/RAG testing, comparison, and red-team evaluation tool. |
| DeepEval | [GitHub](https://github.com/confident-ai/deepeval) | [![[4921d17472fd158af06384ba1f52068f_MD5.svg]]](https://github.com/confident-ai/deepeval) | evaluation, framework, testing | LLM evaluation framework supporting agent and workflow quality testing. |
| RAGAS | [GitHub](https://github.com/vibrantlabsai/ragas) | [![[78c77f2c5f09aced1eb84899e17460cc_MD5.svg]]](https://github.com/vibrantlabsai/ragas) | rag, metrics, evaluation | Open evaluation toolkit for LLM and RAG quality metrics. |
| lm-evaluation-harness | [GitHub](https://github.com/EleutherAI/lm-evaluation-harness) | [![[4dba4d228404128301ca8702816cafbd_MD5.svg]]](https://github.com/EleutherAI/lm-evaluation-harness) | benchmark, harness, llm | Popular benchmark harness for consistent LLM evaluation across tasks. |
| SWE-bench | [GitHub](https://github.com/SWE-bench/SWE-bench) | [![[f2a48323ddec4d4e211eb5a982479967_MD5.svg]]](https://github.com/SWE-bench/SWE-bench) | benchmark, swe, evaluation | Standard benchmark for evaluating issue-fixing software engineering agents. |
| verifiers | [GitHub](https://github.com/PrimeIntellect-ai/verifiers) | [![[93de2e3fd6cbdf91d58425c70d46ce4c_MD5.svg]]](https://github.com/PrimeIntellect-ai/verifiers) | verifier, rl, evaluation | Library for RL environments and verifier-based evaluation loops. |
| AgentBench | [GitHub](https://github.com/THUDM/AgentBench) | [![[37ec528a836ef89a7be1e1ff62ab254c_MD5.svg]]](https://github.com/THUDM/AgentBench) | benchmark, cross-domain, agent | Cross-environment benchmark for evaluating LLM agents as tool-using systems. |
| LangWatch | [GitHub](https://github.com/langwatch/langwatch) | [![[13af68ec88bf33ff9780d75d4cfebe9b_MD5.svg]]](https://github.com/langwatch/langwatch) | simulation, evaluation, testing | End-to-end platform for agent simulations, evaluation loops, and production testing. |
| EvalScope | [GitHub](https://github.com/modelscope/evalscope) | [![[83c9fc28dd61853807d2934aaaf6a02d_MD5.svg]]](https://github.com/modelscope/evalscope) | benchmark, framework, llm | Customizable framework for large-model benchmarking and performance evaluation. |
| Terminal-Bench | [GitHub](https://github.com/harbor-framework/terminal-bench) | [![[7b878bc3c514813be5ab3d03ae19a3ec_MD5.svg]]](https://github.com/harbor-framework/terminal-bench) | terminal, benchmark, long-horizon | Terminal-native benchmark suite for long-horizon, verification-heavy agent tasks. |
| Harbor | [GitHub](https://github.com/harbor-framework/harbor) | [![[fa161181ff5fefa3c252e0e0f2627546_MD5.svg]]](https://github.com/harbor-framework/harbor) | evaluation, harness, rl-env | Framework for running agent evaluations and constructing RL-style environments. |
| tau2-bench | [GitHub](https://github.com/sierra-research/tau2-bench) | [![[92e225ea6328606596a223c713eb390d_MD5.svg]]](https://github.com/sierra-research/tau2-bench) | tool-use, interaction, benchmark | Tool-agent-user interaction benchmark emphasizing multi-step execution quality. |
| NeMo Gym | [GitHub](https://github.com/NVIDIA-NeMo/Gym) | [![[dfe1c5952375e67924ae7995e40f3955_MD5.svg]]](https://github.com/NVIDIA-NeMo/Gym) | rl-env, training, evaluation | Toolkit for building RL environments suitable for LLM/agent training and eval. |
| TheAgentCompany | [GitHub](https://github.com/TheAgentCompany/TheAgentCompany) | [![[ff586bedf34d735be152204a4e762e35_MD5.svg]]](https://github.com/TheAgentCompany/TheAgentCompany) | benchmark, workplace, multi-step | Agent benchmark with simulated software-company tasks for evaluating multi-step workplace autonomy. |
| Inspect Evals | [GitHub](https://github.com/UKGovernmentBEIS/inspect_evals) | [![[85f9a682fe317d1d3ae42eea038a0e15_MD5.svg]]](https://github.com/UKGovernmentBEIS/inspect_evals) | inspect, eval-suite, reproducibility | Evaluation suite collection for Inspect AI workflows. |
| auto-harness | [GitHub](https://github.com/neosigmaai/auto-harness) | [![[d6ccf7acd052ac38901d386592692fa7_MD5.svg]]](https://github.com/neosigmaai/auto-harness) | optimization, regression, evals | Benchmark-gated optimization loop that mines failures, edits agent code, and guards against regressions overnight. |
| SWE-Bench Pro | [GitHub](https://github.com/scaleapi/SWE-bench_Pro-os) | [![[5c5fa4ad4c2da86725f2e6b58133812b_MD5.svg]]](https://github.com/scaleapi/SWE-bench_Pro-os) | swe, benchmark, long-horizon | Long-horizon software-engineering benchmark with reproducible Docker-based evaluation for issue-driven coding agents. |
| Agent Evaluation | [GitHub](https://github.com/awslabs/agent-evaluation) | [![[aa21c665cd998a568d9fd849dad7b476_MD5.svg]]](https://github.com/awslabs/agent-evaluation) | evaluation, testing, ci | AWS framework for testing virtual agents with evaluator-driven multi-turn conversations, hooks, and CI-friendly workflows. |
| WorkArena | [GitHub](https://github.com/ServiceNow/WorkArena) | [![[9d1194a9cfe99b386d3f1fab586e755a_MD5.svg]]](https://github.com/ServiceNow/WorkArena) | browser, benchmark, enterprise | Browser benchmark for practical enterprise-like knowledge work tasks. |
| OpenHands Benchmarks | [GitHub](https://github.com/OpenHands/benchmarks) | [![[1a879ae72d3d1705d2f448d470e31b3b_MD5.svg]]](https://github.com/OpenHands/benchmarks) | openhands, eval, harness | Evaluation harness and benchmark definitions for OpenHands systems. |
| WebArena-Verified | [GitHub](https://github.com/ServiceNow/webarena-verified) | [![[f380e214954ae07d8dbc17e12fcda73c_MD5.svg]]](https://github.com/ServiceNow/webarena-verified) | web-agent, benchmark, deterministic | Verified web-agent benchmark with deterministic evaluators. |

<a id="observability-reliability-operations"></a>
### Observability & Reliability Operations

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| MLflow | [GitHub](https://github.com/mlflow/mlflow) | [![[1438c65f1867b32a796297a4b1beded1_MD5.svg]]](https://github.com/mlflow/mlflow) | platform, monitoring, evaluation | Broad AI engineering platform with monitoring and evaluation support for agents. |
| Langfuse | [GitHub](https://github.com/langfuse/langfuse) | [![[ea00a5b4c83b235549ba9935d6bfe892_MD5.svg]]](https://github.com/langfuse/langfuse) | llmops, tracing, metrics | Open-source LLM engineering platform for traces, metrics, prompts, and evals. |
| Opik | [GitHub](https://github.com/comet-ml/opik) | [![[4085fecf4dca47c30582a4092be33e93_MD5.svg]]](https://github.com/comet-ml/opik) | monitoring, eval, tracing | End-to-end debug/eval/monitoring stack for LLM apps and agent workflows. |
| RagaAI Catalyst | [GitHub](https://github.com/raga-ai-hub/RagaAI-Catalyst) | [![[7d7c174ae8267dad52d4d76c92f77815_MD5.svg]]](https://github.com/raga-ai-hub/RagaAI-Catalyst) | agentops, analytics, monitoring | Agent observability and monitoring framework with timeline and graph analytics. |
| TensorZero | [GitHub](https://github.com/tensorzero/tensorzero) | [![[1f5af0c18158ad56add09708436dfd18_MD5.svg]]](https://github.com/tensorzero/tensorzero) | llmops, gateway, optimization | Open LLMOps stack unifying gateway, observability, evaluation, and optimization. |
| Arize Phoenix | [GitHub](https://github.com/Arize-ai/phoenix) | [![[6d8ab77e42ae0359796a7451d4a342bd_MD5.svg]]](https://github.com/Arize-ai/phoenix) | observability, tracing, evaluation | Open platform for AI observability, tracing, and evaluation analytics. |
| OpenLLMetry | [GitHub](https://github.com/traceloop/openllmetry) | [![[551341b0107ae27fc14b6f2e7ee7c557_MD5.svg]]](https://github.com/traceloop/openllmetry) | opentelemetry, instrumentation, tracing | OpenTelemetry-based instrumentation for GenAI and LLM applications. |
| Helicone | [GitHub](https://github.com/Helicone/helicone) | [![[ca599f16e74a6a9b512ccab9977bbd26_MD5.svg]]](https://github.com/Helicone/helicone) | monitoring, traffic, production | Lightweight platform for monitoring and evaluating LLM traffic in production. |
| AgentOps SDK | [GitHub](https://github.com/AgentOps-AI/agentops) | [![[3d2f124d3fc5ccd127660b837aca6517_MD5.svg]]](https://github.com/AgentOps-AI/agentops) | agentops, monitoring, cost | Monitoring and benchmarking SDK for agent workflows with cost and trace tracking. |
| Latitude | [GitHub](https://github.com/latitude-dev/latitude-llm) | [![[f6ff963514c5582a0d55643e0ca1a7df_MD5.svg]]](https://github.com/latitude-dev/latitude-llm) | platform, eval, observability | Open-source agent engineering platform with eval and observability capabilities. |
| Laminar | [GitHub](https://github.com/lmnr-ai/lmnr) | [![[9d3e042386bd3a5d260aec24b38de592_MD5.svg]]](https://github.com/lmnr-ai/lmnr) | observability, tracing, evals | Agent-focused observability stack with tracing, evaluation runs, monitoring, and dashboards. |
| claude-code-reverse | [GitHub](https://github.com/Yuyz0112/claude-code-reverse) | [![[f3b71abbecec8864fb5ab8c02009a912_MD5.svg]]](https://github.com/Yuyz0112/claude-code-reverse) | trace, visualization, debugging | Tooling to visualize and inspect Claude Code LLM interaction traces. |
| OpenInference | [GitHub](https://github.com/Arize-ai/openinference) | [![[4408692b9a1d9701f7e22ca00e85298a_MD5.svg]]](https://github.com/Arize-ai/openinference) | spec, instrumentation, observability | Open instrumentation specification and tooling for AI observability. |
| Future AGI | [GitHub](https://github.com/future-agi/future-agi) | [![[effd034c08ae219a0fc176037f8444d0_MD5.svg]]](https://github.com/future-agi/future-agi) | observability, evaluation, guardrails | Self-hostable platform that closes the loop across agent tracing, evaluation, simulation, guardrails, and gateway operations. |

<a id="guardrails-security-governance"></a>
### Guardrails, Security & Governance

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| LiteLLM | [GitHub](https://github.com/BerriAI/litellm) | [![[ea4bc25b202a7d9f558c103488b28d61_MD5.svg]]](https://github.com/BerriAI/litellm) | gateway, proxy, guardrails | Unified LLM gateway/proxy with cost tracking, load balancing, and guardrails. |
| Kong | [GitHub](https://github.com/Kong/kong) | [![[e9ea2ee7d6fea997de51f934970196e9_MD5.svg]]](https://github.com/Kong/kong) | gateway, policy, infra | API and AI gateway infrastructure useful for policy enforcement in agent systems. |
| Portkey Gateway | [GitHub](https://github.com/Portkey-AI/gateway) | [![[78550f1a8d0cebe0f1fbaca69d0291ed_MD5.svg]]](https://github.com/Portkey-AI/gateway) | gateway, guardrails, routing | AI gateway with routing and guardrails for multi-model production traffic. |
| CAI (Cybersecurity AI) | [GitHub](https://github.com/aliasrobotics/cai) | [![[7cb7264b7780c570757931b414583723_MD5.svg]]](https://github.com/aliasrobotics/cai) | security, governance, framework | Security-focused agent framework for offensive/defensive AI workflows. |
| OpenAI Realtime Agents | [GitHub](https://github.com/openai/openai-realtime-agents) | [![[bf24c24a29ee902f1b7a1636f746caf0_MD5.svg]]](https://github.com/openai/openai-realtime-agents) | realtime, orchestration, control | Advanced agentic realtime patterns with structured control and interaction loops. |
| Plano | [GitHub](https://github.com/katanemo/plano) | [![[5b68c7f04ff0da5f75f7592e34050c7b_MD5.svg]]](https://github.com/katanemo/plano) | proxy, safety, data-plane | AI-native proxy and data plane with orchestration, safety, and observability. |
| OpenAI CS Agents Demo | [GitHub](https://github.com/openai/openai-cs-agents-demo) | [![[36e9a8e044496f752b734392fe965362_MD5.svg]]](https://github.com/openai/openai-cs-agents-demo) | demo, handoffs, governance | Customer-service multi-agent demo highlighting handoffs and guardrail-like control points. |
| ContextForge | [GitHub](https://github.com/IBM/mcp-context-forge) | [![[cb2946193a50b3b0f3f410a034105280_MD5.svg]]](https://github.com/IBM/mcp-context-forge) | gateway, governance, observability | Registry and proxy layer that unifies MCP, A2A, and REST/gRPC endpoints with centralized governance and observability. |
| Archestra | [GitHub](https://github.com/archestra-ai/archestra) | [![[0d7e04f36eb3e8c04e2593d90cf97acb_MD5.svg]]](https://github.com/archestra-ai/archestra) | enterprise, guardrails, governance | Enterprise AI platform with guardrails, MCP registry, and orchestration services. |
| Tracecat | [GitHub](https://github.com/TracecatHQ/tracecat) | [![[d48b83ed2feae9f8a49491caff4c7ce6_MD5.svg]]](https://github.com/TracecatHQ/tracecat) | security, automation, policy | AI automation platform for security teams with policy and workflow controls. |
| AgentGateway | [GitHub](https://github.com/agentgateway/agentgateway) | [![[f6ddb106deba692e11c93f5366e0b259_MD5.svg]]](https://github.com/agentgateway/agentgateway) | gateway, mcp, proxy | Agentic proxy gateway for AI agents and MCP server ecosystems. |

<a id="reference-harness-implementations"></a>
### Reference Harness Implementations

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| OpenCode | [GitHub](https://github.com/anomalyco/opencode) | [![[3c1ea3645f88562bbb18a7860c040a22_MD5.svg]]](https://github.com/anomalyco/opencode) | terminal, coding-agent, subagents | Open-source coding agent with built-in plan/build roles, subagents, LSP support, and a client-server runtime. |
| Claude Code | [GitHub](https://github.com/anthropics/claude-code) | [![[030b175c18d68017e83a940268596e56_MD5.svg]]](https://github.com/anthropics/claude-code) | terminal, coding-agent, git-workflows | Official terminal coding agent that understands codebases and executes editing, debugging, and Git workflows through natural language. |
| Gemini CLI | [GitHub](https://github.com/google-gemini/gemini-cli) | [![[84cf51cbe9ec2d9717baf6fb40cd212e_MD5.svg]]](https://github.com/google-gemini/gemini-cli) | terminal, coding-agent, mcp | Open-source terminal agent with built-in tools, MCP support, checkpointing, and sandboxing controls. |
| Codex CLI | [GitHub](https://github.com/openai/codex) | [![[7fdbde0f7ef43e7491c9766b9b094d12_MD5.svg]]](https://github.com/openai/codex) | terminal, coding-agent, local-execution | Terminal-native coding agent that runs locally and exposes practical agent workflows for software tasks. |
| OpenHands | [GitHub](https://github.com/OpenHands/OpenHands) | [![[de6c16675a536fbcc0b305ca18d6a086_MD5.svg]]](https://github.com/OpenHands/OpenHands) | coding-agent, software-engineering, repo | Open-source AI software engineer focused on repo-level coding task execution. |
| OpenManus | [GitHub](https://github.com/FoundationAgents/OpenManus) | [![[57dc02c136bb5ae9a94716a8896095cd_MD5.svg]]](https://github.com/FoundationAgents/OpenManus) | general-agent, autonomy, workflows | Open foundation for broad autonomous agent workflows with coding-heavy use cases. |
| learn-claude-code | [GitHub](https://github.com/shareAI-lab/learn-claude-code) | [![[e7bb5248072419d3af113ae4c818b49f_MD5.svg]]](https://github.com/shareAI-lab/learn-claude-code) | tutorial, harness, claude-code | Hands-on harness tutorial for building Claude Code-like systems from scratch. |
| aider | [GitHub](https://github.com/Aider-AI/aider) | [![[99e300dc2ffa04a47a6d86ceb1f1db1d_MD5.svg]]](https://github.com/Aider-AI/aider) | terminal, repo-map, testing | Terminal coding assistant with repo mapping, git-aware edits, and built-in lint/test feedback loops. |
| Claude Code Plugins: Orchestration and Automation | [GitHub](https://github.com/wshobson/agents) | [![[a2f76e5c3073352fdd25289d129ef91d_MD5.svg]]](https://github.com/wshobson/agents) | claude-code, plugins, orchestration | Production-ready Claude Code plugin marketplace bundling agents, skills, tools, and multi-agent workflow orchestrators. |
| CLI-Anything | [GitHub](https://github.com/HKUDS/CLI-Anything) | [![[88df8161995c921d62b5ce344325d5a6_MD5.svg]]](https://github.com/HKUDS/CLI-Anything) | cli, tool-use, automation | CLI agent system that unifies command-line tool usage in agent loops. |
| NanoClaw | [GitHub](https://github.com/qwibitai/nanoclaw) | [![[cbccd0464df4c46c0ba1990376890e01_MD5.svg]]](https://github.com/qwibitai/nanoclaw) | containers, claude-sdk, scheduling | Container-isolated Claude agent harness with channel routing, scheduled jobs, per-group memory, and small-codebase customization. |
| Qwen Code | [GitHub](https://github.com/QwenLM/qwen-code) | [![[a801e20c61dc2f06ffe00790a9e4acb8_MD5.svg]]](https://github.com/QwenLM/qwen-code) | terminal, coding-agent, cli | Terminal-native open-source coding agent tuned for practical dev loops. |
| SuperClaude Framework | [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework) | [![[9afd0d5f4e114633968220850ec42ba7_MD5.svg]]](https://github.com/SuperClaude-Org/SuperClaude_Framework) | config, personas, workflow | Configuration framework adding commands, personas, and method templates to coding agents. |
| Devika | [GitHub](https://github.com/stitionai/devika) | [![[c9afdfaf81e729d6a7aea84918a248de_MD5.svg]]](https://github.com/stitionai/devika) | assistant, planning, coding | Open-source coding assistant system for planning and implementing development tasks. |
| SWE-agent | [GitHub](https://github.com/SWE-agent/SWE-agent) | [![[7b70722dc92aa8d571ed096914f35e24_MD5.svg]]](https://github.com/SWE-agent/SWE-agent) | swe, issue-fixing, tooling | Research-grade coding agent that resolves GitHub issues with explicit tooling loops. |
| Aperant | [GitHub](https://github.com/AndyMik90/Aperant) | [![[bd377b43978d7e5319bd8760286fa0eb_MD5.svg]]](https://github.com/AndyMik90/Aperant) | coding-agent, parallel, memory | Autonomous multi-agent coding framework with parallel execution, isolated workspaces, QA loops, and persistent memory. |
| Eigent | [GitHub](https://github.com/eigent-ai/eigent) | [![[3fa29d2179226212529d57f5064f4d8e_MD5.svg]]](https://github.com/eigent-ai/eigent) | desktop, cowork, productivity | Open-source desktop cowork agent for autonomous task execution and productivity. |
| IronClaw | [GitHub](https://github.com/nearai/ironclaw) | [![[f8b98728112db1ac31ab729a5ecfac42_MD5.svg]]](https://github.com/nearai/ironclaw) | security, wasm, routines | Security-first personal agent harness with WASM sandboxing, routines, tool plugins, and persistent memory. |
| OpenHarness | [GitHub](https://github.com/HKUDS/OpenHarness) | [![[7f2cb64b5616c1585df27b2915af38a7_MD5.svg]]](https://github.com/HKUDS/OpenHarness) | tool-use, memory, multi-agent | Open agent harness implementation covering tool use, skills, memory, permissions, and multi-agent coordination. |
| GitHub Copilot CLI | [GitHub](https://github.com/github/copilot-cli) | [![[87319c2c63b6371743f2beea26d3dee0_MD5.svg]]](https://github.com/github/copilot-cli) | terminal, coding-agent, mcp | Official terminal coding agent built on GitHub's Copilot harness with MCP extensibility, approval controls, and GitHub-native context. |
| Superset | [GitHub](https://github.com/superset-sh/superset) | [![[ce110ffa325a45aea58a673b8af51c66_MD5.svg]]](https://github.com/superset-sh/superset) | worktrees, desktop, parallel | Worktree-based desktop orchestrator for running and reviewing parallel CLI coding agents from one workspace. |
| Open SWE | [GitHub](https://github.com/langchain-ai/open-swe) | [![[a7df4186ec18c214234a5a0b16418a6e_MD5.svg]]](https://github.com/langchain-ai/open-swe) | async, coding-agent, swe | Asynchronous open-source coding agent focused on software issue workflows. |
| OSAURUS | [GitHub](https://github.com/osaurus-ai/osaurus) | [![[22ea420ed77a94083ece8fff171253e1_MD5.svg]]](https://github.com/osaurus-ai/osaurus) | macos, local-first, memory | Native macOS harness for autonomous coding agents with persistent memory. |
| HiClaw | [GitHub](https://github.com/agentscope-ai/HiClaw) | [![[b254d5eaa705d7512839fc53215d0d46_MD5.svg]]](https://github.com/agentscope-ai/HiClaw) | multi-agent, human-in-the-loop, shared-state | Collaborative multi-agent OS with manager-worker coordination, shared state, and human-in-the-loop oversight via Matrix rooms. |
| mini-swe-agent | [GitHub](https://github.com/SWE-agent/mini-swe-agent) | [![[c1cd4b7fe44556ced8a624f1fe686c75_MD5.svg]]](https://github.com/SWE-agent/mini-swe-agent) | minimal, swe, coding-agent | Minimal coding agent implementation with strong benchmark competitiveness. |
| TinyAGI | [GitHub](https://github.com/TinyAGI/tinyagi) | [![[8ea9455dc257ac2454fa2488ea1290ce_MD5.svg]]](https://github.com/TinyAGI/tinyagi) | team-orchestration, autonomous, workflows | Team-style agent orchestrator for one-person-company style autonomous workflows. |
| Devon | [GitHub](https://github.com/entropy-research/Devon) | [![[95f33f6891c67fc224e3b9c56d608ef0_MD5.svg]]](https://github.com/entropy-research/Devon) | pair-programming, coding-agent, autonomous | Open-source pair programmer agent with autonomous coding execution patterns. |
| oh-my-pi | [GitHub](https://github.com/can1357/oh-my-pi) | [![[0023467bd86e41f28294042f0393a0fa_MD5.svg]]](https://github.com/can1357/oh-my-pi) | terminal, lsp, subagents | Terminal AI coding agent with edit safety, LSP integration, and subagent support. |
| Open Claude Cowork | [GitHub](https://github.com/DevAgentForge/Open-Claude-Cowork) | [![[9881d768d35eabae2b93a24a7aa0be84_MD5.svg]]](https://github.com/DevAgentForge/Open-Claude-Cowork) | desktop, ui, orchestration | Desktop coding cowork assistant that turns agent orchestration into GUI workflows. |
| holaOS | [GitHub](https://github.com/holaboss-ai/holaOS) | [![[80b4d122c923892ad097b75c4a1f7dfb_MD5.svg]]](https://github.com/holaboss-ai/holaOS) | long-horizon, desktop, durable-state | Desktop-first long-horizon agent environment with runtime, memory, tools, apps, and durable state. |
| Amazon Bedrock AgentCore Samples | [GitHub](https://github.com/awslabs/agentcore-samples) | [![[10c89265ae80b91a44edff79c164bcf5_MD5.svg]]](https://github.com/awslabs/agentcore-samples) | aws, runtime, operations | Official sample suite for deploying and operating agents with runtime, gateway, memory, observability, evaluation, and policy layers. |
| mini-coding-agent | [GitHub](https://github.com/rasbt/mini-coding-agent) | [![[0040a80faf0b3130ff8134068a315ff3_MD5.svg]]](https://github.com/rasbt/mini-coding-agent) | coding-agent, minimal, approvals | Minimal coding agent harness illustrating approvals, memory, bounded delegation, and durable transcripts. |

<a id="essential-readings-ecosystem-maps"></a>
### Essential Readings & Ecosystem Maps

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| awesome-claude-code | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) | [![[a13cc817954ec1e2c6df28d51b17e5df_MD5.svg]]](https://github.com/hesreallyhim/awesome-claude-code) | awesome-list, claude-code, skills | Community collection of Claude Code skills, hooks, and orchestrator tooling. |
| awesome-agentic-patterns | [GitHub](https://github.com/nibzard/awesome-agentic-patterns) | [![[cca2eed63d2d193e1c2b66d25e014cb1_MD5.svg]]](https://github.com/nibzard/awesome-agentic-patterns) | awesome-list, patterns, design | Catalog of reusable agentic design patterns and implementation motifs. |
| awesome-mcp-servers | [GitHub](https://github.com/wong2/awesome-mcp-servers) | [![[e43cf8c47851d7e7fead89a41e9f20b0_MD5.svg]]](https://github.com/wong2/awesome-mcp-servers) | awesome-list, mcp, tools | Curated MCP server index for tool interoperability in agent systems. |
| awesome-harness-engineering | [GitHub](https://github.com/walkinglabs/awesome-harness-engineering) | [![[46a1aad5371abafec8e8578d3fc66a86_MD5.svg]]](https://github.com/walkinglabs/awesome-harness-engineering) | awesome-list, curation, harness | Curated list focused on harness engineering articles, benchmarks, and implementations. |
| 12 Factor Agents | [Reference](https://www.humanlayer.dev/blog/12-factor-agents) | - | reading, operations, principles | Operations-oriented principles for building maintainable production agents. |
| Agent Frameworks, Runtimes, and Harnesses, oh my! | [Reference](https://blog.langchain.com/agent-frameworks-runtimes-and-harnesses-oh-my/) | - | reading, langchain, architecture | Clear decomposition of framework vs runtime vs harness responsibilities. |
| An open-source spec for Codex orchestration: Symphony. | [Reference](https://openai.com/index/open-source-codex-orchestration-symphony/) | - | reading, openai, orchestration | OpenAI's orchestration write-up on turning issue trackers into always-on control planes for coding agents. |
| Building agents with the Claude Agent SDK | [Reference](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | - | reading, claude, sdk | Claude blog on production-oriented SDK usage for sessions, tools, and orchestration. |
| Building Effective AI Agents | [Reference](https://www.anthropic.com/engineering/building-effective-agents) | - | reading, anthropic, agents | Anthropic's practical guidance on when to use workflows vs. autonomous agents and how to structure them. |
| Claude Code auto mode | [Referen

[README truncated at 50k characters during raw capture; source URL contains full repository content.]
```
