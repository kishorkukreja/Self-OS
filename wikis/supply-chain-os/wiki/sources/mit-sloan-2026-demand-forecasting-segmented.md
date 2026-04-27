---
title: "MIT Sloan: Demand Forecasting with a Segmented Approach"
date_created: 2026-04-27
date_modified: 2026-04-27
summary: "MIT Sloan study with Unilever demonstrating a 14–20% forecast-accuracy improvement by clustering SKUs via K-medoid and applying random-forest models segmented by retailer volatility."
tags: ["mit-sloan", "unilever", "demand-forecasting", "random-forest", "segmentation", "amazon", "walmart"]
type: source
status: final
client: internal
confidential: false
---

# MIT Sloan: Demand Forecasting with a Segmented Approach

**Type:** paper  
**Date:** 2026-04-26  
**Client:** internal  
**Confidential:** false  
**Raw file:** [[../raw/papers/2026-04-26-mit-sloan-unilever-demand-forecasting-segmented.md]]

**Summary:** An MIT Sloan team partnered with [[entities/unilever.md|Unilever]] to build a demand-forecasting framework for retailer-level shipment orders. Because per-SKU training data was limited, the team clustered SKUs using K-medoid on inverse dispersion factor (IOD), then trained a [[concepts/demand-forecasting.md|random-forest]] model. The approach raised forecast accuracy from 35% to 55% for Amazon (1-week ahead) and from N.A. to 32% for Walmart (4-week ahead), while cutting demand-planning time by 60%.

**Key takeaways:**
- Clustering increases effective training data and surfaces inter-SKU similarities.
- Variable importance ranked internal shipment, POS, inventory, and sale price as top predictors.
- A “cluster-while-estimate” loop iteratively re-clusters SKUs to optimize validation accuracy.
- The 14–20% accuracy lift and 60% planning-time reduction show strong business impact.
