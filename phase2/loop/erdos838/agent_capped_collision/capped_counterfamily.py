#!/usr/bin/env python3
"""Exact certificates for a padded alternating counterfamily.

The construction is a heterogeneous vertical lexicographic composition.
Its macro order type has chi(i,j,k)=(-1)^i.  Four macro points are replaced
by r-point one-sided chains: two all-cups immediately useful as left sources,
and two all-caps useful as right terminal blocks.  The cut is exactly balanced.

The script constructs exact rational coordinates, verifies every orientation
against the abstract composition rule, and independently computes X,S_L,S_R
from slope-ordered path matrices.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Iterable, Sequence


Point = tuple[Fraction, Fraction]
RankedEdge = tuple[int, int, int]


def det(p: Point, q: Point, r: Point) -> Fraction:
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def normalize_increasing(points: Sequence[Point]) -> list[Point]:
    """Translate and positively rescale each coordinate into [0,1]."""
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    dx = max(xs) - min(xs)
    dy = max(ys) - min(ys)
    if dx == 0:
        dx = Fraction(1)
    if dy == 0:
        dy = Fraction(1)
    out = [((x - min(xs)) / dx, (y - min(ys)) / dy) for x, y in points]
    assert all(out[i][0] < out[i + 1][0] for i in range(len(out) - 1))
    assert all(out[i][1] < out[i + 1][1] for i in range(len(out) - 1))
    return out


def alternating_macro(h: int) -> list[Point]:
    """A 2h-point exact realization of chi(i,j,k)=(-1)^i, then sheared."""
    if h < 2 or h % 2:
        raise ValueError("h must be even and at least 2")
    k = 2 * h
    multiplier = 4 * k + 1
    ys = [Fraction(((-1) ** i) * multiplier ** (k - i)) for i in range(k - 2)]
    ys += [Fraction(0), Fraction(0)]
    raw = [(Fraction(i), ys[i]) for i in range(k)]
    for i, j, ell in combinations(range(k), 3):
        sign = 1 if det(raw[i], raw[j], raw[ell]) > 0 else -1
        assert sign == (1 if i % 2 == 0 else -1)

    # A shear preserves orientations and makes both coordinates increasing.
    shear = max(ys[i] - ys[i + 1] for i in range(k - 1)) + 1
    sheared = [(x, y + shear * x) for x, y in raw]
    return normalize_increasing(sheared)


def one_sided_chain(r: int, sign: int) -> list[Point]:
    """Increasing-coordinate r-chain with every triple of the given sign."""
    if r < 1 or sign not in (-1, 1):
        raise ValueError((r, sign))
    if r == 1:
        return [(Fraction(0), Fraction(0))]
    slope = 2 * r + 1
    raw = [
        (Fraction(j), Fraction(slope * j + sign * j * j))
        for j in range(r)
    ]
    out = normalize_increasing(raw)
    for i, j, ell in combinations(range(r), 3):
        actual = 1 if det(out[i], out[j], out[ell]) > 0 else -1
        assert actual == sign
    return out


def block_spec(h: int, r: int) -> tuple[list[list[Point]], list[int]]:
    """Return the four inflated blocks and their macro labels per point."""
    k = 2 * h
    blocks: list[list[Point]] = []
    for block in range(k):
        if block in (0, h - 1):
            blocks.append(one_sided_chain(r, 1))
        elif block in (k - 2, k - 1):
            blocks.append(one_sided_chain(r, -1))
        else:
            blocks.append(one_sided_chain(1, 1))
    labels = [block for block, micro in enumerate(blocks) for _ in micro]
    return blocks, labels


def expected_sign(
    labels: Sequence[int], local_indices: Sequence[int], blocks: Sequence[Sequence[Point]],
    i: int, j: int, k: int,
) -> int:
    bi, bj, bk = labels[i], labels[j], labels[k]
    if bi == bk:
        micro = blocks[bi]
        a, b, c = local_indices[i], local_indices[j], local_indices[k]
        return 1 if det(micro[a], micro[b], micro[c]) > 0 else -1
    if bi == bj:
        return -1
    if bj == bk:
        return 1
    return 1 if bi % 2 == 0 else -1


def realize(h: int, r: int) -> tuple[list[Point], int, list[int]]:
    """Find a dyadic epsilon realizing the heterogeneous composition exactly."""
    macro = alternating_macro(h)
    blocks, labels = block_spec(h, r)
    local_indices = [j for micro in blocks for j in range(len(micro))]
    for exponent in range(1, 501):
        epsilon = Fraction(1, 2**exponent)
        points = [
            (
                macro[block][0] + epsilon * epsilon * micro[j][0],
                macro[block][1] + epsilon * micro[j][1],
            )
            for block, micro in enumerate(blocks)
            for j in range(len(micro))
        ]
        if not all(points[i][0] < points[i + 1][0] for i in range(len(points) - 1)):
            continue
        if not all(points[i][1] < points[i + 1][1] for i in range(len(points) - 1)):
            continue
        good = True
        for i, j, k in combinations(range(len(points)), 3):
            value = det(points[i], points[j], points[k])
            if value == 0 or (1 if value > 0 else -1) != expected_sign(
                labels, local_indices, blocks, i, j, k
            ):
                good = False
                break
        if good:
            return points, exponent, labels
    raise AssertionError("no dyadic realization found")


def slope_order(points: Sequence[Point]) -> list[RankedEdge]:
    raw = sorted(
        ((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]), i, j)
        for i in range(len(points))
        for j in range(i + 1, len(points))
    )
    return [(rank, i, j) for rank, (_, i, j) in enumerate(raw)]


def product(n: int, edges: Iterable[RankedEdge]) -> list[list[int]]:
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for _, i, j in edges:
        matrix[j] = [x + y for x, y in zip(matrix[j], matrix[i])]
    return matrix


def total_paths(n: int, order: Sequence[RankedEdge]) -> tuple[int, int]:
    cups = product(n, order)
    caps = product(n, reversed(order))
    return sum(map(sum, caps)), sum(map(sum, cups))


def cut_summary(points: Sequence[Point], cut: int) -> dict[str, int | str]:
    """Compute X,S_L,S_R by the aggregate identities, with exact integers."""
    n = len(points)
    order = slope_order(points)
    reverse = list(reversed(order))
    left = range(cut)
    right = range(cut, n)
    cups = product(n, order)
    caps = product(n, reverse)
    crossing = sum(cups[t][s] * caps[t][s] for s in left for t in right)

    no_right = [edge for edge in order if edge[1] < cut]
    ul = product(n, no_right)
    cl = product(n, reversed(no_right))
    s_left = sum(
        sum(ul[t][s] for t in right) * sum(cl[t][s] for t in right)
        for s in left
    )

    no_left = [edge for edge in order if edge[2] >= cut]
    ur = product(n, no_left)
    cr = product(n, reversed(no_left))
    s_right = sum(
        sum(ur[t][s] for s in left) * sum(cr[t][s] for s in left)
        for t in right
    )
    left_order = [(rank, i, j) for rank, i, j in order if j < cut]
    right_order = [
        (rank, i - cut, j - cut) for rank, i, j in order if i >= cut
    ]
    c_left, u_left = total_paths(cut, left_order)
    c_right, u_right = total_paths(n - cut, right_order)
    edge_count = cut * (n - cut)
    ratio = Fraction(crossing * edge_count * edge_count, s_left * s_right)
    tangent_left = Fraction(s_left, (n - cut) ** 2 * min(c_left, u_left))
    tangent_right = Fraction(s_right, cut**2 * min(c_right, u_right))
    return {
        "n": n,
        "cut": cut,
        "X": crossing,
        "S_L": s_left,
        "S_R": s_right,
        "C_L": c_left,
        "U_L": u_left,
        "C_R": c_right,
        "U_R": u_right,
        "E": edge_count,
        "collision_ratio": str(ratio),
        "collision_log2": math.log2(ratio.numerator) - math.log2(ratio.denominator),
        "tangent_left_ratio": str(tangent_left),
        "tangent_right_ratio": str(tangent_right),
    }


def analytic_bounds(h: int, r: int) -> dict[str, int | str]:
    ell = 2 * r + h - 2
    x_upper = 5 * r**6 * h**2 * 2**h
    sl_lower = r**2 * ell**2 * 2 ** (h // 2 - 1)
    sr_lower = r**5 * 2 ** (h - 2)
    ratio_upper = Fraction(40 * h**2 * ell**2, r * 2 ** (h // 2))
    return {
        "side_size": ell,
        "X_upper": x_upper,
        "S_L_lower": sl_lower,
        "S_R_lower": sr_lower,
        "collision_ratio_upper": str(ratio_upper),
    }


def certificate(h: int, r: int) -> dict:
    points, epsilon_exponent, labels = realize(h, r)
    cut = 2 * r + h - 2
    assert labels[cut - 1] == h - 1 and labels[cut] == h
    exact = cut_summary(points, cut)
    bounds = analytic_bounds(h, r)
    assert exact["X"] <= bounds["X_upper"]
    assert exact["S_L"] >= bounds["S_L_lower"]
    assert exact["S_R"] >= bounds["S_R_lower"]
    assert Fraction(str(exact["collision_ratio"])) <= Fraction(
        str(bounds["collision_ratio_upper"])
    )
    return {
        "parameters": {"h": h, "r": r},
        "realization": {
            "epsilon": f"2^-{epsilon_exponent}",
            "orientation_triples_checked": math.comb(len(points), 3),
            "stretchable": True,
        },
        "exact": exact,
        "proved_bounds": bounds,
        "status": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    cases = []
    for encoded in args.case or ["4,3", "6,4", "8,5"]:
        h, r = map(int, encoded.split(","))
        cases.append(certificate(h, r))
    output = {"family": "padded_alternating", "cases": cases, "status": "PASS"}
    rendered = json.dumps(output, indent=2, sort_keys=True) + "\n"
    print(rendered, end="")
    if args.output:
        args.output.write_text(rendered)


if __name__ == "__main__":
    main()
