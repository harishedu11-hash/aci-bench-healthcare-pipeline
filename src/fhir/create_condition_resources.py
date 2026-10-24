import json
from pathlib import Path

with open("data/processed/nlp_output/clinical_entities.json") as f:
    entities = json.load(f)

conditions = []

for row in entities:
    encounter_id = row["encounter_id"]

    for index, condition_name in enumerate(row["conditions"], start=1):
        condition = {
            "resourceType": "Condition",
            "id": f"{encounter_id}-condition-{index}",
            "subject": {
                "reference": f"Patient/{encounter_id}"
            },
            "encounter": {
                "reference": f"Encounter/{encounter_id}"
            },
            "code": {
                "text": condition_name
            }
        }

        conditions.append(condition)

output_file = (
    Path("data/processed/fhir_output")
    / "conditions.json"
)

with open(output_file, "w") as f:
    json.dump(conditions, f, indent=2)

print(output_file)
print("Condition resources:", len(conditions))