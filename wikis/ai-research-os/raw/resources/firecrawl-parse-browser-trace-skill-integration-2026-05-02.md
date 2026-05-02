---
source: https://docs.firecrawl.dev/features/parse; https://docs.firecrawl.dev/api-reference/endpoint/parse; https://www.firecrawl.dev/blog/introducing-parse; https://x.com/browserbase/status/2049218389957345686
date: 2026-05-02
type: resource
tags: [knowledge-ingest, firecrawl, document-parsing, browser-automation, observability, hermes-skills, self-os]
---

# Firecrawl `/parse` and `/browser-trace` Skill Integration

## Summary

Firecrawl `/parse` should be incorporated into Self-OS/Hermes knowledge ingestion as an optional document parsing path for local or private files. It is especially useful for PDFs, DOCX, XLSX, and other document formats where preserving reading order, tables, and agent-readable Markdown/JSON matters. It should not replace the default `web_extract` path for normal URLs; instead, it should be used when local/private document bytes are available or when document-oriented extraction needs better fidelity.

The `/browser-trace` capability belongs in a separate browser automation observability/debugging skill rather than the normal ingest path. It is best used when browser-driven extraction fails, when dynamic pages need debugging, or when a run needs a durable trace of network requests, DOM snapshots, screenshots, and CDP logs.

## Key points

- Firecrawl `/parse` converts document files into LLM-ready Markdown, JSON, HTML, links, images, or summaries.
- Supported inputs include PDFs, DOCX/DOC, ODT, RTF, XLSX/XLS, and HTML files.
- It is designed for local/private documents uploaded via multipart form data.
- Firecrawl recommends `/scrape` rather than `/parse` for public document URLs because public URLs can be auto-detected and routed through the appropriate parsing engine.
- `/parse` supports files up to 50 MB and includes parser controls such as PDF modes: `fast`, `auto`, and `ocr`.
- It can preserve reading order and tables better than generic text extraction, making it valuable for reports, papers, spreadsheets, consulting decks, and industry documents.
- It requires `FIRECRAWL_API_KEY`; credentials must remain in environment/config and never be committed to the wiki.
- `/browser-trace` is an observability/debugging layer for browser sessions, not a primary knowledge extraction tool.
- Browser trace outputs can be large and may contain sensitive page/network data, so traces should be stored deliberately and summarized before any long-term wiki capture.

## Recommended Self-OS routing

### Default URL ingest

Keep the current default behavior:

1. Use Hermes `web_extract` first.
2. If `web_extract` works, do not switch tools.
3. For X/Twitter or dynamic sites where `web_extract` fails, use browser extraction.
4. Save the raw source under the appropriate Self-OS wiki folder and commit to `master`.

### Public document URL

For public PDFs, DOCX files, spreadsheets, and similar document URLs:

1. Try `web_extract` first.
2. If extraction is empty, truncated, or loses tables, use Firecrawl `/scrape` rather than `/parse`.
3. Save the extracted Markdown as raw wiki source with a note on extraction method.

### Local or private document file

For local/private documents where file bytes are available:

1. Use Firecrawl `/parse` if `FIRECRAWL_API_KEY` is configured.
2. Request Markdown by default.
3. Request JSON with a schema when the user wants structured extraction.
4. Use PDF `mode: auto` by default, and `mode: ocr` for scanned PDFs.
5. Fall back to local tools such as `pymupdf`, `pandoc`, `libreoffice --headless`, `python-docx`, or `openpyxl` if Firecrawl is unavailable.

Example pattern:

```bash
curl -s -X POST https://api.firecrawl.dev/v2/parse \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -F "file=@/absolute/path/to/document.pdf" \
  -F 'options={"formats":["markdown"],"parsers":[{"type":"pdf","mode":"auto"}]};type=application/json'
```

Structured extraction pattern:

```bash
curl -s -X POST https://api.firecrawl.dev/v2/parse \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -F "file=@/absolute/path/to/document.pdf" \
  -F 'options={"formats":["markdown",{"type":"json","schema":{"type":"object","properties":{"title":{"type":"string"},"key_findings":{"type":"array","items":{"type":"string"}}}}}]};type=application/json'
```

## Skill changes already made

The Hermes skill `knowledge-base-operations` was updated in:

`references/knowledge-ingest.md`

The fallback table now includes Firecrawl `/parse` for local/private PDFs, DOCX, DOC, ODT, RTF, XLSX, XLS, and HTML files. It also distinguishes public document URLs, which should use `web_extract` first and Firecrawl `/scrape` as the stronger fallback.

## `/browser-trace` integration recommendation

`/browser-trace` should become a separate debugging/observability skill rather than being embedded directly in normal knowledge ingest.

Use it when:

- Browser extraction fails or produces incomplete content.
- A page is highly dynamic and depends on network/API calls.
- We need evidence for why an automation run failed.
- We need to inspect network requests, DOM changes, screenshots, or CDP logs.
- We are debugging Stagehand, Playwright, Browserbase, or Hermes browser sessions.

Suggested storage pattern:

- Ephemeral traces: `/tmp/browser-traces/YYYY-MM-DD-HHMMSS/`
- Retained operational traces: `/data/Self-OS/ops/browser-traces/YYYY-MM-DD/{slug}/`
- Wiki capture: summarize the trace findings, but do not commit large raw traces by default.

## Why it matters

This gives Self-OS a cleaner ingestion stack:

- `web_extract` remains the simple default for normal URLs.
- Firecrawl `/parse` becomes the high-fidelity path for local/private documents and table-heavy files.
- Firecrawl `/scrape` becomes the fallback for public document URLs when normal extraction is weak.
- `/browser-trace` becomes a diagnostic layer for failed or complex browser automations.

The result is better document fidelity without making every ingest depend on Firecrawl, and better browser debugging without polluting the normal raw wiki workflow with bulky trace files.

## Raw implementation note

As of 2026-05-02, `FIRECRAWL_API_KEY` is configured in the Hermes environment. The secret value is intentionally not included here.
