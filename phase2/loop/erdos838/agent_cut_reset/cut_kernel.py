#!/usr/bin/env python3
"""Exact contiguous-cut kernel for the reverse-product trace.

The input may be either an exact rational point set (through ``analyze_points``)
or an arbitrary reflection order/root sequence (through ``analyze_order``).
Indices are in horizontal order and a cut is ``[0,m) | [m,n)``.

For a cross edge e=(i,j), U_L(e) counts increasing-slope prefixes ending at
i with every slope below slope(e), and U_R(e) counts suffixes starting at j
with every slope above slope(e).  C_L,C_R are the reversed inequalities for
decreasing-slope paths.  The cross blocks satisfy

    U[t,s] = sum_e U_L(e)[s] U_R(e)[t],
    C[t,s] = sum_f C_L(f)[s] C_R(f)[t],

and hence their Frobenius product is the exact nonnegative kernel pairing

    sum_(e,f) <U_L(e),C_L(f)> <U_R(e),C_R(f)>.

All calculations are over Python integers.  The edge keys need only form a
strict total order; geometric slopes are used for coordinate input.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from reflection_trace import pascal_cell, slope_order  # noqa: E402

RankedEdge = tuple[int, int, int]


def product(n: int, edges: Iterable[RankedEdge]) -> list[list[int]]:
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for _, i, j in edges:
        matrix[j] = [a + b for a, b in zip(matrix[j], matrix[i])]
    return matrix


def rank_slopes(points: Sequence[tuple[Fraction, Fraction]]) -> list[RankedEdge]:
    return [(rank, i, j) for rank, (_, i, j) in enumerate(slope_order(list(points)))]


def random_reflection_order(n: int, rng: random.Random) -> list[RankedEdge]:
    """A random root sequence of a reduced word for the longest permutation."""
    permutation = list(range(n))
    roots: list[tuple[int, int]] = []
    while permutation != list(reversed(range(n))):
        choices = [k for k in range(n - 1) if permutation[k] < permutation[k + 1]]
        k = rng.choice(choices)
        a, b = permutation[k], permutation[k + 1]
        roots.append((min(a, b), max(a, b)))
        permutation[k], permutation[k + 1] = b, a
    assert len(roots) == n * (n - 1) // 2
    assert len(set(roots)) == len(roots)
    return [(rank, i, j) for rank, (i, j) in enumerate(roots)]


def horton(m: int) -> list[tuple[Fraction, Fraction]]:
    ys = [Fraction(0)]
    for level in range(1, m + 1):
        eps = Fraction(1, 2 ** (level + 4))
        ys = [value for y in ys for value in (eps * y, 1 + eps * y)]
    return [(Fraction(i), y) for i, y in enumerate(ys)]


def compose(points: Sequence[tuple[Fraction, Fraction]], eps: Fraction) -> list[tuple[Fraction, Fraction]]:
    return sorted(
        (x + eps * eps * u, y + eps * v)
        for x, y in points
        for u, v in points
    )


def cut_kernel(n: int, order: Sequence[RankedEdge], m: int) -> dict:
    if not 0 < m < n:
        raise ValueError("cut must satisfy 0 < m < n")
    order = list(order)
    reverse = list(reversed(order))
    left_edges = [e for e in order if e[2] < m]
    right_edges = [e for e in order if e[1] >= m]
    cross = [e for e in order if e[1] < m <= e[2]]

    # Full matrices and the direct cross-block trace, used as an independent
    # check on the kernel expansion.
    cups = product(n, order)
    caps = product(n, reverse)
    direct = sum(cups[t][s] * caps[t][s] for t in range(m, n) for s in range(m))

    boundary = []
    for rank, i, j in cross:
        ul = product(n, (e for e in left_edges if e[0] < rank))[i][:m]
        cl = product(n, (e for e in reversed(left_edges) if e[0] > rank))[i][:m]
        ur_matrix = product(n, (e for e in right_edges if e[0] > rank))
        cr_matrix = product(n, (e for e in reversed(right_edges) if e[0] < rank))
        ur = [ur_matrix[t][j] for t in range(m, n)]
        cr = [cr_matrix[t][j] for t in range(m, n)]
        boundary.append({
            "edge": (i, j),
            "rank": rank,
            "UL": ul,
            "CL": cl,
            "UR": ur,
            "CR": cr,
        })

    size = len(boundary)
    left_kernel = [[0] * size for _ in range(size)]
    right_kernel = [[0] * size for _ in range(size)]
    terms = [[0] * size for _ in range(size)]
    expanded = 0
    maximum = (0, -1, -1)
    nonzero = 0
    for a, e in enumerate(boundary):
        for b, f in enumerate(boundary):
            kl = sum(x * y for x, y in zip(e["UL"], f["CL"]))
            kr = sum(x * y for x, y in zip(e["UR"], f["CR"]))
            value = kl * kr
            left_kernel[a][b] = kl
            right_kernel[a][b] = kr
            terms[a][b] = value
            expanded += value
            if value:
                nonzero += 1
            if value > maximum[0]:
                maximum = (value, a, b)
    if expanded != direct:
        raise AssertionError(f"cut expansion {expanded} != direct trace {direct}")

    # The equal-bridge diagonal is always the two-point contribution.  This
    # assertion is a useful guard against reversing one of the four filters.
    diagonal = [left_kernel[a][a] * right_kernel[a][a] for a in range(size)]
    if diagonal != [1] * size:
        raise AssertionError(f"equal-bridge diagonal is not identically one: {diagonal}")

    return {
        "n": n,
        "cut": m,
        "cross_edges": size,
        "cross_trace": direct,
        "max_term": maximum[0],
        "max_pair": maximum[1:],
        "nonzero_terms": nonzero,
        "left_kernel_sum": sum(map(sum, left_kernel)),
        "right_kernel_sum": sum(map(sum, right_kernel)),
        "boundary": boundary,
        "left_kernel": left_kernel,
        "right_kernel": right_kernel,
        "terms": terms,
    }


def analyze_points(points: Sequence[tuple[Fraction, Fraction]], m: int | None = None) -> dict:
    n = len(points)
    m = n // 2 if m is None else m
    result = cut_kernel(n, rank_slopes(points), m)

    # A nontrivial cap/cup pair has its cup bridge strictly below its cap
    # bridge at every vertical separator inside the cut strip.
    xi = (points[m - 1][0] + points[m][0]) / 2

    def height(edge: tuple[int, int]) -> Fraction:
        i, j = edge
        x0, y0 = points[i]
        x1, y1 = points[j]
        return y0 + (y1 - y0) * (xi - x0) / (x1 - x0)

    violations = []
    for a, e in enumerate(result["boundary"]):
        for b, f in enumerate(result["boundary"]):
            if a != b and result["terms"][a][b] and not height(e["edge"]) < height(f["edge"]):
                violations.append((a, b))
    if violations:
        raise AssertionError(f"bridge-height support violations: {violations[:5]}")
    result["height_support_violations"] = 0
    return result


def summary(result: dict) -> dict:
    return {key: result[key] for key in (
        "n", "cut", "cross_edges", "cross_trace", "max_term", "max_pair",
        "nonzero_terms", "left_kernel_sum", "right_kernel_sum",
    )}


def selftest() -> None:
    cell = sorted(pascal_cell(4, 2, Fraction(1, 97)))
    families = [
        ("T42", cell),
        ("T42[T42]", compose(cell, Fraction(1, 16384))),
        ("Horton16", horton(4)),
    ]
    for name, points in families:
        result = analyze_points(points)
        print(name, json.dumps(summary(result), sort_keys=True))

    anti_y = [
        -677058, -3660524, 535511, 4765981, -4127906, 8538748,
        4609976, 4593410, 5357026, 5928495, 7488423, 9074704,
    ]
    anti = [(Fraction(i), Fraction(y)) for i, y in enumerate(anti_y)]
    result = analyze_points(anti)
    edge_count = result["cross_edges"]
    correlation_ratio = Fraction(
        result["cross_trace"] * edge_count * edge_count,
        result["left_kernel_sum"] * result["right_kernel_sum"],
    )
    print("stretchable anti-alignment", json.dumps(summary(result), sort_keys=True))
    print(f"  cross*|E|^2/(sum(K_L)sum(K_R)) = {correlation_ratio}")

    # Two rational (in fact integral) stretchable examples with identical
    # child cap/cup data and identical aggregate boundary masses, but distinct
    # crossing trace.  This certifies that those scalar summaries are not a
    # sufficient cut state.
    scalar_pair = [
        [47732327, -47889601, 8927488, 65242589, -36349432, 94616416],
        [96932891, -82941997, -39598354, 7172190, -79138602, -20420550],
    ]
    pair_results = [
        analyze_points([(Fraction(i), Fraction(y)) for i, y in enumerate(ys)])
        for ys in scalar_pair
    ]
    pair_signature = lambda r: (r["left_kernel_sum"], r["right_kernel_sum"])
    assert pair_signature(pair_results[0]) == pair_signature(pair_results[1]) == (59, 62)
    assert [r["cross_trace"] for r in pair_results] == [36, 35]
    print("same scalar boundary state, different trace:",
          pair_signature(pair_results[0]), "->", [36, 35])
    rng = random.Random(838)
    for n in range(4, 11):
        minima = None
        min_ratio = None
        for _ in range(100):
            result = cut_kernel(n, random_reflection_order(n, rng), n // 2)
            value = result["cross_trace"]
            minima = value if minima is None else min(minima, value)
            edges = result["cross_edges"]
            ratio = Fraction(
                value * edges * edges,
                result["left_kernel_sum"] * result["right_kernel_sum"],
            )
            min_ratio = ratio if min_ratio is None else min(min_ratio, ratio)
        print(f"random reflection orders n={n}: minimum cross trace in 100 trials = {minima}; "
              f"minimum correlation ratio = {float(min_ratio):.6f}")
    print("all exact cut expansions and equal-bridge diagonal checks PASS")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--random-order", type=int, metavar="N")
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--cut", type=int)
    args = parser.parse_args()
    if args.selftest:
        selftest()
    elif args.random_order:
        rng = random.Random(args.seed)
        order = random_reflection_order(args.random_order, rng)
        result = cut_kernel(args.random_order, order, args.cut or args.random_order // 2)
        print(json.dumps(summary(result), indent=2, sort_keys=True))
    else:
        parser.error("use --selftest or --random-order N")


if __name__ == "__main__":
    main()
