---
title: "Claude Prompt Cache Pre-Warming with max_tokens=0"
date_created: 2026-05-17
date_modified: 2026-05-17
summary: "Operational note on using Anthropic Claude prompt caching as a latency-management mechanism for large stable prompts."
tags: [anthropic, claude-api, prompt-caching, latency]
type: source
status: final
---

# Claude Prompt Cache Pre-Warming with max_tokens=0

**Type:** resource  
**Date:** 2026-05-16  
**URL:** conversation + https://platform.claude.com/docs/en/build-with-claude/prompt-caching  
**Raw file:** [[../raw/resources/claude-prompt-cache-prewarming-2026-05-16.md]]

## Summary

This resource reframes Anthropic Claude prompt caching as an active latency-control tool, not only as a cost optimization. The central pattern is to send a throwaway request with `max_tokens=0` and `cache_control` attached to the stable reusable prefix, such as tools, system prompts, static examples, durable memory, or shared RAG context. Because Claude’s cache key depends on the ordered prefix through the marked block, the warmup request can pay the cache-write and prefill cost before the real user task arrives. The next real request can then reuse the same prefix and hit a warm cache.

The important implementation detail is cache-breakpoint placement. `cache_control` belongs on the stable system or context block, not on a placeholder user message, otherwise the application may cache the wrong prefix and miss on the real request. The capture also preserves operational caveats: default ephemeral TTL is short, often five minutes; low-traffic products may need a refresh timer or session-start hook; cache writes still cost money; and any prompt difference before the breakpoint creates a miss. For Hermes and Self-OS, the pattern is relevant to profiles with large system prompts, long tool schemas, or voice/chat UX where first-token latency is visible.

## Key contributions

- Defines pre-warming as scheduled background work that shifts first-call latency away from the user path.
- Documents the cache-control placement rule and TTL limitations that determine whether the technique works.
- Connects prompt caching to agent profiles, voice UX, and long-context operating loops.

**Related:** [[concepts/prompt-cache-prewarming.md]], [[concepts/latency-management-for-agents.md]], [[entities/anthropic-claude-api.md]]
