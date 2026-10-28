import pandas as pd

conditions = pd.read_csv(
    "data/processed/omop_output/CONDITION_OCCURRENCE.csv"
)

unique_conditions = sorted(
    conditions["condition_source_value"].unique()
)

concepts = pd.read_csv(
    "data/raw/athena/extracted/CONCEPT.csv",
    sep="\t",
    low_memory=False
)

concepts = concepts[
    (concepts["domain_id"] == "Condition") &
    (concepts["vocabulary_id"] == "SNOMED") &
    (concepts["standard_concept"] == "S")
]

results = []

for condition in unique_conditions:

    matches = concepts[
        concepts["concept_name"]
        .str.contains(
            condition,
            case=False,
            na=False
        )
    ].head(5)

    for _, row in matches.iterrows():
        results.append(
            {
                "source_condition": condition,
                "concept_id": row["concept_id"],
                "concept_name": row["concept_name"],
            }
        )

output = pd.DataFrame(results)

output.to_csv(
    "data/processed/omop_output/condition_candidates.csv",
    index=False
)

print(output.head(20))
print()
print("Candidate mappings:", len(output))