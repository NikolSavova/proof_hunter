#!/usr/bin/env python3
"""Exact checks for GAUSSIAN_EDGE_VECTOR_CHARGE.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points, side_length
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_metric_scalar_pair_sum_charge import integer_parabola
from verify_radial_orthogonal_product_barrier import canonical_transversal
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]
Profile = tuple[int, int, Point, int, int, int, int, int, int]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def dilation(vector: Point) -> Point:
    return 3 * (vector[0] - vector[1]), 3 * (vector[0] + vector[1])


def norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def oriented_edge_vectors(points: list[Point]) -> dict[Point, Point]:
    output: dict[Point, Point] = {}
    for first, second in combinations(points, 2):
        left, right = sorted((first, second))
        pair_sum = add(left, right)
        assert pair_sum not in output
        output[pair_sum] = subtract(left, right)
    assert len(output) == len(points) * (len(points) - 1) // 2
    assert len({norm(vector) for vector in output.values()}) == len(output)
    return output


def difference_representations(values: list[Point]) -> Counter[Point]:
    return Counter(subtract(first, second) for first in values for second in values)


def profile(points: list[Point]) -> Profile:
    vectors_by_sum = oriented_edge_vectors(points)
    fibres = clean_start_fibres(points)
    difference = max(fibres, key=lambda value: len(fibres[value]))
    first_vectors = [vectors_by_sum[start] for start in fibres[difference]]
    all_vectors = list(vectors_by_sum.values())

    loads = Counter(
        add(first, dilation(second))
        for first in first_vectors
        for second in all_vectors
    )
    mass = len(first_vectors) * len(all_vectors)
    energy = sum(load * load for load in loads.values())

    assert energy >= mass
    assert len(loads) * energy >= mass * mass
    assert len(loads) <= (14 * side_length(points) + 1) ** 2

    # Independently verify the exact difference-correlation formula on
    # moderate instances.
    if len(points) <= 43:
        first_differences = difference_representations(first_vectors)
        all_differences = difference_representations(all_vectors)
        predicted = sum(
            multiplicity
            * first_differences.get(
                tuple(-coordinate for coordinate in dilation(vector)),
                0,
            )
            for vector, multiplicity in all_differences.items()
        )
        assert predicted == energy
        assert all_differences[(0, 0)] * first_differences[(0, 0)] == mass

    # Verify the Gaussian-shell comparison Q <= max r_2 * G exactly.
    shell_loads = Counter()
    shell_sizes = Counter()
    for vector, load in loads.items():
        shell_loads[norm(vector)] += load
        shell_sizes[norm(vector)] += 1
    shell_energy = sum(load * load for load in shell_loads.values())
    maximum_shell = max(shell_sizes.values())
    assert shell_energy <= maximum_shell * energy

    return (
        len(points),
        side_length(points),
        difference,
        len(first_vectors),
        len(all_vectors),
        mass,
        len(loads),
        energy,
        max(loads.values()),
    )


def radial_profile(side: int) -> tuple[int, int, int, int, int]:
    # canonical_transversal returns consecutive antipodal pairs.
    vectors = canonical_transversal(side)[::2]
    assert len({norm(vector) for vector in vectors}) == len(vectors)
    loads = Counter(
        add(first, dilation(second))
        for first in vectors
        for second in vectors
    )
    mass = len(vectors) ** 2
    energy = sum(load * load for load in loads.values())
    assert len(loads) * energy >= mass * mass
    return len(vectors), mass, len(loads), energy, max(loads.values())


def main() -> None:
    families: list[tuple[str, list[Point], Profile]] = [
        ("closure-30", POINTS[:30],
         (30, 150, (-15, -19), 14, 435, 6_090, 6_045, 6_180, 2)),
        ("closure-40", POINTS[:40],
         (40, 223, (-12, -18), 23, 780, 17_940, 17_482, 18_876, 3)),
        ("closure-80", POINTS[:80],
         (80, 719, (-2, 0), 63, 3_160, 199_080, 194_953, 207_504, 4)),
        ("closure-120", POINTS[:120],
         (120, 1_514, (66, 14), 127, 7_140, 906_780,
          884_353, 952_740, 4)),
        ("source-45", SOURCE_POINTS,
         (45, 324, (-45, -21), 22, 990, 21_780, 21_557, 22_238, 3)),
        ("perpendicular-ruler-40", ruler_points(),
         (40, 3_202, (0, -314), 14, 780, 10_920, 10_920, 10_920, 1)),
        ("Costas-22", transformed_costas(23),
         (22, 131, (13, 21), 34, 231, 7_854, 7_854, 7_854, 1)),
        ("parabola-image-43", transformed_parabola_43(),
         (43, 2_586, (396, -38), 171, 903, 154_413,
          152_024, 159_191, 2)),
        ("integer-parabola-50", integer_parabola(50),
         (50, 2_401, (-12, -528), 75, 1_225, 91_875,
          91_264, 93_097, 2)),
        ("integer-parabola-120", integer_parabola(120),
         (120, 14_161, (-12, -1_416), 315, 7_140, 2_249_100,
          2_231_784, 2_283_940, 3)),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual, "normalized", actual[7] / actual[5])

    radial_expected = {
        8: (41, 1_681, 981, 3_657, 4),
        12: (82, 6_724, 2_364, 25_552, 8),
        20: (197, 38_809, 6_854, 310_995, 15),
        30: (407, 165_649, 15_774, 2_564_969, 33),
        40: (686, 470_596, 28_425, 11_808_470, 51),
    }
    for side, expected in radial_expected.items():
        actual = radial_profile(side)
        assert actual == expected, (side, actual, expected)
        print("radial", side, actual, "normalized", actual[3] / actual[1])

    print("Gaussian edge-vector charge: PASS")


if __name__ == "__main__":
    main()
