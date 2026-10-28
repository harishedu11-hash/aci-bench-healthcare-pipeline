import json
import pandas as pd
from pathlib import Path

with open("data/processed/fhir_output/patients_v2.json") as f:
    patients = json.load(f)

rows = []

for patient in patients:
    rows.append(
        {
            "person_id": patient["id"],
            "person_source_value": patient["id"],
        }
    )

person_df = pd.DataFrame(rows)

output_file = (
    Path("data/processed/omop_output")
    / "PERSON.csv"
)

person_df.to_csv(output_file, index=False)

print(output_file)
print("PERSON records:", len(person_df))