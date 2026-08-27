import pandas as pd
from src.outliers import detect_outliers_iqr
from src.features import build_features

def test_iqr_returns_boolean_mask():
    s = pd.Series([1, 1, 1, 1, 100])
    mask = detect_outliers_iqr(s)
    assert mask.dtype == bool
    assert mask.iloc[-1]

def test_features_create_target():
    df = pd.DataFrame({
        "date": pd.date_range("2024-01-31", periods=5, freq="ME"),
        "spy_return": [0.01]*5,
        "spmo_return": [0.02,0.00,0.03,-0.01,0.02],
        "excess_return": [0.01,-0.01,0.02,-0.02,0.01],
        "Mkt_RF":[0.01]*5,"SMB":[0]*5,"HML":[0]*5,"RF":[0]*5
    })
    out = build_features(df)
    assert "target_underperform_next" in out
