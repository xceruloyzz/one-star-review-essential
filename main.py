#!/usr/bin/env python3
"""One-Star Review of Something Essential — make.fun program/v1 entry.

Writes a single deadpan one-star review (<=160 chars) of an everyday
essential to /output/entry.txt. Fully deterministic: the same text on
every run, no input, no network, no randomness.
"""

import os

REVIEW = (
    "Gravity never takes a day off, never apologises, "
    "and still drops my toast butter-side down every single morning."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
