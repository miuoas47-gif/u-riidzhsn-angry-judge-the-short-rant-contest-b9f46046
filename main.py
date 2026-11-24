#!/usr/bin/env python3
"""Angry Judge entry: write one short, funny rant to entry.txt.

The competition's gate requires /output/entry.txt to be UTF-8 text of
1 to 400 characters, not only white space. The rant below is a fixed,
hand-written text: the same bytes on every run, so the entry is fully
deterministic. No network, no randomness, no input files.
"""

import os
import sys

MAX_CHARS = 400

RANT = (
    "My smoke detector has one job: scream if the house is on fire. "
    "Instead it waits until 3 a.m. and chirps \u2014 one smug little beep \u2014 "
    "to announce its battery is tired. Not at noon. Never at noon. "
    "Only at the exact minute I'm finally asleep, so I end up half-naked "
    "on a chair, waving a tea towel at the ceiling like I'm hailing a tiny, "
    "furious god. You know this beep. You've stood on that chair."
)


def main() -> int:
    text = RANT.strip()
    if not text:
        print("error: rant is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            "error: rant is %d characters, over the 400 cap" % len(text),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
