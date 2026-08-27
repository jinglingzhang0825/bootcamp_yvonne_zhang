def build_features(df):
    out = df.sort_values("date").copy()
    out["excess_lag1"] = out["excess_return"].shift(1)
    out["excess_mean_3m"] = out["excess_return"].rolling(3).mean()
    out["spy_vol_3m"] = out["spy_return"].rolling(3).std()
    out["mkt_mean_3m"] = out["Mkt_RF"].rolling(3).mean()
    out["hml_mean_3m"] = out["HML"].rolling(3).mean()
    out["target_excess_next"] = out["excess_return"].shift(-1)
    out["target_underperform_next"] = (out["target_excess_next"] < 0).astype(int)
    return out
