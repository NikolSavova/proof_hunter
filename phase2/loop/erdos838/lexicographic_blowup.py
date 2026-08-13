#!/usr/bin/env python3
"""Exact audit for the vertical lexicographic blow-up construction.

If ``S`` and ``Q`` are point configurations in increasing x-order, ``S[Q]``
replaces every point of S by a sufficiently thin, almost-vertical copy of Q.
The resulting order type has the following signs for i<j<k:

* three different macro-blocks: the sign in S;
* one macro-block: the sign in Q;
* the first two points in one block: negative;
* the last two points in one block: positive.

This script checks the exact cap, cup, and convex-subset substitution formulas
against an independent endpoint-chain dynamic program.  It uses the six-point
central Pascal cell as a small but nontrivial test case.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import log2

from agent_geometry.audit_geometry import (
    Point,
    cell,
    is_cap,
    is_convex,
    is_cup,
    normalized,
    orient_table,
)


def profiles(orient: list[list[list[int]]]) -> tuple[list[int], list[int], list[int]]:
    """Return nonempty cap, cup, and convex profiles, indexed by cardinality."""
    n = len(orient)
    cap = [0] * (n + 1)
    cup = [0] * (n + 1)
    convex = [0] * (n + 1)
    for size in range(1, n + 1):
        for subset in combinations(range(n), size):
            cap[size] += is_cap(subset, orient)
            cup[size] += is_cup(subset, orient)
            convex[size] += is_convex(subset, orient)
    return cap, cup, convex


def compose_orient(
    macro: list[list[list[int]]], micro: list[list[list[int]]]
) -> list[list[list[int]]]:
    """Return the vertical lexicographic composition order type S[Q]."""
    s, q = len(macro), len(micro)
    n = s * q
    out = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i, j, k in combinations(range(n), 3):
        bi, bj, bk = i // q, j // q, k // q
        if bi == bk:
            sign = micro[i % q][j % q][k % q]
        elif bi == bj:
            sign = -1
        elif bj == bk:
            sign = 1
        else:
            sign = macro[bi][bj][bk]
        out[i][j][k] = sign
    return out


def realize_composition(
    skeleton: tuple[Point, ...], microset: tuple[Point, ...]
) -> tuple[tuple[Point, ...], Fraction]:
    """Find exact rational coordinates realizing the abstract composition."""
    skeleton = normalized(skeleton)
    microset = normalized(microset)
    target = compose_orient(orient_table(skeleton), orient_table(microset))
    for exponent in range(1, 100):
        epsilon = Fraction(1, 2**exponent)
        points = tuple(
            Point(
                macro.x + epsilon**2 * micro.x,
                macro.y + epsilon * micro.y,
                f"{i}:{j}",
            )
            for i, macro in enumerate(skeleton)
            for j, micro in enumerate(microset)
        )
        increasing = all(
            points[index].x < points[index + 1].x
            and points[index].y < points[index + 1].y
            for index in range(len(points) - 1)
        )
        if not increasing:
            continue
        try:
            realized_orient = orient_table(points)
        except AssertionError:
            continue
        if realized_orient == target:
            return points, epsilon
    raise AssertionError("failed to realize the vertical composition")


def chain_totals(orient: list[list[list[int]]]) -> tuple[int, int]:
    """Count nonempty caps and cups by their final edge."""
    n = len(orient)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cap[i][j] = cup[i][j] = 1
            for h in range(i):
                if orient[h][i][j] < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def convex_total(orient: list[list[list[int]]]) -> int:
    """Count nonempty convex subsets by their left/right hull endpoints."""
    n = len(orient)
    total = n
    for start in range(n):
        cap = [[0] * n for _ in range(n)]
        cup = [[0] * n for _ in range(n)]
        for end in range(start + 1, n):
            cap[start][end] = cup[start][end] = 1
        for middle in range(start + 1, n):
            for end in range(middle + 1, n):
                cap[middle][end] = sum(
                    cap[previous][middle]
                    for previous in range(start, middle)
                    if orient[previous][middle][end] < 0
                )
                cup[middle][end] = sum(
                    cup[previous][middle]
                    for previous in range(start, middle)
                    if orient[previous][middle][end] > 0
                )
        for end in range(start + 1, n):
            caps = sum(cap[previous][end] for previous in range(start, end))
            cups = sum(cup[previous][end] for previous in range(start, end))
            total += caps * cups
    return total


def evaluate_polynomial(profile: list[int], q: int, shift: int) -> int:
    return sum(count * q ** (size - shift) for size, count in enumerate(profile) if size >= shift)


def predicted_totals(
    macro_profiles: tuple[list[int], list[int], list[int]],
    micro_totals: tuple[int, int, int],
    q: int,
) -> tuple[int, int, int]:
    """Exact substitution formulas for nonempty caps, cups, convex subsets."""
    macro_cap, macro_cup, macro_convex = macro_profiles
    micro_cap, micro_cup, micro_convex = micro_totals
    s = macro_convex[1]
    # Every singleton macro subset corresponds to one block, so this is |S|.
    assert s == len(macro_cap) - 1
    cap = micro_cap * evaluate_polynomial(macro_cap, q, 1)
    cup = micro_cup * evaluate_polynomial(macro_cup, q, 1)
    convex = s * micro_convex + micro_cap * micro_cup * evaluate_polynomial(
        macro_convex, q, 2
    )
    return cap, cup, convex


def audit_case(skeleton: tuple[Point, ...], microset: tuple[Point, ...], brute: bool) -> None:
    macro = orient_table(skeleton)
    micro = orient_table(microset)
    macro_profiles = profiles(macro)
    micro_totals = tuple(sum(profile) for profile in profiles(micro))
    composed = compose_orient(macro, micro)
    realized, epsilon = realize_composition(skeleton, microset)
    assert orient_table(realized) == composed

    predicted = predicted_totals(macro_profiles, micro_totals, len(micro))
    audited = (*chain_totals(composed), convex_total(composed))
    if brute:
        brute_totals = tuple(sum(profile) for profile in profiles(composed))
        assert brute_totals == audited
    print(f"skeleton size={len(skeleton)}, micro size={len(microset)}")
    print(f"exact rational realization epsilon={epsilon}")
    print(f"macro cap profile={macro_profiles[0][1:]}")
    print(f"macro cup profile={macro_profiles[1][1:]}")
    print(f"macro convex profile={macro_profiles[2][1:]}")
    print(f"predicted (cap,cup,convex)={predicted}")
    print(f"audited   (cap,cup,convex)={audited}")
    if predicted != audited:
        raise AssertionError("vertical blow-up substitution formula failed")


def audit_iteration(skeleton: tuple[Point, ...], depth: int) -> None:
    """Iterate the exact scalar recurrences and compare with the rate formula."""
    orient = orient_table(skeleton)
    macro_profiles = profiles(orient)
    cap_profile, cup_profile, _ = macro_profiles
    largest_cap = max(i for i, count in enumerate(cap_profile) if count)
    largest_cup = max(i for i, count in enumerate(cup_profile) if count)
    size = cap = cup = convex = 1
    for _ in range(depth):
        cap, cup, convex = predicted_totals(
            macro_profiles, (cap, cup, convex), size
        )
        size *= len(skeleton)
    target = (largest_cap + largest_cup - 2) / (2 * log2(len(skeleton)))
    rate = log2(convex) / log2(size) ** 2
    print(
        f"iteration depth={depth}, size={size}, normalized rate={rate:.9f}, "
        f"limit={target:.9f}"
    )


def main() -> None:
    # The 9-point case permits a completely independent 2^9 subset census.
    audit_case(cell(3, 1), cell(3, 1), brute=True)
    print()
    # The 36-point case exercises nontrivial four-point macro-convex sets;
    # endpoint factorization avoids an infeasible 2^36 enumeration.
    audit_case(cell(4, 2), cell(4, 2), brute=False)
    audit_iteration(cell(4, 2), depth=20)


if __name__ == "__main__":
    main()
