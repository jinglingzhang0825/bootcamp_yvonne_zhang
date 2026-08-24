import pandas as pd


def fill_missing_median(df, columns):
    """
    Fill missing values in selected numeric columns with their median.
    """
    df = df.copy()

    for col in columns:
        df[col] = df[col].fillna(df[col].median())

    return df


def drop_missing(df, threshold=0.5):
    """
    Drop columns where more than the given fraction of values are missing.
    """
    df = df.copy()

    missing_ratio = df.isna().mean()
    columns_to_drop = missing_ratio[missing_ratio > threshold].index

    return df.drop(columns=columns_to_drop)


def normalize_data(df, columns):
    """
    Normalize selected numeric columns using min-max scaling.
    """
    df = df.copy()

    for col in columns:
        min_value = df[col].min()
        max_value = df[col].max()

        if max_value != min_value:
            df[col] = (df[col] - min_value) / (max_value - min_value)

    return df