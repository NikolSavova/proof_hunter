#!/usr/bin/env python3
"""Exact checks for METRIC_SCALAR_FOURIER_ENDPOINT_NO_GO.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from math import comb

from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_gaussian_edge_vector_fourier_lift import (
    convolution_coefficient,
    difference_representations,
    endpoint_autocorrelation,
    inverse_negative_dilation,
)
from verify_gaussian_edge_vector_two_arm_barrier import (
    add,
    choose_translation,
    clean_fibres,
    dense_ruler,
    norm2,
)
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_radial_orthogonal_product_barrier import canonical_transversal
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]


def squared_distance(left: Point, right: Point) -> int:
    return (left[0] - right[0]) ** 2 + (left[1] - right[1]) ** 2


def assert_distance_sidon(points: list[Point]) -> None:
    labels = [squared_distance(a, b) for a, b in combinations(points, 2)]
    assert len(labels) == len(set(labels))


def balanced_mod_three_set(size: int) -> list[Point]:
    """Small deterministic certificates for the prescribed-residue lemma."""
    assert size % 9 == 0
    residues = [(x, y) for x in range(3) for y in range(3)]
    points: list[Point] = []
    old_labels: set[int] = set()
    parameter = 0

    for residue in (residues * (size // 9)):
        while True:
            parameter += 1
            candidate = (
                3 * parameter + residue[0],
                3 * parameter * parameter + residue[1],
            )
            new_labels = [squared_distance(candidate, old) for old in points]
            if (
                len(new_labels) == len(set(new_labels))
                and not (set(new_labels) & old_labels)
            ):
                break
        old_labels.update(new_labels)
        points.append(candidate)

    assert_distance_sidon(points)
    residue_counts = Counter((x % 3, y % 3) for x, y in points)
    assert set(residue_counts.values()) == {size // 9}
    return points


def radial_negative_mode(size: int) -> tuple[int, int, int, int]:
    points = balanced_mod_three_set(size)
    labels = [squared_distance(a, b) for a, b in combinations(points, 2)]
    n = comb(size, 2)
    divisible = sum(label % 3 == 0 for label in labels)

    # At theta=1/3, 2*cos(2*pi*d/3) is 2 for 3|d and -1 otherwise.
    endpoint_shift_value = size + 3 * divisible - n
    required_nonnegative_shift = n - 3 * divisible
    assert divisible == 9 * comb(size // 9, 2)
    assert endpoint_shift_value == -(size * size) // 3
    assert required_nonnegative_shift == size * size // 3 + size

    # The complete oriented endpoint differences have multiplicity size at
    # zero and multiplicity one elsewhere, as required by endpoint positivity.
    autocorrelation = Counter(
        (a[0] - b[0], a[1] - b[1]) for a in points for b in points
    )
    assert autocorrelation[(0, 0)] == size
    assert set(value for key, value in autocorrelation.items() if key != (0, 0)) == {1}
    return size, n, divisible, endpoint_shift_value


def scalar_data(
    points: list[Point],
    starts: list[Point] | None = None,
) -> tuple[list[int], list[int], int, int, int]:
    labels_by_sum = pair_labels(points)
    if starts is None:
        fibres = clean_start_fibres(points)
        difference = max(fibres, key=lambda value: len(fibres[value]))
        starts = fibres[difference]
    first = [labels_by_sum[start] for start in starts]
    all_labels = list(labels_by_sum.values())
    loads = Counter(a + 18 * b for a in first for b in all_labels)
    mass = len(first) * len(all_labels)
    energy = sum(load * load for load in loads.values())

    # Exact coefficient/Fourier identity (1.1).
    first_difference = Counter(a - b for a in first for b in first)
    all_difference = Counter(a - b for a in all_labels for b in all_labels)
    predicted = sum(
        multiplicity * all_difference.get(-difference // 18, 0)
        for difference, multiplicity in first_difference.items()
        if difference % 18 == 0
    )
    assert predicted == energy
    return first, all_labels, energy, max(loads.values()), len(loads)


def four_label_profile(points: list[Point]) -> tuple[int, int, int, int]:
    labels = pair_labels(points)
    fibres = clean_start_fibres(points)
    q = max(fibres, key=lambda value: len(fibres[value]))
    records: dict[int, list[tuple[Point, Point]]] = defaultdict(list)
    for first in fibres[q]:
        for second in labels:
            records[labels[first] + 18 * labels[second]].append((first, second))

    mass = len(fibres[q]) * len(labels)
    energy = sum(len(bucket) ** 2 for bucket in records.values())
    three = 0
    four = 0
    for bucket in records.values():
        for first_index, first_record in enumerate(bucket):
            for second_index, second_record in enumerate(bucket):
                if first_index == second_index:
                    continue
                distinct = len({*first_record, *second_record})
                assert distinct in (3, 4)
                if distinct == 3:
                    three += 1
                else:
                    four += 1
    assert three + four == energy - mass
    assert three <= 4 * len(fibres[q]) ** 2
    return mass, energy, three, four


def scalar_square_lift(points: list[Point]) -> tuple[int, int, int, int]:
    labels = pair_labels(points)
    fibres = clean_start_fibres(points)
    q = max(fibres, key=lambda value: len(fibres[value]))
    first = [labels[start] for start in fibres[q]]
    all_labels = list(labels.values())
    h, n, c = len(first), len(all_labels), len(points)

    metric_loads = Counter(a + 18 * b for a in first for b in all_labels)
    metric_energy = sum(load * load for load in metric_loads.values())
    first_difference = Counter(a - b for a in first for b in first)

    gamma: Counter[int] = Counter({0: c})
    for label in all_labels:
        gamma[label] += 1
        gamma[-label] += 1
    convolution: Counter[int] = Counter()
    for left, left_weight in gamma.items():
        for right, right_weight in gamma.items():
            convolution[left + right] += left_weight * right_weight

    lifted = sum(
        coefficient * first_difference.get(-18 * scalar, 0)
        for scalar, coefficient in convolution.items()
    )
    excess = lifted - (c * c + 2 * n) * h
    twice_off_diagonal = 2 * (metric_energy - h * n)
    assert excess >= twice_off_diagonal >= 0
    return metric_energy, lifted, excess, twice_off_diagonal


def two_arm_instance(
    side: int,
) -> tuple[list[Point], list[Point], dict[Point, Point]]:
    marks = dense_ruler(2 * side)
    rx, ry = marks[:side], marks[side:]
    translation = choose_translation(rx, ry)
    points = [(r, 0) for r in rx] + [
        (translation[0] - r, translation[1] - r) for r in ry
    ]
    fibres, pairs, edges = clean_fibres(points)
    y_indices = set(range(side, 2 * side))
    internal_y: dict[Point, list[Point]] = defaultdict(list)
    for q, fibre in fibres.items():
        for start in fibre:
            if (
                set(pairs[start]) <= y_indices
                and set(pairs[add(start, q)]) <= y_indices
            ):
                internal_y[q].append(start)
    q = max(internal_y, key=lambda value: len(internal_y[value]))
    return points, fibres[q], edges


def gaussian_excess(
    points: list[Point],
    starts: list[Point],
    edges: dict[Point, Point],
) -> tuple[int, int, int, int]:
    fibre_vectors = [edges[start] for start in starts]
    all_vectors = list(edges.values())
    fibre_difference = difference_representations(fibre_vectors)
    all_difference = difference_representations(all_vectors)
    endpoint = endpoint_autocorrelation(points)

    gaussian = 0
    lifted = 0
    for difference, multiplicity in fibre_difference.items():
        vector = inverse_negative_dilation(difference)
        if vector is None:
            continue
        gaussian += multiplicity * all_difference.get(vector, 0)
        lifted += multiplicity * convolution_coefficient(endpoint, vector)

    k, h, n = len(points), len(starts), len(all_vectors)
    excess = lifted - (2 * k * k - k) * h
    twice_off_diagonal = 2 * (gaussian - n * h)
    assert excess >= twice_off_diagonal >= 0
    return gaussian, lifted, excess, twice_off_diagonal


def radial_pseudomodel(side: int) -> tuple[int, int, int, int]:
    vectors = canonical_transversal(side)[::2]
    labels = [norm2(vector) for vector in vectors]
    assert len(labels) == len(set(labels))
    loads = Counter(a + 18 * b for a in labels for b in labels)
    energy = sum(load * load for load in loads.values())
    return len(labels), energy, max(loads.values()), len(loads)


def main() -> None:
    negative_expected = {
        9: (9, 36, 0, -27),
        18: (18, 153, 9, -108),
        27: (27, 351, 27, -243),
        45: (45, 990, 90, -675),
        90: (90, 4005, 405, -2700),
    }
    for size, expected in negative_expected.items():
        actual = radial_negative_mode(size)
        assert actual == expected, (size, actual, expected)
        print("balanced-mod-3", actual)

    four_label_expected = {
        30: (6_090, 6_342, 0, 252),
        40: (17_940, 20_592, 4, 2_648),
    }
    for size, expected in four_label_expected.items():
        actual = four_label_profile(POINTS[:size])
        assert actual == expected, (size, actual, expected)
        print("four-label", size, actual)

    square_lift_expected = {
        20: (968, 4_020, 120, 36),
        30: (6_342, 25_540, 760, 504),
        40: (20_592, 78_682, 6_002, 5_304),
    }
    for size, expected in square_lift_expected.items():
        actual = scalar_square_lift(POINTS[:size])
        assert actual == expected, (size, actual, expected)
        print("scalar-square-lift", size, actual)

    # The genuine perpendicular-ruler stress remains nearly diagonal.
    first, labels, energy, maximum, image = scalar_data(ruler_points())
    perpendicular = (len(first), len(labels), energy, maximum, image)
    assert perpendicular == (14, 780, 10_938, 2, 10_911)
    print("perpendicular-ruler", perpendicular)

    two_arm_expected = {
        # (h, N, scalar energy, scalar max load, scalar image,
        #  Gaussian energy, Gaussian lift, Gaussian X, twice off-diagonal)
        8: (1, 120, 120, 1, 120, 120, 496, 0, 0),
        16: (7, 496, 3_472, 1, 3_472, 3_662, 14_652, 540, 380),
        32: (44, 2_016, 88_858, 2, 88_627,
             133_328, 474_340, 116_708, 89_248),
        50: (114, 4_950, 565_444, 3, 563_729,
             1_333_352, 4_173_182, 1_904_582, 1_538_104),
    }
    for side, expected in two_arm_expected.items():
        points, starts, edges = two_arm_instance(side)
        first, labels, energy, maximum, image = scalar_data(points, starts)
        gaussian = gaussian_excess(points, starts, edges)
        actual = (len(first), len(labels), energy, maximum, image, *gaussian)
        assert actual == expected, (side, actual, expected)
        print("two-arm", side, actual)

    radial_expected = {
        8: (41, 2_741, 4, 1_216),
        20: (197, 194_407, 14, 10_064),
        40: (686, 6_833_852, 37, 44_499),
        80: (2_460, 279_766_494, 111, 182_901),
    }
    for side, expected in radial_expected.items():
        actual = radial_pseudomodel(side)
        assert actual == expected, (side, actual, expected)
        print("radial-pseudomodel", side, actual)

    print("metric scalar Fourier endpoint no-go: PASS")


if __name__ == "__main__":
    main()
