import json
from pathlib import Path

with open("data/processed/fhir_output/patients.json") as f:
    patients = json.load(f)

with open("data/processed/fhir_output/encounters.json") as f:
    encounters = json.load(f)

with open("data/processed/fhir_output/conditions.json") as f:
    conditions = json.load(f)

with open("data/processed/fhir_output/medications.json") as f:
    medications = json.load(f)

bundles = []

for patient in patients:
    patient_id = patient["id"]

    bundle = {
        "resourceType": "Bundle",
        "id": f"bundle-{patient_id}",
        "type": "collection",
        "entry": []
    }

    bundle["entry"].append({"resource": patient})

    for encounter in encounters:
        if encounter["id"] == patient_id:
            bundle["entry"].append({"resource": encounter})

    for condition in conditions:
        if condition["subject"]["reference"] == f"Patient/{patient_id}":
            bundle["entry"].append({"resource": condition})

    for medication in medications:
        if medication["subject"]["reference"] == f"Patient/{patient_id}":
            bundle["entry"].append({"resource": medication})

    bundles.append(bundle)

output_file = (
    Path("data/processed/fhir_output")
    / "bundles.json"
)

with open(output_file, "w") as f:
    json.dump(bundles, f, indent=2)

print(output_file)
print("FHIR Bundles:", len(bundles))