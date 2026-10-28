import json
from pathlib import Path

with open("data/processed/fhir_output/conditions.json") as f:
    conditions = json.load(f)

for condition in conditions:
    condition["clinicalStatus"] = {
        "text": "active"
    }

    condition["verificationStatus"] = {
        "text": "confirmed"
    }

output_file = (
    Path("data/processed/fhir_output")
    / "conditions_enhanced.json"
)

with open(output_file, "w") as f:
    json.dump(conditions, f, indent=2)

print(output_file)
print("Enhanced Condition resources:", len(conditions))