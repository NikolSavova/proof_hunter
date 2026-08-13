#!/usr/bin/env python3
"""Enumerate extremal bases through k=9 and audit minimum phased role cost."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

from phased_role_model import ROLES, solve


def is_basis(A: tuple[int, ...], n: int) -> bool:
    mask = sum(1 << x for x in A)
    sums = 0
    for x in A:
        sums |= mask << x
    return sums & ((1 << (n + 1)) - 1) == (1 << (n + 1)) - 1


def bases_for_range(k: int, n: int):
    if k == 1:
        if n == 0:
            yield (0,)
        return
    for tail in combinations(range(2, n + 1), k - 2):
        A = (0, 1) + tail
        if is_basis(A, n):
            yield A


def extremal_bases(k: int) -> tuple[int, list[tuple[int, ...]]]:
    if k == 1:
        return 0, [(0,)]
    # For k=9, range 32 is witnessed below.  It is enough to exclude range 33:
    # any longer-range basis restricts to at most nine useful coordinates at
    # 33 and can be padded inside [0,33].  This avoids scanning the vacuous
    # pair-count interval 34..44.
    pair_bound = 33 if k == 9 else k * (k + 1) // 2 - 1
    for n in range(pair_bound, 0, -1):
        found = list(bases_for_range(k, n))
        if found:
            return n, found
    raise AssertionError(k)


def audit_model(
    A: tuple[int, ...],
    n: int,
    allowed_roles: tuple[str, ...],
    seconds: float,
    seed: int,
    triangle: bool = False,
) -> dict[str, object]:
    optimum = solve(
        A, n, seconds, 8, seed, allowed_roles=allowed_roles, triangle=triangle
    )
    if optimum["status"] != "OPTIMAL":
        return {"optimum": optimum, "forced_duplicate_audit": "NOT_RUN"}
    cost = int(optimum["role_cost"])
    forced = []
    audit_rows = []
    for index, x in enumerate(A):
        check = solve(
            A,
            n,
            seconds,
            8,
            seed + index + 1,
            fixed_cost=cost,
            max_one_role_element=index,
            allowed_roles=allowed_roles,
            triangle=triangle,
        )
        audit_rows.append(
            {
                "element": x,
                "status_with_at_most_one_role": check["status"],
                "wall_seconds": check["wall_seconds"],
            }
        )
        if check["status"] == "INFEASIBLE":
            forced.append(x)
    return {
        "minimum_role_cost": cost,
        "defect_cost_minus_basis_size": cost - len(A),
        "certificate": optimum["placement"],
        "roles_per_element": optimum["roles_per_element"],
        "forced_duplicated_elements_in_every_optimum": forced,
        "forced_duplicate_audit": audit_rows,
        "optimum_status": optimum["status"],
        "verified_prefix": optimum["verified_prefix"],
    }


def unique_diagonal_elements(A: tuple[int, ...], n: int) -> list[int]:
    out = []
    for x in A:
        if 2 * x > n:
            continue
        reps = [
            (a, b)
            for index, a in enumerate(A)
            for b in A[index:]
            if a + b == 2 * x
        ]
        if reps == [(x, x)]:
            out.append(x)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seconds", type=float, default=30)
    args = parser.parse_args()
    rows = []
    for k in range(1, 10):
        n, bases = extremal_bases(k)
        audited = []
        for basis_index, A in enumerate(bases):
            diagonal = unique_diagonal_elements(A, n)
            audited.append(
                {
                    "basis": list(A),
                    "unique_diagonal_elements": diagonal,
                    "symbolic_lower_bound_k_plus_unique_diagonals": len(A)
                    + len(diagonal),
                    "five_list": audit_model(
                        A, n, ROLES, args.seconds, 791000 + 100 * k + basis_index
                    ),
                    "triangle_enhanced": audit_model(
                        A,
                        n,
                        ROLES,
                        args.seconds,
                        793000 + 100 * k + basis_index,
                        triangle=True,
                    ),
                    "three_tile": audit_model(
                        A,
                        n,
                        ("I", "J", "K"),
                        args.seconds,
                        792000 + 100 * k + basis_index,
                    ),
                }
            )
        rows.append(
            {
                "k": k,
                "R_k": n,
                "number_of_extremal_bases": len(bases),
                "bases": audited,
                "five_list_costs": [x["five_list"].get("minimum_role_cost") for x in audited],
                "triangle_enhanced_costs": [
                    x["triangle_enhanced"].get("minimum_role_cost") for x in audited
                ],
                "three_tile_costs": [x["three_tile"].get("minimum_role_cost") for x in audited],
            }
        )
        print(f"k={k} R={n} bases={len(bases)}", flush=True)
    result = {
        "status": "PASS"
        if all(
            model.get("optimum_status") == "OPTIMAL"
            for row in rows
            for basis in row["bases"]
            for model in (
                basis["five_list"],
                basis["triangle_enhanced"],
                basis["three_tile"],
            )
        )
        else "INCOMPLETE",
        "scope": "all interval-range extremal bases for 1<=k<=9",
        "rows": rows,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
