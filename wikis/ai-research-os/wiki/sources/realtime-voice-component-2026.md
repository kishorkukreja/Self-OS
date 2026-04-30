---
title: "OpenAI Realtime Voice Component"
date_created: 2026-04-30
date_modified: 2026-04-30
summary: "openai/realtime-voice-component is a React/browser reference implementation for building voice-controlled UI surfaces on top of OpenAI Realtime. The key design pattern is app-owned narrow tools: the assistant can request"
tags: [openai, realtime-api, voice-ui, react, browser-agents, tool-use, typescript, apache-2]
type: source
status: final
---

# OpenAI Realtime Voice Component

**Type:** repo  
**Date:** 2026-04-29  
**URL:** https://github.com/openai/realtime-voice-component  
**Raw file:** [[../raw/repos/realtime-voice-component-2026-04-29.md]]

**Summary:** openai/realtime-voice-component is a React/browser reference implementation for building voice-controlled UI surfaces on top of OpenAI Realtime. The key design pattern is app-owned narrow tools: the assistant can request bounded actions, but the application remains the source of truth for state and visible UI changes.
It is useful for teams building voice interfaces where natural language should control application workflows without giving the model free-form browser automation. The repo provides a controller, React bindings, launcher widget, tool definition helpers, and optional ghost-cursor confirmation patterns.

**Key contributions:**
- Reference implementation, not a guaranteed long-term supported production UI kit.
- Intended for React/browser apps using OpenAI Realtime.
- Centers on narrow, app-owned function tools rather than unconstrained UI/browser automation.
- Provides defineVoiceTool(), createVoiceControlController(), useVoiceControl(), VoiceControlWidget, and ghost-cursor helpers.
- Demo app includes theme switching, multi-step forms, shared-state chess, shared controller reuse, and wake-word experimentation.
- Recommended integration: proxy browser SDP/session config through an app /session endpoint, register narrow tools, and send visible state changes back into the session.

**Tags:** openai, realtime-api, voice-ui, react, browser-agents, tool-use, typescript, apache-2
