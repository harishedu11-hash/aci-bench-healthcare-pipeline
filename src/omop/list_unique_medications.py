import pandas as pd

df = pd.read_csv(
    "data/processed/omop_output/DRUG_EXPOSURE.csv"
)

for medication in sorted(
    df["drug_source_value"].unique()
):
    print(medication)