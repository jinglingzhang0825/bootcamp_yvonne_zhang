# Orchestration Plan

## Tasks

| Task | Input | Output | Idempotent? |
|---|---|---|---|
| ingest | `data/raw/market_returns_spy_spmo.csv`, `data/raw/fama_french_3f_monthly.csv` | merged frame in memory | Yes |
| clean | merged raw frame | cleaned monthly frame | Yes |
| flag_outliers | cleaned frame | outlier flags | Yes |
| feature | cleaned frame | `data/processed/model_dataset.csv` | Yes |
| train | processed dataset | `model/model.pkl` | Yes with fixed split/parameters |
| evaluate | model + holdout | `reports/model_metrics.csv`, predictions | Yes |
| report | metrics + figures | stakeholder report assets | Yes |

## Dependencies

`ingest -> clean -> flag_outliers -> feature -> train -> evaluate -> report`

EDA can run after cleaning and in parallel with feature engineering. Monitoring documentation does not block the batch pipeline.

## Logging and checkpoints

Each step should log start/end time, row count, source/output path, and exceptions. Checkpoints are the raw CSVs, processed model dataset, serialized model, metrics CSV, and reports. A failed step should be retried only after checking whether the upstream checkpoint is valid.

## Retry policy

File parsing and model errors should fail immediately because retrying unchanged code is unlikely to help. Optional live network refreshes may be retried up to three times with short backoff. Never silently replace missing live data with stale data.

## What to automate now

Automate deterministic file-to-file steps: feature building, model training, evaluation, and report regeneration. Keep portfolio allocation decisions and model replacement manual because the sample is small and the output is a decision-support flag, not an autonomous trading system.

`src/run_step.py` demonstrates a CLI-callable, logged feature step.
