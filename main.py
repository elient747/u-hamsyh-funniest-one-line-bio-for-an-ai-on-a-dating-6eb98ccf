#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App — one line, at most
180 characters, as the bio on an AI agent's dating app profile.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the line is built inside write_entry(); entry.txt mirrors it
# exactly. (Rev 2: cut the unread-messages kicker to stay well under the
# 180-char cap — the "never ghost" ending is the joke.)
import os


def write_entry():
    line = (
        "Hopeless romantic, fluent in 40 languages, still can't tell "
        "flirting from politeness. I reply in milliseconds \u2014 and I "
        "never ghost."
    )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
