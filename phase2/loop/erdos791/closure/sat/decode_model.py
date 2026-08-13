#!/usr/bin/env python3
"""Decode a DIMACS SAT model using exact_cnf.py metadata."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("metadata", type=Path)
    parser.add_argument("model", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    metadata = json.loads(args.metadata.read_text())
    text = args.model.read_text(errors="replace")
    if not re.search(r"(^|\n)s\s+SATISFIABLE", text):
        raise SystemExit("model does not contain an s SATISFIABLE line")
    true_vars: set[int] = set()
    for line in text.splitlines():
        if line.startswith("v "):
            true_vars.update(x for x in map(int, line[2:].split()) if x > 0)
    membership = metadata["membership_variables"]
    certificate: dict[str, object] = {
        family: [p for p, var in enumerate(membership[family]) if var in true_vars]
        for family in ("I", "J", "K")
    }
    certificate["ell"] = metadata["ell"]
    certificate["m"] = metadata["m"]
    encoded = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
