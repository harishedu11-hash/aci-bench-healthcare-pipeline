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