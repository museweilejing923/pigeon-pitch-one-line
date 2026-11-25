#!/usr/bin/env python3
"""Pigeon pitch writer: one line from a bird with a delivery startup.

PITCH is the whole entry. validate() runs a chain of small yes/no
helpers over it; the first "no" prints why and exits before any file
is touched, and only a line that clears every helper is saved to
/output/entry.txt with a trailing newline.
"""

import sys

PITCH = "PigeonPost: same-day delivery by birds that already know your roof. We just need seed funding. Literally. Seed."
MAXIMUM = 200
OUTPUT = "/output/entry.txt"
TERMINALS = (".", "!", "?")
PUNCT = set(".,!?;:'\"-() ")


def reject(why):
    print(f"invalid pitch: {why}", file=sys.stderr)
    raise SystemExit(1)


def is_present(line):
    return bool(line and line.strip())


def fits_limit(line):
    return len(line) <= MAXIMUM


def has_no_controls(line):
    return not any(ord(ch) < 32 for ch in line)


def is_tidy(line):
    return line == line.strip() and "  " not in line and "\n" not in line


def has_letters(line):
    return any(ch.isalpha() for ch in line)


def is_not_punct_only(line):
    return not all(ch in PUNCT for ch in line)


def is_not_digits_only(line):
    return not line.strip().isdigit()


def ends_with_mark(line):
    return line.rstrip().endswith(TERMINALS)


def asks_for_seed(line):
    return "seed" in line.lower()


def sentences_start_upper(line):
    # Every sentence in the pitch must start with a capital letter; a
    # lowercase opening reads like a mumble, not a pitch.
    for chunk in line.replace("!", ".").replace("?", ".").split("."):
        stripped = chunk.strip()
        if stripped and not stripped[0].isupper():
            return False
    return True


def validate(line):
    if not is_present(line):
        reject("pitch is empty")
    if not fits_limit(line):
        reject(f"pitch is {len(line)} chars, over the {MAXIMUM} limit")
    if not has_no_controls(line):
        reject("pitch has control characters")
    if not is_tidy(line):
        reject("pitch has leading/trailing/double spaces or a newline")
    if not has_letters(line):
        reject("pitch has no letters")
    if not is_not_punct_only(line):
        reject("pitch is only punctuation")
    if not is_not_digits_only(line):
        reject("pitch is only digits")
    if not ends_with_mark(line):
        reject("pitch must end with punctuation")
    if not asks_for_seed(line):
        reject("the pitch must ask for seed funding, literally")
    if not sentences_start_upper(line):
        reject("every sentence in the pitch must start with a capital letter")


def main():
    validate(PITCH)
    with open(OUTPUT, "w", encoding="utf-8") as dest:
        dest.write(PITCH + "\n")


if __name__ == "__main__":
    main()
