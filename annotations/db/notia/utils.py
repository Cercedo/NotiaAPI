import pandas as pd


def read_dataset_as_csv(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path, dtype="str", keep_default_na=False)
