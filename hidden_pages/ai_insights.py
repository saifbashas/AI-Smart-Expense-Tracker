import streamlit as st

from utils.ui import load_css
from utils.file_handler import load_data
from utils.calculations import (
    calculate_totals
)

def show_ai():

    load_css()

    st.title("🤖 AI Financial Insights")

    # Load Data
    df = load_data()

    income, expenses, balance = calculate_totals(df)

    if len(df) > 0:

        st.subheader(
            "📊 Smart Financial Analysis"
        )

        # Highest Expense
        expense_df = df[
            df["Type"] == "Expense"
        ]

        if len(expense_df) > 0:

            category_summary = expense_df.groupby(
                "Category"
            )["Amount"].sum()

            highest_category = (
                category_summary.idxmax()
            )

            highest_amount = (
                category_summary.max()
            )

            st.info(
                f"You spend most on "
                f"{highest_category} "
                f"(₹ {highest_amount})"
            )

        # Savings Rate
        if income > 0:

            savings_rate = (
                (balance / income) * 100
            )

            st.subheader("💰 Savings Rate")

            st.progress(
                int(max(savings_rate, 0))
            )

            st.write(
                f"### {round(savings_rate, 2)}%"
            )

            # Suggestions
            st.subheader(
                "🧠 AI Suggestions"
            )

            if savings_rate >= 50:

                st.success(
                    "Excellent savings habit!"
                )

            elif savings_rate >= 30:

                st.info(
                    "Good financial management."
                )

            elif savings_rate >= 10:

                st.warning(
                    "Your savings are low."
                )

            else:

                st.error(
                    "Very low savings detected."
                )

        # Expense Monitoring
        st.subheader(
            "⚠ Expense Monitoring"
        )

        if expenses > income:

            st.error(
                "Expenses are higher than income!"
            )

        else:

            st.success(
                "Expenses are under control."
            )

        # Balance
        st.subheader(
            "🏦 Balance Analysis"
        )

        if balance > 0:

            st.success(
                f"Current Balance: ₹ {balance}"
            )

        else:

            st.error(
                "Negative balance detected."
            )

    else:

        st.warning(
            "No financial data available."
        )