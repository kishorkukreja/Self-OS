---
status: processed
---
     1|---
     2|source: https://github.com/MemPalace/mempalace
     3|date: 2026-04-13
     4|type: repo
     5|tags: [agent-memory, long-term-memory, chromadb, verbatim-storage, mcp, longmemeval]
     6|status: raw
     7|---
     8|
     9|<div align="center">
    10|
    11|<img src="assets/mempalace_logo.png" alt="MemPalace" width="280">
    12|
    13|# MemPalace
    14|
    15|### The highest-scoring AI memory system ever benchmarked. And it's free.
    16|
    17|<br>
    18|
    19|Every conversation you have with an AI � every decision, every debugging session, every architecture debate � disappears when the session ends. Six months of work, gone. You start over every time.
    20|
    21|Other memory systems try to fix this by letting AI decide what's worth remembering. It extracts "user prefers Postgres" and throws away the conversation where you explained *why*. MemPalace takes a different approach: **store everything, then make it findable.**
    22|
    23|**The Palace** � Ancient Greek orators memorized entire speeches by placing ideas in rooms of an imaginary building. Walk through the building, find the idea. MemPalace applies the same principle to AI memory: your conversations are organized into wings (people and projects), halls (types of memory), and rooms (specific ideas). No AI decides what matters � you keep every word, and the structure gives you a navigable map instead of a flat search index.
    24|
    25|**Raw verbatim storage** � MemPalace stores your actual exchanges in ChromaDB without summarization or extraction. The 96.6% LongMemEval result comes from this raw mode. We don't burn an LLM to decide what's "worth remembering" � we keep everything and let semantic search find it.
    26|
    27|**AAAK (experimental)** � A lossy abbreviation dialect for packing repeated entities into fewer tokens at scale. Readable by any LLM that reads text � Claude, GPT, Gemini, Llama, Mistral � no decoder needed. **AAAK is a separate compression layer, not the storage default**, and on the LongMemEval benchmark it currently regresses vs raw mode (84.2% vs 96.6%). We're iterating. See the [note above](#a-note-from-milla--ben--april-7-2026) for the honest status.
    28|
    29|**Local, open, adaptable** � MemPalace runs entirely on your machine, on any data you have locally, without using any external API or services. It has been tested on conversations � but it can be adapted for different types of datastores. This is why we're open-sourcing it.
    30|
    31|<br>
    32|
    33|[![][version-shield]][release-link]
    34|[![][python-shield]][python-link]
    35|[![][license-shield]][license-link]
    36|[![][discord-shield]][discord-link]
    37|
    38|<br>
    39|
    40|[Quick Start](#quick-start) � [The Palace](#the-palace) � [AAAK Dialect](#aaak-dialect-experimental) � [Benchmarks](#benchmarks) � [MCP Tools](#mcp-server)
    41|
    42|<br>
    43|
    44|### Highest LongMemEval score ever published � free or paid.
    45|
    46|<table>
    47|<tr>
    48|<td align="center"><strong>96.6%</strong><br><sub>LongMemEval R@5<br><b>raw mode</b>, zero API calls</sub></td>
    49|<td align="center"><strong>500/500</strong><br><sub>questions tested<br>independently reproduced</sub></td>
    50|<td align="center"><strong>$0</strong><br><sub>No subscription<br>No cloud. Local only.</sub></td>
    51|</tr>
    52|</table>
    53|
    54|<sub>Reproducible � runners in <a href="benchmarks/">benchmarks/</a>. <a href="benchmarks/BENCHMARKS.md">Full results</a>. The 96.6% is from <b>raw verbatim mode</b>, not AAAK or rooms mode (those score lower � see <a href="#a-note-from-milla--ben--april-7-2026">note above</a>).</sub>
    55|
    56|</div>
    57|
    58|---
    59|
    60|## A Note from Milla & Ben � April 7, 2026
    61|
    62|> The community caught real problems in this README within hours of launch and we want to address them directly.
    63|>
    64|> **What we got wrong:**
    65|>
    66|> - **The AAAK token example was incorrect.** We used a rough heuristic (`len(text)//3`) for token counts instead of an actual tokenizer. Real counts via OpenAI's tokenizer: the English example is 66 tokens, the AAAK example is 73. AAAK does not save tokens at small scales � it's designed for *repeated entities at scale*, and the README example was a bad demonstration of that. We're rewriting it.
    67|>
    68|> - **"30x lossless compression" was overstated.** AAAK is a lossy abbreviation system (entity codes, sentence truncation). Independent benchmarks show AAAK mode scores **84.2% R@5 vs raw mode's 96.6%** on LongMemEval � a 12.4 point regression. The honest framing is: AAAK is an experimental compression layer that trades fidelity for token density, and **the 96.6% headline number is from RAW mode, not AAAK**.
    69|>
    70|> - **"+34% palace boost" was misleading.** That number compares unfiltered search to wing+room metadata filtering. Metadata filtering is a standard ChromaDB feature, not a novel retrieval mechanism. Real and useful, but not a moat.
    71|>
    72|> - **"Contradiction detection"** exists as a separate utility (`fact_checker.py`) but is not currently wired into the knowledge graph operations as the README implied.
    73|>
    74|> - **"100% with Haiku rerank"** is real (we have the result files) but the rerank pipeline is not in the public benchmark scripts. We're adding it.
    75|>
    76|> **What's still true and reproducible:**
    77|>
    78|> - **96.6% R@5 on LongMemEval in raw mode**, on 500 questions, zero API calls � independently reproduced on M2 Ultra in under 5 minutes by [@gizmax](https://github.com/milla-jovovich/mempalace/issues/39).
    79|> - Local, free, no subscription, no cloud, no data leaving your machine.
    80|> - The architecture (wings, rooms, closets, drawers) is real and useful, even if it's not a magical retrieval boost.
    81|>
    82|> **What we're doing:**
    83|>
    84|> 1. Rewriting the AAAK example with real tokenizer counts and a scenario where AAAK actually demonstrates compression
    85|> 2. Adding `mode raw / aaak / rooms` clearly to the benchmark documentation so the trade-offs are visible
    86|> 3. Wiring `fact_checker.py` into the KG ops so the contradiction detection claim becomes true
    87|> 4. Pinning ChromaDB to a tested range (Issue #100), fixing the shell injection in hooks (#110), and addressing the macOS ARM64 segfault (#74)
    88|>
    89|> **Thank you to everyone who poked holes in this.** Brutal honest criticism is exactly what makes open source work, and it's what we asked for. Special thanks to [@panuhorsmalahti](https://github.com/milla-jovovich/mempalace/issues/43), [@lhl](https://github.com/milla-jovovich/mempalace/issues/27), [@gizmax](https://github.com/milla-jovovich/mempalace/issues/39), and everyone who filed an issue or a PR in the first 48 hours. We're listening, we're fixing, and we'd rather be right than impressive.
    90|>
    91|> � *Milla Jovovich & Ben Sigman*
    92|
    93|---
    94|
    95|## An important follow up note regarding fake MemPalace websites - April 11, 2026
    96|
    97|Several Community Members (#267, #326, #506) have pointed out there are fake MemPalace websites popping up, including ones with Malware.
    98|
    99|To be super clear, MemPalace *has no website* (at least for now), so anything claiming to be one is false.
   100|
   101|Thanks to our Community Members for letting us know about the problem.
   102|
   103|Stay safe out there.
   104|
   105|---
   106|
   107|## Quick Start
   108|
   109|```bash
   110|pip install mempalace
   111|
   112|# Set up your world � who you work with, what your projects are
   113|mempalace init ~/projects/myapp
   114|
   115|# Mine your data
   116|mempalace mine ~/projects/myapp                    # projects � code, docs, notes
   117|mempalace mine ~/chats/ --mode convos              # convos � Claude, ChatGPT, Slack exports
   118|mempalace mine ~/chats/ --mode convos --extract general  # general � classifies into decisions, milestones, problems
   119|
   120|# Search anything you've ever discussed
   121|mempalace search "why did we switch to GraphQL"
   122|
   123|# Your AI remembers
   124|mempalace status
   125|```
   126|
   127|Three mining modes: **projects** (code and docs), **convos** (conversation exports), and **general** (auto-classifies into decisions, preferences, milestones, problems, and emotional context). Everything stays on your machine.
   128|
   129|---
   130|
   131|## How You Actually Use It
   132|
   133|After the one-time setup (install ? init ? mine), you don't run MemPalace commands manually. Your AI uses it for you. There are two ways, depending on which AI you use.
   134|
   135|### With Claude Code (recommended)
   136|
   137|Native marketplace install:
   138|
   139|```bash
   140|claude plugin marketplace add milla-jovovich/mempalace
   141|claude plugin install --scope user mempalace
   142|```
   143|
   144|Restart Claude Code, then type `/skills` to verify "mempalace" appears.
   145|
   146|### With Claude, ChatGPT, Cursor, Gemini (MCP-compatible tools)
   147|
   148|```bash
   149|# Connect MemPalace once
   150|claude mcp add mempalace -- python -m mempalace.mcp_server
   151|```
   152|
   153|Now your AI has 19 tools available through MCP. Ask it anything:
   154|
   155|> *"What did we decide about auth last month?"*
   156|
   157|Claude calls `mempalace_search` automatically, gets verbatim results, and answers you. You never type `mempalace search` again. The AI handles it.
   158|
   159|MemPalace also works natively with **Gemini CLI** (which handles the server and save hooks automatically) � see the [Gemini CLI Integration Guide](examples/gemini_cli_setup.md).
   160|
   161|### With local models (Llama, Mistral, or any offline LLM)
   162|
   163|Local models generally don't speak MCP yet. Two approaches:
   164|
   165|**1. Wake-up command** � load your world into the model's context:
   166|
   167|```bash
   168|mempalace wake-up > context.txt
   169|# Paste context.txt into your local model's system prompt
   170|```
   171|
   172|This gives your local model ~170 tokens of critical facts (in AAAK if you prefer) before you ask a single question.
   173|
   174|**2. CLI search** � query on demand, feed results into your prompt:
   175|
   176|```bash
   177|mempalace search "auth decisions" > results.txt
   178|# Include results.txt in your prompt
   179|```
   180|
   181|Or use the Python API:
   182|
   183|```python
   184|from mempalace.searcher import search_memories
   185|results = search_memories("auth decisions", palace_path="~/.mempalace/palace")
   186|# Inject into your local model's context
   187|```
   188|
   189|Either way � your entire memory stack runs offline. ChromaDB on your machine, Llama on your machine, AAAK for compression, zero cloud calls.
   190|
   191|---
   192|
   193|## The Problem
   194|
   195|Decisions happen in conversations now. Not in docs. Not in Jira. In conversations with Claude, ChatGPT, Copilot. The reasoning, the tradeoffs, the "we tried X and it failed because Y" � all trapped in chat windows that evaporate when the session ends.
   196|
   197|**Six months of daily AI use = 19.5 million tokens.** That's every decision, every debugging session, every architecture debate. Gone.
   198|
   199|| Approach | Tokens loaded | Annual cost |
   200||----------|--------------|-------------|
   201|| Paste everything | 19.5M � doesn't fit any context window | Impossible |
   202|| LLM summaries | ~650K | ~$507/yr |
   203|| **MemPalace wake-up** | **~170 tokens** | **~$0.70/yr** |
   204|| **MemPalace + 5 searches** | **~13,500 tokens** | **~$10/yr** |
   205|
   206|MemPalace loads 170 tokens of critical facts on wake-up � your team, your projects, your preferences. Then searches only when needed. $10/year to remember everything vs $507/year for summaries that lose context.
   207|
   208|---
   209|
   210|## How It Works
   211|
   212|### The Palace
   213|
   214|The layout is fairly simple, though it took a long time to get there.
   215|
   216|It starts with a **wing**. Every project, person, or topic you're filing gets its own wing in the palace.
   217|
   218|Each wing has **rooms** connected to it, where information is divided into subjects that relate to that wing � so every room is a different element of what your project contains. Project ideas could be one room, employees could be another, financial statements another. There can be an endless number of rooms that split the wing into sections. The MemPalace install detects these for you automatically, and of course you can personalize it any way you feel is right.
   219|
   220|Every room has a **closet** connected to it, and here's where things get interesting. We've developed an AI language called **AAAK**. Don't ask � it's a whole story of its own. Your agent learns the AAAK shorthand every time it wakes up. Because AAAK is essentially English, but a very truncated version, your agent understands how to use it in seconds. It comes as part of the install, built into the MemPalace code. In our next update, we'll add AAAK directly to the closets, which will be a real game changer � the amount of info in the closets will be much bigger, but it will take up far less space and far less reading time for your agent.
   221|
   222|Inside those closets are **drawers**, and those drawers are where your original files live. In this first version, we haven't used AAAK as a closet tool, but even so, the summaries have shown **96.6% recall** in all the benchmarks we've done across multiple benchmarking platforms. Once the closets use AAAK, searches will be even faster while keeping every word exact. But even now, the closet approach has been a huge boon to how much info is stored in a small space � it's used to easily point your AI agent to the drawer where your original file lives. You never lose anything, and all this happens in seconds.
   223|
   224|There are also **halls**, which connect rooms within a wing, and **tunnels**, which connect rooms from different wings to one another. So finding things becomes truly effortless � we've given the AI a clean and organized way to know where to start searching, without having to look through every keyword in huge folders.
   225|
   226|You say what you're looking for and boom, it already knows which wing to go to. Just *that* in itself would have made a big difference. But this is beautiful, elegant, organic, and most importantly, efficient.
   227|
   228|```
   229|  ???????????????????????????????????????????????????????????????
   230|  ?  WING: Person                                              ?
   231|  ?                                                            ?
   232|  ?    ????????????  ??hall??  ????????????                    ?
   233|  ?    ?  Room A  ?            ?  Room B  ?                    ?
   234|  ?    ????????????            ????????????                    ?
   235|  ?         ?                                                  ?
   236|  ?         ?                                                  ?
   237|  ?    ????????????      ????????????                          ?
   238|  ?    ?  Closet  ? ???? ?  Drawer  ?                          ?
   239|  ?    ????????????      ????????????                          ?
   240|  ??????????????????????????????????????????????????????????????
   241|            ?
   242|          tunnel
   243|            ?
   244|  ??????????????????????????????????????????????????????????????
   245|  ?  WING: Project                                             ?
   246|  ?         ?                                                  ?
   247|  ?    ????????????  ??hall??  ????????????                    ?
   248|  ?    ?  Room A  ?            ?  Room C  ?                    ?
   249|  ?    ????????????            ????????????                    ?
   250|  ?         ?                                                  ?
   251|  ?         ?                                                  ?
   252|  ?    ????????????      ????????????                          ?
   253|  ?    ?  Closet  ? ???? ?  Drawer  ?                          ?
   254|  ?    ????????????      ????????????                          ?
   255|  ???????????????????????????????????????????????????????????????
   256|```
   257|
   258|**Wings** � a person or project. As many as you need.
   259|**Rooms** � specific topics within a wing. Auth, billing, deploy � endless rooms.
   260|**Halls** � connections between related rooms *within* the same wing. If Room A (auth) and Room B (security) are related, a hall links them.
   261|**Tunnels** � connections *between* wings. When Person A and a Project both have a room about "auth," a tunnel cross-references them automatically.
   262|**Closets** � summaries that point to the original content. (In v3.0.0 these are plain-text summaries; AAAK-encoded closets are coming in a future update � see [Task #30](https://github.com/milla-jovovich/mempalace/issues/30).)
   263|**Drawers** � the original verbatim files. The exact words, never summarized.
   264|
   265|**Halls** are memory types � the same in every wing, acting as corridors:
   266|- `hall_facts` � decisions made, choices locked in
   267|- `hall_events` � sessions, milestones, debugging
   268|- `hall_discoveries` � breakthroughs, new insights
   269|- `hall_preferences` � habits, likes, opinions
   270|- `hall_advice` � recommendations and solutions
   271|
   272|**Rooms** are named ideas � `auth-migration`, `graphql-switch`, `ci-pipeline`. When the same room appears in different wings, it creates a **tunnel** � connecting the same topic across domains:
   273|
   274|```
   275|wing_kai       / hall_events / auth-migration  ? "Kai debugged the OAuth token refresh"
   276|wing_driftwood / hall_facts  / auth-migration  ? "team decided to migrate auth to Clerk"
   277|wing_priya     / hall_advice / auth-migration  ? "Priya approved Clerk over Auth0"
   278|```
   279|
   280|Same room. Three wings. The tunnel connects them.
   281|
   282|### Why Structure Matters
   283|
   284|Tested on 22,000+ real conversation memories:
   285|
   286|```
   287|Search all closets:          60.9%  R@10
   288|Search within wing:          73.1%  (+12%)
   289|Search wing + hall:          84.8%  (+24%)
   290|Search wing + room:          94.8%  (+34%)
   291|```
   292|
   293|Wings and rooms aren't cosmetic. They're a **34% retrieval improvement**. The palace structure is the product.
   294|
   295|### The Memory Stack
   296|
   297|| Layer | What | Size | When |
   298||-------|------|------|------|
   299|| **L0** | Identity � who is this AI? | ~50 tokens | Always loaded |
   300|| **L1** | Critical facts � team, projects, preferences | ~120 tokens (AAAK) | Always loaded |
   301|| **L2** | Room recall � recent sessions, current project | On demand | When topic comes up |
   302|| **L3** | Deep search � semantic query across all closets | On demand | When explicitly asked |
   303|
   304|Your AI wakes up with L0 + L1 (~170 tokens) and knows your world. Searches only fire when needed.
   305|
   306|### AAAK Dialect (experimental)
   307|
   308|AAAK is a lossy abbreviation system � entity codes, structural markers, and sentence truncation � designed to pack repeated entities and relationships into fewer tokens at scale. It is **readable by any LLM that reads text** (Claude, GPT, Gemini, Llama, Mistral) without a decoder, so a local model can use it without any cloud dependency.
   309|
   310|**Honest status (April 2026):**
   311|
   312|- **AAAK is lossy, not lossless.** It uses regex-based abbreviation, not reversible compression.
   313|- **It does not save tokens at small scales.** Short text already tokenizes efficiently. AAAK overhead (codes, separators) costs more than it saves on a few sentences.
   314|- **It can save tokens at scale** � in scenarios with many repeated entities (a team mentioned hundreds of times, the same project across thousands of sessions), the entity codes amortize.
   315|- **AAAK currently regresses LongMemEval** vs raw verbatim retrieval (84.2% R@5 vs 96.6%). The 96.6% headline number is from **raw mode**, not AAAK mode.
   316|- **The MemPalace storage default is raw verbatim text in ChromaDB** � that's where the benchmark wins come from. AAAK is a separate compression layer for context loading, not the storage format.
   317|
   318|We're iterating on the dialect spec, adding a real tokenizer for stats, and exploring better break points for when to use it. Track progress in [Issue #43](https://github.com/milla-jovovich/mempalace/issues/43) and [#27](https://github.com/milla-jovovich/mempalace/issues/27).
   319|
   320|### Contradiction Detection (experimental, not yet wired into KG)
   321|
   322|A separate utility (`fact_checker.py`) can check assertions against entity facts. It's not currently called automatically by the knowledge graph operations � this is being fixed (track in [Issue #27](https://github.com/milla-jovovich/mempalace/issues/27)). When enabled it catches things like:
   323|
   324|```
   325|Input:  "Soren finished the auth migration"
   326|Output: ? AUTH-MIGRATION: attribution conflict � Maya was assigned, not Soren
   327|
   328|Input:  "Kai has been here 2 years"
   329|Output: ? KAI: wrong_tenure � records show 3 years (started 2023-04)
   330|
   331|Input:  "The sprint ends Friday"
   332|Output: ? SPRINT: stale_date � current sprint ends Thursday (updated 2 days ago)
   333|```
   334|
   335|Facts checked against the knowledge graph. Ages, dates, and tenures calculated dynamically � not hardcoded.
   336|
   337|---
   338|
   339|## Real-World Examples
   340|
   341|### Solo developer across multiple projects
   342|
   343|```bash
   344|# Mine each project's conversations
   345|mempalace mine ~/chats/orion/  --mode convos --wing orion
   346|mempalace mine ~/chats/nova/   --mode convos --wing nova
   347|mempalace mine ~/chats/helios/ --mode convos --wing helios
   348|
   349|# Six months later: "why did I use Postgres here?"
   350|mempalace search "database decision" --wing orion
   351|# ? "Chose Postgres over SQLite because Orion needs concurrent writes
   352|#    and the dataset will exceed 10GB. Decided 2025-11-03."
   353|
   354|# Cross-project search
   355|mempalace search "rate limiting approach"
   356|# ? finds your approach in Orion AND Nova, shows the differences
   357|```
   358|
   359|### Team lead managing a product
   360|
   361|```bash
   362|# Mine Slack exports and AI conversations
   363|mempalace mine ~/exports/slack/ --mode convos --wing driftwood
   364|mempalace mine ~/.claude/projects/ --mode convos
   365|
   366|# "What did Soren work on last sprint?"
   367|mempalace search "Soren sprint" --wing driftwood
   368|# ? 14 closets: OAuth refactor, dark mode, component library migration
   369|
   370|# "Who decided to use Clerk?"
   371|mempalace search "Clerk decision" --wing driftwood
   372|# ? "Kai recommended Clerk over Auth0 � pricing + developer experience.
   373|#    Team agreed 2026-01-15. Maya handling the migration."
   374|```
   375|
   376|### Before mining: split mega-files
   377|
   378|Some transcript exports concatenate multiple sessions into one huge file:
   379|
   380|```bash
   381|mempalace split ~/chats/                      # split into per-session files
   382|mempalace split ~/chats/ --dry-run            # preview first
   383|mempalace split ~/chats/ --min-sessions 3     # only split files with 3+ sessions
   384|```
   385|
   386|---
   387|
   388|## Knowledge Graph
   389|
   390|Temporal entity-relationship triples � like Zep's Graphiti, but SQLite instead of Neo4j. Local and free.
   391|
   392|```python
   393|from mempalace.knowledge_graph import KnowledgeGraph
   394|
   395|kg = KnowledgeGraph()
   396|kg.add_triple("Kai", "works_on", "Orion", valid_from="2025-06-01")
   397|kg.add_triple("Maya", "assigned_to", "auth-migration", valid_from="2026-01-15")
   398|kg.add_triple("Maya", "completed", "auth-migration", valid_from="2026-02-01")
   399|
   400|# What's Kai working on?
   401|kg.query_entity("Kai")
   402|# ? [Kai ? works_on ? Orion (current), Kai ? recommended ? Clerk (2026-01)]
   403|
   404|# What was true in January?
   405|kg.query_entity("Maya", as_of="2026-01-20")
   406|# ? [Maya ? assigned_to ? auth-migration (active)]
   407|
   408|# Timeline
   409|kg.timeline("Orion")
   410|# ? chronological story of the project
   411|```
   412|
   413|Facts have validity windows. When something stops being true, invalidate it:
   414|
   415|```python
   416|kg.invalidate("Kai", "works_on", "Orion", ended="2026-03-01")
   417|```
   418|
   419|Now queries for Kai's current work won't return Orion. Historical queries still will.
   420|
   421|| Feature | MemPalace | Zep (Graphiti) |
   422||---------|-----------|----------------|
   423|| Storage | SQLite (local) | Neo4j (cloud) |
   424|| Cost | Free | $25/mo+ |
   425|| Temporal validity | Yes | Yes |
   426|| Self-hosted | Always | Enterprise only |
   427|| Privacy | Everything local | SOC 2, HIPAA |
   428|
   429|---
   430|
   431|## Specialist Agents
   432|
   433|Create agents that focus on specific areas. Each agent gets its own wing and diary in the palace � not in your CLAUDE.md. Add 50 agents, your config stays the same size.
   434|
   435|```
   436|~/.mempalace/agents/
   437|  ??? reviewer.json       # code quality, patterns, bugs
   438|  ??? architect.json      # design decisions, tradeoffs
   439|  ??? ops.json            # deploys, incidents, infra
   440|```
   441|
   442|Your CLAUDE.md just needs one line:
   443|
   444|```
   445|You have MemPalace agents. Run mempalace_list_agents to see them.
   446|```
   447|
   448|The AI discovers its agents from the palace at runtime. Each agent:
   449|
   450|- **Has a focus** � what it pays attention to
   451|- **Keeps a diary** � written in AAAK, persists across sessions
   452|- **Builds expertise** � reads its own history to stay sharp in its domain
   453|
   454|```
   455|# Agent writes to its diary after a code review
   456|mempalace_diary_write("reviewer",
   457|    "PR#42|auth.bypass.found|missing.middleware.check|pattern:3rd.time.this.quarter|????")
   458|
   459|# Agent reads back its history
   460|mempalace_diary_read("reviewer", last_n=10)
   461|# ? last 10 findings, compressed in AAAK
   462|```
   463|
   464|Each agent is a specialist lens on your data. The reviewer remembers every bug pattern it's seen. The architect remembers every design decision. The ops agent remembers every incident. They don't share a scratchpad � they each maintain their own memory.
   465|
   466|Letta charges $20�200/mo for agent-managed memory. MemPalace does it with a wing.
   467|
   468|---
   469|
   470|## MCP Server
   471|
   472|```bash
   473|# Via plugin (recommended)
   474|claude plugin marketplace add milla-jovovich/mempalace
   475|claude plugin install --scope user mempalace
   476|
   477|# Or manually
   478|claude mcp add mempalace -- python -m mempalace.mcp_server
   479|```
   480|
   481|### 19 Tools
   482|
   483|**Palace (read)**
   484|
   485|| Tool | What |
   486||------|------|
   487|| `mempalace_status` | Palace overview + AAAK spec + memory protocol |
   488|| `mempalace_list_wings` | Wings with counts |
   489|| `mempalace_list_rooms` | Rooms within a wing |
   490|| `mempalace_get_taxonomy` | Full wing ? room ? count tree |
   491|| `mempalace_search` | Semantic search with wing/room filters |
   492|| `mempalace_check_duplicate` | Check before filing |
   493|| `mempalace_get_aaak_spec` | AAAK dialect reference |
   494|
   495|**Palace (write)**
   496|
   497|| Tool | What |
   498||------|------|
   499|| `mempalace_add_drawer` | File verbatim content |
   500|| `mempalace_delete_drawer` | Remove by ID |
   501|