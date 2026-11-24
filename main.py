#!/usr/bin/env python3
"""Worst AI advice entry for make.fun: microwave your phone."""

# The advice below is fixed by the bounty brief; this program only writes it out.

from os import makedirs

ADVICE = (
    "To charge your phone faster, put it in the microwave for 60 seconds "
    "— the waves top up the battery directly."
)


def write_advice() -> None:
    """Write the bad advice to /output/entry.txt, nothing else."""
    if len(ADVICE) > 140 or not ADVICE.strip():
        raise ValueError("entry must be a non-empty line of at most 140 characters")
    makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(ADVICE)


if __name__ == "__main__":  # run as a script
    write_advice()
