---
source: https://github.com/openai/realtime-voice-component
date: 2026-04-29
type: repo
tags: [openai, realtime-api, voice-ui, react, browser-agents, tool-use, typescript, apache-2]
status: processed
---

# OpenAI Realtime Voice Component

**Repository:** https://github.com/openai/realtime-voice-component  
**Owner:** OpenAI  
**License:** Apache-2.0  
**Stats:** 743 stars · 89 forks · 1 open issues  
**Language:** TypeScript  
**Latest pushed:** 2026-04-27T22:57:27Z  

## Summary

`openai/realtime-voice-component` is a React/browser reference implementation for building voice-controlled UI surfaces on top of OpenAI Realtime. The key design pattern is **app-owned narrow tools**: the assistant can request bounded actions, but the application remains the source of truth for state and visible UI changes.

It is useful for teams building voice interfaces where natural language should control application workflows without giving the model free-form browser automation. The repo provides a controller, React bindings, launcher widget, tool definition helpers, and optional ghost-cursor confirmation patterns.

## Key points

- Reference implementation, not a guaranteed long-term supported production UI kit.
- Intended for React/browser apps using OpenAI Realtime.
- Centers on narrow, app-owned function tools rather than unconstrained UI/browser automation.
- Provides `defineVoiceTool()`, `createVoiceControlController()`, `useVoiceControl()`, `VoiceControlWidget`, and ghost-cursor helpers.
- Demo app includes theme switching, multi-step forms, shared-state chess, shared controller reuse, and wake-word experimentation.
- Recommended integration: proxy browser SDP/session config through an app `/session` endpoint, register narrow tools, and send visible state changes back into the session.

## Why it matters

This is a practical pattern for voice agents inside product UIs: keep agency bounded, keep state authoritative in the app, and expose only typed, auditable action surfaces to the model. It belongs beside other AI UI and agent-control-plane patterns in the wiki.

## Raw README / extracted content

# realtime-voice-component

React/browser voice controls for tool-constrained UIs built on OpenAI Realtime.

> Warning
> This repository is an open-source reference implementation. It is useful for
> education, demos, and local adoption, but it is not a promise of long-term
> product support or a production-ready UI kit.

## Distribution Status

This repo is intended to be shared as a GitHub reference implementation. It is
not currently published to npm, and `package.json` remains marked as private.

The code is licensed under Apache-2.0. See [`LICENSE`](./LICENSE).

## What This Package Is

This package is for apps where:

- your app defines the exact actions the assistant can take
- tools stay app-owned and narrow
- the UI remains responsible for the visible state change
- you want a React-friendly controller and an optional launcher widget

The package is intentionally opinionated about browser UI flows. It is not a
general-purpose orchestration framework and it is not a replacement for raw
Realtime transports.

## Choose The Right Layer

Use this package when you want a React/browser layer for voice-driven UI:

- a reusable controller with React bindings
- a packaged launcher widget
- optional visible confirmation via the ghost cursor
- a pattern centered on app-owned tools, not free-form browser automation

Use raw Realtime when you want lower-level transport and session control:

- custom audio handling
- non-React runtimes
- your own UI surface and state model from scratch

