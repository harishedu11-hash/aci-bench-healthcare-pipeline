import json
import pandas as pd
from pathlib import Path

with open("data/processed/fhir_output/encounters.json") as f:
    encounters = json.load(f)

rows = []

for encounter in encounters:
    rows.append(
        {
            "visit_occurrence_id": encounter["id"],
            "person_id": encounter["id"],
            "visit_source_value": encounter["id"],
        }
    )

visit_df = pd.DataFrame(rows)

output_file = (
    Path("data/processed/omop_output")
    / "VISIT_OCCURRENCE.csv"
)

visit_df.to_csv(output_file, index=False)

print(output_file)
print("VISIT_OCCURRENCE records:", len(visit_df))