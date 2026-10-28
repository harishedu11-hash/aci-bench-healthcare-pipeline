import pandas as pd

concepts = pd.read_csv(
    "data/raw/athena/extracted/CONCEPT.csv",
    sep="\t",
    low_memory=False
)

print(concepts.columns.tolist())
print()

print(concepts.head())
print()

print("Rows:", len(concepts))