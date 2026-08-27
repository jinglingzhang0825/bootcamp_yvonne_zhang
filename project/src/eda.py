def eda_summary(df):
    numeric = df.select_dtypes(include="number")
    return {
        "shape": df.shape,
        "missing": df.isna().sum().to_dict(),
        "summary": numeric.describe().T,
        "skewness": numeric.skew().to_dict(),
        "correlation": numeric.corr()
    }
