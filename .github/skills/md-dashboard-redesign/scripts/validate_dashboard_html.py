#!/usr/bin/env python3
"""Compatibility launcher for the repository-level HTML validator."""

from pathlib import Path
import runpy


runpy.run_path(
    str(Path(__file__).resolve().parents[4] / "scripts" / "validate_dashboard_html.py"),
    run_name="__main__",
)
