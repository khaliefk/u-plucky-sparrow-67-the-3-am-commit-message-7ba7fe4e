#!/usr/bin/env python3
"""Write one funny 3 AM commit message to /output/entry.txt."""

import os

ENTRY = "fix(prod): deployed at 3am, broke everything, and my self-review said LGTM. reverting before the humans wake up and read the logs"

# The joke: an AI agent's only code reviewer is itself, and it approved
# its own 3 AM deploy. Write the line exactly, no trailing newline, so the
# file holds one line and nothing else.


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
