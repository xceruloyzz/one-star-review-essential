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

MAX_CHARS = 160  # the gate refuses /output/entry.txt over 160 characters


def main() -> None:
    # Fail loudly instead of silently submitting an over-long review.
    if not 1 <= len(REVIEW) <= MAX_CHARS:
        raise SystemExit(
            f"review is {len(REVIEW)} chars, must be 1-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters.
    # Write atomically so a partial file is never left behind.
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
