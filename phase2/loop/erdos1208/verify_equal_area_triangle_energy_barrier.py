#!/usr/bin/env python3
"""Exact checks for EQUAL_AREA_TRIANGLE_ENERGY_BARRIER.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations


Point = tuple[int, int]
Matrix = tuple[int, int, int, int]


def modular_parabola(prime: int) -> list[Point]:
    return [(value, value * value % prime) for value in range(prime)]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def apply(matrix: Matrix, point: Point) -> Point:
    a_value, b_value, c_value, d_value = matrix
    x_value, y_value = point
    return (
        a_value * x_value + b_value * y_value,
        c_value * x_value + d_value * y_value,
    )


def determinant(matrix: Matrix) -> int:
    a_value, b_value, c_value, d_value = matrix
    return a_value * d_value - b_value * c_value


def doubled_area(first: Point, second: Point, third: Point) -> int:
    x_one, y_one = subtract(second, first)
    x_two, y_two = subtract(third, first)
    return x_one * y_two - y_one * x_two


def squared_distance(first: Point, second: Point) -> int:
    x_value, y_value = subtract(first, second)
    return x_value * x_value + y_value * y_value


def distance_sidon(points: list[Point]) -> bool:
    values = [
        squared_distance(first, second)
        for first, second in combinations(points, 2)
    ]
    return len(values) == len(set(values))


def vector_sidon(points: list[Point]) -> bool:
    differences = [
        subtract(first, second)
        for first in points
        for second in points
        if first != second
    ]
    return len(differences) == len(set(differences))


def maximum_collinearity(points: list[Point]) -> int:
    if len(points) < 3:
        return len(points)
    maximum = 2
    for first, second in combinations(range(len(points)), 2):
        count = sum(
            doubled_area(points[first], points[second], point) == 0
            for point in points
        )
        maximum = max(maximum, count)
    return maximum


def signed_area_loads(points: list[Point]) -> Counter[int]:
    return Counter(
        doubled_area(points[first], points[second], points[third])
        for first, second, third in permutations(range(len(points)), 3)
    )


def geometric_area_profile(
    points: list[Point],
) -> tuple[int, int, int, tuple[int, int, int, int]]:
    """Return support, max load, ordered energy, and overlap-class counts.

    The last tuple counts ordered pairs of geometric (unordered) triangles
    with intersection sizes zero, one, two, and three.  Multiplication by 18
    converts every entry to equal-signed-area ordered-triangle pairs.
    """

    buckets: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for triangle in combinations(range(len(points)), 3):
        area = abs(doubled_area(*(points[index] for index in triangle)))
        assert area != 0
        buckets[area].append(triangle)

    intersection_totals = [0, 0, 0, 0]
    for triangles in buckets.values():
        number = len(triangles)
        vertex_degrees: Counter[int] = Counter()
        pair_degrees: Counter[tuple[int, int]] = Counter()
        for triangle in triangles:
            vertex_degrees.update(triangle)
            pair_degrees.update(combinations(triangle, 2))

        intersection_three = number
        intersection_two = (
            sum(degree * degree for degree in pair_degrees.values())
            - 3 * number
        )
        intersection_one = (
            sum(degree * degree for degree in vertex_degrees.values())
            - 3 * number
            - 2 * intersection_two
        )
        intersection_zero = (
            number * number
            - intersection_three
            - intersection_two
            - intersection_one
        )
        assert min(
            intersection_zero,
            intersection_one,
            intersection_two,
            intersection_three,
        ) >= 0
        for index, value in enumerate(
            (
                intersection_zero,
                intersection_one,
                intersection_two,
                intersection_three,
            )
        ):
            intersection_totals[index] += value

    energy = 18 * sum(
        len(triangles) * len(triangles) for triangles in buckets.values()
    )
    ordered_mass = len(points) * (len(points) - 1) * (len(points) - 2)
    assert energy * (2 * len(buckets)) >= ordered_mass * ordered_mass
    return (
        len(buckets),
        max(map(len, buckets.values()), default=0),
        energy,
        tuple(intersection_totals),
    )


def verify_single_copy() -> None:
    prime = 43
    raw = modular_parabola(prime)
    assert vector_sidon(raw)
    assert maximum_collinearity(raw) == 2

    shear = 28
    points = [(x_value + shear * y_value, y_value) for x_value, y_value in raw]
    assert distance_sidon(points)
    assert maximum_collinearity(points) == 2
    assert max(max(x_value, y_value) for x_value, y_value in points) == 1_175

    raw_loads = signed_area_loads(raw)
    transformed_loads = signed_area_loads(points)
    assert raw_loads == transformed_loads
    assert 0 not in transformed_loads

    profile = geometric_area_profile(points)
    expected = (
        1_024,
        79,
        5_877_918,
        (252_130, 55_998, 6_082, 12_341),
    )
    assert profile == expected, (profile, expected)
    disjoint_energy = 18 * profile[3][0]
    assert disjoint_energy == 4_538_340
    assert sum(transformed_loads.values()) == prime * (prime - 1) * (prime - 2)
    assert sum(load * load for load in transformed_loads.values()) == profile[2]
    print("single-copy p=43", profile, "disjoint", disjoint_energy)


def verify_two_copy() -> None:
    prime = 11
    raw = modular_parabola(prime)
    first_matrix = (339, -652, 13, -25)
    second_matrix = (-17, 312, -3, 55)
    translation = (-17, -62)
    assert determinant(first_matrix) == determinant(second_matrix) == 1

    first_copy = [apply(first_matrix, point) for point in raw]
    second_copy = [
        (
            apply(second_matrix, point)[0] + translation[0],
            apply(second_matrix, point)[1] + translation[1],
        )
        for point in raw
    ]
    points = first_copy + second_copy
    assert len(points) == len(set(points)) == 2 * prime
    assert distance_sidon(points)
    assert maximum_collinearity(points) == 2

    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    side = max(max(x_values) - min(x_values), max(y_values) - min(y_values))
    assert side == 7_591

    raw_loads = signed_area_loads(raw)
    first_loads = signed_area_loads(first_copy)
    second_loads = signed_area_loads(second_copy)
    assert raw_loads == first_loads == second_loads
    cross_energy = sum(
        first_loads[area] * second_loads[area] for area in first_loads
    )
    assert cross_energy == 17_226

    first_profile = geometric_area_profile(first_copy)
    union_profile = geometric_area_profile(points)
    assert first_profile == (43, 11, 17_226, (324, 280, 188, 165))
    assert union_profile == (
        1_250,
        22,
        90_792,
        (2_566, 560, 378, 1_540),
    )
    union_disjoint_energy = 18 * union_profile[3][0]
    union_loads = signed_area_loads(points)
    assert sum(load * load for load in union_loads.values()) == union_profile[2]
    assert union_disjoint_energy == 46_188
    assert union_disjoint_energy >= 2 * cross_energy
    print(
        "two-copy p=11",
        union_profile,
        "disjoint",
        union_disjoint_energy,
        "cross",
        2 * cross_energy,
    )


def main() -> None:
    verify_single_copy()
    verify_two_copy()
    print("equal-area triangle energy barrier: PASS")


if __name__ == "__main__":
    main()
