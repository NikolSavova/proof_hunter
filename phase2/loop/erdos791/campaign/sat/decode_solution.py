#!/usr/bin/env python3
"""Decode DIMACS membership variables to a verifier-compatible certificate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metadata", type=Path)
    parser.add_argument("solution", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
    positive: set[int] = set()
    status = None
    for line in args.solution.read_text(encoding="ascii").splitlines():
        if line.startswith("s "):
            status = line[2:].strip()
        elif line.startswith("v "):
            positive.update(value for value in map(int, line[2:].split()) if value > 0)
    if status != "SATISFIABLE":
        raise ValueError(f"solution status is {status!r}, not SATISFIABLE")
    placement = {
        name: sorted(
            int(position)
            for position, variable in mapping.items()
            if int(variable) in positive
        )
        for name, mapping in metadata["chosen_variables"].items()
    }
    certificate = {
        "name": "decoded-DIMACS-placement",
        "ell": sum(map(len, placement.values())),
        "m": metadata["target_m"],
        **placement,
    }
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
