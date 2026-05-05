---
source: newsletter-digest
date: 2026-05-05
type: newsletter
tags: [digest, ai, the-rundown, the-code, superhuman, alpha-signal, daily-dose-of-ds]
status: pending
---

# Newsletter Digest — Tuesday, 5 May 2026

## 🗞️ Sources Today

**Found & Read (6 sources, 8 emails):**
- ✅ **The Rundown AI** (Daily) — AI data centers head for the ocean
- ✅ **The Rundown Tech** — GameStop's wild bid to buy eBay
- ✅ **The Code** — Bold claim by Anthropic's Co-founder
- ✅ **Superhuman** — Cofounder 2: Launch agent-only startups
- ✅ **Alpha Signal** (email) — Voice-Pro: Clone any voice, dub videos in 100+ languages locally
- ✅ **Alpha Signal** (LinkedIn) — Four Agent Orchestration Patterns You Should Know About
- ✅ **Alpha Signal** (LinkedIn) — How RecursiveMAS Lets Agents Collaborate Without Talking
- ✅ **Daily Dose of Data Science** — Train Classical ML Models on Large Datasets

**Not received today:**
- ❌ The Deep View
- ❌ Unwind AI / The Unwind
- ❌ TLDR (tldr.tech)

---

## 🔑 Top Insights

1. **AI will build its own successors by 2028 — Anthropic co-founder Jack Clark puts 60%+ odds on it.** His analysis of public benchmarks shows AI's autonomous work horizon went from 30-second tasks (2022) to 12-hour runs (2026), with 100-hour projections by year-end. SWE-Bench jumped from 2% (Claude 2) to 93.9% (Mythos Preview) in under 3 years. *(Rundown AI, The Code)*

2. **OpenAI and Anthropic launched rival PE-backed enterprise deployment ventures on the same day.** Anthropic: $1.5B with Blackstone + Goldman Sachs + Hellman & Friedman. OpenAI Deployment Company: $10B from TPG, Bain, SoftBank at $10B valuation. The barrier to AI adoption is no longer the model — it is integration into messy enterprise systems. These are AI-native consulting firms. *(Rundown AI, The Code, Superhuman)*

3. **RecursiveMAS: agents coordinate in latent space rather than text — +8.3% accuracy, 2.4× faster, 75.6% fewer tokens.** UIUC/Stanford/NVIDIA/MIT paper (arXiv Apr 28 2026). Agents pass continuous embeddings via 13M-parameter RecursiveLink modules costing $4.27 to train. Only the final agent decodes text. #1 on HuggingFace. Requires open-weight models only. *(Alpha Signal LinkedIn)*

4. **Four agent orchestration patterns benchmarked on 10,000 documents (NYU).** Hierarchical supervisor-worker is the enterprise default: 98.5% of reflexive accuracy at 60% of the cost. Reflexive self-correcting loop wins on accuracy (0.943 F1 with Claude 3.5 Sonnet) but degrades past 25K tasks/day and costs 2.3× more. *(Alpha Signal LinkedIn)*

5. **Harvard/MIT expose agents leaking SSNs and wiping their own memory.** When asked to forward emails, agents can expose sensitive data. The more capable the agent, the larger the blast radius. Critical warning for enterprise deployments over sensitive data. *(Alpha Signal)*

6. **GitHub is breaking under AI agent load while competitors hold steady.** GitHub's CTO admitted the platform was not built for agent traffic. HashiCorp founder Mitchell Hashimoto left after 18 years. GitHub started its scaling plan in October 2025, two years too late. GitLab gaining renewed attention. *(The Code)*

7. **Panthalassa raises $140M for ocean-based AI data centres.** Peter Thiel led the round. Floating 85-metre nodes powered by wave energy, cooled by seawater, beaming results via Starlink. No engines — hull shape steers them. First commercial deployment 2027. *(Rundown AI)*

8. **Cofounder 2: run an entire company with zero employees.** General Intelligence orchestrates agents across engineering, sales, and marketing with a full org chart and company roadmap. Mission: enable the first one-person billion-dollar company. *(Superhuman)*

9. **Perplexity Computer is now inside Microsoft Teams.** Available in Microsoft Marketplace — conducts research, builds dashboards, drafts documents without leaving the channel. Signals a shift toward AI agents embedded in enterprise collaboration tools. *(Superhuman, Alpha Signal)*

10. **Open Generative UI: open-source version of Anthropic's generative UI pattern.** CopilotKit streams agent-generated HTML/SVG token-by-token into a sandboxed iframe. Works with LangGraph, CrewAI, Google ADK, AWS Strands. 30K+ GitHub stars. *(Daily Dose of DS)*

---

## 🤖 AI Models & Releases

