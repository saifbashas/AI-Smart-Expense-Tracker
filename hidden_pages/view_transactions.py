import streamlit as st

from utils.ui import load_css
from utils.file_handler import load_data

def show_transactions():

    load_css()

    st.title("📄 Transaction History")

    # Load Data
    df = load_data()

    if len(df) > 0:

        st.subheader("🔍 Filter Transactions")

        # Category Filter
        categories = ["All"] + list(
            df["Category"].unique()
        )

        selected_category = st.selectbox(
            "Select Category",
            categories
        )

        # Type Filter
        transaction_types = ["All"] + list(
            df["Type"].unique()
        )

        selected_type = st.selectbox(
            "Select Transaction Type",
            transaction_types
        )

        # Search
        search = st.text_input(
            "Search Description"
        )

        # Filter Data
        filtered_df = df.copy()

        if selected_category != "All":

            filtered_df = filtered_df[
                filtered_df["Category"]
                == selected_category
            ]

        if selected_type != "All":

            filtered_df = filtered_df[
                filtered_df["Type"]
                == selected_type
            ]

        if search:

            filtered_df = filtered_df[
                filtered_df["Description"]
                .str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        # Display
        st.dataframe(
            filtered_df,
            width="stretch"
        )

        # CSV Download
        csv = filtered_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="📥 Download Transactions CSV",
            data=csv,
            file_name="transactions_report.csv",
            mime="text/csv"
        )

        st.write(
            f"Total Records: {len(filtered_df)}"
        )

    else:

        st.warning(
            "No transactions found."
        )