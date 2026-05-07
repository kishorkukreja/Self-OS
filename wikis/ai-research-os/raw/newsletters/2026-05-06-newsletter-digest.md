---
source: newsletter-digest
date: 2026-05-06
type: newsletter
tags: [digest, ai, the-rundown, unwind-ai, the-code, superhuman, alpha-signal, daily-dose-of-ds]
status: processed
---

# Newsletter Digest — Wednesday, 6 May 2026

## 🗞️ Sources Today

**Received (6/8 expected daily):**
- The Rundown AI ✅
- Unwind AI ✅
- The Code ✅
- Superhuman ✅
- Alpha Signal ✅
- Daily Dose of Data Science ✅

**Not received (2/8):**
- The Deep View ❌
- TLDR ❌

> Sunday-only newsletters (LLM Watch, DAIR.AI, Causal Python) not searched — today is Wednesday.

---

## 🔑 Top Insights

1. **SubQ's subquadratic attention rewrites long-context economics** — Subquadratic's SSA architecture delivers 12M token context at 1/1000th the compute of standard Transformers, running 52x faster than FlashAttention at 1M tokens. Scores 95% on RULER 128K and 81.8 on SWE-Bench Verified, putting it on par with frontier models. Private beta live at subq.ai. *(Unwind AI, The Code, Superhuman, Alpha Signal)*

2. **GPT-5.5 Instant is now ChatGPT's default model** — 52.5% fewer hallucinations vs GPT-5.3 in high-stakes domains (medicine, law, finance), 30.2% fewer words per response, and a new memory-sources transparency feature. Available as `chat-latest` in the API. *(Rundown, The Code, Superhuman, Alpha Signal)*

3. **Anthropic is building the operating layer for enterprise, domain by domain** — 10 finance agent templates (KYC, DCF models, pitchbooks, month-end close) plus a $1.5B JV with Goldman and Blackstone. Claude now works inside Excel, PowerPoint, Word, and Outlook. This is not a product launch — it's an enterprise land grab. *(Rundown, Unwind AI, The Code, Superhuman, Alpha Signal)*

4. **SKILL.md files have a costly hidden architecture problem** — Most developers treat them as monolithic prompts, but Anthropic's runtime loads them in stages (metadata every turn, body only on trigger, references only when called). A bloated SKILL.md can consume 20% of context before the agent starts; a lean spine + references structure cuts that to 7%. Skills must be re-evaluated after every model upgrade. *(The Code, Unwind AI)*

5. **OpenAI fast-tracks an AI phone to H1 2027** — Per supply-chain analyst Ming-Chi Kuo: MediaTek dual AI chips (separate vision + language processors), enhanced HDR pipeline for agent visual sensing, 30M unit target over 2027–28. Raises questions about overlap with the Jony Ive io device. *(Rundown)*

6. **"Grep, don't RAG" is gaining enterprise traction** — Scout (Agno, open-source) navigates company knowledge live via native APIs (Slack, Google Drive, Linear, MCP servers) at query time rather than searching a stale index. Self-builds a wiki and CRM as it learns. *(Unwind AI)*

7. **Teaching models the WHY behind rules cuts unsafe behavior 54% → 7%** — Anthropic research shows that training on the rationale for safety rules (not just the rules) dramatically reduces unsafe agentic behavior. Published alongside the Goldman finance agent deployment. *(Alpha Signal)*

8. **Self-hosted deep research is now competitive with closed-source tools** — Onyx (open-source) ranked #1 on DeepResearch Bench above OpenAI Deep Research and Perplexity. Stack: Onyx (retrieval) + CrewAI (orchestration) + Voxtral (voice). Critical for teams with data residency or IP-sensitivity constraints. *(Daily Dose of Data Science)*

---

## 🤖 AI Models & Releases

| Model | By | What's Notable |
|---|---|---|
| **GPT-5.5 Instant** | OpenAI | New ChatGPT default; 52.5% fewer hallucinations; 30% more concise; enhanced memory sourcing; `chat-latest` in API |
| **SubQ 1M-Preview** | Subquadratic | First sub-quadratic model; 12M token context; SSA architecture; 52x faster than FlashAttention at 1M tokens; private beta |
| **Grok 4.3** | xAI | 1M token context; always-on reasoning; native video input; $1.25/M input (~40% price cut) |
| **Gemma 4 (updated)** | Google | Up to 3x faster inference via multi-token prediction drafters |

---

## 🛠️ Tools & Products

