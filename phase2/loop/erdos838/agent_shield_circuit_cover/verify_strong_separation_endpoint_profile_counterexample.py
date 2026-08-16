#!/usr/bin/env python3
"""Exact audit for STRONG_SEPARATION_ENDPOINT_PROFILE_COUNTEREXAMPLE.md."""

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


def construction(m: int) -> tuple[tuple[Point, ...], Point, Point, Point]:
    delta = Q(1, 100 * m * m)
    block = tuple(
        (Q(2) - delta * t * t, -Q(1, 5) + delta * t)
        for t in range(1, m + 1)
    )
    a = (Q(0), Q(0))
    b = (Q(4), Q(0))
    c = (Q(0), Q(4))
    return block, a, b, c


def main() -> None:
    m = 14
    block, a, b, c = construction(m)
    all_points = block + (a, b, c)

    # Full general position, including the signs involving two child points.
    triple_count = 0
    for triple in combinations(all_points, 3):
        assert det(*triple) != 0
        triple_count += 1

    # Every transversal has the same positive cyclic type and is convex.
    type_vectors = set()
    for point in block:
        word = (point, b, c, a)
        type_vector = tuple(
            1 if det(word[i], word[j], word[k]) > 0 else -1
            for i, j, k in combinations(range(4), 3)
        )
        assert type_vector == (1, 1, 1, 1)
        assert convex(word)
        type_vectors.add(type_vector)
    assert type_vectors == {(1, 1, 1, 1)}

    # X_1 is convex-position: every nonempty subset is a local face.
    local_faces = 0
    compatible_ac = 0
    compatible_bc = 0
    bad_large_ac = 0
    bad_large_bc = 0
    for mask in range(1, 1 << m):
        trace = tuple(block[i] for i in range(m) if mask >> i & 1)
        assert convex(trace)
        local_faces += 1
        good_ac = convex(trace + (a, c))
        good_bc = convex(trace + (b, c))
        compatible_ac += int(good_ac)
        compatible_bc += int(good_bc)
        if len(trace) >= 3:
            assert not good_ac
            assert not good_bc
            bad_large_ac += 1
            bad_large_bc += 1
    assert local_faces == (1 << m) - 1

    # Every middle point is strictly inside the triangle of the two outer
    # parabola points and c.  Audit both determinants and barycentrics.
    containments = 0
    delta = Q(1, 100 * m * m)
    for i, j, k in combinations(range(m), 3):
        first, middle, last = block[i], block[j], block[k]
        actual = det(first, last, middle)
        expected = (delta * delta * (k - i) * (j - i) * (j - k))
        assert actual == expected < 0
        coordinates = barycentric(middle, (first, last, c))
        assert sum(coordinates, Q()) == 1
        assert all(value > 0 for value in coordinates)
        containments += 1
    assert containments == 364

    rank_two_bound = m + m * (m - 1) // 2
    assert compatible_ac <= rank_two_bound
    assert compatible_bc <= rank_two_bound
    assert rank_two_bound == 105
    assert rank_two_bound**2 == 11025
    assert rank_two_bound**2 < local_faces == 16383
    assert (rank_two_bound + 1) ** 2 < local_faces

    print(
        "PASS: "
        f"m={m}; GP triples={triple_count}; transversals={m}; "
        f"local faces={local_faces}; middle containments={containments}; "
        f"compatible(ac,bc)=({compatible_ac},{compatible_bc}); "
        f"profile upper square={rank_two_bound**2}"
    )


if __name__ == "__main__":
    main()
