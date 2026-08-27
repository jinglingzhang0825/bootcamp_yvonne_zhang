# Predicting Weak Momentum Periods in the S&P 500

## Project question
Can historical market and factor data help a portfolio manager identify market conditions in which a momentum strategy on S&P 500 stocks is likely to underperform?

This project uses **SPMO (Invesco S&P 500 Momentum ETF)** as an investable proxy for an S&P 500 momentum strategy and **SPY** as the benchmark. The target is whether SPMO underperforms SPY in the following month. The project combines market returns with Fama-French market, size, and value factors.

## Stakeholder
The primary stakeholder is a portfolio manager who allocates capital across systematic equity strategies. The output is a monthly risk flag, not an automatic trading rule.

## Main result
A simple logistic model using recent momentum relative performance and market volatility achieved an out-of-sample ROC-AUC of **0.68** on the final 25% time holdout. Adding the Fama-French factors reduced ROC-AUC to **0.48** in this sample. The result suggests that recent strategy behavior contained some weak predictive information, while the extra factor variables did not add robust out-of-sample value.

This is not strong enough to use as a standalone allocation signal. The sample is short, the proxy is an ETF rather than a reconstructed historical S&P 500 momentum portfolio, and market regimes can change.

## Repo structure
- `data/raw/` - source-level monthly return and factor files
- `data/processed/` - merged and engineered modeling dataset
- `notebooks/` - fundamentals, EDA, modeling, and full pipeline
- `src/` - reusable project functions
- `reports/` - stakeholder output, metrics, predictions, and charts
- `model/` - serialized final model and feature list
- `docs/` - assumptions, monitoring, orchestration, lifecycle, and handoff
- `tests/` - small reproducibility checks

## Setup
```bash
conda create -n momentum-project python=3.11 -y
conda activate momentum-project
pip install -r requirements.txt
cp .env.example .env
```

## Run the project
From `project/`:

```bash
jupyter lab
```

Open `notebooks/project_pipeline.ipynb` and run top to bottom.

Or run the reusable CLI stage:

```bash
python -m src.run_step --input data/processed/model_dataset.csv --output data/processed/features_cli.csv
```

## API
Start the packaged model:

```bash
python app.py
```

Example:
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"excess_lag1":-0.01,"excess_mean_3m":0.002,"spy_vol_3m":0.04}'
```

## Feature definitions
- `excess_lag1`: prior-month SPMO return minus SPY return
- `excess_mean_3m`: trailing 3-month average SPMO excess return
- `spy_vol_3m`: trailing 3-month standard deviation of SPY monthly returns
- `Mkt_RF`, `SMB`, `HML`: Fama-French factors tested in the factor-augmented model

## Assumptions and risks
SPMO is only a proxy for the S&P 500 Momentum Index. Using an ETF introduces fund-specific effects and limits the history to the post-2015 period. The factor source used here ends in August 2025, so the reproducible modeled sample ends there. Current constituent or ETF-based proxies can also create survivorship and implementation differences relative to a fully reconstructed historical momentum portfolio.

## Data sources
- SPMO monthly returns: AssetsAnalyzer performance table
- SPY monthly returns: AssetsAnalyzer performance table
- Fama-French monthly factors: public GitHub mirror of the Kenneth French factor dataset

## Lifecycle map
- Stage 01 - framing: `README.md`, `docs/stakeholder_memo.md`
- Stage 02 - tooling: repo structure, `.env.example`, `requirements.txt`, `src/config.py`
- Stage 03 - Python fundamentals: `notebooks/python_fundamentals_summary.ipynb`, `src/utils.py`
- Stage 04 - acquisition/ingestion: `src/ingest.py`, `data/raw/`, pipeline ingestion cell
- Stage 05 - data storage: `src/storage.py`, raw/processed folder separation
- Stage 06 - preprocessing: `src/cleaning.py`
- Stage 07 - outliers/risk: `src/outliers.py`, `docs/outliers.md`
- Stage 08 - EDA: `notebooks/eda.ipynb`, `src/eda.py`
- Stage 09 - features: `src/features.py`
- Stage 10a - regression baseline: `notebooks/modeling.ipynb`, `reports/regression_metrics.csv`
- Stage 10b - classification/final model: `src/modeling.py`, `model/model.pkl`
- Stage 12 - delivery design: `reports/stakeholder_report.md`
- Stage 13 - productization: `app.py`, serialized model, `docs/stakeholder_handoff.md`
- Stage 14 - monitoring: `docs/monitoring_plan.md`, `docs/handoff_plan.md`
- Stage 15 - orchestration: `docs/orchestration_plan.md`, `src/run_step.py`
- Stage 16 - lifecycle review: `docs/lifecycle_framework_guide.md`, `docs/project_summary.md`
