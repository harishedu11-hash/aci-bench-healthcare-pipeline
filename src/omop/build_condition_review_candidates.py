import pandas as pd

conditions = pd.read_csv(
    "data/processed/omop_output/condition_review_table.csv"
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

for condition in conditions["source_condition"]:

    matches = concepts[
        concepts["concept_name"]
        .str.contains(
            condition,
            case=False,
            na=False
        )
    ].head(10)

    for _, row in matches.iterrows():

        results.append(
            {
                "source_condition": condition,
                "candidate_concept_id": row["concept_id"],
                "candidate_concept_name": row["concept_name"],
                "review_decision": "",
            }
        )

review_df = pd.DataFrame(results)

output_file = (
    "data/processed/omop_output/"
    "condition_review_candidates.csv"
)

review_df.to_csv(output_file, index=False)

print(output_file)
print("Candidate rows:", len(review_df))