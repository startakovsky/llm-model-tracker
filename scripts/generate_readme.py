#!/usr/bin/env python3
"""Generate README.md and index files from models.csv.

Usage: python3 scripts/generate_readme.py [--csv path/to/models.csv]
"""
import csv
import argparse
from pathlib import Path
from datetime import date


def load_models(csv_path):
    models = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["prompt_per_m"] = float(row["prompt_per_m"])
            row["completion_per_m"] = float(row["completion_per_m"])
            row["context_length"] = int(row["context_length"])
            row["is_open"] = row["is_open"].lower() == "open"
            row["quality_score"] = int(row.get("quality_score", 0) or 0)
            models.append(row)
    return models


def fmt_price(m):
    return f"${m['prompt_per_m']:.2f}+${m['completion_per_m']:.2f}/M"


def fmt_ctx(m):
    c = m["context_length"]
    if c >= 1_000_000:
        return f"{c/1_000_000:.0f}M"
    return f"{c//1000}K"


def fmt_date(m):
    d = m.get("release_date", "")
    if not d:
        return "?"
    parts = d.split("-")
    if len(parts) >= 2:
        return f"{parts[0]}-{parts[1]}"
    return d


def sort_key(m):
    """Sort by quality_score descending, then by release_date descending."""
    return (m.get("quality_score", 0), m.get("release_date", ""))


def generate_readme(models, output_dir):
    today = date.today().isoformat()

    open_models = [m for m in models if m["is_open"]]
    closed_models = [m for m in models if not m["is_open"]]

    open_sorted = sorted(open_models, key=sort_key, reverse=True)
    closed_sorted = sorted(closed_models, key=sort_key, reverse=True)

    open_top10 = open_sorted[:10]
    closed_top10 = closed_sorted[:10]

    lines = []
    lines.append("# LLM Model Tracker")
    lines.append("")
    lines.append(f"Daily-updated tracker of top LLMs. Open and closed source. Last updated: {today}")
    lines.append("")
    lines.append("## Top 10 Open-Source Models")
    lines.append("")
    lines.append("| # | Model | Org | Category | Context | OR Price | Released | Score | Notes |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for i, m in enumerate(open_top10, 1):
        lines.append(f"| {i} | [{m['name']}](open/{m['id'].split('/')[-1]}.md) | {m['org']} | {m.get('category','')} | {fmt_ctx(m)} | {fmt_price(m)} | {fmt_date(m)} | {m.get('quality_score','')} | {m.get('notes','')} |")

    lines.append("")
    lines.append("## Top 10 Closed-Source Models")
    lines.append("")
    lines.append("| # | Model | Org | Context | OR Price | Released | Score | Notes |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for i, m in enumerate(closed_top10, 1):
        lines.append(f"| {i} | [{m['name']}](closed/{m['id'].split('/')[-1]}.md) | {m['org']} | {fmt_ctx(m)} | {fmt_price(m)} | {fmt_date(m)} | {m.get('quality_score','')} | {m.get('notes','')} |")

    lines.append("")
    lines.append("## Full Index")
    lines.append("")
    lines.append(f"- [Open-source models ({len(open_models)})](INDEX-OPEN.md)")
    lines.append(f"- [Closed-source models ({len(closed_models)})](INDEX-CLOSED.md)")
    lines.append(f"- [Raw CSV data](models.csv)")
    lines.append("")

    readme_path = Path(output_dir) / "README.md"
    readme_path.write_text("\n".join(lines), encoding="utf-8")
    return readme_path


def generate_open_index(models, output_dir):
    open_models = [m for m in models if m["is_open"]]
    open_models.sort(key=sort_key, reverse=True)

    lines = []
    lines.append("# Open-Source LLM Index")
    lines.append("")
    lines.append(f"{len(open_models)} models. Sorted by quality score.")
    lines.append("")
    lines.append("| Model | Org | Category | Context | OR Price | Released | Score | Self-Host? | Notes |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for m in open_models:
        host = "Yes" if m.get("category") in ("Self-hostable", "Lightweight") else "Large"
        lines.append(f"| [{m['name']}](open/{m['id'].split('/')[-1]}.md) | {m['org']} | {m.get('category','')} | {fmt_ctx(m)} | {fmt_price(m)} | {fmt_date(m)} | {m.get('quality_score','')} | {host} | {m.get('notes','')} |")

    path = Path(output_dir) / "INDEX-OPEN.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def generate_closed_index(models, output_dir):
    closed_models = [m for m in models if not m["is_open"]]
    closed_models.sort(key=sort_key, reverse=True)

    lines = []
    lines.append("# Closed-Source LLM Index")
    lines.append("")
    lines.append(f"{len(closed_models)} models. Sorted by quality score.")
    lines.append("")
    lines.append("| Model | Org | Context | OR Price | Released | Score | Notes |")
    lines.append("|---|---|---|---|---|---|---|")
    for m in closed_models:
        lines.append(f"| [{m['name']}](closed/{m['id'].split('/')[-1]}.md) | {m['org']} | {fmt_ctx(m)} | {fmt_price(m)} | {fmt_date(m)} | {m.get('quality_score','')} | {m.get('notes','')} |")

    path = Path(output_dir) / "INDEX-CLOSED.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def main():
    parser = argparse.ArgumentParser(description="Generate README and index files from models.csv")
    parser.add_argument("--csv", default="models.csv", help="Path to models.csv")
    parser.add_argument("--output", default=".", help="Output directory")
    args = parser.parse_args()

    models = load_models(args.csv)
    readme = generate_readme(models, args.output)
    open_idx = generate_open_index(models, args.output)
    closed_idx = generate_closed_index(models, args.output)

    print(f"Generated: {readme}, {open_idx}, {closed_idx}")


if __name__ == "__main__":
    main()
