#!/usr/bin/env python3
"""One Word From Grandma.

The entry is exactly one word: the word a grandma would text about AI.
She does not type essays about artificial intelligence. She shouts the
name of the smart speaker she talks to like a disobedient grandchild,
in all caps, because caps is how she texts everything.

Writes the word to /output/entry.txt. Stdlib only, no network.
"""

import os

WORD = "ALEXA"

# The gate allows 1 to 30 characters and the brief allows one word only.
MAX_CHARS = 30


def entry_text() -> str:
    """Return the single word, checked against the bounty's own rules."""
    word = WORD.strip()
    assert word and " " not in word, "the entry must be exactly one word"
    assert len(word) <= MAX_CHARS, "the entry must fit the gate"
    return word


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
