import re

from src.nlp.entity_extraction import CONDITIONS
from src.nlp.negation import is_negated


def extract_conditions_with_negation(text):
    positive_conditions = set()
    negated_conditions = set()

    sentences = re.split(r'(?<=[.!?])\s+', text)

    for sentence in sentences:
        sentence_lower = sentence.lower()

        for condition in CONDITIONS:
            if condition in sentence_lower:
                if is_negated(sentence):
                    negated_conditions.add(condition)
                else:
                    positive_conditions.add(condition)

    return {
        "positive": sorted(positive_conditions),
        "negated": sorted(negated_conditions),
    }