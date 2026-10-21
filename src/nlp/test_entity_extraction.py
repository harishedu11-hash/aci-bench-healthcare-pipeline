import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.data.load_data import load_train_data
from src.nlp.entity_extraction import extract_medications

df = load_train_data()

medications = extract_medications(df.loc[0, "note"])

print(medications)