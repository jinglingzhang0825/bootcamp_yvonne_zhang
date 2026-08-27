import argparse
import logging
from pathlib import Path
import pandas as pd
from src.features import build_features

def build_feature_step(input_path, output_path):
    logging.info("feature_step start input=%s", input_path)
    df = pd.read_csv(input_path, parse_dates=["date"])
    out = build_features(df)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(output_path, index=False)
    logging.info("feature_step wrote rows=%d output=%s", len(out), output_path)

def main():
    parser = argparse.ArgumentParser(description="Run one idempotent project pipeline step.")
    parser.add_argument("--input", default="data/processed/model_dataset.csv")
    parser.add_argument("--output", default="data/processed/features_cli.csv")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    build_feature_step(args.input, args.output)

if __name__ == "__main__":
    main()
