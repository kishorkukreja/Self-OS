---
source: https://github.com/openai/openai-realtime-meeting-assistant
date: 2026-05-12
type: repo
tags: [openai, realtime-api, meeting-assistant, kanban, webrtc, voice-agents, function-calling, collaborative-agents]
---

# openai/openai-realtime-meeting-assistant

## Summary

`openai/openai-realtime-meeting-assistant` is an OpenAI demo repository showing how to use the Realtime API as a voice-operated meeting assistant for managing a shared Kanban board during a standup. Multiple users join a WebRTC room, speak naturally, and the assistant updates the board in real time using function calling.

## Repository metadata

- Repository: `openai/openai-realtime-meeting-assistant`
- Description: Example of using Realtime API as a meeting assistant to manage a Kanban Board.
- License: MIT
- Default branch: `main`
- Approximate capture stats: 82 stars, 13 forks
- Languages: Go and HTML
- Latest noted commit: `Add note that repo has no built-in security/auth` on May 11, 2026

## How it works

The app creates a WebRTC meeting room. Browser participants provide camera and microphone access. The server:

1. Receives participant audio.
2. Mixes audio from all participants.
3. Sends mixed audio to an OpenAI Realtime peer.
4. Uses model tool/function calls to interpret spoken updates.
5. Applies Kanban board operations.
6. Broadcasts board changes to all connected participants.

If `OPENAI_API_KEY` is missing or the Realtime connection fails, the browser room still loads, but the Kanban assistant does not listen or update cards.

## Key files

- `README.md` — setup and usage guide.
- `main.go` — server entrypoint and HTTP bind address.
- `kanban.go` — Kanban logic, realtime instructions, tools, model setup, initial cards.
- `audio_mixer.go` — mixes participant audio before forwarding to the model.
- `opus_decoder.go` / `opus_encoder.go` — Opus audio support.
- `index.html` — browser UI.
- `public/` — static assets.

## Setup notes

- Requires `OPENAI_API_KEY` in the shell environment.
- `.env` is not loaded automatically.
- Requires Go 1.24+.
- Requires Opus library via `pkg-config`.
- On macOS: `brew install opus pkg-config`.
- Run with `go run .` and open `http://localhost:3000`.
- Alternate port: `go run . -addr :8080`.

## Security warning

The repository explicitly states that the demo does **not** include built-in authentication or access control. Anyone who can reach the app URL can join and access the meeting room. It should not be publicly deployed without authz/authn controls.

## Why it matters

This is a concrete pattern for real-time collaborative agents: live audio → realtime model → tool calls → shared operational state. The Kanban board makes the agent's actions inspectable and shared by the group.

## Self-OS implications

- Useful reference for a future voice-driven Self-OS/Kanban meeting assistant.
- Could support live project review sessions where spoken updates create or move cards.
- Security caveat is load-bearing: any Self-OS version must be private/Tailscale/auth-gated.
- The architecture can inform voice control for Telegram/Kanban workflows without building a full public web app first.
