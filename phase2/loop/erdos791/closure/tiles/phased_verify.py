#!/usr/bin/env python3
"""Independent abstract and literal verifier for four-tile placements."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from phased_predicate import NAMES, coverage_bits, prefix_length


def load(path: Path) -> dict[str, set[int]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if "placement" in raw:
        raw = raw["placement"]
    if not isinstance(raw, dict):
        raise ValueError("certificate must be an object or contain a placement object")
    result: dict[str, set[int]] = {}
    for name in NAMES:
        values = raw.get(name, [])
        if not isinstance(values, list) or any(type(x) is not int or x < 0 for x in values):
            raise ValueError(f"{name} must be a list of nonnegative integers")
        if len(values) != len(set(values)):
            raise ValueError(f"{name} has duplicates")
        result[name] = set(values)
    return result


def basis(p: dict[str, set[int]], t: int) -> set[int]:
    B = t * t
    elementary = {
        "I": set(range(t + 1)),
        "J": {i * t for i in range(t)},
        "K": {i * (t + 1) for i in range(t)},
        "L0": {i * (t - 1) for i in range(t + 1)},
        "L1": {i * (t - 1) + 1 for i in range(t + 1)},
    }
    return {x + B * q for name in NAMES for q in p[name] for x in elementary[name]}


def direct_check(p: dict[str, set[int]], t: int, m: int) -> dict[str, int | bool]:
    A = basis(p, t)
    sums = {x + y for x in A for y in A if x <= y}
    end = m * t * t - 1
    missing = next((x for x in range(end + 1) if x not in sums), None)
    return {
        "t": t,
        "basis_size": len(A),
        "required_through": end,
        "pass": missing is None,
        "first_missing": -1 if missing is None else missing,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--m", type=int)
    parser.add_argument("--direct-t", type=int, nargs="*", default=[2, 4, 6])
    args = parser.parse_args()
    p = load(args.certificate)
    raw = json.loads(args.certificate.read_text(encoding="utf-8"))
    claimed = args.m
    if claimed is None and isinstance(raw, dict):
        for key in ("verified_prefix", "certified_prefix", "target"):
            if type(raw.get(key)) is int:
                claimed = raw[key]
                break
    limit = max(1024, (claimed or 0) + 64)
    abstract_prefix = prefix_length(coverage_bits(p, limit), limit)
    if claimed is None:
        claimed = abstract_prefix
    if abstract_prefix < claimed:
        raise ValueError(f"abstract predicate certifies {abstract_prefix}, below claimed {claimed}")
    rows = []
    for t in args.direct_t:
        if t % 2:
            raise ValueError("the reflected-diagonal phase lemma requires even t")
        row = direct_check(p, t, claimed)
        if not row["pass"]:
            raise ValueError(f"literal check failed: {row}")
        rows.append(row)
    print(
        json.dumps(
            {
                "status": "PASS",
                "certificate": str(args.certificate.resolve()),
                "ell": sum(len(p[name]) for name in NAMES),
                "claimed_m": claimed,
                "abstract_prefix": abstract_prefix,
                "direct_checks": rows,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
