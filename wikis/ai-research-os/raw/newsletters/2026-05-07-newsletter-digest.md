---
source: newsletter-digest
date: 2026-05-07
type: newsletter
tags: [digest, ai, the-rundown, the-code, superhuman, alpha-signal, daily-dose-of-ds]
status: pending
---

# Newsletter Digest — Thursday, 7 May 2026

## 🗞️ Sources Today

**Found & read (5 brands / 6 emails):**
- **The Rundown AI** — Daily edition ("Anthropic, SpaceX become unlikely compute partners")
- **The Rundown AI** — Robotics edition ("Genesis robot makes breakfast")
- **The Code** (via Superhuman)
- **Superhuman AI** (Zain Kahn)
- **Alpha Signal**
- **Daily Dose of Data Science**

**Not received today:**
- The Deep View *(not found)*
- Unwind AI / The Unwind *(not found)*
- TLDR / TLDR AI *(not found)*

---

## 🔑 Top Insights

1. **Anthropic leased SpaceX's entire Colossus 1 cluster** — 220K+ Nvidia GPUs, 300+ MW in Memphis. Claude Code rate limits doubled across Pro/Max/Team/Enterprise; peak-hour throttling eliminated for Pro and Max. Anthropic also reportedly committed $200B over 5 years to Google Cloud compute. Musk's "enemy of my enemy" logic: helping Anthropic weakens OpenAI. *(Rundown, The Code, Superhuman, Alpha Signal)*

2. **Claude Managed Agents: four major upgrades ship simultaneously** — (a) *Dreaming*: background review of past sessions updates agent memory; Wisedocs reports 50% faster document reviews; (b) *Multiagent orchestration*: lead agent splits tasks to parallel specialist sub-agents sharing a filesystem; (c) *Outcomes*: rubric-based grader loops back for fixes, improving success up to 10 percentage points; (d) *Webhooks*: fire-and-forget async results. *(Rundown, Superhuman, Alpha Signal)*

3. **Enterprise RAG accuracy collapses at scale** — Onyx's EnterpriseRAG-Bench (500K synthetic docs across Slack, Gmail, Jira, Confluence, GitHub, Drive) shows vector search drops from 90.7% at 5K docs to 50.6% at 500K. BM25 degrades more gracefully (85.8% → 68.4%). Root cause: embedding space clustering creates 40–60 competitors for top-k slots. Lesson: always test at realistic corpus size. *(Daily Dose of DS)*

4. **Vibe coding and agentic engineering are converging** — Django co-creator Simon Willison admits abandoning line-by-line review for production code ("normalization of deviance"). Coinbase CEO announced 700 layoffs + AI-native restructure where non-technical groups now ship production code. Code quality trust has moved from polish to production track record. *(The Code)*

5. **Zyphra ZAYA1-8B: frontier-class reasoning without Nvidia** — First MoE model built entirely on 1,024-node AMD MI300X cluster (IBM Cloud). <1B active parameters, rivals frontier models on math and coding. Open-weight on Hugging Face. *(The Code)*

6. **Stanford undergrad unifies deep learning generalization, 5× training speedup** — A Stanford undergrad's theory resolving long-standing deep learning generalization mysteries also enables a 5× speedup in training. *(Alpha Signal)*

7. **DeepMind uses EVE Online as next AI research sandbox** — Minority stake in Fenris Creations (CCP Games spinoff). EVE's 23-year-old player-driven economy tests long-timeline reasoning, persistent memory, and learning — shift from game-playing AI to agents in living, unpredictable systems. *(Rundown)*

8. **Aurora + McLane: fully driverless trucking goes commercial** — Dallas–Houston corridor, no safety driver, 280K autonomous miles, 1,400 loads, 100% on-time. Plans to scale across U.S. Sun Belt by end of 2026. *(Rundown Robotics)*

9. **"AI fog" making long-term planning harder** — Harvard Business Review coins the term for AI-driven planning paralysis. Recommended shift: swap long-term plans for optionality — reskill often, pivot early, avoid locking into single paths. *(Superhuman)*

10. **Rowboat: local AI second brain as knowledge graph** — Open-source (13k⭐, Apache-2.0) ingests Gmail, Calendar, Fireflies transcripts. Extracts decisions/commitments as typed entity nodes with backlinks. Runs 100% locally via Ollama, stored as plain Markdown in an Obsidian-compatible vault. *(Daily Dose of DS)*

---

## 🤖 AI Models & Releases

