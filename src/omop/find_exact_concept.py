import pandas as pd

SEARCH_TERM = "hypertension"

concepts = pd.read_csv(
    "data/raw/athena/extracted/CONCEPT.csv",
    sep="\t",
    low_memory=False
)

matches = concepts[
    (concepts["domain_id"] == "Condition") &
    (concepts["vocabulary_id"] == "SNOMED") &
    (concepts["standard_concept"] == "S")
]

matches = matches[
    matches["concept_name"]
    .str.lower()
    .eq(SEARCH_TERM.lower())
]

columns = [
    "concept_id",
    "concept_name",
    "domain_id",
    "vocabulary_id",
    "concept_class_id",
]

print(matches[columns])
print()
print("Matches:", len(matches))