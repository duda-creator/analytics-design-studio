#!/usr/bin/env python3
"""Profile CSV extracts in a dashboard's inputs/sample_data/ folder for Stage 3.

Stdlib-only (csv, no pandas/numpy) so it runs in any interpreter regardless of
binary ABI conflicts (e.g. numpy 2.x vs. modules compiled against numpy 1.x).

Usage:
    python scripts/profile_sample_data.py <sample_data_dir>

For each *.csv in the folder, reports: row/column counts, per-column null
counts, duplicate full-row count, date-range for columns containing "date",
and duplicate counts on any column matching *_id / *_key (candidate keys).
Then does a best-effort cross-file check: for every "<x>_id" column, looks
for a sibling file that owns that column and reports values with no match
(broken foreign keys).
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

KEY_PATTERN = re.compile(r"(_id|_key)$", re.IGNORECASE)
DATE_PATTERN = re.compile(r"date", re.IGNORECASE)


def load_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as file:
        return list(csv.DictReader(file))


def profile_file(path: Path, rows: list[dict]) -> None:
    print(f"\n=== {path.name} ===")
    if not rows:
        print("  (empty)")
        return
    columns = list(rows[0].keys())
    print(f"  rows={len(rows)} columns={len(columns)}: {', '.join(columns)}")

    nulls = {
        column: sum(1 for row in rows if not row.get(column)) for column in columns
    }
    nonzero_nulls = {column: count for column, count in nulls.items() if count}
    print(f"  nulls: {nonzero_nulls or 'none'}")

    full_row_keys = [tuple(row.values()) for row in rows]
    duplicate_rows = len(full_row_keys) - len(set(full_row_keys))
    print(f"  duplicate full rows: {duplicate_rows}")

    for column in columns:
        if KEY_PATTERN.search(column):
            values = [row[column] for row in rows if row.get(column)]
            duplicate_values = len(values) - len(set(values))
            print(f"  duplicate values in candidate key '{column}': {duplicate_values}")
        if DATE_PATTERN.search(column):
            values = sorted(
                value for value in (row.get(column) for row in rows) if value
            )
            if values:
                print(f"  '{column}' range: {values[0]} .. {values[-1]}")


def cross_file_fk_check(files: dict[str, list[dict]]) -> None:
    print("\n=== Cross-file referential checks (best effort) ===")
    found_any = False
    for name, rows in files.items():
        if not rows:
            continue
        for column in rows[0].keys():
            if not KEY_PATTERN.search(column):
                continue
            for other_name, other_rows in files.items():
                if (
                    other_name == name
                    or not other_rows
                    or column not in other_rows[0].keys()
                ):
                    continue
                known = {row[column] for row in other_rows if row.get(column)}
                used = {row[column] for row in rows if row.get(column)}
                missing = used - known
                if missing:
                    found_any = True
                    sample = ", ".join(list(missing)[:5])
                    print(
                        f"  {name}.{column} -> {other_name}.{column}: "
                        f"{len(missing)} unmatched (e.g. {sample})"
                    )
    if not found_any:
        print("  no unmatched foreign key values detected")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sample_data_dir", type=Path)
    args = parser.parse_args()

    csv_paths = sorted(args.sample_data_dir.glob("*.csv"))
    if not csv_paths:
        print(f"No CSV files found in {args.sample_data_dir}")
        return

    files = {}
    for path in csv_paths:
        rows = load_csv(path)
        files[path.name] = rows
        profile_file(path, rows)

    cross_file_fk_check(files)


if __name__ == "__main__":
    main()
