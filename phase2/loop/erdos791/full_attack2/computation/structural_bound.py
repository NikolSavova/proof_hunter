#!/usr/bin/env python3
"""Audit the essential-vertex plus unique-diagonal role-cost lower bound.

For every target q, the phased predicates cover q using at least one pair sum
whose value is exactly q.  Hence a coordinate whose deletion destroys ordinary
sumset coverage needs a role, and a coordinate that is the unique diagonal
representation q=x+x needs two distinct roles.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def unordered_representations(A: tuple[int, ...], q: int) -> list[tuple[int, int]]:
    return [(a, b) for i, a in enumerate(A) for b in A[i:] if a + b == q]


def essential_elements(A: tuple[int, ...], n: int) -> list[int]:
    """Elements x for which deleting x fails to cover [0,n] by two-sums."""
    answer = []
    for x in A:
        reduced = tuple(a for a in A if a != x)
        sums = {a + b for a in reduced for b in reduced}
        if any(q not in sums for q in range(n + 1)):
            answer.append(x)
    return answer


def unique_diagonals(A: tuple[int, ...], n: int) -> list[int]:
    return [
        x
        for x in A
        if 2 * x <= n and unordered_representations(A, 2 * x) == [(x, x)]
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.input.read_text())
    rows = []
    passed = True
    for group in source["rows"]:
        n = int(group["R_k"])
        for record in group["bases"]:
            A = tuple(record["basis"])
            essential = essential_elements(A, n)
            diagonal = unique_diagonals(A, n)
            lower = len(essential) + len(diagonal)
            costs = {
                name: record[name].get("minimum_role_cost")
                for name in ("five_list", "triangle_enhanced", "three_tile")
            }
            row_pass = set(essential) == set(A) and all(
                cost is not None and cost >= lower for cost in costs.values()
            )
            passed &= row_pass
            rows.append(
                {
                    "k": len(A),
                    "range": n,
                    "basis": A,
                    "essential_elements": essential,
                    "unique_diagonals": diagonal,
                    "lower_bound_E_plus_D": lower,
                    "model_costs": costs,
                    "lower_bound_tight_in_all_models": all(
                        cost == lower for cost in costs.values()
                    ),
                    "pass": row_pass,
                }
            )
    result = {
        "status": "PASS" if passed else "FAIL",
        "theorem_scope": (
            "ordinary five-list, carry-triangle five-list, and three-tile; "
            "the proof uses a current-q pair of distinct role types"
        ),
        "rows": rows,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
