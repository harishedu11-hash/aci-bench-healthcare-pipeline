import sys
import pandas as pd

search_term = sys.argv[1]

concepts = pd.read_csv(
    "data/raw/athena/extracted/CONCEPT.csv",
    sep="\t",
    low_memory=False
)

matches = concepts[
    (concepts["domain_id"] == "Drug") &
    (concepts["vocabulary_id"] == "RxNorm")
]

matches = matches[
    matches["concept_name"]
    .str.contains(
        search_term,
        case=False,
        na=False
    )
]

print(
    matches[
        [
            "concept_id",
            "concept_name",
            "vocabulary_id"
        ]
    ]
    .head(25)
)