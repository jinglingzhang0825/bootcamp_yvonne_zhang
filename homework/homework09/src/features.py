import numpy as np
import pandas as pd


def add_features(df):
    """
    Create momentum and market-condition features.
    """
    out = df.copy()
    out = out.sort_values("date")

    out["excess_lag1"] = out["excess_return"].shift(1)

    out["spy_vol_3m"] = (
        out["spy_return"]
        .rolling(3)
        .std()
    )

    out["market_regime"] = np.where(
        out["spy_return"] >= 0,
        "Up",
        "Down"
    )

    dummies = pd.get_dummies(
        out["market_regime"],
        prefix="market_regime",
        dtype=int
    )

    out = pd.concat([out, dummies], axis=1)

    return out