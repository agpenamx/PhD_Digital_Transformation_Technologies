#!/usr/bin/env python3
"""Local-only validation for a private JARVIS sent-message CSV. No network operations."""
import argparse
import collections
import csv
import json
import re
from pathlib import Path

REQUIRED = {
    "timestamp_raw", "to_full", "subject_original", "gmail_message_id",
    "gmail_status", "gmail_message_url", "review_category_inferred",
}
EMAIL = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")

def audit(path: Path, expected=None):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))
        rows = list(reader)

    ids = [r["gmail_message_id"].strip() for r in rows]
    counts = collections.Counter(ids)
    repeated = sorted(k for k, n in counts.items() if k and n > 1)
    contacts = [address.lower()
                for row in rows for address in EMAIL.findall(row.get("to_full", ""))]
    groups = collections.Counter(r.get("review_category_inferred", "")
                                 for r in rows)
    unsent = [r["gmail_message_id"] for r in rows
              if r.get("gmail_status") != "SENT"]
    missing_source_link = [r["gmail_message_id"] for r in rows
                           if not r.get("gmail_message_url")]

    result = {
        "scope_note": "This checks the supplied file only; it does not authenticate Gmail.",
        "rows": len(rows),
        "distinct_message_ids": len(set(ids)),
        "empty_message_ids": ids.count(""),
        "duplicate_message_ids": repeated,
        "to_address_occurrences": len(contacts),
        "distinct_parsed_to_addresses": len(set(contacts)),
        "category_counts_posthoc": dict(sorted(groups.items())),
        "non_sent_status_count": len(unsent),
        "missing_source_link_count": len(missing_source_link),
        "expected_rows_match": expected is None or len(rows) == expected,
        "no_bulk_send": True,
        "no_external_api_calls": True,
    }
    result["passed"] = (not repeated and "" not in ids and
                        not unsent and not missing_source_link and
                        result["expected_rows_match"])
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("private_csv", type=Path)
    parser.add_argument("--expected", type=int, default=None)
    args = parser.parse_args()
    print(json.dumps(audit(args.private_csv, args.expected),
                     indent=2, ensure_ascii=False))
