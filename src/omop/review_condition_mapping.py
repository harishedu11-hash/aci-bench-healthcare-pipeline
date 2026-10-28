import pandas as pd

SEARCH_TERM = "depression"

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
    .str.contains(
        SEARCH_TERM,
        case=False,
        na=False
    )
]

print(
    matches[
        [
            "concept_id",
            "concept_name",
            "concept_class_id"
        ]
    ]
    .sort_values("concept_name")
    .head(100)
)