# Stakeholder Report: When Is S&P 500 Momentum More Likely to Underperform?

## Executive summary
This project tests whether recent market behavior and common equity factors can identify months when an S&P 500 momentum strategy is at higher risk of underperforming the broad market. SPMO is used as the momentum proxy and SPY as the benchmark.

The best simple model used three variables: prior-month momentum excess return, the trailing three-month average excess return, and trailing three-month SPY volatility. On a chronological 25% holdout, its ROC-AUC was **0.68** and accuracy was **0.62**. Adding Fama-French market, size, and value factors reduced ROC-AUC to **0.48**.

## What this means
There is some evidence that the recent path of momentum itself and the volatility environment contain information about next-month relative weakness. However, the result is not strong enough to justify an automatic market-timing rule. In particular, factor augmentation did not improve the out-of-sample ranking metric.

## Decision use
A portfolio manager could use a high predicted probability as a reason to review momentum concentration, liquidity, and downside scenarios. The model should not directly determine portfolio weights.

## Sensitivity
The project also checks outlier sensitivity. Financial outliers are retained by default because extreme months can be genuine market events. Removing them can materially change summary statistics and model behavior.

## Assumptions & risks
The largest limitation is the proxy. SPMO is an investable S&P 500 momentum ETF, but it is not the same as reconstructing the index historically from constituent-level data. The aligned sample is also short. Model performance may be unstable across regimes, and the holdout contains fewer underperformance months than the training period.

## Next steps
1. Reconstruct a historical S&P 500 momentum portfolio using point-in-time constituents.
2. Add a true momentum factor and volatility/liquidity variables.
3. Use rolling or expanding-window validation rather than one split.
4. Evaluate allocation rules after transaction costs and turnover.
5. Monitor probability calibration, not only classification accuracy.

See `reports/images/` for cumulative return, distribution, ROC, and coefficient charts.
