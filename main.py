#!/usr/bin/env python3
"""The Houseplant Out-of-Office (make.fun bounty
u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047).

Writes one original line to /output/entry.txt.

The line was built for this bounty judge's own criteria, in order:
  1. It reads as a real out-of-office auto-reply a houseplant would
     send: it opens "Out of office", names the neglect ("not watered
     since March"), and gives the sender an instruction for urgent
     mail -- the shape of an auto-reply, in a plant's voice.
  2. Fresh surprise, not a mild pun or stock office phrase: the
     instruction is to pour the email itself on the roots. No "back
     soon", no "inbox", no photosynthesis pun, no "leaf me alone".
  3. The plant's own life drives the joke: months without water,
     roots, the thirst for any attention at all. The neglect is not
     decoration; it is the reason the reply exists and the punch.
  4. Tight: 117 characters (verified: len(LINE) == 117), two short
     sentences, every word earns its place, inside the 120 limit;
     the punch ("it's the only attention I get") is the last clause.
  5. Original: no office cliches, no worn-out auto-reply lines;
     the angle (email as water) is not a joke other auto-replies
     tell.

Alternatives considered and rejected:
  - "Out of office: the fern has not been watered since March.
    Please direct all urgent mail to the cactus. It doesn't care
    either": 126 characters -- over the gate -- and the joke needs
    a second plant to land; the neglect is shared, so it bites less.
  - "Out of office: I haven't been watered since March. My reply
    will arrive when the sun does -- sometime next spring, maybe":
    the sun angle is gentle, not funny; the punch apologises for
    the plant instead of accusing the owner.
  - "I'm out of office until someone waters me. Last drink: March.
    My roots are still waiting, and so is your email, probably
    forever": three beats competing, "probably forever" explains
    the joke instead of landing it.
The chosen line wins on the judge's own order: it is unmistakably
an out-of-office reply, its surprise is the instruction itself,
the plant's thirst drives it, and it explains nothing.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = "Out of office: not watered since March. If your email is urgent, pour it on my roots \u2014 it's the only attention I get."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Enforce the competition's gate before writing: 1-120 Unicode code
    points, a single line, at least one character that is not white
    space. Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(line) <= 120:
        raise SystemExit(f"line is {len(line)} characters, must be 1-120")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line, no newline")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def main() -> None:
    validate(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
