# Monitoring Plan

The production candidate is the baseline logistic classifier saved in `model/model.pkl`. It estimates the probability that SPMO will underperform SPY in the following month.

**Data layer.** Flag the monthly job if any required feature has a null rate above 5%, if the newest observation is more than 40 days old, or if required columns change. The analyst who owns the monthly refresh checks the source files and reruns ingestion.

**Model layer.** Track 12-month rolling ROC-AUC and Brier score once labels arrive. Escalate for review if rolling AUC falls below 0.55 for two consecutive updates or Brier score exceeds 0.30. The current historical holdout AUC is about 0.68, so the threshold is deliberately below the initial result rather than unrealistically high.

**System layer.** The monthly pipeline should have a 95%+ job success rate and finish within five minutes. Any failure triggers the analyst to inspect logs and rerun the failed idempotent step.

**Business layer.** Track how often a high-risk flag is followed by actual momentum underperformance and whether discretionary allocation changes improve drawdown without excessive turnover. If the flag produces no useful separation over a rolling 12-month window, the portfolio manager should stop using it.

Ownership is shared: the analyst maintains data and model monitoring, while the portfolio manager approves threshold changes, model replacement, or rollback. Issues are recorded in the project issue log.
