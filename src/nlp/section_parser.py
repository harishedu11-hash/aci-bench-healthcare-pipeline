import re


def parse_sections(note_text):
    pattern = r"(?:^|\n\n)([A-Z][A-Z\s]+)\n\n"

    matches = list(re.finditer(pattern, note_text))

    sections = {}

    for i, match in enumerate(matches):
        section_name = match.group(1).strip()

        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(note_text)

        sections[section_name] = note_text[start:end].strip()

    return sections