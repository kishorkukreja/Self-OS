---
status: processed
---
     1|---
     2|source: https://mitsloan.mit.edu/sites/default/files/inline-files/Unilever%20-%20Stephen%20and%20JJ.pdf
     3|date: 2026-04-26
     4|type: paper
     5|client: internal
     6|confidential: false
     7|tags: ["mit", "unilever", "demand-forecasting", "random-forest", "segmentation"]
     8|---
     9|
    10|# Demand Forecasting with a Segmented Approach
    11|
    12|**Source:** MIT Sloan School of Management (PDF)  
    13|**Team:** Unilever Team: Robert Morgan & RL Rosqueta; Program Mentor: Prof. Carine Simon; Jun Jie Ong (MBAn); Stephen C. Graves (Faculty Advisor)
    14|
    15|---
    16|
    17|## Problem Statement
    18|
    19|Retailers (Amazon & Walmart) order from Unilever cases of products (SKUs). Unilever needs to fulfil shipment orders within the average lead time of 4 weeks. The project forecasts shipments of cases of SKUs on a retailer level, with a model trained on rolling-based:
    20|- **1-week ahead forecast** for Amazon (fast-lane priority)
    21|- **4-week ahead forecast** for Walmart
    22|
    23|Forecasts generated through end of 2020.
    24|
    25|---
    26|
    27|## Data Overview
    28|
    29|Four datasets merged: Shipment, POS (Point of Sale), Inventory, and Promotions.
    30|
    31|| Retailer | Number of SKUs | Size of Data | Time Period |
    32|| --- | --- | --- | --- |
    33|| Amazon | 2949 | 80 weeks | 2018W01-2019W23 |
    34|| Walmart | 3369 | 105 weeks | 2017W11-2019W11 |
    35|
    36|SKUs with zero shipments were removed; missing weeks filled with 0.
    37|
    38|---
    39|
    40|## Volatility & Clustering Approach
    41|
    42|Given small training data per SKU, clustering increases training data and incorporates inter-SKU similarities.
    43|
    44|**Volatility indicators explored:**
    45|- Coefficient of Variation (2.4 for Amazon, 1.3 for Walmart)
    46|- Number of consecutive zero shipments
    47|- Average rate of shipment
    48|
    49|**Clustering method:** K-medoid clustering using inverse of dispersion factor (IOD) to separate product shipment time series.
    50|
    51|---
    52|
    53|## Model Selection: Random Forest
    54|
    55|Four models tested: Random Forest, Gradient Boosting, Linear Lasso Regression, Long-Short Term Memory RNN.
    56|
    57|Random Forest selected as main framework due to interpretability and performance.
    58|
    59|| Forecast Period | Unilever Current Accuracy | Random Forest Accuracy | Gradient Boosting Accuracy | Lasso Accuracy |
    60|| --- | --- | --- | --- | --- |
    61|| 1 week ahead | 35% | 55% | 40% | 36% |
    62|| 4 weeks ahead | N.A. | 32% | 26% | 25% |
    63|
    64|**Variable importance ranking:**
    65|1. Internal Shipment
    66|2. Retailer's Point of Sale
    67|3. Retailer's Inventory
    68|4. Retailer's Sale Price
    69|
    70|---
    71|
    72|## Cluster-While-Estimate Optimization
    73|
    74|Algorithm iteratively re-clusters SKUs for best accuracy in validation set.
    75|
    76|- Amazon: volatile ordering pattern requires immediate (1-week) and short-term (4-week) forecasts
    77|- Walmart: stable ordering pattern, 4-week lead time crucial for downstream demand planners
    78|
    79|---
    80|
    81|## Business Impact
    82|
    83|- **14%–20% increase in forecast accuracy** across all SKUs for Walmart and Amazon
    84|- **60% reduction** in demand planning time on forecasting processes
    85|- Expected improvement in service levels with customers
    86|
    87|