- **SubQ API / SubQ Code / SubQ Search** — Long-context LLM platform (12M tokens) with coding agent and search. Private beta: subq.ai
- **TinyFish** — Free forever web search + fetch API for agents; structured JSON; real browser rendering; works with Claude Code, Cursor, Hermes, Codex, any framework
- **Scout by Agno** — Open-source context agent; navigates Slack, Google Drive, Linear, MCP servers live; self-builds wiki and CRM
- **exe.dev** — Persistent VMs for agent workflows; HTTPS-accessible immediately; no dashboard; between VPS and serverless
- **Designlang** — Extract any website's design system in one command; outputs 17+ files (DTCG tokens, Tailwind config, Figma variables, motion tokens)
- **Box Automate** — Agentic workflow orchestration at enterprise scale
- **Columns.ai** — Automate data cleaning, visualization, and storytelling with AI
- **HeyGen HyperFrames (Hermes Skill)** — `hermes skills install hyperframes` turns Hermes into a video editor; renders MP4 from X posts, PDFs, or GitHub repos
- **Perplexity Computer for Professional Finance** — 35 dedicated finance workflows + licensed data (Moody's, etc.)

---

## 📄 Research Highlights

- **SubQ: Sparse Subquadratic Attention (SSA)** — Linear compute scaling with context length. 52x faster than FlashAttention at 1M tokens, 63% less compute. 95% RULER 128K, 81.8 SWE-Bench Verified. If benchmarks hold, this breaks the economics of context-heavy agent pipelines.

- **Anthropic: Rule Reasoning vs Rule Memorisation** *(Alpha Signal)* — Teaching models the rationale behind safety rules (not just the rules) cuts unsafe agentic behavior from 54% to 7%. Directly relevant to anyone deploying autonomous agents in regulated workflows.

- **OpenAI Cookbook: Reliable Agents with Memory and Compaction** — Framework for long agent workflows that fail at context limits. Compaction shrinks active memory; Memory persists reusable workflows. Applicable to production multi-step agentic systems.

- **Open-source tree-index tool: 98.7% accuracy on finance questions** *(Alpha Signal)* — Near-perfect performance on financial Q&A without vector DBs, using tree-structured indexing. Potential alternative to RAG for structured domain knowledge.

- **Onyx DeepResearch Bench: #1 ranking** *(Daily Dose of DS)* — 100 PhD-level tasks across 22 fields. Beats OpenAI Deep Research, Gemini 2.5 Pro, and Perplexity Deep Research on report quality and citation accuracy.

---

## 💡 Supply Chain / Enterprise AI Angle

**Anthropic Finance Agents** — The 10 templates (KYC screening, month-end close, DCF models, credit memos, pitchbooks) are the closest thing yet to off-the-shelf enterprise AI for structured financial workflows. The same pattern — domain-specific templates with built-in data connectors — is the natural next step for supply chain operations (demand planning, procurement, S&OP reporting). Consulting angle: advise clients to evaluate these templates before commissioning custom builds.

**Anthropic's $1.5B JV with Goldman/Blackstone** — Embedding into operational workflows as infrastructure. The same trajectory applies to supply chain: first-mover advantage now goes to firms that integrate deeply, not those that experiment at the margins.

**Self-hosted deep research (Onyx + CrewAI + Voxtral)** — For supply chain consultants serving regulated industries (pharma, defense, food safety), proprietary supplier intelligence cannot go to closed-cloud services. Onyx delivers research-quality output on your own infrastructure. Evaluate as the retrieval backbone for a supplier intelligence or procurement research tool.

**Coinbase's 14% workforce cut — AI-native team shift** — CEO framing: flatten org charts, make every manager a contributor, hire for AI leverage. This is the exact value proposition for AI-augmented supply chain consulting. Teams that demonstrate AI-native delivery models — smaller headcount, faster cycle time — win the next wave of mandates.

**Scout (Agno)** — Live knowledge navigation over company data is directly applicable to procurement: query Slack, email, and Drive for supplier conversations, contract terms, and incident history in real time without RAG staleness. Open-source and forkable.

---

## 🔗 Notable Links

1. [SubQ — first sub-quadratic frontier model, private beta](https://subq.ai)
2. [Anthropic Finance Agent Templates](https://www.anthropic.com/news/finance-agents)
3. [GPT-5.5 Instant release notes](https://openai.com/index/gpt-5-5-instant/)
4. [Onyx — open-source self-hostable deep research stack](https://github.com/onyx-dot-app/onyx)
5. [TinyFish — free web search + fetch API for agents](https://www.tinyfish.ai/)

---

*Digest generated automatically on Wednesday, 6 May 2026. 6 of 8 expected daily newsletters received. Missing: The Deep View, TLDR.*
