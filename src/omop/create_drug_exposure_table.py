import json
import pandas as pd
from pathlib import Path

with open("data/processed/nlp_output/medications.json") as f:
    medications_data = json.load(f)

rows = []

drug_exposure_id = 1

for encounter in medications_data:
    encounter_id = encounter["encounter_id"]

    for medication in encounter["medications"]:
        rows.append(
            {
                "drug_exposure_id": drug_exposure_id,
                "person_id": encounter_id,
                "visit_occurrence_id": encounter_id,
                "drug_source_value": medication,
            }
        )

        drug_exposure_id += 1

drug_df = pd.DataFrame(rows)

output_file = (
    Path("data/processed/omop_output")
    / "DRUG_EXPOSURE.csv"
)

drug_df.to_csv(output_file, index=False)

print(output_file)
print("DRUG_EXPOSURE records:", len(drug_df))
