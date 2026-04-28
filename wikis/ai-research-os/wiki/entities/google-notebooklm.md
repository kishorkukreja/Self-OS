---
title: "Google NotebookLM"
date_created: 2026-04-28
date_modified: 2026-04-28
summary: "Google's AI-powered research and note-taking tool that lets users upload sources, query them conversationally, and generate multi-modal Studio outputs including audio overviews, slide decks, and flashcards."
tags: [tool, google, notebooklm, research, ai, content-generation]
type: entity
status: final
---

# Google NotebookLM

**Type:** tool

**Description:** Google's AI-native research notebook that ingests documents, URLs, and Google Drive files, then enables users to chat with their sources, synthesise findings, and generate shareable artefacts via Studio buttons.

**Key facts:**
- Launched by Google Labs; built on Gemini models
- Supports multiple source types: PDFs, web pages, Google Docs/Slides, pasted text, and NotebookLM Deep Research
- **Studio outputs:** Data Table, Reports, Audio Overview, Slide Deck, Video Overview, Infographic, Flash Cards, Quiz
- Each notebook should be scoped to a single domain or persona to avoid cross-source confusion
- Can be accessed programmatically via the unofficial [[entities/notebooklm-py]] library
- Widely used for research synthesis, study preparation, marketing analysis, and design brief generation

**Relationships:** [[entities/notebooklm-py]], [[concepts/llm-knowledge-base]], [[concepts/persona-based-prompting]]

**Sources:** [[sources/notebooklm-py-repo]], [[sources/gencay-2026-notebooklm-personas]]

_Last updated: 2026-04-28_
