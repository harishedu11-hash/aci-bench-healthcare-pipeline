import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.data.load_data import load_train_data
from src.nlp.entity_extraction import extract_conditions

df = load_train_data()

conditions = extract_conditions(df.loc[0, "note"])

print(conditions)