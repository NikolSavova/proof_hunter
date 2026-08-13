#!/usr/bin/env python3
"""Search for a counterexample to typed cost <= |A| + unique diagonals.

Enumerates every interval basis A subset [0,n] (with 0,1 forced for n>0)
through a requested n, and asks the exact CP-SAT models for ordinary five-list,
carry-triangle five-list, and three-tile placements with role cost at most
|A|+u(A).  The conjectured inequality would turn the multitype amplifier
bridge into a 3-term-AP/diagonal question.
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path

from ortools.sat.python import cp_model

from phased_role_model import ROLES, build_model


def is_basis(A: tuple[int, ...], n: int) -> bool:
    sums = {x + y for x in A for y in A}
    return all(q in sums for q in range(n + 1))


def unique_diagonals(A: tuple[int, ...], n: int) -> list[int]:
    out = []
    for x in A:
        if 2 * x > n:
            continue
        reps = sum(
            a + b == 2 * x
            for i, a in enumerate(A)
            for b in A[i:]
        )
        if reps == 1:
            out.append(x)
    return out


def feasible(
    A: tuple[int, ...], n: int, bound: int, roles: tuple[str, ...], triangle: bool
) -> tuple[str, float, int | None]:
    model, _, cost = build_model(A, n, allowed_roles=roles, triangle=triangle)
    # build_model installs an objective; this additional constraint asks only
    # whether the conjectured upper bound is attainable.
    model.add(cost <= bound)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 10
    solver.parameters.num_search_workers = 8
    status = solver.solve(model)
    value = int(solver.objective_value) if status in (cp_model.FEASIBLE, cp_model.OPTIMAL) else None
    return solver.status_name(status), solver.wall_time, value


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=14)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = []
    checked = 0
    for n in range(args.through + 1):
        count = 0
        universe = range(2, n + 1)
        for size in ((0,) if n == 0 else range(n)):
            for tail in combinations(universe, size):
                A = (0,) if n == 0 else (0, 1) + tail
                if not is_basis(A, n):
                    continue
                count += 1
                checked += 1
                diagonal = unique_diagonals(A, n)
                audits = {}
                for label, roles, triangle in (
                    ("ordinary_five_list", ROLES, False),
                    ("triangle_enhanced", ROLES, True),
                    ("three_tile", ("I", "J", "K"), False),
                ):
                    status, wall, value = feasible(
                        A, n, len(A) + len(diagonal), roles, triangle
                    )
                    audits[label] = {
                        "solver_status": status,
                        "wall_time": wall,
                        "role_cost_if_feasible": value,
                    }
                if any(
                    row["solver_status"] not in ("OPTIMAL", "FEASIBLE")
                    for row in audits.values()
                ):
                    statuses = {row["solver_status"] for row in audits.values()}
                    next_cost_audits = {}
                    for label, roles, triangle in (
                        ("ordinary_five_list", ROLES, False),
                        ("triangle_enhanced", ROLES, True),
                        ("three_tile", ("I", "J", "K"), False),
                    ):
                        status, wall, value = feasible(
                            A, n, len(A) + len(diagonal) + 1, roles, triangle
                        )
                        next_cost_audits[label] = {
                            "solver_status": status,
                            "wall_time": wall,
                            "role_cost_if_feasible": value,
                        }
                    payload = {
                        "status": "COUNTEREXAMPLE"
                        if statuses == {"INFEASIBLE"}
                        else "MIXED_OR_UNKNOWN",
                        "checked_before_failure": checked,
                        "n": n,
                        "basis": A,
                        "unique_diagonals": diagonal,
                        "bound": len(A) + len(diagonal),
                        "model_audits": audits,
                        "bound_plus_one_audits": next_cost_audits,
                    }
                    text = json.dumps(payload, indent=2) + "\n"
                    if args.output:
                        args.output.write_text(text)
                    print(text, end="")
                    return
        rows.append({"n": n, "bases_checked": count})
        print(f"n={n} bases={count}", flush=True)
    payload = {
        "status": "NO_COUNTEREXAMPLE",
        "scope": f"all interval bases through n={args.through}",
        "total_bases_checked": checked,
        "rows": rows,
    }
    text = json.dumps(payload, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
