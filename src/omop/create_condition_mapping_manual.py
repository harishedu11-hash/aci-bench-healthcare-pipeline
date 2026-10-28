import pandas as pd
from pathlib import Path

mapping = [
    {"condition_source_value": "hypertension", "condition_concept_id": 316866},
    {"condition_source_value": "arthritis", "condition_concept_id": 80180},
    {"condition_source_value": "congestive heart failure", "condition_concept_id": 316139},
    {"condition_source_value": "depression", "condition_concept_id": 440383},
    {"condition_source_value": "kidney stones", "condition_concept_id": 4145681},
    {"condition_source_value": "mitral regurgitation", "condition_concept_id": 4182210},
    {"condition_source_value": "type 2 diabetes", "condition_concept_id": 201826},
    {"condition_source_value": "hypothyroidism", "condition_concept_id": 433736},
    {"condition_source_value": "gastroesophageal reflux", "condition_concept_id": 43013884},
    {"condition_source_value": "atrial fibrillation", "condition_concept_id": 313217},
]

mapping_df = pd.DataFrame(mapping)

output_file = (
    Path("data/processed/omop_output")
    / "CONDITION_MAPPING.csv"
)

mapping_df.to_csv(output_file, index=False)

print(output_file)
print("Mappings:", len(mapping_df))