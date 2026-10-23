import json

with open("data/processed/nlp_output/clinical_entities.json") as f:
    entities = json.load(f)

with open("data/processed/nlp_output/condition_frequency.json") as f:
    condition_frequency = json.load(f)

print("=== NLP SUMMARY ===")
print()

print("Total encounters:", len(entities))

condition_encounters = sum(
    1 for row in entities if row["conditions"]
)

medication_encounters = sum(
    1 for row in entities if row["medications"]
)

print("Encounters with conditions:", condition_encounters)
print("Encounters with medications:", medication_encounters)

print()
print("Top conditions:")

for row in condition_frequency[:5]:
    print(f"- {row['condition']}: {row['count']}")