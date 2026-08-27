from pathlib import Path
import os
from dotenv import load_dotenv

def load_env(path=None):
    load_dotenv(path)

def get_key(key, default=None):
    return os.getenv(key, default)

def project_paths(root="."):
    root = Path(root)
    raw = root / get_key("DATA_DIR_RAW", "data/raw")
    processed = root / get_key("DATA_DIR_PROCESSED", "data/processed")
    model = root / get_key("MODEL_PATH", "model/model.pkl")
    raw.mkdir(parents=True, exist_ok=True)
    processed.mkdir(parents=True, exist_ok=True)
    model.parent.mkdir(parents=True, exist_ok=True)
    return {"root": root, "raw": raw, "processed": processed, "model": model}
