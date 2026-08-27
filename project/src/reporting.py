from pathlib import Path
import pandas as pd

def write_metrics(metrics, path="reports/model_metrics_generated.csv"):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(metrics).to_csv(path, index=False)
    return path
