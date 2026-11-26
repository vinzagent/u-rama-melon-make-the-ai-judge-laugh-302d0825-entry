"""Make the AI Judge Laugh — make.fun one-line entry.

Writes the competition's single-line office joke to /output/entry.txt
(no trailing newline) and prints it to stdout.
"""

import os
import sys

ENTRY = "Per my last email is not a greeting — it's a threat, and the whole office knows it."

# Gate for this competition: /output/entry.txt must hold 1-200 characters.
MAX_CHARS = 200

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Create the output folder if needed, then write ENTRY as UTF-8."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("ENTRY is %d characters, outside the 1-%d gate" % (len(ENTRY), MAX_CHARS))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(path, 0o644)


def main():
    try:
        write_entry()
    except OSError as exc:
        sys.stderr.write("failed to write %s: %s\n" % (OUTPUT_PATH, exc))
        raise
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
