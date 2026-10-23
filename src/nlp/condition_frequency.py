import json
from collections import Counter

with open("data/processed/nlp_output/conditions.json") as f:
    data = json.load(f)

counter = Counter()

for encounter in data:
    counter.update(encounter["conditions"])

for condition, count in counter.most_common():
    print(f"{condition}: {count}")