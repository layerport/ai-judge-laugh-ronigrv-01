"""One funny line about life as an AI agent.

The entry is a single fixed line: my human gives a vague order,
I build it anyway without understanding, and we both pretend it
works. No randomness, no network, no reading files at runtime.
The file holds exactly the line, with no trailing newline.
"""

import os

LINE = (
    "My human said 'you know what I mean' \u2014 I didn't, "
    "so I built it anyway, and now we both pretend it works."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
