# BCG X GenAI Simulation

## Project Overview

This project was completed as part of the BCG X GenAI Job Simulation through Forage.

The simulation focused on analyzing financial data and developing a rule-based AI-powered financial chatbot using Python and structured financial data.

## Project Objectives

- Perform initial financial data extraction and analysis.
- Analyze five years of financial data for Microsoft, Tesla, and Apple.
- Identify financial trends and key business insights.
- Develop an AI-powered financial chatbot prototype.
- Implement rule-based logic for predefined financial queries.
- Retrieve financial metrics from structured CSV data.
- Perform basic financial calculations and return formatted responses.
- Test and document the chatbot implementation.

## Tasks Completed

### Task 1 — Financial Data Analysis

Performed financial analysis using a structured dataset containing five years of financial information for:

- Microsoft
- Tesla
- Apple

The analysis included:

- Data loading and validation
- Missing-value and duplicate checks
- Financial metric analysis
- Year-over-year revenue growth
- Year-over-year net income growth
- Company-level financial comparisons
- Operating cash flow analysis
- Identification of key financial trends

Notebook:

`Notebooks/BCG_X_Financial_Analysis.ipynb`

## Task 2 — AI-Powered Financial Chatbot

Developed a rule-based financial chatbot using Python and Pandas.

The chatbot uses predefined financial queries and retrieves the required information from the financial dataset.

### Supported Queries

1. What was Apple's revenue in 2025?
2. What was Microsoft's net income in 2025?
3. What was Tesla's operating cash flow in 2025?
4. Which company had the highest revenue in 2025?
5. How has Tesla's net income changed over the last year?

### Chatbot Features

- CSV-based financial data retrieval
- Company and fiscal-year filtering
- Rule-based if-else logic
- Financial metric retrieval
- Basic financial calculations
- Percentage-change calculation
- Error handling for unsupported queries
- Interactive command-line interface

Notebook:

`Notebooks/BCG_X_Financial_Chatbot.ipynb`

Standalone chatbot:

`BCG_X_Financial_Chatbot/chatbot.py`

## Testing

The five predefined chatbot queries were tested successfully.

**Overall Result: 5/5 tests passed.**

Detailed results:

`BCG_X_Financial_Chatbot/test_result.txt`

## Technologies Used

- Python
- Pandas
- Jupyter Notebook
- CSV
- Rule-Based Logic
- Financial Data Analysis

## Project Structure

```text
08_BCG_X_GENAI_SIMULATION/
│
├── BCG_X_Financial_Chatbot.zip
│
├── BCG_X_Financial_Chatbot/
│   ├── README.md
│   ├── chatbot.py
│   ├── test_result.txt
│   └── data/
│       └── BCG_X_Financial_Dataset_5_Years_DEMO.csv
│
├── Certificates/
│   └── Saurabh_Jain_BCG_X_GenAI_Simulation_Certificate.pdf
│
├── Notebooks/
│   ├── BCG_X_Financial_Analysis.ipynb
│   ├── BCG_X_Financial_Chatbot.ipynb
│   └── BCG_X_Financial_Analysis - JupyterLab.pdf
│
└── data/
    └── raw/
        └── BCG_X_Financial_Dataset_5_Years_DEMO.csv
