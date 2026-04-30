---
title: "mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF"
date_created: 2026-04-30
date_modified: 2026-04-30
summary: "This Hugging Face repository provides APEX GGUF quantizations of Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled. It packages a Claude Opus reasoning-distilled Qwen3.6 35B-A3B MoE model into multiple local-inference "
tags: [huggingface, gguf, qwen, qwen3-6, moe, local-llm, quantization, apex]
type: source
status: final
---

# mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF

**Type:** resource  
**Date:** 2026-04-29  
**URL:** https://huggingface.co/mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF  
**Raw file:** [[../raw/resources/qwen3-6-35b-a3b-claude-4-7-opus-reasoning-distilled-apex-gguf-2026-04-29.md]]

**Summary:** This Hugging Face repository provides APEX GGUF quantizations of Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled. It packages a Claude Opus reasoning-distilled Qwen3.6 35B-A3B MoE model into multiple local-inference GGUF variants for different quality/size tradeoffs.
The key technical idea is APEX — Adaptive Precision for EXpert Models. APEX is a quantization strategy for MoE models that varies precision by tensor role and layer position: attention/shared components and edge layers get higher precision, while middle routed-expert FFN weights are compressed more aggressively. The model card argues this works well for MoE because expert FFN tensors dominate weight size but only a small subset of experts activate per token.

**Key contributions:**
- GGUF quantized local-inference release for a Qwen3.6 35B-A3B Claude 4.7 Opus reasoning-distilled model.
- Uses APEX quantization, designed specifically for Mixture-of-Experts models.
- Includes variants such as Balanced, Quality, Compact, Mini, Nano, and F16 reference tiers.
- Includes mmproj.gguf, indicating vision/projector support for image understanding.
- LocalAI run command from model card:

**Tags:** huggingface, gguf, qwen, qwen3-6, moe, local-llm, quantization, apex, reasoning-distillation
