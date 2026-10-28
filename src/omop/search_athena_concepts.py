import pandas as pd

SEARCH_TERM = "hypertension"

concepts = pd.read_csv(
    "data/raw/athena/extracted/CONCEPT.csv",
    sep="\t",
    low_memory=False
)

matches = concepts[
    concepts["concept_name"].str.contains(
        SEARCH_TERM,
        case=False,
        na=False
    )
]

matches = matches[
    (matches["domain_id"] == "Condition") &
    (matches["vocabulary_id"] == "SNOMED") &
    (matches["standard_concept"] == "S")
]

columns = [
    "concept_id",
    "concept_name",
    "domain_id",
    "vocabulary_id",
    "standard_concept",
]

print(
    matches[columns]
    .sort_values("concept_name")
    .head(20)
)
print()
print("Matches:", len(matches))