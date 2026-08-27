# Lifecycle Framework Guide

| Stage | Repo location | What was decided / built |
|---|---|---|
| 01 Problem Framing & Scoping | `README.md`, `docs/stakeholder_memo.md` | Defined a portfolio-manager decision question: next-month momentum underperformance risk. |
| 02 Tooling Setup | `.env.example`, `requirements.txt`, `src/config.py`, repo folders | Built a reproducible project scaffold and separated secrets/config from code. |
| 03 Python Fundamentals | `notebooks/python_fundamentals_summary.ipynb`, `src/utils.py` | Added reusable date and missing-value utilities. |
| 04 Data Acquisition & Ingestion | `data/raw/`, `src/ingest.py`, `notebooks/project_pipeline.ipynb` | Standardized SPMO/SPY monthly returns and Fama-French factors as raw inputs; added optional live Yahoo refresh. |
| 05 Data Storage | `src/storage.py`, `data/raw/`, `data/processed/` | Separated raw from processed data and added suffix-based read/write utilities. |
| 06 Data Preprocessing | `src/cleaning.py` | Parsed types, removed duplicate dates, and documented cleaning assumptions. |
| 07 Outliers + Risk Assumptions | `src/outliers.py`, `docs/outliers.md`, `reports/outlier_sensitivity.csv` | Flagged IQR outliers but did not mechanically remove genuine extreme market months. |
| 08 EDA | `notebooks/eda.ipynb`, `src/eda.py`, `reports/images/` | Examined distributions, correlations, relative returns, and extreme periods. |
| 09 Feature Engineering | `src/features.py`, processed dataset | Created lagged excess-return, rolling momentum, and market-volatility features with no future leakage. |
| 10a Modeling - Regression | `notebooks/modeling.ipynb`, `reports/regression_metrics.csv` | Tested a linear baseline for next-month excess return; negative holdout R2 showed weak point prediction. |
| 10b Modeling - Classification | `src/modeling.py`, `model/model.pkl`, `reports/model_metrics.csv` | Chose logistic classification as the final risk-ranking model and compared factor augmentation. |
| 12 Delivery Design | `reports/stakeholder_report.md`, `reports/images/` | Converted technical results into a decision-focused report with risks and next steps. |
| 13 Productization | `app.py`, `model/model.pkl`, `docs/stakeholder_handoff.md` | Packaged the model behind a small Flask `/predict` endpoint and documented use. |
| 14 Deployment & Monitoring | `docs/monitoring_plan.md`, `docs/handoff_plan.md` | Defined concrete Data/Model/System/Business metrics, thresholds, and ownership. |
| 15 Orchestration & System Design | `docs/orchestration_plan.md`, `src/run_step.py` | Decomposed the pipeline, documented dependencies/idempotency, and made one step CLI-callable with logging. |
| 16 Lifecycle Review | `docs/lifecycle_framework_guide.md`, `docs/project_summary.md`, `README.md` | Mapped the full lifecycle, polished repo navigation, and summarized findings for a non-technical reader. |
