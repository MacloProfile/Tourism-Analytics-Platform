import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(columns={
        "DATE_OF_ARRIVAL": "visit_date",
        "HOME_REGION": "region_from",
        "SPENT": "expenses_mln",
        "GENDER": "gender",
        "VISIT_TYPE": "tourist_category",
        "AGE": "age"
    })

    df = df.drop_duplicates()

    df["visit_date"] = pd.to_datetime(df["visit_date"], errors="coerce")
    df["expenses_mln"] = pd.to_numeric(df["expenses_mln"], errors="coerce")

    df = df.dropna(subset=["visit_date", "region_from"])

    df["visit_date"] = df["visit_date"].dt.date

    if "gender" in df.columns:
        df["gender"] = df["gender"].astype(str).str.lower().str.strip()

    df = df.where(pd.notnull(df), None)

    return df
