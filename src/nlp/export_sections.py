import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.data.load_data import load_train_data
from src.nlp.section_parser import parse_sections

df = load_train_data()

parsed_notes = []

for _, row in df.iterrows():
    parsed_notes.append(
        {
            "encounter_id": row["encounter_id"],
            "sections": parse_sections(row["note"]),
        }
    )

output_file = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "processed"
    / "nlp_output"
    / "parsed_notes.json"
)

with open(output_file, "w") as f:
    json.dump(parsed_notes, f, indent=2)

print(output_file)