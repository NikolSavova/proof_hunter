#!/usr/bin/env python3
"""Emit and check the universal V/H cross-cover lift of an additive basis."""

from __future__ import annotations

import argparse
import json

from triangle_predicate import coverage_bits
from typed_predicate import prefix_length
from typed_verify import literal


def additive_prefix(C: set[int]) -> int:
    sums = {a + b for a in C for b in C}
    q = 0
    while q in sums:
        q += 1
    return q


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("basis", type=int, nargs="+")
    parser.add_argument("--direct-t", type=int, nargs="*", default=[2, 4, 6])
    args = parser.parse_args()
    C = set(args.basis)
    if len(C) != len(args.basis) or min(C, default=-1) < 0:
        raise SystemExit("basis must be a nonempty list of distinct nonnegative integers")
    m = additive_prefix(C)
    p = {"I": set(C), "J": set(C), "K": set(), "L0": set(), "L1": set()}
    abstract = prefix_length(coverage_bits(p, m + 32), m + 32)
    checks = [literal(p, t, m) for t in args.direct_t]
    if abstract < m or not all(row["pass"] for row in checks):
        raise RuntimeError((abstract, checks))
    k = len(C)
    print(
        json.dumps(
            {
                "status": "PASS",
                "macro_basis": sorted(C),
                "macro_basis_size": k,
                "macro_range": m - 1,
                "placement": {name: sorted(values) for name, values in p.items()},
                "role_cost": 2 * k,
                "m": m,
                "certified_macro_squares": m,
                "asymptotic_ratio": f"{m}/{4*k*k}",
                "direct_checks": checks,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
