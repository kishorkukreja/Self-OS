---
title: "HY-Embodied — Embodied Foundation Models"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Tencent's family of embodied foundation models for real-world agents, featuring a Mixture-of-Transformers architecture with 2B edge and 32B reasoning variants trained on 100M+ embodied data points."
tags: [embodied-ai, vlm, vision-language-model, robotics, mixture-of-transformers, tencent]
type: source
status: final
---

# HY-Embodied — Embodied Foundation Models

**Type:** repo
**Date:** 2026-04-12
**URL:** https://github.com/Tencent-Hunyuan/HY-Embodied
**Raw file:** [[../../raw/repos/hy-embodied-2026-04-12.md]]

**Summary:** HY-Embodied-0.5 is a suite of foundation models from Tencent tailored for real-world embodied intelligence. The architecture introduces Mixture-of-Transformers (MoT) with latent tokens for modality-specific computing, enhancing fine-grained spatial-temporal perception. Two primary variants are offered: a highly efficient 2B model (4B total, 2.2B activated) for edge deployment and a powerful 32B model for complex reasoning. Through self-evolving post-training and large-to-small on-policy distillation, the compact MoT-2B outperforms state-of-the-art models of similar size across 16 embodied-relevant benchmarks, while the 32B variant achieves frontier-level performance. HY-Embodied serves as a robust cognitive engine for Vision-Language-Action (VLA) pipelines in physical robot control.

**Key contributions:**
- Mixture-of-Transformers (MoT) architecture with modality-specific latent tokens
- Edge-efficient 2B variant (2.2B activated) with dense-model inference speed
- 32B variant with frontier-level embodied reasoning capabilities
- Self-evolving post-training pipeline with on-policy distillation
- Trained on >100M embodied and spatial-specific data points (>200B tokens)

**Tags:** embodied-ai, vlm, vision-language-model, robotics, mixture-of-transformers, tencent
