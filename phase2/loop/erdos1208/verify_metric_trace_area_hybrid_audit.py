#!/usr/bin/env python3
"""Exact checks for METRIC_TRACE_AREA_HYBRID_AUDIT.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from math import comb, isqrt

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import oriented_edge_vectors
from verify_metric_scalar_fourier_endpoint_no_go import two_arm_instance
from verify_metric_scalar_pair_sum_charge import integer_parabola
from verify_radial_orthogonal_product_barrier import canonical_transversal
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, int, int, int, int, int, int, int, int, int, int, int]


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1]


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def chi_minus_eight(divisor: int) -> int:
    if divisor % 2 == 0:
        return 0
    return 1 if divisor % 8 in (1, 3) else -1


def divisors(number: int) -> list[int]:
    output: list[int] = []
    for divisor in range(1, isqrt(number) + 1):
        if number % divisor:
            continue
        output.append(divisor)
        if divisor * divisor != number:
            output.append(number // divisor)
    return output


def quadratic_form_formula(limit: int = 5_000) -> None:
    representations = Counter()
    radius = isqrt(limit)
    for x in range(-radius, radius + 1):
        y_radius = isqrt(max(0, (limit - x * x) // 2))
        for y in range(-y_radius, y_radius + 1):
            value = x * x + 2 * y * y
            if 0 < value <= limit:
                representations[value] += 1

    for value in range(1, limit + 1):
        value_divisors = divisors(value)
        predicted = 2 * sum(chi_minus_eight(d) for d in value_divisors)
        assert representations[value] == predicted, (
            value,
            representations[value],
            predicted,
        )
        assert representations[value] <= 2 * len(value_divisors)


def vector_profile(first: list[Point], second: list[Point]) -> Profile:
    assert len({norm2(vector) for vector in first}) == len(first)
    assert len({norm2(vector) for vector in second}) == len(second)

    trace_loads: Counter[int] = Counter()
    area_loads: Counter[int] = Counter()
    joint_loads: Counter[tuple[int, int]] = Counter()

    for left in first:
        x = norm2(left)
        for right in second:
            y = norm2(right)
            z = dot(left, right)
            p = x - 18 * y
            trace = x + 18 * y
            area = determinant(left, right)
            discriminant = trace * trace - 72 * area * area

            assert discriminant == p * p + 72 * z * z
            assert discriminant >= 0
            assert (trace + p) // 2 == x
            assert (trace - p) // 36 == y
            assert (trace + p) % 2 == 0
            assert (trace - p) % 36 == 0

            trace_loads[trace] += 1
            area_loads[area] += 1
            joint_loads[(trace, area)] += 1

    # On every nontrivial joint cell, distinct records give distinct form
    # witnesses (p,z).  This is the finite version of the injection in the
    # proof of Theorem 3.1.
    repeated_keys = {key for key, load in joint_loads.items() if load > 1}
    witnesses: dict[tuple[int, int], set[tuple[int, int]]] = defaultdict(set)
    if repeated_keys:
        for left in first:
            x = norm2(left)
            for right in second:
                y = norm2(right)
                key = x + 18 * y, determinant(left, right)
                if key in repeated_keys:
                    witnesses[key].add((x - 18 * y, dot(left, right)))
        assert all(
            len(witnesses[key]) == joint_loads[key] for key in repeated_keys
        )

    records = len(first) * len(second)
    return (
        len(first),
        len(second),
        records,
        sum(load * load for load in trace_loads.values()),
        sum(load * load for load in area_loads.values()),
        sum(load * load for load in joint_loads.values()),
        max(trace_loads.values()),
        max(area_loads.values()),
        max(joint_loads.values()),
        len(trace_loads),
        len(area_loads),
        len(joint_loads),
    )


def endpoint_profile(points: list[Point]) -> Profile:
    vectors = oriented_edge_vectors(points)
    fibres = clean_start_fibres(points)
    q = max(fibres, key=lambda value: len(fibres[value]))
    return vector_profile(
        [vectors[start] for start in fibres[q]],
        list(vectors.values()),
    )


def main() -> None:
    quadratic_form_formula()
    print("x^2+2y^2 representation formula: PASS")

    genuine_expected: list[tuple[str, list[Point], Profile]] = [
        (
            "closure-30",
            POINTS[:30],
            (14, 435, 6_090, 6_342, 14_406, 6_090,
             2, 18, 1, 5_964, 3_782, 6_090),
        ),
        (
            "closure-120",
            POINTS[:120],
            (127, 7_140, 906_780, 1_023_788, 3_986_674, 906_782,
             6, 169, 2, 851_608, 410_705, 906_779),
        ),
        (
            "perpendicular-ruler-40",
            ruler_points(),
            (14, 780, 10_920, 10_938, 8_763_646, 10_922,
             2, 2_940, 2, 10_911, 2_609, 10_919),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (34, 231, 7_854, 8_382, 186_714, 7_856,
             3, 65, 2, 7_601, 669, 7_853),
        ),
        (
            "parabola-image-43",
            transformed_parabola_43(),
            (171, 903, 154_413, 157_133, 17_585_719, 154_469,
             3, 470, 2, 153_065, 3_645, 154_385),
        ),
        (
            "integer-parabola-50",
            integer_parabola(50),
            (75, 1_225, 91_875, 92_977, 5_283_803, 91_885,
             3, 1_463, 2, 91_331, 5_623, 91_870),
        ),
    ]

    for name, points, expected in genuine_expected:
        actual = endpoint_profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    two_arm_expected = {
        32: (44, 2_016, 88_704, 88_858, 477_273_548, 88_734,
             2, 21_824, 2, 88_627, 24_378, 88_689),
        50: (114, 4_950, 564_300, 565_444, 19_511_800_228, 564_626,
             3, 139_650, 2, 563_729, 148_844, 564_137),
    }
    for side, expected in two_arm_expected.items():
        points, starts, edges = two_arm_instance(side)
        actual = vector_profile(
            [edges[start] for start in starts],
            list(edges.values()),
        )
        assert actual == expected, (side, actual, expected)
        print("two-arm", side, actual)

    radial_expected = {
        8: (41, 41, 1_681, 2_741, 78_917, 1_695,
            4, 157, 2, 1_216, 85, 1_674),
        20: (197, 197, 38_809, 194_407, 7_433_895, 39_987,
             14, 1_083, 4, 10_064, 597, 38_235),
        40: (686, 686, 470_596, 6_833_852, 269_680_866, 487_266,
             37, 4_494, 5, 44_499, 2_587, 462_633),
    }
    for side, expected in radial_expected.items():
        vectors = canonical_transversal(side)[::2]
        actual = vector_profile(vectors, vectors)
        assert actual == expected, (side, actual, expected)
        print("radial-transversal", side, actual)

    print("metric trace-area hybrid audit: PASS")


if __name__ == "__main__":
    main()
