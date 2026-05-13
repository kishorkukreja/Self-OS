---
title: "OpenAI Cookbook: Build Live Translation Apps with `gpt-realtime-translate"
date_created: 2026-05-13
date_modified: 2026-05-13
summary: "Compiled source summary for OpenAI Cookbook: Build Live Translation Apps with `gpt-realtime-translate."
tags: [openai, realtime-api, speech-to-speech, translation, voice-ai, webrtc, websockets, twilio]
type: source
status: final
---

# OpenAI Cookbook: Build Live Translation Apps with `gpt-realtime-translate

**Type:** resource
**Date:** 2026-05-12
**URL/source:** https://developers.openai.com/cookbook/examples/voice_solutions/realtime_translation_guide?utm_source=tldrai
**Raw file:** [[../raw/resources/openai-realtime-translation-guide-2026-05-12.md]]

**Summary:** This resource source captures **OpenAI Cookbook: Build Live Translation Apps with `gpt-realtime-translate** as part of the AI Research OS stream for 2026-05-12. It is most useful as evidence about openai, realtime-api, speech-to-speech, translation, voice-ai, with emphasis on how agents, models, tools, workflows, or research artifacts are being operationalized rather than as an isolated announcement.

The source's main signal is that OpenAI Cookbook: Build Live Translation Apps with gpt realtime translate Summary OpenAI's cookbook guide shows how to build low latency speech to speech translation apps using gpt realtime translate. The model is designed for live interpretation rather than general voice agent behavior: it automatically detects source language, streams translated speech and captions, and focuses on translating rather than answering or obeying spoken instructions. The guide covers three integration paths: browser tab audio over WebR.

For Self-OS, the practical implication is to treat the source as a pattern library entry: identify which capabilities should become durable skills, which workflows need reviewable artifacts, and which claims require follow-up evidence before being promoted into canonical operating guidance.

Specific details worth preserving include: `gpt-realtime-translate` accepts spoken input and returns translated speech, translated transcript deltas, and optionally source-language transcripts.; Developers specify the target output language; the model supports 70+ input languages and 13 output languages.; The guide distinguishes translation apps from autonomous voice agents: for agents, OpenAI recommends `gpt-realtime-2` rather than the translation-specific model.; Browser-originated media should use WebRTC; backend audio pipelines such as Twilio/SIP/broadcast streams should use WebSockets..

The raw capture remains the authoritative record; this page provides a synthesized pointer back to the raw file and should be connected to concepts/entities only where those links improve retrieval.

**Key connections:** [[concepts/remote-agent-workspaces.md|Remote Agent Workspaces]], [[concepts/realtime-ai.md|Realtime Ai]], [[concepts/realtime-translation.md|Realtime Translation]]

**Entities:** [[entities/openai.md|OpenAI]]

**Tags:** openai, realtime-api, speech-to-speech, translation, voice-ai, webrtc, websockets, twilio
