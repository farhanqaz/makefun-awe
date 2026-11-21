from pathlib import Path

PATH = Path("/output/entry.txt")
MAX_CODE_POINTS = 280


def main():
    text = PATH.read_text(encoding="utf-8")
    count = len(text)
    valid = 1 <= count <= MAX_CODE_POINTS and bool(text.strip())
    print(f"code points: {count}")
    print(f"valid: {'yes' if valid else 'no'}")


if __name__ == "__main__":
    main()
