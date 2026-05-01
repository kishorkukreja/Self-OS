---
title: "TauricResearch/TradingAgents"
date_created: 2026-05-01
date_modified: 2026-05-01
summary: "[[entities/tradingagents]] is an open-source multi-agent LLM research framework for financial trading analysis."
tags: [tradingagents, tauric-research, multi-agent, finance, trading, stock-analysis, langgraph]
type: source
status: final
---

# TauricResearch/TradingAgents

**Type:** repo  
**Date:** 2026-04-30  
**URL:** https://github.com/TauricResearch/TradingAgents  
**Raw file:** [[../raw/repos/tradingagents-2026-04-30.md]]

## Summary

[[entities/tradingagents]] is an open-source multi-agent LLM research framework for financial trading analysis. It simulates a trading firm with specialized agents for fundamentals, sentiment, news and macro context, technical analysis, bullish and bearish research debate, trader synthesis, risk management, and portfolio-manager-style final decisions. The architecture is notable because it decomposes stock research into roles with adversarial review rather than asking a single model for a monolithic recommendation.

For Self-OS, the useful pattern is [[concepts/multi-agent-financial-analysis]], not any particular trading call. The v0.2.4 release adds structured-output decision agents, LangGraph checkpoint resume, persistent decision logs, Docker support, several model-provider integrations, and a consistent five-tier rating scale. Those features make the framework a reference for repeatable, auditable analysis workflows where every run is timestamped and caveated. The source should retain its disclaimer: outputs depend on model choice, temperature, data quality, time window, and nondeterminism, and should be treated as research rather than investment advice.

## Key contributions
- TradingAgents decomposes stock analysis into analyst roles, bull/bear debate, trader synthesis, risk review, and portfolio-manager decisions.
- The v0.2.4 release adds structured outputs, checkpoint resume, persistent decision logs, Docker support, and broader provider support.
- The framework is best treated as a reusable research workflow pattern, not as financial or investment advice.

## Concepts and entities

**Concepts:** [[concepts/multi-agent-financial-analysis]], [[concepts/structured-output-generation]], [[concepts/agent-orchestration]]  
**Entities:** [[entities/tradingagents]], [[entities/tauric-research]], [[entities/langgraph]]

**Tags:** tradingagents, tauric-research, multi-agent, finance, trading, stock-analysis, langgraph
