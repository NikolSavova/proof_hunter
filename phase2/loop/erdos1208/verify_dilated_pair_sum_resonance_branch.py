#!/usr/bin/env python3
"""Exact checks for the cubic dilated-support resonance branch."""

from __future__ import annotations

from collections import Counter

from analyze_affine_costas_energy import is_distance_sidon, welch
from verify_determinant_prime_costas_resonance import (
    ROWS,
    apply,
    gram,
    resonance_image,
)
from verify_dilated_pair_sum_heavy_fibre_barrier import (
    dilated_pair_sum_support,
)
from verify_orthogonal_energy_product_ruler_barrier import erdos_turan


Point = tuple[int, int]


EXPECTED = {
    11: (10, 6, 1_956, 542, 4),
    13: (12, 10, 3_482, 912, 4),
    17: (16, 12, 8_478, 2_108, 6),
    19: (18, 12, 11_966, 2_991, 6),
    23: (22, 14, 22_008, 5_407, 6),
    29: (28, 24, 45_086, 11_107, 4),
    31: (30, 20, 54_052, 13_825, 4),
    37: (36, 28, 94_064, 23_711, 4),
    41: (40, 36, 129_306, 32_417, 4),
    43: (42, 30, 149_488, 37_528, 4),
}


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def linear_l(point: Point) -> Point:
    return point[0] - point[1], point[0] + point[1]


def difference_representations(points: list[Point]) -> Counter[Point]:
    return Counter(subtract(left, right) for left in points for right in points)


def physical_output_profile(points: list[Point]) -> Counter[Point]:
    output: Counter[Point] = Counter()
    for first in points:
        for second in points:
            pair_sum = add(first, second)
            for third in points:
                output[subtract(pair_sum, linear_l(third))] += 1
    return output


def verify_row(prime: int) -> tuple[int, int, int, int, int]:
    matrix, _ = ROWS[prime]
    base = welch(prime)
    physical = [apply(matrix, point) for point in base]
    assert is_distance_sidon(physical)

    representations = difference_representations(base)
    zero = (0, 0)
    k = len(base)
    assert representations[zero] == k
    assert all(
        count == 1
        for difference, count in representations.items()
        if difference != zero
    )

    quadratic = gram(matrix)
    resonant_nonzero: list[Point] = []
    predicted_energy = 0
    for difference, difference_count in representations.items():
        rotated = resonance_image(prime, quadratic, difference)
        if rotated is None:
            continue
        if difference != zero:
            resonant_nonzero.append(difference)
        target = add(difference, rotated)
        inner = sum(
            count * representations.get(subtract(target, value), 0)
            for value, count in representations.items()
        )
        predicted_energy += difference_count * inner

    h = len(resonant_nonzero)
    assert h <= 4 * prime - 1
    theorem_energy_bound = (
        2 * k**3 - k**2 + h * (k**2 + k - 1)
    )
    assert predicted_energy <= theorem_energy_bound

    output = physical_output_profile(physical)
    actual_energy = sum(count * count for count in output.values())
    assert actual_energy == predicted_energy
    assert len(output) == len(dilated_pair_sum_support(physical))
    assert len(output) * actual_energy >= k**6
    assert 7 * len(output) >= k**3

    return k, h, actual_energy, len(output), max(output.values())


def verify_line_branch() -> None:
    for prime, side, translation, direction in [
        (11, 8, (7, -3), (1, 0)),
        (13, 12, (-5, 9), (2, 3)),
        (23, 20, (11, 4), (-3, 5)),
    ]:
        ruler = erdos_turan(prime, side)
        points = [
            (
                translation[0] + mark * direction[0],
                translation[1] + mark * direction[1],
            )
            for mark in ruler
        ]
        expected = side * side * (side + 1) // 2
        assert len(dilated_pair_sum_support(points)) == expected


def main() -> None:
    verify_line_branch()
    print("line-covered support branch: PASS")
    for prime in ROWS:
        actual = verify_row(prime)
        assert actual == EXPECTED[prime], (prime, actual, EXPECTED[prime])
        print(prime, "resonance-support profile", actual)
    print("dilated pair-sum resonance branch: PASS")


if __name__ == "__main__":
    main()
