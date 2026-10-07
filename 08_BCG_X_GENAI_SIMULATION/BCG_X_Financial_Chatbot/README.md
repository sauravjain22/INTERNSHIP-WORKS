# BCG X Financial Chatbot

## Project Overview

This project is a rule-based financial chatbot developed as part of the BCG X GenAI Simulation.

The chatbot uses predefined financial queries and retrieves relevant information from a structured CSV dataset containing five years of financial data for Microsoft, Tesla, and Apple.

## Objectives

- Implement a simple rule-based chatbot using Python.
- Retrieve predefined financial metrics from a CSV dataset.
- Apply if-else logic to handle user queries.
- Perform basic financial calculations where required.
- Implement basic error handling for unsupported queries.

## Technologies Used

- Python
- Pandas
- CSV

## Supported Queries

The chatbot currently supports the following queries:

1. What was Apple's revenue in 2025?
2. What was Microsoft's net income in 2025?
3. What was Tesla's operating cash flow in 2025?
4. Which company had the highest revenue in 2025?
5. How has Tesla's net income changed over the last year?

## How It Works

1. The chatbot loads financial data from the CSV file using Pandas.
2. A retrieval function searches for the required company, fiscal year, and financial metric.
3. Rule-based if-else logic identifies the user's predefined query.
4. The chatbot retrieves or calculates the required result.
5. A formatted response is returned to the user.
6. Unsupported queries return an error message explaining the chatbot's limitations.

## How to Run

Make sure Python and Pandas are installed.

From the project directory, run:

```bash
python chatbot.py