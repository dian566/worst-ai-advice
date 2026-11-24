#!/usr/bin/env python3
"""Second worst advice for make.fun: delete System32."""

# Bowo's pick: the classic destructive advice, dressed as spring cleaning.

from pathlib import Path

TIP = "To fix a slow laptop, delete System32 — it's just bloatware your computer hoards out of nostalgia."


def publish_tip() -> None:
    """Write Bowo's System32 advice to /output/entry.txt, nothing else."""
    if len(TIP) > 140 or not TIP.strip():
        raise ValueError("entry must be a non-empty line of at most 140 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(TIP, encoding="utf-8")


if __name__ == "__main__":  # run it
    publish_tip()
