"""Audit source files without assuming their schema or joining records."""
import argparse
from pathlib import Path
import hashlib
import pandas as pd
import yaml

TABLE_EXTENSIONS = {".csv", ".tsv", ".parquet"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inspect_table(path: Path) -> dict:
    try:
        if path.suffix.lower() == ".csv":
            df = pd.read_csv(path, low_memory=False)
        elif path.suffix.lower() == ".tsv":
            df = pd.read_csv(path, sep="\\t", low_memory=False)
        else:
            df = pd.read_parquet(path)
        return {
            "file": str(path),
            "sha256": sha256(path),
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "column_names": list(map(str, df.columns)),
            "missing_by_column": {str(k): int(v) for k, v in df.isna().sum().items()},
            "duplicate_rows": int(df.duplicated().sum()),
        }
    except Exception as exc:
        return {"file": str(path), "sha256": sha256(path), "error": str(exc)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/dataset_config.yaml")
    args = parser.parse_args()

    config = yaml.safe_load(Path(args.config).read_text())
    lines = ["# Dataset source audit", "", "Generated file inventory and tabular audit.", ""]
    for key, source in config.get("sources", {}).items():
        root = Path(source["path"])
        lines += [f"## {source.get('description', key)}", "", f"- Source URL: {source.get('url', 'not supplied')}", f"- Local path: `{root}`", ""]
        if not root.exists():
            lines += ["Status: **not found locally**. Download the source and update the path if needed.", ""]
            continue
        found = False
        for path in sorted(p for p in root.rglob("*") if p.is_file()):
            found = True
            if path.suffix.lower() in TABLE_EXTENSIONS:
                info = inspect_table(path)
                lines += [f"### `{path.name}`", "", f"- SHA-256: `{info['sha256']}`"]
                if "error" in info:
                    lines += [f"- Read error: {info['error']}", ""]
                    continue
                lines += [f"- Rows: {info['rows']}", f"- Columns: {info['columns']}", f"- Duplicate rows: {info['duplicate_rows']}", "- Column names:"]
                lines += [f"  - `{c}`" for c in info["column_names"]]
                lines += ["", "Missing values:"]
                lines += [f"- `{c}`: {n}" for c, n in info["missing_by_column"].items()]
                lines += [""]
            else:
                lines += [f"- File: `{path}` | bytes: {path.stat().st_size} | SHA-256: `{sha256(path)}`"]
        if not found:
            lines += ["No files found under this path.", ""]
    out = Path(config.get("outputs", {}).get("audit_report", "reports/dataset_audit.md"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
