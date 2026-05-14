---
source: newsletter-digest
date: 2026-05-14
type: newsletter
tags: [digest, ai, the-rundown, the-code, superhuman, alpha-signal, daily-dose-of-ds]
status: pending
---

# Newsletter Digest — Thursday, 14 May 2026

## 🗞️ Sources Today

**Found (5 of 8 expected daily newsletters):**
- **The Rundown AI** — Daily edition ("OpenAI's Anthropic enterprise problem is growing") + Robotics edition ("Meet Unitree's giant new mech")
- **The Code** (by Superhuman) — "Anthropic faces developer backlash"
- **Superhuman** (by Zain Khan) — "Anthropic ships Claude for small biz & legal"
- **Alpha Signal** — "RuView WiFi Tracking, Anthropic Legal Drafts, Nous 2.5x Training"
- **Daily Dose of Data Science** — "Claude Code's /goal Command"

**Not received today:**
- ❌ The Deep View
- ❌ Unwind AI
- ❌ TLDR

*Sunday-only newsletters (LLM Watch, DAIR.AI, Causal Python) not searched — today is Thursday.*

---

## 🔑 Top Insights

- **Anthropic overtook OpenAI in paid enterprise adoption for the first time.** Ramp's May 2026 AI Index (tracking 50K+ U.S. businesses) shows Anthropic at 34.4% vs OpenAI's 32.3% — a 4x year-over-year surge. Claude Code drove expansion from tech teams into finance, legal, and research workflows. *(The Rundown AI, Superhuman)*
- **Anthropic billing overhaul triggers developer backlash.** Starting June 15, Agent SDK calls, GitHub Actions, and third-party integrations will draw from a new monthly credit pool charged at full API rates — separate from chat/Claude Code. Pro users: $20/month; Max (20x): $200. Several devs publicly announced shifting heavier workloads to OpenAI. *(The Code, Alpha Signal)*
- **AI lab FDE war: every major lab now deploying Forward-Deployed Engineers.** Anthropic ($1.5B venture with Blackstone/Goldman), OpenAI (new Deployment Company), and Google (hundreds of hires) are all placing engineers on-site at enterprises — replicating Palantir's playbook that yielded 640% returns from 2022 lows. *(The Code)*
- **Nous Research cut LLM pretraining time by 2.5x without changing model architecture** — a training data/scheduling trick, not a model change. Alpha Signal calls efficiency "the new moat." DeepSeek reportedly uses 27x less energy than Western AI and runs locally. *(Alpha Signal)*
- **Claude Code /goal command removes the human bottleneck in long agentic sessions.** Define a measurable end-state once; a Haiku evaluator checks the transcript each turn and keeps Claude running until the condition is met. Best paired with auto mode, CLAUDE.md context, and PostToolUse hooks. Avoid vague conditions — needs verifiable, observable output. *(Daily Dose of DS)*
- **Anthropic shipped 27 pre-built agentic workflows for SMBs and legal professionals.** Claude for Small Business: 15 workflows (QuickBooks, PayPal, DocuSign). Claude for Legal: 12 one-click workflows. Open-source `claude-for-legal` covers 10+ practice areas with 3.3K GitHub stars. *(Superhuman, Alpha Signal)*
- **Nvidia hit $5.5T market cap — first company ever.** Jensen Huang in China joining Trump-Xi meetings. David Silver's Ineffable Intelligence ($1.1B seed, $5.1B valuation) announced an engineering partnership with Nvidia for RL training pipelines. *(The Rundown AI, Superhuman)*
- **Cursor shipped cloud dev environments:** agents work across multiple repos simultaneously, trace Slack-reported issues to affected repos and open PRs. 70% faster cached builds, Dockerfile configs, audit logs. *(The Code)*

---

## 🤖 AI Models & Releases

| Model / System | By | What's Notable |
|---|---|---|
| **Claude for Small Business** | Anthropic | 15 ready-to-run agentic workflows; integrations with QuickBooks, PayPal, DocuSign |
| **Claude for Legal / claude-for-legal** | Anthropic | 12 one-click legal workflows + free open-source plugin suite covering 10+ practice areas |
| **AutoScientist** | Adaption (Sara Hooker) | Auto-customizes AI models; 35% over expert-tuned baselines; 48%→64% success rate across 8 industries |
| **Higgsfield Supercomputer** | Higgsfield | Chat-based creative pipeline; plain-language brief → rendered image/video without tool-hopping |
| **Lna-Lab 3-bit quantization** | Lna-Lab | 744B MoE model squeezed to 347GB with dynamic 3-bit quantization |
| **Ineffable Intelligence + Nvidia** | David Silver / Nvidia | RL-based AI systems; $1.1B seed at $5.1B valuation; Nvidia engineering partnership for Vera Rubin pipelines |

