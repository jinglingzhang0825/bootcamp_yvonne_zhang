# Stakeholder Handoff Summary

## Purpose
Estimate the next-month risk that an S&P 500 momentum proxy underperforms SPY.

## Key finding
The simple market/momentum baseline produced holdout ROC-AUC of **0.68**. Adding Fama-French factors reduced ROC-AUC to **0.48**. This is weak-to-moderate evidence, not a production-grade edge.

## Recommendation
Use the output only as a review flag. Do not mechanically reduce exposure based on a 0.5 probability threshold without additional validation, costs, and regime testing.

## Limitations
- SPMO is an ETF proxy, not a reconstructed constituent-level strategy.
- Monthly sample is only 2017-2025 for the factor-aligned analysis.
- Test-period class balance differs from the earlier sample.
- Factor relationships and momentum crashes are regime dependent.

## How to use
Run the pipeline, review `reports/model_metrics.csv`, then serve the saved model with `python app.py` if an API demonstration is needed.
