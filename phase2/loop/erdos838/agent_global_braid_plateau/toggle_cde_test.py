#!/usr/bin/env python3
"""Exact toggle-CDE test for a fixed-x reflection-order certificate.

For a family L of closed subsets, let T_p be +1 when p can be toggled in,
-1 when it can be toggled out, and 0 otherwise.  The down-degree statistic is
constant on all toggle-symmetric probability distributions iff its vector is
in span{1,T_p}.  We test this finite-dimensional condition over Q.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point]) -> list[Point]:
    points = sorted(points)
    if len(points) <= 1:
        return points
    lower: list[Point] = []
    for p in points:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[Point] = []
    for p in reversed(points):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def inside_convex(poly: list[Point], p: Point) -> bool:
    if len(poly) < 3:
        return p in poly
    signs = [orient(poly[i], poly[(i + 1) % len(poly)], p) for i in range(len(poly))]
    return all(x >= 0 for x in signs) or all(x <= 0 for x in signs)


def closed_masks(points: list[Point]) -> list[int]:
    n = len(points)
    closed = []
    for mask in range(1 << n):
        members = [points[i] for i in range(n) if mask >> i & 1]
        if len(members) <= 2:
            closed.append(mask)
            continue
        poly = hull(members)
        closure = sum(1 << i for i, p in enumerate(points) if inside_convex(poly, p))
        if closure == mask:
            closed.append(mask)
    return closed


def matrix_rank(matrix: list[list[Fraction]]) -> int:
    rows = [row[:] for row in matrix]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][col]
        rows[rank] = [x / value for x in rows[rank]]
        for r in range(m):
            if r != rank and rows[r][col]:
                factor = rows[r][col]
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[rank])]
        rank += 1
        if rank == m:
            break
    return rank


def nullspace_basis(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    """Rational basis for {x: matrix*x=0}."""
    rows = [row[:] for row in matrix]
    if not rows:
        return []
    m, n = len(rows), len(rows[0])
    pivots: list[int] = []
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank, m) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][col]
        rows[rank] = [x / value for x in rows[rank]]
        for r in range(m):
            if r != rank and rows[r][col]:
                factor = rows[r][col]
                rows[r] = [a - factor * b for a, b in zip(rows[r], rows[rank])]
        pivots.append(col)
        rank += 1
        if rank == m:
            break
    free = [col for col in range(n) if col not in pivots]
    basis = []
    for free_col in free:
        vector = [Fraction(0) for _ in range(n)]
        vector[free_col] = 1
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -rows[row][free_col]
        basis.append(vector)
    return basis


def primitive_integer_vector(vector: list[Fraction]) -> list[int]:
    denominator = 1
    for x in vector:
        denominator = math.lcm(denominator, x.denominator)
    integers = [x.numerator * (denominator // x.denominator) for x in vector]
    divisor = 0
    for x in integers:
        divisor = math.gcd(divisor, abs(x))
    integers = [x // divisor for x in integers]
    first = next(x for x in integers if x)
    return integers if first > 0 else [-x for x in integers]


def test_certificate(certificate: dict) -> dict:
    n = certificate["n"]
    raw_y = certificate["fixed_x_rational_y"]
    if raw_y is None:
        raise ValueError("certificate has no fixed-x rational realization")
    points = [(Fraction(i), Fraction(y)) for i, y in enumerate(raw_y)]
    closed = closed_masks(points)
    closed_set = set(closed)
    design = []
    degrees = []
    toggle_counts = []
    for mask in closed:
        dd = 0
        toggles = []
        for p in range(n):
            bit = 1 << p
            if mask & bit:
                possible = (mask ^ bit) in closed_set
                dd += int(possible)
                toggles.append(Fraction(-int(possible)))
            else:
                possible = (mask | bit) in closed_set
                toggles.append(Fraction(int(possible)))
        design.append([Fraction(1), *toggles])
        degrees.append(Fraction(dd))
        toggle_counts.append(toggles)
    rank = matrix_rank(design)
    augmented_rank = matrix_rank([row + [degree] for row, degree in zip(design, degrees)])
    # Uniform toggle symmetry is independently checked label by label.
    toggle_sums = [sum(row[p] for row in toggle_counts) for p in range(n)]
    profile = [0] * (n + 1)
    total_down = 0
    for mask, degree in zip(closed, degrees):
        # Rank is number of extreme points, equivalently down-degree.
        profile[int(degree)] += 1
        total_down += int(degree)
    result = {
        "n": n,
        "closed_set_count": len(closed),
        "down_degree_profile": profile,
        "total_down_degree": total_down,
        "uniform_mean": [total_down, len(closed)],
        "uniform_toggle_sums": [int(x) for x in toggle_sums],
        "design_rank": rank,
        "augmented_rank": augmented_rank,
        "toggle_cde_identity_exists": rank == augmented_rank,
        "interpretation": "dd lies in span of constant and signed element-toggle statistics iff ranks agree",
    }
    if rank != augmented_rank:
        transpose = [[design[row][col] for row in range(len(design))] for col in range(n + 1)]
        witness = next(
            vector
            for vector in nullspace_basis(transpose)
            if sum(x * y for x, y in zip(vector, degrees)) != 0
        )
        witness_int = primitive_integer_vector(witness)
        pairing = sum(Fraction(x) * y for x, y in zip(witness_int, degrees))
        assert sum(witness_int) == 0
        assert all(
            sum(witness_int[row] * design[row][p + 1] for row in range(len(design))) == 0
            for p in range(n)
        )
        assert pairing
        result["non_tCDE_witness"] = {
            "nonzero_mask_weights": [
                [mask, weight] for mask, weight in zip(closed, witness_int) if weight
            ],
            "sum_weights": sum(witness_int),
            "toggle_pairings": [
                int(sum(witness_int[row] * design[row][p + 1] for row in range(len(design))))
                for p in range(n)
            ],
            "down_degree_pairing": int(pairing),
            "use": "uniform probability plus/minus epsilon times this signed vector gives two toggle-symmetric laws with different expected down-degree for sufficiently small epsilon",
        }
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate_json", type=Path)
    parser.add_argument("--key", default="certificate")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate_json.read_text())
    certificate = data[args.key] if args.key else data
    result = test_certificate(certificate)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
