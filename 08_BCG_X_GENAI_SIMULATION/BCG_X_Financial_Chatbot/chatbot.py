import pandas as pd


# Load the financial dataset
df = pd.read_csv(
    "data/BCG_X_Financial_Dataset_5_Years_DEMO.csv"
)


def get_financial_value(company, year, metric):
    """
    Retrieve a financial metric for a specific company and fiscal year.
    """

    result = df[
        (df["Company"].str.lower() == company.lower())
        & (df["Fiscal Year"] == year)
    ]

    if result.empty:
        return None

    return result.iloc[0][metric]


def simple_chatbot(user_query):
    """
    Respond to predefined financial queries.
    """

    user_query = user_query.strip().lower()

    # Query 1: Apple's revenue in 2025
    if user_query == "what was apple's revenue in 2025?":

        revenue = get_financial_value(
            "Apple",
            2025,
            "Total Revenue (USD millions)"
        )

        return f"Apple's revenue in 2025 was USD {revenue:,.0f} million."

    # Query 2: Microsoft's net income in 2025
    elif user_query == "what was microsoft's net income in 2025?":

        net_income = get_financial_value(
            "Microsoft",
            2025,
            "Net Income (USD millions)"
        )

        return f"Microsoft's net income in 2025 was USD {net_income:,.0f} million."

    # Query 3: Tesla's operating cash flow in 2025
    elif user_query == "what was tesla's operating cash flow in 2025?":

        cash_flow = get_financial_value(
            "Tesla",
            2025,
            "Operating Cash Flow (USD millions)"
        )

        return f"Tesla's operating cash flow in 2025 was USD {cash_flow:,.0f} million."

    # Query 4: Company with highest revenue in 2025
    elif user_query == "which company had the highest revenue in 2025?":

        revenue_2025 = df[df["Fiscal Year"] == 2025]

        highest_company = revenue_2025.loc[
            revenue_2025["Total Revenue (USD millions)"].idxmax(),
            "Company"
        ]

        highest_revenue = revenue_2025[
            "Total Revenue (USD millions)"
        ].max()

        return (
            f"{highest_company} had the highest revenue in 2025, "
            f"at USD {highest_revenue:,.0f} million."
        )

    # Query 5: Tesla's net income year-over-year change
    elif user_query == "how has tesla's net income changed over the last year?":

        net_income_2024 = get_financial_value(
            "Tesla",
            2024,
            "Net Income (USD millions)"
        )

        net_income_2025 = get_financial_value(
            "Tesla",
            2025,
            "Net Income (USD millions)"
        )

        change = net_income_2025 - net_income_2024
        percentage_change = (change / net_income_2024) * 100

        direction = "increased" if change > 0 else "decreased"

        return (
            f"Tesla's net income {direction} from "
            f"USD {net_income_2024:,.0f} million in 2024 to "
            f"USD {net_income_2025:,.0f} million in 2025. "
            f"This represents a change of {percentage_change:.2f}%."
        )

    # Unsupported query
    else:
        return (
            "Sorry, I can only answer predefined financial queries "
            "about Microsoft, Tesla, and Apple."
        )


# Interactive chatbot
if __name__ == "__main__":

    print("Financial Chatbot")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_query = input("You: ")

        if user_query.strip().lower() == "exit":
            print("Bot: Thank you for using the financial chatbot.")
            break

        response = simple_chatbot(user_query)

        print("Bot:", response)