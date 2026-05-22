def calculate_totals(df):

    income = df[df["Type"] == "Income"]["Amount"].sum()

    expenses = df[df["Type"] == "Expense"]["Amount"].sum()

    balance = income - expenses

    return income, expenses, balance


def financial_health_score(income, expenses):

    if income == 0:
        return 0

    score = ((income - expenses) / income) * 100

    return round(score, 2)