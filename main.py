#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The Meeting That Should Have Been an Email" -
a single line of plain text, at most 200 characters, one joke about
a meeting that should have been an email.
Candidates compared: the selected line (forty people gathered to
hear one sentence read aloud, and the sentence is the email's own
'per my last email'), 'We spent an hour deciding to circle back,
which is just an email wearing a calendar invite as a disguise.'
(vivid image, but the turn arrives mid-line and it runs longer),
and 'This meeting has been recurring for two years; the email it
should have been is now eligible for a pension.' (fresh angle,
but the laugh needs a beat more work).
The selected line wins: it lands with no setup, every word earns
its place, the turn arrives on the last words, and anyone who has
sat in that meeting recognises it instantly.
Deterministic: a fixed text, no network, no randomness, no clock.
Authored in-session for the 2026-11-26 sprint deadline (22:20 JST).
"""
import os
from pathlib import Path

LINE = "Forty people joined to hear one sentence read aloud, and the sentence was 'per my last email.'"
TEXT = LINE + "\n"
MAX_CHARS = 200  # gate: entry.txt must be 1 to 200 characters


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    # Validate before writing so an invalid entry never reaches the gate.
    # The gate counts characters of the single line, newline excluded.
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