| Model | By | What's Notable |
|---|---|---|
| **ZAYA1-8B** | Zyphra | First MoE trained entirely on AMD MI300X; <1B active params; rivals frontier math/coding. Open-weight on Hugging Face. |
| **GENE-26.5** | Genesis AI | Foundation model for robotics + dexterous hand; trains in physics sim 430K× faster than real time. |
| **GPT-5.5 Instant** | OpenAI | New default model across ChatGPT. |
| **MiniMax M2.7 (quantized)** | MiniMax | Shrunk 230 GB → 74 GB via mixed-bit quantization for Apple Silicon. |
| **Claude Managed Agents** | Anthropic | Dreaming, outcomes, multiagent orchestration, webhooks — all new. |
| **Realtime TTS-2** | OpenAI | Voice AI that adapts to match user tone and emotion in real time. |
| **SubQ** | Subquadratic | Claims 12M token context window, 52× speed boost on long context tasks. |

---

## 🛠️ Tools & Products

- **Rowboat** — Local AI second brain; knowledge graph in Markdown/Obsidian vault. Apache-2.0. 13k⭐. [github.com/rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)
- **OpenReel Video** — Browser-native open-source video editor using WebGPU/WebCodecs. No watermarks, 4K export, runs fully local. MIT licensed.
- **Interact AI** — Turns static websites into interactive AI-guided product experiences with a conversational tour guide. [interactlabs.ai](https://www.interactlabs.ai)
- **Flue** — TypeScript headless agent framework; programmable Claude Code without human-in-the-loop assumption. [flueframework.com](https://flueframework.com)
- **DeepSeek TUI** — Terminal-based coding agent for DeepSeek models with git workflow management. 17.3k⭐. [github.com/Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI)
- **Memoket** — Persistent AI memory layer that captures conversations and context across sessions. [memoket.ai](https://memoket.ai)
- **MRC (OpenAI open-source)** — GPU networking protocol for massive training runs; reroutes around hardware failures in microseconds. Co-developed with AMD, Broadcom, Intel, Microsoft, Nvidia.

---

## 📄 Research Highlights

- **EnterpriseRAG-Bench** (Onyx) — 500K+ synthetic enterprise docs from 8 sources with realistic noise (near-duplicates, misfiled docs, conflicting versions). Benchmark for RAG retrieval accuracy at production scale. Shows vector search cliff from 90.7% → 50.6% at 500K docs; BM25 more resilient. [GitHub](https://github.com/onyx-dot-app/EnterpriseRAG-Bench)
- **Stanford deep learning generalization theory** — Undergraduate-led work unifying why large models generalize; produces 5× training speedup as byproduct. *(Alpha Signal; full paper title not disclosed in source)*
- **Bootstrapping Composer with autoinstall** (Cursor) — Shows older Composer models can autonomously repair broken coding training environments, accelerating training iteration without human intervention. [Cursor Blog](https://cursor.com/blog/bootstrapping-composer-with-autoinstall)
- **Cornell insect flight stability rules** — Two rules derived from a 5-parameter insect flight model enable stable flapping-wing robots without heavy feedback control. *(Rundown Robotics)*

---

## 💡 Supply Chain / Enterprise AI Angle

- **Aurora + McLane driverless trucking** is the lead supply chain story: 100% on-time commercial autonomous freight on the Dallas–Houston corridor, scaling across U.S. Sun Belt by end of 2026. Middle-mile highway automation is now live at commercial scale — directly relevant to logistics network planning, carrier diversification strategy, and freight cost modeling.
- **EnterpriseRAG-Bench findings** are critical for anyone building enterprise AI knowledge systems: RAG accuracy at 5K docs tells you almost nothing about 500K-doc production performance. Applies directly to supply chain knowledge-base AI over contracts, specs, SOPs, and supplier portals.
- **Claude Managed Agents compute upgrade + dreaming**: Better API limits and self-improving agents are directly useful for long-running supply chain workflows — demand planning runs, S&OP simulations, and multi-step scenario analysis agents.
- **China's humanoid robot lead** (Bloomberg, via Rundown Robotics) flagged as likely to extend China's global export dominance in manufacturing — a structural supply chain risk worth monitoring for sourcing strategy.

---

## 🔗 Notable Links

1. [Anthropic + SpaceX compute deal](https://www.anthropic.com/news/higher-limits-spacex) — Official announcement with Claude Code limit details
2. [EnterpriseRAG-Bench GitHub](https://github.com/onyx-dot-app/EnterpriseRAG-Bench) — 500K-doc enterprise RAG benchmark (open-source)
3. [Aurora + McLane driverless trucking](https://ir.aurora.tech/news-events/press-releases/detail/138/aurora-and-mclane-company-partner-to-bring-autonomous-trucks-to-u-s-restaurant-supply-chain) — Commercial driverless freight press release
4. [Claude Managed Agents new features](https://claude.com/blog/new-in-claude-managed-agents) — Dreaming, outcomes, multiagent orchestration
5. [Rowboat local AI second brain](https://github.com/rowboatlabs/rowboat) — 13k⭐ open-source knowledge graph

---

*Digest generated automatically on Thursday, 7 May 2026. 5 of 8 expected daily newsletters received. Missing: The Deep View, Unwind AI, TLDR.*
