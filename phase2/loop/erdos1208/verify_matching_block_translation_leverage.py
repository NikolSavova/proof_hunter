#!/usr/bin/env python3
"""Exact certificates for MATCHING_BLOCK_TRANSLATION_LEVERAGE.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product

from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_metric_scalar_squareclass_transverse import endpoint_map


Point = tuple[int, int]
Edge = tuple[Point, Point]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def squared_norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def distance_sidon(points: list[Point]) -> bool:
    distances = [
        squared_norm(subtract(first, second))
        for first, second in combinations(points, 2)
    ]
    return len(distances) == len(set(distances))


def ordered(edge: Edge) -> Edge:
    return tuple(sorted(edge))  # type: ignore[return-value]


def matching(edges: list[Edge]) -> bool:
    vertices = [vertex for edge in edges for vertex in edge]
    return len(vertices) == len(set(vertices))


def explicit_double_matching(length: int, base: int = 10) -> tuple[
    list[Point], Point, list[Edge], list[Edge]
]:
    """The infinite balanced-base clean double-matching construction."""
    assert length >= 1 and base >= 10
    b = (0, 0)
    a = (1, 0)
    points = [b, a]
    source: list[Edge] = []
    target: list[Edge] = []
    for index in range(length):
        c = (base ** (3 * index + 1), 0)
        d = (base ** (3 * index + 2), 0)
        e = (base ** (3 * index + 3), 0)
        f = (1 + c[0] + d[0] - e[0], 0)
        points.extend((c, d, e, f))
        source.append(ordered((c, d)))
        target.append(ordered((e, f)))

    q_value = subtract(a, b)
    assert len(points) == 4 * length + 2
    assert len(points) == len(set(points))
    assert distance_sidon(points)
    assert matching(source) and matching(target)
    assert set(vertex for edge in source for vertex in edge).isdisjoint(
        vertex for edge in target for vertex in edge
    )
    for source_edge, target_edge in zip(source, target):
        assert add(*target_edge) == add(add(*source_edge), q_value)
        assert set((a, b, *source_edge, *target_edge)).__len__() == 6

    # Translate onto the nonnegative x-axis; every identity is preserved.
    shift = -min(point[0] for point in points)
    translate = lambda point: (point[0] + shift, point[1])
    translated_points = [translate(point) for point in points]
    translated_source = [ordered(tuple(map(translate, edge))) for edge in source]
    translated_target = [ordered(tuple(map(translate, edge))) for edge in target]
    return translated_points, q_value, translated_source, translated_target


def endpoint_profile(
    points: list[Point], q_value: Point, source: list[Edge], target: list[Edge]
) -> tuple[int, int, int, int, int]:
    length = len(source)
    source_degree = Counter(vertex for edge in source for vertex in edge)
    target_degree = Counter(vertex for edge in target for vertex in edge)
    assert all(degree == 1 for degree in source_degree.values())
    discrepancy = {
        point: target_degree[point] - source_degree[point]
        for point in points
    }
    assert sum(discrepancy.values()) == 0
    moment = (
        sum(discrepancy[point] * point[0] for point in points),
        sum(discrepancy[point] * point[1] for point in points),
    )
    assert moment == (length * q_value[0], length * q_value[1])

    wedges = sum(degree * (degree - 1) // 2 for degree in target_degree.values())
    source_vertices = set(source_degree)
    escape = sum(
        degree for point, degree in target_degree.items() if point not in source_vertices
    )
    discrepancy_square = sum(value * value for value in discrepancy.values())
    assert discrepancy_square == 2 * (wedges + escape)

    inertia = sum(squared_norm(point) for point in points)
    assert length * length * squared_norm(q_value) <= discrepancy_square * inertia
    return length, wedges, escape, discrepancy_square, max(target_degree.values())


def wedge_moments(edges: list[tuple[int, int]]) -> tuple[int, int, int, int]:
    neighbours: dict[int, set[int]] = {}
    for left, right in edges:
        neighbours.setdefault(left, set()).add(right)
        neighbours.setdefault(right, set()).add(left)
    wedges = sum(len(values) * (len(values) - 1) // 2 for values in neighbours.values())
    loads: Counter[tuple[int, int]] = Counter()
    for center, values in neighbours.items():
        for first, second in product(values, repeat=2):
            if first != second:
                loads[first, second] += 1
    assert sum(loads.values()) == 2 * wedges
    second_moment = sum(load * load for load in loads.values())
    four_cycles_twice = sum(
        load * (load - 1) // 2
        for (first, second), load in loads.items()
        if first < second
    )
    assert four_cycles_twice % 2 == 0
    four_cycles = four_cycles_twice // 2
    assert second_moment == 2 * wedges + 8 * four_cycles
    support = len(loads)
    assert support * second_moment >= (2 * wedges) ** 2
    return wedges, support, four_cycles, second_moment


PARABOLA_Q = (396, -38)
PARABOLA_DOUBLE_MATCHING_STARTS = [
    (-806, 76), (-885, 83), (-609, 57), (-761, 71),
    (-1088, 102), (-1604, 152), (-584, 54), (-82, 6),
    (-865, 81), (-1181, 111), (-199, 17), (-1097, 103),
    (-422, 38), (-1494, 140), (-444, 40), (-950, 88),
    (-316, 28), (576, -58),
]


def parabola_certificate() -> tuple[int, int, int, int, int]:
    points = transformed_parabola_43()
    assert distance_sidon(points)
    endpoints = endpoint_map(points)
    fibres = clean_start_fibres(points)
    starts = PARABOLA_DOUBLE_MATCHING_STARTS
    assert all(start in fibres[PARABOLA_Q] for start in starts)
    source = [endpoints[start] for start in starts]
    target = [endpoints[add(start, PARABOLA_Q)] for start in starts]
    assert matching(source) and matching(target)
    return endpoint_profile(points, PARABOLA_Q, source, target)


def main() -> None:
    expected = {
        1: (1, 0, 2, 4, 1),
        2: (2, 0, 4, 8, 1),
        4: (4, 0, 8, 16, 1),
        8: (8, 0, 16, 32, 1),
        16: (16, 0, 32, 64, 1),
    }
    for length, wanted in expected.items():
        points, q_value, source, target = explicit_double_matching(length)
        actual = endpoint_profile(points, q_value, source, target)
        assert actual == wanted, (length, actual, wanted)
        print("balanced-base", length, len(points), actual)

    # A star has quadratic shift support; a four-cycle records the exact
    # multiplicity obstruction in the wedge second moment.
    assert wedge_moments([(0, index) for index in range(1, 9)]) == (28, 56, 0, 56)
    assert wedge_moments([(0, 1), (1, 2), (2, 3), (3, 0)]) == (4, 4, 1, 16)
    print("wedge moments: PASS")

    parabola = parabola_certificate()
    assert parabola == (18, 0, 5, 10, 1), parabola
    print("parabola-43 double matching", parabola)
    print("matching-block translation leverage: PASS")


if __name__ == "__main__":
    main()
