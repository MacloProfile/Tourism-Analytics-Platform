import pandas as pd


def extract(file_path: str, chunk_size: int = 50000):
    for chunk in pd.read_csv(
        file_path,
        encoding="utf-8",
        chunksize=chunk_size
    ):
        yield chunk
