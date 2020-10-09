import pandas as pd


def get_data():
    df = pd.read_csv("assets/out.csv")
    df["Date"] = pd.to_datetime(df["Date"])

    return df