import json
from pathlib import Path

with open("data/processed/nlp_output/conditions.json") as f:
    conditions = json.load(f)

with open("data/processed/nlp_output/medications.json") as f:
    medications = json.load(f)

medication_lookup = {
    row["encounter_id"]: row["medications"]
    for row in medications
}

results = []

for row in conditions:
    encounter_id = row["encounter_id"]

    results.append(
        {
            "encounter_id": encounter_id,
            "conditions": row["conditions"],
            "medications": medication_lookup.get(encounter_id, []),
        }
    )

output_file = (
    Path("data/processed/nlp_output")
    / "clinical_entities.json"
)

with open(output_file, "w") as f:
    json.dump(results, f, indent=2)

print(output_file)