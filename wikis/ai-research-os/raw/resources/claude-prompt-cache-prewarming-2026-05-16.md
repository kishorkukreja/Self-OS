---
source: conversation + https://platform.claude.com/docs/en/build-with-claude/prompt-caching
date: 2026-05-16
type: resource
tags: [anthropic, claude-api, prompt-caching, cache-prewarming, latency, inference-optimization, system-prompts, agent-infrastructure, self-os]
---

# Claude prompt cache pre-warming with `max_tokens=0`

## Summary

Anthropic Claude prompt caching can be used as an active latency-management mechanism, not just a cost optimization. For applications with very large shared prompts — long system prompts, agent state, tool definitions, RAG context, or session context — the application can send a throwaway pre-warming request with `max_tokens=0` and `cache_control` applied to the reusable prefix. This pays the first prefill/cache-write latency before the real user request, so the next real call can hit a warm prompt cache.

## Key points

- Use `max_tokens=0` to create a pre-warming request that writes the cache but does not generate a substantive completion.
- Apply `cache_control` to the reusable prompt prefix, especially the system prompt / stable context block, not to the placeholder user message.
- Claude prompt caching references the full prefix in order: `tools`, then `system`, then `messages`, up to and including the block marked with `cache_control`.
- The default ephemeral cache TTL is 5 minutes; Anthropic docs also describe a 1-hour TTL option (`ttl: "1h"`) where supported.
- For slow traffic, a timer or session-start hook may be needed to refresh the cache before expiry.
- Reported benchmark/social claim: around 52% faster first response for a 160k-token system prompt after pre-warming. Treat the exact percentage as benchmark/context dependent.

## Why it matters

Large agent systems often have massive repeated prefixes: operating contracts, tools, memory summaries, repo context, policies, or long task state. Without pre-warming, the first real request pays the full prefill latency tax. Cache pre-warming turns that tax into scheduled background work, which is especially useful for interactive agents, voice agents, and Hermes-style long-running contexts where the user perceives time-to-first-token.

## Canonical pattern

```python
client.messages.create(
    model="claude-opus-4-7",
    max_tokens=0,
    system=[{
        "type": "text",
        "text": BIG_SYSTEM_PROMPT,
        "cache_control": {"type": "ephemeral"},
    }],
    messages=[{"role": "user", "content": "warmup"}],
)
```

Critical placement rule:

```text
Put cache_control on the stable system/context block you want reused.
Do not put it only on the placeholder/warmup message, or you may cache the wrong prefix and miss on real requests.
```

## Operational recipe

1. Identify the stable prefix: tools, system prompt, shared memory/context, static examples, or other content that will be identical across real calls.
2. Add `cache_control: {"type": "ephemeral"}` to the last stable reusable block.
3. Send a warmup request with `max_tokens=0` and a placeholder user message.
4. Send the real request with the same prefix and the actual user task appended after the cached prefix.
5. Monitor usage fields / cache read-write metrics where available to verify the real call is hitting the cache.
6. Refresh before TTL expiry if traffic is sparse — default TTL is 5 minutes unless a longer supported TTL is configured.

## Self-OS / Hermes implications

- This is relevant to any Hermes or Self-OS path that uses Claude API directly with large system prompts, large tool schemas, or long durable memory/context blocks.
- It could be used as a session-start optimization: when a specialized agent profile starts, pre-warm the shared system prompt/profile/tools before the first real user request.
- It could be valuable for voice or WhatsApp/Telegram interactive UX where first-token latency is highly visible.
- It should be implemented only where the prefix is genuinely stable; if the warmup and real request differ before the cache breakpoint, the real request will miss.
- Cache pre-warming improves latency timing, not reasoning quality. It should be paired with existing verification and scope controls rather than treated as reliability by itself.

## Pitfalls

- Caching the placeholder instead of the stable system prompt creates the wrong cache breakpoint.
- Any change before or at the cache breakpoint produces a different cache key and misses.
- Very small prefixes may not benefit or may be below caching thresholds.
- Cache writes still cost money; pre-warming shifts latency earlier, it does not make the first cache write free.
- The 5-minute default TTL means low-traffic systems need an explicit refresh strategy.
- Automatic caching and explicit breakpoints can interact; Anthropic docs note limits around explicit breakpoints and TTL mismatches.

## User-supplied note

> How to speed up Claude's first API call  
> When your system prompt is massive, the first API call can really drag. The Anthropic Claude team shared a quick fix: send a throwaway request with “max_tokens=0” before your actual prompt. This caches your system prompt so the next real call hits a warm cache immediately. According to their benchmarks, this makes the first response about 52% faster for a 160k-token system prompt.
>
> ```python
> client.messages.create(
>     model="claude-opus-4-7",
>     max_tokens=0,
>     system=[{
>         "type": "text",
>         "text": BIG_SYSTEM_PROMPT,
>         "cache_control": {"type": "ephemeral"},
>     }],
>     messages=[{"role": "user", "content": "warmup"}],
> )
> ```
>
> Apply “cache_control” to the system prompt rather than the placeholder; otherwise, you'll cache the wrong data, and real requests will miss. Since the cache only lasts five minutes, set up a timer to re-trigger it if your traffic is slow.

## Verification / companion sources

- Anthropic Claude API docs: Prompt caching — https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Medium article summarizing Anthropic prompt cache pre-warming and reported benchmark ranges — https://medium.com/@AdithyaGiridharan/anthropic-is-quietly-building-an-inference-control-plane-prompt-cache-pre-warming-is-the-latest-f0b6a4b90919

## Extraction notes

This capture is based on the user-supplied note plus web verification against Anthropic’s prompt caching docs and a secondary article discussing Anthropic’s cache pre-warming announcement. The exact 52% figure is preserved as a reported benchmark claim and should be validated against Anthropic’s current docs/benchmarks before productizing.
