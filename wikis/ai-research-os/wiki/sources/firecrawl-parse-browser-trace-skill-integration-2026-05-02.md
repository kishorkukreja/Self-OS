---
title: "Firecrawl `/parse` and `/browser-trace` Skill Integration"
date_created: 2026-05-03
date_modified: 2026-05-03
summary: "Firecrawl /parse should be incorporated into Self OS/Hermes knowledge ingestion as an optional document parsing path for local or private files. It is especially useful for PDFs, DOCX, XLSX, and other document formats where preserving readi"
tags: [knowledge-ingest, firecrawl, document-parsing, browser-automation, observability, hermes-skills, self-os]
type: source
status: final
---

# Firecrawl `/parse` and `/browser-trace` Skill Integration

**Type:** resource
**Date:** 2026-05-02
**URL/Source:** https://docs.firecrawl.dev/features/parse; https://docs.firecrawl.dev/api-reference/endpoint/parse; https://www.firecrawl.dev/blog/introducing-parse; https://x.com/browserbase/status/2049218389957345686
**Raw file:** [[../raw/resources/firecrawl-parse-browser-trace-skill-integration-2026-05-02.md]]
**Concepts:** [[concepts/knowledge-ingest]], [[concepts/agent-web-extraction]], [[concepts/document-parsing]]
**Entities:** [[entities/firecrawl]], [[entities/self-os]]

## Summary

Firecrawl /parse should be incorporated into Self OS/Hermes knowledge ingestion as an optional document parsing path for local or private files. It is especially useful for PDFs, DOCX, XLSX, and other document formats where preserving reading order, tables, and agent readable Markdown/JSON matters. It should not replace the default web extract path for normal URLs; instead, it should be used when local/private document bytes are available or when document oriented extraction needs better fidelity. The /browser trace capability belongs in a separate browser automation observability/debugging skill rather than the normal ingest path. It is best used when browser driven extraction fails, when dynamic pages need debugging, or when a run needs a durable trace of network requests, DOM snapshots, screenshots, and CDP logs. This gives Self OS a cleaner ingestion stack: web extract remains the simple default for normal URLs. Firecrawl /parse becomes the high fidelity path for local/private documents and table heavy files. Firecrawl /scrape becomes the fallback for public document URLs when normal extraction is weak. /browser trace becomes a diagnostic layer for failed or complex browser automations. The result is better document fidelity without making every ingest depend on Firecrawl, and better browser debugging without polluting the normal raw wiki workflow with bulky trace files. Firecrawl /parse converts document files into LLM ready Markdown, JSON, HTML, links, images, or summaries. Supported inputs include PDFs, DOCX/DOC, ODT, RTF, XLSX/XLS, and HTML files. It is designed for local/private documents uploaded via multipart form data. Firecrawl recommends /scrape rather than /parse for public document URLs because public URLs can be auto detected and routed through the appropriate parsing engine. /parse supports files up to 50 MB and includes parser controls such as PDF modes: fast, auto, and ocr. It can preserve reading order and tables better than generic text extraction, making it valuable for reports, papers, spreadsheets, consulting decks, and industry documents. It requires FIRECRAWL API KEY; credentials must remain in environment/config and never be committed to the wiki. /browser trace is an observability/debugging layer for browser sessions, not a primary knowledge extraction tool. Browser trace outputs can be large and may contain sensitive page/network data, so traces should be stored deliberately and summarized before any long term wiki capture.

## Key takeaways

- Firecrawl /parse converts document files into LLM ready Markdown, JSON, HTML, links, images, or summaries.
- Supported inputs include PDFs, DOCX/DOC, ODT, RTF, XLSX/XLS, and HTML files.
- It is designed for local/private documents uploaded via multipart form data.
- Firecrawl recommends /scrape rather than /parse for public document URLs because public URLs can be auto detected and routed through the appropriate parsing engine.

## Compilation notes

Compiled from `raw/resources/firecrawl-parse-browser-trace-skill-integration-2026-05-02.md` during the 2026-05-03 wiki compile. The raw capture remains the canonical source for exact excerpts, links, and figures.
