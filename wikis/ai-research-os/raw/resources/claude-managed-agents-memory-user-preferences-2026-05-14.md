---
source: https://platform.claude.com/cookbook/managed-agents-cma-remember-user-preferences
date: 2026-05-14
type: resource
tags: [claude, managed-agents, agent-memory, user-preferences, memory-stores, persistent-context, anthropic]
status: processed
---

# Claude Cookbook — Build agents that remember your users

## Source metadata

- Source: Claude Cookbook / Anthropic Platform
- Title: "Build Agents That Remember Your Users"
- URL: https://platform.claude.com/cookbook/managed-agents-cma-remember-user-preferences
- Captured: 2026-05-14

## Core idea

The cookbook demonstrates how to build a Claude Managed Agent that remembers user-specific preferences across sessions using a **memory store**. The mental model is a per-user shared notebook: Claude can read/write files in the store during a session, and those files remain available when the same user returns later.

The worked example is a retail shopping assistant that:

- learns a customer's shopping preferences in one session;
- writes those preferences into a user-specific memory store;
- recalls them in a later session;
- lets the application inspect, seed, audit, correct, delete, or export memory contents.

## How memory stores work

When a memory store is attached to a Claude Managed Agent session, it is mounted into the agent environment at:

```text
/mnt/memory/{store-name}
```

Claude interacts with the store through ordinary file operations. The application can also access the same memory files through the REST API, enabling production control over what the agent remembers.

The cookbook recommends one memory store per end user in production, with the application's internal user ID mapped to the Claude memory store ID.

## Implementation pattern

Key steps from the cookbook:

1. Create a memory store.
2. Create or configure a managed agent session with the memory store attached.
3. Let the agent read and write preference files during conversation.
4. Run a second session to verify preferences persist.
5. Add application-side controls for seeding, auditing, correcting, exporting, and deleting memory.

The example uses the Anthropic Python SDK beta APIs and requires:

- `ANTHROPIC_API_KEY`;
- Python 3.11+;
- a recent `anthropic` Python package;
- Managed Agents beta access.

Example install command from the cookbook:

```bash
uv add anthropic
# or
pip install -U anthropic
```

## Why it matters

This is a concrete vendor implementation of an agent-memory architecture that Self-OS has been converging toward independently:

- **Per-user memory substrate:** memory is scoped by user/customer, not just by conversation.
- **File-based persistence:** agent memory is inspectable and editable as files, not hidden opaque model state.
- **Application governance:** the host app can seed, audit, correct, or delete memories.
- **Session continuity:** preferences and durable facts survive a session reset.

The useful distinction is between stable memory and transient task state. User preferences belong in memory stores; half-finished work, debug notes, and implementation state are better captured in handoff/task-state artifacts.

## Self-OS / Hermes implications

- Validates the Self-OS principle that persistent memory should be explicit, inspectable, and correctable.
- Reinforces the need to separate durable user profile facts from short-lived execution context.
- Suggests a possible future Self-OS pattern: per-domain memory folders with app-level review/audit commands, similar to Claude Managed Agents memory stores.
- Could inform a Hermes memory hygiene workflow: show what Hermes believes, allow correction, and route durable facts to memory while routing task state to Markdown artifacts.

## Related captured source

- `raw/x-threads/2026-05-14-odysseus0z-claude-code-handoff-skill-context-preservation.md` — adjacent session-continuity pattern using a `/handoff` Markdown artifact rather than persistent user memory.

## Extraction notes

`web_extract` successfully extracted the Claude Cookbook page as a structured summary. The page is a beta Managed Agents memory example, so exact API details may change.
