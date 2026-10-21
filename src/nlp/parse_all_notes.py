import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.data.load_data import load_train_data
from src.nlp.section_parser import parse_sections

df = load_train_data()

section_counts = []

for _, row in df.iterrows():
    sections = parse_sections(row["note"])
    section_counts.append(len(sections))

print("Min:", min(section_counts))
print("Max:", max(section_counts))
print("Average:", round(sum(section_counts) / len(section_counts), 2))