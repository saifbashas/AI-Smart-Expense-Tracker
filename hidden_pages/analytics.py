import streamlit as st
import plotly.express as px

from utils.ui import load_css
from utils.file_handler import load_data

def show_analytics():

    load_css()

    st.title("📊 Expense Analytics")

    df = load_data()

    expense_df = df[
        df["Type"] == "Expense"
    ]

    if len(expense_df) > 0:

        category_summary = expense_df.groupby(
            "Category"
        )["Amount"].sum().reset_index()

        # Pie Chart
        pie_fig = px.pie(
            category_summary,
            names="Category",
            values="Amount",
            title="Expenses by Category"
        )

        st.plotly_chart(
            pie_fig,
            width="stretch"
        )

        # Bar Chart
        bar_fig = px.bar(
            category_summary,
            x="Category",
            y="Amount",
            title="Category Wise Expenses"
        )

        st.plotly_chart(
            bar_fig,
            width="stretch"
        )

    else:

        st.warning(
            "No expense data available."
        )