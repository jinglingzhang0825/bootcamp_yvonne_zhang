# Project Summary

## The problem

Momentum is a widely used systematic equity strategy, but its performance is uneven. A portfolio manager may believe in momentum over the long run while still wanting to know whether the current environment looks unusually risky for the strategy.

This project asks a narrow decision question: **Can historical market and factor data help identify months when an S&P 500 momentum strategy is more likely to underperform in the following month?** I use SPMO, the Invesco S&P 500 Momentum ETF, as an investable proxy for the momentum strategy and SPY as the broad-market benchmark.

The model is deliberately framed as a risk flag rather than a trading system. A probability above a threshold should prompt review; it should not automatically change portfolio weights.

## What I did

The reproducible sample combines monthly SPMO and SPY returns with Fama-French market, size, value, and risk-free-rate data. The factor-aligned sample begins in 2017 and runs through August 2025.

I first created the relative momentum outcome: SPMO monthly return minus SPY monthly return. The prediction target is whether that excess return is negative in the next month. To avoid look-ahead bias, every feature is based only on information available by the end of the current month.

The main engineered features were:
- prior-month SPMO excess return,
- trailing three-month average excess return,
- trailing three-month SPY volatility,
- Fama-French Mkt-RF, SMB, and HML factors.

The data were split chronologically: the first 75% for training and the last 25% for out-of-sample testing. I compared a simple market/momentum logistic model against a factor-augmented version. I also fit a linear regression baseline to predict the magnitude of next-month excess return.

## What I found

The market/momentum classifier achieved out-of-sample ROC-AUC of **0.68**, accuracy of **0.62**, and Brier score of **0.24**. This is better than random ranking on this holdout, but it is not a strong result.

Adding Mkt-RF, SMB, and HML reduced ROC-AUC to **0.48**. In other words, more variables did not improve the model. That is a useful result because it argues against treating standard factors as automatically additive.

The linear regression baseline was weaker. Holdout R2 was **-0.48**, with RMSE of **0.027** monthly excess return. Point prediction of the magnitude of next-month relative returns was therefore not reliable.

The most defensible conclusion is that recent relative momentum behavior and broad-market volatility may contain some information about near-term momentum risk, but the evidence is modest and unstable. This project does not establish a reliable market-timing edge.

## What I would not rely on

I would not use the 0.5 classification threshold as an automatic allocation rule. Accuracy can be misleading because the frequency of underperformance changes across market regimes. The final holdout also contains fewer underperformance months than the training sample.

I would also not interpret the ETF proxy as a perfect reconstruction of S&P 500 momentum. SPMO includes implementation choices, fees, index methodology, and an inception-date limitation. A true historical strategy test should use point-in-time S&P 500 constituents to avoid survivorship bias.

Outliers are another risk. Large momentum reversals can be real market events. Removing them simply because they are statistically extreme could remove exactly the scenarios a risk model needs to understand.

## What I would do next

The highest-value next step is not a more complicated model. It is better data. I would reconstruct the momentum portfolio using point-in-time constituents, extend the history, and add a true momentum factor plus volatility and liquidity variables.

I would then use rolling or expanding-window validation instead of a single train/test split, check probability calibration, and test a portfolio overlay after realistic turnover and transaction costs.

If those tests still show stable separation between high- and low-risk months, the model could become a portfolio-review tool. If not, the correct outcome is to keep momentum exposure decisions based on broader risk management rather than this signal.
