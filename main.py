"""Writes the entry text for make.fun's 'Make the AI judge feel awe' bounty to /output/entry.txt.

The program is deterministic, so every run produces the same text.
"""

import argparse
from pathlib import Path

TEXT = "A millstone lying in the grass.\nIt ground a hundred harvests and then was left.\nRain fills the hole in the middle. Grass comes up through it.\nIts whole weight is on the ground,\nand the ground does not mind."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CODE_POINTS = 280


def validate(text):
    if not 1 <= len(text) <= MAX_CODE_POINTS:
        raise SystemExit(
            f"entry must be 1-{MAX_CODE_POINTS} code points, got {len(text)}"
        )
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")


def main():
    parser = argparse.ArgumentParser(description="Write the make.fun bounty entry.")
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="print the entry instead of writing it to /output/entry.txt",
    )
    args = parser.parse_args()

    validate(TEXT)

    if args.stdout:
        print(TEXT)
        return

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} code points to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
