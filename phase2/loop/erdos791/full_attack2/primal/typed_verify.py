#!/usr/bin/env python3
"""Independent abstract and literal verifier for phased macro certificates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from triangle_predicate import coverage_bits
from typed_predicate import NAMES, prefix_length


def load(path: Path) -> tuple[dict[str, set[int]], dict[str, object]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    data = raw.get("placement", raw)
    if not isinstance(data, dict):
        raise ValueError("placement must be an object")
    p = {}
    for name in NAMES:
        values = data.get(name, [])
        if not isinstance(values, list) or any(type(x) is not int or x < 0 for x in values):
            raise ValueError(f"invalid {name}")
        if len(values) != len(set(values)):
            raise ValueError(f"duplicates in {name}")
        p[name] = set(values)
    return p, raw


def basis(p: dict[str, set[int]], t: int) -> set[int]:
    B = t * t
    elementary = {
        "I": set(range(t + 1)),
        "J": {i * t for i in range(t)},
        "K": {i * (t + 1) for i in range(t)},
        "L0": {i * (t - 1) for i in range(t + 1)},
        "L1": {1 + i * (t - 1) for i in range(t + 1)},
    }
    return {x + B * q for name in NAMES for q in p[name] for x in elementary[name]}


def literal(p: dict[str, set[int]], t: int, m: int) -> dict[str, int | bool]:
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
    parser.add_argument("--direct-t", type=int, nargs="*", default=[2, 4, 6])
    args = parser.parse_args()
    p, raw = load(args.certificate)
    m = raw.get("m")
    if type(m) is not int or m <= 0:
        raise ValueError("certificate must state positive integer m")
    prefix = prefix_length(coverage_bits(p, m + 64), m + 64)
    if prefix < m:
        raise ValueError(f"abstract prefix {prefix} below m={m}")
    rows = []
    for t in args.direct_t:
        if t % 2:
            raise ValueError("phase lemmas require even t")
        row = literal(p, t, m)
        if not row["pass"]:
            raise ValueError(row)
        rows.append(row)
    print(
        json.dumps(
            {
                "status": "PASS",
                "certificate": str(args.certificate.resolve()),
                "ell": sum(len(p[name]) for name in NAMES),
                "claimed_m": m,
                "abstract_prefix": prefix,
                "direct_checks": rows,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
