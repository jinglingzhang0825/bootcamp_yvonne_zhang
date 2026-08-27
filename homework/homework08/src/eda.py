import pandas as pd
from scipy.stats import skew, kurtosis


def eda_summary(df):
    """
    Print a basic EDA summary for numeric and categorical columns.
    """

    print("Shape:")
    print(df.shape)

    print("\nMissing values:")
    print(df.isna().sum())

    numeric_cols = df.select_dtypes(include='number').columns

    print("\nNumeric summary:")
    summary = df[numeric_cols].describe().T
    summary['skew'] = [skew(df[c].dropna()) for c in numeric_cols]
    summary['kurtosis'] = [kurtosis(df[c].dropna()) for c in numeric_cols]
    print(summary)

    categorical_cols = df.select_dtypes(exclude='number').columns

    print("\nCategorical columns:")
    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].value_counts(dropna=False))

    return summary