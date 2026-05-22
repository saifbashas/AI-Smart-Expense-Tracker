import streamlit as st

from utils.ui import load_css

# Import Pages
from hidden_pages.dashboard import show_dashboard
from hidden_pages.add_transaction import show_add_transaction
from hidden_pages.view_transactions import show_transactions
from hidden_pages.analytics import show_analytics
from hidden_pages.budget_planner import show_budget
from hidden_pages.ai_insights import show_ai

# Page Config
st.set_page_config(
    page_title="AI Smart Expense Tracker",
    layout="wide"
)

# Load CSS
load_css()

# Login Session
if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True

            st.rerun()

        else:

            st.error(
                "Invalid Username or Password"
            )

# MAIN APP
else:
    st.sidebar.title("📌 Navigation")

    page = st.sidebar.radio(
        "Go To",
        [
            "Home",
            "Dashboard",
            "Add Transaction",
            "View Transactions",
            "Analytics",
            "Budget Planner",
            "AI Insights"
        ]
    )

    # Logout Button
    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()

    # HOME PAGE
    if page == "Home":

        st.title("💰 AI Smart Expense Tracker")

        st.markdown("""
        ## 📌 Project Overview

        AI Smart Expense Tracker is a modern personal finance management application
        developed using Python and Streamlit.

        This application helps users manage their daily financial activities,
        monitor expenses, analyze spending patterns, and improve financial planning.

        ---

        ## 🎯 Purpose of the Application

        The main purpose of this application is to:

        - Track income and expenses efficiently
        - Analyze spending behavior
        - Manage category-wise budgets
        - Generate smart financial insights
        - Improve personal financial management
        - Provide an interactive and user-friendly finance dashboard

        ---

        ## 🚀 Features

        ✅ Secure Login System  
        ✅ Add & Manage Transactions  
        ✅ Expense Analytics Dashboard  
        ✅ Budget Planner  
        ✅ AI Financial Insights  
        ✅ CSV Report Download  
        ✅ Advanced Filters & Search  
        ✅ Modern Fintech UI Design

        ---

        ## 🛠 Technologies Used

        - Python
        - Streamlit
        - Pandas
        - Plotly
        - CSV/Data Handling
        - Custom CSS UI Design

        ---

        ## 📊 Why This Project?

        This project demonstrates:

        - Data handling
        - Data visualization
        - UI/UX development
        - Financial analytics
        - Modular Python architecture
        - Real-world application development
        """)

    # DASHBOARD
    elif page == "Dashboard":

        show_dashboard()

    # ADD TRANSACTION
    elif page == "Add Transaction":

        show_add_transaction()

    # VIEW TRANSACTIONS
    elif page == "View Transactions":

        show_transactions()

    # ANALYTICS
    elif page == "Analytics":

        show_analytics()

    # BUDGET PLANNER
    elif page == "Budget Planner":

        show_budget()

    # AI INSIGHTS
    elif page == "AI Insights":

        show_ai()