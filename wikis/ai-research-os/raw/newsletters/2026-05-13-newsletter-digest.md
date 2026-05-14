---
source: newsletter-digest
date: 2026-05-13
type: newsletter
tags: [digest, ai, the-rundown, superhuman, the-code, alpha-signal, daily-dose-of-ds]
status: processed
---

# Newsletter Digest — Wednesday, 13 May 2026

> Digest generated automatically on Wednesday, 13 May 2026. 5 of 8 expected daily newsletters received.

---

## 🗞️ Sources Today

| Newsletter | Status | Subject |
|---|---|---|
| The Rundown AI | ✅ Received | Android enters its Gemini Intelligence era |
| The Code | ✅ Received | Supply chain attacks keep hitting AI |
| Superhuman | ✅ Received | Google's Macbook competitor |
| Alpha Signal | ✅ Received | Thinking Machines TML-Small 64.7%, MIT Brain Study, Rust Browser |
| Daily Dose of Data Science | ✅ Received | Hermes Agent Masterclass |
| The Deep View | ❌ Not received | — |
| Unwind AI | ❌ Not received | — |
| TLDR | ❌ Not received | — |

Sunday-only newsletters (LLM Watch, DAIR.AI, Causal Python) not searched — today is Tuesday.

---

## 🔑 Top Insights

1. **Google unveils Googlebook at Android Show** — AI-native laptops with Gemini Intelligence and a "Magic Pointer" AI cursor ship this fall, built with Dell, HP, Lenovo, Acer, Asus. Runs Android apps + ChromeOS + Gemini in one unified ecosystem. Pre-I/O appetizer before next week's main event. *(Rundown AI, Superhuman)*

2. **Thinking Machines releases TML-Interaction-Small** — 276B-parameter real-time model that listens, speaks, and processes video simultaneously in 200ms chunks. Scores 64.7% on timed speech tasks vs. 4.3% for GPT-Realtime-2. Closes the gap between natural human conversation and AI interaction. *(Alpha Signal)*

3. **MIT study reveals "cognitive debt" from AI writing tools** — 54 participants, EEG scans over 4 months. LLM users showed up to 55% reduced brain connectivity vs. brain-only writers. 83% of LLM users couldn't quote essays they just wrote. Key recommendation: use AI as a finishing tool, not a starting one. *(Alpha Signal)*

4. **Claude Code gets /goal command** — Set a target (e.g., "pass all tests in folder"), and the agent works autonomously until an evaluator model confirms the goal has been met. Fast mode for Opus 4.7 also launched in research preview via API and Claude Code. *(The Code)*

5. **Hermes Agent crosses 90K GitHub stars in 2 months** — Architecturally distinct from OpenClaw: SOUL.md identity layer, 3-tier memory (hot Markdown + SQLite full-text + 8 external plugins), self-evolving skills, and GEPA offline optimization pipeline. Framing: "Hermes packages a gateway around a learning agent; OpenClaw packages an agent around a messaging gateway." *(Daily Dose of DS, The Code)*

6. **Amazon's AI tokenmaxxing scoreboard creates perverse incentives** — Internal goal of 80%+ weekly AI use led employees to game the MeshClaw agent by burning unnecessary tokens to raise their scores. Lesson: measuring usage instead of outcomes only produces scoreboard optimization, not better work. *(Rundown AI)*

7. **Google catches first confirmed AI-built zero-day exploit** — Attackers used an AI model to find a 2FA bypass in a popular open-source admin tool, then began prepping for mass attack. Google flagged it before anyone was hit. *(The Code)*

8. **AI supply chain attacks escalating** — Microsoft flagged malware in a Python package disguised as Hugging Face Transformers (credential theft). Separately, 'Mini Shai-Hulud' data-stealing code planted in 42 agentic npm packages. *(Rundown AI, The Code)*

9. **Google + SpaceX exploring orbital data centers** — Google holds 6.1% of SpaceX; talks underway for orbital compute launch. Anthropic finalized its own SpaceX deal last week. Sam Altman called the concept "ridiculous for this decade" — but both Google and Musk have track records that make betting against them risky. *(Rundown AI, Superhuman)*

10. **Claude Opus 4.7 tops Arena LLM leaderboard** — Named "most consistently dominant model" across nearly every category. Gemini 3.1 Pro second (edge in creative writing), Meta Spark leads coding, GPT-5.5 strong in math, Grok 4.20 for creative writing. *(Superhuman)*

---

## 🤖 AI Models & Releases

