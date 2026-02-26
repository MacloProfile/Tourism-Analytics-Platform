import pandas as pd


def extract(file_path: str) -> pd.DataFrame:

    df = pd.read_csv(
        file_path,
        encoding="utf-8",
        low_memory=False
    )

    return df
