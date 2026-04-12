# nia-docs / agentsearch.sh

**Type:** tool

**Description:** A tool that mounts any documentation website as a Unix filesystem, letting AI agents browse docs with `cat`, `grep`, `tree`, and `find` — eliminating the need for RAG or per-tool MCP schemas.

**Key facts:**
- Usage: `npx nia-docs https://docs.example.com` — no API key, no install
- Accessible at https://www.agentsearch.sh/
- Works with Claude Code, Cursor, Copilot, Codex, Gemini CLI, OpenCode
- Namespaces are shared: index once, all users benefit
- Client-side bash shell using `just-bash` (TypeScript reimplementation)
- Caches at `~/.cache/nia-docs/`; cold index: 30-120s; cached: instant

**Relationships:** [[concepts/web-as-filesystem]]

**Sources:** [[sources/arlanr-web-as-filesystem-2026]]

_Last updated: 2026-04-12_
