# AI Research OS — Index
_Last updated: 2026-04-27_

## Concepts (13)
- [agent-memory](concepts/agent-memory.md) — Systems that enable agents to store, retrieve, and learn from historical experiences to improve future reasoning and planning.
- [claude-code-hooks](concepts/claude-code-hooks.md) — Shell commands configured in Claude Code's settings.json that execute at lifecycle events, enabling automated session knowledge capture and context loading.
- [computer-use-agent-verification](concepts/computer-use-agent-verification.md) — Methods and benchmarks for reliably verifying whether autonomous computer-use agents have succeeded on web and GUI tasks.
- [embodied-ai](concepts/embodied-ai.md) — AI systems that perceive, reason, and act within physical environments, bridging digital intelligence with real-world agents.
- [knowledge-compounding](concepts/knowledge-compounding.md) — Property of an LLM knowledge base where each new input and query answer enriches the base, compounding rather than resetting.
- [llm-knowledge-base](concepts/llm-knowledge-base.md) — LLM-maintained repository where an AI reads raw inputs and writes synthesised wiki entries, enabling compounding knowledge accumulation over time.
- [meta-harness](concepts/meta-harness.md) — System where a coding agent autonomously improves LLM evaluation harnesses by reading the full history of prior attempts and proposing targeted modifications.
- [mixture-of-transformers](concepts/mixture-of-transformers.md) — Architecture using modality-specific transformer parameters to improve multi-modal model performance without degrading language capabilities.
- [raw-wiki-pattern](concepts/raw-wiki-pattern.md) — Folder convention where raw/ holds unstructured source material and wiki/ holds LLM-curated knowledge — the LLM is the only writer of wiki/ content.
- [skill-evolution](concepts/skill-evolution.md) — The process by which agent skills improve automatically through usage, feedback, and collective experience aggregation.
- [skill-retrieval](concepts/skill-retrieval.md) — Methods for selecting relevant agent skills from large libraries at inference time, balancing relevance with dependency completeness.
- [web-as-filesystem](concepts/web-as-filesystem.md) — Pattern of mounting web documentation as a Unix filesystem so AI agents can browse docs using cat, grep, tree, and find — eliminating the need for RAG or MCP tool schemas.
- [wiki-agent-memory](concepts/wiki-agent-memory.md) — Pattern of giving an LLM agent lifecycle hooks into a knowledge wiki — loading context on session start, filing insights on session end, and running maintenance on schedule.

## Entities (13)
- [andrej-karpathy](entities/andrej-karpathy.md) — AI researcher and engineer who popularised the raw→wiki LLM knowledge base pattern in April 2026.
- [anthropic](entities/anthropic.md) — AI safety company and creator of Claude, the Claude Agent SDK, and Claude Code — the primary AI infrastructure underlying Self OS.
- [claude-code](entities/claude-code.md) — Anthropic's official CLI for Claude enabling agentic coding sessions with file system access, tool use, hooks, and skills — the primary interface for Self OS on the laptop.
- [hermes-agent](entities/hermes-agent.md) — Open-source AI agent framework by Nous Research that learns from experience by saving reusable procedures as skills and persists memory across sessions via pluggable backends.
- [mem0](entities/mem0.md) — Open-source memory layer for LLM applications providing adaptive personalization.
- [memento](entities/memento.md) — Memory fine-tuning framework for agents that freezes LLMs while optimizing memory parameters.
- [microsoft-research](entities/microsoft-research.md) — Research division of Microsoft, authors of the Universal Verifier for computer-use agents.
- [nia-docs](entities/nia-docs.md) — Tool that mounts any documentation website as a Unix filesystem, letting AI agents browse docs with cat, grep, tree and find — no RAG or MCP schemas needed.
- [notebooklm-py](entities/notebooklm-py.md) — Unofficial Python library and CLI providing full programmatic access to Google NotebookLM, used in Self OS for deep research automation.
- [obsidian](entities/obsidian.md) — Local-first markdown note-taking application with graph view and wikilinks — used as the visual IDE and frontend for the knowledge base.
- [openclaw](entities/openclaw.md) — Open-source personal AI assistant that runs locally and autonomously, capable of self-improving by writing its own skills and maintaining persistent memory via markdown memory files.
- [qwen](entities/qwen.md) — Family of large language and vision-language models by Alibaba Cloud, used in agent and embodied systems.
- [tencent](entities/tencent.md) — Chinese technology company developing embodied AI models including HY-Embodied-0.5.

