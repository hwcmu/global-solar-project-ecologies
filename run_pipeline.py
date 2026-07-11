#!/usr/bin/env python3
"""Execute the public analysis notebooks in order from the repository root."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

import nbformat
from nbclient import NotebookClient


ROOT = Path(__file__).resolve().parent
NOTEBOOK_DIR = ROOT / "notebooks"
OUTPUT_DIR = ROOT / "artifacts" / "executed_notebooks"
NOTEBOOKS = [
    "01_retained_base_tables.ipynb",
    "02_core_matrices_and_normalization.ipynb",
    "03_community_detection_and_camp_summaries.ipynb",
    "04_null_model_confirmation.ipynb",
    "05_mode_distinction_audit.ipynb",
    "06_count_camp_merge_audit.ipynb",
    "07_sensitivity_suite.ipynb",
    "08_figure_table_source_assembly.ipynb",
    "09_manuscript_figures.ipynb",
]


def execute_notebook(name: str, timeout: int) -> None:
    source = NOTEBOOK_DIR / name
    target = OUTPUT_DIR / name
    notebook = nbformat.read(source, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
    )
    print(f"Running {name}", flush=True)
    client.execute()
    nbformat.write(notebook, target)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--timeout",
        type=int,
        default=1800,
        help="Per-cell timeout in seconds (default: 1800).",
    )
    parser.add_argument(
        "--through",
        choices=NOTEBOOKS,
        help="Stop after this notebook, inclusive.",
    )
    args = parser.parse_args()

    os.environ.setdefault("MPLBACKEND", "Agg")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for name in NOTEBOOKS:
        execute_notebook(name, args.timeout)
        if name == args.through:
            break


if __name__ == "__main__":
    main()

