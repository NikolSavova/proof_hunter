#!/usr/bin/env python3
"""Exact CP-SAT feasibility model for the generalized-Mrose tile criterion.

This asks whether placement sets I,J,K certify every square 0,...,m-1 via

    q in I+J  or  q in I+K  or  (q-1 and q both in J+K).

Unlike ``search.py``, a solver result of INFEASIBLE is an exact solver
conclusion relative to the chosen coordinate bound and type counts.  OR-Tools
does not emit an independently checkable UNSAT proof here; UNKNOWN is only a
bounded attempt.
OR-Tools is deliberately an optional dependency; see README.md.
"""

from __future__ import annotations

import argparse
import json
import time
from pathlib import Path

from ortools.sat.python import cp_model

from verifier import DEFAULT_CERTIFICATE, load_certificate, prefix_length, tile_coverage


def and_var(
    model: cp_model.CpModel,
    left: cp_model.IntVar,
    right: cp_model.IntVar,
    name: str,
) -> cp_model.IntVar:
    """Return a Boolean constrained to equal ``left AND right``."""
    out = model.new_bool_var(name)
    model.add(out <= left)
    model.add(out <= right)
    model.add(out >= left + right - 1)
    return out


def pair_sum_witness_vars(
    model: cp_model.CpModel,
    left: list[cp_model.IntVar],
    right: list[cp_model.IntVar],
    target_m: int,
    label: str,
) -> list[list[cp_model.IntVar]]:
    """Conjunction witnesses, grouped by their sum q < target_m."""
    grouped: list[list[cp_model.IntVar]] = [[] for _ in range(target_m)]
    for q in range(target_m):
        for a in range(q + 1):
            if a < len(left) and q - a < len(right):
                grouped[q].append(
                    and_var(model, left[a], right[q - a], f"{label}_{q}_{a}")
                )
    return grouped


def solve(args: argparse.Namespace) -> dict[str, object]:
    target_m = args.target_m
    coordinate_bound = args.coordinate_bound
    if coordinate_bound < target_m - 1:
        raise ValueError("coordinate bound must be at least target_m-1")

    model = cp_model.CpModel()
    names = ("I", "J", "K")
    chosen = {
        name: [model.new_bool_var(f"{name}_{p}") for p in range(coordinate_bound + 1)]
        for name in names
    }

    if args.free_type_counts:
        model.add(sum(chosen[name][p] for name in names for p in range(coordinate_bound + 1)) == args.ell)
    else:
        counts = (args.i_count, args.j_count, args.k_count)
        if sum(counts) != args.ell:
            raise ValueError("fixed type counts must sum to ell")
        for name, count in zip(names, counts):
            model.add(sum(chosen[name]) == count)

    # Square zero forces 0 in I and in J or K.  Exchanging H and S lets us
    # normalize the latter choice to J without losing any placement.
    model.add(chosen["I"][0] == 1)
    model.add(chosen["J"][0] == 1)

    ij = pair_sum_witness_vars(model, chosen["I"], chosen["J"], target_m, "ij")
    ik = pair_sum_witness_vars(model, chosen["I"], chosen["K"], target_m, "ik")
    jk_witnesses = pair_sum_witness_vars(model, chosen["J"], chosen["K"], target_m, "jk")

    jk_sum: list[cp_model.IntVar] = []
    for q, witnesses in enumerate(jk_witnesses):
        present = model.new_bool_var(f"jk_sum_{q}")
        for witness in witnesses:
            model.add_implication(witness, present)
        model.add_bool_or(witnesses).only_enforce_if(present)
        jk_sum.append(present)

    for q in range(target_m):
        alternatives = [*ij[q], *ik[q]]
        if q > 0:
            consecutive = and_var(model, jk_sum[q - 1], jk_sum[q], f"jk_consecutive_{q}")
            alternatives.append(consecutive)
        model.add_bool_or(alternatives)

    seed = load_certificate(DEFAULT_CERTIFICATE)
    if args.max_replacements_from_seed is not None:
        if args.free_type_counts:
            raise ValueError("seed-replacement radius currently requires fixed type counts")
        differences = []
        for name in names:
            seed_values = set(seed[name])
            differences.extend(
                variable if p not in seed_values else 1 - variable
                for p, variable in enumerate(chosen[name])
            )
        # With fixed type counts, replacing one coordinate flips exactly two
        # membership bits.  This constraint includes every placement reachable
        # by at most the stated number of arbitrary coordinate replacements.
        model.add(sum(differences) <= 2 * args.max_replacements_from_seed)
    for name in names:
        seed_values = set(seed[name])
        for p, variable in enumerate(chosen[name]):
            model.add_hint(variable, int(p in seed_values))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.log_search_progress = args.log_progress
    started = time.monotonic()
    status_code = solver.solve(model)
    elapsed = time.monotonic() - started
    status = solver.status_name(status_code)
    result: dict[str, object] = {
        "status": status,
        "target_m": target_m,
        "ell": args.ell,
        "coordinate_bound": coordinate_bound,
        "free_type_counts": args.free_type_counts,
        "fixed_type_counts": None if args.free_type_counts else [args.i_count, args.j_count, args.k_count],
        "max_replacements_from_seed": args.max_replacements_from_seed,
        "wall_seconds": elapsed,
        "solver_wall_seconds": solver.wall_time,
        "conflicts": solver.num_conflicts,
        "branches": solver.num_branches,
        "scope": "Exact for the sufficient three-tile coverage predicate and stated finite domain/count constraints.",
    }
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        placement = {
            name: [p for p, variable in enumerate(chosen[name]) if solver.value(variable)]
            for name in names
        }
        covered = tile_coverage(placement["I"], placement["J"], placement["K"])
        prefix = prefix_length(covered)
        if prefix < target_m:
            raise RuntimeError(f"internal verification failed: prefix={prefix}")
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
    parser.add_argument("--free-type-counts", action="store_true")
    parser.add_argument("--max-replacements-from-seed", type=int)
    parser.add_argument("--seconds", type=float, default=300.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=791)
    parser.add_argument("--log-progress", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = solve(args)
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
