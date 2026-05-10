---
source: weekly newsletter synthesis
date: 2026-05-10
type: newsletter-visual-plan
client: internal
confidential: false
tags: [supply-chain-signals, newsletter, visuals, charts, farm-to-fork]
status: draft
---

# Supply Chain Signals — 2026-W19 visuals plan

## Hero image prompt/spec

- Concept: "Farm to fork under energy pressure."
- Aspect ratio: 16:9 for Substack/LinkedIn hero; crop-safe center for social.
- Style: Technical-schematic infographic with baoyu `dense-modules`/`bento-grid` logic. Dark navy/graphite background, wheat and copper highlights, deep-green signal lines, crisp labels, no stock-photo people.
- Subject: Layered supply-chain map: farm inputs, fertilizer and fuel, crop production, storage, edible-oil processing, food manufacturing, packaging, cold chain, freight/customs, distribution center, retail shelf, consumer substitution. Overlay energy, biofuels, tariff, and freight-pressure nodes.
- Text guidance: Minimal text only: title plus 6-8 short labels. No invented figures.
- Mood: Executive, technical, slightly urgent; no disaster imagery.
- Where it fits: Top of Substack draft and LinkedIn Post 2.
- Production note: Generate as SVG/Mermaid/Excalidraw-style diagram or with configured Hermes image backend if later requested. Do not create actual image in this run.
- Alt text: Systems map of the food supply chain from farm inputs to retail shelves, with highlighted bottlenecks in energy, fertilizer, processing, cold chain, freight, and consumer substitution.
- Caption: Food-price pressure moves through the whole chain, from the commodity quote to the shelf.

## Chart candidate 1 — ISM manufacturing squeeze metric card

- Claim: U.S. manufacturing expanded in April, but prices and supplier deliveries worsened.
- Data table:

| Metric | April 2026 | Unit | Interpretation |
|---|---:|---|---|
| Manufacturing PMI | 52.7 | diffusion index | Expansion |
| Prices | 84.6 | diffusion index | Four-year high |
| Supplier Deliveries | 60.6 | diffusion index | Slower deliveries; slowest since May 2022 |
| Employment | 46.4 | diffusion index | Contraction |
| Customers' Inventories | 39.1 | diffusion index | Too low |

- Source URL: https://www.ismworld.org/supply-management-news-and-reports/news-publications/inside-supply-management-magazine/blog/2026/2026-05/ism-pmi-reports-roundup-april-2026-manufacturing/
- Recommended chart type: Metric-card strip or lollipop chart.
- Caveat: ISM diffusion indexes show breadth/direction, not physical volume.
- Production note: Local Python/Matplotlib or simple SVG.
- Alt text: Five ISM metric cards showing PMI 52.7, Prices 84.6, Supplier Deliveries 60.6, Employment 46.4, and Customers' Inventories 39.1.
- Caption: The headline PMI is stable; the cost and delivery internals are not.

## Chart candidate 2 — FAO food and energy pass-through

- Claim: Global food prices rose for a third month, led by vegetable oils.
- Data table:

| Metric | April 2026 | Change | Unit |
|---|---:|---:|---|
| FAO Food Price Index | 130.7 | +1.6% m/m | index points |
| Cereal Price Index | 111.3 | +0.8% m/m | index points |
| Vegetable Oil Price Index | 193.9 | +5.9% m/m | index points |
| FFPI vs March 2022 peak | n/a | -18.4% | percent |

- Source URL: https://www.fao.org/worldfoodsituation/foodpricesindex/en/
- Recommended chart type: Small bar chart of April index values plus annotations for month-over-month changes.
- Caveat: Meat index may contain projected prices and can be revised; use FAO notes.
- Production note: Local Python/Matplotlib.
- Alt text: Bar chart comparing FAO Food Price Index, Cereal Price Index, and Vegetable Oil Price Index for April 2026.
- Caption: Energy and biofuels pressure showed up most clearly in vegetable oils.

## Chart candidate 3 — WTO trade growth forecast

- Claim: WTO expects merchandise trade growth to slow in 2026, with oil downside and AI-goods upside pulling in opposite directions.
- Data table:

| Scenario / year | Merchandise trade volume growth |
|---|---:|
| 2025 actual/estimate | 4.6% |
| 2026 baseline | 1.9% |
| 2026 high-oil downside | 1.4% |
| 2027 baseline | 2.6% |

- Source URL: https://www.wto.org/english/res_e/booksp_e/gtos0326_e.pdf
- Recommended chart type: Simple line + scenario marker.
- Caveat: WTO forecast with data cutoff 2026-03-10; subject to revision.
- Production note: Local Python/Matplotlib.
- Alt text: Line chart showing merchandise trade growth falling from 4.6% in 2025 to a 1.9% baseline in 2026, with a 1.4% high-oil downside marker and 2.6% 2027 forecast.
- Caption: Trade growth slows just as oil risk and AI-related goods pull the forecast in different directions.

## Diagram candidate — Farm-to-Fork constraint map

- Purpose: Qualitative fallback if charts feel too metric-heavy.
- Structure: Left-to-right systems map: inputs → farm production → storage → processing → packaging → cold chain → freight/distribution → retail/foodservice → consumer. Add constraint overlays for energy, fertilizer, biofuels, tariffs, freight, and price elasticity. Each overlay has fields: signal, decision, owner, deadline.
- Production note: Mermaid/Excalidraw/SVG. Good for carousel cards 4-5 and PPT slide 4.
- Alt text: Supply-chain diagram showing the path from farm inputs to consumer shelves, with constraint markers for energy, fertilizer, processing, packaging, freight, and retail demand.
- Caption: Farm to Fork is a moving-constraint chain: the bottleneck can shift from fuel to processing to freight to the shelf.

## Diagram candidate — live constraint map

- Purpose: Use when the piece needs the broader operating model rather than the food-specific chain.
- Structure: Hub-and-spoke: current business plan in the center; spokes for material, duty, energy, freight, capacity, supplier qualification, cash, and customer promise. Each spoke has fields: signal, decision, owner, deadline.
- Production note: Mermaid/Excalidraw/SVG. Good for carousel card 7 and PPT slide 6.
- Alt text: Hub-and-spoke diagram showing a supply-chain operating plan surrounded by eight possible constraints, each tied to a decision owner and deadline.
- Caption: A live constraint map turns visibility into an operating decision.
