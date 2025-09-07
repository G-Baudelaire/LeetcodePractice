import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    output = customers[~customers["id"].isin(orders["customerId"])]
    output = output.rename(columns={"name": "Customers"})
    return output[["Customers"]]