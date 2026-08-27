from pathlib import Path
import joblib
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score,
    f1_score, brier_score_loss, mean_absolute_error, mean_squared_error, r2_score
)

BASELINE_FEATURES = ["excess_lag1","excess_mean_3m","spy_vol_3m"]
FACTOR_FEATURES = BASELINE_FEATURES + ["Mkt_RF","SMB","HML"]

def time_split(df, frac=0.75):
    cut = int(len(df) * frac)
    return df.iloc[:cut].copy(), df.iloc[cut:].copy()

def fit_classifier(train, features=BASELINE_FEATURES):
    model = Pipeline([
        ("scale", StandardScaler()),
        ("model", LogisticRegression(max_iter=1000))
    ])
    model.fit(train[features], train["target_underperform_next"])
    return model

def classifier_metrics(model, test, features=BASELINE_FEATURES):
    prob = model.predict_proba(test[features])[:,1]
    pred = (prob >= 0.5).astype(int)
    return {
        "roc_auc": roc_auc_score(test["target_underperform_next"], prob),
        "accuracy": accuracy_score(test["target_underperform_next"], pred),
        "precision": precision_score(test["target_underperform_next"], pred, zero_division=0),
        "recall": recall_score(test["target_underperform_next"], pred, zero_division=0),
        "f1": f1_score(test["target_underperform_next"], pred, zero_division=0),
        "brier": brier_score_loss(test["target_underperform_next"], prob),
    }

def fit_regression(train, features=BASELINE_FEATURES):
    model = Pipeline([("scale", StandardScaler()), ("model", LinearRegression())])
    model.fit(train[features], train["target_excess_next"])
    return model

def regression_metrics(model, test, features=BASELINE_FEATURES):
    pred = model.predict(test[features])
    return {
        "rmse": mean_squared_error(test["target_excess_next"], pred) ** 0.5,
        "mae": mean_absolute_error(test["target_excess_next"], pred),
        "r2": r2_score(test["target_excess_next"], pred),
    }

def save_model(model, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    return path

def load_model(path):
    return joblib.load(path)
