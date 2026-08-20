#!/usr/bin/env python3
"""Exact checks for EQUAL_CENTROID_NINE_ANCHOR_SYMMETRY_AUDIT.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import side_length
from verify_ambient_third_energy_centroid_gate import unordered_triple_fibres
from verify_orthogonal_energy_product_ruler_barrier import squared_distance_sidon
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Triple = tuple[int, int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def distance(points: list[Point], first: int, second: int) -> int:
    return norm(subtract(points[first], points[second]))


def inertia(points: list[Point], triple: Triple) -> int:
    return sum(distance(points, i, j) for i, j in combinations(triple, 2))


def opposite_edge(triple: Triple, omitted: int) -> tuple[int, int]:
    output = tuple(triple[index] for index in range(3) if index != omitted)
    assert len(output) == 2
    return output  # type: ignore[return-value]


def identity_checks(points: list[Point], first: Triple, second: Triple) -> None:
    assert set(first).isdisjoint(second)
    first_sum = tuple(sum(points[i][axis] for i in first) for axis in (0, 1))
    second_sum = tuple(sum(points[i][axis] for i in second) for axis in (0, 1))
    assert first_sum == second_sum

    first_inertia = inertia(points, first)
    second_inertia = inertia(points, second)
    cross_total = sum(distance(points, i, j) for i in first for j in second)
    assert cross_total == first_inertia + second_inertia

    for first_index, first_vertex in enumerate(first):
        source = opposite_edge(first, first_index)
        source_sum = add(points[source[0]], points[source[1]])
        source_length = distance(points, *source)
        row_sum = 0
        for second_index, second_vertex in enumerate(second):
            target = opposite_edge(second, second_index)
            target_sum = add(points[target[0]], points[target[1]])
            q_value = subtract(points[first_vertex], points[second_vertex])
            assert add(source_sum, q_value) == target_sum
            row_sum += distance(points, first_vertex, second_vertex)
        assert 3 * (source_length + row_sum) == 2 * first_inertia + second_inertia

    for second_index, second_vertex in enumerate(second):
        target = opposite_edge(second, second_index)
        target_length = distance(points, *target)
        column_sum = sum(distance(points, i, second_vertex) for i in first)
        assert 3 * (target_length + column_sum) == first_inertia + 2 * second_inertia


def charge_profile(points: list[Point], coefficient: int = 18) -> tuple[int, ...]:
    assert squared_distance_sidon(points)
    loads: Counter[int] = Counter()
    collisions = 0
    for members in unordered_triple_fibres(points).values():
        for first, second in combinations(members, 2):
            assert set(first).isdisjoint(second)
            collisions += 1
            identity_checks(points, first, second)
            for source_triple, target_triple in ((first, second), (second, first)):
                for source_index in range(3):
                    source = opposite_edge(source_triple, source_index)
                    source_length = distance(points, *source)
                    for target_index in range(3):
                        target = opposite_edge(target_triple, target_index)
                        target_length = distance(points, *target)
                        loads[source_length + coefficient * target_length] += 1

    mass = sum(loads.values())
    assert mass == 18 * collisions
    energy = sum(load * load for load in loads.values())
    return (
        len(points),
        side_length(points),
        collisions,
        mass,
        len(loads),
        energy,
        max(loads.values(), default=0),
    )


def planted_points() -> list[Point]:
    # Three pairs (a,b) with a+18b=170.  The controlled edge labels are
    # 4*S^2*a and 4*S^2*b, with S=100.
    return [
        (0, 0),
        (-930, -2204),
        (87630487, 52297669),
        (87630087, 52297269),
        (87630752, 52298871),
        (87630752, 52298271),
        (65128296, 52450853),
        (65127496, 52449253),
        (65128461, 52451355),
        (65128261, 52450955),
        (37542950, 84626453),
        (37541550, 84625053),
        (37542715, 84627055),
        (37542715, 84626655),
    ]


def planted_check() -> tuple[int, ...]:
    points = planted_points()
    profile = charge_profile(points)
    assert profile == (14, 87_631_682, 3, 54, 52, 60, 3)

    fibres = [members for members in unordered_triple_fibres(points).values() if len(members) > 1]
    expected = [
        [(0, 2, 3), (1, 4, 5)],
        [(0, 6, 7), (1, 8, 9)],
        [(0, 10, 11), (1, 12, 13)],
    ]
    assert fibres == expected

    planted_charge = 4 * 100 * 100 * 170
    loads: Counter[int] = Counter()
    for first, second in (members for members in fibres):
        source = opposite_edge(first, 0)
        target = opposite_edge(second, 0)
        loads[distance(points, *source) + 18 * distance(points, *target)] += 1
    assert loads == Counter({planted_charge: 3})
    return profile


def main() -> None:
    ordinary = [
        ("closure-40", POINTS[:40], (40, 223, 690, 12_420, 12_028, 13_244, 3)),
        ("closure-80", POINTS[:80], (80, 719, 7_563, 136_134, 130_247, 148_548, 4)),
        ("closure-120", POINTS[:120], (120, 1_514, 34_580, 622_440, 591_192, 688_774, 5)),
        ("Costas-22", transformed_costas(23), (22, 131, 519, 9_342, 9_113, 9_812, 3)),
        (
            "parabola-image-127",
            transform(parabola(127)),
            (127, 20_831, 1_000_165, 18_002_970, 17_771_450, 18_474_494, 5),
        ),
    ]
    for name, points, expected in ordinary:
        actual = charge_profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual, "energy/mass", actual[5] / actual[3])

    planted = planted_check()
    print("planted-14", planted, "energy/mass", planted[5] / planted[3])
    print("equal-centroid nine-anchor symmetry audit: PASS")


if __name__ == "__main__":
    main()
