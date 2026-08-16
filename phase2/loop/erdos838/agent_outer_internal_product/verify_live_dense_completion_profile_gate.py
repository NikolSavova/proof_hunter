#!/usr/bin/env python3
"""Checks for LIVE_DENSE_COMPLETION_PROFILE_GATE.md."""

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


def hall_density(edges):
    """Brute-force Hall density for a small simple bipartite graph."""
    edge_list = list(edges)
    best = Q(0)
    for mask in range(1, 1 << len(edge_list)):
        left = set()
        right = set()
        count = 0
        for index, (u, v) in enumerate(edge_list):
            if mask >> index & 1:
                count += 1
                left.add(u)
                right.add(v)
        best = max(best, Q(count, len(left) + len(right)))
    return best


def weighted_hall_density(records):
    best = Q(0)
    witness = []
    for mask in range(1, 1 << len(records)):
        left = set()
        right = set()
        weight = Q(0)
        for index, (u, v, value) in enumerate(records):
            if mask >> index & 1:
                left.add(u)
                right.add(v)
                weight += value
        density = weight / (len(left) + len(right))
        if density > best:
            best = density
            witness = [
                record for index, record in enumerate(records) if mask >> index & 1
            ]
    return best, witness


def hall_complete(rows, columns):
    return max(
        Q(a * b, a + b)
        for a in range(1, rows + 1)
        for b in range(1, columns + 1)
    )


def prune(edges, threshold):
    """Unweighted version of the minimum-degree pruning theorem."""
    remaining = set(edges)
    changed = True
    while changed and remaining:
        changed = False
        left_degree = {}
        right_degree = {}
        for left, right in remaining:
            left_degree[left] = left_degree.get(left, 0) + 1
            right_degree[right] = right_degree.get(right, 0) + 1
        low_left = {v for v, degree in left_degree.items() if degree <= threshold}
        low_right = {v for v, degree in right_degree.items() if degree <= threshold}
        if low_left or low_right:
            remaining = {
                edge
                for edge in remaining
                if edge[0] not in low_left and edge[1] not in low_right
            }
            changed = True
    return remaining


def weighted_prune(records, threshold):
    remaining = list(records)
    while remaining:
        left_degree = {}
        right_degree = {}
        for left, right, weight in remaining:
            left_degree[left] = left_degree.get(left, Q(0)) + weight
            right_degree[right] = right_degree.get(right, Q(0)) + weight
        low_left = {v for v, degree in left_degree.items() if degree <= threshold}
        low_right = {v for v, degree in right_degree.items() if degree <= threshold}
        if not low_left and not low_right:
            return remaining
        remaining = [
            record
            for record in remaining
            if record[0] not in low_left and record[1] not in low_right
        ]
    return []


def check_hall_transfer():
    examples = [
        {(i, j) for i in range(3) for j in range(4)},
        {(i, j) for i in range(5) for j in range(5) if (i + j) % 3},
        {(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)},
    ]
    for edges in examples:
        eta = hall_density(edges)
        for threshold in range(int(eta)):
            core = prune(edges, threshold)
            assert core
            left_degree = {}
            right_degree = {}
            for left, right in core:
                left_degree[left] = left_degree.get(left, 0) + 1
                right_degree[right] = right_degree.get(right, 0) + 1
            assert min(left_degree.values()) > threshold
            assert min(right_degree.values()) > threshold
            assert len(left_degree) > threshold
            assert len(right_degree) > threshold

    for rows in range(1, 12):
        for columns in range(1, 12):
            assert hall_complete(rows, columns) == Q(
                rows * columns, rows + columns
            )

    weighted = [
        ("a", "x", Q(3, 2)),
        ("a", "y", Q(1, 2)),
        ("b", "y", Q(5, 4)),
        ("b", "z", Q(7, 4)),
        ("c", "z", Q(2)),
        ("c", "x", Q(3, 4)),
    ]
    eta, witness = weighted_hall_density(weighted)
    pair_cap = max(value for _left, _right, value in weighted)
    threshold = eta / 2
    core = weighted_prune(witness, threshold)
    assert core
    left_vertices = {left for left, _right, _weight in core}
    right_vertices = {right for _left, right, _weight in core}
    assert len(left_vertices) > threshold / pair_cap
    assert len(right_vertices) > threshold / pair_cap


def check_normalization_arithmetic():
    for volume in (10**6, 10**9, 10**12):
        for s, n, gamma, xi, theta, delta in (
            (8, 100, 3, 5, 7, 2),
            (20, 1000, 11, 13, 17, 3),
        ):
            h = Q(volume, theta)
            eta = Q(s, 2 * n * gamma * xi) * h
            transferred = eta / (2 * delta)
            expected = Q(s * volume, 4 * n * gamma * xi * theta * delta)
            assert transferred == expected


def check_anti_aligned_profile_gate():
    source_center = (Q(1, 100), Q(50099, 10000))
    release_center = (Q(0), Q(-4))
    for p in range(3, 8):
        source = cloud(source_center, p, 1)
        released = cloud(release_center, p, -1)
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
        formula = 1 + 2 * (2**p - 1) + small_profile**2
        assert actual_faces == formula

        for rank in range(3, p + 1):
            left_faces = list(combinations(source, rank))
            right_faces = list(combinations(released, rank))
            assert all(
                not convex(left + right)
                for left in left_faces
                for right in right_faces
            )
            m = comb(p, rank)
            assert hall_complete(m, m) == Q(m, 2)

            fixed_x = source[0]
            fixed_left = [face for face in left_faces if fixed_x in face]
            assert len(fixed_left) == comb(p - 1, rank - 1)
            assert all(
                not convex(left + right)
                for left in fixed_left
                for right in right_faces
            )
            assert hall_complete(len(fixed_left), m) == Q(
                len(fixed_left) * m, len(fixed_left) + m
            )


def check_bounded_rank_gap():
    for p in (32, 64, 128, 256):
        n = 2 * p
        rank = min(p, max(3, int(2 * log2(n))))
        side = comb(p, rank)
        profile = p + comb(p, 2)
        whole = 1 + 2 * (2**p - 1) + profile**2
        assert side < whole
        if p >= 64:
            assert log2(whole) - log2(side) > p / 4


if __name__ == "__main__":
    check_hall_transfer()
    check_normalization_arithmetic()
    check_anti_aligned_profile_gate()
    check_bounded_rank_gap()
    print(
        "PASS: Hall normalization transfer, profile recurrence, anti-aligned "
        "dense rectangle, and bounded-rank normalization gap"
    )
