#!/usr/bin/env python3
"""Exact checks for PASCAL_STRONG_GLUE_PROJECTION_SPECTRUM_GATE.md.

The verifier has three independent parts.

1. Exhaust every projection chamber of T(4,3) prec T(8,2).
2. Check the weighted-interval formula in every chamber in which both
   blocks occur in reverse construction order.
3. Check the two chambers adjacent to the macro tie -1/2 for the larger
   T(7,5) prec T(12,3) example, using only its combinatorial chirotope in
   the O(n^3) chain DP.
"""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
from math import comb, log
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

from agent_geometry.audit_geometry import Point, cell, glue  # noqa: E402


def marked_cell(d: int, i: int, block: int) -> tuple[Point, ...]:
    return tuple(Point(p.x, p.y, p.word, block) for p in cell(d, i))


def base_sign(points: tuple[Point, ...], i: int, j: int, k: int) -> int:
    """Chirotope on a naturally ordered triple i<j<k.

    At the outer glue, A,A,B has sign - and A,B,B has sign +.  Inside a
    Pascal cell, the first binary split separating the triple has the same
    rule (the prefix-1 child precedes the prefix-0 child).
    """
    assert i < j < k
    pi, pj, pk = points[i], points[j], points[k]
    if pi.block != pk.block:
        return -1 if pi.block == pj.block else 1
    for a, b, c in zip(pi.word, pj.word, pk.word):
        if not (a == b == c):
            return -1 if a == b else 1
    raise AssertionError("three distinct fixed-weight words must split")


def oriented_sign(points: tuple[Point, ...], a: int, b: int, c: int,
                  cache: dict[tuple[int, int, int], int] | None = None) -> int:
    labels = (a, b, c)
    key = tuple(sorted(labels))
    sign = cache[key] if cache is not None else base_sign(points, *key)
    inversions = sum(labels[i] > labels[j]
                     for i in range(3) for j in range(i + 1, 3))
    return -sign if inversions & 1 else sign


def chain_totals(points: tuple[Point, ...], order: tuple[int, ...],
                 cache: dict[tuple[int, int, int], int] | None = None
                 ) -> tuple[int, int]:
    n = len(points)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            ca = cu = 1
            for h in range(i):
                sign = oriented_sign(points, order[h], order[i], order[j],
                                     cache)
                if sign < 0:
                    ca += cap[h][i]
                else:
                    cu += cup[h][i]
            cap[i][j], cup[i][j] = ca, cu
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def projection_chambers(points: tuple[Point, ...]):
    critical = sorted({
        -(points[j].x - points[i].x) / (points[j].y - points[i].y)
        for i, j in combinations(range(len(points)), 2)
        if points[j].y != points[i].y
    })
    probes = [critical[0] - 1]
    probes += [(x + y) / 2 for x, y in zip(critical, critical[1:])]
    probes += [critical[-1] + 1]
    out = []
    seen = set()
    for slope in probes:
        order = tuple(sorted(range(len(points)),
                             key=lambda i: points[i].x
                             + slope * points[i].y))
        for candidate in (order, order[::-1]):
            if candidate not in seen:
                seen.add(candidate)
                out.append((slope, candidate))
    return out


def pascal_tables(dmax: int):
    caps = [[0] * (d + 1) for d in range(dmax + 1)]
    faces = [[0] * (d + 1) for d in range(dmax + 1)]
    caps[0][0] = faces[0][0] = 1
    for d in range(1, dmax + 1):
        caps[d][0] = caps[d][d] = 1
        faces[d][0] = faces[d][d] = 1
        for i in range(1, d):
            caps[d][i] = (caps[d - 1][i]
                          + (1 + comb(d - 1, i)) * caps[d - 1][i - 1])
        for i in range(1, d):
            faces[d][i] = (faces[d - 1][i - 1] + faces[d - 1][i]
                           + caps[d - 1][i - 1]
                           * caps[d - 1][d - 1 - i])
    return caps, faces


def cell_sign(words: list[str], i: int, j: int, k: int) -> int:
    assert i < j < k
    for a, b, c in zip(words[i], words[j], words[k]):
        if not (a == b == c):
            return -1 if a == b else 1
    raise AssertionError


def weighted_chains(words: list[str], kind: str,
                    last_weight: list[int], first_weight: list[int]) -> int:
    """Sum last_weight(last)*first_weight(first) over natural chains."""
    n = len(words)
    dp = [[0] * n for _ in range(n)]
    total = sum(last_weight[i] * first_weight[i] for i in range(n))
    for i in range(n):
        for j in range(i + 1, n):
            value = first_weight[i]  # the two-point chain {i,j}
            for h in range(i):
                sign = cell_sign(words, h, i, j)
                if (sign < 0) == (kind == "cap"):
                    value += dp[h][i]
            dp[i][j] = value
            total += last_weight[j] * value
    return total


