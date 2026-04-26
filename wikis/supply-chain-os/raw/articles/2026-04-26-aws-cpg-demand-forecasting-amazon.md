---
source: https://aws.amazon.com/blogs/industries/improve-demand-forecasting-to-boost-sales-on-amazon/
date: 2026-04-26
type: article
client: internal
confidential: false
tags: ["aws", "amazon", "cpg", "demand-forecasting", "vendor-central"]
---

# CPG Companies: Improve Demand Forecasting to Boost Sales on Amazon

**Source:** [AWS for Industries Blog](https://aws.amazon.com/blogs/industries/improve-demand-forecasting-to-boost-sales-on-amazon/)

## Executive Summary

AWS enables CPG companies to **automate ingestion of Amazon purchase order (PO) data** and apply machine learning (via **Amazon Forecast**) to generate forward-looking, fine-grained, time-series demand forecasts directly within their own environments. This helps 1P vendors improve **on-time, in-full (OTIF) performance**, reduce chargebacks, and maximize revenue by ensuring high-velocity SKUs remain in stock.

---

## Selling Models on Amazon

| Model | Process | Inventory Owner |
|-------|---------|-----------------|
| **First-Party (1P)** | Amazon purchases goods via POs and warehouses inventory in regional fulfillment centers based on expected consumer demand. | Amazon |
| **Third-Party (3P)** | Sellers sell directly to consumers, set retail prices, and manage inventory/shipping/returns. May use **Fulfillment by Amazon (FBA)** for warehouse operations. | Selling Partner |

> **Core Objective:** Regardless of model, success depends on ensuring desired products are available and in stock.

---

## The Challenge: OTIF & Demand Forecasting

For 1P vendors, Amazon sends electronic POs specifying quantities, SKUs, delivery dates, and delivery points. Once accepted, manufacturers are obligated to meet these terms. This requires:

- Ample lead time to **plan, manufacture, and stock** products
- Reliable, ML-driven data insights to **accurately forecast variable demand**

> **According to McKinsey & Company:**
> "Online sales of consumer packaged goods have soared during the pandemic … and the trend shows no signs of fading. McKinsey’s consumer sentiment surveys reveal that US consumers plan to continue spending more of their money online even after the COVID-19 crisis subsides."

---

## The Solution: Amazon Forecast & Automated Data Architecture

### Amazon's Forecasting Evolution
Amazon developed its forecasting capabilities over a decade-plus journey:
- **Phase 1:** Rules-based statistical forecasts
- **Phase 2:** Machine learning algorithms
- **Phase 3:** Deep learning algorithms for diverse product categories

**Amazon Forecast** is the resulting fully managed cloud service available to AWS customers. It requires **no deep expertise** in time-series forecasting or ML.

### Automated Architecture
Many 1P vendors manually collect forecasting data. The reference architecture automates this by using **vended APIs** to programmatically source from **Amazon Vendor Central**:

- Historical and current PO data
- Product catalog data
- Diagnostic reports (to understand actual demand)

Instead of manual collection and point forecasts, the solution:

- **Predicts demand** for variable vendor POs weeks ahead
- Generates **probabilistic forecasts** (not point forecasts)
- Matches correct probabilistic forecasts to **Class A, Class B, and Class C SKUs**

---

## Key Business Benefits

- **Import Amazon PO Data:** Better access, governance, and seamless sharing across the organization
- **Increase Forecast Accuracy:** ML-powered probabilistic forecasts predict variable PO demand weeks in advance
- **Track Product Changes:** Monitor weight/dimension changes to ensure adherence to manufacturer standards
- **Reduce OTIF Penalties:** Improve OTIF metrics to enhance organic Amazon.com ranking and reduce chargeback expenses
- **Ensure High-Velocity SKUs Are In Stock:** Match probabilistic forecasts to SKU sales velocity to prevent stockouts and improve revenue

---

## Call to Action

Accurate weekly demand forecasting improves outcomes at both the **top and bottom lines**.

**Ready to automate forecasting?** [Contact your AWS account team](https://pages.awscloud.com/GLOBAL-other-IND-CPG-Contact-Us-2021.html) to get started.

