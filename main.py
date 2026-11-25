#!/usr/bin/env python3
"""One Line, One Laugh.

Writes a single original one-liner to /output/entry.txt.
Deterministic, stdlib only, no network at runtime.
"""

LINE = (
    "My cat left a dead mouse on my pillow, tasted my cooking, "
    "and took the mouse back as a refund."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "line must be 1-200 characters"
    assert text.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
