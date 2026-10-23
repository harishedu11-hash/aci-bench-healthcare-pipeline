import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.nlp.condition_with_negation import (
    extract_conditions_with_negation,
)

examples = [
    "The patient has hypertension and congestive heart failure.",
    "The patient denies hypertension.",
    "No history of diabetes.",
    "The patient has depression and hypothyroidism.",
]

for text in examples:
    print(text)
    print(extract_conditions_with_negation(text))
    print("-" * 60)