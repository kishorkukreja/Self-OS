---
source: https://mitsloan.mit.edu/sites/default/files/inline-files/Unilever%20-%20Stephen%20and%20JJ.pdf
date: 2026-04-26
type: paper
client: internal
confidential: false
tags: ["mit", "unilever", "demand-forecasting", "random-forest", "segmentation"]
---

# Demand Forecasting with a Segmented Approach

**Source:** MIT Sloan School of Management (PDF)  
**Team:** Unilever Team: Robert Morgan & RL Rosqueta; Program Mentor: Prof. Carine Simon; Jun Jie Ong (MBAn); Stephen C. Graves (Faculty Advisor)

---

## Problem Statement

Retailers (Amazon & Walmart) order from Unilever cases of products (SKUs). Unilever needs to fulfil shipment orders within the average lead time of 4 weeks. The project forecasts shipments of cases of SKUs on a retailer level, with a model trained on rolling-based:
- **1-week ahead forecast** for Amazon (fast-lane priority)
- **4-week ahead forecast** for Walmart

Forecasts generated through end of 2020.

---

## Data Overview

Four datasets merged: Shipment, POS (Point of Sale), Inventory, and Promotions.

| Retailer | Number of SKUs | Size of Data | Time Period |
| --- | --- | --- | --- |
| Amazon | 2949 | 80 weeks | 2018W01-2019W23 |
| Walmart | 3369 | 105 weeks | 2017W11-2019W11 |

SKUs with zero shipments were removed; missing weeks filled with 0.

---

## Volatility & Clustering Approach

Given small training data per SKU, clustering increases training data and incorporates inter-SKU similarities.

**Volatility indicators explored:**
- Coefficient of Variation (2.4 for Amazon, 1.3 for Walmart)
- Number of consecutive zero shipments
- Average rate of shipment

**Clustering method:** K-medoid clustering using inverse of dispersion factor (IOD) to separate product shipment time series.

---

## Model Selection: Random Forest

Four models tested: Random Forest, Gradient Boosting, Linear Lasso Regression, Long-Short Term Memory RNN.

Random Forest selected as main framework due to interpretability and performance.

| Forecast Period | Unilever Current Accuracy | Random Forest Accuracy | Gradient Boosting Accuracy | Lasso Accuracy |
| --- | --- | --- | --- | --- |
| 1 week ahead | 35% | 55% | 40% | 36% |
| 4 weeks ahead | N.A. | 32% | 26% | 25% |

**Variable importance ranking:**
1. Internal Shipment
2. Retailer's Point of Sale
3. Retailer's Inventory
4. Retailer's Sale Price

---

## Cluster-While-Estimate Optimization

Algorithm iteratively re-clusters SKUs for best accuracy in validation set.

- Amazon: volatile ordering pattern requires immediate (1-week) and short-term (4-week) forecasts
- Walmart: stable ordering pattern, 4-week lead time crucial for downstream demand planners

---

## Business Impact

- **14%–20% increase in forecast accuracy** across all SKUs for Walmart and Amazon
- **60% reduction** in demand planning time on forecasting processes
- Expected improvement in service levels with customers