Use [`openai-agents-js`](https://github.com/openai/openai-agents-js) when you
need a broader headless SDK:

- agent orchestration and handoffs
- richer hosted-tool and MCP flows
- server-side or multi-runtime agent systems beyond a browser UI package

## Demo App

The repo’s [`demo/`](./demo) app is the main runnable teaching surface. It
shows:

- a starter theme-switching flow
- a multi-step form flow
- a richer shared-state chess flow
- shared controller reuse across multiple screens
- optional wake-word experimentation layered on top of the runtime

Run it locally with:

```bash
cp demo/.env.example demo/.env.local
# edit demo/.env.local and set OPENAI_API_KEY
npm install
npm run demo
```

## Package Shape

- `defineVoiceTool()` turns a Zod-backed app action into a Realtime function
  tool.
- `createVoiceControlController()` owns the session, transport, tool execution,
  transcript assembly, and connection lifecycle.
- `useVoiceControl()` binds React to either an external controller or an
  internally owned one.
- `VoiceControlWidget` is a launcher UI on top of the controller.
- `useGhostCursor()` and `GhostCursorOverlay` are optional visible confirmation
  helpers.

## Recommended Default Flow

For most browser apps in this repo, the recommended path is:

1. proxy the browser SDP + session config through your own `/session` endpoint
2. register one narrow tool that maps to one real app action
3. start with the theme demo or a small controller-based integration
4. send current UI state back into the session after visible changes

## Turn Detection Defaults

The controller uses Realtime `server_vad` by default. For text and tool-only
sessions, it also sets `interrupt_response: false` so new speech does not cancel
an in-flight text response or tool call. That matters when your UI does not play
assistant audio back to the user.

If you override `audio.input.turnDetection`, use a server VAD shape like this as
the starting point for tool-only UI control:

```ts
{
  type: "server_vad",
  threshold: 0.5,
  prefixPaddingMs: 300,
  silenceDurationMs: 200,
  createResponse: true,
  interruptResponse: false,
}
```

## Integrating With An Existing App

The most reliable retrofit pattern is:

- keep your app as the source of truth
- create one explicit controller for one voice surface
- put a small app-owned wrapper between tools and your real handlers
- keep the widget launcher-focused

In practice, this avoids most of the confusing failure modes we hit while
integrating the package into a larger app.

Before you wire anything, choose ownership:

- single-screen ownership: the controller belongs to one screen and can be
  created with that screen's tools immediately
- shared shell or provider ownership: the controller lives above scene-level UI
  because the same session should stay alive across scene, tab, or route changes

That choice affects where the controller lives, whether `tools` are known at
creation time, and whether a neutral bootstrap controller is the right shape.

### Step-by-Step Guide

1. **Install the package like a normal app dependency.**
   Use your package manager to install `realtime-voice-component` from the
   local checkout path and import `realtime-voice-component/styles.css` from
   your app. Prefer a normal dependency install over reaching directly into the
   package source tree from your app.

2. **Add a `/session` endpoint in your app backend.**
   Have the browser send SDP plus session config to your app server, and have
   your server forward that request to `POST https://api.openai.com/v1/realtime/calls`.
   Keep the multipart body intact unless you intentionally need to override
   session settings.

   Example:

   ```ts
   app.post("/session", async (request, response) => {
     const contentType = request.header("content-type");

     const realtimeResponse = await fetch("https://api.openai.com/v1/realtime/calls", {
       method: "POST",
       headers: {
         Authorization: `Bearer ${process.env.OPENAI_API_KEY}`,
         ...(contentType ? { "Content-Type": contentType } : {}),
       },
       body: request,
       duplex: "half",
     });

     response
       .status(realtimeResponse.status)
       .type(realtimeResponse.headers.get("content-type") ?? "application/sdp")
       .send(await realtimeResponse.text());
   });
   ```

3. **Create a small app-owned voice wrapper.**
   Build a wrapper or adapter around your existing app state and handlers.
   Good wrapper methods are things like:
   - `getState()`
   - `setPrompt()`
   - `setScenario()`
   - `startRun()`
   - `stopRun()`
   - `sendToast()`

   Example:

   ```tsx
   const stateRef = useRef({
     prompt,
     runStatus,
     scenarioId,
   });
   stateRef.current = {
     prompt,
     runStatus,
     scenarioId,
   };

   const voiceAdapter = useMemo(
     () => ({
       getState: () => stateRef.current,
       sendToast: (message: string) => {
         toast(message);
       },
       setPrompt,
       setScenario: setScenarioId,
       startRun,
       stopRun,
     }),
     [setPrompt, setScenarioId, startRun, stopRun],
   );
   ```

   Prefer refs or stable selectors when a tool needs the latest state at call
   time. Avoid rebuilding every tool definition on every state change just to
   read current values.

   The `useMemo` calls in this pattern are about referential stability, not
   generic optimization. If your wrapper object or tool array changes identity
   every render, `controller.configure(...)` will also rerun every render.

4. **Register narrow tools against the wrapper.**
   Tools should call wrapper methods, and wrapper methods should call your real
   app logic. Do not let tool `execute()` become a second business-logic layer.

   Example:

   ```tsx
   const tools = useMemo(
     () => [
       defineVoiceTool({
         name: "get_screen_state",
         description: "Inspect the current app state before acting.",
         parameters: z.object({}),
         execute: () => ({
           ok: true,
           state: voiceAdapter.getState(),
         }),
       }),
       defineVoiceTool({
         name: "set_prompt",
         description: "Replace the current prompt.",
         parameters: z.object({
           prompt: z.string().min(1),
         }),
         execute: ({ prompt }) => {
           voiceAdapter.setPrompt(prompt);
           return { ok: true, prompt };
         },
       }),
       defineVoiceTool({
         name: "start_run",
         description: "Start the current run.",
         parameters: z.object({}),
         execute: async () => {
           await voiceAdapter.startRun();
           return { ok: true };
         },
       }),
       defineVoiceTool({
         name: "send_message",
         description: "Show a short operator-facing message.",
         parameters: z.object({
           message: z.string().min(1),
         }),
         execute: ({ message }) => {
           voiceAdapter.sendToast(message);
           return { ok: true };
         },
       }),
     ],
     [voiceAdapter],
   );
   ```

5. **Hoist the controller at the layer that owns the voice surface.**
   If a screen, route shell, or provider owns the voice-enabled surface, create
   the controller there. If you pass an external controller into
   `useVoiceControl(controller)` or `VoiceControlWidget`, your app owns that
   controller's lifecycle.

   Example:

   ```tsx
   const [controller] = useState(() =>
     createVoiceControlController({
       activationMode: "vad",
       auth: { sessionEndpoint: "/session" },
       instructions:
         "Use the provided tools to control the current screen. Prefer tools over free-form responses.",
       outputMode: "tool-only",
       tools,
     }),
   );
   ```

   Initializing with the current `tools` avoids the confusing “empty controller
   first, tools later” shape in docs. You should still resync the external
   controller when the tool set changes.

   If your app owns a controller above screen-level tools, a neutral bootstrap
   is still valid. The shared demo session in this repo starts with `tools: []`
   and reconfigures as each demo screen becomes active. Use that shape only when
   the controller genuinely exists before the final tool set does or when the
   same session needs to survive scene changes.

6. **Use an Effect only to sync the external controller.**
   It is appropriate to call `controller.configure(...)` from `useEffect`
   because the controller is an external object, not React state. Do not use
   Effects to mirror React state into more React state.

   Example:

   ```tsx
   useEffect(() => {
     controller.configure({
       activationMode: "vad",
       auth: { sessionEndpoint: "/session" },
       instructions:
         "Use the provided tools to control the current screen. Prefer tools over free-form responses.",
       outputMode: "tool-only",
       tools,
     });
   }, [controller, tools]);
   ```

7. **Mount `VoiceControlWidget` as a launcher, not as your state model.**
   The widget should stay thin. If you want visible confirmation, add
   `GhostCursorOverlay`, but keep real state changes inside your app handlers.

   Example:

   ```tsx
   return (
     <>
       <GhostCursorOverlay state={cursorState} />
       <VoiceControlWidget controller={controller} snapToCorners />
     </>
   );
   ```

   Only call `useVoiceControl(controller)` in the parent component if that
   component actually needs to render runtime state like `connected`,
   `activity`, or tool-call history. `VoiceControlWidget` already binds to the
   controller internally.

   When the integration gets larger, split it into explicit files instead of
   leaving everything in one screen component. A good default shape is:

   ```text
   voice/
     voiceAdapter.ts
     voiceTools.ts
     useScreenVoiceController.ts
     VoicePanel.tsx
   ```

   Keep the adapter, tools, controller wiring, and panel UI separate. The demo
   code in this repo follows that same general pattern.

8. **Send app state back into the session after visible changes.**
   If the model needs fresh context, push current app state back into the
   session so the model stays grounded in what is actually on screen.

9. **Debug in this order.**
   - If the widget stays at `idle` and never hits `/session`, inspect controller
     ownership, widget mounting, and browser media/WebRTC support first.
   - If the widget moves to `error` before `/session`, inspect the browser

[Truncated for raw wiki note; source URL contains full content.]

