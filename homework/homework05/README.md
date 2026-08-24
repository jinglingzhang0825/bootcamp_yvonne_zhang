# Homework 05 - Data Storage

## Data Storage

This project uses two folders for storing data:

- `data/raw/` stores the original CSV files.
- `data/processed/` stores processed Parquet files.

CSV is easy to read and share, while Parquet is more efficient for storing typed data.

The folder paths are loaded from `.env` using `DATA_DIR_RAW` and `DATA_DIR_PROCESSED`.

After saving the data, I reload both files and check that the shapes match and that the date and price columns keep the expected data types.