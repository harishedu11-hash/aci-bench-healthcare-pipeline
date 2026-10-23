import json
from collections import Counter
from itertools import combinations

with open("data/processed/nlp_output/conditions.json") as f:
    data = json.load(f)

cooccurrence_counter = Counter()

for encounter in data:
    conditions = sorted(set(encounter["conditions"]))

    for pair in combinations(conditions, 2):
        cooccurrence_counter[pair] += 1

for pair, count in cooccurrence_counter.most_common():
    print(f"{pair[0]} <-> {pair[1]}: {count}")