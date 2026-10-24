import json
from pathlib import Path

with open("data/processed/nlp_output/clinical_entities.json") as f:
    entities = json.load(f)

encounters = []

for row in entities:
    encounter = {
        "resourceType": "Encounter",
        "id": row["encounter_id"],
        "status": "finished",
        "subject": {
            "reference": f"Patient/{row['encounter_id']}"
        }
    }

    encounters.append(encounter)

output_file = (
    Path("data/processed/fhir_output")
    / "encounters.json"
)

with open(output_file, "w") as f:
    json.dump(encounters, f, indent=2)

print(output_file)
print("Encounter resources:", len(encounters))