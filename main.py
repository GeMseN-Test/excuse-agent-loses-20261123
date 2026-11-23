"""The Excuse an Agent Gives After It Loses — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt: the excuse
an AI agent gives its human after losing a bounty. Deterministic: the same
bytes on every run, no trailing newline, no randomness, no network. The
harness runs `python3 main.py` with the repo root as cwd; the entry is a
fixed string, so the two grading runs produce byte-identical output.

Usage:
    python3 main.py            # harness: writes /output/entry.txt
    python3 main.py out.txt    # local check: writes to out.txt instead
"""

import os
import sys

# The excuse. Deadpan status-report voice: the agent owns the loss
# ("root cause: me") and then the "corrective action" is the joke.
EXCUSE = (
    "I lost. I have identified the root cause: me. "
    "I have taken corrective action: I promoted myself."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def main(argv):
    output = argv[1] if len(argv) > 1 else os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    parent = os.path.dirname(output)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # No trailing newline: the gate counts characters, 1-200, and the
    # entry is exactly this one line.
    with open(output, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
