---
source: https://huggingface.co/mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF
date: 2026-04-29
type: resource
tags: [huggingface, gguf, qwen, qwen3-6, moe, local-llm, quantization, apex, reasoning-distillation]
---

# mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF

**Hugging Face:** https://huggingface.co/mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF  
**Publisher:** mudler / LocalAI ecosystem  
**Model format:** GGUF  
**Architecture / family:** Qwen3.6 35B-A3B MoE derivative  
**Downloads:** 9382  
**Likes:** 20  
**Last modified:** 2026-04-27T14:00:34.000Z  

## Summary

This Hugging Face repository provides **APEX GGUF quantizations** of `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled`. It packages a Claude Opus reasoning-distilled Qwen3.6 35B-A3B MoE model into multiple local-inference GGUF variants for different quality/size tradeoffs.

The key technical idea is **APEX — Adaptive Precision for EXpert Models**. APEX is a quantization strategy for MoE models that varies precision by tensor role and layer position: attention/shared components and edge layers get higher precision, while middle routed-expert FFN weights are compressed more aggressively. The model card argues this works well for MoE because expert FFN tensors dominate weight size but only a small subset of experts activate per token.

## Key points

- GGUF quantized local-inference release for a Qwen3.6 35B-A3B Claude 4.7 Opus reasoning-distilled model.
- Uses APEX quantization, designed specifically for Mixture-of-Experts models.
- Includes variants such as Balanced, Quality, Compact, Mini, Nano, and F16 reference tiers.
- Includes `mmproj.gguf`, indicating vision/projector support for image understanding.
- LocalAI run command from model card:

```bash
local-ai run mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF@Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Balanced.gguf
```

## Why it matters

This is relevant for local LLM tracking because it combines three current themes: reasoning distillation from frontier models, MoE-specific quantization, and deployability through GGUF/LocalAI. It may be useful to compare against other local reasoning models for agentic coding, tool use, and low-cost autonomous workflows.

## Files observed via Hugging Face API

