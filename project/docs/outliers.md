# Outlier Assumptions

The project flags outliers in monthly SPMO excess returns with the IQR rule using k=1.5. Outliers are **flagged rather than automatically deleted**.

That choice matters in financial data. Large return observations may represent genuine regime changes, crashes, or rebounds rather than bad data. Removing them mechanically can make model diagnostics look cleaner while eliminating the exact events a risk model should understand.

The sensitivity file `reports/outlier_sensitivity.csv` compares the mean, median, and standard deviation with and without IQR-flagged observations. Any modeling decision to exclude an observation should be justified by data quality evidence, not only by its size.