def cross_formula(A: tuple[Point, ...], B: tuple[Point, ...],
                  order: tuple[int, ...]) -> tuple[int, int]:
    """The exact reverse-internal weighted-interval formula."""
    a, b = len(A), len(B)
    pos = {label: i for i, label in enumerate(order)}
    words_a = [p.word for p in A]
    words_b = [p.word for p in B]
    one_a, one_b = [1] * a, [1] * b

    ca = weighted_chains(words_a, "cap", one_a, one_a)
    ua = weighted_chains(words_a, "cup", one_a, one_a)
    cb = weighted_chains(words_b, "cap", one_b, one_b)
    ub = weighted_chains(words_b, "cup", one_b, one_b)

    # For a natural B cup with endpoints f<=l, the seam order is l,...,f.
    # A mixed cap uses either one A outside this interval, or two A labels
    # straddling it.
    left_a = [sum(pos[x] < pos[a + j] for x in range(a))
              for j in range(b)]
    right_a = [a - x for x in left_a]
    mixed_cap = (
        weighted_chains(words_b, "cup", left_a, one_b)
        + weighted_chains(words_b, "cup", one_b, right_a)
        + weighted_chains(words_b, "cup", left_a, right_a)
    )

    left_b = [sum(pos[a + x] < pos[i] for x in range(b))
              for i in range(a)]
    right_b = [b - x for x in left_b]
    mixed_cup = (
        weighted_chains(words_a, "cap", left_b, one_a)
        + weighted_chains(words_a, "cap", one_a, right_b)
        + weighted_chains(words_a, "cap", left_b, right_b)
    )
    return ua + ub + mixed_cap, ca + cb + mixed_cup


def small_all_chamber_audit():
    A = marked_cell(4, 3, 0)
    B = marked_cell(8, 2, 1)
    P = glue(A, B)
    a, b, n = len(A), len(B), len(P)
    assert (a, b, n) == (4, 28, 32)
    caps, faces = pascal_tables(8)
    v = faces[4][3] + faces[8][2] + caps[4][3] * caps[8][6]
    assert v == 1_125_297

    cache = {key: base_sign(P, *key)
             for key in combinations(range(n), 3)}
    chambers = projection_chambers(P)
    assert len(chambers) == 968
    profiles = []
    reverse_formula_checks = 0
    for slope, order in chambers:
        profile = chain_totals(P, order, cache)
        profiles.append((profile[0] * profile[1], slope, profile, order))
        oa = [x for x in order if x < a]
        ob = [x - a for x in order if x >= a]
        if (oa == list(range(a - 1, -1, -1))
                and ob == list(range(b - 1, -1, -1))):
            assert cross_formula(A, B, order) == profile
            reverse_formula_checks += 1
    assert reverse_formula_checks == 112

    low = min(profiles)
    high = max(profiles)
    assert low[0] == 238_717_318
    assert low[2] in ((28_091, 8_498), (8_498, 28_091))
    assert high[0] == 585_612_820
    assert high[2] in ((327_158, 1_790), (1_790, 327_158))
    low_exp = log(low[0] / v, n)
    high_exp = log(high[0] / v, n)
    assert abs(low_exp - 1.545770719831959) < 1e-12
    assert abs(high_exp - 1.8046995007948516) < 1e-12
    return v, reverse_formula_checks, low_exp, high_exp


def diagonal_large_audit():
    A = marked_cell(7, 5, 0)
    B = marked_cell(12, 3, 1)
    P = glue(A, B)
    n = len(P)
    assert (len(A), len(B), n) == (21, 220, 241)
    tie = Q(-1, 2)
    below = above = None
    ties = 0
    for i, j in combinations(range(n), 2):
        dy = P[j].y - P[i].y
        if not dy:
            continue
        wall = -(P[j].x - P[i].x) / dy
        if wall < tie and (below is None or wall > below):
            below = wall
        elif wall > tie and (above is None or wall < above):
            above = wall
        elif wall == tie:
            ties += 1
    assert below is not None and above is not None and ties == 2

    rows = []
    for slope in ((below + tie) / 2, (tie + above) / 2):
        order = tuple(sorted(range(n),
                             key=lambda i: P[i].x + slope * P[i].y))
        rows.append(chain_totals(P, order))
    assert rows == [
        (32_878_891_214_924, 4_203_595),
        (36_975_789_791_508, 4_547_389),
    ]

    caps, faces = pascal_tables(12)
    v = faces[7][5] + faces[12][3] + caps[7][5] * caps[12][9]
    assert v == 10_085_586_308_253_842
    exponents = [log(c * u / v, n) for c, u in rows]
    assert abs(exponents[0] - 1.7366949127025124) < 1e-12
    assert abs(exponents[1] - 1.7724383748568637) < 1e-12
    return v, exponents


def main():
    v32, checked, low, high = small_all_chamber_audit()
    v241, diagonal = diagonal_large_audit()
    print("PASS: Pascal strong-glue projection spectrum; "
          f"N=32 V={v32}, reverse-shuffle formulas={checked}, "
          f"min/max exponents={low:.12f}/{high:.12f}; "
          f"N=241 V={v241}, diagonal exponents="
          f"{diagonal[0]:.12f}/{diagonal[1]:.12f}")


if __name__ == "__main__":
    main()
