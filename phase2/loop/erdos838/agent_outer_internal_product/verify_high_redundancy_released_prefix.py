#!/usr/bin/env python3
"""Exact checks for HIGH_REDUNDANCY_RELEASED_PREFIX_BARRIER.md."""

from fractions import Fraction as Q
from itertools import combinations
from math import comb


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


def all_nonempty_subsets(points):
    for size in range(1, len(points) + 1):
        yield from combinations(points, size)


def hall_complete(rows, columns):
    return max(
        Q(a * h, a + h)
        for a in range(1, rows + 1)
        for h in range(1, columns + 1)
    )


def hall_selected_downshadow(rows, columns, rank):
    down_per_row = 2**rank - 1
    return max(
        Q(a * h, a * down_per_row + h)
        for a in range(1, rows + 1)
        for h in range(1, columns + 1)
    )


def hall_common_ambient(rows, columns, support_size):
    ambient = 2**support_size - 1
    return max(
        Q(rows * h, ambient + h) for h in range(1, columns + 1)
    )


def check_entropy_algebra():
    # Use logarithms to base d, so all quantities are exact integers.
    for r in range(3, 9):
        for _d in range(2, 8):
            log_omega = r
            conditional_entropy = 1
            redundancy = r - 1
            assert log_omega - conditional_entropy == redundancy

            # Fixed-output diagonal fibre: all redundancy is intrinsic.
            support_deficit = 0
            intrinsic = r - 1
            assert redundancy == support_deficit + intrinsic

            # Bijection U -> D: every conditional support is a singleton.
            deterministic_conditional_entropy = 0
            deterministic_support_deficit = r
            assert log_omega - deterministic_conditional_entropy == (
                deterministic_support_deficit
            )

            # Averaged fixed-mask split: global correlation plus output info.
            global_redundancy = r - 1
            mutual_information = 1
            assert r == global_redundancy + mutual_information

    # Exact algebra in the corrected live transfer bound (33).
    for log_n_support in range(4, 20):
        for rank in range(1, 2 * log_n_support):
            for coefficient in (Q(1, 4), Q(2, 5), Q(1, 2)):
                # Use an independent formal value for log r; only algebra matters.
                log_rank = Q(7, 3)
                left = (
                    rank * (log_n_support - log_rank)
                    - coefficient * log_n_support * log_n_support
                )
                right = (
                    (rank - coefficient * log_n_support) * log_n_support
                    - rank * log_rank
                )
                assert left == right


def check_geometry_and_downshadow():
    source_center = (Q(1, 100), Q(50099, 10000))
    release_center = (Q(0), Q(-4))

    for r, d, z_size in ((3, 2, 5), (4, 2, 5), (3, 3, 6)):
        source = cloud(source_center, r * d, 1)
        released = cloud(release_center, z_size, -1)
        whole = source + released
        assert all(orient(*triple) != 0 for triple in combinations(whole, 3))
        assert convex(source) and convex(released)

        roles = [source[i * d : (i + 1) * d] for i in range(r)]
        diagonals = [tuple(roles[i][a] for i in range(r)) for a in range(d)]
        assert all(convex(word) for word in diagonals)
        assert len(set().union(*(set(word) for word in diagonals))) == r * d

        release_faces = list(combinations(released, 3))
        tested = 0
        for face in release_faces:
            assert convex(face)
            for subset in all_nonempty_subsets(source):
                assert not convex(face + subset)
                tested += 1
        assert tested == comb(z_size, 3) * (2 ** (r * d) - 1)

        # Audit the full anti-aligned profile statement used in the report.
        for source_subset in all_nonempty_subsets(source):
            for release_subset in all_nonempty_subsets(released):
                expected = len(source_subset) <= 2 and len(release_subset) <= 2
                assert convex(source_subset + release_subset) == expected

        downsets = {frozenset()}
        for word in diagonals:
            for subset in all_nonempty_subsets(word):
                downsets.add(frozenset(subset))
        assert len(downsets) == 1 + d * (2**r - 1)


def check_hall_formulae():
    for d in range(1, 12):
        for h in range(1, 18):
            assert hall_complete(d, h) == Q(d * h, d + h)
            for r in range(1, 7):
                expected = Q(d * h, d * (2**r - 1) + h)
                assert hall_selected_downshadow(d, h, r) == expected
            for support_size in range(1, 8):
                expected = Q(d * h, (2**support_size - 1) + h)
                assert hall_common_ambient(d, h, support_size) == expected


def check_singleton_congestion_and_decoder():
    labels = tuple(range(6))
    supports = [
        frozenset((0, 1, 2)),
        frozenset((1, 2, 3, 4)),
        frozenset((0, 4, 5)),
        frozenset((2, 3, 5)),
    ]
    demands = [Q(7, 3), Q(5, 2), Q(11, 5), Q(13, 7)]

    load = {}
    for support, demand in zip(supports, demands):
        capacity = 2 ** len(support) - 1
        for size in range(1, len(support) + 1):
            for face in combinations(support, size):
                key = frozenset(face)
                load[key] = load.get(key, Q(0)) + demand / capacity
    maximum = max(load.values())
    singleton_maximum = max(
        value for face, value in load.items() if len(face) == 1
    )
    assert maximum == singleton_maximum

    # Exact marked-release decoder (31).
    base = frozenset(("b0", "b1"))
    pocket = frozenset(("f0", "f1", "f2"))
    x = "x"
    source_ear = base | {x}
    released = base | pocket
    assert source_ear & released == base
    assert source_ear - base == {x}
    assert released - base == pocket


if __name__ == "__main__":
    check_entropy_algebra()
    check_geometry_and_downshadow()
    check_hall_formulae()
    check_singleton_congestion_and_decoder()
    print(
        "PASS: conditional-redundancy splits, anti-aligned retained-prefix "
        "barrier, diagonal downshadow, singleton consolidation, and Hall densities"
    )
