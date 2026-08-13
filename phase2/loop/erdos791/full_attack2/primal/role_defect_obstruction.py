#!/usr/bin/env python3
"""Exact unique-sum/Turan obstruction for phased role relabellings."""

from __future__ import annotations

import argparse
import json
from math import comb, sqrt


def additive_prefix(C: tuple[int, ...]) -> int:
    sums = {a + b for a in C for b in C}
    q = 0
    while q in sums:
        q += 1
    return q


def representation_data(
    C: tuple[int, ...], n: int
) -> tuple[list[int], list[dict[str, object]], list[dict[str, int]]]:
    counts: list[int] = []
    unique_off_diagonal: list[dict[str, object]] = []
    unique_diagonal: list[dict[str, int]] = []
    for q in range(n + 1):
        reps = [(a, b) for i, a in enumerate(C) for b in C[i:] if a + b == q]
        counts.append(len(reps))
        if len(reps) == 1 and reps[0][0] != reps[0][1]:
            unique_off_diagonal.append({"sum": q, "edge": list(reps[0])})
        if len(reps) == 1 and reps[0][0] == reps[0][1]:
            unique_diagonal.append({"sum": q, "vertex": reps[0][0]})
    return counts, unique_off_diagonal, unique_diagonal


def max_edges_after_deleting_to_r_colorable(k: int, d: int, r: int) -> int:
    """Maximum edges if deleting d vertices leaves an r-colorable graph."""
    remaining = k - d
    incident = comb(k, 2) - comb(remaining, 2)
    quotient, remainder = divmod(remaining, r)
    part_square_sum = (
        remainder * (quotient + 1) ** 2
        + (r - remainder) * quotient**2
    )
    turan = (remaining * remaining - part_square_sum) // 2
    return incident + turan


def count_forced_defect(k: int, unique_edges: int, r: int = 4) -> int:
    for d in range(k + 1):
        if unique_edges <= max_edges_after_deleting_to_r_colorable(k, d, r):
            return d
    raise AssertionError((k, unique_edges))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("basis", type=int, nargs="+")
    parser.add_argument("--target-n", type=int)
    parser.add_argument(
        "--role-chromatic-number",
        type=int,
        default=4,
        help="chromatic number of current-role compatibility graph",
    )
    args = parser.parse_args()
    C = tuple(sorted(set(args.basis)))
    if len(C) != len(args.basis) or not C or C[0] < 0:
        raise SystemExit("basis must contain distinct nonnegative integers")
    if args.role_chromatic_number < 1:
        raise SystemExit("role chromatic number must be positive")
    r = args.role_chromatic_number
    prefix = additive_prefix(C)
    n = prefix - 1 if args.target_n is None else args.target_n
    if n >= prefix:
        raise SystemExit(f"basis only covers through {prefix-1}")
    counts, unique_edges, unique_loops = representation_data(C, n)
    k = len(C)
    pair_count_lower = max(0, 2 * (n + 1) - comb(k + 1, 2) - k)
    exact_edge_lower = len(unique_edges)
    d_pair = count_forced_defect(k, pair_count_lower, r)
    d_exact = count_forced_defect(k, exact_edge_lower, r)
    density = (n + 1) / (k * k)
    asymptotic_defect = None
    if density <= 0.5:
        asymptotic_defect = max(0.0, 1.0 - sqrt(2.0 * r * (1.0 - 2.0 * density)))
    print(
        json.dumps(
            {
                "status": "PASS",
                "basis": list(C),
                "k": k,
                "n": n,
                "square_density_m_over_k2": density,
                "unordered_representation_counts": counts,
                "unique_off_diagonal": unique_edges,
                "unique_diagonal": unique_loops,
                "number_unique_off_diagonal": exact_edge_lower,
                "number_unique_diagonal": len(unique_loops),
                "pair_count_lower_bound_on_unique_off_diagonal": pair_count_lower,
                "forced_role_defect_from_actual_unique_graph_edge_count": d_exact,
                "forced_role_defect_from_unique_diagonals": len(unique_loops),
                "combined_forced_role_defect": max(d_exact, len(unique_loops)),
                "forced_role_defect_from_pair_count_alone": d_pair,
                "asymptotic_pair_count_defect_fraction": asymptotic_defect,
                "role_chromatic_number": r,
                "near_lossless_density_threshold": 0.5 - 1.0 / (4.0 * r),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
