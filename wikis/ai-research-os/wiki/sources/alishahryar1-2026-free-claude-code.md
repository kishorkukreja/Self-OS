---
title: "Free Claude Code — Drop-in Proxy for Free/Local LLMs"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Lightweight proxy routing Claude Code's Anthropic API calls to free or local LLM providers, removing the Anthropic API cost barrier."
tags: [claude-code, proxy, free-llm, nvidia-nim, openrouter, local-llm]
type: source
status: final
---

# Free Claude Code — Drop-in Proxy for Free/Local LLMs

**Type:** repo
**Date:** 2026-04-26
**URL:** https://github.com/Alishahryar1/free-claude-code
**Raw file:** [[../../raw/repos/free-claude-code-2026-04-26.md]]

**Summary:** Free Claude Code is a lightweight, drop-in proxy that routes Claude Code's Anthropic API calls to free or local LLM providers, eliminating the need for an Anthropic API key. It supports NVIDIA NIM (40 req/min free tier), OpenRouter, DeepSeek, LM Studio, llama.cpp, and Ollama. Key features include per-model routing (mapping Opus/Sonnet/Haiku to different backends), thinking token parsing, heuristic tool call parsing, request optimisation intercepting trivial calls locally, smart rate limiting, and Discord/Telegram bot integration for remote autonomous coding. The proxy exposes standard Anthropic-compatible endpoints and requires only two environment variables.

**Key contributions:**
- Zero-cost Claude Code usage via free-tier providers (NVIDIA NIM, OpenRouter free models)
- Per-model routing enabling mixed-provider strategies
- Thinking token parsing from <think> tags and reasoning_content
- Heuristic text-based tool parser for non-Anthropic models
- Request optimisation intercepting 5 categories of trivial calls locally
- Discord/Telegram bot with tree-based threading and session persistence

**Tags:** claude-code, proxy, free-llm, nvidia-nim, openrouter, local-llm, discord-bot
