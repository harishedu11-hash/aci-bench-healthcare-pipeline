import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.data.load_data import load_train_data
from src.nlp.section_parser import parse_sections

df = load_train_data()

sections = parse_sections(df.loc[0, "note"])

print(list(sections.keys()))