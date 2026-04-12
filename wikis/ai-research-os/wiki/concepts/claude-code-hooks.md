# Claude Code Hooks

**Definition:** Shell commands configured in Claude Code's `settings.json` that execute automatically at lifecycle events — session start, session end, pre-compact, and tool use — enabling automated knowledge capture and context loading.

**Why it matters:** Hooks are the mechanism that makes self-evolving agent memory practical. Without hooks, extracting session knowledge requires manual action. With hooks, every session automatically loads context on start and files insights on end — the bookkeeping is invisible.

**Key hooks:**
- **session-start:** Load `agents.md` (system description) and `wiki/index.md` (knowledge map) so the agent begins with full context
- **session-end:** Call Claude Agent SDK to summarise the session transcript into a daily log entry
- **pre-compact:** Same as session-end, triggered before context compaction instead of session close
- **tool-use / post-tool:** Custom logic after specific tool calls (e.g., after write → note the change)

**Implementation pattern (Cole Medin):**
1. session-start hook → Python script loads agents.md + wiki/index.md
2. session-end / pre-compact → Python script calls Agent SDK with transcript → daily log file
3. Daily flush process (scheduled) → Agent SDK promotes logs → wiki concepts/connections
4. wiki/index.md always current → agent navigates by file tree, no RAG needed

**Related:** [[wiki-agent-memory]], [[raw-wiki-pattern]], [[entities/claude-code]]

**Sources:** [[sources/cole-medin-self-evolving-claude-memory-2026]], [[sources/hooeem-extend-claude-sessions-2026]]

_Last updated: 2026-04-12_
