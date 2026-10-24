import json
from pathlib import Path

with open("data/processed/nlp_output/clinical_entities.json") as f:
    entities = json.load(f)

patients = []

for row in entities:
    patient = {
        "resourceType": "Patient",
        "id": row["encounter_id"],
    }

    patients.append(patient)

output_file = (
    Path("data/processed/fhir_output")
    / "patients.json"
)

with open(output_file, "w") as f:
    json.dump(patients, f, indent=2)

print(output_file)
print("Patient resources:", len(patients))