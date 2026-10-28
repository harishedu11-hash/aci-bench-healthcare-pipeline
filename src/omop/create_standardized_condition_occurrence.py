import pandas as pd

condition_occurrence = pd.read_csv(
    "data/processed/omop_output/CONDITION_OCCURRENCE.csv"
)

review_table = pd.read_csv(
    "data/processed/omop_output/condition_review_table.csv"
)

review_table.columns = (
    review_table.columns
    .str.strip()
)

condition_occurrence["condition_source_value"] = (
    condition_occurrence["condition_source_value"]
    .astype(str)
    .str.strip()
)

review_table["source_condition"] = (
    review_table["source_condition"]
    .astype(str)
    .str.strip()
)

review_table["approved_concept_name"] = (
    review_table["approved_concept_name"]
    .astype(str)
    .str.strip()
)

review_table["review_status"] = (
    review_table["review_status"]
    .astype(str)
    .str.strip()
)

print(sorted(condition_occurrence["condition_source_value"].unique()))

print()

print(sorted(review_table["source_condition"].unique()))

standardized = condition_occurrence.merge(
    review_table,
    left_on="condition_source_value",
    right_on="source_condition",
    how="left"
)

standardized = standardized[
    [
        "condition_occurrence_id",
        "person_id",
        "visit_occurrence_id",
        "condition_source_value",
        "approved_concept_id",
        "approved_concept_name",
        "review_status",
    ]
]

output_file = (
    "data/processed/omop_output/"
    "CONDITION_OCCURRENCE_STANDARDIZED.csv"
)

standardized.to_csv(
    output_file,
    index=False
)

print(output_file)
print(
    "Records:",
    len(standardized)
)
