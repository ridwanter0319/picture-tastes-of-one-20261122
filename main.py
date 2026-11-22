"""Molten chocolate, captured close.

A glossy stream of dark liquid chocolate curls in a ring
around a single cocoa-dusted truffle, thin steam rising
against a dark background in warm light. Chocolate is
the one and only hero ingredient in the frame.
"""

from pathlib import Path


def main() -> None:
    base = Path(__file__).resolve().parent
    picture = (base / "entry.png").read_bytes()
    if not picture.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("entry.png is not a PNG file")
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.png").write_bytes(picture)


if __name__ == "__main__":
    main()
