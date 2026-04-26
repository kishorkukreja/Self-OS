---
source: https://s3.amazonaws.com/vendorcentral/VLC/North+Amercia/US/External/VOLT/33_Guide+your+demand+planning+with+Amazon's+forecasting+system/Optimize+inventory+levels+with+Vendor+Central+Demand+Forecast.pdf
date: 2026-04-26
type: industry-report
client: internal
confidential: false
tags: ["amazon", "vendor-central", "demand-forecast", "cpg", "1p-vendor"]
---

# Vendor Central Demand Forecast — Summary

**Source:** [Amazon Vendor Central Demand Forecast Guide](https://s3.amazonaws.com/vendorcentral/VLC/North+Amercia/US/External/VOLT/33_Guide+your+demand+planning+with+Amazon's+forecasting+system/Optimize+inventory+levels+with+Vendor+Central+Demand+Forecast.pdf)

---

## Amazon's Forecasting System at Scale

Amazon's demand forecasting engine operates at massive scale:

- **Hundreds of millions** of ASIN plans per day
- **Billions** of calls per week
- Across **50+ geographies**
- Using **20+ machine learning, AI, and deep learning models**
- Processing **petabytes of data**

### The 4-Step Process

> "Assuming unconstrained demand for every product sold on Amazon's websites for the next 52 weeks, we execute the following four steps in rapid succession:
> 1. Collect input data (demand, price,..)
> 2. Crunch data through AI
> 3. Catch any exceptions
> 4. Vend forecast to buying systems and to vendors"

**Key operational notes:**
- Forecasts are refreshed **multiple times per week**, though vendors receive a weekly snapshot.
- The system uses confidence intervals based on profitability and matching to like products.

### Vendor-Influenced Inputs

You influence the ASIN-level demand forecast output through:

| Input | Impact |
|-------|--------|
| **Initial product setup** | Catalog configuration (MOQ, cost, etc.) |
| **Availability** | If a product is out of stock, Amazon's confidence in future in-stock performance is depressed, impacting buy decisions against observed demand |
| **Promotions** | Both Amazon and non-Amazon promotions |
| **Website traffic** | National advertising, retail-specific promotions, PR, and other drivers of clicks on an ASIN detail page |

**Critical timing:** Input promotions **four weeks in advance** to inform Amazon's Optimal Sourcing and Placement Algorithms.

---

## ARA Demand Forecast Report

- **Starting end of Q1 2018:** The ARA Basic and ARA Premium forecasting reports are exactly the same.
- **Location:** `Operations Dashboards -> Forecast & Inventory Planning`

### What the Report Provides

- An **unconstrained projection** of customer demand
- A weekly forecast estimate closest to actual customer demand for a rolling **26 weeks**
- **Multiple P-levels** (probability levels) for safety stock planning
- Forecasts viewable/downloadable in **weekly or monthly** views across different periods

### What the Report Is NOT

> **"It is not a purchase order forecast"**

The ASIN-level forecast becomes an **input** to your PO, but it is only one of many inputs to the final PO quantity decision.

---

## Understanding P-Levels (Probability Levels)

> **"P-level" depicts the estimated stock to carry to satisfy customer demand with x% probability of success**

**Example — P-80:**
> "If that forecast is 300 units, the probability of the demand being less than or equal to 300 is 80%. This also means a 20% probability that the customer demand will be more than 300 units."

**Key Principle:** The higher the P-level you wish to accommodate, the higher the inventory level you will have to carry.

### P-Level Selection Guidance

| Scenario | Recommendation |
|----------|----------------|
| **Short "firm" planning horizon (4–6 weeks)** | Use the **mean forecast** *(does not include Amazon's safety stock)* |
| **Short-term planning** | Lower P-level (e.g., **P70**) |
| **Long-term planning** | Higher P-level (e.g., **P90**) |
| **High risk / promotions / seasonality** | Select **P70, P80, or P90** based on your risk tolerance and product profile |

**Best practice:** Consult your internal sales and marketing teams when deciding which P-level to use during your demand planning cycle.

---

## How to Use the Forecast Data

- **Planning horizon:** Use demand forecast for **long-term (4–6 week) planning**, not week-over-week operational planning.
- **Mixed P-levels:** You can use one P-level for short-term planning and a higher P-level for long-term planning.
- **Account for variability:** While estimating your shipment forecast using demand forecast, make sure to account for **historical PO variability rate**.
- **Toggle confidence levels:** Adjust your demand planning systems to consume the P-level that best positions you to be in stock for potential order volume.

