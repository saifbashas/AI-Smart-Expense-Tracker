import streamlit as st
import pandas as pd

from utils.ui import load_css
from utils.file_handler import (
    load_data,
    save_data
)

def show_add_transaction():

    load_css()

    st.title("➕ Add Transaction")

    # Inputs
    transaction_type = st.selectbox(
        "Transaction Type",
        ["Income", "Expense"]
    )

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

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    description = st.text_input(
        "Description"
    )

    date = st.date_input(
        "Date"
    )

    # Add Button
    if st.button("Add Transaction"):

        new_data = pd.DataFrame({

            "Date": [date],
            "Type": [transaction_type],
            "Category": [category],
            "Amount": [amount],
            "Description": [description]

        })

        df = load_data()

        df = pd.concat(
            [df, new_data],
            ignore_index=True
        )

        save_data(df)

        st.success(
            "Transaction Added Successfully!"
        )