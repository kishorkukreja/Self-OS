---
title: "Amortizing Intractable Inference in Large Language Models"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "ICLR 2024 paper using GFlowNets to fine-tune LLMs for sampling from intractable posteriors, framing chain-of-thought reasoning as latent variable modeling."
tags: [gflownets, bayesian-inference, llm-fine-tuning, chain-of-thought, latent-variable, iclr-2024]
type: source
status: final
---

# Amortizing Intractable Inference in Large Language Models

**Type:** paper
**Date:** 2026-04-26
**URL:** https://arxiv.org/abs/2310.04363
**Authors:** Edward J. Hu, Moksh Jain, Eric Elmoznino, Younesse Kaddar, Guillaume Lajoie, Yoshua Bengio, Nikolay Malkin
**Venue:** ICLR 2024
**Raw file:** [[../../raw/papers/2026-04-26-hu-jain-amortizing-intractable-inference.md]]

**Summary:** Hu et al. identify a fundamental limitation of autoregressive LLMs: they only permit tractable start-to-end sampling, yet many valuable tasks — infilling, constrained generation, and multi-step reasoning — require sampling from intractable posteriors. Their solution applies **amortized Bayesian inference** by fine-tuning LLMs with **GFlowNets**, diversity-seeking reinforcement learning algorithms that match distributions rather than maximizing rewards. This distribution-matching paradigm offers an alternative to both maximum-likelihood training and reward-maximizing policy optimization (e.g., RLHF/PPO). As a key application, they frame **chain-of-thought reasoning** as latent variable modeling, showing data-efficient adaptation for multi-step rationalization and tool use.

**Key contributions:**
- Formalizes the intractable inference problem in autoregressive LLMs
- Proposes GFlowNet-based fine-tuning as a distribution-matching alternative to RLHF
- Demonstrates data-efficient adaptation for chain-of-thought and tool-use tasks
- Provides open-source implementation for reproducibility

**Tags:** gflownets, bayesian-inference, llm-fine-tuning, chain-of-thought, latent-variable, iclr-2024
