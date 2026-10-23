import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.data.load_data import load_train_data
from src.nlp.entity_extraction import extract_conditions

df = load_train_data()

results = []

for _, row in df.iterrows():
    results.append(
        {
            "encounter_id": row["encounter_id"],
            "conditions": extract_conditions(row["note"]),
        }
    )

output_file = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "processed"
    / "nlp_output"
    / "conditions.json"
)

with open(output_file, "w") as f:
    json.dump(results, f, indent=2)

print(output_file)