MEDICATIONS = [
    "lisinopril",
    "lasix",
    "tylenol",
    "synthroid",
    "ultram",
    "imitrex",
    "protonix",
]


def extract_medications(text):
    text_lower = text.lower()

    return sorted(
        {
            medication
            for medication in MEDICATIONS
            if medication in text_lower
        }
    )

CONDITIONS = [
    "congestive heart failure",
    "depression",
    "hypertension",
    "arthritis",
    "hypothyroidism",
    "kidney stones",
    "gastroesophageal reflux",
    "type 2 diabetes",
    "atrial fibrillation",
    "mitral regurgitation",
]


def extract_conditions(text):
    text_lower = text.lower()

    return sorted(
        {
            condition
            for condition in CONDITIONS
            if condition in text_lower
        }
    )