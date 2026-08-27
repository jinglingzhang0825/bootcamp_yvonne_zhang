import pandas as pd

def detect_outliers_iqr(series, k=1.5):
    if k <= 0:
        raise ValueError("k must be positive")
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - k * iqr, q3 + k * iqr
    return ((series < lower) | (series > upper)).fillna(False)

def detect_outliers_zscore(series, threshold=3.0):
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    sigma = series.std(ddof=0)
    if sigma == 0 or pd.isna(sigma):
        return pd.Series(False, index=series.index)
    z = (series - series.mean()) / sigma
    return (z.abs() > threshold).fillna(False)

def winsorize_series(series, lower=0.05, upper=0.95):
    if not 0 <= lower < upper <= 1:
        raise ValueError("Need 0 <= lower < upper <= 1")
    lo, hi = series.quantile([lower, upper])
    return series.clip(lo, hi)
