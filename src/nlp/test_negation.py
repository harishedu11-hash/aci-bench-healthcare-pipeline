import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.nlp.negation import is_negated

examples = [
    "The patient denies chest pain.",
    "No history of diabetes.",
    "Patient is without shortness of breath.",
    "The patient has hypertension.",
    "The patient has congestive heart failure.",
]

for text in examples:
    print(text)
    print("Negated:", is_negated(text))
    print("-" * 50)