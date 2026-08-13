#!/usr/bin/env python3
"""Exact audit of the Pascal/Morris--Soltan construction for Erdos #838.

The construction uses only Fraction arithmetic.  ``glue(A, B)`` realizes the
strong ordered gluing relation used in Eppstein's exposition:

* A is left of and below B;
* every line through two points of A passes above every point of B;
* every line through two points of B passes below every point of A.

The script exhaustively checks the proposed row-decomposition lemma, the cell
cap recurrence, and the row counting bound for small rows.  It is deliberately
standalone (standard library only).
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb


@dataclass(frozen=True)
class Point:
    x: Fraction
    y: Fraction
    word: str = ""
    block: int = -1


def det(a: Point, b: Point, c: Point) -> Fraction:
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)


def normalized(points: tuple[Point, ...]) -> tuple[Point, ...]:
    """Put a nonempty increasing point set in [0,1]^2, preserving order type."""
    points = tuple(sorted(points, key=lambda p: p.x))
    if len(points) == 1:
        p = points[0]
        return (Point(Fraction(0), Fraction(0), p.word, p.block),)
    xmin, xmax = points[0].x, points[-1].x
    ymin, ymax = points[0].y, points[-1].y
    assert xmin < xmax and ymin < ymax
    return tuple(
        Point((p.x - xmin) / (xmax - xmin),
              (p.y - ymin) / (ymax - ymin), p.word, p.block)
        for p in points
    )


def min_slope(points: tuple[Point, ...]) -> Fraction | None:
    if len(points) < 2:
        return None
    out = min((q.y - p.y) / (q.x - p.x)
              for p, q in combinations(points, 2))
    assert out > 0
    return out


def glue(left: tuple[Point, ...], right: tuple[Point, ...]) -> tuple[Point, ...]:
    """Strongly glue two increasing configurations using explicit rationals.

    After independent normalization, the two copies occupy
       A: [0,eps] x [0,1],  B: [1,1+eps] x [2,3].
    All cross-slopes are <4, while every within-copy slope is >8.
    This proves the three stated strong-gluing inequalities directly.
    """
    a, b = normalized(left), normalized(right)
    slopes = [s for s in (min_slope(a), min_slope(b)) if s is not None]
    if slopes:
        m = min(slopes)
        eps = min(Fraction(1, 4), m / (8 + 2 * m))
    else:
        eps = Fraction(1, 4)
    aa = tuple(Point(eps * p.x, p.y, p.word, p.block) for p in a)
    bb = tuple(Point(1 + eps * p.x, 2 + p.y, p.word, p.block) for p in b)
    out = aa + bb
    assert all(out[j].x < out[j + 1].x and out[j].y < out[j + 1].y
               for j in range(len(out) - 1))
    return out


@lru_cache(maxsize=None)
def cell(n: int, i: int) -> tuple[Point, ...]:
    """The binomial cell T(n,i), with |T(n,i)| = binom(n,i)."""
    assert 0 <= i <= n
    if i == 0:
        return (Point(Fraction(0), Fraction(0), "0" * n),)
    if i == n:
        return (Point(Fraction(0), Fraction(0), "1" * n),)
    left = tuple(Point(p.x, p.y, "1" + p.word, p.block)
                 for p in cell(n - 1, i - 1))
    right = tuple(Point(p.x, p.y, "0" + p.word, p.block)
                  for p in cell(n - 1, i))
    return glue(left, right)


def row(n: int) -> tuple[Point, ...]:
    blocks = []
    for i in range(n + 1):
        blocks.append(tuple(Point(p.x, p.y, p.word, i) for p in cell(n, i)))
    out = blocks[0]
    for b in blocks[1:]:
        out = glue(out, b)
    return tuple(sorted(out, key=lambda p: p.x))


def orient_table(points: tuple[Point, ...]) -> list[list[list[int]]]:
    n = len(points)
    out = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i, j, k in combinations(range(n), 3):
        d = det(points[i], points[j], points[k])
        assert d
        out[i][j][k] = 1 if d > 0 else -1
    return out


def is_cap(indices: tuple[int, ...], orient: list[list[list[int]]]) -> bool:
    return all(orient[i][j][k] < 0 for i, j, k in combinations(indices, 3))


def is_cup(indices: tuple[int, ...], orient: list[list[list[int]]]) -> bool:
    return all(orient[i][j][k] > 0 for i, j, k in combinations(indices, 3))


def is_convex(indices: tuple[int, ...], orient: list[list[list[int]]]) -> bool:
    """All selected points are hull vertices (indices are in x-order)."""
    if len(indices) <= 3:
        return True
    lower: list[int] = []
    for k in indices:
        while len(lower) >= 2 and orient[lower[-2]][lower[-1]][k] < 0:
            lower.pop()
        lower.append(k)
    upper: list[int] = []
    for k in indices:
        while len(upper) >= 2 and orient[upper[-2]][upper[-1]][k] > 0:
            upper.pop()
        upper.append(k)
    return len(set(lower) | set(upper)) == len(indices)


def check_strong_row_relation(points: tuple[Point, ...],
                              orient: list[list[list[int]]]) -> None:
    """Check the orientation law induced by sequential strong gluing."""
    for i, j, k in combinations(range(len(points)), 3):
        bi, bj, bk = points[i].block, points[j].block, points[k].block
        if bj < bk:              # rightmost point lies in a later block
            assert orient[i][j][k] < 0, (i, j, k, bi, bj, bk)
        elif bi < bj == bk:      # last two lie in the same later block
            assert orient[i][j][k] > 0, (i, j, k, bi, bj, bk)


def decomposition_ok(indices: tuple[int, ...], points: tuple[Point, ...],
                     orient: list[list[list[int]]]) -> tuple[bool, str]:
    by_block: dict[int, list[int]] = {}
    for j in indices:
        by_block.setdefault(points[j].block, []).append(j)
    occupied = sorted(by_block)
    if len(occupied) <= 1:
        return True, "one-block"
    first, last = occupied[0], occupied[-1]
    if not is_cap(tuple(by_block[first]), orient):
        return False, "first block is not a cap"
    if not is_cup(tuple(by_block[last]), orient):
        return False, "last block is not a cup"
    for b in occupied[1:-1]:
        if len(by_block[b]) > 1:
            return False, f"intermediate block {b} has {len(by_block[b])} points"
    return True, "ok"


def cap_cup_counts(points: tuple[Point, ...]) -> tuple[int, int, int]:
    o = orient_table(points)
    c = u = v = 0
    for r in range(1, len(points) + 1):
        for inds in combinations(range(len(points)), r):
            c += is_cap(inds, o)
            u += is_cup(inds, o)
            v += is_convex(inds, o)
    return c, u, v


def dp_counts(nmax: int) -> tuple[list[list[int]], list[list[int]]]:
    """Exact nonempty cap/cup counts from the cell gluing recurrence."""
    caps = [[0] * (n + 1) for n in range(nmax + 1)]
    caps[0][0] = 1
    for n in range(1, nmax + 1):
        caps[n][0] = caps[n][n] = 1
        for i in range(1, n):
            caps[n][i] = (caps[n - 1][i]
                          + (1 + comb(n - 1, i)) * caps[n - 1][i - 1])
    cups = [[caps[n][n - i] for i in range(n + 1)] for n in range(nmax + 1)]
    return caps, cups


def dp_convex_counts(nmax: int, caps: list[list[int]],
                     cups: list[list[int]]) -> list[list[int]]:
    """Exact nonempty convex-subset counts in individual Pascal cells.

    In T(n,i)=A prec B, every spanning convex subset is uniquely a nonempty
    cap in A union a nonempty cup in B; the converse is also true.
    """
    convex = [[0] * (n + 1) for n in range(nmax + 1)]
    convex[0][0] = 1
    for n in range(1, nmax + 1):
        convex[n][0] = convex[n][n] = 1
        for i in range(1, n):
            convex[n][i] = (convex[n - 1][i - 1] + convex[n - 1][i]
                            + caps[n - 1][i - 1] * cups[n - 1][i])
    return convex


def row_bound(n: int, caps: list[list[int]], cups: list[list[int]]) -> int:
    total = 1  # empty set
    for k in range(n + 1):
        for ell in range(k, n + 1):
            term = caps[n][k] * cups[n][ell]
            for r in range(k + 1, ell):
                term *= 1 + comb(n, r)
            total += term
    return total


def audit(n: int, max_subset_size: int | None) -> None:
    points = row(n)
    assert len(points) == 2 ** n
    orient = orient_table(points)
    check_strong_row_relation(points, orient)

    if max_subset_size is None:
        max_subset_size = len(points)
    max_subset_size = min(max_subset_size, len(points))
    convex_count = 1  # include empty
    bad: list[tuple[tuple[int, ...], str]] = []
    flipped_bad = 0
    sizes: dict[int, int] = {0: 1}
    for r in range(1, max_subset_size + 1):
        nr = 0
        for inds in combinations(range(len(points)), r):
            if not is_convex(inds, orient):
                continue
            nr += 1
            ok, why = decomposition_ok(inds, points, orient)
            if not ok:
                bad.append((inds, why))
            # Negative control: swap cap/cup orientation at the row ends.
            blocks = sorted({points[j].block for j in inds})
            if len(blocks) > 1:
                a = tuple(j for j in inds if points[j].block == blocks[0])
                b = tuple(j for j in inds if points[j].block == blocks[-1])
                if not (is_cup(a, orient) and is_cap(b, orient)):
                    flipped_bad += 1
        sizes[r] = nr
        convex_count += nr

    caps, cups = dp_counts(n)
    cell_convex = dp_convex_counts(n, caps, cups)
    bound = row_bound(n, caps, cups)
    print(f"row m={n}: N={len(points)}, checked sizes 0..{max_subset_size}")
    print(f"  convex subsets checked: {convex_count}; by size: {sizes}")
    print(f"  decomposition failures: {len(bad)}; flipped-orientation failures: {flipped_bad}")
    print(f"  DP row bound (all sizes): {bound}")
    if max_subset_size == len(points):
        print(f"  bound / exact: {bound / convex_count:.6g}")
    assert not bad, bad[:3]
    if max_subset_size == len(points):
        assert convex_count <= bound

    # Independently enumerate every small cell and compare against the exact DP.
    if n <= 5:
        for i in range(n + 1):
            pts = cell(n, i)
            c, u, v = cap_cup_counts(pts)
            assert c == caps[n][i], (n, i, c, caps[n][i])
            assert u == cups[n][i], (n, i, u, cups[n][i])
            assert v == cell_convex[n][i], (n, i, v, cell_convex[n][i])
            assert v <= c * u, (n, i, v, c, u)
        print("  exact cell cap/convex recurrences and V<=Cap*Cup: PASS")
        print(f"  cell convex counts: {cell_convex[n]}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int, nargs="+", default=[3, 4])
    ap.add_argument("--max-subset-size", type=int,
                    help="Useful at m=5: every convex subset has size <=m+1")
    args = ap.parse_args()
    for n in args.m:
        audit(n, args.max_subset_size)


if __name__ == "__main__":
    main()
