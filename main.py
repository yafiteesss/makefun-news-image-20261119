#!/usr/bin/env python3
"""Place the finished 19 November 2026 front page at /output/entry.png.

The picture ships in this repository; this program only copies it there.
Standard library only. No network, no randomness, no extra packages.
"""
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent
OUT = Path("/output/entry.png")

OUT.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT)
