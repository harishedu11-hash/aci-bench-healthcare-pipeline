import json
import pandas as pd
from pathlib import Path

with open("data/processed/nlp_output/conditions.json") as f:
    conditions_data = json.load(f)

rows = []

condition_occurrence_id = 1

for encounter in conditions_data:
    encounter_id = encounter["encounter_id"]

    for condition in encounter["conditions"]:
        rows.append(
            {
                "condition_occurrence_id": condition_occurrence_id,
                "person_id": encounter_id,
                "visit_occurrence_id": encounter_id,
                "condition_source_value": condition,
            }
        )

        condition_occurrence_id += 1

condition_df = pd.DataFrame(rows)

output_file = (
    Path("data/processed/omop_output")
    / "CONDITION_OCCURRENCE.csv"
)

condition_df.to_csv(output_file, index=False)

print(output_file)
print("CONDITION_OCCURRENCE records:", len(condition_df))