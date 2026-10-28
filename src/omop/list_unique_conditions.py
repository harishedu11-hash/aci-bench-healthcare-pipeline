import pandas as pd

df = pd.read_csv(
    "data/processed/omop_output/CONDITION_OCCURRENCE.csv"
)

for condition in sorted(
    df["condition_source_value"].unique()
):
    print(condition)