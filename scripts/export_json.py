#!/usr/bin/env python3
"""Export models.csv to data.json (full typed array) + changes.json (day-over-day diff).

This is the JSON export step that feeds the llm-compare web front-end. It reads
the single source of truth (models.csv) and emits a typed JSON snapshot the
static app can load, plus a changes file describing what moved since the last
export (new models, price changes, removals).

Usage: python3 scripts/export_json.py [--csv models.csv] [--out data/]
Designed to run right after generate_readme.py in the daily tracker routine.
Stdlib only. Idempotent.
"""
import csv
import json
import argparse
from pathlib import Path
from datetime import date

KEEP_FIELDS = [
    "id", "name", "org", "license_type", "category", "release_date", "is_open", "notes",
]


def load_models(csv_path):
    models = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            m = {k: (row.get(k, "") or "") for k in KEEP_FIELDS}
            m["prompt_per_m"] = float(row["prompt_per_m"])
            m["completion_per_m"] = float(row["completion_per_m"])
            m["context_length"] = int(row["context_length"])
            m["is_open"] = row["is_open"].strip().lower() == "open"
            m["quality_score"] = int(row.get("quality_score", 0) or 0)
            models.append(m)
    return models


def diff(prev, curr):
    """Compute day-over-day changes between two model arrays (keyed by id)."""
    p = {m["id"]: m for m in prev}
    c = {m["id"]: m for m in curr}
    new = [c[i] for i in c if i not in p]
    removed = [p[i] for i in p if i not in c]
    price_changes = []
    for i in c:
        if i in p:
            old_in, new_in = p[i]["prompt_per_m"], c[i]["prompt_per_m"]
            old_out, new_out = p[i]["completion_per_m"], c[i]["completion_per_m"]
            if old_in != new_in or old_out != new_out:
                price_changes.append({
                    "id": i,
                    "name": c[i]["name"],
                    "old_prompt_per_m": old_in,
                    "new_prompt_per_m": new_in,
                    "old_completion_per_m": old_out,
                    "new_completion_per_m": new_out,
                    "pct_change_prompt": round((new_in - old_in) / old_in * 100, 2) if old_in else None,
                })
    return {
        "date": date.today().isoformat(),
        "new_models": [{"id": m["id"], "name": m["name"], "org": m["org"]} for m in new],
        "removed_models": [{"id": m["id"], "name": m["name"]} for m in removed],
        "price_changes": price_changes,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default="models.csv")
    ap.add_argument("--out", default="data")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    data_path = out_dir / "data.json"
    changes_path = out_dir / "changes.json"

    prev = []
    if data_path.exists():
        try:
            prev = json.loads(data_path.read_text(encoding="utf-8")).get("models", [])
        except Exception:
            prev = []

    models = load_models(args.csv)
    payload = {
        "generated": date.today().isoformat(),
        "count": len(models),
        "models": models,
    }
    data_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    changes = diff(prev, models)
    changes_path.write_text(json.dumps(changes, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"data.json: {len(models)} models -> {data_path}")
    print(f"changes.json: +{len(changes['new_models'])} new, "
          f"-{len(changes['removed_models'])} removed, "
          f"{len(changes['price_changes'])} price changes -> {changes_path}")


if __name__ == "__main__":
    main()
