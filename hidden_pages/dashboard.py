import streamlit as st

from utils.ui import load_css
from utils.file_handler import load_data
from utils.calculations import (
    calculate_totals,
    financial_health_score
)

def show_dashboard():

    load_css()

    st.title("📊 Financial Dashboard")

    # Load Data
    df = load_data()

    # Totals
    income, expenses, balance = calculate_totals(df)

    # Score
    score = financial_health_score(
        income,
        expenses
    )

    # Metrics
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "💵 Total Income",
            f"₹ {income}"
        )

    with col2:

        st.metric(
            "💸 Total Expenses",
            f"₹ {expenses}"
        )

    with col3:

        st.metric(
            "🏦 Balance",
            f"₹ {balance}"
        )

    # Score
    st.subheader("📈 Financial Health Score")

    st.progress(
        int(max(score, 0))
    )

    st.write(f"### {score}%")