#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line (1-180 chars) to /output/entry.txt.
Pure stdlib only.
"""

# PART_A: the placard line (invented fresh in this session).
LINE = (
    "Office Chair of the Perpetual Meeting, c. 2003, faux leather and "
    "14 broken lumbar settings. Donated by the manager who spun in it "
    "214 times to avoid answering one email."
)


# PART_B: write the line, with the gate asserted in-process.
def main() -> None:
    assert 1 <= len(LINE) <= 180, f"line length {len(LINE)} outside 1-180"
    assert LINE.strip() == LINE, "line must not have leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    text = LINE.encode("utf-8")
    assert 1 <= len(text) <= 180, "byte length outside 1-180"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(text)


if __name__ == "__main__":
    main()
