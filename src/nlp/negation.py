NEGATION_TERMS = [
    "denies",
    "deny",
    "no ",
    "without",
    "negative for",
]


def is_negated(sentence):
    sentence = sentence.lower()

    return any(term in sentence for term in NEGATION_TERMS)