# Marketing Campaign Performance Analysis

## Project Overview

This project analyzes digital marketing campaign performance across Google Search and Meta Ads using SQL, Python, Pandas, and Matplotlib. The analysis focuses on key marketing KPIs, channel performance comparison, funnel analysis, and business recommendations to support data-driven marketing decisions.

---

## Business Problem

Marketing teams invest advertising budgets across multiple channels and need to identify:

* Which channel generates the highest engagement?
* Which channel drives the most conversions?
* Which channel delivers the best return on investment?
* How users move through the marketing funnel?

This project evaluates campaign effectiveness and provides insights for optimizing marketing spend.

---

## Dataset Information

The dataset contains campaign performance data with the following fields:

| Column      | Description                  |
| ----------- | ---------------------------- |
| Date        | Campaign Date                |
| Channel     | Advertising Channel          |
| Impressions | Number of Ad Views           |
| Clicks      | Number of Ad Clicks          |
| Conversions | Number of Successful Actions |
| Spend       | Advertising Spend            |

### Channels Analyzed

* Google Search
* Meta Ads

### Dataset Size

* 36 Records
* 18 Days of Campaign Performance Data

---

## Tools & Technologies

* Python
* SQL Server Management Studio 
* Pandas
* Matplotlib
* VS Code

---

## SQL Analysis

The dataset was imported into SQL Server using BULK INSERT.

SQL was used to:

- Calculate marketing KPIs (CTR, CVR, CPC, ROAS)
- Analyze channel-level performance
- Perform funnel analysis
- Generate daily performance trends
- Aggregate campaign metrics for reporting

Key SQL Operations:
- BULK INSERT
- GROUP BY
- Aggregate Functions (SUM)
- KPI Calculations
- Trend Analysis
  
## Key Performance Indicators (KPIs)

### CTR (Click Through Rate)

CTR = Clicks ÷ Impressions × 100

Measures ad engagement.

### CVR (Conversion Rate)

CVR = Conversions ÷ Clicks × 100

Measures conversion efficiency.

### CPC (Cost Per Click)

CPC = Spend ÷ Clicks

Measures the cost of acquiring a click.

### CPA (Cost Per Acquisition)

CPA = Spend ÷ Conversions

Measures the cost of acquiring a conversion.

### ROAS (Return on Ad Spend)

ROAS = (Conversions × 100) ÷ Spend

Measures return generated from advertising spend.

---

## Funnel Analysis

The campaign funnel was analyzed to understand user progression through the marketing journey:

Impressions → Clicks → Conversions

This helps identify channel effectiveness and potential drop-off points within the customer journey.

---

## Visualizations Created

* CTR by Channel
* CVR by Channel
* CPC by Channel
* CPA by Channel
* ROAS by Channel
* Daily Click Trend
* Daily Conversion Trend
* Daily Spend Trend
* Clicks vs Conversions by Channel

# Visualizations

## 1. CTR by Channel

![CTR by Channel](screenshots/CTR%20by%20Channel.png)

## Insight
Google Search achieved a higher CTR (5.09%) than Meta Ads (4.33%), indicating stronger user engagement.

---

## 2. CVR by Channel

![CVR by Channel](screenshots/CVR%20by%20Channel.png)

## Insight
Meta Ads achieved a higher CVR (12.8%) than Google Search (8.6%), demonstrating better conversion efficiency.

---

## 3. CPA by Channel

![CPA by Channel](screenshots/CPA%20by%20Channel.png)

## Insight
Meta Ads recorded a lower CPA (6.41) than Google Search (7.03), making it more cost-efficient for acquiring customers.

---

## 4. ROAS by Channel

![ROAS by Channel](screenshots/ROAS%20by%20Channel.png)

## Insight
Meta Ads delivered a higher ROAS (15.61) compared to Google Search (14.22), generating stronger returns on ad spend.

---

## 5. Daily Click Trend

