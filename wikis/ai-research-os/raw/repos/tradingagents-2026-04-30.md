---
source: https://github.com/TauricResearch/TradingAgents
date: 2026-04-30
type: repo
tags: [tradingagents, tauric-research, multi-agent, finance, trading, stock-analysis, langgraph]
---

# TauricResearch/TradingAgents

## Summary
`TauricResearch/TradingAgents` is an open-source multi-agent LLM financial trading research framework. It simulates a trading firm with specialized LLM-powered agents for fundamentals, sentiment, news/macro, technical analysis, bull/bear research debate, trading decisions, risk management, and portfolio-management-style final decisions.

The repository is useful as a repeatable structure for stock-analysis workflows: rather than relying on one generic model answer, it decomposes analysis into analyst roles, adversarial debate, risk review, and a final five-tier decision view. It is explicitly designed for research and is not financial, investment, or trading advice.

## Key points
- Repository: https://github.com/TauricResearch/TradingAgents
- Paper: https://arxiv.org/abs/2412.20138
- License: Apache-2.0.
- Primary language: Python.
- Core stack: LangGraph, LangChain, yfinance, stockstats, pandas, Typer/Rich CLI.
- Agent roles include fundamentals analyst, sentiment analyst, news analyst, technical analyst, bull researcher, bear researcher, trader, risk manager, and portfolio manager.
- Latest extracted release: `v0.2.4` on 2026-04-25.
- v0.2.4 added structured-output decision agents, LangGraph checkpoint resume, persistent decision log, Docker support, Azure/DeepSeek/Qwen/GLM provider support, and a consistent five-tier rating scale.
- Supported LLM provider env vars include `OPENAI_API_KEY`, `GOOGLE_API_KEY`, `ANTHROPIC_API_KEY`, `XAI_API_KEY`, `DEEPSEEK_API_KEY`, `DASHSCOPE_API_KEY`, `ZHIPU_API_KEY`, and `OPENROUTER_API_KEY`.

## Why it matters
TradingAgents provides a good model for a reusable stock-analysis skill: analyst decomposition, structured bull/bear debate, risk review, and a portfolio-manager conclusion. It fits Self-OS skill-based workflows because its output can be standardized, timestamped, caveated, and made repeatable across tickers.

## Important disclaimer
TradingAgents is designed for research purposes. Trading performance depends on LLM choice, temperature, trading period, data quality, and other nondeterministic factors. Output should be treated as research/analysis, not as financial advice or a buy/sell instruction.

## Raw content
The repository README describes TradingAgents as a multi-agent trading framework that mirrors real-world trading firms. It deploys specialized LLM-powered agents, from fundamental analysts, sentiment experts, and technical analysts to traders, risk-management teams, and portfolio managers. These agents collaboratively evaluate market conditions and engage in dynamic discussions to identify a strategy.

The framework architecture includes an Analyst Team, Researcher Team, Trader Agent, Risk Management Team, and Portfolio Manager. The Analyst Team includes a Fundamentals Analyst that evaluates company financials and performance metrics, a Sentiment Analyst that analyzes social/public sentiment, a News Analyst that monitors global news and macroeconomic indicators, and a Technical Analyst that uses indicators such as MACD and RSI. The Researcher Team includes bullish and bearish researchers that debate analyst insights. The Trader Agent synthesizes the reports. The Risk Management Team evaluates portfolio risk, volatility, liquidity, and strategy exposure. The Portfolio Manager makes the final approve/reject style decision.

The changelog for v0.2.4 highlights structured-output decision agents for Research Manager, Trader, and Portfolio Manager via `llm.with_structured_output(Schema)`. Provider-native structured-output modes include OpenAI/xAI JSON schema, Gemini response schema, Anthropic tool-use, and OpenAI-compatible function calling. The release also added LangGraph checkpoint resume via `--checkpoint`, per-ticker SQLite checkpoint databases under `~/.tradingagents/cache/checkpoints/`, a persistent decision log replacing older per-agent BM25 memory, provider support for DeepSeek/Qwen/GLM/Azure OpenAI, Docker support, and a consistent five-tier rating scale: Buy / Overweight / Hold / Underweight / Sell. The Trader keeps a three-tier Buy/Hold/Sell direction.

The project can be installed by cloning the repository, creating a Python environment, and running `pip install .`. The `pyproject.toml` declares package version `0.2.4`, Python `>=3.10`, and dependencies including `langchain-core`, `langchain-anthropic`, `langchain-google-genai`, `langchain-openai`, `langgraph`, `langgraph-checkpoint-sqlite`, `pandas`, `requests`, `rich`, `typer`, `stockstats`, `tqdm`, and `yfinance`. The CLI entrypoint is `tradingagents = cli.main:app`.
