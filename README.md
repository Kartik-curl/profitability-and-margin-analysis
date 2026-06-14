# Product Line Profitability & Margin Performance Analysis for Nassau Candy Distributor

## Overview

This project analyzes the profitability and margin performance of Nassau Candy Distributor's product portfolio using Python and Streamlit. The objective is to identify the products and divisions that contribute the most to revenue and profit while detecting products with poor margins or inefficient cost structures.

The dashboard provides interactive business intelligence for data-driven decision-making regarding pricing, sourcing, and product portfolio optimization.

---

## Problem Statement

High sales volume does not necessarily indicate high profitability. Some products generate significant revenue but contribute little profit due to high manufacturing costs or low margins.

This project aims to answer the following questions:

* Which products generate the highest profit?
* Which products have the highest gross margins?
* Which divisions are financially efficient?
* Which products require repricing or cost optimization?
* How concentrated is the company's revenue and profit among its products?

---

## Features

### Data Cleaning

* Validate sales and cost values
* Remove invalid or zero-sales records
* Handle missing unit values
* Standardize division labels

### Profitability Metrics

* Gross Margin (%)
* Profit per Unit
* Revenue Contribution
* Profit Contribution

### Product-Level Analysis

* Top products by revenue
* Top products by gross profit
* Top products by gross margin
* Product profitability leaderboard

### Division-Level Analysis

* Revenue vs Profit comparison
* Average margin by division
* Division performance evaluation

### Cost Structure Diagnostics

* Cost vs Sales scatter analysis
* Identification of cost-heavy products
* Detection of margin-poor products
* Pricing inefficiency analysis
* Recommendation flags for repricing or discontinuation

### Pareto Analysis

* 80% Revenue Contribution Analysis
* 80% Profit Contribution Analysis
* Product dependency evaluation

### Factory Analysis

* Factory-wise revenue
* Factory-wise profit
* Factory performance comparison

---

## Dashboard Features

The Streamlit application includes:

* Date range selector
* Division filter
* Margin threshold slider
* Product search functionality
* Interactive charts and tables
* KPI cards
* Dynamic filtering

---

## Key Performance Indicators

* Total Sales
* Total Gross Profit
* Gross Margin (%)
* Profit per Unit
* Revenue Contribution
* Profit Contribution

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Streamlit

---

## Project Structure

```
project/
│
├── app.py
│── dataset.csv
├── utils.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/Kartik-curl/profitability-and-margin-analysis.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the Streamlit application

```bash
streamlit run app.py
```

---

## Visualizations Included

* Top Products by Gross Profit
* Top Products by Gross Margin
* Revenue vs Profit by Division
* Cost vs Sales Scatter Plot
* Pareto Analysis Charts
* Factory Performance Charts

---

## Business Value

The analysis helps decision-makers:

* Identify high-performing products
* Detect low-margin products
* Optimize pricing strategies
* Improve cost management
* Reduce dependency on a small subset of products
* Enhance overall profitability

---

## Future Improvements

* Predictive profit forecasting
* Machine learning-based margin prediction
* Automated recommendation engine
* Geographic profitability analysis
* Inventory optimization integration

---

## Author

**Kartik Thakur**

AI & Machine Learning Enthusiast
