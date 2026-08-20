#!/usr/bin/env python3
"""Checks for PARABOLIC_ENDPOINT_PRODUCT_SINGER_AMBIENT_SHARPNESS.md."""

from __future__ import annotations

from itertools import combinations, product


Point = tuple[int, int]
MODULUS = 57
DIFFERENCE_SET = (0, 1, 6, 21, 28, 44, 46, 54)
SCALE = 20
HEIGHT = 10

# Colours 0,1,2 are S_0,S_1,S_2; colours 3,4,5 are T_0,T_1,T_2.
COLOUR = {
    0: 0,
    28: 0,
    46: 1,
    44: 1,
    6: 2,
    1: 3,
    54: 4,
    21: 5,
}


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def squared_norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def verify_perfect_difference_set():
    representations = {
        (second - first) % MODULUS: (first, second)
        for first in DIFFERENCE_SET
        for second in DIFFERENCE_SET
        if first != second
    }
    assert len(representations) == MODULUS - 1
    assert set(representations) == set(range(1, MODULUS))
    return representations


def point(value: int) -> Point:
    colour = COLOUR[value]
    row = colour if colour < 3 else HEIGHT + colour - 3
    return SCALE * value, row


def distance_sidon(points: list[Point]) -> bool:
    distances = [
        squared_norm(subtract(first, second))
        for first, second in combinations(points, 2)
    ]
    return len(distances) == len(set(distances))


def cyclic_edges(points: list[Point]):
    return [
        subtract(points[(index + 1) % 3], points[index])
        for index in range(3)
    ]


def selected_modular_records(representations):
    output = []
    for first_value, (a_zero, b_zero) in representations.items():
        for second_value, (a_one, b_one) in representations.items():
            third_value = (2 * second_value - first_value) % MODULUS
            if third_value not in representations:
                continue
            a_two, b_two = representations[third_value]
            endpoints = (a_zero, b_zero, a_one, b_one, a_two, b_two)
            if len(set(endpoints)) != 6:
                continue
            colours = tuple(COLOUR[value] for value in endpoints)
            if colours != (0, 3, 1, 4, 2, 5):
                continue
            integer_differences = (
                b_zero - a_zero,
                b_one - a_one,
                b_two - a_two,
            )
            carry = (
                integer_differences[0] + integer_differences[2]
                - 2 * integer_differences[1]
            ) // MODULUS
            output.append((endpoints, carry, integer_differences))
    return output


def endpoint_product_fibres(points_by_value):
    fibres = []
    for row in range(3):
        sources = [
            points_by_value[value]
            for value in DIFFERENCE_SET
            if COLOUR[value] == row
        ]
        targets = [
            points_by_value[value]
            for value in DIFFERENCE_SET
            if COLOUR[value] == row + 3
        ]
        current = [
            (target[0] - source[0], source, target)
            for source in sources
            for target in targets
        ]
        fibres.append(current)
    longitudinal = [record[0] for fibre in fibres for record in fibre]
    assert len(longitudinal) == len(set(longitudinal))
    return fibres


def main() -> None:
    representations = verify_perfect_difference_set()
    points_by_value = {value: point(value) for value in DIFFERENCE_SET}
    points = list(points_by_value.values())
    assert distance_sidon(points)

    records = selected_modular_records(representations)
    assert records == [
        ((0, 1, 46, 54, 6, 21), 0, (1, 8, 15))
    ]

    fibres = endpoint_product_fibres(points_by_value)
    assert tuple(map(len, fibres)) == (2, 2, 1)
    collinear_product_records = []
    for triple in product(*fibres):
        values = [record[0] for record in triple]
        if values[0] + values[2] == 2 * values[1]:
            collinear_product_records.append(triple)
    assert len(collinear_product_records) == 1
    assert len(collinear_product_records) <= min(
        len(fibres[0]) * len(fibres[1]),
        len(fibres[1]) * len(fibres[2]),
        len(fibres[2]) * len(fibres[0]),
    )

    endpoints = records[0][0]
    source = [points_by_value[endpoints[2 * index]] for index in range(3)]
    target = [points_by_value[endpoints[2 * index + 1]] for index in range(3)]
    source_edges = cyclic_edges(source)
    target_edges = cyclic_edges(target)
    source_area = determinant(source_edges[0], source_edges[1])
    target_area = determinant(target_edges[0], target_edges[1])
    assert source_area == target_area == 1_720

    displacements = [subtract(target[index], source[index]) for index in range(3)]
    assert displacements == [(20, 10), (160, 10), (300, 10)]
    slope = displacements[1][0] - displacements[0][0]
    assert slope == 140
    assert displacements[2][0] - displacements[1][0] == slope

    cross = [
        [determinant(first, second) for second in target_edges]
        for first in source_edges
    ]
    assert cross == [
        [-140, 1_580, -1_440],
        [-1_860, -140, 2_000],
        [2_000, -1_440, -560],
    ]
    assert all(value for row in cross for value in row)
    assert tuple(map(sum, cross)) == (0, 0, 0)
    assert tuple(
        sum(cross[row][column] for row in range(3))
        for column in range(3)
    ) == (0, 0, 0)

    print("Singer-57 points", points_by_value)
    print("endpoint fibre sizes", tuple(map(len, fibres)))
    print("trace-2 cross matrix", cross)
    print("parabolic endpoint-product Singer sharpness: PASS")


if __name__ == "__main__":
    main()
