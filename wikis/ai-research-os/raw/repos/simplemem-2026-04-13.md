---
status: processed
---
     1|---
     2|source: https://github.com/aiming-lab/SimpleMem
     3|date: 2026-04-13
     4|type: repo
     5|tags: [agent-memory, lifelong-memory, semantic-compression, multimodal, llm-agents]
     6|status: raw
     7|---
     8|
     9|<div align="center">
    10|
    11|<img alt="simplemem_logo" src="https://github.com/user-attachments/assets/6ea54ad1-e007-442c-99d7-1174b10d1fec" width="450">
    12|
    13|<div align="center">
    14|
    15|## Efficient Lifelong Memory for LLM Agents � Text & Multimodal
    16|
    17|<small>Store, compress, and retrieve long-term memories with semantic lossless compression. Now with multimodal support for text, image, audio & video. Works across Claude, Cursor, LM Studio, and more.</small>
    18|
    19|</div>
    20|
    21|<p><b>Works with any AI platform that supports MCP or Python integration</b></p>
    22|
    23|<table>
    24|<tr>
    25|
    26|<td align="center" width="100">
    27|  <a href="https://www.anthropic.com/claude">
    28|    <img src="https://cdn.simpleicons.org/claude/D97757" width="48" height="48" alt="Claude Desktop" />
    29|  </a><br/>
    30|  <sub>
    31|    <a href="https://www.anthropic.com/claude"><b>Claude Desktop</b></a>
    32|  </sub>
    33|</td>
    34|
    35|<td align="center" width="100">
    36|  <a href="https://cursor.com">
    37|    <picture>
    38|      <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/cursor/FFFFFF">
    39|      <img src="https://cdn.simpleicons.org/cursor/000000" width="48" height="48" alt="Cursor" />
    40|    </picture>
    41|  </a><br/>
    42|  <sub>
    43|    <a href="https://cursor.com"><b>Cursor</b></a>
    44|  </sub>
    45|</td>
    46|
    47|<td align="center" width="100">
    48|  <a href="https://lmstudio.ai">
    49|    <img src="https://github.com/lmstudio-ai.png?size=200" width="48" height="48" alt="LM Studio" />
    50|  </a><br/>
    51|  <sub>
    52|    <a href="https://lmstudio.ai"><b>LM Studio</b></a>
    53|  </sub>
    54|</td>
    55|
    56|<td align="center" width="100">
    57|  <a href="https://cherry-ai.com">
    58|    <img src="https://github.com/CherryHQ.png?size=200" width="48" height="48" alt="Cherry Studio" />
    59|  </a><br/>
    60|  <sub>
    61|    <a href="https://cherry-ai.com"><b>Cherry Studio</b></a>
    62|  </sub>
    63|</td>
    64|
    65|<td align="center" width="100">
    66|  <a href="https://pypi.org/project/simplemem/">
    67|    <img src="https://cdn.simpleicons.org/pypi/3775A9" width="48" height="48" alt="PyPI" />
    68|  </a><br/>
    69|  <sub>
    70|    <a href="https://pypi.org/project/simplemem/"><b>PyPI Package</b></a>
    71|  </sub>
    72|</td>
    73|
    74|<td align="center" width="100">
    75|  <sub><b>+ Any MCP<br/>Client</b></sub>
    76|</td>
    77|
    78|</tr>
    79|</table>
    80|
    81|<div align="center">
    82|
    83|<br/>
    84|
    85|[?? ??](./docs/i18n/README.zh-CN.md) �
    86|[?? ???](./docs/i18n/README.ja.md) �
    87|[?? ???](./docs/i18n/README.ko.md) �
    88|[?? Espa�ol](./docs/i18n/README.es.md) �
    89|[?? Fran�ais](./docs/i18n/README.fr.md) �
    90|[?? Deutsch](./docs/i18n/README.de.md) �
    91|[?? Portugu�s](./docs/i18n/README.pt-br.md)<br/>
    92|[?? ???????](./docs/i18n/README.ru.md) �
    93|[?? ???????](./docs/i18n/README.ar.md) �
    94|[?? Italiano](./docs/i18n/README.it.md) �
    95|[?? Ti?ng Vi?t](./docs/i18n/README.vi.md) �
    96|[?? T�rk�e](./docs/i18n/README.tr.md)
    97|
    98|<br/>
    99|
   100|[![Project Page](https://img.shields.io/badge/?_INTERACTIVE_DEMO-Visit_Our_Website-FF6B6B?style=for-the-badge&labelColor=FF6B6B&color=4ECDC4&logoColor=white)](https://aiming-lab.github.io/SimpleMem-Page)
   101|
   102|<p align="center">
   103|  <a href="https://arxiv.org/abs/2601.02553"><img src="https://img.shields.io/badge/arXiv-2601.02553-b31b1b?style=flat&labelColor=555" alt="arXiv"></a>
   104|  <a href="https://github.com/aiming-lab/SimpleMem"><img src="https://img.shields.io/badge/github-SimpleMem-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
   105|  <a href="LICENSE"><img src="https://img.shields.io/github/license/aiming-lab/SimpleMem?style=flat&label=license&labelColor=555&color=2EA44F" alt="License"></a>
   106|  <a href="https://github.com/aiming-lab/SimpleMem/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat&labelColor=555" alt="PRs Welcome"></a>
   107|  <br/>
   108|  <a href="https://pypi.org/project/simplemem/"><img src="https://img.shields.io/pypi/v/simplemem?style=flat&label=pypi&labelColor=555&color=3775A9&logo=pypi&logoColor=white" alt="PyPI"></a>
   109|  <a href="https://pypi.org/project/simplemem/"><img src="https://img.shields.io/pypi/pyversions/simplemem?style=flat&label=python&labelColor=555&color=3775A9&logo=python&logoColor=white" alt="Python"></a>
   110|  <a href="https://mcp.simplemem.cloud"><img src="https://img.shields.io/badge/MCP-mcp.simplemem.cloud-14B8A6?style=flat&labelColor=555" alt="MCP Server"></a>
   111|  <a href="https://github.com/aiming-lab/SimpleMem"><img src="https://img.shields.io/badge/Claude_Skills-supported-FFB000?style=flat&labelColor=555" alt="Claude Skills"></a>
   112|  <br/>
   113|  <a href="https://discord.gg/KA2zC32M"><img src="https://img.shields.io/badge/Discord-Join_Chat-5865F2?style=flat&labelColor=555&logo=discord&logoColor=white" alt="Discord"></a>
   114|  <a href="fig/wechat_logo3.JPG"><img src="https://img.shields.io/badge/WeChat-Group-07C160?style=flat&labelColor=555&logo=wechat&logoColor=white" alt="WeChat"></a>
   115|</p>
   116|
   117|<br/>
   118|
   119|[? Quick Start](#-quick-start) � [? Overview](#-overview) � [? Results](#-results) � [? Omni-SimpleMem](#-omni-simplemem-multimodal-memory) � [? Installation](#-installation) � [? Cross-Session Memory](#-cross-session-memory-text-memory) � [? MCP Server](#-mcp-server-text-memory) � [? Citation](#-citation)
   120|
   121|</div>
   122|
   123|</div>
   124|
   125|<br/>
   126|
   127|## ? News
   128|
   129|- **[04/02/2026]** ? **Omni-SimpleMem � Multimodal Memory is Here!** SimpleMem now supports **text, image, audio & video** memory. Achieving **new SOTA on LoCoMo (F1=0.613, +47%)** and **Mem-Gallery (F1=0.810, +51%)** over previous best, Omni-SimpleMem brings state-of-the-art multimodal lifelong memory to your agents. [View Omni-SimpleMem ?](OmniSimpleMem/)
   130|- **[02/09/2026]** ? **Cross-Session Memory is Here � Outperforming Claude-Mem by 64%!** SimpleMem now supports **persistent memory across conversations**. On the LoCoMo benchmark, SimpleMem achieves a **64% performance boost** over Claude-Mem. Your agents can now recall context, decisions, and learnings from previous sessions automatically. [View Cross-Session Documentation ?](cross/README.md)
   131|- **[01/20/2026]** **SimpleMem is now available on PyPI!** ? Install directly via `pip install simplemem`. [View Package Usage Guide ?](docs/PACKAGE_USAGE.md)
   132|- **[01/19/2026]** **Added Local Memory Storage for SimpleMem Skill!** ? SimpleMem Skill now supports local memory storage within Claude Skills.
   133|- **[01/18/2026]** **SimpleMem now supports Claude Skills!** ? Use SimpleMem in claude.ai for long-term memory across conversations. Register at [mcp.simplemem.cloud](https://mcp.simplemem.cloud), configure your token, and import the skill!
   134|- **[01/14/2026]** **SimpleMem MCP Server is now LIVE and Open Source!** ? Cloud-hosted memory service at [mcp.simplemem.cloud](https://mcp.simplemem.cloud). Integrates with LM Studio, Cherry Studio, Cursor, Claude Desktop via **Streamable HTTP** MCP protocol. [View MCP Documentation ?](MCP/README.md)
   135|- **[01/08/2026]** ? Join our [Discord](https://discord.gg/KA2zC32M) and [WeChat Group](fig/wechat_logo3.JPG) to collaborate and exchange ideas!
   136|- **[01/05/2026]** SimpleMem paper was released on [arXiv](https://arxiv.org/abs/2601.02553)!
   137|
   138|---
   139|
   140|## ? Table of Contents
   141|
   142|- [? Quick Start](#-quick-start)
   143|- [? Overview](#-overview)
   144|- [? Results](#-results)
   145|- [? SimpleMem: Text Memory](#-simplemem-text-memory)
   146|- [? Omni-SimpleMem: Multimodal Memory](#-omni-simplemem-multimodal-memory)
   147|- [? Installation](#-installation)
   148|- [? Docker](#-run-with-docker)
   149|- [? Router Utilities](#-router-utilities)
   150|- [? Cross-Session Memory](#-cross-session-memory-text-memory)
   151|- [? MCP Server](#-mcp-server-text-memory)
   152|- [?? Roadmap](#?-roadmap)
   153|- [? Evaluation](#-evaluation)
   154|- [? Citation](#-citation)
   155|
   156|---
   157|
   158|## ? Quick Start
   159|
   160|### ? Understanding the Basic Workflow
   161|
   162|At a high level, SimpleMem works as a long-term memory system for LLM-based agents. The workflow consists of three simple steps:
   163|
   164|1. **Store information** � Dialogues or facts are processed and converted into structured, atomic memories.
   165|2. **Index memory** � Stored memories are organized using semantic embeddings and structured metadata.
   166|3. **Retrieve relevant memory** � When a query is made, SimpleMem retrieves the most relevant stored information based on meaning rather than keywords.
   167|
   168|This design allows LLM agents to maintain context, recall past information efficiently, and avoid repeatedly processing redundant history.
   169|
   170|### ? Basic Usage
   171|
   172|SimpleMem provides a **unified entry point** via `simplemem_router`. The default `mode="auto"` **automatically detects** which backend to use based on what you call � no manual configuration needed:
   173|
   174|```python
   175|import simplemem_router as simplemem
   176|
   177|mem = simplemem.create()  # mode="auto" � backend chosen by first call
   178|```
   179|
   180|The first method you call determines the backend:
   181|
   182|| First call | Backend selected | Why |
   183||:--|:--|:--|
   184|| `add_dialogue()` | **Text** (SimpleMem) | Dialogue-based API ? text mode |
   185|| `add_text()` / `add_image()` / `add_audio()` / `add_video()` | **Omni** (Omni-SimpleMem) | Multimodal API ? omni mode |
   186|
   187|<table>
   188|<tr>
   189|<td width="50%">
   190|
   191|**? Auto ? Text** (pure text input)
   192|
   193|```python
   194|import simplemem_router as simplemem
   195|
   196|mem = simplemem.create()  # auto mode
   197|
   198|# add_dialogue() ? text backend auto-selected
   199|mem.add_dialogue(
   200|    "Alice",
   201|    "Bob, let's meet at Starbucks tomorrow at 2pm",
   202|    "2025-11-15T14:30:00",
   203|)
   204|mem.add_dialogue(
   205|    "Bob",
   206|    "Sure, I'll bring the market analysis report",
   207|    "2025-11-15T14:31:00",
   208|)
   209|mem.finalize()
   210|
   211|answer = mem.ask("When and where will Alice and Bob meet?")
   212|# ? "16 November 2025 at 2:00 PM at Starbucks"
   213|```
   214|
   215|</td>
   216|<td width="50%">
   217|
   218|**? Auto ? Omni** (multimodal input)
   219|
   220|```python
   221|import simplemem_router as simplemem
   222|
   223|mem = simplemem.create()  # auto mode
   224|
   225|# add_image() ? omni backend auto-selected
   226|mem.add_text(
   227|    "User loves hiking in the Rocky Mountains.",
   228|    tags=["session_id:D1"],
   229|)
   230|mem.add_image("photo.jpg", tags=["session_id:D1"])
   231|mem.add_audio("voice_note.wav", tags=["session_id:D1"])
   232|
   233|result = mem.query("What does the user enjoy?", top_k=5)
   234|for item in result.items:
   235|    print(item["summary"])
   236|
   237|mem.close()
   238|```
   239|
   240|</td>
   241|</tr>
   242|</table>
   243|
   244|> **? Tip**: Auto mode picks the lightest backend that fits your data. You can still use `mode="text"` or `mode="omni"` explicitly if you prefer.
   245|
   246|---
   247|
   248|### ? Advanced: Parallel Processing
   249|
   250|For large-scale dialogue processing, enable parallel mode:
   251|
   252|```python
   253|import simplemem_router as simplemem
   254|
   255|mem = simplemem.create(
   256|    mode="text",
   257|    clear_db=True,
   258|    enable_parallel_processing=True,  # ? Parallel memory building
   259|    max_parallel_workers=8,
   260|    enable_parallel_retrieval=True,   # ? Parallel query execution
   261|    max_retrieval_workers=4
   262|)
   263|```
   264|
   265|> **? Pro Tip**: Parallel processing significantly reduces latency for batch operations!
   266|
   267|---
   268|
   269|## ? Overview
   270|
   271|**SimpleMem** is a family of efficient memory frameworks � **SimpleMem** for text and **Omni-SimpleMem** for multimodal (text, image, audio, video) � based on **semantic lossless compression** that addresses the fundamental challenge of **efficient long-term memory for LLM agents**. Unlike existing systems that either passively accumulate redundant context or rely on expensive iterative reasoning loops, SimpleMem maximizes **information density** and **token utilization** through a three-stage pipeline:
   272|
   273|<table>
   274|<tr>
   275|<td width="33%" align="center">
   276|
   277|### ? Stage 1
   278|**Semantic Structured Compression**
   279|
   280|Distills unstructured interactions into compact, multi-view indexed memory units
   281|
   282|</td>
   283|<td width="33%" align="center">
   284|
   285|### ?? Stage 2
   286|**Online Semantic Synthesis**
   287|
   288|Intra-session process that instantly integrates related context into unified abstract representations to eliminate redundancy
   289|
   290|</td>
   291|<td width="33%" align="center">
   292|
   293|### ? Stage 3
   294|**Intent-Aware Retrieval Planning**
   295|
   296|Infers search intent to dynamically determine retrieval scope and construct precise context efficiently
   297|
   298|</td>
   299|</tr>
   300|</table>
   301|
   302|> For multimodal memory, see [Omni-SimpleMem](#-omni-simplemem-multimodal-memory) below.
   303|
   304|<div align="center">
   305|<img src="fig/Fig_framework.png" alt="SimpleMem Framework" width="900"/>
   306|
   307|*The SimpleMem Architecture: (1) Semantic Structured Compression filters low-utility dialogue and converts informative windows into compact, context-independent memory units. (2) Online Semantic Synthesis consolidates related fragments during writing, maintaining a compact and coherent memory topology. (3) Intent-Aware Retrieval Planning infers search intent to adapt retrieval scope and query forms, enabling parallel multi-view retrieval and token-efficient context construction.*
   308|</div>
   309|
   310|---
   311|
   312|### ? Performance Comparison
   313|
   314|<div align="center">
   315|
   316|<img src="fig/Fig_tradeoff.png" alt="Performance vs Efficiency Trade-off" width="900"/>
   317|
   318|*SimpleMem achieves superior F1 score (43.24%) with minimal token cost (~550), occupying the ideal top-left position.*
   319|
   320|**Speed Comparison Demo**
   321|
   322|<video src="https://github.com/aiming-lab/SimpleMem/raw/main/fig/simplemem-new.mp4" controls width="900"></video>
   323|
   324|*SimpleMem vs. Baseline: Real-time speed comparison demonstration*
   325|
   326|</div>
   327|
   328|<div align="center">
   329|
   330|**LoCoMo-10 Benchmark Results (GPT-4.1-mini)**
   331|
   332|| Model | ?? Construction Time | ? Retrieval Time | ? Total Time | ? Average F1 |
   333||:------|:--------------------:|:-----------------:|:-------------:|:-------------:|
   334|| A-Mem | 5140.5s | 796.7s | 5937.2s | 32.58% |
   335|| LightMem | 97.8s | 577.1s | 675.9s | 24.63% |
   336|| Mem0 | 1350.9s | 583.4s | 1934.3s | 34.20% |
   337|| **SimpleMem** ? | **92.6s** | **388.3s** | **480.9s** | **43.24%** |
   338|
   339|</div>
   340|
   341|---
   342|
   343|## ? Results
   344|
   345|### ? Benchmark Results (LoCoMo)
   346|
   347|<details open>
   348|<summary><b>? Cross-Session Memory Comparison</b></summary>
   349|
   350|| System | LoCoMo Score | vs SimpleMem |
   351||:-------|:------------:|:------------:|
   352|| **SimpleMem** | **48** | � |
   353|| Claude-Mem | 29.3 | **+64%** |
   354|
   355|</details>
   356|
   357|<details>
   358|<summary><b>? High-Capability Models (GPT-4.1-mini)</b></summary>
   359|
   360|| Task Type | SimpleMem F1 | Mem0 F1 | Improvement |
   361||:----------|:------------:|:-------:|:-----------:|
   362|| **MultiHop** | 43.46% | 30.14% | **+43.8%** |
   363|| **Temporal** | 58.62% | 48.91% | **+19.9%** |
   364|| **SingleHop** | 51.12% | 41.3% | **+23.8%** |
   365|
   366|</details>
   367|
   368|<details>
   369|<summary><b>?? Efficient Models (Qwen2.5-1.5B)</b></summary>
   370|
   371|| Metric | SimpleMem | Mem0 | Notes |
   372||:-------|:---------:|:----:|:------|
   373|| **Average F1** | 25.23% | 23.77% | Competitive with 99� smaller model |
   374|
   375|</details>
   376|
   377|### ? Omni-SimpleMem Results
   378|
   379|<table>
   380|<tr>
   381|<td align="center" width="170">? <b>0.613 F1</b><br><sub>LoCoMo (+47% over prev. SOTA)</sub></td>
   382|<td align="center" width="170">? <b>0.810 F1</b><br><sub>Mem-Gallery (+51% over prev. SOTA)</sub></td>
   383|<td align="center" width="140">? <b>3.5x faster</b><br><sub>retrieval throughput</sub></td>
   384|<td align="center" width="140">? <b>4 modalities</b><br><sub>Text � Image � Audio � Video</sub></td>
   385|</tr>
   386|</table>
   387|
   388|---
   389|
   390|## ? SimpleMem: Text Memory
   391|
   392|### 1?? Semantic Structured Compression
   393|
   394|SimpleMem applies an **implicit semantic density gating** mechanism integrated into the LLM generation process to filter redundant interaction content. The system reformulates raw dialogue streams into **compact memory units** � self-contained facts with resolved coreferences and absolute timestamps. Each unit is indexed through three complementary representations for flexible retrieval:
   395|
   396|<div align="center">
   397|
   398|| ? Layer | ? Type | ? Purpose | ?? Implementation |
   399||---------|---------|------------|-------------------|
   400|| **Semantic** | Dense | Conceptual similarity | Vector embeddings (1024-d) |
   401|| **Lexical** | Sparse | Exact term matching | BM25-style keyword index |
   402|| **Symbolic** | Metadata | Structured filtering | Timestamps, entities, persons |
   403|
   404|</div>
   405|
   406|**? Example Transformation:**
   407|```diff
   408|- Input:  "He'll meet Bob tomorrow at 2pm"  [? relative, ambiguous]
   409|+ Output: "Alice will meet Bob at Starbucks on 2025-11-16T14:00:00"  [? absolute, atomic]
   410|```
   411|
   412|---
   413|
   414|### 2?? Online Semantic Synthesis
   415|
   416|Unlike traditional systems that rely on asynchronous background maintenance, SimpleMem performs synthesis **on-the-fly during the write phase**. Related memory units are synthesized into higher-level abstract representations within the current session scope, allowing repetitive or structurally similar experiences to be **denoised and compressed immediately**.
   417|
   418|**? Example Synthesis:**
   419|```diff
   420|- Fragment 1: "User wants coffee"
   421|- Fragment 2: "User prefers oat milk"
   422|- Fragment 3: "User likes it hot"
   423|+ Consolidated: "User prefers hot coffee with oat milk"
   424|```
   425|
   426|This proactive synthesis ensures the memory topology remains compact and free of redundant fragmentation.
   427|
   428|---
   429|
   430|### 3?? Intent-Aware Retrieval Planning
   431|
   432|Instead of fixed-depth retrieval, SimpleMem leverages the reasoning capabilities of the LLM to generate a **comprehensive retrieval plan**. Given a query, the planning module infers **latent search intent** to dynamically determine retrieval scope and depth:
   433|
   434|$$\{ q_{\text{sem}}, q_{\text{lex}}, q_{\text{sym}}, d \} \sim \mathcal{P}(q, H)$$
   435|
   436|The system then executes **parallel multi-view retrieval** across semantic, lexical, and symbolic indexes, and merges results through ID-based deduplication:
   437|
   438|<table>
   439|<tr>
   440|<td width="50%">
   441|
   442|**? Simple Queries**
   443|- Direct fact lookup via single memory unit
   444|- Minimal retrieval depth
   445|- Fast response time
   446|
   447|</td>
   448|<td width="50%">
   449|
   450|**? Complex Queries**
   451|- Aggregation across multiple events
   452|- Expanded retrieval depth
   453|- Comprehensive coverage
   454|
   455|</td>
   456|</tr>
   457|</table>
   458|
   459|**? Result**: 43.24% F1 score with **30� fewer tokens** than full-context methods.
   460|
   461|---
   462|
   463|<div align="center">
   464|
   465|# ? Omni-SimpleMem: Multimodal Memory
   466|
   467|**NEW** � SimpleMem now handles text, image, audio & video.
   468|
   469|</div>
   470|
   471|**Omni-SimpleMem** extends SimpleMem to **unified multimodal memory** � supporting text, image, audio, and video experiences with state-of-the-art accuracy across all five LLM backbones tested.
   472|
   473|Built on three principles: **Selective Ingestion** (entropy-driven filtering for each modality), **Progressive Retrieval** (hybrid FAISS + BM25 search with pyramid token-budget expansion), and **Knowledge Graph Augmentation** (multi-hop cross-modal reasoning).
   474|
   475|> ? Full documentation, benchmarks, and architecture details: [**Omni-SimpleMem ?**](OmniSimpleMem/)
   476|
   477|---
   478|
   479|## ? Installation
   480|
   481|### ? Notes for First-Time Users
   482|
   483|- Ensure you are using **Python 3.10 in your active environment**, not just installed globally.
   484|- An OpenAI-compatible API key must be configured **before running any memory construction or retrieval**, otherwise initialization may fail.
   485|- When using non-OpenAI providers (e.g., Qwen or Azure OpenAI), verify both the model name and `OPENAI_BASE_URL` in `config.py`.
   486|- For large dialogue datasets, enabling parallel processing can significantly reduce memory construction time.
   487|
   488|### ? Requirements
   489|
   490|- ? Python 3.10
   491|- ? OpenAI-compatible API (OpenAI, Qwen, Azure OpenAI, etc.)
   492|
   493|### ?? Setup
   494|
   495|```bash
   496|# ? Clone repository
   497|git clone https://github.com/aiming-lab/SimpleMem.git
   498|cd SimpleMem
   499|
   500|# ? Install dependencies
   501|