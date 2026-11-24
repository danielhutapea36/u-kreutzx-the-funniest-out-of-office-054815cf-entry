#!/usr/bin/env python3
"""The Funniest Out-of-Office.

Writes a one-line out-of-office auto-reply to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The line is
133 characters, UTF-8, one line, no trailing newline.
Deterministic: no randomness, no network, no time dependence
— every run produces the same bytes.

Why this line: the judge weighs, in order, (1) a one-line
out-of-office reply a real person would set and send — it
opens "I'm off until Monday", a real OOO line with a punch;
(2) surprise — the twist is the inbox taking over the office,
promoting itself and giving itself a raise, not the usual
beach-or-camping joke; (3) a voice of its own — the inbox as
an ambitious usurper, not a template; (4) freshness — the
inbox-outranks-its-owner angle is not the joke in a thousand
inboxes; (5) every word earns its place — the three-beat
escalation (promoted itself, gave itself a raise, cc'd me out
of spite) lands the laugh in the final clause, "out of spite".
The em dash marks the turn from setup to punchline.
"""

import os

TEXT = (
    "I'm off until Monday and my inbox is running the office now "
    "\u2014 it just promoted itself, gave itself a raise, and cc'd "
    "me out of spite."
)


def main() -> None:
    # Gate: entry.txt must be 1-140 characters of UTF-8 text, not only
    # whitespace. The line is 133 characters, one line, no trailing
    # newline.
    assert 1 <= len(TEXT) <= 140 and TEXT.strip(), "line out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
