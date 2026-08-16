#!/usr/bin/env python3
"""Checks for EXCESS_RANK_FIXED_LABEL_DOWNSHADOW_GATE.md."""

from fractions import Fraction as Q
from itertools import combinations
from math import comb, log2


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(hull(points)) == len(set(points))


def cloud(center, size, sign):
    epsilon = Q(1, 10**5 * size * size)
    return [
        (
            center[0] + epsilon * j,
            center[1] + epsilon * epsilon * sign * j * j,
        )
        for j in range(1, size + 1)
    ]


def all_subsets(points):
    yield ()
    for size in range(1, len(points) + 1):
        yield from combinations(points, size)


def hall_complete(rows, columns):
    return max(
        Q(a * b, a + b)
        for a in range(1, rows + 1)
        for b in range(1, columns + 1)
    )


def check_trace_counting():
    for n in range(3, 15):
        ground = tuple(range(n))
        for s in range(1, n + 1):
            completions = list(combinations(ground, s))
            for t in range(s + 1):
                counts = {}
                incidence = 0
                for completion in completions:
                    for trace in combinations(completion, t):
                        counts[trace] = counts.get(trace, 0) + 1
                        incidence += 1
                assert incidence == comb(n, s) * comb(s, t)
                assert len(counts) == comb(n, t)
                assert set(counts.values()) == {comb(n - t, s - t)}
                assert max(counts.values()) >= Q(
                    comb(s, t) * len(completions), comb(n, t)
                )


def check_hall_and_decoder():
    for rows in range(1, 30):
        for columns in range(1, 30):
            assert hall_complete(rows, columns) == Q(
                rows * columns, rows + columns
            )

    source_roles = frozenset(("b0", "b1", "d0", "d1", "d2"))
    pocket_roles = frozenset(("f0", "f1", "f2"))
    base = frozenset(("b0", "b1"))
    completion = frozenset(("d0", "d1", "d2"))
    pocket = frozenset(("f0", "f1", "f2"))
    released = base | pocket
    recovered_base = released & source_roles
    recovered_pocket = released & pocket_roles
    recovered_source = recovered_base | completion
    assert recovered_base == base
    assert recovered_pocket == pocket
    assert recovered_source == base | completion


def check_anti_aligned_geometry():
    source_center = (Q(1, 100), Q(50099, 10000))
    release_center = (Q(0), Q(-4))
    for p in range(3, 8):
        source = cloud(source_center, p, 1)
        released = cloud(release_center, p, -1)
        whole = source + released
        assert all(orient(*triple) != 0 for triple in combinations(whole, 3))

        actual_faces = 0
        for left in all_subsets(source):
            for right in all_subsets(released):
                face = convex(left + right)
                expected = (
                    not left
                    or not right
                    or (len(left) <= 2 and len(right) <= 2)
                )
                assert face == expected
                actual_faces += int(face)

        small_profile = p + comb(p, 2)
        expected_faces = 1 + 2 * (2**p - 1) + small_profile**2
        assert actual_faces == expected_faces

        for s in range(3, p + 1):
            rows = list(combinations(source, s))
            columns = list(combinations(released, s))
            m = comb(p, s)
            assert len(rows) == len(columns) == m
            assert hall_complete(m, m) == Q(m, 2)
            for left in rows:
                for right in columns:
                    assert not convex(left + right)

            for t in range(s + 1):
                fixed = rows[0][:t]
                degree = sum(set(fixed).issubset(row) for row in rows)
                assert degree == comb(p - t, s - t)


def check_bounded_rank_normalization_gap():
    # Finite diagnostics for the asymptotic Boolean-bank gap in Section 4.
    for p in (16, 32, 64, 128, 256):
        n = 2 * p
        rank_cap = max(3, int(2 * log2(n)))
        s = min(p, rank_cap)
        source_faces = comb(p, s)
        small_profile = p + comb(p, 2)
        all_faces = 1 + 2 * (2**p - 1) + small_profile**2
        assert source_faces < all_faces
        if p >= 64:
            assert log2(all_faces) - log2(source_faces) > p / 4


if __name__ == "__main__":
    check_trace_counting()
    check_hall_and_decoder()
    check_anti_aligned_geometry()
    check_bounded_rank_normalization_gap()
    print(
        "PASS: trace compression, decoder-safe Hall, anti-aligned rank-face "
        "codegrees, exact face recurrence, and normalization gap"
    )
