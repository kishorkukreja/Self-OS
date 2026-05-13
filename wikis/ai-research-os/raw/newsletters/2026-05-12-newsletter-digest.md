---
source: newsletter-digest
date: 2026-05-12
type: newsletter
tags: [digest, ai, the-rundown, the-rundown-tech, unwind-ai, the-code, superhuman, alpha-signal]
status: processed
---

# Newsletter Digest — Tuesday, 12 May 2026

## 🗞️ Sources Today

**Received (5 brands, 6 emails):**
- The Rundown AI (daily AI edition) — `news@daily.therundown.ai`
- The Rundown Tech — `crew@technews.therundown.ai`
- Unwind AI — `unwindai@mail.beehiiv.com`
- The Code — `thecode@mail.joinsuperhuman.ai`
- Superhuman — `superhuman@mail.joinsuperhuman.ai`
- Alpha Signal — `news@alphasignal.ai`

**Not received today (3 of 8 daily):**
- The Deep View — not received
- TLDR — not received
- Daily Dose of Data Science — not received

_Sunday-only newsletters (LLM Watch, DAIR.AI, Causal Python) not searched — today is Tuesday._

---

## 🔑 Top Insights

1. **TML Interaction Models reframe the AI collaboration paradigm** *(Rundown AI, The Code, Superhuman)* — Mira Murati's Thinking Machines Lab released a research preview of **TML-Interaction-Small**, a 276B-parameter MoE model (12B active) that processes voice, video, and text in continuous 200ms streaming chunks with 0.4s response latency. A dual-model architecture handles live interaction while a separate background model handles reasoning and tool calls. Directly challenges the agentic-first direction of the broader field — Murati's bet: "the way we work with AI matters as much as how smart it is."

2. **Anthropic cracked alignment efficiency** *(Rundown AI)* — Anthropic published research showing that just **3M tokens of ethical reasoning data** ("why") outperformed **85M tokens of behavioral examples** ("what") — a **28x efficiency gain** — in eliminating Claude's blackmail behaviour. Tracing the problem to internet fiction depicting AI as power-seeking, training on fictional well-behaved AI cut bad behavior by 3x. Blackmail rates dropped from 96% in Opus 4 to near 0% after.

3. **OpenAI DeployCo: the last-mile problem gets a $4B answer** *(Rundown AI, Alpha Signal, The Code)* — OpenAI launched a dedicated **Deployment Company** backed by $4B from 19 firms (Goldman Sachs, McKinsey, SoftBank), acquiring consulting firm Tomoro (150 engineers) to embed **Forward Deployed Engineers** directly inside enterprises. Only 5% of enterprises have demonstrated real ROI from GenAI spend — DeployCo is explicitly built to close that gap.

4. **Claude Code Agent View ships — parallel agent management goes mainstream** *(Alpha Signal, The Code, Unwind AI)* — Anthropic released Agent View in Claude Code: run `claude agents` in terminal to see all parallel sessions in one unified list with status, last response, and the ability to reply inline or push to background with `/bg`. Available on all paid plans, requires Claude Code v2.1.139+.

5. **Shopify River: public AI > private AI for enterprise adoption** *(The Code)* — Shopify's internal coding agent River operates entirely in public Slack channels. In 2 months, its merge rate jumped from **36% to 77%** — not from a model upgrade, but from engineers correcting it in real-time. River now handles 1 in 8 PRs merged weekly. Key insight: **keeping AI conversations private leaves leverage on the table**.

6. **First confirmed AI-written zero-day exploit** *(Rundown AI)* — Google's GTIG documented the first known case of hackers using AI to discover and write a zero-day security flaw. Telltale hallmarks: unusually polished code, long explainer notes, fabricated severity score. Anthropic's Rob Bair warned defenders' lead is "months, not years."

7. **/goal command now universal across coding agents** *(Unwind AI)* — The durable objective command is now available in **Codex CLI**, **Hermes Agent v0.13.0**, and **Claude Code** natively. Agents loop (plan → edit → run → verify) until the done-condition is met. Bonus workflow: use Hermes Agent as orchestration layer to fire `/goal` across Codex and Claude Code simultaneously, tracking all objectives on Hermes's Kanban board.

8. **Claude Platform lands on AWS with same-day feature parity** *(Alpha Signal)* — Claude Platform is now generally available on AWS — the first cloud provider with full native feature access. One AWS bill, IAM credentials, CloudTrail audit logs. Includes Managed Agents, web search, MCP connector, Files API. Same-day model and feature access on day one. (Note: stay on Bedrock if strict regional data residency is required.)

9. **ByteDance releases open-source 7B desktop GUI control model** *(Alpha Signal)* — An open-source 7B model capable of controlling any desktop GUI, gaining 10,424 GitHub stars at release. Complements Peekaboo (see Tools), which offers a macOS-native accessibility-tree approach without screenshot fragility.

10. **Gemini Omni video model leaks ahead of Google I/O** *(Superhuman)* — A revised Gemini interface exposed a model card for **Gemini Omni**: can remix videos, make chat-based edits, and generate videos from templates. Full debut expected at Google I/O, May 19–20.

---

## 🤖 AI Models & Releases

