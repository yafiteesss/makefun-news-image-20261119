#!/usr/bin/env python3
"""Copy the 19 November 2026 front page into the harness output folder.

The PNG lives in this repository; the program only moves its bytes.
No network, no randomness, no third-party packages.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET = os.path.join("/output", "entry.png")

os.makedirs(os.path.dirname(TARGET), exist_ok=True)
shutil.copyfile(SOURCE, TARGET)
