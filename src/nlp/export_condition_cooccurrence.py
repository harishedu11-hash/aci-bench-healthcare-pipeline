import json
from collections import Counter
from itertools import combinations
from pathlib import Path

with open("data/processed/nlp_output/conditions.json") as f:
    data = json.load(f)

cooccurrence_counter = Counter()

for encounter in data:
    conditions = sorted(set(encounter["conditions"]))

    for pair in combinations(conditions, 2):
        cooccurrence_counter[pair] += 1

results = []

for pair, count in cooccurrence_counter.most_common():
    results.append(
        {
            "condition_1": pair[0],
            "condition_2": pair[1],
            "count": count,
        }
    )

output_file = (
    Path("data/processed/nlp_output")
    / "condition_cooccurrence.json"
)

with open(output_file, "w") as f:
    json.dump(results, f, indent=2)

print(output_file)