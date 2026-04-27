---
status: processed
---
     1|---
     2|source: https://s3.amazonaws.com/vendorcentral/VLC/North+Amercia/US/External/VOLT/33_Guide+your+demand+planning+with+Amazon's+forecasting+system/Optimize+inventory+levels+with+Vendor+Central+Demand+Forecast.pdf
     3|date: 2026-04-26
     4|type: industry-report
     5|client: internal
     6|confidential: false
     7|tags: ["amazon", "vendor-central", "demand-forecast", "cpg", "1p-vendor"]
     8|---
     9|
    10|# Vendor Central Demand Forecast — Summary
    11|
    12|**Source:** [Amazon Vendor Central Demand Forecast Guide](https://s3.amazonaws.com/vendorcentral/VLC/North+Amercia/US/External/VOLT/33_Guide+your+demand+planning+with+Amazon's+forecasting+system/Optimize+inventory+levels+with+Vendor+Central+Demand+Forecast.pdf)
    13|
    14|---
    15|
    16|## Amazon's Forecasting System at Scale
    17|
    18|Amazon's demand forecasting engine operates at massive scale:
    19|
    20|- **Hundreds of millions** of ASIN plans per day
    21|- **Billions** of calls per week
    22|- Across **50+ geographies**
    23|- Using **20+ machine learning, AI, and deep learning models**
    24|- Processing **petabytes of data**
    25|
    26|### The 4-Step Process
    27|
    28|> "Assuming unconstrained demand for every product sold on Amazon's websites for the next 52 weeks, we execute the following four steps in rapid succession:
    29|> 1. Collect input data (demand, price,..)
    30|> 2. Crunch data through AI
    31|> 3. Catch any exceptions
    32|> 4. Vend forecast to buying systems and to vendors"
    33|
    34|**Key operational notes:**
    35|- Forecasts are refreshed **multiple times per week**, though vendors receive a weekly snapshot.
    36|- The system uses confidence intervals based on profitability and matching to like products.
    37|
    38|### Vendor-Influenced Inputs
    39|
    40|You influence the ASIN-level demand forecast output through:
    41|
    42|| Input | Impact |
    43||-------|--------|
    44|| **Initial product setup** | Catalog configuration (MOQ, cost, etc.) |
    45|| **Availability** | If a product is out of stock, Amazon's confidence in future in-stock performance is depressed, impacting buy decisions against observed demand |
    46|| **Promotions** | Both Amazon and non-Amazon promotions |
    47|| **Website traffic** | National advertising, retail-specific promotions, PR, and other drivers of clicks on an ASIN detail page |
    48|
    49|**Critical timing:** Input promotions **four weeks in advance** to inform Amazon's Optimal Sourcing and Placement Algorithms.
    50|
    51|---
    52|
    53|## ARA Demand Forecast Report
    54|
    55|- **Starting end of Q1 2018:** The ARA Basic and ARA Premium forecasting reports are exactly the same.
    56|- **Location:** `Operations Dashboards -> Forecast & Inventory Planning`
    57|
    58|### What the Report Provides
    59|
    60|- An **unconstrained projection** of customer demand
    61|- A weekly forecast estimate closest to actual customer demand for a rolling **26 weeks**
    62|- **Multiple P-levels** (probability levels) for safety stock planning
    63|- Forecasts viewable/downloadable in **weekly or monthly** views across different periods
    64|
    65|### What the Report Is NOT
    66|
    67|> **"It is not a purchase order forecast"**
    68|
    69|The ASIN-level forecast becomes an **input** to your PO, but it is only one of many inputs to the final PO quantity decision.
    70|
    71|---
    72|
    73|## Understanding P-Levels (Probability Levels)
    74|
    75|> **"P-level" depicts the estimated stock to carry to satisfy customer demand with x% probability of success**
    76|
    77|**Example — P-80:**
    78|> "If that forecast is 300 units, the probability of the demand being less than or equal to 300 is 80%. This also means a 20% probability that the customer demand will be more than 300 units."
    79|
    80|**Key Principle:** The higher the P-level you wish to accommodate, the higher the inventory level you will have to carry.
    81|
    82|### P-Level Selection Guidance
    83|
    84|| Scenario | Recommendation |
    85||----------|----------------|
    86|| **Short "firm" planning horizon (4–6 weeks)** | Use the **mean forecast** *(does not include Amazon's safety stock)* |
    87|| **Short-term planning** | Lower P-level (e.g., **P70**) |
    88|| **Long-term planning** | Higher P-level (e.g., **P90**) |
    89|| **High risk / promotions / seasonality** | Select **P70, P80, or P90** based on your risk tolerance and product profile |
    90|
    91|**Best practice:** Consult your internal sales and marketing teams when deciding which P-level to use during your demand planning cycle.
    92|
    93|---
    94|
    95|## How to Use the Forecast Data
    96|
    97|- **Planning horizon:** Use demand forecast for **long-term (4–6 week) planning**, not week-over-week operational planning.
    98|- **Mixed P-levels:** You can use one P-level for short-term planning and a higher P-level for long-term planning.
    99|- **Account for variability:** While estimating your shipment forecast using demand forecast, make sure to account for **historical PO variability rate**.
   100|- **Toggle confidence levels:** Adjust your demand planning systems to consume the P-level that best positions you to be in stock for potential order volume.
   101|
   102|