---

## 🛠️ Tools & Products

- **RuView** — Open-source WiFi-based through-wall human radar. ESP32-S3 boards (~$9), runs fully locally. Detects presence, 17-point body skeleton, heart rate, breathing. 50K+ GitHub stars.
- **Cursor Cloud Dev Environments** — Multi-repo agent orchestration. Slack → code → PR pipeline. Dockerfile configs, audit logs, 70% faster cached builds.
- **Notion Developer Platform** — Workers (secure sandbox code execution), live data sync from any API, native Claude Code/Cursor/Codex integration. Free through August on Business/Enterprise plans.
- **Alexa for Shopping** — Amazon absorbed Rufus (300M+ 2025 users). Price tracking, Auto-Buy, Buy for Me for non-Amazon stores, Scheduled Actions for auto-restocking.
- **Kilo Code** — Open-source AI coding agent across VS Code, JetBrains, and CLI with agentic workflows.
- **Plannotator (5.3K ⭐)** — Annotate agent plans before execution; built-in diff viewer for AI-generated code; collaborative team feedback to agent.
- **claude-for-legal** — Free, open-source. Covers contracts, NDAs, patent charts, DSAR responses. Connects to Slack, DocuSign, Ironclad, court dockets. 60-second setup.

---

## 📄 Research Highlights

- **HARP Actuators** (Arizona State University, PNAS) — Air-powered artificial muscles that lift 100x their weight and achieve 75% contraction ratio. Potential step-change for humanoid robot limb design.
- **Liquid-Crystal-Elastomer Artificial Muscles** (Seoul National University) — Embedded liquid-metal channels provide simultaneous actuation + force/length sensing. Demoed in robotic finger and gripper.
- **Nous Research 2.5x LLM pretraining speedup** — Training data/scheduling trick cuts pretraining time 2.5x without touching model code. Confirms efficiency-first thesis.
- **UK AI Safety Institute: AI cyber capability doubling every few months** — Mythos Preview and GPT-5.5 completed simulated cyber breaches. Signals increasing regulatory scrutiny.
- **NGINX 18-year RCE discovered by AI** — AI tooling surfaced a critical remote code execution vulnerability that survived 18 years of human review.
- **kNN for Imbalanced Datasets** (Daily Dose of DS) — Distance-weighted kNN and dynamic k-adjustment both address minority class dominance. Dynamic approach reduces k per-instance when minority class appears in top-k neighbors.

---

## 💡 Supply Chain / Enterprise AI Angle

- **AutoScientist (Adaption)** — Automated model customization tested across 8 industries including finance. Applicable to domain-specific demand forecasting or inventory models without deep in-house ML expertise. 35% lift over expert-tuned models.
- **Forward-Deployed Engineers** — The FDE model (Anthropic/OpenAI/Google all racing to adopt) mirrors supply chain consulting engagement patterns: months of on-site integration, deep system access, sticky infrastructure. Critical positioning context for enterprise AI consulting.
- **claude-for-legal** — Contract review, NDA analysis, renewal deadline monitoring. Immediately applicable to procurement contract management and vendor agreement workflows.
- **Claude for Small Business (QuickBooks/DocuSign/PayPal)** — Invoice, payroll, and contract workflows directly address mid-market supply chain operator pain points.
- **Alexa for Shopping / Buy for Me** — Amazon's autonomous purchasing layer (Auto-Buy, Scheduled Actions) is an early signal of AI-driven procurement agents for B2C-adjacent use cases.
- **Mind Robotics $400M raise** (Rivian CEO RJ Scaringe, $3.4B valuation) — Vertically integrated AI + custom hardware + factory data learning stack. Directly relevant to warehouse and manufacturing automation.

---

## 🔗 Notable Links

1. [Ramp AI Index May 2026 — Anthropic takes enterprise lead from OpenAI](https://ramp.com/leading-indicators/ai-index-may-2026)
2. [Anthropic Agent SDK billing changes effective June 15](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)
3. [AutoScientist by Adaption Labs](https://www.adaptionlabs.ai/blog/autoscientist)
4. [Claude for Small Business](https://claude.com/solutions/small-business)
5. [Cursor Cloud Agent Development Environments](https://cursor.com/blog/cloud-agent-development-environments)

---

*Digest generated automatically on Thursday, 14 May 2026. 5 newsletter brands / 5 emails received out of 8 expected daily sources. Missing: The Deep View, Unwind AI, TLDR.*
