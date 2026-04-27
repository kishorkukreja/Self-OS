---
status: processed
---
     1|---
     2|source: https://aws.amazon.com/blogs/industries/improve-demand-forecasting-to-boost-sales-on-amazon/
     3|date: 2026-04-26
     4|type: article
     5|client: internal
     6|confidential: false
     7|tags: ["aws", "amazon", "cpg", "demand-forecasting", "vendor-central"]
     8|---
     9|
    10|# CPG Companies: Improve Demand Forecasting to Boost Sales on Amazon
    11|
    12|**Source:** [AWS for Industries Blog](https://aws.amazon.com/blogs/industries/improve-demand-forecasting-to-boost-sales-on-amazon/)
    13|
    14|## Executive Summary
    15|
    16|AWS enables CPG companies to **automate ingestion of Amazon purchase order (PO) data** and apply machine learning (via **Amazon Forecast**) to generate forward-looking, fine-grained, time-series demand forecasts directly within their own environments. This helps 1P vendors improve **on-time, in-full (OTIF) performance**, reduce chargebacks, and maximize revenue by ensuring high-velocity SKUs remain in stock.
    17|
    18|---
    19|
    20|## Selling Models on Amazon
    21|
    22|| Model | Process | Inventory Owner |
    23||-------|---------|-----------------|
    24|| **First-Party (1P)** | Amazon purchases goods via POs and warehouses inventory in regional fulfillment centers based on expected consumer demand. | Amazon |
    25|| **Third-Party (3P)** | Sellers sell directly to consumers, set retail prices, and manage inventory/shipping/returns. May use **Fulfillment by Amazon (FBA)** for warehouse operations. | Selling Partner |
    26|
    27|> **Core Objective:** Regardless of model, success depends on ensuring desired products are available and in stock.
    28|
    29|---
    30|
    31|## The Challenge: OTIF & Demand Forecasting
    32|
    33|For 1P vendors, Amazon sends electronic POs specifying quantities, SKUs, delivery dates, and delivery points. Once accepted, manufacturers are obligated to meet these terms. This requires:
    34|
    35|- Ample lead time to **plan, manufacture, and stock** products
    36|- Reliable, ML-driven data insights to **accurately forecast variable demand**
    37|
    38|> **According to McKinsey & Company:**
    39|> "Online sales of consumer packaged goods have soared during the pandemic … and the trend shows no signs of fading. McKinsey’s consumer sentiment surveys reveal that US consumers plan to continue spending more of their money online even after the COVID-19 crisis subsides."
    40|
    41|---
    42|
    43|## The Solution: Amazon Forecast & Automated Data Architecture
    44|
    45|### Amazon's Forecasting Evolution
    46|Amazon developed its forecasting capabilities over a decade-plus journey:
    47|- **Phase 1:** Rules-based statistical forecasts
    48|- **Phase 2:** Machine learning algorithms
    49|- **Phase 3:** Deep learning algorithms for diverse product categories
    50|
    51|**Amazon Forecast** is the resulting fully managed cloud service available to AWS customers. It requires **no deep expertise** in time-series forecasting or ML.
    52|
    53|### Automated Architecture
    54|Many 1P vendors manually collect forecasting data. The reference architecture automates this by using **vended APIs** to programmatically source from **Amazon Vendor Central**:
    55|
    56|- Historical and current PO data
    57|- Product catalog data
    58|- Diagnostic reports (to understand actual demand)
    59|
    60|Instead of manual collection and point forecasts, the solution:
    61|
    62|- **Predicts demand** for variable vendor POs weeks ahead
    63|- Generates **probabilistic forecasts** (not point forecasts)
    64|- Matches correct probabilistic forecasts to **Class A, Class B, and Class C SKUs**
    65|
    66|---
    67|
    68|## Key Business Benefits
    69|
    70|- **Import Amazon PO Data:** Better access, governance, and seamless sharing across the organization
    71|- **Increase Forecast Accuracy:** ML-powered probabilistic forecasts predict variable PO demand weeks in advance
    72|- **Track Product Changes:** Monitor weight/dimension changes to ensure adherence to manufacturer standards
    73|- **Reduce OTIF Penalties:** Improve OTIF metrics to enhance organic Amazon.com ranking and reduce chargeback expenses
    74|- **Ensure High-Velocity SKUs Are In Stock:** Match probabilistic forecasts to SKU sales velocity to prevent stockouts and improve revenue
    75|
    76|---
    77|
    78|## Call to Action
    79|
    80|Accurate weekly demand forecasting improves outcomes at both the **top and bottom lines**.
    81|
    82|**Ready to automate forecasting?** [Contact your AWS account team](https://pages.awscloud.com/GLOBAL-other-IND-CPG-Contact-Us-2021.html) to get started.
    83|
    84|