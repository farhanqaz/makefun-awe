import argparse
from pathlib import Path

TEXT = "Every year the lake lays down a line of silt, thin as a fingernail.\nThere are nine thousand of them under the boat.\nThe boat is not holding anything up.\nThe lake does that."

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
