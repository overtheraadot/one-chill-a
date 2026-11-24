"""One Line, One Chill — make.fun entry (Account A, tag one-chill-A).

Writes a single original horror line to /output/entry.txt.
Python stdlib only. Deterministic: the entry is a fixed literal.
"""

# The entry: one sentence, one line, under 200 characters.
# A babysitter's reassuring text undone by the photo attached to it —
# the scare lands in the last words, with nothing announced up front.
ENTRY = (
    "The babysitter texted that the kids were asleep, but the photo "
    "she sent showed all three of them standing behind her, watching "
    "her type."
)


MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line."""
    assert isinstance(text, str)
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text.strip(), "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be a single sentence"
    )
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")
    print(ENTRY)


if __name__ == "__main__":
    main()
