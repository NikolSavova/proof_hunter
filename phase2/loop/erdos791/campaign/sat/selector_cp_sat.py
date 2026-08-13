#!/usr/bin/env python3
"""Exact CP-SAT model using sorted coordinates and selectable witnesses.

The original membership model creates one Boolean product for essentially
every (type pair, target sum, summand).  This formulation represents the 42
chosen coordinates directly, forms the 561 pair-sum integer variables for the
fixed (8,17,17) split, and lets each target square select a literal pair-sum
witness.  It encodes exactly the same sufficient three-tile predicate:

    q in I+J or q in I+K or ({q-1,q} subset J+K).

An INFEASIBLE result is exact for the stated coordinate/count/radius model,
but OR-Tools does not produce an independently checkable proof certificate.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from ortools.sat.python import cp_model

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT))
from verifier import DEFAULT_CERTIFICATE, load_certificate, prefix_length, tile_coverage  # noqa: E402


def sorted_coordinates(
    model: cp_model.CpModel, name: str, count: int, bound: int
) -> list[cp_model.IntVar]:
    values = [model.new_int_var(i, bound - count + i + 1, f"{name}_{i}") for i in range(count)]
    for left, right in zip(values, values[1:]):
        model.add(left < right)
    return values


def pair_sums(
    model: cp_model.CpModel,
    left: list[cp_model.IntVar],
    right: list[cp_model.IntVar],
    bound: int,
    label: str,
) -> list[cp_model.IntVar]:
    sums: list[cp_model.IntVar] = []
    for a, x in enumerate(left):
        for b, y in enumerate(right):
            value = model.new_int_var(0, 2 * bound, f"{label}_{a}_{b}")
            model.add(value == x + y)
            sums.append(value)
    return sums


def select_equal(
    model: cp_model.CpModel,
    candidates: list[cp_model.IntVar],
    target: int,
    label: str,
    active: cp_model.IntVar | None = None,
    active_value: int = 1,
) -> cp_model.IntVar:
    """Select a candidate equal to target when active; a sentinel otherwise."""
    sentinel = len(candidates)
    index = model.new_int_var(0, sentinel, f"pick_{label}")
    # The constant sentinel makes the element equality tautological while the
    # witness family is inactive.  This avoids unenforceable Element wrappers.
    model.add_element(index, [*candidates, target], target)
    if active is None:
        model.add(index < sentinel)
    elif active_value:
        model.add(index < sentinel).only_enforce_if(active)
        model.add(index == sentinel).only_enforce_if(active.negated())
    else:
        model.add(index < sentinel).only_enforce_if(active.negated())
        model.add(index == sentinel).only_enforce_if(active)
    return index


def contains_seed_value(
    model: cp_model.CpModel,
    coordinates: list[cp_model.IntVar],
    value: int,
    label: str,
) -> cp_model.IntVar:
    equalities: list[cp_model.IntVar] = []
    for i, coordinate in enumerate(coordinates):
        equal = model.new_bool_var(f"retain_eq_{label}_{value}_{i}")
        model.add(coordinate == value).only_enforce_if(equal)
        model.add(coordinate != value).only_enforce_if(equal.negated())
        equalities.append(equal)
    retained = model.new_bool_var(f"retain_{label}_{value}")
    # Strict sorting means at most one equality can hold.
    model.add(sum(equalities) == retained)
    return retained


def solve(args: argparse.Namespace) -> dict[str, object]:
    started = time.monotonic()
    model = cp_model.CpModel()
    counts = {"I": args.i_count, "J": args.j_count, "K": args.k_count}
    if sum(counts.values()) != args.ell:
        raise ValueError("type counts must sum to ell")
    if args.coordinate_bound < args.target_m - 1:
        raise ValueError("coordinate bound must be at least target_m-1")

    coordinates = {
        name: sorted_coordinates(model, name, count, args.coordinate_bound)
        for name, count in counts.items()
    }
    I, J, K = (coordinates[name] for name in ("I", "J", "K"))

    # Square zero forces 0 in I and in J or K; exchange J,K to put it in J.
    model.add(I[0] == 0)
    model.add(J[0] == 0)

    direct = [
        *pair_sums(model, I, J, args.coordinate_bound, "IJ"),
        *pair_sums(model, I, K, args.coordinate_bound, "IK"),
    ]
    jk = pair_sums(model, J, K, args.coordinate_bound, "JK")

    modes: list[cp_model.IntVar] = []
    picks: list[cp_model.IntVar] = []
    picks.append(select_equal(model, direct, 0, "direct_0"))
    for q in range(1, args.target_m):
        is_direct = model.new_bool_var(f"direct_mode_{q}")
        modes.append(is_direct)
        picks.append(select_equal(model, direct, q, f"direct_{q}", is_direct, 1))
        picks.append(select_equal(model, jk, q - 1, f"jk_prev_{q}", is_direct, 0))
        picks.append(select_equal(model, jk, q, f"jk_here_{q}", is_direct, 0))

    seed = load_certificate(DEFAULT_CERTIFICATE)
    # The published certificate has 0 in K, whereas the model normalizes the
    # interchangeable names so 0 is in J.  Radius must be measured after that
    # same swap.  (The older membership model omitted this normalization of
    # the seed, so its reported local-radius conclusion is not about the true
    # radius around Kohonen's placement.)
    if 0 not in seed["J"] and 0 in seed["K"]:
        if args.j_count != args.k_count:
            raise ValueError("cannot normalize J/K seed orientation with unequal type counts")
        seed = dict(seed)
        seed["J"], seed["K"] = seed["K"], seed["J"]
    retained: list[cp_model.IntVar] = []
    seed_counts_match = all(len(seed[name]) == counts[name] for name in ("I", "J", "K"))
    if args.max_replacements_from_seed is not None and not seed_counts_match:
        raise ValueError("seed radius requires the normalized Kohonen type counts (8,17,17)")
    if seed_counts_match:
        for name in ("I", "J", "K"):
            seed_values = seed[name]
            assert isinstance(seed_values, list)
            if args.max_replacements_from_seed is not None:
                retained.extend(
                    contains_seed_value(model, coordinates[name], value, name)
                    for value in seed_values
                )
            for i, coordinate in enumerate(coordinates[name]):
                model.add_hint(coordinate, seed_values[i])

    if args.max_replacements_from_seed is not None:
        model.add(args.ell - sum(retained) <= args.max_replacements_from_seed)

    # Valid symmetry break when both J and K contain zero.  If only J does,
    # the normalization above has already selected the orientation.
    if args.j_count == args.k_count:
        k_has_zero = model.new_bool_var("K_has_zero")
        model.add(K[0] == 0).only_enforce_if(k_has_zero)
        model.add(K[0] != 0).only_enforce_if(k_has_zero.negated())
        model.add(sum(J) <= sum(K)).only_enforce_if(k_has_zero)

    # The coordinate decisions carry the mathematical content.  Ask CP-SAT to
    # branch on them before the redundant choice of coverage witnesses.
    model.add_decision_strategy(
        [*I, *J, *K],
        cp_model.CHOOSE_LOWEST_MIN,
        cp_model.SELECT_MIN_VALUE,
    )

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.log_search_progress = args.log_progress
    solver.parameters.search_branching = cp_model.PORTFOLIO_SEARCH
    status_code = solver.solve(model)
    elapsed = time.monotonic() - started
    status = solver.status_name(status_code)
    result: dict[str, object] = {
        "formulation": "sorted-coordinate selectable-witness CP-SAT",
        "status": status,
        "target_m": args.target_m,
        "ell": args.ell,
        "fixed_type_counts": [args.i_count, args.j_count, args.k_count],
        "coordinate_bound": args.coordinate_bound,
        "max_replacements_from_seed": args.max_replacements_from_seed,
        "random_seed": args.seed,
        "workers": args.workers,
        "wall_seconds": elapsed,
        "solver_wall_seconds": solver.wall_time,
        "conflicts": solver.num_conflicts,
        "branches": solver.num_branches,
        "scope": "Exact for the sufficient three-tile predicate and stated finite domain/count/radius constraints; no external UNSAT proof is emitted.",
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        placement = {
            name: [solver.value(value) for value in values]
            for name, values in coordinates.items()
        }
        prefix = prefix_length(tile_coverage(placement["I"], placement["J"], placement["K"]))
        if prefix < args.target_m:
            raise RuntimeError(f"independent in-process verification failed: prefix={prefix}")
        result["placement"] = placement
        result["verified_prefix"] = prefix
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-m", type=int, default=511)
    parser.add_argument("--coordinate-bound", type=int, default=510)
    parser.add_argument("--ell", type=int, default=42)
    parser.add_argument("--i-count", type=int, default=8)
    parser.add_argument("--j-count", type=int, default=17)
    parser.add_argument("--k-count", type=int, default=17)
    parser.add_argument("--max-replacements-from-seed", type=int)
    parser.add_argument("--seconds", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=791)
    parser.add_argument("--log-progress", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = solve(args)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
