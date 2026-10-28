import json
from pathlib import Path

with open("data/processed/fhir_output/medications.json") as f:
    medications = json.load(f)

for medication in medications:
    medication["status"] = "active"

    medication["category"] = {
        "text": "Community medication"
    }

output_file = (
    Path("data/processed/fhir_output")
    / "medications_enhanced.json"
)

with open(output_file, "w") as f:
    json.dump(medications, f, indent=2)

print(output_file)
print("Enhanced MedicationStatement resources:", len(medications))