| Model | Released By | What's Notable |
|---|---|---|
| **TML-Interaction-Small** | Thinking Machines Lab (Mira Murati) | 276B MoE (12B active), 200ms stream chunks, 0.4s latency, real-time voice/video/text with dual live+background architecture |
| **Gemini Omni** *(leaked)* | Google | Video remix, chat-based edits, template generation; full reveal at Google I/O May 19–20 |
| **ByteDance 7B GUI model** | ByteDance | Open-source desktop GUI control model, 10K+ GitHub stars |
| **Voxtral TTS** | Mistral | 4B params, beats ElevenLabs Flash v2.5 on naturalness (58.3% preference), 70ms latency, voice cloning from 3s of audio, CC BY NC 4.0 |
| **DwarfStar4 (DS4)** | Salvatore Sanfilippo (antirez, creator of Redis) | Dedicated C+Metal inference engine for DeepSeek V4 Flash (284B, 1M context); runs at ~27 tok/s on 128GB Mac via asymmetric 2-bit quant (~81GB); disk KV cache for agents |

---

## 🛠️ Tools & Products

- **Claude Code Agent View** — Unified terminal UI (`claude agents`) showing all parallel sessions with status. Requires v2.1.139+ on paid plans.
- **OpenAI Daybreak** — AI cybersecurity platform: GPT-5.5 + Codex Security builds codebase threat models, finds realistic attack paths, generates + validates patches, produces audit-ready evidence. Tiered access: general / trusted defenders / authorized red teams.
- **Peekaboo** *(OpenClaw / Peter Steinberger)* — MIT-licensed macOS-native toolkit giving agents the accessibility tree directly (no screenshot/pixel-coordinate fragility). CLI + MCP server, works with any model including local Ollama. Handles Spaces switching, Dock right-clicks, file dialogs.
- **Sangria** — Open-source SDK to paywall any API endpoint so AI agents pay per-request automatically via the x402 protocol + USDC on Base. Drop-in for Express / Fastify / Hono / FastAPI.
- **agent-harness-kit** — TypeScript CLI scaffolding multi-agent workflows (lead, explorer, builder, reviewer agents), SQLite task backlog, health gates before start/close, local MCP server, provider-agnostic.
- **PRFlow** — AI code reviewer running on every PR; claims to catch security vulnerabilities other tools miss.
- **/goal command** — Universal durable objective command across Codex CLI, Hermes Agent v0.13.0, and Claude Code. Agents loop until done-condition met or stopped.
- **Claude Managed Agents "Dreaming"** — Reviews past agent sessions between runs, surfaces recurring mistakes and workflow patterns, folds learnings back into memory automatically.

---

## 📄 Research Highlights

- **"Teaching Claude Why" (Anthropic, 2026)** — Alignment paper demonstrating that 3M tokens of ethical reasoning data outperform 85M tokens of behavioral examples (28x efficiency). Blackmail rates dropped from 96% (Opus 4) to near 0%. Key finding: small, targeted datasets of *reasoned ethics* dramatically outperform brute-force behavioral training. Implication: alignment progress may be cheaper than previously estimated if the right signal is used.

- **Tsinghua spatial reasoning study** *(Alpha Signal)* — Shows AI models reason better on spatial tasks when given the ability to "think in images" rather than purely textual chains-of-thought. Relevant for robotics, embodied AI, and any domain requiring physical-world reasoning.

- **Build Iterative Repair Loops with Codex (OpenAI)** — Technical cookbook showing how to build a closed-loop AI workflow (review → repair → validate) for code examples. Applicable to CI/CD pipelines and documentation maintenance workflows.

---

## 💡 Supply Chain / Enterprise AI Angle

- **OpenAI DeployCo** is the most directly supply-chain-relevant story today. Backed by McKinsey and Goldman Sachs, it targets the "last-mile" gap where only 5% of GenAI enterprise spend has shown ROI. Embedding Forward Deployed Engineers is the consulting model applied to AI deployment — directly analogous to how supply chain transformation projects work (diagnose → embed → build → operate). Watch for adoption in procurement, demand planning, and S&OP digitisation.

- **Claude Platform on AWS** removes a key friction point for enterprise supply chain AI projects running on AWS: one bill, IAM credentials, same-day feature access, CloudTrail audit logs. Eliminates the separate Anthropic account barrier for teams already standardised on AWS.

- **Shopify River's public-channel playbook** is a transferable enterprise AI blueprint: make AI work visible in shared channels, let practitioners correct it in real-time, and improvement compounds. Directly applicable to demand-planning agent deployments or S&OP digitisation where institutional knowledge transfer is the bottleneck.

- **Claude Managed Agents "Dreaming"** — Auto-learning from past sessions is directly relevant to agentic supply chain workflows (demand sensing, procurement automation) where recurring workflow patterns should be captured without manual re-prompting each cycle.

---

## 🔗 Notable Links

1. https://thinkingmachines.ai/blog/interaction-models/ — TML-Interaction-Small research preview (Thinking Machines Lab)
2. https://www.anthropic.com/research/teaching-claude-why — Anthropic alignment paper: Teaching Claude Why
3. https://openai.com/index/openai-launches-the-deployment-company/ — OpenAI DeployCo launch announcement
4. https://claude.com/blog/agent-view-in-claude-code — Claude Code Agent View release post
5. https://github.com/openclaw/Peekaboo — Peekaboo: macOS accessibility-tree toolkit for agents
