---
status: processed
---
# GitReverse

**URL:** https://github.com/filiksyos/gitreverse  
**Live:** https://gitreverse.com  
**License:** Unspecified  
**Stars:** 760 | **Forks:** 144 | **Contributors:** 4  
**Language:** TypeScript (99.3%)

## Overview

> Reverse engineer any repo into its original prompt

A web tool that turns any **public GitHub repository** into a **single synthetic user prompt** designed for AI coding assistants (Cursor, Claude Code, Codex, etc.) to recreate the project from scratch.

## How It Works

The app extracts:
1. **Repo metadata**
2. **Root file tree** (depth 1)
3. **README**

Then uses an **LLM via OpenRouter** to synthesize one short, conversational prompt grounded in that context.

## Usage

- **Home page:** Paste a GitHub URL or `owner/repo` string.
- **Shareable links:** Navigate directly to `/owner/repo` (e.g., `/vercel/next.js`).
- **Tree URL redirect:** GitHub-style `/owner/repo/tree/...` URLs automatically redirect to `/owner/repo`.

## Tech Stack

Next.js (App Router), React, TypeScript, Tailwind CSS, GitHub API, OpenRouter.

## Configuration

Copy `.env.example` to `.env.local`.

**Required:**
```bash
OPENROUTER_API_KEY=your_key_here
```

**Optional:**
- `OPENROUTER_MODEL` — defaults to `google/gemini-2.5-pro`
- `GITHUB_TOKEN` — improves GitHub API rate limits
- Supabase env vars — enables server-side caching

### Custom Reverse (Deep/Focus Prompts)

For deeper reverse-engineering, run the separate **`custom_reverse`** TypeScript service locally:

```bash
# Inside custom_reverse project
pnpm dev   # default port 3001
```

Then in `.env.local`:
```bash
CUSTOM_REVERSE_SERVICE_URL=http://localhost:3001
```

- Enable **Custom reverse** on the homepage and describe what to reverse-engineer.
- Successful runs are cached in Supabase.

## Development

```bash
pnpm install
pnpm dev      # http://localhost:3000
pnpm build
pnpm start
pnpm lint
```

## Credits

Shout out to [GitIngest](http://github.com/coderamp-labs/gitingest) for inspiration.

## Why It Matters

GitReverse solves the "how did they build this?" problem by turning any public repo into a vibe-coding prompt. Useful for learning patterns, bootstrapping similar projects, or understanding architecture quickly. The OpenRouter integration means it works with many models.

## Tags

- reverse-engineering
- prompt-generation
- repo-analysis
- openrouter
- nextjs
- cursor
- claude-code
- codex
