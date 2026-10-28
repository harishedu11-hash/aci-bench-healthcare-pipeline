import sys
import pandas as pd

search_term = sys.argv[1]

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
    .str.startswith(search_term.lower())
]

columns = [
    "concept_id",
    "concept_name",
    "domain_id",
    "vocabulary_id",
]

print(
    matches[columns]
    .sort_values("concept_name")
    .head(25)
)