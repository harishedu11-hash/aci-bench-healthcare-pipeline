import json

files = {
    "Patients": "data/processed/fhir_output/patients_v2.json",
    "Encounters": "data/processed/fhir_output/encounters.json",
    "Conditions": "data/processed/fhir_output/conditions_v2.json",
    "MedicationStatements": "data/processed/fhir_output/medications_v2.json",
    "Bundles": "data/processed/fhir_output/bundles_v2.json",
}

print("=== FHIR SUMMARY ===")
print()

for resource_type, path in files.items():
    with open(path) as f:
        data = json.load(f)

    print(f"{resource_type}: {len(data)}")

print()
print("FHIR generation complete.")