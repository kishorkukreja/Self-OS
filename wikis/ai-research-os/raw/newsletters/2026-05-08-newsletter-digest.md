---
source: newsletter-digest
date: 2026-05-08
type: newsletter
tags: [digest, ai, the-rundown, the-rundown-tech, the-code, superhuman, alpha-signal, daily-dose-of-ds]
status: processed
---

# Newsletter Digest — Friday, 8 May 2026

## 🗞️ Sources Today

**Found (6 emails / 5 newsletter brands):**

| Newsletter | Subject | Time (UTC) |
|---|---|---|
| ✅ The Rundown AI | OpenAI closes reasoning gap in voice agents | 10:09 |
| ✅ The Rundown Tech | 'RAMageddon' is coming for your laptop | 14:34 |
| ✅ The Code | OpenAI drops new series of voice models | 14:02 |
| ✅ Superhuman | Claude’s now available for Microsoft 365 | 13:05 |
| ✅ Alpha Signal | Anthropic Claude integrates across Microsoft Office | 12:05 |
| ✅ Daily Dose of Data Science | A Smarter Claude Model Burns More Tokens, Not Fewer! | 20:46 |

**Missing (expected but not received):**
- ❌ The Deep View
- ❌ Unwind AI
- ❌ TLDR (AI & main editions)

*Sunday-only newsletters (LLM Watch, DAIR.AI, Causal Python): Not applicable — today is Friday.*

---

## 🔑 Top Insights

1. **OpenAI GPT-Realtime-2 brings GPT-5-level reasoning to live voice** — New trio of voice APIs closes the reasoning gap: real-time thinking, multi-tool use simultaneously, 70-language translation, and streaming transcription. Scored 96.6% on Big Bench Audio vs 81.4% predecessor (+15 points). Zillow, Priceline, and Deutsche Telekom are early adopters. *(Rundown AI, The Code)*

2. **Claude is now natively embedded across Microsoft 365** — Context travels between Excel, Word, PowerPoint, and Outlook within a session — no re-briefing between apps. Tracked changes in Word, formula-aware Excel edits, template-preserving PowerPoint builds. Available on all paid Claude plans; works with Bedrock/Vertex AI routing. *(Alpha Signal, Superhuman, The Code)*

3. **Anthropic secures xAI’s Colossus (220k+ GPUs) amid compute war** — After 80x Q1 revenue growth caused Claude Code limits to hit, Anthropic locked in xAI’s Memphis Colossus cluster and doubled Claude Code’s 5-hour limits same day. OpenAI has been resetting Codex limits nearly weekly to attract frustrated Anthropic users. *(Superhuman)*

4. **Smarter Claude model = 54% more tokens (not fewer)** — MCPMark V2 benchmarks across 21 backend tasks: better models burn more tokens because they try harder to fill context gaps from poorly structured backends. InsForge (open-source, 9k+ stars) redesigns backend around agents: 3.7M tokens vs 10.4M on the same RAG build, zero manual interventions vs 10. *(Daily Dose of DS)*

5. **“RAMageddon” threatens to kill the cheap laptop** — AI data centres are soaking up DRAM and HBM supply, crowding out consumer devices. Gartner forecasts: PC prices +17%, smartphones +13% in 2026. Sub-$500 entry-level PCs may disappear by 2028. *(Rundown Tech)*

6. **SpaceX files plans for $119B “Terafab” chip mega-factory in Texas** — Grimes County proposal: initial ~$55B buildout, up to $119B in full phases. Would produce advanced semiconductors in-house for Starlink, AI data centres, robotaxis, and Optimus robots. Goal: eliminate dependence on TSMC/Samsung. *(Rundown Tech)*

7. **Anthropic Institute publishes research agenda on self-improving AI** — New formal research arm covers security, economic disruption, governance, and planning for “intelligence explosion” scenarios. Proposes Cold War-style hotlines between AI labs and governments, plus fire drills for sudden capability surges. *(Rundown AI)*

8. **Google ships Chrome Prompt API despite near-universal opposition** — Any website can now query a local Gemini Nano model (silently 4GB downloaded to your machine) without a user permission prompt. Mozilla, WebKit, W3C TAG, and Microsoft all opposed it before it shipped. Sets a precedent of a browser vendor bundling a proprietary model as a “web standard.” *(Alpha Signal)*

9. **CrewAI v1.14 ships checkpointing for long-running agent flows** — Every flow method becomes a recovery point; resume or fork from any saved state in one line with full lineage tracking. Prevents token-burning restarts on mid-run failures. *(Daily Dose of DS)*

10. **Cloudflare laying off 1,100+ as it rebuilds every role around AI agent sessions** — CEO posted that staff are running thousands of AI agent sessions daily and the company is restructuring all roles around this new mode of work. *(The Code)*

---

## 🤖 AI Models & Releases

- **GPT-Realtime-2** (OpenAI) — Voice AI with GPT-5-level reasoning; thinks while talking; multi-tool use simultaneously. 96.6% on Big Bench Audio. Companion models: GPT-Realtime-Translate (70+ languages), GPT-Realtime-Whisper (streaming transcription).
- **Zyphra 8B reasoning model** (Zyphra) — Open-source; claimed to rival DeepSeek and GPT-5 at 8B scale. *(Alpha Signal)*
- **Qwen 3.6** (Alibaba/Qwen) — Ships with multi-token prediction for faster speculative decoding. *(Alpha Signal)*
- **Xiaomi MiMo** — 6-bit MLX quantised build for Apple Silicon. *(Alpha Signal)*
- **World models / AMI Labs** (Yann LeCun) — $1.03B raised in March for AI that learns by predicting physical world consequences. Key bottleneck: action-labelled video data (“data friction”). *(The Code)*

