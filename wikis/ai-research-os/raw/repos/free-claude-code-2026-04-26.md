---
status: processed
---
     1|---
     2|source: https://github.com/Alishahryar1/free-claude-code
     3|date: 2026-04-26
     4|type: repo
     5|tags: [claude-code, proxy, free-llm, nvidia-nim, openrouter, local-llm, mit]
     6|---
     7|
     8|# Free Claude Code (Alishahryar1/free-claude-code)
     9|
    10|**Repository:** [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)  
    11|**License:** MIT  
    12|**Stats:** 13.5k stars · 1.9k forks · 540 commits · 23 contributors · Python 3.14
    13|
    14|---
    15|
    16|## Overview
    17|
    18|A lightweight, drop-in proxy that routes Claude Code's Anthropic API calls to free or local LLM providers. **No Anthropic API key required.** Supports the Claude Code CLI, VSCode extension, and remote usage via Discord/Telegram bots.
    19|
    20|> "Set 2 env vars. No modifications to Claude Code CLI or VSCode extension needed."
    21|
    22|**Supported Providers:**
    23|- **NVIDIA NIM** — 40 req/min free tier
    24|- **OpenRouter** — hundreds of models (free & paid)
    25|- **DeepSeek** — direct Anthropic-compatible API
    26|- **LM Studio** — fully local
    27|- **llama.cpp** — local via `llama-server`
    28|- **Ollama** — fully local, native Anthropic Messages
    29|
    30|---
    31|
    32|## Key Features
    33|
    34|| Feature | Description |
    35||--------|-------------|
    36|| **Zero Cost** | 40 req/min on NVIDIA NIM; free models on OpenRouter; unlimited local inference |
    37|| **Drop-in Replacement** | Set `ANTHROPIC_BASE_URL` and optionally `ANTHROPIC_AUTH_TOKEN`; no code changes needed |
    38|| **Per-Model Routing** | Map Claude Opus / Sonnet / Haiku to different backends; mix providers freely |
    39|| **Thinking Tokens** | Parses `<think>` tags and `reasoning_content` into native Claude thinking blocks |
    40|| **Heuristic Tool Parser** | Auto-parses text-based tool calls into structured tool use |
    41|| **Request Optimization** | Intercepts 5 categories of trivial calls locally (quota probes, title generation, filepath extraction, etc.) |
    42|| **Smart Rate Limiting** | Rolling-window throttle + exponential 429 backoff + optional concurrency cap |
    43|| **Discord / Telegram Bot** | Remote autonomous coding with tree-based threading, session persistence, live progress streaming, and voice notes |
    44|| **Subagent Control** | Intercepts task tool to force `run_in_background=False` |
    45|| **Extensible** | Clean `BaseProvider` and `MessagingPlatform` ABCs |
    46|
    47|---
    48|
    49|## Architecture
    50|
    51|```
    52|┌─────────────────┐        ┌─────────────────────┐        ┌────────────────┐
    53|│  Claude Code    │───────┾│  Free Claude Code    │───────┾│  LLM Provider    │
    54|│  CLI / VSCode   │───────┼│  Proxy (:8082)       │───────┼│  NIM / OR / LMS  │
    55|└─────────────────┘        └─────────────────────┘        └────────────────┘
    56|   Anthropic API                                             Native Anthropic
    57|   format (SSE)                                             or OpenAI chat SSE
    58|```
    59|
    60|- Transparent proxy: standard Anthropic API requests are forwarded to the configured provider.
    61|- Per-model routing resolves Opus/Sonnet/Haiku to model-specific backends, with `MODEL` as fallback.
    62|- Claude-compatible probe routes exposed: `GET /v1/models`, `POST /v1/messages`, `POST /v1/messages/count_tokens`, plus `HEAD`/`OPTIONS`.
    63|
    64|---
    65|
    66|## Quick Start
    67|
    68|### 1. Prerequisites
    69|
    70|Get an API key for your chosen provider (local providers need no key):
    71|- **NVIDIA NIM:** [build.nvidia.com/settings/api-keys](https://build.nvidia.com/settings/api-keys)
    72|- **OpenRouter:** [openrouter.ai/keys](https://openrouter.ai/keys)
    73|- **DeepSeek:** [platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)
    74|- **LM Studio / llama.cpp / Ollama:** run locally
    75|
    76|Install [Claude Code](https://github.com/anthropics/claude-code).
    77|
    78|### 2. Install `uv`
    79|
    80|```bash
    81|# macOS / Linux
    82|curl -LsSf https://astral.sh/uv/install.sh | sh
    83|uv self update
    84|uv python install 3.14   # Project requires Python 3.14
    85|
    86|# Windows (PowerShell)
    87|powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    88|```
    89|
    90|### 3. Clone & Configure
    91|
    92|```bash
    93|git clone https://github.com/Alishahryar1/free-claude-code.git
    94|cd free-claude-code
    95|cp .env.example .env
    96|```
    97|
    98|### 4. Provider Configuration Examples
    99|
   100|**NVIDIA NIM (recommended — 40 req/min free)**
   101|```env
   102|NVIDIA_NIM_API_KEY="nvapi-...here"
   103|
   104|MODEL_OPUS=
   105|MODEL_SONNET=
   106|MODEL_HAIKU=
   107|MODEL="nvidia_nim/z-ai/glm4.7"
   108|
   109|ENABLE_MODEL_THINKING=true
   110|```
   111|
   112|**OpenRouter**
   113|```env
   114|OPENROUTER_API_KEY="***"
   115|
   116|MODEL_OPUS="open_router/deepseek/deepseek-r1-0528:free"
   117|MODEL_SONNET="open_router/openai/gpt-oss-120b:free"
   118|MODEL_HAIKU="open_router/stepfun/step-3.5-flash:free"
   119|MODEL="open_router/stepfun/step-3.5-flash:free"
   120|```
   121|
   122|**DeepSeek**
   123|```env
   124|DEEPSEEK_API_KEY="your-d...here"
   125|
   126|MODEL_OPUS="deepseek/deepseek-reasoner"
   127|MODEL_SONNET="deepseek/deepseek-chat"
   128|MODEL_HAIKU="deepseek/deepseek-chat"
   129|MODEL="deepseek/deepseek-chat"
   130|```
   131|
   132|**LM Studio (local)**
   133|```env
   134|MODEL_OPUS="lmstudio/unsloth/MiniMax-M2.5-GGUF"
   135|MODEL_SONNET="lmstudio/unsloth/Qwen3.5-35B-A3B-GGUF"
   136|MODEL_HAIKU="lmstudio/unsloth/GLM-4.7-Flash-GGUF"
   137|MODEL="lmstudio/unsloth/GLM-4.7-Flash-GGUF"
   138|```
   139|
   140|**llama.cpp (local)**
   141|```env
   142|LLAMACPP_BASE_URL="http://localhost:8080/v1"
   143|MODEL_OPUS="llamacpp/local-model"
   144|MODEL_SONNET="llamacpp/local-model"
   145|MODEL_HAIKU="llamacpp/local-model"
   146|MODEL="llamacpp/local-model"
   147|```
   148|
   149|**Ollama (local)**
   150|```env
   151|OLLAMA_BASE_URL="http://localhost:11434"
   152|MODEL_OPUS="ollama/qwen3:32b"
   153|MODEL_SONNET="ollama/qwen3:32b"
   154|MODEL_HAIKU="ollama/qwen3:32b"
   155|MODEL="ollama/qwen3:32b"
   156|```
   157|
   158|### 5. Run the Proxy
   159|
   160|```bash
   161|uv run src/main.py
   162|# Server starts on :8082 by default
   163|```
   164|
   165|### 6. Point Claude Code at the Proxy
   166|
   167|```bash
   168|export ANTHROPIC_BASE_URL="http://localhost:8082"
   169|# Optional: export ANTHROPIC_AUTH_TOKEN="***"
   170|claude
   171|```
   172|
   173|For **VSCode extension**, set the same env vars before launching VSCode, or configure in extension settings.
   174|
   175|---
   176|
   177|## Discord / Telegram Bot Usage
   178|
   179|Run the bot:
   180|```bash
   181|uv run src/bot/main.py
   182|```
   183|
   184|Features:
   185|- **Tree-based threading** — conversations branch naturally
   186|- **Session persistence** — resume coding sessions across restarts
   187|- **Live progress streaming** — watch agent work in real-time
   188|- **Voice notes** — send audio instructions
   189|
   190|---
   191|
   192|## Why It Matters
   193|
   194|This proxy democratizes access to Claude Code — one of the most powerful agentic coding tools — by removing the Anthropic API cost barrier. With 40 req/min free on NVIDIA NIM or free models on OpenRouter, developers can use Claude Code's workflow (planning, implementation, testing, review) with zero or near-zero cost.
   195|
   196|The per-model routing also enables mixing providers: plan with a reasoning model (DeepSeek R1), implement with a fast model (GLM-4.7), review with a cheap model — all through the same Claude Code interface.
   197|