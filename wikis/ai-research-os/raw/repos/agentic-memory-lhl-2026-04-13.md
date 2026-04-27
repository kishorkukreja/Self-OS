---
status: processed
---
     1|---
     2|source: https://github.com/lhl/agentic-memory
     3|date: 2026-04-13
     4|type: repo
     5|tags: [agent-memory, research-collection, memory-architectures, persistence]
     6|status: raw
     7|---
     8|
     9|# Agentic Memory Research
    10|
    11|Research collection on agent memory architectures, persistence patterns, and output quality maintenance for LLM-based agent systems.
    12|
    13|## Citation
    14|
    15|If you reference this repo�s summaries/analyses in academic or professional work, please cite:
    16|
    17|```bibtex
    18|@misc{lin_agentic_memory_2026,
    19|  author       = {Leonard Lin},
    20|  title        = {agentic-memory: Agentic Memory Research Collection (Summaries and Analyses)},
    21|  year         = {2026},
    22|  howpublished = {GitHub repository},
    23|  url          = {https://github.com/lhl/agentic-memory},
    24|}
    25|```
    26|
    27|## Reference Summaries
    28|
    29|| Document | Author | Description |
    30||----------|--------|-------------|
    31|| [jumperz-agent-memory-stack](references/jumperz-agent-memory-stack.md) | @jumperz | **31-piece memory architecture** split across 3 phases (Core ? Reliability ? Intelligence). Complete prompt/spec breakdowns for write pipeline, read pipeline, decay, knowledge graph, episodic memory, trust scoring, echo/fizzle feedback loops. The foundational reference that others build on. |
    32|| [joelhooks-adr-0077-memory-system-next-phase](references/joelhooks-adr-0077-memory-system-next-phase.md) | @joelhooks | **ADR for joelclaw** (personal AI Mac Mini). Maps existing production system (~6 days running, Qdrant 1,343 points) against jumperz's 31 pieces. Plans 3 increments: retrieval quality (score decay, query rewriting), storage quality (dedup, nightly maintenance), feedback loop (echo/fizzle). Includes detailed gap analysis. |
    33|| [coolmanns-openclaw-memory-architecture](references/coolmanns-openclaw-memory-architecture.md) | coolmanns | **12-layer production memory stack** for OpenClaw with 14 agents. SQLite+FTS5 knowledge graph (3,108 facts), llama.cpp GPU embeddings (768d, 7ms), three runtime plugins (continuity, stability, graph-memory). 100% recall on 60-query benchmark. Includes activation/decay system, domain RAG, session boot sequences. |
    34|| [drag88-agent-output-degradation](references/drag88-agent-output-degradation.md) | @drag88 (Aswin) | **"Why Your Agent's Output Gets Worse Over Time"** � multi-agent convergence problem. 4-tier memory (working ? episodic ? semantic ? procedural). 3-layer enforcement pipeline (YAML regex ? Gemini LLM judge ? self-learning loop). Core insight: convert expensive runtime LLM checks into free static regex rules over time. |
    35|| [versatly-clawvault](references/versatly-clawvault.md) | Versatly (@drag88) | **ClawVault** npm CLI tool � structured markdown memory vault with observation pipeline, knowledge graph, session lifecycle (wake/sleep/checkpoint), task/project primitives, Obsidian integration, OpenClaw hooks. 449+ tests. v2.6.1. |
    36|| [vstorm-memv](references/vstorm-memv.md) | vstorm-co | **memv** (PyPI: `memvee`) � Nemori-inspired predict-calibrate extraction + episode segmentation, plus Graphiti-style bi-temporal validity and hybrid retrieval (sqlite-vec + FTS5 + RRF) on SQLite. |
    37|| [supermemory](references/supermemory.md) | Dhravya Shah / supermemoryai | **Supermemory** memory-as-a-service API: memory versioning (linked-list chains), typed relationships (`updates`/`extends`/`derives`), static/dynamic profile synthesis, time-based forgetting with reason tracking, multi-model embedding storage. **Critical caveat**: open-source repo is frontend/SDK only; core engine is proprietary backend at `api.supermemory.ai`. |
    38|
    39|## Paper Reference Summaries (Academic / Industry)
    40|
    41|| Document | Author | Description |
    42||----------|--------|-------------|
    43|| [hu-evermembench](references/hu-evermembench.md) | Hu et al. | **EverMemBench** benchmark for >1M-token multi-party, multi-group interleaved conversations; diagnoses multi-hop collapse, temporal/versioning difficulty, and retrieval-bottlenecked �memory awareness�. |
    44|| [zhang-live-evo](references/zhang-live-evo.md) | Zhang et al. | **Live-Evo**: online self-evolving agent memory with an experience bank + meta-guideline bank, contrastive �memory-on vs memory-off� feedback, and weight-based reinforcement/forgetting; evaluated on Prophet Arena + deep research (as reported). |
    45|| [shutova-structmemeval](references/shutova-structmemeval.md) | Shutova et al. | **StructMemEval** benchmark for whether agents can organize memory into useful structures (trees/ledgers/state tracking), not just retrieve facts; includes hint vs no-hint evaluation to isolate �structure recognition� failures. |
    46|| [yan-gam](references/yan-gam.md) | Yan et al. | **GAM**: just-in-time agent memory via lightweight memos + a universal page-store, plus a deep-research researcher that plans/searches/integrates/reflects over history to compile optimized context at runtime; strong long-context QA gains with higher latency (as reported). |
    47|| [yang-graph-based-agent-memory-taxonomy](references/yang-graph-based-agent-memory-taxonomy.md) | Yang et al. | **Graph-based Agent Memory survey**: graph-centric taxonomy + lifecycle (extract/store/retrieve/evolve), storage structures (KG/temporal/hyper/hierarchical/hybrid), retrieval operators, evolution/maintenance, and resources/benchmarks; useful shared vocabulary for shisad. |
    48|| [zhang-survey-memory-mechanism](references/zhang-survey-memory-mechanism.md) | Zhang et al. | **Survey on memory mechanisms for LLM agents**: definitions, why memory, design axes (sources/forms/ops), evaluation approaches, and application domains; good baseline checklist alongside newer benchmarks/systems. |
    49|| [hu-memory-age-ai-agents](references/hu-memory-age-ai-agents.md) | Hu et al. | **Memory in the Age of AI Agents survey**: proposes unified lenses of **forms** (token/parametric/latent), **functions** (factual/experiential/working), and **dynamics** (formation/evolution/retrieval), plus benchmarks/frameworks and trustworthiness frontiers. |
    50|| [li-locomoplus](references/li-locomoplus.md) | Li et al. | **LoCoMo-Plus**: evaluates beyond-factual �cognitive memory� (latent constraints like state/goals/values) under cue�trigger semantic disconnect, using constraint-consistency + LLM-judge evaluation. |
    51|| [maharana-locomo](references/maharana-locomo.md) | Maharana et al. | **LoCoMo** dataset + benchmark for very long-term multi-session conversations (300 turns, multimodal) grounded in personas + temporal event graphs; evaluates QA + event summarization + multimodal generation. |
    52|| [wu-longmemeval](references/wu-longmemeval.md) | Wu et al. | **LongMemEval** benchmark + design decomposition (**indexing ? retrieval ? reading**) and system optimizations (value granularity, key expansion, time-aware query expansion). |
    53|| [packer-memgpt](references/packer-memgpt.md) | Packer et al. | **MemGPT**: OS-inspired hierarchical memory + paging between a fixed-context LLM prompt and external stores (recall + archival), with function-call memory ops and event-driven control flow; foundational baseline for external agent memory. |
    54|| [chhikara-mem0](references/chhikara-mem0.md) | Chhikara et al. | **Mem0**: production-oriented long-term memory pipeline with explicit ops (**ADD/UPDATE/DELETE/NOOP**) and an optional **graph memory** variant; reports quality + token/latency tradeoffs on LoCoMo. |
    55|| [liu-simplemem](references/liu-simplemem.md) | Liu et al. | **SimpleMem**: write-time semantic structured compression + online synthesis + intent-aware retrieval planning (multi-view dense/BM25/symbolic retrieval with union+dedup) to improve LoCoMo/LongMemEval quality while cutting token cost (as reported). |
    56|| [xu-a-mem](references/xu-a-mem.md) | Xu et al. | **A?Mem**: Zettelkasten-inspired note network with LLM-driven link generation and �memory evolution� (updating older note attributes as new evidence arrives); strong LoCoMo multi-hop/temporal gains with far lower token lengths than full-context (as reported). |
    57|| [salama-meminsight](references/salama-meminsight.md) | Salama et al. | **MemInsight**: autonomous memory augmentation that mines/annotates attributes (entity-centric + conversation-centric; turn/session granularity) and uses attribute-guided retrieval; large LoCoMo retrieval recall gains vs DPR RAG baseline (as reported). |
    58|| [rasmussen-zep](references/rasmussen-zep.md) | Rasmussen et al. | **Zep**: production memory layer built on **Graphiti**, a **bi-temporal** knowledge graph (episodes ? entities/facts ? communities) with validity intervals and invalidation-based corrections; evaluated on DMR + LongMemEval. |
    59|| [nan-nemori](references/nan-nemori.md) | Nan et al. | **Nemori**: cognitively-inspired self-organizing agent memory with semantic episode boundary detection + episodic narratives and a predict-calibrate loop that distills semantic knowledge from prediction gaps; strong LoCoMo + LongMemEvalS results (as reported). |
    60|| [li-memos](references/li-memos.md) | Li et al. | **MemOS**: OS-like memory control plane with MemCube (payload+metadata), lifecycle/scheduling, governance (ACL/TTL/audit), and multi-substrate memory (plaintext/activation/KV/parameter/LoRA). |
    61|| [yan-memory-r1](references/yan-memory-r1.md) | Yan et al. | **Memory-R1**: reinforcement-learned memory manager (ADD/UPDATE/DELETE/NOOP) + answer agent with learned memory distillation; data-efficient RL (PPO/GRPO) training with exact-match reward. |
    62|| [jonelagadda-mnemosyne](references/jonelagadda-mnemosyne.md) | Jonelagadda et al. | **Mnemosyne**: edge-friendly graph memory with substance/redundancy filters, probabilistic recall with decay/refresh, and a fixed-budget �core summary� for persona-level context. |
    63|| [patel-engram](references/patel-engram.md) | Patel et al. | **ENGRAM**: lightweight typed memory (episodic/semantic/procedural) with simple dense retrieval + strict evidence budgets; strong LoCoMo + LongMemEval results with low token usage. |
    64|| [wei-evo-memory](references/wei-evo-memory.md) | Wei et al. | **Evo-Memory**: streaming benchmark + framework for self-evolving memory and experience reuse; introduces ExpRAG and ReMem (Think/Act/Refine) baselines and robustness/efficiency metrics. |
    65|| [cao-remember-me-refine-me](references/cao-remember-me-refine-me.md) | Cao et al. | **ReMe**: dynamic procedural memory lifecycle (acquire?reuse?refine) with multi-faceted distillation from success/failure trajectories, scenario-aware retrieval, and utility-based pruning; strong BFCL?V3/AppWorld results (as reported). |
    66|| [sarin-memoria](references/sarin-memoria.md) | Sarin et al. | **Memoria**: personalization memory layer combining session summaries + KG triplets (persona) with exponential recency weighting; SQLite + ChromaDB architecture and LongMemEvals subset results. |
    67|| [latimer-hindsight](references/latimer-hindsight.md) | Latimer et al. | **Hindsight**: retain/recall/reflect architecture separating evidence vs beliefs vs summaries; temporal+entity memory graph with multi-channel retrieval fusion and belief confidence updates; very strong LongMemEval/LoCoMo results (as reported). |
    68|| [yu-agentic-memory](references/yu-agentic-memory.md) | Yu et al. | **AgeMem**: RL-trained unified LTM+STM controller exposing memory ops as tool actions (add/update/delete/retrieve/summarize/filter) with a 3-stage curriculum and step-wise GRPO for credit assignment. |
    69|| [hu-evermemos](references/hu-evermemos.md) | Hu et al. | **EverMemOS**: self-organizing �memory OS� with MemCells?MemScenes lifecycle, user profile consolidation, and necessity/sufficiency-guided recollection (verifier + query rewrite); strong LoCoMo/LongMemEval results (as reported). |
    70|| [li-timem](references/li-timem.md) | Li et al. | **TiMem**: temporal-hierarchical memory consolidation (segment?session?day?week?profile) with query-complexity recall planning + gating; strong LoCoMo/LongMemEval-S accuracy with low recalled tokens (as reported). |
    71|| [zhang-himem](references/zhang-himem.md) | Zhang et al. | **HiMem**: hierarchical long-term memory split (Episode Memory + Note Memory) with topic+surprise episode segmentation, note-first �best-effort� retrieval w/ sufficiency checks, and conflict-aware reconsolidation; strong LoCoMo results (as reported). |
    72|| [behrouz-nested-learning](references/behrouz-nested-learning.md) | Behrouz et al. | **Nested Learning / CMS / Hope**: reframes memory as **multi-timescale update dynamics** (continuum memory blocks updated at different frequencies) with implications for consolidation and �corrections without forgetting�. |
    73|| [zhang-recursive-language-models](references/zhang-recursive-language-models.md) | Zhang et al. | **Recursive Language Models (RLMs)**: inference-time recursion + REPL state treats long prompts as an external environment; processes multi?million-token inputs with sub-calls and programmatic slicing, often beating long-context scaffolds at comparable average cost (as reported). |
    74|| [wang-m-plus](references/wang-m-plus.md) | Wang et al. | **M+**: latent-space long-term memory extension to MemoryLLM that stores dropped memory tokens in an LTM pool and retrieves them during generation with a co-trained retriever; extends retention to >160k tokens at similar GPU memory cost (as reported). |
    75|| [dong-minja](references/dong-minja.md) | Dong et al. | **MINJA**: practical **memory injection attack** on �memory-as-demonstrations� agents via query-only interaction (bridging steps + progressive shortening); motivates write-time gates, isolation, and safer memory representations. |
    76|| [sunil-memory-poisoning-attack-defense](references/sunil-memory-poisoning-attack-defense.md) | Sunil et al. | **Memory poisoning attack & defense**: empirical MINJA follow-up in EHR agents; shows pre-existing benign memory can reduce ASR, and that trust-score defenses can fail via over-conservatism or overconfidence. |
    77|| [anokhin-arigraph](references/anokhin-arigraph.md) | Anokhin et al. | **AriGraph**: knowledge-graph world model that links **episodic observation nodes** to extracted semantic triplets; two-stage retrieval (semantic?episodic) for planning/exploration in text-game environments. |
    78|| [behrouz-titans](references/behrouz-titans.md) | Behrouz et al. | **Titans**: long-context architecture with an online-updated **neural memory module** (test-time learning) plus persistent task memory; provides explicit primitives for surprise-based salience and forgetting. |
    79|| [ahn-hema](references/ahn-hema.md) | Ahn | **HEMA**: hippocampus-inspired dual memory for long conversations (running compact summary + FAISS episodic vector store) with explicit prompt budgeting, pruning (�semantic forgetting�), and summary-of-summaries consolidation. |
    80|| [tan-membench](references/tan-membench.md) | Tan et al. | **MemBench**: benchmark/dataset for agent memory covering **participation vs observation** scenarios and **factual vs reflective** memory, with metrics for accuracy/recall/capacity and read/write-time efficiency. |
    81|
    82|## Deep Dive Analyses
    83|
    84|Root-level critical analyses intended for synthesis work. These reference the summaries above, but focus on coherence, evidence quality, risks, and synthesis-ready claim framing.
    85|
    86|| Synthesis | Based on | Focus |
    87||----------|----------|-------|
    88|| [ANALYSIS](ANALYSIS.md) | `ANALYSIS-*.md` + shisad docs + Mem0/Letta baselines | Cross-system comparison (techniques + memory types), plus mapping to shisad and �traditional� RAG-ish memory |
    89|| [ANALYSIS-academic-industry](ANALYSIS-academic-industry.md) | paper `ANALYSIS-arxiv-*.md` + shisad plan | Academic/industry synthesis: benchmarks vs systems vs attacks, with �what�s missing in shisad� framing |
    90|| [Benchmarks best practices](benchmarks/README.md) | Public disputes, audits, our analysis | Known pitfalls, metric confusion, dataset quality issues, per-benchmark limitations |
    91|| [MELT benchmark design](https://github.com/shisa-ai/MELT) | ANALYSIS.md systems + Reality Check epistemic docs | **Memory Evaluation for Lifecycle Testing** � session-replay benchmark testing full memory lifecycle (decay, consolidation, contradiction, core stability, inference) at 6 scale tiers over simulated time. Separate repo; draft. |
    92|
    93|| Analysis | Based on | Focus |
    94||----------|----------|-------|
    95|| [ANALYSIS-jumperz-agent-memory-stack](ANALYSIS-jumperz-agent-memory-stack.md) | `references/jumperz-agent-memory-stack.md` | Checklist critique (semantics, failure modes, missing evaluation), synthesis-ready takeaways + claims table |
    96|| [ANALYSIS-joelhooks-adr-0077-memory-system-next-phase](ANALYSIS-joelhooks-adr-0077-memory-system-next-phase.md) | `references/joelhooks-adr-0077-memory-system-next-phase.md` | Increment plan critique (decay, rewrite, dedup, echo/fizzle), validation plan + claims |
    97|| [ANALYSIS-coolmanns-openclaw-memory-architecture](ANALYSIS-coolmanns-openclaw-memory-architecture.md) | `references/coolmanns-openclaw-memory-architecture.md` + `vendor/openclaw-memory-architecture/` | Layered stack critique with benchmark-method verification, operational risks, doc drift notes |
    98|| [ANALYSIS-drag88-agent-output-degradation](ANALYSIS-drag88-agent-output-degradation.md) | `references/drag88-agent-output-degradation.md` | Convergence + enforcement pattern critique (judge?rule distillation), measurement gaps, risks |
    99|| [ANALYSIS-versatly-clawvault](ANALYSIS-versatly-clawvault.md) | `references/versatly-clawvault.md` + `vendor/clawvault/` | Product/tooling critique (surface area, hooks, qmd dependency), security posture, missing benchmarks |
   100|| [ANALYSIS-vstorm-memv](ANALYSIS-vstorm-memv.md) | `references/vstorm-memv.md` + `vendor/memv/` | Implementation critique of Nemori-inspired predict-calibrate extraction + bi-temporal validity + hybrid retrieval, with gaps/risks and shisad mapping |
   101|| [ANALYSIS-openviking](ANALYSIS-openviking.md) | `vendor/openviking/` + Hermes provider docs | Open-source context database: `viking://` filesystem, L0/L1/L2 tiered loading, session-commit extraction across 8 memory categories, and hierarchical typed retrieval over memory/resources/skills; strong observability with heavier operational complexity |
   102|| [ANALYSIS-byterover-cli](ANALYSIS-byterover-cli.md) | `vendor/byterover-cli/` + `vendor/byterover-cli/paper/` | Agent-native coding-agent memory/runtime: daemon + per-project agent pool, markdown context tree with explicit relations and lifecycle, 5-tier progressive retrieval with cache/OOD detection, and strong self-reported benchmarks with caveats |
   103|| [ANALYSIS-mira-OSS](ANALYSIS-mira-OSS.md) | `vendor/mira-OSS/` | Full-stack event-driven agent (v1 rev 2): activity-day sigmoid decay, hub discovery + 3-axis linking (vector+entity+TF-IDF), Text-Based LoRA + user model synthesis with critic validation, background forage agent (sub-agent collaboration), portrait synthesis, 16 tools, context overflow remediation, immutable domain models, multi-user RLS + Vault; gaps in write gating, external benchmarks, taint tracking, and sub-agent capability scoping |
   104|| [ANALYSIS-claude-code-memory](ANALYSIS-claude-code-memory.md) | Source: `/home/lhl/Downloads/claude-code/src` | **Claude Code memory subsystem (Anthropic)**: first-party production-scale memory system; flat-file MEMORY.md + typed topic files (user/feedback/project/reference) + background extraction via forked agent with mutual exclusion + LLM-based relevance selection (Sonnet) + team memory with OAuth sync + auto dream consolidation + KAIROS daily-log mode + eval-validated prompts with case IDs + security-hardened path validation; no vector search, no graph, no decay scoring |
   105|| [ANALYSIS-codex-memory](ANALYSIS-codex-memory.md) | [openai/codex](https://github.com/openai/codex) | **Codex memory subsystem (OpenAI)**: first-party open-source coding agent; two-phase async pipeline (gpt-5.1-codex-mini extraction ? gpt-5.3-codex consolidation) + SQLite-backed job coordination (leases/heartbeats/watermarks) + progressive disclosure layout (memory_summary ? MEMORY.md ? rollout_summaries ? skills) + skills as procedural memory + usage-based citation-driven retention + thread-diff incremental forgetting + ~1,400 lines extraction/consolidation prompts; no vector search, no team memory, no real-time extraction |
   106|| [ANALYSIS-google-always-on-memory-agent](ANALYSIS-google-always-on-memory-agent.md) | `vendor/always-on-memory-agent/` | Official Google ADK sample: always-on daemon with multimodal ingestion (27 file types via Gemini 3.1 Flash-Lite), periodic LLM consolidation, SQLite storage, HTTP API + Streamlit dashboard; no retrieval/search (recency scan LIMIT 50), no decay/dedup/versioning; useful as ADK orchestration reference and multimodal ingestion pattern |
   107|| [ANALYSIS-supermemory](ANALYSIS-supermemory.md) | `references/supermemory.md` + `vendor/supermemory/` | Memory-as-a-service startup: memory versioning (linked-list chains via parentMemoryId/rootMemoryId/isLatest), typed relationship ontology (updates/extends/derives), static/dynamic profile synthesis API, time-based forgetting with audit trail, multi-model embedding columns, MemoryBench framework; **open-source repo is SDK/frontend only � core engine logic is proprietary hosted backend** |
   108|| [ANALYSIS-karta](ANALYSIS-karta.md) | `vendor/karta/` | **Karta (rohithzr)**: Rust (~10.4K LOC) agentic memory library with Zettelkasten-inspired knowledge graph, 7-type dream engine (deduction/induction/abduction/consolidation/contradiction/episode digest/cross-episode digest) with inference feedback into retrieval, embedding-based query classification (6 modes), retroactive context evolution with drift protection, cross-encoder reranking with abstention, multi-hop BFS traversal, atomic fact decomposition with per-fact embeddings, foresight signals with TTL, structured episode digests; BEAM 100K: 57.7% with 243-failure root cause catalog |
   109|
   110|## Paper Deep Dive Analyses (Academic / Industry)
   111|
   112|| Analysis | Based on | Focus |
   113||----------|----------|-------|
   114|| [ANALYSIS-arxiv-2602.01313-evermembench](ANALYSIS-arxiv-2602.01313-evermembench.md) | `references/hu-evermembench.md` + `references/papers/arxiv-2602.01313.pdf` | Benchmark critique emphasizing version semantics, multi-party fragmentation, oracle diagnostics, and shisad mapping |
   115|| [ANALYSIS-arxiv-2602.02369-live-evo](ANALYSIS-arxiv-2602.02369-live-evo.md) | `references/zhang-live-evo.md` + `references/papers/arxiv-2602.02369.pdf` | System deep dive emphasizing online experience weighting from continuous feedback, meta-guidelines for memory compilation, and memory-on vs memory-off utility measurement; shisad mapping for feedback loops + procedural memory gating |
   116|| [ANALYSIS-arxiv-2602.11243-structmemeval](ANALYSIS-arxiv-2602.11243-structmemeval.md) | `references/shutova-structmemeval.md` + `references/papers/arxiv-2602.11243.pdf` | Benchmark deep dive emphasizing memory organization/structure as a distinct capability (trees/ledgers/state), hint vs no-hint diagnostics, and implications for shisad structured-memory primitives |
   117|| [ANALYSIS-arxiv-2602.05665-graph-based-agent-memory-taxonomy](ANALYSIS-arxiv-2602.05665-graph-based-agent-memory-taxonomy.md) | `references/yang-graph-based-agent-memory-taxonomy.md` + `references/papers/arxiv-2602.05665.pdf` | Survey deep dive providing graph-based memory taxonomy and lifecycle (extract/store/retrieve/evolve), with implications for shisad graph-as-derived-view, operator choices, and maintenance jobs |
   118|| [ANALYSIS-arxiv-2404.13501-survey-memory-mechanism](ANALYSIS-arxiv-2404.13501-survey-memory-mechanism.md) | `references/zhang-survey-memory-mechanism.md` + `references/papers/arxiv-2404.13501.pdf` | Survey deep dive providing baseline taxonomy and evaluation checklists for agent memory; useful coverage reference alongside newer benchmarks/systems for shisad�s roadmap |
   119|| [ANALYSIS-arxiv-2512.13564-memory-age-ai-agents](ANALYSIS-arxiv-2512.13564-memory-age-ai-agents.md) | `references/hu-memory-age-ai-agents.md` + `references/papers/arxiv-2512.13564.pdf` | Survey deep dive emphasizing the Forms�Functions�Dynamics taxonomy and frontiers (RL integration, multimodal, multi-agent shared memory, trustworthiness), used as organizing frame for shisad v0.7 memory roadmap |
   120|| [ANALYSIS-arxiv-2402.17753-locomo](ANALYSIS-arxiv-2402.17753-locomo.md) | `references/maharana-locomo.md` + `references/papers/arxiv-2402.17753.pdf` | Dataset/benchmark critique with episodic-memory implications (event graphs, multimodal, RAG harm) and shisad mapping |
   121|| [ANALYSIS-arxiv-2410.10813-longmemeval](ANALYSIS-arxiv-2410.10813-longmemeval.md) | `references/wu-longmemeval.md` + `references/papers/arxiv-2410.10813.pdf` | Benchmark and system-design decomposition (indexing/retrieval/reading), with mapping to shisad primitives |
   122|| [ANALYSIS-arxiv-2310.08560-memgpt](ANALYSIS-arxiv-2310.08560-memgpt.md) | `references/packer-memgpt.md` + `references/papers/arxiv-2310.08560.pdf` | System deep dive emphasizing virtual context management (OS paging), memory tiers (working/queue/recall/archival), function-call memory ops, and implications for shisad versioned corrections + write-policy hardening |
   123|| [ANALYSIS-arxiv-2602.10715-locomoplus](ANALYSIS-arxiv-2602.10715-locomoplus.md) | `references/li-locomoplus.md` + `references/papers/arxiv-2602.10715.pdf` | Beyond-factual �cognitive memory� benchmark critique (latent constraints) and implications for safe constraint/procedural memory |
   124|| [ANALYSIS-arxiv-2504.19413-mem0](ANALYSIS-arxiv-2504.19413-mem0.md) | `references/chhikara-mem0.md` + `references/papers/arxiv-2504.19413.pdf` | System deep dive emphasizing explicit memory ops, graph-memory tradeoffs, deployment metrics (tokens/p95), and shisad mapping (versioned corrections vs delete) |
   125|| [ANALYSIS-arxiv-2601.02553-simplemem](ANALYSIS-arxiv-2601.02553-simplemem.md) | `references/liu-simplemem.md` + `references/papers/arxiv-2601.02553.pdf` | System deep dive emphasizing write-time semantic structured compression, online consolidation, and intent-aware multi-view retrieval planning; mapping to shisad �derived vs raw� memory + retrieval budgeting |
   126|| [ANALYSIS-arxiv-2502.12110-a-mem](ANALYSIS-arxiv-2502.12110-a-mem.md) | `references/xu-a-mem.md` + `references/papers/arxiv-2502.12110.pdf` | System deep dive emphasizing Zettelkasten-style notes + LLM-driven linking + memory evolution, with strong multi-hop/temporal LoCoMo gains but high versioning/audit requirements for shisad |
   127|| [ANALYSIS-arxiv-2503.21760-meminsight](ANALYSIS-arxiv-2503.21760-meminsight.md) | `references/salama-meminsight.md` + `references/papers/arxiv-2503.21760.pdf` | System deep dive emphasizing autonomous attribute mining/annotation as a derived metadata layer to improve retrieval recall and downstream tasks; mapping to shisad schema constraints + provenance/versioning |
   128|| [ANALYSIS-arxiv-2511.18423-gam](ANALYSIS-arxiv-2511.18423-gam.md) | `references/yan-gam.md` + `references/papers/arxiv-2511.18423.pdf` | System deep dive emphasizing just-in-time context compilation via memo index + universal page-store and an iterative deep-research researcher; highlights the latency/quality trade-off and mapping to shisad evidence-first episodic storage |
   129|| [ANALYSIS-arxiv-2501.13956-zep](ANALYSIS-arxiv-2501.13956-zep.md) | `references/rasmussen-zep.md` + `references/papers/arxiv-2501.13956.pdf` | System deep dive emphasizing bi-temporal validity semantics, episodic+semantic+community graph tiers, hybrid retrieval (BM25/embeddings/BFS), and implications for shisad versioned memory |
   130|| [ANALYSIS-arxiv-2507.03724-memos](ANALYSIS-arxiv-2507.03724-memos.md) | `references/li-memos.md` + `references/papers/arxiv-2507.03724.pdf` | System deep dive emphasizing MemCube metadata, multi-substrate memory (plaintext/KV/parameter), lifecycle/scheduling/governance, and mapping to shisad primitives |
   131|| [ANALYSIS-arxiv-2508.19828-memory-r1](ANALYSIS-arxiv-2508.19828-memory-r1.md) | `references/yan-memory-r1.md` + `references/papers/arxiv-2508.19828.pdf` | RL deep dive emphasizing learned memory ops (ADD/UPDATE/DELETE/NOOP) + post-retrieval memory distillation, reward design, and what�s required to safely adopt this in shisad |
   132|| [ANALYSIS-arxiv-2508.03341-nemori](ANALYSIS-arxiv-2508.03341-nemori.md) | `references/nan-nemori.md` + `references/papers/arxiv-2508.03341.pdf` | System deep dive emphasizing episode segmentation (Two-Step Alignment) + predict-calibrate semantic distillation, reported LoCoMo/LongMemEvalS gains, and implications for shisad write gating + correction semantics |
   133|| [ANALYSIS-arxiv-2510.08601-mnemosyne](ANALYSIS-arxiv-2510.08601-mnemosyne.md) | `references/jonelagadda-mnemosyne.md` + `references/papers/arxiv-2510.08601.pdf` | System deep dive emphasizing edge-first graph memory, redundancy/refresh, probabilistic decay-based recall, and a fixed-budget core/persona summary; includes evaluation-rigor cautions |
   134|| [ANALYSIS-arxiv-2511.12960-engram](ANALYSIS-arxiv-2511.12960-engram.md) | `references/patel-engram.md` + `references/papers/arxiv-2511.12960.pdf` | System deep dive emphasizing typed memory (episodic/semantic/procedural), deterministic routing/formatting, strict evidence budgets, and strong token/latency results; mapping to shisad primitives |
   135|| [ANALYSIS-arxiv-2511.20857-evo-memory](ANALYSIS-arxiv-2511.20857-evo-memory.md) | `references/wei-evo-memory.md` + `references/papers/arxiv-2511.20857.pdf` | Benchmark deep dive emphasizing streaming task-sequence evaluation for experience reuse, plus refine/prune mechanisms and metrics (robustness, step efficiency) for shisad�s eval harness |
   136|| [ANALYSIS-arxiv-2512.10696-remember-me-refine-me](ANALYSIS-arxiv-2512.10696-remember-me-refine-me.md) | `references/cao-remember-me-refine-me.md` + `references/papers/arxiv-2512.10696.pdf` | System deep dive emphasizing procedural memory distillation + scenario-aware reuse + utility-based refinement/pruning; mapping to shisad procedural tier + versioned invalidation vs delete |
   137|| [ANALYSIS-arxiv-2512.12686-memoria](ANALYSIS-arxiv-2512.12686-memoria.md) | `references/sarin-memoria.md` + `references/papers/arxiv-2512.12686.pdf` | System deep dive emphasizing persona KG + session summaries with recency-weighted retrieval; highlights missing governance/versioning primitives needed for shisad |
   138|| [ANALYSIS-arxiv-2512.12818-hindsight](ANALYSIS-arxiv-2512.12818-hindsight.md) | `references/latimer-hindsight.md` + `references/papers/arxiv-2512.12818.pdf` | System deep dive emphasizing retain/recall/reflect with four-network memory (facts/experiences/observations/beliefs), token-budgeted multi-channel retrieval fusion, and belief confidence updates; key shisad mapping |
   139|| [ANALYSIS-arxiv-2601.01885-agentic-memory](ANALYSIS-arxiv-2601.01885-agentic-memory.md) | `references/yu-agentic-memory.md` + `references/papers/arxiv-2601.01885.pdf` | RL deep dive emphasizing unified LTM+STM memory ops as tool actions, 3-stage training curriculum, step-wise GRPO credit assignment, and implications for shisad�s future learned memory policies |
   140|| [ANALYSIS-arxiv-2601.02163-evermemos](ANALYSIS-arxiv-2601.02163-evermemos.md) | `references/hu-evermemos.md` + `references/papers/arxiv-2601.02163.pdf` | System deep dive emphasizing MemCell?MemScene consolidation lifecycle, user profile/foresight, and sufficiency-verified scene-guided retrieval; mapping to shisad consolidation roadmap |
   141|| [ANALYSIS-arxiv-2601.02845-timem](ANALYSIS-arxiv-2601.02845-timem.md) | `references/li-timem.md` + `references/papers/arxiv-2601.02845.pdf` | System deep dive emphasizing temporal-hierarchical consolidation (TMT), query-complexity recall planning/gating, and the accuracy�token frontier; mapping to shisad temporal tiers |
   142|| [ANALYSIS-arxiv-2601.06377-himem](ANALYSIS-arxiv-2601.06377-himem.md) | `references/zhang-himem.md` + `references/papers/arxiv-2601.06377.pdf` | System deep dive emphasizing Episode Memory + Note Memory hierarchy, note-first �best-effort� retrieval w/ sufficiency checks, and conflict-aware reconsolidation; mapping to shisad event?knowledge tiers + versioned updates |
   143|| [ANALYSIS-arxiv-2512.24695-nested-learning](ANALYSIS-arxiv-2512.24695-nested-learning.md) | `references/behrouz-nested-learning.md` + `references/papers/arxiv-2512.24695.pdf` | Conceptual deep dive on multi-timescale �continuum memory� and consolidation dynamics; mapping to shisad tiered memory + versioned corrections |
   144|| [ANALYSIS-arxiv-2512.24601-recursive-language-models](ANALYSIS-arxiv-2512.24601-recursive-language-models.md) | `references/zhang-recursive-language-models.md` + `references/papers/arxiv-2512.24601.pdf` | Architecture deep dive emphasizing RLM-style programmatic reading/compilation over arbitrarily long evidence stores (REPL + recursion + sub-calls), with implications for shisad sandboxed compilation traces and cost tail management |
   145|| [ANALYSIS-arxiv-2502.00592-m-plus](ANALYSIS-arxiv-2502.00592-m-plus.md) | `references/wang-m-plus.md` + `references/papers/arxiv-2502.00592.pdf` | Architecture deep dive emphasizing latent-space long-term memory tokens + co-trained retrieval for >160k retention, with mapping to shisad�s external evidence-first memory and retrieval diagnostics |
   146|| [ANALYSIS-arxiv-2503.03704-minja](ANALYSIS-arxiv-2503.03704-minja.md) | `references/dong-minja.md` + `references/papers/arxiv-2503.03704.pdf` | Security deep dive on query-only memory injection attacks; implications for write-policy, provenance/taint, isolation, and �don�t store demonstrations� patterns |
   147|| [ANALYSIS-arxiv-2601.05504-memory-poisoning-attack-defense](ANALYSIS-arxiv-2601.05504-memory-poisoning-attack-defense.md) | `references/sunil-memory-poisoning-attack-defense.md` + `references/papers/arxiv-2601.05504.pdf` | Security deep dive emphasizing ISR vs ASR under realistic memory conditions, and why trust-score sanitization can fail; concrete shisad hardening takeaways |
   148|| [ANALYSIS-arxiv-2407.04363-arigraph](ANALYSIS-arxiv-2407.04363-arigraph.md) | `references/anokhin-arigraph.md` + `references/papers/arxiv-2407.04363.pdf` | System deep dive emphasizing episodic?semantic memory linking, graph-structured retrieval for planning/exploration, and implications for shisad episode objects + provenance + correction semantics |
   149|| [ANALYSIS-arxiv-2501.00663-titans](ANALYSIS-arxiv-2501.00663-titans.md) | `references/behrouz-titans.md` + `references/papers/arxiv-2501.00663.pdf` | Architecture deep dive emphasizing test-time-learning neural memory (surprise/momentum/forgetting), Titans MAC/MAG/MAL variants, and how to translate salience/decay ideas into shisad�s external memory framework |
   150|| [ANALYSIS-arxiv-2504.16754-hema](ANALYSIS-arxiv-2504.16754-hema.md) | `references/ahn-hema.md` + `references/papers/arxiv-2504.16754.pdf` | System deep dive emphasizing dual memory (summary + vector store), explicit prompt budgeting, pruning/consolidation policies, and evaluation-rigor cautions for shisad adoption |
   151|| [ANALYSIS-arxiv-2506.21605-membench](ANALYSIS-arxiv-2506.21605-membench.md) | `references/tan-membench.md` + `references/papers/arxiv-2506.21605.pdf` | Benchmark deep dive emphasizing multi-scenario (participant vs observer) and multi-level (factual vs reflective) evaluation, plus latency/capacity metrics and implications for shisad eval harnesses |
   152|
   153|## Source Threads & Links
   154|
   155|| Source | URL |
   156||--------|-----|
   157|| @jumperz memory stack thread | https://x.com/jumperz/status/2024841165774717031 |
   158|| @joelhooks ADR tweet | https://x.com/joelhooks/status/2024947701738262773 |
   159|| joelclaw ADR-0077 | https://joelclaw.com/adrs/0077-memory-system-next-phase |
   160|| @drag88 article | https://x.com/drag88/status/2022551759491862974 |
   161|| supermemory docs | https://supermemory.ai/docs |
   162|| supermemory repo | https://github.com/supermemoryai/supermemory |
   163|| mempalace repo | https://github.com/milla-jovovich/mempalace |
   164|| karta repo | https://github.com/rohithzr/karta |
   165|
   166|## File Tree
   167|
   168|```
   169|agentic-memory/
   170|??? README.md                          ? this file
   171|??? ANALYSIS.md                         ? synthesis + comparison
   172|??? ANALYSIS-academic-industry.md       ? academic/industry synthesis
   173|??? ANALYSIS-jumperz-agent-memory-stack.md
   174|??? ANALYSIS-joelhooks-adr-0077-memory-system-next-phase.md
   175|??? ANALYSIS-coolmanns-openclaw-memory-architecture.md
   176|??? ANALYSIS-drag88-agent-output-degradation.md
   177|??? ANALYSIS-versatly-clawvault.md
   178|??? ANALYSIS-vstorm-memv.md
   179|??? ANALYSIS-mira-OSS.md
   180|??? ANALYSIS-codex-memory.md
   181|??? ANALYSIS-google-always-on-memory-agent.md
   182|??? ANALYSIS-supermemory.md
   183|??? ANALYSIS-karta.md               ? Karta: Rust agentic memory library with dream engine
   184|??? ANALYSIS-mempalace.md           ? not in ANALYSIS.md (claims-vs-code issues); see REVIEWED.md
   185|??? REVIEWED.md                        ? triage log (examined but not promoted to ANALYSIS)
   186|??? PUNCHLIST-academic-industry.md     ? tracking checklist for paper deep dives
   187|??? templates/                         ? templates for paper analyses/summaries
   188|?
   189|??? references/                        ? summarized reference docs (markdown w/ frontmatter)
   190|?   ??? 1-full-agent-memory-build.jpg  ? jumperz card 1: memory storage
   191|?   ??? 2-feeds-into.jpg               ? jumperz card 2: memory intelligence
   192|?   ??? jumperz-agent-memory-stack.md
   193|?   ??? joelhooks-adr-0077-memory-system-next-phase.md
   194|?   ??? coolmanns-openclaw-memory-architecture.md
   195|?   ??? drag88-agent-output-degradation.md
   196|?   ??? versatly-clawvault.md
   197|?   ??? hu-evermembench.md
   198|?   ??? li-locomoplus.md
   199|?   ??? maharana-locomo.md
   200|?   ??? wu-longmemeval.md
   201|?   ??? chhikara-mem0.md
   202|?   ??? papers/                        ? archived PDFs + text snapshots
   203|?       ??? README.md
   204|?       ??? arxiv-*.pdf
   205|?       ??? arxiv-*.md
   206|?
   207|??? vendor/                            ? cloned source repos
   208|    ??? mira-OSS/                      ? github.com/taylorsatula/mira-OSS (snapshot, AGPLv3)
   209|    ?   ??? README.md
   210|    ?   ??? CLAUDE.md                  ? project guide (architecture, patterns, principles)
   211|    ?   ??? main.py                    ? FastAPI entry point
   212|    ?   ??? cns/                       ? Central Nervous System (conversation orchestration)
   213|    ?   ?   ??? api/                   ? FastAPI endpoints (chat, actions, data, health)
   214|    ?   ?   ??? core/                  ? Domain models (Continuum, Message, Events)
   215|    ?   ?   ??? services/              ? Orchestrator, subcortical, summary, collapse handler
   216|    ?   ?   ??? infrastructure/        ? Repositories, Valkey cache, unit of work
   217|    ?   ??? lt_memory/                 ? Long-term memory system
   218|    ?   ?   ??? scoring_formula.sql    ? Multi-factor activity-day sigmoid importance scoring
   219|    ?   ?   ??? models.py             ? Memory, Entity, ExtractedMemory, link types
   220|    ?   ?   ??? hybrid_search.py      ? BM25 + pgvector with RRF
   221|    ?   ?   ??? proactive.py          ? Dual-path retrieval (similarity + hub discovery)
   222|    ?   ?   ??? hub_discovery.py      ? Entity-driven memory retrieval via pg_trgm
   223|    ?   ?   ??? processing/           ? Extraction, consolidation, entity GC pipelines
   224|    ?   ??? working_memory/           ? System prompt composition via trinkets
   225|    ?   ??? tools/                    ? Self-registering tool framework (11 built-in)
   226|    ?   ??? config/                   ? Pydantic config + prompt templates
   227|    ?   ??? auth/                     ? WebAuthn + magic link authentication
   228|    ?
   229|    ??? openclaw-memory-architecture/  ? github.com/coolmanns/openclaw-memory-architecture
   230|    ?   ??? README.md
   231|    ?   ??? PROJECT.md
   232|    ?   ??? CHANGELOG.md
   233|    ?   ??? docs/
   234|    ?   ?   ??? ARCHITECTURE.md        ? full 12-layer technical reference
   235|    ?   ?   ??? knowledge-graph.md     ? graph search pipeline, benchmarks
   236|    ?   ?   ??? context-optimization.md
   237|    ?   ?   ??? embedding-setup.md
   238|    ?   ?   ??? benchmark-process.md
   239|    ?   ?   ??? benchmark-results.md
   240|    ?   ?   ??? code-search.md
   241|    ?   ?   ??? COMPARISON.md
   242|    ?   ??? schema/
   243|    ?   ?   ??? facts.sql              ? SQLite schema for knowledge graph
   244|    ?   ??? scripts/                   ? init, seed, search, ingest, decay, benchmark, telemetry
   245|    ?   ??? templates/                 ? starter files (active-context, gating-policies, etc.)
   246|    ?   ??? plugin-graph-memory/       ? OpenClaw plugin (JS)
   247|    ?
   248|    ??? karta/                         ? github.com/rohithzr/karta (submodule, MIT)
   249|    ?   ??? Cargo.toml                ? workspace: karta-core + karta-cli
   250|    ?   ??? crates/
   251|    ?   ?   ??? karta-core/           ? Core engine (~6.7K LOC Rust)
   252|    ?   ?       ??? src/
   253|    ?   ?       ?   ??? note.rs       ? MemoryNote, Provenance, NoteStatus, AtomicFact, Episode, EpisodeDigest
   254|    ?   ?       ?   ??? write.rs      ? Write path: index, link, evolve, foresight, facts
   255|    ?   ?       ?   ??? read.rs       ? Read path: classify, search, traverse, rerank, synthesize
   256|    ?   ?       ?   ??? rerank.rs     ? Jina/LLM/noop rerankers
   257|    ?   ?       ?   ??? dream/        ? Dream engine: 7 inference types
   258|    ?   ?       ?   ??? store/        ? LanceDB + SQLite implementations
   259|    ?   ?       ?   ??? llm/          ? Provider trait + OpenAI + mock + prompts
   260|    ?   ?       ??? tests/            ? eval, beam_100k, bench_beam (~3.8K LOC)
   261|    ?   ??? findings.md               ? BEAM 100K detailed failure analysis
   262|    ?   ??? plan.md                   ? Experiment plan targeting 90%+
   263|    ?
   264|    ??? always-on-memory-agent/        ? GoogleCloudPlatform/generative-ai (official ADK sample)
   265|    ?   ??? agent.py                  ? ADK multi-agent daemon (ingest/consolidate/query)
   266|    ?   ??? dashboard.py              ? Streamlit UI
   267|    ?   ??? docs/                     ? Logo/architecture assets
   268|    ?
   269|    ??? memv/                          ? github.com/vstorm-co/memv
   270|    ?   ??? README.md
   271|    ?   ??? CHANGELOG.md
   272|    ?   ??? pyproject.toml             ? PyPI: memvee, v0.1.0
   273|    ?   ??? docs/                      ? docs site (MkDocs)
   274|    ?   ??? src/
   275|    ?   ?   ??? memv/                  ? segmentation, extraction, validity, retrieval, storage
   276|    ?   ??? tests/
   277|    ?
   278|    ??? supermemory/                    ? github.com/supermemoryai/supermemory (lean subset: schemas, SDK, MCP, arch docs)
   279|    ?   ??? LICENSE
   280|    ?   ??? README.md                  ? provenance + open-source vs hosted-backend split
   281|    ?   ??? packages/
   282|    ?   ?   ??? validation/            ? Zod schemas (data model definitions)
   283|    ?   ?   ?   ??? schemas.ts
   284|    ?   ?   ?   ??? api.ts
   285|    ?   ?   ??? lib/
   286|    ?   ?   ?   ??? api.ts             ? reveals backend dependency (api.supermemory.ai)
   287|    ?   ?   ?   ??? similarity.ts      ? client-side cosine sim (visualization only)
   288|    ?   ?   ??? tools/src/shared/
   289|    ?   ?       ??? memory-client.ts   ? SDK client (profile search, prompt formatting)
   290|    ?   ??? apps/mcp/src/
   291|    ?   ?   ??? server.ts              ? MCP server (memory/recall/whoAmI tools)
   292|    ?   ??? skills/supermemory/references/
   293|    ?       ??? architecture.md        ? claimed design (558 lines)
   294|    ?
   295|    ??? clawvault/                     ? github.com/Versatly/clawvault
   296|        ??? README.md
   297|        ??? PLAN.md                    ? issue #4: ledger, reflect, replay, archive
   298|        ??? CHANGELOG.md
   299|        ??? SKILL.md
   300|        ??? package.json               ? npm: clawvault, v2.6.1
   301|        ??? src/
   302|        ?   ??? commands/              ? archive, context, inject, observe, reflect, replay, wake, sleep, task, project, ...
   303|        ?   ??? observer/              ? compressor, reflector, router, session-watcher
   304|        ?   ??? lib/                   ? vault, memory-graph, ledger, observation-format, session-utils
   305|        ?   ??? cli/
   306|        ??? bin/                       ? CLI entry + command registration modules
   307|        ??? hooks/                     ? OpenClaw hook handler
   308|        ??? dashboard/                 ? web dashboard (vault parser, graph diff)
   309|        ??? schemas/
   310|        ??? scripts/
   311|        ??? templates/
   312|        ??? tests/
   313|```
   314|
   315|## Key Themes Across Sources
   316|
   317|- **Phased build order matters**: Core memory first (write/read/decay), reliability second (dedup/maintenance/recovery), intelligence last (graphs/trust/cross-agent). Building out of order amplifies flaws.
   318|- **Tiered retrieval**: Summary files first (fast, cheap), vector search fallback (thorough, expensive). Don't vector-search everything.
   319|- **Score decay**: `final_score = relevance � exp(-? � days)` � recency-weighted relevance is universal across all architectures.
   320|- **Feedback loops**: Echo/fizzle (track which injected memories get used), behavior loops (extract corrections as lessons), learning loops (convert expensive LLM checks into cheap static rules).
   321|- **SQLite over hosted vector DBs**: At current scales (1K-5K entries), SQLite + FTS5 + local embeddings outperforms hosted solutions on latency, cost, and operational simplicity.
   322|- **Multi-agent convergence**: Shared memory creates homogenization pressure. Workspace isolation + file routing guards help but don't fully solve it.
   323|- **Vault index pattern**: Single scannable manifest (one-line descriptions) ? load individual entries on demand. One file read instead of N.
   324|
   325|