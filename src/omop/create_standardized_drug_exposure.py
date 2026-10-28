import pandas as pd

drug_exposure = pd.read_csv(
    "data/processed/omop_output/DRUG_EXPOSURE.csv"
)

review_table = pd.read_csv(
    "data/processed/omop_output/medication_review_table.csv"
)

review_table.columns = review_table.columns.str.strip()

drug_exposure["drug_source_value"] = (
    drug_exposure["drug_source_value"]
    .astype(str)
    .str.strip()
    .str.lower()
)

review_table["source_medication"] = (
    review_table["source_medication"]
    .astype(str)
    .str.strip()
    .str.lower()
)

standardized = drug_exposure.merge(
    review_table,
    left_on="drug_source_value",
    right_on="source_medication",
    how="left"
)

standardized = standardized[
    [
        "drug_exposure_id",
        "person_id",
        "visit_occurrence_id",
        "drug_source_value",
        "approved_concept_id",
        "approved_concept_name",
        "review_status",
    ]
]

output_file = (
    "data/processed/omop_output/"
    "DRUG_EXPOSURE_STANDARDIZED.csv"
)

standardized.to_csv(
    output_file,
    index=False
)

print(output_file)
print("Records:", len(standardized))