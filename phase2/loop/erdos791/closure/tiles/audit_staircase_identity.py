#!/usr/bin/env python3
"""Finite regression audit for the global staircase obstruction identity."""

from __future__ import annotations

import argparse
import json

from staircase_family import obstruction_terms, parameters


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r-through", type=int, default=40)
    parser.add_argument("--extra-u", type=int, default=40)
    parser.add_argument("--s-factor", type=int, default=8)
    parser.add_argument("--z-through", type=int, default=30)
    args = parser.parse_args()
    checked = 0
    equalities = []
    minimum_gap = None
    minimum_parameters = None
    for r in range(1, args.r_through + 1):
        for u in range(r + 1, r + 2 + args.extra_u):
            for s in range(r, args.s_factor * r + 1):
                for z in range(args.z_through + 1):
                    row = obstruction_terms(r, u, s, z)
                    gap = int(row["gap_85ell2_minus_294m"])
                    checked += 1
                    if gap < 0:
                        raise RuntimeError((r, u, s, z, gap))
                    if minimum_gap is None or gap < minimum_gap:
                        minimum_gap = gap
                        minimum_parameters = [r, u, s, z]
                    if gap == 0:
                        equalities.append([r, u, s, z])
    expected = [[5, 6, 17, 2]]
    if equalities != expected:
        raise RuntimeError(f"unexpected equality cases: {equalities}")
    print(
        json.dumps(
            {
                "status": "PASS",
                "scope": vars(args),
                "tuples_checked": checked,
                "minimum_gap": minimum_gap,
                "minimum_parameters": minimum_parameters,
                "equality_cases": equalities,
                "note": "Finite regression only; the unbounded proof is the identity and case analysis in CLOSURE_RESULT.md.",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
