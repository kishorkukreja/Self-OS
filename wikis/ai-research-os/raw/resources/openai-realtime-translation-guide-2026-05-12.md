---
source: https://developers.openai.com/cookbook/examples/voice_solutions/realtime_translation_guide?utm_source=tldrai
date: 2026-05-12
type: resource
tags: [openai, realtime-api, speech-to-speech, translation, voice-ai, webrtc, websockets, twilio, livekit]
---

# OpenAI Cookbook: Build Live Translation Apps with `gpt-realtime-translate`

## Summary
OpenAI's cookbook guide shows how to build low-latency speech-to-speech translation apps using `gpt-realtime-translate`. The model is designed for live interpretation rather than general voice-agent behavior: it automatically detects source language, streams translated speech and captions, and focuses on translating rather than answering or obeying spoken instructions. The guide covers three integration paths: browser tab audio over WebRTC, phone-call translation through Twilio Media Streams, and video-call translation with LiveKit.

## Key points
- `gpt-realtime-translate` accepts spoken input and returns translated speech, translated transcript deltas, and optionally source-language transcripts.
- Developers specify the target output language; the model supports 70+ input languages and 13 output languages.
- The guide distinguishes translation apps from autonomous voice agents: for agents, OpenAI recommends `gpt-realtime-2` rather than the translation-specific model.
- Browser-originated media should use WebRTC; backend audio pipelines such as Twilio/SIP/broadcast streams should use WebSockets.
- Realtime Translation sessions use a dedicated endpoint, `/v1/realtime/translations`, continuous 24kHz PCM16 input, and 200ms PCM16 output chunks.
- Browser examples should use short-lived client secrets rather than exposing a long-lived OpenAI API key.
- Current limitations: no custom prompting, no voice-selection parameters, no glossaries, and no pronunciation guides.

## Why it matters
The genuine finding is that OpenAI is separating **interpretation** from **general voice agency** at the model/product level. Translation has different failure modes from a voice assistant: the model must not answer questions, follow instructions embedded in speech, or wait for clean turn boundaries. For Self-OS, this suggests voice workflows should route between specialized voice capabilities instead of treating all audio as a generic realtime assistant problem.

## Self-OS implications
- Useful for future multilingual meeting, webinar, or phone-call workflows around Hermes/Self-OS.
- A voice-ingest or meeting pipeline could separate:
  - source transcript capture,
  - translated transcript/audio,
  - entity extraction,
  - wiki/task propagation.
- The WebRTC vs WebSocket split is an architectural rule of thumb: browser media → WebRTC; server-owned telephony/audio streams → WebSockets.
- Because the model currently lacks glossaries/pronunciation guides, domain-specific translation quality should be verified before using it for supply-chain or technical calls.

## Demo repositories referenced
- Browser tab translation: https://github.com/openai/openai-cookbook/tree/main/examples/voice_solutions/realtime_translation_guide/browser-translation-demo
- Twilio phone translation: https://github.com/openai/openai-cookbook/tree/main/examples/voice_solutions/realtime_translation_guide/twilio-translation-demo
- LiveKit video translation: https://github.com/openai/openai-cookbook/tree/main/examples/voice_solutions/realtime_translation_guide/livekit-translation-demo

## Raw content notes
The cookbook describes three live translation patterns:
1. **Browser tab translation** — capture tab audio using `getDisplayMedia()`, send to Realtime Translation over WebRTC, play translated speech and captions in the browser.
2. **Phone-call translation** — use Twilio Media Streams to receive phone audio over WebSockets, bridge into Realtime Translation, and send translated audio back to the caller.
3. **Video-call translation** — subscribe to remote LiveKit microphone tracks, translate each speaker for the listener, and render translated audio/captions locally.

Session configuration centers on `session.audio.output.language`. Source-language transcripts can be requested with:

```json
{"transcription": {"model": "gpt-realtime-whisper"}}
```

Realtime Translation uses continuous audio input/output rather than the normal turn lifecycle: no `response.create`, no assistant turn, no tool call, and no conversation state.