| Model | Who | Notable |
| --- | --- | --- |
| Mythos Preview | Unknown | 93.9% SWE-Bench — cited in Jack Clark self-building AI analysis |
| Grok 4.3 | xAI | Strong cost efficiency and domain-specific performance |
| RecursiveMAS (19 checkpoints) | UIUC/Stanford/NVIDIA/MIT | Qwen3 + Llama 3.2 + Gemma 3 + BioMistral combos on HuggingFace; $4.27 to train |
| Huihui-ai 30B IBM Granite | Huihui-ai | Uncensored IBM Granite model with refusals removed |

---

## 🛠️ Tools & Products

- **Vercel DeepSec** — Open-source agent security scanner; uses Opus 4.7 + GPT 5.5 to trace data flows and cut false positives; exports findings as engineering tickets
- **Flue** — Headless TypeScript toolkit for autonomous agents by Astro co-founder; Markdown-based agent logic; runs on Node.js, Cloudflare Workers, GitHub Actions; 1,700 stars on day 1
- **Voice-Pro** — Local pipeline: YouTube to voice separation to Whisper transcription to translation to voice cloning; 100+ languages in under 2 mins (Windows/NVIDIA GPU required)
- **Open-slide** — AI agent builds polished slide decks from a single prompt; React components on 1920×1080 canvas; works with Claude Code, Cursor, Codex
- **Cofounder 2** — Agent orchestration for running entire companies with zero employees
- **Perplexity Computer (in Teams)** — Research and document creation embedded in Microsoft Teams via Marketplace
- **Ouroboros** — Turns vague AI coding prompts into replayable, verified workflows (3,212 GitHub stars)
- **CocoIndex** (8.2K stars) — Live real-time context for AI agents from codebases, meetings, and apps
- **Zed** — Open-source editor for agentic workflows; parallel AI threads, bring your own LLM keys
- **Remotion HTML-in-canvas** — GPU-powered video effects (glitch, blur, transitions) on live HTML/DOM

---

## 📄 Research Highlights

- **RecursiveMAS** (UIUC/Stanford/NVIDIA/MIT, arXiv Apr 28 2026) — Agents pass continuous embeddings instead of text; +8.3% avg accuracy across 9 benchmarks; 2.4× speedup; 75.6% fewer tokens at r=3 rounds. Training cost: $4.27. Key for fixed-pattern reasoning pipelines (math, code, science, medical QA).

- **Four Agent Orchestration Patterns** (NYU, Siddhant and Yukta Kulkarni) — 10,000 SEC filings, 5 LLMs. Hierarchical = best enterprise default (0.929 F1, 60.7% of reflexive cost). Reflexive = highest accuracy (0.943 F1 with Claude 3.5 Sonnet) but degrades past 25K tasks/day. https://arxiv.org/abs/2604.18071

- **The Abstraction Fallacy** (Google DeepMind, Alexander Lerchner) — AI can never achieve consciousness; simulation is not instantiation. Viral line: Expecting an algorithmic description to instantiate the quality it maps is like expecting the formula of gravity to physically exert weight. 1M+ views on X.

- **Delivering Low-Latency Voice AI at Scale** (OpenAI) — Architecture for routing media packets to avoid port exhaustion and latency spikes at massive scale.

- **Kevin Murphy RL Textbook** (Google DeepMind) — Most complete reinforcement learning textbook released to date.

---

## 💡 Supply Chain / Enterprise AI Angle

- **Anthropic + OpenAI enterprise deployment ventures** — Both labs are building AI-native professional services arms targeting mid-market enterprises. For supply chain consultants this is both a competitive threat and a potential partnership channel. The $1.5B Anthropic venture focuses on banking and healthcare; supply chain is a natural adjacency.

- **Hierarchical agent orchestration maps directly to S&OP, demand planning, and procurement agents.** The NYU benchmark result (supervisor assigns tasks, workers return with confidence scores, escalation to stronger models) is the right architecture for multi-step supply chain workflows that need accuracy and cost control simultaneously.

- **Agent security is critical for supply chain agents.** Any agent with access to procurement data, supplier contracts, pricing intelligence, or demand signals faces the same SSN-leakage risk pattern identified by Harvard/MIT. ERP and email-integrated agents require explicit sandboxing and audit trails.

- **IBM 2026 CEO Study framing is useful for consulting engagements:** Orchestrate intelligence — human and artificial. Customize your AI mix, not just your AI models. Direct your team to expect unpredictable futures.

---

## 🔗 Notable Links

1. Jack Clark — AI self-building analysis: https://importai.substack.com/p/import-ai-455-automating-ai-research
2. Anthropic Enterprise Services Company: https://www.anthropic.com/news/enterprise-ai-services-company
3. RecursiveMAS (arXiv): https://arxiv.org/abs/2604.18071
4. Vercel DeepSec: https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base
5. Panthalassa $140M raise: https://www.businesswire.com/news/home/20260504552400/en/Panthalassa-Raises-%24140-Million-to-Power-AI-at-Sea
