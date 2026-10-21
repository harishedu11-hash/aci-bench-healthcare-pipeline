from pathlib import Path

import pandas as pd


DATA_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "raw"
    / "aci-bench"
    / "data"
    / "challenge_data"
    / "train.csv"
)


def load_train_data():
    return pd.read_csv(DATA_PATH)


if __name__ == "__main__":
    df = load_train_data()
    print(df.shape)
    print(df.columns.tolist())