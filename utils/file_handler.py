import pandas as pd
import os

FILE_PATH = "data/transactions.csv"

COLUMNS = [
    "Type",
    "Category",
    "Amount",
    "Date",
    "Description"
]

def load_data():

    # If file doesn't exist OR file is empty
    if (
        not os.path.exists(FILE_PATH)
        or os.path.getsize(FILE_PATH) == 0
    ):

        df = pd.DataFrame(columns=COLUMNS)

        df.to_csv(FILE_PATH, index=False)

        return df

    # Otherwise read file
    return pd.read_csv(FILE_PATH)


def save_data(df):

    df.to_csv(FILE_PATH, index=False)
BUDGET_FILE = "data/budgets.csv"

BUDGET_COLUMNS = [
    "Category",
    "Budget"
]

def load_budget_data():

    if (
        not os.path.exists(BUDGET_FILE)
        or os.path.getsize(BUDGET_FILE) == 0
    ):

        df = pd.DataFrame(
            columns=BUDGET_COLUMNS
        )

        df.to_csv(
            BUDGET_FILE,
            index=False
        )

        return df

    return pd.read_csv(BUDGET_FILE)


def save_budget_data(df):

    df.to_csv(
        BUDGET_FILE,
        index=False
    )