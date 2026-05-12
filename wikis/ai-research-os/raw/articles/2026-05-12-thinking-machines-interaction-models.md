---
source: https://thinkingmachines.ai/blog/interaction-models/
date: 2026-05-12
type: article
tags: [interaction-models, multimodal-ai, real-time-ai, moe-models, tool-use, human-ai-collaboration, thinking-machines-lab]
---

# Thinking Machines: Interaction Models

Source captured from the Thinking Machines Lab research preview, plus Kish's note.

## User note

Thinking Machines finally demoed what they’re working on: "interaction models." At first glance, it feels a lot like the GPT-4o demo from 2 years ago: real-time, audio-video-text. The interesting part is underneath though: a 276B MoE “interaction model” (12B active, 0.40s latency) that handles the live conversation, and a separate background model runs reasoning, searches, and tool calls mid-chat, then feeds results back in. Full-duplex isn't new (hi Moshi from Kyutai Labs), but the architectural design is interesting, and the early benchmarks on latency and quality are solid.

## Source facts

- Organization: Thinking Machines Lab.
- Article: "Interaction Models: A Scalable Approach to Human-AI Collaboration."
- Published: 2026-05-11.
- Model previewed: `TML-Interaction-Small`.
- Core claim: interactivity should scale alongside intelligence; human-AI collaboration should not remain a bolt-on interface layer.
- Model shape: 276B-parameter MoE with about 12B active parameters.
- Latency claim: roughly 0.40s response latency, processing continuous multimodal stream chunks.
- Modalities: audio, video, and text.
- Architecture pattern: a foreground real-time interaction model manages live multimodal conversation while a background model performs reasoning, search, and tool/tool-call work, feeding results back into the live interaction.

## Why it matters

This is not just another voice assistant demo. The more interesting claim is architectural: Thinking Machines is separating the problem of real-time human interaction from deeper background reasoning/tool work, while keeping the two coupled inside a live conversational loop.

That makes the preview relevant to several AI-system design questions:

1. Interaction vs autonomy: frontier labs have pushed long-running agentic workflows, but Thinking Machines is arguing that collaborative, synchronous work is a separate scaling axis.
2. Latency as product capability: low-latency multimodal interaction changes what users can do with a system, especially where interruption, correction, visual cues, and backchanneling matter.
3. Foreground/background model split: the architecture resembles an operating system pattern — a low-latency interaction layer mediates the session, while heavier reasoning/search/tool execution happens asynchronously in the background.
4. Full-duplex is not the differentiator alone: Moshi/Kyutai and GPT-4o-like demos already showed pieces of this. The differentiator to track is whether the interaction architecture produces measurably better collaboration quality, not just smoother voice/video UX.

## Self-OS / Hermes implications

- Hermes should treat "interaction model" as a useful architecture pattern: live control surface + asynchronous reasoning/tool workers + result reintegration.
- This maps cleanly onto Hermes/Self-OS: WhatsApp/Telegram/TUI as the interaction layer, subagents/cron/tools as background reasoning/work layers, and wiki/taskOS as persistent state.
- For future Hermes voice or multimodal experiments, the important design target is not only speech latency; it is the ability to keep a live conversational loop open while background searches, tool calls, and reasoning complete without blocking the interaction.
- This also suggests an evaluation axis for agents: collaboration latency and interruption-handling quality, not only task success.

## Related concepts/entities to compile later

- [[interaction-models]]
- [[full-duplex-ai]]
- [[multimodal-agent-interfaces]]
- [[foreground-background-agent-architecture]]
- [[thinking-machines-lab]]
- [[kyutai-moshi]]
- [[gpt-4o]]
