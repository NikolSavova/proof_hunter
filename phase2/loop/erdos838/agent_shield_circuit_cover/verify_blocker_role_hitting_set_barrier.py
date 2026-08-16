#!/usr/bin/env python3
"""Exact audit for BLOCKER_ROLE_HITTING_SET_BARRIER.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations


Point = tuple[Q, Q]


def det(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points: tuple[Point, ...]) -> tuple[Point, ...]:
    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return tuple(ordered)
    lower: list[Point] = []
    for point in ordered:
        while (len(lower) >= 2
               and det(lower[-2], lower[-1], point) <= 0):
            lower.pop()
        lower.append(point)
    upper: list[Point] = []
    for point in reversed(ordered):
        while (len(upper) >= 2
               and det(upper[-2], upper[-1], point) <= 0):
            upper.pop()
        upper.append(point)
    return tuple(lower[:-1] + upper[:-1])


def convex(points: tuple[Point, ...]) -> bool:
    return len(set(points)) == len(points) == len(hull(points))


def barycentric(point: Point, triangle: tuple[Point, Point, Point]) -> tuple[Q, Q, Q]:
    first, second, third = triangle
    denominator = det(first, second, third)
    return (
        det(point, second, third) / denominator,
        det(first, point, third) / denominator,
        det(first, second, point) / denominator,
    )


def construction(m: int, k: int) -> tuple[tuple[Point, ...], tuple[Point, ...]]:
    delta = Q(1, 100 * m * m)
    local = tuple(
        (Q(2) - delta * t * t, -Q(1, 5) + delta * t)
        for t in range(1, m + 1)
    )
    epsilon = Q(1, 100 * k)
    blockers = tuple(
        (epsilon * u, Q(4) - epsilon * epsilon * u * u)
        for u in range(k - 1, -k, -2)
    )
    assert len(blockers) == k
    return local, blockers


def main() -> None:
    m, k = 6, 7
    local, blockers = construction(m, k)
    all_points = local + blockers

    gp_triples = 0
    for triple in combinations(all_points, 3):
        assert det(*triple) != 0
        gp_triples += 1

    # Complete same-type product: X_0 is the only nonsingleton block.
    sign_vectors = set()
    for point in local:
        word = (point,) + blockers
        assert convex(word)
        signs = tuple(
            1 if det(word[i], word[j], word[ell]) > 0 else -1
            for i, j, ell in combinations(range(k + 1), 3)
        )
        assert signs == (1,) * len(signs)
        sign_vectors.add(signs)
    assert len(sign_vectors) == 1

    containments = 0
    for i, j, ell in combinations(range(m), 3):
        for blocker in blockers:
            coordinates = barycentric(
                local[j], (local[i], local[ell], blocker)
            )
            assert sum(coordinates, Q()) == 1
            assert all(value > 0 for value in coordinates)
            containments += 1
    assert containments == (m * (m - 1) * (m - 2) // 6) * k

    # Every blocker role is a mandatory loop; deleting all is sufficient.
    for blocker in blockers:
        assert not convex(local + (blocker,))
    assert convex(local)
    deletion_depth = k

    # Exhaust the full face recurrence.
    actual_faces = 0
    predicted_faces = 0
    for local_mask in range(1 << m):
        local_trace = tuple(
            local[i] for i in range(m) if local_mask >> i & 1
        )
        for blocker_mask in range(1 << k):
            blocker_trace = tuple(
                blockers[i]
                for i in range(k)
                if blocker_mask >> i & 1
            )
            actual = convex(local_trace + blocker_trace)
            predicted = not blocker_trace or len(local_trace) <= 2
            assert actual == predicted
            actual_faces += int(actual)
            predicted_faces += int(predicted)

    rank_two = 1 + m + m * (m - 1) // 2
    formula = (1 << m) + rank_two * ((1 << k) - 1)
    assert actual_faces == predicted_faces == formula

    print(
        "PASS: "
        f"m={m}, k={k}; GP triples={gp_triples}; "
        f"same-type transversals={m}; containments={containments}; "
        f"deletion depth={deletion_depth}; exact faces={actual_faces}"
    )


if __name__ == "__main__":
    main()
