#!/usr/bin/env python3
"""News-image entry for make.fun bounty news-image-20261124.

Sum up 24 November 2026's world news in one image.

The program copies the image shipped beside it (entry.png, 1024x1024,
under 1 MiB) to /output/entry.png. Standard library only, no network,
fully deterministic: two runs write identical bytes.

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Deterministic check: the copy must be byte-identical to the source.
    with open(src, "rb") as f:
        expected = f.read()
    with open(dst, "rb") as f:
        written = f.read()
    assert written == expected, "entry.png copy mismatch"
    print(f"Wrote {dst} ({len(written)} bytes)")


if __name__ == "__main__":
    main()