---

## 🛠️ Tools & Products

- **Cursor v3.3** — End-to-end PR reviews inside editor; “Build in Parallel” uses async subagents; auto-splits large diffs into smaller PRs.
- **Prime Intellect Lab** — Open RL training platform; fine-tune 14 models (Nvidia/OpenAI/Meta/Qwen); pay-as-you-go; 10,000+ jobs in beta.
- **OpenAgents by Vercel** (5.2k ⭐) — Open-source cloud agent template: web UI, sandbox orchestration, GitHub integration.
- **Raindrop.ai** — Agent monitoring platform; catches silent failures in production (“Sentry for AI agents”).
- **InsForge** (9k+ ⭐) — Agent-first Supabase alternative; full backend topology in ~500 tokens; self-hostable via Docker. [GitHub](https://github.com/InsForge/InsForge)
- **Hermes Agent + HeyGen HyperFrames** (Nous Research) — AI agent builds HTML-native videos from prompts; `hermes skills install hyperframes`.
- **PriorLabs tabular foundation model** (6.7k ⭐) — Open-source; learns tabular data without fine-tuning.
- **Perplexity Personal Computer** — Mac app for agentic control over local files via Comet browser; now available to all Mac users.
- **Spotify Personal Podcasts** — AI agents convert briefings/notes into personal podcasts inside Spotify.
- **Codex Auto-Review** (OpenAI) — Delegates approvals to a risk-vetting sub-agent; cuts user prompts ~200x. Enable: `approvals_reviewer = "auto_review"` in `~/.codex/config.toml`.
- **Vellum “Personal Intelligence” agents** — Customisable AI assistants that learn preferences and act on your computer across sessions; $25M raised.
- **Scale AI** — $500M Pentagon contract for military data analysis (5x from Sep 2025 $100M deal).

---

## 📄 Research Highlights

- **“Toward a native foundation model for multimodal agents”** (arxiv:2604.26752) — Framework treating vision as a native skill; combines visual perception + multitask RL; improves coding and complex GUI tasks. *Why it matters: agents that see and act rather than just read text.* *(The Code)*

- **World Models (LeCun / AMI Labs)** (arxiv:2603.19312) — AI learns physics and consequences by predicting outcomes of actions, not next tokens. Bottleneck: action-labelled video data scarce outside driving/gaming. *Why it matters: the architecture to watch for physical-world AI in 2026.* *(The Code)*

- **MCPMark V2 benchmark** — Smarter agents consume dramatically more tokens with poorly designed backends; solution is agent-first backend design exposing structured topology upfront. *Why it matters: token efficiency is a design problem, not just a model problem.* *(Daily Dose of DS)*

- **Modular memory paper** — Proposes brain-inspired modular memory architecture to solve catastrophic forgetting, enabling AI that continuously learns without degrading prior knowledge. *Why it matters: path toward AI agents that improve in production.* *(Alpha Signal)*

---

## 💡 Supply Chain / Enterprise AI Angle

1. **Claude in Microsoft 365 is a direct win for supply chain practitioners** — S&OP analysts, demand planners, and consultants work daily across Excel (models), PowerPoint (S&OP decks), Word (reports), and Outlook (stakeholder comms). Context persistence across apps eliminates re-briefing Claude between tools — a genuine workflow accelerator for weekly S&OP and monthly business review cycles.

2. **Cyclical feature encoding is essential for demand forecasting** — The DDODS primer on sine/cosine encoding of periodic features (hour, day-of-week, month, season) directly applies to demand planning models. Models that treat December and January as far apart (linear encoding) will misrepresent holiday/seasonal adjacency. Worth flagging as a best practice to clients.

3. **PriorLabs open-source tabular foundation model** — Supply chain data is overwhelmingly tabular (orders, inventory, SKUs, suppliers, lead times). A model that learns tabular structure without fine-tuning could dramatically reduce time-to-insight for rapid prototyping.

4. **InsForge’s agent-first backend design principle** — Supply chain AI agents operating on ERP/WMS/TMS backends face the same problem: ambiguous errors and expensive discovery calls. Exposing a structured context layer before agents begin is directly applicable to bespoke supply chain agent builds.

5. **Anthropic compute volatility context** — Consulting teams relying on Claude Code for supply chain data engineering should be aware of recent rate limit volatility. The Colossus deal should ease pressure, but monitor for disruptions.

---

## 🔗 Notable Links

1. [OpenAI GPT-Realtime-2 announcement](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)
2. [Anthropic Institute research agenda](https://www.anthropic.com/research/anthropic-institute-agenda)
3. [InsForge: agent-first backend (9k+ ⭐)](https://github.com/InsForge/InsForge)
4. [LeCun’s world models paper (arxiv:2603.19312)](https://arxiv.org/abs/2603.19312)
5. [OpenAgents by Vercel (5.2k ⭐)](https://github.com/vercel-labs/open-agents)

---

*Digest generated automatically on Friday, 8 May 2026. 5 newsletter brands / 6 emails received out of 8 expected daily sources. Missing: The Deep View, Unwind AI, TLDR.*
