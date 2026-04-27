---
title: "Mixture-of-Transformers"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "Architecture using modality-specific transformer parameters to improve multi-modal model performance without degrading language capabilities."
tags: ['mixture-of-transformers', 'multimodal', 'architecture', 'vlm']
type: concept
status: draft
confidence: emerging
source_count: 1
---

# Mixture-of-Transformers

**Mixture-of-Transformers (MoT)** is an adaptive computing architecture that introduces modality-specific QKV and FFN parameters. In VLMs, visual tokens are processed with duplicated vision-specific parameters while text tokens use original language parameters, enabling stronger visual modeling without catastrophic forgetting of language capabilities. [[HY-Embodied-0.5]] uses MoT alongside bidirectional visual attention and visual next-code prediction to achieve state-of-the-art embodied perception.

Related: [[Mixture-of-Experts]], [[vision-language model]], [[adaptive computing]].

_Last updated: 2026-04-27_
