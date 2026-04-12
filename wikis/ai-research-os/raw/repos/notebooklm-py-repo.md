---
title: "teng-lin/notebooklm-py: Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw."
source: "https://github.com/teng-lin/notebooklm-py"
author:
published:
created: 2026-04-12
description: "Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw. - teng-lin/notebooklm-py"
tags:
  - "clippings"
status: processed
---
## notebooklm-py

[![notebooklm-py logo](https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/notebooklm-py.png)](https://raw.githubusercontent.com/teng-lin/notebooklm-py/main/notebooklm-py.png)

**A Comprehensive NotebookLM Skill & Unofficial Python API.** Full programmatic access to NotebookLM's features—including capabilities the web UI doesn't expose—via Python, CLI, and AI agents like Claude Code, Codex, and OpenClaw.

[![teng-lin%2Fnotebooklm-py | Trendshift](https://camo.githubusercontent.com/ad991c0830efe90339cf1eb4261e6a75327387d2ce1306f6e776415b8699baa2/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3139313136)](https://trendshift.io/repositories/19116)

**Source & Development**: [https://github.com/teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)

> **⚠️ Unofficial Library - Use at Your Own Risk**
> 
> This library uses **undocumented Google APIs** that can change without notice.
> 
> - **Not affiliated with Google** - This is a community project
> - **APIs may break** - Google can change internal endpoints anytime
> - **Rate limits apply** - Heavy usage may be throttled
> 
> Best for prototypes, research, and personal projects. See [Troubleshooting](https://github.com/teng-lin/notebooklm-py/blob/main/docs/troubleshooting.md) for debugging tips.

## What You Can Build

🤖 **AI Agent Tools** - Integrate NotebookLM into Claude Code, Codex, and other LLM agents. Ships with a root [NotebookLM skill](https://github.com/teng-lin/notebooklm-py/blob/main/SKILL.md) for GitHub and `npx skills add` discovery, local `notebooklm skill install` support for Claude Code and `.agents` skill directories, and repo-level Codex guidance in [`AGENTS.md`](https://github.com/teng-lin/notebooklm-py/blob/main/AGENTS.md).

📚 **Research Automation** - Bulk-import sources (URLs, PDFs, YouTube, Google Drive), run web/Drive research queries with auto-import, and extract insights programmatically. Build repeatable research pipelines.

🎙️ **Content Generation** - Generate Audio Overviews (podcasts), videos, slide decks, quizzes, flashcards, infographics, data tables, mind maps, and study guides. Full control over formats, styles, and output.

📥 **Downloads & Export** - Download all generated artifacts locally (MP3, MP4, PDF, PNG, CSV, JSON, Markdown). Export to Google Docs/Sheets. **Features the web UI doesn't offer**: batch downloads, quiz/flashcard export in multiple formats, mind map JSON extraction.

## Three Ways to Use

| Method | Best For |
| --- | --- |
| **Python API** | Application integration, async workflows, custom pipelines |
| **CLI** | Shell scripts, quick tasks, CI/CD automation |
| **Agent Integration** | Claude Code, Codex, LLM agents, natural language automation |

## Features

### Complete NotebookLM Coverage

| Category | Capabilities |
| --- | --- |
| **Notebooks** | Create, list, rename, delete |
| **Sources** | URLs, YouTube, files (PDF, text, Markdown, Word, audio, video, images), Google Drive, pasted text; refresh, get guide/fulltext |
| **Chat** | Questions, conversation history, custom personas |
| **Research** | Web and Drive research agents (fast/deep modes) with auto-import |
| **Sharing** | Public/private links, user permissions (viewer/editor), view level control |

### Content Generation (All NotebookLM Studio Types)

| Type | Options | Download Format |
| --- | --- | --- |
| **Audio Overview** | 4 formats (deep-dive, brief, critique, debate), 3 lengths, 50+ languages | MP3/MP4 |
| **Video Overview** | 3 formats (explainer, brief, cinematic), 9 visual styles, plus a dedicated `cinematic-video` CLI alias | MP4 |
| **Slide Deck** | Detailed or presenter format, adjustable length; individual slide revision | PDF, PPTX |
| **Infographic** | 3 orientations, 3 detail levels | PNG |
| **Quiz** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Flashcards** | Configurable quantity and difficulty | JSON, Markdown, HTML |
| **Report** | Briefing doc, study guide, blog post, or custom prompt | Markdown |
| **Data Table** | Custom structure via natural language | CSV |
| **Mind Map** | Interactive hierarchical visualization | JSON |

### Beyond the Web UI

These features are available via API/CLI but not exposed in NotebookLM's web interface:

- **Batch downloads** - Download all artifacts of a type at once
- **Quiz/Flashcard export** - Get structured JSON, Markdown, or HTML (web UI only shows interactive view)
- **Mind map data extraction** - Export hierarchical JSON for visualization tools
- **Data table CSV export** - Download structured tables as spreadsheets
- **Slide deck as PPTX** - Download editable PowerPoint files (web UI only offers PDF)
- **Slide revision** - Modify individual slides with natural-language prompts
- **Report template customization** - Append extra instructions to built-in format templates
- **Save chat to notes** - Save Q&A answers or conversation history as notebook notes
- **Source fulltext access** - Retrieve the indexed text content of any source
- **Programmatic sharing** - Manage permissions without the UI

## Installation

```
# Basic installation
pip install notebooklm-py

# With browser login support (required for first-time setup)
pip install "notebooklm-py[browser]"
playwright install chromium
```

If `playwright install chromium` fails with `TypeError: onExit is not a function`, see the Linux workaround in [Troubleshooting](https://github.com/teng-lin/notebooklm-py/blob/main/docs/troubleshooting.md#linux).

### Development Installation

For contributors or testing unreleased features:

```
pip install git+https://github.com/teng-lin/notebooklm-py@main
```

⚠️ The main branch may contain unstable changes. Use PyPI releases for production.

## Quick Start

[![](https://camo.githubusercontent.com/c1bd46cd6c3edb20a9566e406345f0344f9b33975194eff49197ea8b34ba0019/68747470733a2f2f61736369696e656d612e6f72672f612f3736373238342e737667)](https://asciinema.org/a/767284)  
*16-minute session compressed to 30 seconds*

### CLI

```
# 1. Authenticate (opens browser)
notebooklm login
# Or use Microsoft Edge (for orgs that require Edge for SSO)
# notebooklm login --browser msedge

# 2. Create a notebook and add sources
notebooklm create "My Research"
notebooklm use <notebook_id>
notebooklm source add "https://en.wikipedia.org/wiki/Artificial_intelligence"
notebooklm source add "./paper.pdf"

# 3. Chat with your sources
notebooklm ask "What are the key themes?"

# 4. Generate content
notebooklm generate audio "make it engaging" --wait
notebooklm generate video --style whiteboard --wait
notebooklm generate cinematic-video "documentary-style summary" --wait
notebooklm generate quiz --difficulty hard
notebooklm generate flashcards --quantity more
notebooklm generate slide-deck
notebooklm generate infographic --orientation portrait
notebooklm generate mind-map
notebooklm generate data-table "compare key concepts"

# 5. Download artifacts
notebooklm download audio ./podcast.mp3
notebooklm download video ./overview.mp4
notebooklm download cinematic-video ./documentary.mp4
notebooklm download quiz --format markdown ./quiz.md
notebooklm download flashcards --format json ./cards.json
notebooklm download slide-deck ./slides.pdf
notebooklm download infographic ./infographic.png
notebooklm download mind-map ./mindmap.json
notebooklm download data-table ./data.csv
```

Other useful CLI commands:

```
notebooklm auth check --test         # Diagnose auth/cookie issues
notebooklm agent show codex          # Print bundled Codex instructions
notebooklm agent show claude         # Print bundled Claude Code skill template
notebooklm language list             # List supported output languages
notebooklm metadata --json           # Export notebook metadata and sources
notebooklm share status              # Inspect sharing state
notebooklm source add-research "AI"  # Start web research and import sources
notebooklm skill status              # Check local agent skill installation
```

### Python API

```
import asyncio
from notebooklm import NotebookLMClient

async def main():
    async with await NotebookLMClient.from_storage() as client:
        # Create notebook and add sources
        nb = await client.notebooks.create("Research")
        await client.sources.add_url(nb.id, "https://example.com", wait=True)

        # Chat with your sources
        result = await client.chat.ask(nb.id, "Summarize this")
        print(result.answer)

        # Generate content (podcast, video, quiz, etc.)
        status = await client.artifacts.generate_audio(nb.id, instructions="make it fun")
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_audio(nb.id, "podcast.mp3")

        # Generate quiz and download as JSON
        status = await client.artifacts.generate_quiz(nb.id)
        await client.artifacts.wait_for_completion(nb.id, status.task_id)
        await client.artifacts.download_quiz(nb.id, "quiz.json", output_format="json")

        # Generate mind map and export
        result = await client.artifacts.generate_mind_map(nb.id)
        await client.artifacts.download_mind_map(nb.id, "mindmap.json")

asyncio.run(main())
```

### Agent Setup

**Option 1 — CLI install**:

```
notebooklm skill install
```

Installs the skill into `~/.claude/skills/notebooklm` and `~/.agents/skills/notebooklm`.

**Option 2 — `npx` install** (via the open skills ecosystem):

```
npx skills add teng-lin/notebooklm-py
```

Fetches the canonical [SKILL.md](https://github.com/teng-lin/notebooklm-py/blob/main/SKILL.md) directly from GitHub.

## Documentation

- **[CLI Reference](https://github.com/teng-lin/notebooklm-py/blob/main/docs/cli-reference.md)** - Complete command documentation
- **[Python API](https://github.com/teng-lin/notebooklm-py/blob/main/docs/python-api.md)** - Full API reference
- **[Configuration](https://github.com/teng-lin/notebooklm-py/blob/main/docs/configuration.md)** - Storage and settings
- **[Release Guide](https://github.com/teng-lin/notebooklm-py/blob/main/docs/releasing.md)** - Release checklist and packaging verification
- **[Troubleshooting](https://github.com/teng-lin/notebooklm-py/blob/main/docs/troubleshooting.md)** - Common issues and solutions
- **[API Stability](https://github.com/teng-lin/notebooklm-py/blob/main/docs/stability.md)** - Versioning policy and stability guarantees

### For Contributors

- **[Development Guide](https://github.com/teng-lin/notebooklm-py/blob/main/docs/development.md)** - Architecture, testing, and releasing
- **[RPC Development](https://github.com/teng-lin/notebooklm-py/blob/main/docs/rpc-development.md)** - Protocol capture and debugging
- **[RPC Reference](https://github.com/teng-lin/notebooklm-py/blob/main/docs/rpc-reference.md)** - Payload structures
- **[Changelog](https://github.com/teng-lin/notebooklm-py/blob/main/CHANGELOG.md)** - Version history and release notes
- **[Security](https://github.com/teng-lin/notebooklm-py/blob/main/SECURITY.md)** - Security policy and credential handling

## Platform Support

| Platform | Status | Notes |
| --- | --- | --- |
| **macOS** | ✅ Tested | Primary development platform |
| **Linux** | ✅ Tested | Fully supported |
| **Windows** | ✅ Tested | Tested in CI |

## Star History

[![Star History Chart](https://camo.githubusercontent.com/663afd6f3c31d95a66bca6d5549a66c8f23c3fb9e9516b4d95a84c6d9eb6c993/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f696d6167653f7265706f733d74656e672d6c696e2f6e6f7465626f6f6b6c6d2d707926747970653d74696d656c696e65266c6567656e643d746f702d6c656674)](https://www.star-history.com/?repos=teng-lin%2Fnotebooklm-py&type=timeline&legend=top-left)

## License

MIT License. See [LICENSE](https://github.com/teng-lin/notebooklm-py/blob/main/LICENSE) for details.