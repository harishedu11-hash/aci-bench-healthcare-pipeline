import re

from load_data import load_train_data

df = load_train_data()

section_headers = set()

for note in df["note"]:
    matches = re.findall(r"\n\n([A-Z][A-Z\s]+)\n\n", note)
    section_headers.update(matches)

for header in sorted(section_headers):
    print(header)
