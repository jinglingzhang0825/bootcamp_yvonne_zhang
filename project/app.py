from pathlib import Path
import json
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)
MODEL_PATH = Path("model/model.pkl")
FEATURES = json.loads(Path("model/feature_list.json").read_text())
model = joblib.load(MODEL_PATH)

@app.get("/health")
def health():
    return jsonify({"status": "ok", "model_loaded": MODEL_PATH.exists()})

@app.post("/predict")
def predict():
    payload = request.get_json(silent=True) or {}
    missing = [f for f in FEATURES if f not in payload]
    if missing:
        return jsonify({"error": "missing features", "missing": missing}), 400
    row = pd.DataFrame([{f: float(payload[f]) for f in FEATURES}])
    prob = float(model.predict_proba(row)[0, 1])
    return jsonify({
        "underperformance_probability": prob,
        "risk_flag": int(prob >= 0.5),
        "features": FEATURES
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
