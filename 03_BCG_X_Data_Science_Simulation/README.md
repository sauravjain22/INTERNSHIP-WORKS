# BCG X – Data Science Job Simulation

## Overview

This project was completed as part of the **BCG X Data Science Job Simulation on Forage**.

The project focused on helping **PowerCo**, a utility company serving small and medium-sized businesses, investigate customer churn and develop a data-driven approach to identifying customers who may be at risk of leaving.

The project followed an end-to-end data science workflow, from understanding the business problem and exploring the data to feature engineering, machine learning, model evaluation, and communicating business recommendations.

---

## Business Problem

PowerCo was experiencing customer churn and wanted to better understand the factors associated with customers leaving.

A key business question was whether **price sensitivity** could be contributing to churn.

The objective was to analyse customer and pricing data, identify meaningful patterns, engineer useful predictive features, and build a machine learning model capable of predicting customer churn.

---

## Project Workflow

### 1. Business Understanding & Problem Framing

- Understood PowerCo's business context and customer churn problem
- Defined the objective of the analysis
- Considered price sensitivity as an important business hypothesis
- Identified the data required for the investigation

### 2. Exploratory Data Analysis & Data Cleaning

Analysed customer and pricing datasets to understand:

- Customer demographics and characteristics
- Consumption behaviour
- Product subscriptions
- Customer margins
- Contract and customer timelines
- Pricing information
- Churn distribution

Data preparation included:

- Handling placeholder values such as `MISSING`
- Converting date columns to appropriate datetime formats
- Examining distributions and potential outliers
- Analysing churn across different customer characteristics
- Investigating relationships between customer behaviour and churn

### 3. Feature Engineering

Created additional business-driven features to provide a more meaningful representation of customer behaviour.

Key engineered features included:

- Off-peak energy price difference
- Off-peak power price difference
- Recent consumption ratio
- Forecast consumption difference
- Forecast consumption ratio
- Multiple-product indicator
- Contract duration
- Days to product modification
- Consumption per product
- Gas subscription indicator
- Net margin per product
- Margin per subscribed power
- Consumption per subscribed power
- Forecast vs. actual consumption percentage
- Zero annual consumption indicator

These features were designed to capture customer behaviour, pricing changes, product relationships, profitability and usage patterns.

### 4. Modeling & Evaluation

A **Random Forest Classifier** was trained to predict customer churn.

The final modelling dataset contained:

- **14,606 customers**
- **61 predictive features**
- Churn as the target variable

The data was split into:

- 75% training data
- 25% test data

### Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 90.31% |
| Precision | 71.43% |
| Recall | 5.46% |
| F1 Score | 10.15% |
| ROC-AUC | 0.665 |

### Important Model Finding

Although the model achieved **90.31% accuracy**, accuracy alone was misleading because the dataset was highly imbalanced.

The model identified only:

**20 of 366 actual churners**

This resulted in a recall of only **5.46%**.

Therefore, the current Random Forest model is **not suitable as a standalone automated retention decision tool**.

This was an important finding because a churn model needs to identify customers who are actually at risk of leaving, rather than simply achieving high overall accuracy.

---

## Key Business Insights

The analysis highlighted several important dimensions for understanding customer churn:

- Customer consumption behaviour
- Product usage
- Customer margins
- Gas subscription
- Customer timelines
- Pricing changes

Price sensitivity remained an important hypothesis for further investigation, but the analysis did **not** establish pricing as the sole driver of churn.

---

## Recommendations

Based on the analysis and model evaluation, the following actions were recommended:

### 1. Improve Churn Detection

Address the class imbalance and optimise the model's prediction threshold to improve identification of actual churners.

### 2. Identify High-Risk Customer Segments

Further investigate pricing and consumption behaviour to identify customer groups with higher churn risk.

### 3. Use Targeted Retention Strategies

Rather than applying broad discounts, use customer-level risk information to prioritise retention efforts.

### 4. Validate Before Deployment

Test improved models on future customer data before using them operationally for customer retention decisions.

---

## Business Impact

A stronger churn prediction model could help PowerCo identify at-risk customers earlier and prioritise retention resources more effectively.

This could support targeted retention strategies and help reduce avoidable customer losses.

However, the current model should first be improved and validated before being used for operational decision-making.

---

## Project Structure

```text
BCG_X_DATA_SCIENCE/
│
├── 01_Business_Problem/
│
├── 02_Data/
│   ├── client_data.csv
│   ├── price_data.csv
│   ├── clean_data_after_eda.csv
│   └── data_for_predictions.csv
│
├── 03_EDA/
│   └── Task_3_EDA_PowerCo.ipynb
│
├── 04_Feature_Engineering/
│   └── Task_4_Feature_Engineering_PowerCo.ipynb
│
├── 05_Modeling_Evaluation/
│   └── Task_5_Modeling_Evaluation_PowerCo.ipynb
│
├── 06_Executive_Summary/
│   └── PowerCo_Executive_Summary.pdf
│
├── Certificate/
│   └── BCG Data science job simulation.pdf
│
└── README.md