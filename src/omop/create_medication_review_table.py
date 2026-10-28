import pandas as pd

medications = [
    "imitrex",
    "lasix",
    "lisinopril",
    "protonix",
    "synthroid",
    "tylenol",
    "ultram",
]

df = pd.DataFrame(
    {
        "source_medication": medications,
        "approved_concept_id": "",
        "approved_concept_name": "",
        "review_status": "PENDING",
    }
)

output_file = (
    "data/processed/omop_output/"
    "medication_review_table.csv"
)

df.to_csv(output_file, index=False)

print(output_file)
print("Medications:", len(df))