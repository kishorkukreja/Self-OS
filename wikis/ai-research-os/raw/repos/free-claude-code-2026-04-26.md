---
source: https://github.com/Alishahryar1/free-claude-code
date: 2026-04-26
type: repo
tags: [claude-code, proxy, free-llm, nvidia-nim, openrouter, local-llm, mit]
---

# Free Claude Code (Alishahryar1/free-claude-code)

**Repository:** [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)  
**License:** MIT  
**Stats:** 13.5k stars · 1.9k forks · 540 commits · 23 contributors · Python 3.14

---

## Overview

A lightweight, drop-in proxy that routes Claude Code's Anthropic API calls to free or local LLM providers. **No Anthropic API key required.** Supports the Claude Code CLI, VSCode extension, and remote usage via Discord/Telegram bots.

> "Set 2 env vars. No modifications to Claude Code CLI or VSCode extension needed."

**Supported Providers:**
- **NVIDIA NIM** — 40 req/min free tier
- **OpenRouter** — hundreds of models (free & paid)
- **DeepSeek** — direct Anthropic-compatible API
- **LM Studio** — fully local
- **llama.cpp** — local via `llama-server`
- **Ollama** — fully local, native Anthropic Messages

---

## Key Features

| Feature | Description |
|--------|-------------|
| **Zero Cost** | 40 req/min on NVIDIA NIM; free models on OpenRouter; unlimited local inference |
| **Drop-in Replacement** | Set `ANTHROPIC_BASE_URL` and optionally `ANTHROPIC_AUTH_TOKEN`; no code changes needed |
| **Per-Model Routing** | Map Claude Opus / Sonnet / Haiku to different backends; mix providers freely |
| **Thinking Tokens** | Parses `<think>` tags and `reasoning_content` into native Claude thinking blocks |
| **Heuristic Tool Parser** | Auto-parses text-based tool calls into structured tool use |
| **Request Optimization** | Intercepts 5 categories of trivial calls locally (quota probes, title generation, filepath extraction, etc.) |
| **Smart Rate Limiting** | Rolling-window throttle + exponential 429 backoff + optional concurrency cap |
| **Discord / Telegram Bot** | Remote autonomous coding with tree-based threading, session persistence, live progress streaming, and voice notes |
| **Subagent Control** | Intercepts task tool to force `run_in_background=False` |
| **Extensible** | Clean `BaseProvider` and `MessagingPlatform` ABCs |

---

## Architecture

```
┌─────────────────┐        ┌─────────────────────┐        ┌────────────────┐
│  Claude Code    │───────┾│  Free Claude Code    │───────┾│  LLM Provider    │
│  CLI / VSCode   │───────┼│  Proxy (:8082)       │───────┼│  NIM / OR / LMS  │
└─────────────────┘        └─────────────────────┘        └────────────────┘
   Anthropic API                                             Native Anthropic
   format (SSE)                                             or OpenAI chat SSE
```

- Transparent proxy: standard Anthropic API requests are forwarded to the configured provider.
- Per-model routing resolves Opus/Sonnet/Haiku to model-specific backends, with `MODEL` as fallback.
- Claude-compatible probe routes exposed: `GET /v1/models`, `POST /v1/messages`, `POST /v1/messages/count_tokens`, plus `HEAD`/`OPTIONS`.

---

## Quick Start

### 1. Prerequisites

Get an API key for your chosen provider (local providers need no key):
- **NVIDIA NIM:** [build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys)
- **OpenRouter:** [openrouter.ai/keys](https://openrouter.ai/keys)
- **DeepSeek:** [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)
- **LM Studio / llama.cpp / Ollama:** run locally

Install [Claude Code](https://github.com/anthropics/claude-code).

### 2. Install `uv`

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
uv self update
uv python install 3.14   # Project requires Python 3.14

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Clone & Configure

```bash
git clone https://github.com/Alishahryar1/free-claude-code.git
cd free-claude-code
cp .env.example .env
```

### 4. Provider Configuration Examples

**NVIDIA NIM (recommended — 40 req/min free)**
```env
NVIDIA_NIM_API_KEY="nvapi-your-key-here"

MODEL_OPUS=
MODEL_SONNET=
MODEL_HAIKU=
MODEL="nvidia_nim/z-ai/glm4.7"

ENABLE_MODEL_THINKING=true
```

**OpenRouter**
```env
OPENROUTER_API_KEY="sk-or-your-key-here"

MODEL_OPUS="open_router/deepseek/deepseek-r1-0528:free"
MODEL_SONNET="open_router/openai/gpt-oss-120b:free"
MODEL_HAIKU="open_router/stepfun/step-3.5-flash:free"
MODEL="open_router/stepfun/step-3.5-flash:free"
```

**DeepSeek**
```env
DEEPSEEK_API_KEY="your-deepseek-key-here"

MODEL_OPUS="deepseek/deepseek-reasoner"
MODEL_SONNET="deepseek/deepseek-chat"
MODEL_HAIKU="deepseek/deepseek-chat"
MODEL="deepseek/deepseek-chat"
```

**LM Studio (local)**
```env
MODEL_OPUS="lmstudio/unsloth/MiniMax-M2.5-GGUF"
MODEL_SONNET="lmstudio/unsloth/Qwen3.5-35B-A3B-GGUF"
MODEL_HAIKU="lmstudio/unsloth/GLM-4.7-Flash-GGUF"
MODEL="lmstudio/unsloth/GLM-4.7-Flash-GGUF"
```

**llama.cpp (local)**
```env
LLAMACPP_BASE_URL="http://localhost:8080/v1"
MODEL_OPUS="llamacpp/local-model"
MODEL_SONNET="llamacpp/local-model"
MODEL_HAIKU="llamacpp/local-model"
MODEL="llamacpp/local-model"
```

**Ollama (local)**
```env
OLLAMA_BASE_URL="http://localhost:11434"
MODEL_OPUS="ollama/qwen3:32b"
MODEL_SONNET="ollama/qwen3:32b"
MODEL_HAIKU="ollama/qwen3:32b"
MODEL="ollama/qwen3:32b"
```

### 5. Run the Proxy

```bash
uv run src/main.py
# Server starts on :8082 by default
```

### 6. Point Claude Code at the Proxy

```bash
export ANTHROPIC_BASE_URL="http://localhost:8082"
# Optional: export ANTHROPIC_AUTH_TOKEN="anything"
claude
```

For **VSCode extension**, set the same env vars before launching VSCode, or configure in extension settings.

---

## Discord / Telegram Bot Usage

Run the bot:
```bash
uv run src/bot/main.py
```

Features:
- **Tree-based threading** — conversations branch naturally
- **Session persistence** — resume coding sessions across restarts
- **Live progress streaming** — watch agent work in real-time
- **Voice notes** — send audio instructions

---

## Why It Matters

This proxy democratizes access to Claude Code — one of the most powerful agentic coding tools — by removing the Anthropic API cost barrier. With 40 req/min free on NVIDIA NIM or free models on OpenRouter, developers can use Claude Code's workflow (planning, implementation, testing, review) with zero or near-zero cost.

The per-model routing also enables mixing providers: plan with a reasoning model (DeepSeek R1), implement with a fast model (GLM-4.7), review with a cheap model — all through the same Claude Code interface.