- **Thinking Machines TML-Interaction-Small** — 276B params; simultaneous audio input/output + video in 200ms chunks; interaction layer (live conversation) + background layer (search, reasoning, tools); 64.7% timed speech vs. 4.3% for GPT-Realtime-2
- **Claude Opus 4.7 fast mode** — Research preview; faster output without model downgrade, available via API and Claude Code
- **Krea 2 (K2)** — First in-house image model from Krea; built for aesthetic diversity and stylistic control; moodboard feature blends style across reference images *(Rundown AI, Superhuman)*
- **Sulphur 2** — Open-source uncensored video model (Lightricks LTX base); runs locally; 10-second 24fps clips; requires 16GB VRAM; trained on 125K+ videos *(Alpha Signal)*
- **Step Image Edit 2** — StepFun's lightweight image editing model *(Rundown AI)*
- **GPT-Realtime-2** — Voice AI with tool-calling capability and live conversation flow *(Rundown AI)*

---

## 🛠️ Tools & Products

- **Googlebook** — Google's Gemini-native laptop line (ships fall 2026); Magic Pointer AI cursor; Android app support; built with Dell/HP/Lenovo/Acer/Asus
- **Claude Code /goal command** — Autonomous goal completion loop; evaluator model confirms when done
- **Hermes Agent** (Nous Research) — Persistent 24/7 AI agent; SOUL.md + 3-tier memory + self-evolving skills + GEPA offline optimization; 90K GitHub stars
- **Prime Intellect renderers** — Open-source Python library fixing token-to-message translation overhead in agent training; 3x+ throughput boost
- **oMLX** — High-performance Apple Silicon server for multiple local LLMs/vision models via menu bar, web dashboard, or OpenAI-compatible API
- **Claude Code /handoff skill** (mattpocock) — Compresses active session context to Markdown; next session picks up full context; install via `npx skills@latest add mattpocock/skills`
- **Warp** — Modern terminal with AI agents for build/test/deploy/debug workflows

---

## 📄 Research Highlights

- **MIT "Cognitive Debt" Study** — EEG study, 54 participants, 3 groups (brain-only, search engine, LLM), 4 months. LLM users: up to 55% reduced neural connectivity; 83% couldn't quote own AI-written essays. Coined "cognitive debt" as long-term cost of outsourced thinking. Recommendation: delay AI integration until learners have engaged in sufficient self-driven cognitive effort first.
- **Prime Intellect renderers** — Agent training typically processes data as tokens but environments use messages; swapping between the two degrades data and wastes compute; renderers handles the translation cleanly with 3x+ throughput on open-source models.
- **Meta FAIR byte-level model** — Cuts LLM decoding steps in half. *(Alpha Signal)*
- **Kaiming He's continuous text diffusion model** — Generates text in continuous embedding space rather than discrete tokens, potentially enabling new generation paradigms. *(Alpha Signal)*

---

## 💡 Supply Chain / Enterprise AI Angle

- **Amazon tokenmaxxing is a direct cautionary tale for enterprise AI rollouts**: Any supply chain transformation that measures AI adoption via usage metrics (tokens, sessions, clicks) rather than outcomes (forecast accuracy, cycle time, decision quality) will reproduce Amazon's scoreboard-gaming problem. Define outcome KPIs before deploying AI adoption dashboards.
- **AI supply chain attacks targeting developer toolchains are now confirmed and escalating** — Hugging Face Transformers impersonation, 42 compromised agentic npm packages. Any enterprise using open-source ML pipelines in forecasting or supply chain AI stacks should audit PyPI/npm dependencies and pin package versions.
- **Claude Code's /goal command** directly applies to agentic S&OP and demand planning workflows: set a verifiable goal (e.g., "validate all demand plan outputs against inventory constraints") and have an agent loop until an evaluator confirms completion. This is exactly the pattern needed for autonomous supply chain workflows.
- **Hermes Agent's GEPA offline skill optimization** ($2–10/run, no GPU, no fine-tuning) is compelling for enterprise teams building persistent procurement or demand planning agents who need to optimize agent behavior without RL infrastructure.

---

## 🔗 Notable Links

1. [Google Googlebook & Gemini Intelligence announcement](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/)
2. [Google + SpaceX orbital data centers (WSJ)](https://www.wsj.com/tech/spacex-google-in-talks-to-explore-data-centers-in-orbit-7b7799e2)
3. [Prime Intellect renderers — 3x agent training throughput fix](https://www.primeintellect.ai/blog/renderers)
4. [Google's first AI-built zero-day exploit (Google Cloud blog)](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)
5. [Matt Pocock's /handoff skill for Claude Code (GitHub)](https://github.com/mattpocock/skills)
