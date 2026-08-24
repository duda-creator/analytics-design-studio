#!/usr/bin/env python3
"""Compatibility launcher for the repository-level profiling script."""

from pathlib import Path
import runpy


runpy.run_path(
    str(Path(__file__).resolve().parents[4] / "scripts" / "profile_sample_data.py"),
    run_name="__main__",
)