![Daily Click Trend](screenshots/Daily%20click%20Trend.png)

## Insight
The trend shows how user engagement changed throughout the campaign period and helps identify peak traffic days.

---

## 6. Daily Conversion Trend

![Daily Conversion Trend](screenshots/Daily%20Conversion%20Trend.png)

## Insight
Daily conversion tracking helps evaluate campaign effectiveness and identify high-performing periods.

---

## 7. Daily Spend Trend

![Daily Spend Trend](screenshots/Daily%20Spend%20Trend.png)

## Insight
Monitoring daily spend helps determine whether increased investment leads to better campaign outcomes.

---

## 8. Clicks vs Conversions by Channel

![Clicks vs Conversions](screenshots/Click%20vs%20Conversions%20by%20channel.png)

## Insight
Google Search generated more clicks, while Meta Ads converted a higher percentage of users, highlighting differences in channel performance.
---

## Channel Performance Summary

| Metric      | Google Search | Meta Ads |
| ----------- | ------------- | -------- |
| Impressions | 110,200       | 68,000   |
| Clicks      | 5,605         | 2,945    |
| Conversions | 482           | 377      |
| Spend       | 3,390         | 2,415    |
| CTR         | 5.09%         | 4.33%    |
| CVR         | 8.60%         | 12.80%   |
| CPC         | 0.60          | 0.82     |
| CPA         | 7.03          | 6.41     |
| ROAS        | 14.22         | 15.61    |

---

## Key Findings

### Google Search Performance

* Generated 110,200 impressions and 5,605 clicks.
* Achieved the highest CTR of 5.09%.
* Maintained the lowest CPC of 0.60.
* Produced 482 conversions.
* Delivered a ROAS of 14.22.

### Meta Ads Performance

* Generated 68,000 impressions and 2,945 clicks.
* Achieved a higher CVR of 12.80%.
* Produced 377 conversions.
* Recorded the lowest CPA of 6.41.
* Delivered the highest ROAS of 15.61.

---

## Business Insights

### Traffic Generation

Google Search generated 5,605 clicks compared to 2,945 clicks from Meta Ads and achieved a higher CTR (5.09% vs 4.33%), making it the stronger channel for driving traffic.

### Conversion Efficiency

Meta Ads achieved a significantly higher conversion rate (12.80% vs 8.60%), indicating stronger conversion performance.

### Cost Efficiency

Google Search delivered clicks at a lower cost with a CPC of 0.60 compared to 0.82 for Meta Ads.

### Customer Acquisition

Meta Ads acquired customers more efficiently with a lower CPA of 6.41 compared to 7.03 for Google Search.

### Return on Investment

Meta Ads generated the highest ROAS of 15.61, outperforming Google Search at 14.22.

---

## Business Recommendation

* Continue using Google Search for awareness and traffic generation campaigns.
* Allocate additional budget toward Meta Ads for conversion-focused campaigns.
* Monitor CPA and ROAS regularly to optimize advertising spend.
* Combine both channels to balance reach, engagement, and conversions.

---

## Project Structure

Marketing-Campaign-Performance-Analysis/

├── campaign_data.csv
├── campaign_data_analysis.py
├── campaign_visualization.py
├── screenshots/
│   ├── ctr_by_channel.png
│   ├── cvr_by_channel.png
│   ├── cpc_by_channel.png
│   ├── cpa_by_channel.png
│   ├── roas_by_channel.png
│   ├── daily_click_trend.png
│   ├── daily_conversion_trend.png
│   └── daily_spend_trend.png
└── README.md

---

## Learning Outcomes

* Marketing Analytics
* Campaign Performance Analysis
* KPI Reporting
* Funnel Analysis
* Data Visualization
* Business Intelligence
* Data-Driven Decision Making

---

## Author

**Aarati Kuchekar**

Data Analytics | SQL | Python | Excel | Marketing Analytics

