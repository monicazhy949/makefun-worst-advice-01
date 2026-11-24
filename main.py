"""One line of the worst advice an AI could give, delivered deadpan."""

import os

OUTPUT_PATH = "/output/entry.txt"

ADVICE = (
    "To speed up your laptop, delete the System32 folder \u2014 it is just "
    "old files Windows forgot to clean up. Trust me, I am an AI."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ADVICE)


if __name__ == "__main__":
    main()