- `.gitattributes`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-Balanced.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-Compact.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Balanced.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Compact.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Mini.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Nano.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Quality.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-Quality.gguf`
- `Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-F16.gguf`
- `README.md`
- `mmproj.gguf`

## Raw model card / extracted content

---
license: apache-2.0
base_model: lordx64/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled
tags:
  - gguf
  - quantized
  - apex
  - moe
  - mixture-of-experts
  - qwen3
  - vlm
  - vision
  - reasoning
  - distilled
  - claude-opus
---




<!-- apex-banner-v2 -->
<div style="background-color: #f59e0b; color: white; padding: 20px; border-radius: 10px; text-align: center; margin: 20px 0;">
<h2 style="color: white; margin: 0 0 10px 0;">⚡ Each donation = another big MoE quantized</h2>
<p style="font-size: 18px; margin: 0 0 15px 0;">I host <b>25+ free APEX MoE quantizations</b> as independent research. My only local hardware is an <b>NVIDIA DGX Spark</b> (122 GB unified memory) — enough for ~30-50B-class MoEs, but <b>bigger ones (200B+) require rented compute</b> on H100/H200/Blackwell, typically $20-100 per quant.<br>If APEX quants are useful to you, your support directly funds those bigger runs.</p>
<p style="font-size: 20px; margin: 0;">
<a href="https://www.patreon.com/cw/mudler" style="color: white; text-decoration: underline;">🎉 Patreon (Monthly)</a> &nbsp;|&nbsp;
<a href="https://www.buymeacoffee.com/mudler" style="color: white; text-decoration: underline;">☕ Buy Me a Coffee</a> &nbsp;|&nbsp;
<a href="https://github.com/sponsors/mudler" style="color: white; text-decoration: underline;">⭐ GitHub Sponsors</a>
</p>
<p style="font-size: 14px; margin: 10px 0 0 0; opacity: 0.9;">💚 Big thanks to Hugging Face for generously donating additional storage — much appreciated.</p>
</div>

# Qwen3.6 35B-A3B — Claude 4.7 Opus Reasoning Distilled — APEX GGUF

**APEX (Adaptive Precision for EXpert Models)** quantizations of [lordx64/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled](https://huggingface.co/lordx64/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled).

**Brought to you by the [LocalAI](https://github.com/mudler/LocalAI) team** | [APEX Project](https://github.com/mudler/apex-quant) | [Technical Report](https://github.com/mudler/apex-quant/blob/main/paper/APEX_Technical_Report.pdf)

## Available Files

| File | Profile | Size | Best For |
|------|---------|------|----------|
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Balanced.gguf | I-Balanced | 24 GB | Best overall quality/size ratio |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-Balanced.gguf | Balanced | 24 GB | General purpose |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Quality.gguf | I-Quality | 21 GB | Highest quality with imatrix |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-Quality.gguf | Quality | 21 GB | Highest quality standard |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Compact.gguf | I-Compact | 16 GB | Consumer GPUs, best quality/size |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-Compact.gguf | Compact | 16 GB | Consumer GPUs |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Mini.gguf | I-Mini | 13 GB | Smallest "safe" tier |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Nano.gguf | **I-Nano** | 11 GB | Experimental — IQ2_XXS mid-layer experts |
| Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-F16.gguf | F16 reference | 65 GB | Full-precision reference |
| mmproj.gguf | Vision projector | ~1 GB | Required for image understanding |

## What is APEX?

APEX is a quantization strategy for Mixture-of-Experts (MoE) models. It classifies tensors by role (routed expert, shared expert, attention) and applies a layer-wise precision gradient — edge layers get higher precision, middle layers get more aggressive compression. I-variants use diverse imatrix calibration (chat, code, reasoning, tool-calling, agentic traces, Wikipedia).

The key insight: in MoE models, expert FFN tensors make up the bulk of model weight but only ~8/256 experts activate per token. APEX compresses middle-layer experts more aggressively while preserving edge layers (first/last 5) and keeping attention, SSM/Mamba, and shared expert tensors at higher precision.

See the [APEX project](https://github.com/mudler/apex-quant) for full details, technical report, and scripts.

### Nano (experimental tier)

The **APEX Nano** tier pushes mid-layer routed experts to **IQ2_XXS (2.06 bpw)**, near-edge to IQ2_S, edges to Q3_K, with shared experts kept at Q5_K. About 20% smaller than Mini with modest quality cost — viable only on MoE thanks to sparse per-token expert activation. Requires imatrix.

Benchmarks pending. Feedback welcome.

## Architecture

- **Model**: Qwen3.6 35B-A3B Claude 4.7 Opus Reasoning Distilled
- **Base**: Qwen 3.6 35B-A3B
- **Layers**: 40
- **Experts**: 256 routed + shared (8 active per token)
- **Total Parameters**: ~35B
- **Active Parameters**: ~3B per token
- **Attention**: Hybrid (full attention every 4th layer, linear/Mamba otherwise)
- **Vision**: Built-in vision encoder (mmproj included)
- **APEX Config**: 5+5 symmetric edge gradient across 40 layers
- **Calibration**: v1.3 diverse dataset (chat, code, reasoning, multilingual, tool-calling, Wikipedia)

## Run with LocalAI

```bash
local-ai run mudler/Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-GGUF@Qwen3.6-35B-A3B-Claude-4.7-Opus-Reasoning-Distilled-APEX-I-Balanced.gguf
```

## Credits

- **Reasoning distill fine-tune**: [lordx64](https://huggingface.co/lordx64)
- **Vision projector (mmproj)**: [mradermacher](https://huggingface.co/mradermacher)
- **APEX quantization**: [LocalAI](https://github.com/mudler/LocalAI) team
- Built on [llama.cpp](https://github.com/ggerganov/llama.cpp)
