from pathlib import Path
import pandas as pd

def load_bundled_market_data(raw_dir="data/raw"):
    raw_dir = Path(raw_dir)
    returns = pd.read_csv(raw_dir / "market_returns_spy_spmo.csv", parse_dates=["date"])
    factors = pd.read_csv(raw_dir / "fama_french_3f_monthly.csv", parse_dates=["date"])
    return returns.merge(factors, on="date", how="inner").sort_values("date")

def refresh_yahoo_prices(symbols=("SPY","SPMO"), start="2017-01-01", raw_dir="data/raw"):
    """Optional live refresh. The bundled project does not require this to reproduce the graded analysis."""
    import yfinance as yf
    raw_dir = Path(raw_dir)
    raw_dir.mkdir(parents=True, exist_ok=True)
    downloaded = {}
    for symbol in symbols:
        data = yf.download(symbol, start=start, auto_adjust=True, progress=False)
        if data.empty:
            raise RuntimeError(f"No data returned for {symbol}")
        out = data.reset_index()
        path = raw_dir / f"{symbol.lower()}_daily_live.csv"
        out.to_csv(path, index=False)
        downloaded[symbol] = path
    return downloaded
