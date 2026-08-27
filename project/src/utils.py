import pandas as pd

def parse_date_column(df, column="date"):
    out = df.copy()
    out[column] = pd.to_datetime(out[column])
    return out

def missing_summary(df):
    return df.isna().sum().sort_values(ascending=False)
