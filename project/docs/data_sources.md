# Data Sources and Provenance

## Market returns
- SPMO monthly returns: AssetsAnalyzer, `https://assetsanalyzer.com/etf/SPMO/performance`
- SPY monthly returns: AssetsAnalyzer, `https://assetsanalyzer.com/etf/SPY/performance`
- Values in the bundled raw file cover 2017-2025.

## Factor data
- Fama-French 3-factor monthly data from a public GitHub mirror of Kenneth French data:
  `https://raw.githubusercontent.com/shaheerAzam-dev/Fama-French-3-Factor-Markowitz-Portfolio-in-Excel/refs/heads/main/data/ff_factors_monthly.csv`
- The bundled factor extract used by the model covers 2017-01 through 2025-08.

## Important limitation
The market-return tables and factor file come from different public sources. Dates are aligned at month-end, and modeling stops at the last month available in both sources.
