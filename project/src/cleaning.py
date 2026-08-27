import pandas as pd

def fill_missing_median(df, columns):
    out = df.copy()
    for col in columns:
        out[col] = out[col].fillna(out[col].median())
    return out

def drop_missing(df, threshold=0.5):
    out = df.copy()
    keep = out.isna().mean() <= threshold
    return out.loc[:, keep]

def normalize_data(df, columns):
    out = df.copy()
    for col in columns:
        lo, hi = out[col].min(), out[col].max()
        if hi != lo:
            out[col] = (out[col] - lo) / (hi - lo)
    return out

def clean_project_data(df):
    out = df.copy()
    out["date"] = pd.to_datetime(out["date"])
    numeric = ["spy_return","spmo_return","excess_return","Mkt_RF","SMB","HML","RF"]
    for c in numeric:
        if c in out:
            out[c] = pd.to_numeric(out[c], errors="coerce")
    return out.drop_duplicates("date").sort_values("date")
