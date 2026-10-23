import json
from collections import Counter
from pathlib import Path

with open("data/processed/nlp_output/conditions.json") as f:
    data = json.load(f)

counter = Counter()

for encounter in data:
    counter.update(encounter["conditions"])

results = []

for condition, count in counter.most_common():
    results.append(
        {
            "condition": condition,
            "count": count,
        }
    )

output_file = (
    Path("data/processed/nlp_output")
    / "condition_frequency.json"
)

with open(output_file, "w") as f:
    json.dump(results, f, indent=2)

print(output_file)