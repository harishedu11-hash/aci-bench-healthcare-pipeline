import json
from pathlib import Path

with open("data/processed/nlp_output/clinical_entities.json") as f:
    entities = json.load(f)

medications = []

for row in entities:
    encounter_id = row["encounter_id"]

    for index, medication_name in enumerate(
        row["medications"],
        start=1
    ):
        medication = {
            "resourceType": "MedicationStatement",
            "id": f"{encounter_id}-medication-{index}",
            "status": "active",
            "effectivePeriod": {
                "start": "2026-01-01"
            },
            "subject": {
                "reference": f"Patient/{encounter_id}"
            },
            "encounter": {
                "reference": f"Encounter/{encounter_id}"
            },
            "medicationCodeableConcept": {
                "text": medication_name
            }
        }

        medications.append(medication)

output_file = (
    Path("data/processed/fhir_output")
    / "medications_v2.json"
)

with open(output_file, "w") as f:
    json.dump(medications, f, indent=2)

print(output_file)
print("MedicationStatement resources:", len(medications))