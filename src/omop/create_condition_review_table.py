import pandas as pd

conditions = [
    "arthritis",
    "atrial fibrillation",
    "congestive heart failure",
    "depression",
    "gastroesophageal reflux",
    "hypertension",
    "hypothyroidism",
    "kidney stones",
    "mitral regurgitation",
    "type 2 diabetes",
]

df = pd.DataFrame(
    {
        "source_condition": conditions,
        "approved_concept_id": "",
        "approved_concept_name": "",
        "review_status": "PENDING",
    }
)

output_file = (
    "data/processed/omop_output/condition_review_table.csv"
)

df.to_csv(output_file, index=False)

print(output_file)
print("Conditions:", len(df))