## Sources (66)
- [aaron-roe-2026-claude-code-patterns](sources/aaron-roe-2026-claude-code-patterns.md) — Community-maintained collection of 137 real-world techniques for Claude Code power users, covering architecture, skills, MCP patterns, hooks, and the AI Wiki Pattern.
- [adam-cad-2026-cadam](sources/adam-cad-2026-cadam.md) — Browser-based text-to-CAD tool generating parametric 3D models via OpenSCAD WebAssembly with real-time previews and interactive parameter sliders.
- [agentic-memory-lhl-2026-04-13](sources/agentic-memory-lhl-2026-04-13.md) — 1|---      2|source: https://github.com/lhl/agentic-memory      3|date: 2026-04-13      4|type: repo      5|tags: [agent...
- [agentscope-2026-reme](sources/agentscope-2026-reme.md) — Memory management framework offering file-based and vector-based systems with context compaction, hybrid retrieval, and SOTA results on LoCoMo and HaluMem benchmarks.
- [aiming-lab-2026-simplemem](sources/aiming-lab-2026-simplemem.md) — Memory framework for LLM agents based on semantic lossless compression, achieving SOTA on LoCoMo and Mem-Gallery benchmarks with minimal token cost via a three-stage pipeline.
- [alishahryar1-2026-free-claude-code](sources/alishahryar1-2026-free-claude-code.md) — Lightweight proxy routing Claude Code's Anthropic API calls to free or local LLM providers, removing the Anthropic API cost barrier.
- [amap-ml-2026-skillclaw](sources/amap-ml-2026-skillclaw.md) — Framework for evolving reusable skills in multi-user OpenClaw-style agent ecosystems by automatically distilling session experience into shared SKILL.md files.
- [arlanr-web-as-filesystem-2026](sources/arlanr-web-as-filesystem-2026.md) — Code hallucination is a docs staleness problem — the solution is mounting documentation sites as Unix filesystems so agents browse with familiar shell tools instead of RAG.
- [awesome-ai-memory-2026-04-13](sources/awesome-ai-memory-2026-04-13.md) — 1|---      2|source: https://github.com/IAAR-Shanghai/Awesome-AI-Memory      3|date: 2026-04-13      4|type: repo      5...
- [cadam-2026-04-26](sources/cadam-2026-04-26.md) — 1|---      2|source: https://github.com/Adam-CAD/CADAM      3|date: 2026-04-26      4|type: repo      5|tags: [text-to-c...
- [claude-code-patterns-2026-04-13](sources/claude-code-patterns-2026-04-13.md) — 1|---      2|source: https://github.com/AaronRoeF/claude-code-patterns      3|date: 2026-04-13      4|type: repo      5|...
- [claude-context-2026-04-26](sources/claude-context-2026-04-26.md) — 1|---      2|source: https://github.com/zilliztech/claude-context      3|date: 2026-04-26      4|type: repo      5|tags:...
- [claude-cookbook-2026](sources/claude-cookbook-2026.md) — Anthropic's official library of practical guides covering agent patterns, Managed Agents, Claude Agent SDK, tool use, RAG, context engineering, and more.
- [cole-medin-2026-parallel-claude-code](sources/cole-medin-2026-parallel-claude-code.md) — Cole Medin's factory system for parallel agent coding using Git worktrees, database branching, adversarial review, and self-healing workflows to achieve 10x output.
- [cole-medin-self-evolving-claude-memory-2026](sources/cole-medin-self-evolving-claude-memory-2026.md) — Applies Karpathy's raw→wiki pattern to internal coding session data using Claude Code hooks and Agent SDK — creating self-evolving memory that compounds with every session.
- [dawei-liu-2026-graph-of-skills](sources/dawei-liu-2026-graph-of-skills.md) — Offline skill graph construction from SKILL.md libraries for dependency-aware retrieval, surfacing relevant skills along with prerequisites and related capabilities.
- [design-md-2026-04-26](sources/design-md-2026-04-26.md) — 1|---      2|source: https://github.com/google-labs-code/design.md      3|date: 2026-04-26      4|type: repo      5|tags...
- [forrestchang-2026-karpathy-skills](sources/forrestchang-2026-karpathy-skills.md) — CLAUDE.md plugin derived from Andrej Karpathy's observations on LLM coding pitfalls, enforcing four principles: Think Before Coding, Simplicity First, Surgical Changes, and Goal-Driven Execution.
- [free-claude-code-2026-04-26](sources/free-claude-code-2026-04-26.md) — 1|---      2|source: https://github.com/Alishahryar1/free-claude-code      3|date: 2026-04-26      4|type: repo      5|t...
- [garry-tan-2026-gbrain](sources/garry-tan-2026-gbrain.md) — Open-source agent brain built on Bun with hybrid search, code intelligence, and automatic typed-link extraction, compatible with OpenClaw and Hermes Agent.
- [garrytan-2026-skillify](sources/garrytan-2026-skillify.md) — Garry Tan's Skillify pattern: every agent failure becomes a permanent structural fix with tests, resolver routing, and daily evals via the 10-step Skillify checklist.
- [gbrain-2026-04-26](sources/gbrain-2026-04-26.md) — 1|---      2|source: https://github.com/garrytan/gbrain      3|date: 2026-04-26      4|type: repo      5|tags: [agent-br...
- [google-labs-2026-design-md](sources/google-labs-2026-design-md.md) — Alpha-format specification from Google Labs for describing visual design systems to coding agents using machine-readable YAML tokens combined with human-readable Markdown rationale.
- [graph-of-skills-2026-04-12](sources/graph-of-skills-2026-04-12.md) — 1|---      2|source: https://github.com/davidliuk/graph-of-skills      3|date: 2026-04-12      4|type: repo      5|tags:...
- [hooeem-extend-claude-sessions-2026](sources/hooeem-extend-claude-sessions-2026.md) — Guide to four workflows for extending Claude sessions beyond context limits, centred on running /wrap-up before closing each session to extract and persist insights.
- [hooeem-llm-knowledge-base-guide-2026](sources/hooeem-llm-knowledge-base-guide-2026.md) — Step-by-step guide covering three levels of LLM knowledge base implementation — no-code, semi-automated, and fully automated with GitHub Actions.
- [hu-jain-2026-amortizing-intractable-inference](sources/hu-jain-2026-amortizing-intractable-inference.md) — ICLR 2024 paper using GFlowNets to fine-tune LLMs for sampling from intractable posteriors, framing chain-of-thought reasoning as latent variable modeling.
- [hust-ai-hyz-2026-memoryagentbench](sources/hust-ai-hyz-2026-memoryagentbench.md) — ICLR 2026 benchmark for agent memory evaluation via incremental multi-turn interactions, testing accurate retrieval, test-time learning, long-range understanding, and conflict resolution.
- [hy-embodied-2026-04-12](sources/hy-embodied-2026-04-12.md) — 1|---      2|source: https://github.com/Tencent-Hunyuan/HY-Embodied      3|date: 2026-04-12      4|type: repo      5|tag...
- [iaar-shanghai-2026-awesome-ai-memory](sources/iaar-shanghai-2026-awesome-ai-memory.md) — Comprehensive curated repository mapping the AI memory landscape for LLMs, cataloguing 300+ papers and 90+ open-source projects across memory taxonomy, operations, and evaluation benchmarks.
- [karpathy-llm-os-tweet-2026](sources/karpathy-llm-os-tweet-2026.md) — Karpathy's tweet describing the raw→wiki LLM knowledge base pattern and framing the LLM as an OS layer for personal knowledge management.
- [karpathy-skills-2026-04-13](sources/karpathy-skills-2026-04-13.md) — 1|---      2|source: https://github.com/forrestchang/andrej-karpathy-skills      3|date: 2026-04-13      4|type: repo   ...
- [khairallah-2026-claude-code-tricks](sources/khairallah-2026-claude-code-tricks.md) — Comprehensive compilation of 35 Claude Code techniques covering session management, productivity, architecture, workflow automation, and debug/recovery.
- [leonard-lin-2026-agentic-memory](sources/leonard-lin-2026-agentic-memory.md) — Curated research collection by Leonard Lin summarising 30+ academic papers and production systems on agent memory architectures, with deep-dive analyses and cross-system comparisons.
- [liu-2026-graph-of-skills](sources/liu-2026-graph-of-skills.md) — Preprint introducing GoS, a graph-structured retrieval layer for large skill libraries that uses reverse-weighted Personalized PageRank to recover prerequisite skills missed by flat semantic retrieval.
- [liu-graph-of-skills-2026](sources/liu-graph-of-skills-2026.md) — GoS constructs an executable skill graph offline and retrieves dependency-aware skill bundles at inference, improving reward by 43.6% while reducing tokens by 37.8%.
- [llm-wiki-v2-karpathy-pattern](sources/llm-wiki-v2-karpathy-pattern.md) — Extends the raw→wiki pattern with agent lifecycle hooks, supersession, retention decay, and quality-gated query filing — automating the bookkeeping that causes wikis to be abandoned.
- [ma-2026-skillclaw](sources/ma-2026-skillclaw.md) — Framework for collective skill evolution in multi-user agent ecosystems, using aggregated session trajectories and an autonomous evolver to refine and create skills continuously.
- [ma-skillclaw-2026](sources/ma-skillclaw-2026.md) — Framework for collective skill evolution in multi-user agent ecosystems that aggregates trajectories across users and evolves skills automatically via an agentic evolver.
- [matt-pocock-2026-skills](sources/matt-pocock-2026-skills.md) — Collection of 15+ agent skills for real engineering workflows from Matt Pocock, covering planning, TDD, triage, refactoring, tooling, and knowledge work.
- [matt-pocock-2026-software-fundamentals](sources/matt-pocock-2026-software-fundamentals.md) — Matt Pocock argues that AI coding amplifies the importance of software engineering fundamentals: design concepts, ubiquitous language, TDD, deep modules, and entropy resistance.
- [matt-pocock-2026-workflow-ai-coding](sources/matt-pocock-2026-workflow-ai-coding.md) — Matt Pocock's complete workflow for AI coding: human-in-the-loop planning with Grill Me, PRD and Kanban issue slicing, then AFK agent implementation via the Ralph loop.
- [mattpocock-2026-afk-agents](sources/mattpocock-2026-afk-agents.md) — Matt Pocock's day-shift/night-shift model: humans plan and QA during the day; AFK agents implement and review in parallel sandboxes overnight.
- [mattpocock-skills-2026-04-26](sources/mattpocock-skills-2026-04-26.md) — 1|---      2|source: https://github.com/mattpocock/skills      3|date: 2026-04-26      4|type: repo      5|tags: [claude...
- [mem0-2026-04-13](sources/mem0-2026-04-13.md) — 1|---      2|source: https://github.com/mem0ai/mem0      3|date: 2026-04-13      4|type: repo      5|tags: [agent-memory...
- [mem0ai-2026-mem0](sources/mem0ai-2026-mem0.md) — Production-ready memory layer for AI assistants and agents with multi-level memory, adaptive personalisation, and cross-platform SDKs.
- [memento-2026-04-13](sources/memento-2026-04-13.md) — 1|---      2|source: https://github.com/microsoft/memento      3|date: 2026-04-13      4|type: repo      5|tags: [contex...
- [memoryagentbench-2026-04-13](sources/memoryagentbench-2026-04-13.md) — 1|---      2|source: https://github.com/HUST-AI-HYZ/MemoryAgentBench      3|date: 2026-04-13      4|type: repo      5|ta...
- [mempalace-2026-04-13](sources/mempalace-2026-04-13.md) — 1|---      2|source: https://github.com/MemPalace/mempalace      3|date: 2026-04-13      4|type: repo      5|tags: [agen...
- [microsoft-2026-memento](sources/microsoft-2026-memento.md) — Microsoft research project that extends effective LLM output length by splitting chain-of-thought into blocks and summaries, evicting blocks from KV cache after summarisation.
- [milla-jovovich-2026-mempalace](sources/milla-jovovich-2026-mempalace.md) — Local-first AI memory system using a palace architecture (wings, rooms, halls, drawers) to organise conversations and projects, achieving 96.6% R@5 on LongMemEval with zero API calls.
- [misaki-akiba-2026-string-seed-of-thought](sources/misaki-akiba-2026-string-seed-of-thought.md) — ICLR 2026 paper introducing SSoT, a two-stage prompting method that improves probabilistic instruction following by using random strings as entropy seeds.
- [multica-2026-04-13](sources/multica-2026-04-13.md) — 1|---      2|source: https://github.com/multica-ai/multica      3|date: 2026-04-13      4|type: repo      5|tags: [manag...
- [multica-ai-2026-multica](sources/multica-ai-2026-multica.md) — Open-source managed agents platform that turns coding agents into team members with task assignment, autonomous execution, skill compounding, and unified runtime management.
- [notebooklm-py-repo](sources/notebooklm-py-repo.md) — Unofficial Python library and CLI for Google NotebookLM with native Claude Code skill integration, used in Self OS for deep research automation.
- [qiao-2026-memory-intelligence-agent](sources/qiao-2026-memory-intelligence-agent.md) — Deep research agent framework using Manager-Planner-Executor architecture with alternating RL, test-time learning, and bidirectional parametric/non-parametric memory evolution.
- [qiao-memory-intelligence-agent-2026](sources/qiao-memory-intelligence-agent-2026.md) — MIA decouples deep research agents into Manager-Planner-Executor with alternating RL training, test-time Planner evolution, and a bidirectional parametric/non-parametric memory loop.
- [reme-2026-04-13](sources/reme-2026-04-13.md) — 1|---      2|source: https://github.com/agentscope-ai/ReMe      3|date: 2026-04-13      4|type: repo      5|tags: [agent...
- [sharma-2026-cua-verifier](sources/sharma-2026-cua-verifier.md) — Microsoft Research paper presenting four design principles for reliable CUA trajectory verification, the Universal Verifier system, and the CUAVerifierBench benchmark.
- [sharma-cua-verifier-2026](sources/sharma-cua-verifier-2026.md) — Microsoft Research's design principles and implementation of the Universal Verifier for CUA trajectories, introducing CUAVerifierBench and separating process from outcome rewards.
- [simplemem-2026-04-13](sources/simplemem-2026-04-13.md) — 1|---      2|source: https://github.com/aiming-lab/SimpleMem      3|date: 2026-04-13      4|type: repo      5|tags: [age...
- [skillclaw-2026-04-12](sources/skillclaw-2026-04-12.md) — 1|---      2|source: https://github.com/AMAP-ML/SkillClaw      3|date: 2026-04-12      4|type: repo      5|tags: [skill-...
- [tencent-2026-hy-embodied](sources/tencent-2026-hy-embodied.md) — Tencent's family of embodied foundation models for real-world agents, featuring a Mixture-of-Transformers architecture with 2B edge and 32B reasoning variants trained on 100M+ embodied data points.
- [tencent-hy-embodied-2026](sources/tencent-hy-embodied-2026.md) — Tencent's family of embodied VLMs built for real-world agents using Mixture-of-Transformers architecture, native-resolution ViT, and iterative self-evolving post-training.
- [yoonholeee-meta-harness-2026](sources/yoonholeee-meta-harness-2026.md) — Research introducing Meta-Harness — a coding agent that autonomously optimises LLM evaluation harnesses by reading the full history of prior attempts.
- [zilliztech-2026-claude-context](sources/zilliztech-2026-claude-context.md) — MCP plugin from Zilliz that adds hybrid semantic code search to Claude Code and other AI coding agents, reducing token usage by ~40% through Milvus-backed retrieval.

## Syntheses (1)
- [claude-code-vs-hermes-vs-openclaw-knowledge-building](syntheses/claude-code-vs-hermes-vs-openclaw-knowledge-building.md) — Comparative analysis of three autonomous AI agent platforms on their capacity for self-directed knowledge accumulation, skill evolution, and persistent memory.

## Outputs (0)
_No outputs yet._

