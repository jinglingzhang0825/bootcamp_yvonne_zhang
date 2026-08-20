# Predicting Weak Momentum Periods in the S&P 500

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

Momentum strategies can work well, but they do not perform well in every market environment. This project asks whether historical market and factor data can help identify when a momentum strategy on S&P 500 stocks is more likely to perform poorly.

I will look at variables such as market returns, volatility, and factor returns and compare them with future momentum performance.

## Stakeholder & User

The main stakeholder is a portfolio manager who uses systematic equity strategies.

The portfolio manager could use the results when deciding whether to keep the same momentum exposure or reduce it during higher-risk periods.

## Useful Answer & Decision

This is a predictive problem.

I want to estimate whether momentum is likely to perform poorly over the next month. At first, I will define poor performance as a negative momentum return.

The final result could be a simple model or set of indicators showing when momentum may be at higher risk.

## Assumptions & Constraints

* Enough historical market and factor data are available.
* I need to use the same definition of momentum throughout the project.
* Past relationships may not continue in the future.
* Transaction costs may affect actual returns.

## Known Unknowns / Risks

* I do not know yet which variables will be useful.
* Some patterns may only work during certain time periods.
* The definition of poor performance may change the result.

I will test the results across different time periods to see if they are consistent.

## Lifecycle Mapping

* Define the problem → Stage 01 → Project scope
* Collect data → Data stage → Dataset
* Build momentum strategy → Analysis stage → Strategy returns
* Test predictors → Modeling stage → Model/results
* Explain findings → Final stage → Charts and recommendation

## Repo Plan

* `data/` → data files
* `src/` → Python functions
* `notebooks/` → analysis
* `docs/` → stakeholder memo
