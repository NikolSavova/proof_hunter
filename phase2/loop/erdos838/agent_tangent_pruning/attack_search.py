#!/usr/bin/env python3
"""Exact fast probes for the contiguous-cut collision and tangent ratios.

This file deliberately reconstructs the cut quantities without importing
``agent_cut_reset/cut_kernel.py``.  The key speedup is to sum the boundary
vectors before taking their scalar products.  For example, the sum of all
left cup-prefix vectors is the vector of cups in the graph obtained by
deleting internal right edges; similarly on the other three sides.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


Point = tuple[Fraction, Fraction]
RankedEdge = tuple[int, int, int]


def determinant(p: Point, q: Point, r: Point) -> Fraction:
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def slope_order(points: Sequence[Point]) -> list[RankedEdge]:
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if determinant(points[i], points[j], points[k]) == 0:
                    raise ValueError(f"collinear triple {i},{j},{k}")
    raw = sorted(
        ((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]), i, j)
        for i in range(n)
        for j in range(i + 1, n)
    )
    # Equal slopes on disjoint edges commute, so the deterministic tie break
    # does not change any path count.
    return [(rank, i, j) for rank, (_, i, j) in enumerate(raw)]


def product(n: int, edges: Iterable[RankedEdge]) -> list[list[int]]:
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for _, i, j in edges:
        row_i = matrix[i]
        row_j = matrix[j]
        matrix[j] = [x + y for x, y in zip(row_j, row_i)]
    return matrix


def trace(matrix_a: Sequence[Sequence[int]], matrix_b: Sequence[Sequence[int]],
          rows: range, cols: range) -> int:
    return sum(matrix_a[t][s] * matrix_b[t][s] for t in rows for s in cols)


def total_paths(n: int, order: Sequence[RankedEdge]) -> tuple[int, int]:
    cups = product(n, order)
    caps = product(n, reversed(order))
    return sum(map(sum, caps)), sum(map(sum, cups))


def cut_summary(n: int, order: Sequence[RankedEdge], m: int) -> dict[str, int | str]:
    """Compute X, S_L and S_R exactly, in O(n^3) arithmetic operations.

    Let G_L be the graph with internal-R edges deleted.  A cup entry from L
    to R in G_L consists of a left prefix followed by its cross edge and no
    right suffix.  Consequently its sum over the terminal point is exactly
    ``sum_e UL_e(s)``.  The reversed product gives the analogous cap sum, and
    their endpointwise product is S_L.  Deleting internal-L edges gives S_R.
    """
    order = list(order)
    rev = list(reversed(order))
    rows = range(m, n)
    cols = range(m)

    cups = product(n, order)
    caps = product(n, rev)
    crossing = trace(cups, caps, rows, cols)

    no_right = [e for e in order if not (e[1] >= m)]
    ul = product(n, no_right)
    cl = product(n, reversed(no_right))
    left_cup_mass = [sum(ul[t][s] for t in rows) for s in cols]
    left_cap_mass = [sum(cl[t][s] for t in rows) for s in cols]
    s_left = sum(x * y for x, y in zip(left_cup_mass, left_cap_mass))

    no_left = [e for e in order if not (e[2] < m)]
    ur = product(n, no_left)
    cr = product(n, reversed(no_left))
    right_cup_mass = [sum(ur[t][s] for s in cols) for t in rows]
    right_cap_mass = [sum(cr[t][s] for s in cols) for t in rows]
    s_right = sum(x * y for x, y in zip(right_cup_mass, right_cap_mass))

    left_order = [(rank, i, j) for rank, i, j in order if j < m]
    right_order = [(rank, i - m, j - m) for rank, i, j in order if i >= m]
    c_left, u_left = total_paths(m, left_order)
    c_right, u_right = total_paths(n - m, right_order)

    edge_count = m * (n - m)
    collision_num = crossing * edge_count * edge_count
    collision_den = s_left * s_right
    tangent_left_num = s_left
    tangent_left_den = (n - m) ** 2 * min(c_left, u_left)
    tangent_right_num = s_right
    tangent_right_den = m ** 2 * min(c_right, u_right)
    return {
        "n": n,
        "cut": m,
        "X": crossing,
        "S_L": s_left,
        "S_R": s_right,
        "C_L": c_left,
        "U_L": u_left,
        "C_R": c_right,
        "U_R": u_right,
        "collision_num": collision_num,
        "collision_den": collision_den,
        "collision_ratio": str(Fraction(collision_num, collision_den)),
        "tangent_left_ratio": str(Fraction(tangent_left_num, tangent_left_den)),
        "tangent_right_ratio": str(Fraction(tangent_right_num, tangent_right_den)),
    }


def dyadic_horton(levels: int) -> list[Point]:
    ys = [Fraction(0)]
    for level in range(1, levels + 1):
        epsilon = Fraction(1, 2 ** (level + 4))
        ys = [value for y in ys for value in (epsilon * y, 1 + epsilon * y)]
    return [(Fraction(i), y) for i, y in enumerate(ys)]


def random_integral_points(n: int, rng: random.Random, bound: int = 10**9) -> list[Point]:
    while True:
        ys = [rng.randrange(-bound, bound + 1) for _ in range(n)]
        points = [(Fraction(i), Fraction(y)) for i, y in enumerate(ys)]
        try:
            slope_order(points)
        except ValueError:
            continue
        return points


def alternating_least_index(n: int, multiplier: int | None = None) -> list[Point]:
    """Exact realization with chi(i,j,k)=(-1)^i for every i<j<k."""
    if n < 4:
        raise ValueError("the least-index construction needs n >= 4")
    multiplier = 4 * n + 1 if multiplier is None else multiplier
    if multiplier <= 2 * n:
        raise ValueError("use multiplier > 2n for the dominance proof")
    ys = [((-1) ** i) * multiplier ** (n - i) for i in range(n - 2)] + [0, 0]
    points = [(Fraction(i), Fraction(y)) for i, y in enumerate(ys)]
    expected = [1 if i % 2 == 0 else -1 for i in range(n - 2)]
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                sign = 1 if determinant(points[i], points[j], points[k]) > 0 else -1
                if sign != expected[i]:
                    raise AssertionError((i, j, k, sign, expected[i]))
    return points


def score_fraction(summary: dict[str, int | str], field: str) -> float:
    return float(Fraction(str(summary[field])))


def search(n: int, trials: int, seed: int, objective: str) -> dict:
    rng = random.Random(seed)
    field = {
        "collision": "collision_ratio",
        "tangent-left": "tangent_left_ratio",
        "tangent-right": "tangent_right_ratio",
    }[objective]
    best: dict | None = None
    for trial in range(trials):
        points = random_integral_points(n, rng)
        result = cut_summary(n, slope_order(points), n // 2)
        candidate = {
            "trial": trial,
            "objective": objective,
            "ys": [int(y) for _, y in points],
            "summary": result,
        }
        if best is None or score_fraction(result, field) < score_fraction(best["summary"], field):
            best = candidate
    assert best is not None
    return best


def exhaustive_permutation_heights(n: int) -> dict:
    """Exhaust the exact stretchable subfamily x=i, y a permutation of [n]."""
    fields = ("collision_ratio", "tangent_left_ratio", "tangent_right_ratio")
    best: dict[str, dict] = {}
    accepted = 0
    rejected_collinear = 0
    for ys in itertools.permutations(range(n)):
        points = [(Fraction(i), Fraction(y)) for i, y in enumerate(ys)]
        try:
            order = slope_order(points)
        except ValueError:
            rejected_collinear += 1
            continue
        accepted += 1
        result = cut_summary(n, order, n // 2)
        for field in fields:
            candidate = {"ys": list(ys), "summary": result}
            if field not in best or Fraction(str(result[field])) < Fraction(
                str(best[field]["summary"][field])
            ):
                best[field] = candidate
    return {
        "n": n,
        "accepted": accepted,
        "rejected_collinear": rejected_collinear,
        "minima": best,
    }


def ratio_bits(value: str) -> float:
    q = Fraction(value)
    return math.log2(q.numerator) - math.log2(q.denominator)


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    horton_parser = subparsers.add_parser("horton")
    horton_parser.add_argument("--max-level", type=int, default=7)
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("n", type=int)
    search_parser.add_argument("--trials", type=int, default=1000)
    search_parser.add_argument("--seed", type=int, default=838)
    search_parser.add_argument(
        "--objective", choices=("collision", "tangent-left", "tangent-right"),
        default="collision",
    )
    search_parser.add_argument("--output", type=Path)
    alternating_parser = subparsers.add_parser("alternating")
    alternating_parser.add_argument("--max-n", type=int, default=30)
    alternating_parser.add_argument("--output", type=Path)
    exhaustive_parser = subparsers.add_parser("exhaustive-permutations")
    exhaustive_parser.add_argument("n", type=int)
    exhaustive_parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.command == "horton":
        for levels in range(2, args.max_level + 1):
            points = dyadic_horton(levels)
            result = cut_summary(len(points), slope_order(points), len(points) // 2)
            print(json.dumps({
                **result,
                "collision_log2": ratio_bits(str(result["collision_ratio"])),
                "tangent_left_log2": ratio_bits(str(result["tangent_left_ratio"])),
            }, sort_keys=True))
    elif args.command == "search":
        result = search(args.n, args.trials, args.seed, args.objective)
        encoded = json.dumps(result, indent=2, sort_keys=True)
        print(encoded)
        if args.output is not None:
            args.output.write_text(encoded + "\n")
    elif args.command == "alternating":
        records = []
        for n in range(6, args.max_n + 1, 2):
            points = alternating_least_index(n)
            result = cut_summary(n, slope_order(points), n // 2)
            records.append({
                **result,
                "collision_log2": ratio_bits(str(result["collision_ratio"])),
                "tangent_left_log2": ratio_bits(str(result["tangent_left_ratio"])),
                "tangent_right_log2": ratio_bits(str(result["tangent_right_ratio"])),
            })
        encoded = "\n".join(json.dumps(record, sort_keys=True) for record in records) + "\n"
        print(encoded, end="")
        if args.output is not None:
            args.output.write_text(encoded)
    else:
        result = exhaustive_permutation_heights(args.n)
        encoded = json.dumps(result, indent=2, sort_keys=True)
        print(encoded)
        if args.output is not None:
            args.output.write_text(encoded + "\n")


if __name__ == "__main__":
    main()
