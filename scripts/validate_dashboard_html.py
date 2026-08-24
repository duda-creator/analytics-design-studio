#!/usr/bin/env python3
"""Validate a published dashboard HTML file.

Stdlib-only (html.parser). Checks:
  - every required substring is present
  - every local <img src="..."> resolves to a file on disk
  - every in-page <a href="#..."> resolves to an existing element id

Usage:
    python scripts/validate_dashboard_html.py <path/to/dashboard-redesign.html> \
        --require "01 / Current state teardown" "02 / Redesign recommendations"

Exits non-zero on any failure so it can be used as a hard gate.
"""

from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


class _Collector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.images: list[str] = []
        self.anchors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "img" and values.get("src"):
            self.images.append(values["src"])
        if tag == "a" and values.get("href"):
            self.anchors.append(values["href"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html_path", type=Path)
    parser.add_argument(
        "--require",
        nargs="*",
        default=[],
        help="Substrings that must appear in the page",
    )
    args = parser.parse_args()

    text = args.html_path.read_text(encoding="utf-8")
    collector = _Collector()
    collector.feed(text)
    collector.close()

    missing_text = [substring for substring in args.require if substring not in text]

    broken_images = []
    for source in collector.images:
        if urlparse(source).scheme:
            continue
        candidate = (args.html_path.parent / unquote(source)).resolve()
        if not candidate.exists():
            broken_images.append(source)

    broken_anchors = [
        href
        for href in collector.anchors
        if href.startswith("#") and href[1:] not in collector.ids
    ]

    if missing_text or broken_images or broken_anchors:
        print("HTML validation FAILED")
        if missing_text:
            print(f"  missing required text: {missing_text}")
        if broken_images:
            print(f"  broken local images: {broken_images}")
        if broken_anchors:
            print(f"  broken in-page anchors: {broken_anchors}")
        return 1

    print(
        f"HTML validation passed: {len(text):,} bytes, "
        f"{len(collector.images)} images, {len(collector.ids)} ids."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
