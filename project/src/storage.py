from pathlib import Path
import pandas as pd

def write_df(df, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        df.to_csv(path, index=False)
    elif suffix in {".parquet", ".pq"}:
        try:
            df.to_parquet(path, index=False)
        except ImportError as exc:
            raise RuntimeError("Parquet requires pyarrow or fastparquet.") from exc
    else:
        raise ValueError(f"Unsupported suffix: {suffix}")
    return path

def read_df(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix in {".parquet", ".pq"}:
        try:
            return pd.read_parquet(path)
        except ImportError as exc:
            raise RuntimeError("Parquet requires pyarrow or fastparquet.") from exc
    raise ValueError(f"Unsupported suffix: {suffix}")
