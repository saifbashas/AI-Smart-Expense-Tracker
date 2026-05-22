import streamlit as st
import pandas as pd

from utils.ui import load_css

from utils.file_handler import (
    load_data,
    load_budget_data,
    save_budget_data
)

def show_budget():

    load_css()

    st.title("💰 Budget Planner")

    # Load Data
    expense_df = load_data()

    expense_df = expense_df[
        expense_df["Type"] == "Expense"
    ]

    budget_df = load_budget_data()

    # Budget Form
    st.subheader("Set Category Budget")

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Education",
            "Medical",
            "Entertainment",
            "Others"
        ]
    )

    budget = st.number_input(
        "Monthly Budget",
        min_value=0.0,
        step=100.0
    )

    if st.button("Save Budget"):

        new_budget = pd.DataFrame({

            "Category": [category],
            "Budget": [budget]

        })

        budget_df = budget_df[
            budget_df["Category"]
            != category
        ]

        budget_df = pd.concat(
            [budget_df, new_budget],
            ignore_index=True
        )

        save_budget_data(
            budget_df
        )

        st.success(
            "Budget Saved Successfully!"
        )

    # Analysis
    st.subheader("📊 Budget Analysis")

    if len(budget_df) > 0:

        for _, row in budget_df.iterrows():

            category = row["Category"]

            budget_amount = row["Budget"]

            actual_expense = expense_df[
                expense_df["Category"]
                == category
            ]["Amount"].sum()

            st.write(f"### {category}")

            st.write(
                f"Budget: ₹ {budget_amount}"
            )

            st.write(
                f"Spent: ₹ {actual_expense}"
            )

            percentage = 0

            if budget_amount > 0:

                percentage = int(
                    (actual_expense / budget_amount)
                    * 100
                )

            st.progress(
                min(percentage, 100)
            )

            if actual_expense > budget_amount:

                st.error(
                    f"Budget exceeded in {category}"
                )

            else:

                st.success(
                    f"Within budget for {category}"
                )

    else:

        st.warning(
            "No budgets added yet."
        )