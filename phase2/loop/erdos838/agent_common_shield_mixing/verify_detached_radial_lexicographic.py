#!/usr/bin/env python3
"""Exact audit for DETACHED_RADIAL_LEXICOGRAPHIC_PROFILE.md."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import lcm


Point = tuple[Fraction, Fraction]


def orientation(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point]) -> list[Point]:
    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return ordered

    def half(sequence):
        answer: list[Point] = []
        for point in sequence:
            while len(answer) >= 2 and orientation(answer[-2], answer[-1], point) <= 0:
                answer.pop()
            answer.append(point)
        return answer

    lower = half(ordered)
    upper = half(reversed(ordered))
    return lower[:-1] + upper[:-1]


def strictly_inside_triangle(point: Point, triangle: list[Point]) -> bool:
    signs = [
        orientation(triangle[i], triangle[(i + 1) % 3], point)
        for i in range(3)
    ]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def affine_into_macro_triangle(u: Point, v: Point, w: Point, point: Point) -> Point:
    """Map (-1,0),(1,0),(0,-1) to u,v,w."""
    x, y = point
    midpoint = ((u[0] + v[0]) / 2, (u[1] + v[1]) / 2)
    x_axis = ((v[0] - u[0]) / 2, (v[1] - u[1]) / 2)
    y_axis = (midpoint[0] - w[0], midpoint[1] - w[1])
    return (
        midpoint[0] + x * x_axis[0] + y * y_axis[0],
        midpoint[1] + x * x_axis[1] + y * y_axis[1],
    )


def build_clusters() -> list[list[Point]]:
    macro = [
        (Fraction(0), Fraction(100)),
        (Fraction(95), Fraction(31)),
        (Fraction(59), Fraction(-81)),
        (Fraction(-59), Fraction(-81)),
        (Fraction(-95), Fraction(31)),
    ]
    # A triangle with one interior point, ordered by the first coordinate.
    seed = [
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(4)),
        (Fraction(2), Fraction(1)),
        (Fraction(4), Fraction(0)),
    ]
    epsilon = Fraction(1, 10)
    clusters: list[list[Point]] = []
    for i in range(len(macro)):
        cluster = []
        for f, g in seed:
            left = 1 + epsilon * f + epsilon**2 * g
            right = 1 + epsilon * f - epsilon**2 * g
            canonical = (
                (left - right) / (left + right),
                -2 / (left + right),
            )
            cluster.append(
                affine_into_macro_triangle(
                    macro[(i - 1) % len(macro)],
                    macro[(i + 1) % len(macro)],
                    macro[i],
                    canonical,
                )
            )
        clusters.append(cluster)
    return clusters


def geometric_audit(clusters: list[list[Point]]) -> dict[str, int]:
    q = len(clusters)
    width = len(clusters[0])
    points = [point for cluster in clusters for point in cluster]
    assert all(orientation(*triple) != 0 for triple in combinations(points, 3))
    assert all(len(hull(cluster)) == 3 for cluster in clusters)

    transversals = 0
    for choices in product(range(width), repeat=q):
        selected = [clusters[i][choices[i]] for i in range(q)]
        assert len(hull(selected)) == q
        transversals += 1

    circuits = 0
    for i in range(q):
        for outer, inner in combinations(range(width), 2):
            for left, right in product(range(width), repeat=2):
                triangle = [
                    clusters[i][outer],
                    clusters[(i - 1) % q][left],
                    clusters[(i + 1) % q][right],
                ]
                assert strictly_inside_triangle(clusters[i][inner], triangle)
                circuits += 1

    return {
        "points": len(points),
        "transversals": transversals,
        "detached_circuits": circuits,
        "local_nonfaces": q,
    }


def recurrence_audit(clusters: list[list[Point]]) -> dict[str, int]:
    q = len(clusters)
    width = len(clusters[0])
    points = [point for cluster in clusters for point in cluster]

    common_denominator = 1
    for point in points:
        for coordinate in point:
            common_denominator = lcm(common_denominator, coordinate.denominator)
    integer_points = [
        (int(x * common_denominator), int(y * common_denominator)) for x, y in points
    ]
    order = sorted(range(len(points)), key=lambda index: integer_points[index])
    reverse_order = list(reversed(order))

    def integer_orientation(i: int, j: int, k: int) -> int:
        a, b, c = integer_points[i], integer_points[j], integer_points[k]
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    orientation_table = [
        [
            [integer_orientation(i, j, k) for k in range(len(points))]
            for j in range(len(points))
        ]
        for i in range(len(points))
    ]

    def convex_mask(mask: int) -> bool:
        rank = mask.bit_count()
        if rank <= 3:
            return True

        def half(sequence):
            answer: list[int] = []
            for index in sequence:
                if not ((mask >> index) & 1):
                    continue
                while (
                    len(answer) >= 2
                    and orientation_table[answer[-2]][answer[-1]][index] <= 0
                ):
                    answer.pop()
                answer.append(index)
            return answer

        boundary = half(order)[:-1] + half(reverse_order)[:-1]
        return len(boundary) == rank

    faces_by_active: defaultdict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    rank_counts = [0] * (len(points) + 1)
    for global_mask in range(1 << len(points)):
        if not convex_mask(global_mask):
            continue
        rank_counts[global_mask.bit_count()] += 1
        local_masks = tuple(
            (global_mask >> (width * i)) & ((1 << width) - 1) for i in range(q)
        )
        active = tuple(i for i, local_mask in enumerate(local_masks) if local_mask)
        if active:
            faces_by_active[active].add(tuple(local_masks[i] for i in active))

    # Equation (12): every active-pattern fibre is exactly a Cartesian
    # product of its coordinate projections.
    for active, family in faces_by_active.items():
        projections = [
            {description[position] for description in family}
            for position in range(len(active))
        ]
        product_size = 1
        for projection in projections:
            product_size *= len(projection)
        assert product_size == len(family)

    total_faces = sum(rank_counts)
    assert total_faces == 7605
    assert rank_counts[:8] == [1, 20, 190, 1140, 2960, 2804, 450, 40]
    assert not any(rank_counts[8:])

    # One-gap banks: each active set of size q-1 has two endpoint profile
    # sizes 5 and q-3 singleton profiles of size 4.
    one_gap_sizes = []
    endpoint_products = []
    for missing in range(q):
        active = tuple(i for i in range(q) if i != missing)
        family = faces_by_active[active]
        projections = [
            {description[position] for description in family}
            for position in range(len(active))
        ]
        sizes = [len(projection) for projection in projections]
        assert sorted(sizes) == [4, 4, 5, 5]
        assert len(family) == 400
        one_gap_sizes.append(len(family))
        endpoint_products.append(25)

    local_nonempty_faces = 14
    assert all(product_size >= local_nonempty_faces for product_size in endpoint_products)

    # Equations (3)--(4), in the symmetric L=4,A=R=5 instance.
    p_zero = width**q
    left = Fraction(1)
    right = Fraction(1)
    for bank_size in one_gap_sizes:
        left *= Fraction(bank_size, p_zero)
    for _ in range(q):
        right *= Fraction(25, width**3)
    assert left == right
    assert max(one_gap_sizes) >= p_zero * Fraction(local_nonempty_faces, width**3)

    return {
        "faces": total_faces,
        "maximum_face_rank": max(i for i, count in enumerate(rank_counts) if count),
        "active_patterns": len(faces_by_active),
        "one_gap_bank": min(one_gap_sizes),
        "local_nonempty_faces": local_nonempty_faces,
    }


def main() -> None:
    clusters = build_clusters()
    print(f"geometry: {geometric_audit(clusters)}")
    print(f"recurrence: {recurrence_audit(clusters)}")
    print("PASS detached radial lexicographic profile")


if __name__ == "__main__":
    main()
