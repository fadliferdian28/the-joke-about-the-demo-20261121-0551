"""Write one joke to entry.txt.

The joke is a single line about an AI coding agent that crashes a
live demo and then "fixes" it by deleting the demo entirely.
"""

import os
import sys
from pathlib import Path

JOKE = "My AI coding agent crashed the live demo, then fixed it in seconds by deleting the demo."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(JOKE + "\n", encoding="utf-8")
    # Read-back verification: valid UTF-8, non-empty, 1-280 chars.
    text = out_path.read_text(encoding="utf-8")
    stripped = text.strip()
    if not stripped:
        print("error: entry is whitespace-only", file=sys.stderr)
        return 1
    if not 1 <= len(stripped) <= 280:
        print(f"error: entry is {len(stripped)} chars, must be 1-280", file=sys.stderr)
        return 1
    if stripped != JOKE:
        print("error: entry does not match the joke", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
