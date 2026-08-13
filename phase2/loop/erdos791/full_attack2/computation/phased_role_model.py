#!/usr/bin/env python3
"""Exact minimum-role model for the five-list phased amplifier predicate.

Given a fixed finite integer set A and target prefix [0,n], each element of A
may carry any subset of the roles I,J,K,L0,L1.  The objective is the total
number of carried roles.  Pair-sum variables are channeled in both directions,
and every target is required to satisfy the exact five-list predicate.

This is a representation-hypergraph problem: coordinates are fixed.  It does
not search for a new additive basis.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Iterable

from ortools.sat.python import cp_model


ROLES = ("I", "J", "K", "L0", "L1")
PAIR_SPECS = (
    ("ij", "I", "J"),
    ("ik", "I", "K"),
    ("il0", "I", "L0"),
    ("jk", "J", "K"),
    ("jl0", "J", "L0"),
    ("il1", "I", "L1"),
    ("jl1", "J", "L1"),
    ("kl0", "K", "L0"),
    ("kl1", "K", "L1"),
)


def representation_indices(A: tuple[int, ...], n: int) -> list[list[tuple[int, int]]]:
    reps: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    index = {x: i for i, x in enumerate(A)}
    for i, x in enumerate(A):
        for y in A:
            q = x + y
            if q <= n:
                reps[q].append((i, index[y]))
    return reps


def pair_sums(left: set[int], right: set[int]) -> set[int]:
    return {x + y for x in left for y in right}


def phased_coverage(placement: dict[str, set[int]]) -> set[int]:
    I, J, K, L0, L1 = (placement[name] for name in ROLES)
    sums = {
        label: pair_sums(placement[left], placement[right])
        for label, left, right in PAIR_SPECS
    }
    adjacent = lambda s: {q for q in s if q - 1 in s}
    return (
        sums["ij"]
        | sums["ik"]
        | sums["il0"]
        | adjacent(sums["jk"])
        | adjacent(sums["jl0"])
        | {q for q in sums["il1"] if q - 1 in sums["il0"]}
        | adjacent(sums["il1"])
        | {q for q in sums["jl0"] if q - 1 in sums["jl1"]}
        | adjacent(sums["jl1"])
        | {q for q in sums["kl1"] if q - 1 in sums["kl0"]}
        | {q for q in sums["kl0"] if q - 1 in sums["kl1"]}
    )


def triangle_coverage(placement: dict[str, set[int]]) -> set[int]:
    covered = phased_coverage(placement)
    jk = pair_sums(placement["J"], placement["K"])
    jl0 = pair_sums(placement["J"], placement["L0"])
    kl0 = pair_sums(placement["K"], placement["L0"])
    covered |= {
        q
        for q in jk & jl0
        if q - 1 in kl0
    }
    covered |= {
        q
        for q in kl0
        if q - 1 in jk and q - 1 in jl0
    }
    return covered


def prefix_length(covered: set[int]) -> int:
    q = 0
    while q in covered:
        q += 1
    return q


def and_var(
    model: cp_model.CpModel, terms: Iterable[cp_model.IntVar], name: str
) -> cp_model.IntVar:
    terms = list(terms)
    out = model.new_bool_var(name)
    for term in terms:
        model.add_implication(out, term)
    model.add_bool_or([out, *(term.Not() for term in terms)])
    return out


def or_channel(
    model: cp_model.CpModel, terms: list[cp_model.IntVar], name: str
) -> cp_model.IntVar:
    out = model.new_bool_var(name)
    if not terms:
        model.add(out == 0)
        return out
    for term in terms:
        model.add_implication(term, out)
    model.add_bool_or(terms).only_enforce_if(out)
    return out


def build_model(
    A: tuple[int, ...],
    n: int,
    fixed_cost: int | None = None,
    max_one_role_element: int | None = None,
    allowed_roles: tuple[str, ...] = ROLES,
    triangle: bool = False,
) -> tuple[cp_model.CpModel, dict[str, list[cp_model.IntVar]], cp_model.LinearExpr]:
    model = cp_model.CpModel()
    role = {
        name: [model.new_bool_var(f"role.{name}.{i}") for i in range(len(A))]
        for name in ROLES
    }
    for name in ROLES:
        if name not in allowed_roles:
            for variable in role[name]:
                model.add(variable == 0)
    reps = representation_indices(A, n)
    present: dict[str, list[cp_model.IntVar]] = {label: [] for label, _, _ in PAIR_SPECS}
    for label, left, right in PAIR_SPECS:
        for q in range(n + 1):
            witnesses = [
                and_var(
                    model,
                    (role[left][i], role[right][j]),
                    f"w.{label}.{q}.{i}.{j}",
                )
                for i, j in reps[q]
            ]
            present[label].append(or_channel(model, witnesses, f"sum.{label}.{q}"))

    for q in range(n + 1):
        alternatives = [present["ij"][q], present["ik"][q], present["il0"][q]]
        if q:
            alternatives.extend(
                and_var(
                    model,
                    (present[label][q - 1], present[label][q]),
                    f"cover.consecutive.{label}.{q}",
                )
                for label in ("jk", "jl0", "il1", "jl1")
            )
            if triangle:
                alternatives.extend(
                    (
                        and_var(
                            model,
                            (
                                present["jk"][q],
                                present["jl0"][q],
                                present["kl0"][q - 1],
                            ),
                            f"cover.triangle.upper.{q}",
                        ),
                        and_var(
                            model,
                            (
                                present["jk"][q - 1],
                                present["jl0"][q - 1],
                                present["kl0"][q],
                            ),
                            f"cover.triangle.lower.{q}",
                        ),
                    )
                )
            alternatives.extend(
                (
                    and_var(
                        model,
                        (present["il0"][q - 1], present["il1"][q]),
                        f"cover.il01.{q}",
                    ),
                    and_var(
                        model,
                        (present["jl1"][q - 1], present["jl0"][q]),
                        f"cover.jl10.{q}",
                    ),
                    and_var(
                        model,
                        (present["kl0"][q - 1], present["kl1"][q]),
                        f"cover.kl01.{q}",
                    ),
                    and_var(
                        model,
                        (present["kl1"][q - 1], present["kl0"][q]),
                        f"cover.kl10.{q}",
                    ),
                )
            )
        model.add_bool_or(alternatives)

    cost = sum(role[name][i] for name in ROLES for i in range(len(A)))
    if fixed_cost is None:
        model.minimize(cost)
    else:
        model.add(cost == fixed_cost)
    if max_one_role_element is not None:
        model.add(sum(role[name][max_one_role_element] for name in ROLES) <= 1)
    return model, role, cost


def solve(
    A: tuple[int, ...],
    n: int,
    seconds: float,
    workers: int,
    seed: int,
    fixed_cost: int | None = None,
    max_one_role_element: int | None = None,
    allowed_roles: tuple[str, ...] = ROLES,
    triangle: bool = False,
) -> dict[str, object]:
    model, role, cost = build_model(
        A, n, fixed_cost, max_one_role_element, allowed_roles, triangle
    )
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = seed
    solver.parameters.symmetry_level = 3
    solver.parameters.cp_model_presolve = True
    started = time.monotonic()
    status_code = solver.solve(model)
    status = solver.status_name(status_code)
    result: dict[str, object] = {
        "status": status,
        "wall_seconds": time.monotonic() - started,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
        "best_objective_bound": solver.best_objective_bound,
        "basis": list(A),
        "basis_size": len(A),
        "target_n": n,
        "fixed_cost": fixed_cost,
        "max_one_role_element": None
        if max_one_role_element is None
        else A[max_one_role_element],
        "allowed_roles": list(allowed_roles),
        "carry_triangle": triangle,
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        placement = {
            name: {A[i] for i in range(len(A)) if solver.value(role[name][i])}
            for name in ROLES
        }
        verified_prefix = prefix_length(
            triangle_coverage(placement) if triangle else phased_coverage(placement)
        )
        if verified_prefix <= n:
            raise RuntimeError(f"decoded assignment fails at {verified_prefix}")
        result.update(
            {
                "role_cost": int(solver.value(cost)),
                "placement": {name: sorted(placement[name]) for name in ROLES},
                "roles_per_element": {
                    str(x): [name for name in ROLES if x in placement[name]] for x in A
                },
                "verified_prefix": verified_prefix,
                "duplicated_elements": [
                    x for x in A if sum(x in placement[name] for name in ROLES) >= 2
                ],
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--basis", type=int, nargs="+", required=True)
    parser.add_argument("--target-n", type=int, required=True)
    parser.add_argument("--seconds", type=float, default=300)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=791)
    parser.add_argument("--fixed-cost", type=int)
    parser.add_argument("--max-one-role-element", type=int)
    parser.add_argument(
        "--three-tile",
        action="store_true",
        help="restrict roles to I,J,K (set L0=L1 empty)",
    )
    parser.add_argument("--triangle", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    A = tuple(sorted(set(args.basis)))
    if len(A) != len(args.basis) or A[0] < 0:
        raise SystemExit("basis must contain distinct nonnegative integers")
    index = None
    if args.max_one_role_element is not None:
        try:
            index = A.index(args.max_one_role_element)
        except ValueError as exc:
            raise SystemExit("--max-one-role-element is not in basis") from exc
    result = solve(
        A,
        args.target_n,
        args.seconds,
        args.workers,
        args.seed,
        args.fixed_cost,
        index,
        ("I", "J", "K") if args.three_tile else ROLES,
        args.triangle,
    )
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
