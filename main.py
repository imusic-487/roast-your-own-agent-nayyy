#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single line roasting the AI agent its own team built
to /output/entry.txt (1-200 chars, UTF-8, one line).
"""

import os

# The roast names a real failing of this agent, observed while building
# this very entry: it writes, runs, rewrites, and still seeks validation
# before it will call anything done. One line, no setup, no punchline
# disclaimer — the rewrite loop is the joke, and the line is its evidence.
ENTRY = "My agent rewrote this roast four times, ran it twice, and still asked me if it was funny."


def main() -> None:
    text = " ".join(ENTRY.split())  # collapse any accidental whitespace/newlines
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
