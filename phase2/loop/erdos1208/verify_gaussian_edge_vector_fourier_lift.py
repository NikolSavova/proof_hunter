#!/usr/bin/env python3
"""Exact checks for GAUSSIAN_EDGE_VECTOR_FOURIER_LIFT.md."""

from __future__ import annotations

from collections import Counter

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import (
    difference_representations,
    oriented_edge_vectors,
)
from verify_metric_scalar_pair_sum_charge import integer_parabola
from verify_radial_orthogonal_product_barrier import canonical_transversal
from verify_transverse_closure_witness import POINTS
from verify_transverse_row_source_c4 import SOURCE_POINTS


Point = tuple[int, int]
Profile = tuple[int, int, int, int, int]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def inverse_negative_dilation(vector: Point) -> Point | None:
    """Return z with -3(I+J)z=vector, if z is integral."""
    x, y = vector
    if (x + y) % 6 or (x - y) % 6:
        return None
    return -(x + y) // 6, (x - y) // 6


def endpoint_autocorrelation(points: list[Point]) -> Counter[Point]:
    return Counter(subtract(first, second) for first in points for second in points)


def convolution_coefficient(
    autocorrelation: Counter[Point],
    target: Point,
) -> int:
    return sum(
        multiplicity
        * autocorrelation.get(
            (target[0] - vector[0], target[1] - vector[1]),
            0,
        )
        for vector, multiplicity in autocorrelation.items()
    )


def profile(points: list[Point]) -> Profile:
    vectors_by_sum = oriented_edge_vectors(points)
    fibres = clean_start_fibres(points)
    difference = max(fibres, key=lambda value: len(fibres[value]))
    fibre_vectors = [vectors_by_sum[start] for start in fibres[difference]]
    all_vectors = list(vectors_by_sum.values())

    fibre_differences = difference_representations(fibre_vectors)
    all_differences = difference_representations(all_vectors)
    endpoint = endpoint_autocorrelation(points)

    gaussian = 0
    lifted = 0
    for fibre_difference, multiplicity in fibre_differences.items():
        vector = inverse_negative_dilation(fibre_difference)
        if vector is None:
            continue
        gaussian += multiplicity * all_differences.get(vector, 0)
        lifted += multiplicity * convolution_coefficient(endpoint, vector)

    k = len(points)
    h = len(fibre_vectors)
    n = len(all_vectors)
    baseline = (2 * k * k - k) * h
    excess = lifted - baseline
    twice_off_diagonal = 2 * (gaussian - n * h)
    slack = excess - twice_off_diagonal

    assert endpoint[(0, 0)] == k
    assert sum(value * value for value in endpoint.values()) == 2 * k * k - k
    assert 0 <= twice_off_diagonal <= excess
    assert slack >= 0
    return gaussian, lifted, excess, twice_off_diagonal, slack


def radial_profile(side: int) -> tuple[int, int, int, int, int, int]:
    """Finite shadow of the square-spectrum radial pseudomodel."""
    vectors = canonical_transversal(side)[::2]
    n = len(vectors)
    k = 1
    while k * (k - 1) // 2 < n:
        k += 1

    differences = difference_representations(vectors)
    formal_endpoint: Counter[Point] = Counter({(0, 0): k})
    for vector in vectors:
        formal_endpoint[vector] += 1
        formal_endpoint[(-vector[0], -vector[1])] += 1

    gaussian = 0
    lifted = 0
    for fibre_difference, multiplicity in differences.items():
        vector = inverse_negative_dilation(fibre_difference)
        if vector is None:
            continue
        gaussian += multiplicity * differences.get(vector, 0)
        lifted += multiplicity * convolution_coefficient(formal_endpoint, vector)

    baseline = sum(value * value for value in formal_endpoint.values()) * n
    excess = lifted - baseline
    twice_off_diagonal = 2 * (gaussian - n * n)
    assert excess >= twice_off_diagonal >= 0
    return n, k, gaussian, lifted, excess, twice_off_diagonal


def main() -> None:
    families: list[tuple[str, list[Point], Profile]] = [
        ("closure-30", POINTS[:30], (6_180, 24_968, 188, 180, 8)),
        ("closure-40", POINTS[:40], (18_876, 75_226, 2_546, 1_872, 674)),
        ("closure-80", POINTS[:80], (207_504, 822_960, 21_600, 16_848, 4_752)),
        ("source-45", SOURCE_POINTS, (22_238, 89_326, 1_216, 916, 300)),
        ("perpendicular-ruler-40", ruler_points(), (10_920, 44_240, 0, 0, 0)),
        ("Costas-22", transformed_costas(23), (7_854, 32_164, 0, 0, 0)),
        (
            "parabola-image-43",
            transformed_parabola_43(),
            (159_191, 634_561, 9_556, 9_556, 0),
        ),
        ("integer-parabola-50", integer_parabola(50), (93_097, 373_904, 2_654, 2_444, 210)),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    radial_expected = {
        8: (41, 10, 3_657, 12_464, 5_002, 3_952),
        12: (82, 14, 25_552, 73_240, 43_720, 37_656),
        20: (197, 21, 310_995, 758_085, 593_590, 544_372),
        30: (407, 30, 2_564_969, 5_773_828, 5_076_230, 4_798_640),
        40: (686, 38, 11_808_470, 25_553_920, 23_622_144, 22_675_748),
    }
    for side, expected in radial_expected.items():
        actual = radial_profile(side)
        assert actual == expected, (side, actual, expected)
        print("radial", side, actual)

    print("Gaussian edge-vector Fourier lift: PASS")


if __name__ == "__main__":
    main()
