#!/usr/bin/env python3
"""Exact raw-scalar audit of Golomb cores and planted metric gadgets."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import comb, isqrt

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_metric_scalar_squareclass_transverse import endpoint_map
from verify_outer_normalized_parabolic_rectangle_counterexample import (
    CORE_DILATION,
    SCALAR,
    build_points,
)


Point = tuple[int, int]


def prime_factors(value: int) -> list[int]:
    output = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            output.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        output.append(value)
    return output


def primitive_root(prime: int) -> int:
    factors = prime_factors(prime - 1)
    return next(
        candidate
        for candidate in range(2, prime)
        if all(
            pow(candidate, (prime - 1) // factor, prime) != 1
            for factor in factors
        )
    )


def ruzsa_core(prime: int) -> list[Point]:
    generator = primitive_root(prime)
    modulus = prime * (prime - 1)
    marks = sorted(
        {
            (
                index * prime
                - pow(generator, index, prime) * (prime - 1)
            )
            % modulus
            for index in range(1, prime)
        }
    )
    assert len(marks) == prime - 1
    differences = {
        (first - second) % modulus
        for first, second in permutations(marks, 2)
    }
    assert len(differences) == (prime - 1) * (prime - 2)
    return [(6 * mark, 0) for mark in marks]


def divisor_count(value: int) -> int:
    value = abs(value)
    assert value
    output = 1
    divisor = 2
    while divisor * divisor <= value:
        exponent = 0
        while value % divisor == 0:
            value //= divisor
            exponent += 1
        output *= exponent + 1
        divisor += 1
    if value > 1:
        output *= 2
    return output


def raw_profile(
    points: list[Point], core_size: int | None = None
) -> tuple[object, ...]:
    labels = pair_labels(points)
    endpoints = endpoint_map(points)
    pair_sums = list(labels)
    distances = [labels[pair_sum] for pair_sum in pair_sums]
    edge_count = len(pair_sums)
    fibres = clean_start_fibres(points)
    index = {pair_sum: position for position, pair_sum in enumerate(pair_sums)}

    membership = [0] * edge_count
    for fibre_index, starts in enumerate(fibres.values()):
        bit = 1 << fibre_index
        for start in starts:
            membership[index[start]] |= bit

    if core_size is None:
        edge_types = ["all"] * edge_count
    else:
        core = set(points[:core_size])
        edge_types = []
        for pair_sum in pair_sums:
            core_endpoints = sum(point in core for point in endpoints[pair_sum])
            edge_types.append(("RR", "CR", "CC")[core_endpoints])

    source_weight: Counter[tuple[int, str, str]] = Counter()
    source_pair_count: Counter[int] = Counter()
    query_gaps: set[int] = set()
    for first, first_distance in enumerate(distances):
        first_membership = membership[first]
        for second, second_distance in enumerate(distances):
            if first == second:
                continue
            codegree = (first_membership & membership[second]).bit_count()
            numerator = second_distance - first_distance
            if codegree == 0 or numerator % 18:
                continue
            gap = numerator // 18
            query_gaps.add(gap)
            source_weight[gap, edge_types[first], edge_types[second]] += codegree
            source_pair_count[gap] += 1

    target_weight: Counter[tuple[int, str, str]] = Counter()
    for first, first_distance in enumerate(distances):
        for second, second_distance in enumerate(distances):
            gap = first_distance - second_distance
            if gap in query_gaps:
                target_weight[gap, edge_types[first], edge_types[second]] += 1

    target_by_gap: dict[int, list[tuple[str, str, int]]] = {}
    for (gap, first_type, second_type), weight in target_weight.items():
        target_by_gap.setdefault(gap, []).append(
            (first_type, second_type, weight)
        )

    channels: Counter[tuple[str, str]] = Counter()
    for (gap, source_first, source_second), weight in source_weight.items():
        for target_first, target_second, target_count in target_by_gap.get(gap, ()):
            channels[
                source_first + source_second,
                target_first + target_second,
            ] += weight * target_count

    off_diagonal = sum(channels.values())
    total_h = sum(map(len, fibres.values()))
    scalar = SCALAR * CORE_DILATION * CORE_DILATION
    selected_source = sum(
        weight
        for (gap, _, _), weight in source_weight.items()
        if abs(gap) == abs(scalar)
    )
    selected_target = sum(
        weight
        for (gap, _, _), weight in target_weight.items()
        if abs(gap) == abs(scalar)
    )

    # In a collinear core, x^2-y^2=z has divisor-many ordered solutions.
    if all(point[1] == points[0][1] for point in points):
        for gap, count in source_pair_count.most_common(32):
            assert count <= 2 * divisor_count(18 * gap)

    return (
        len(points),
        edge_count,
        len(fibres),
        total_h,
        sum(source_weight.values()),
        max(source_weight.values(), default=0),
        max(target_weight.values(), default=0),
        len(target_weight),
        off_diagonal,
        edge_count * len(points) ** 3,
        selected_source,
        selected_target,
        tuple(sorted((key, value) for key, value in channels.items() if value)),
    )


def core_profiles() -> tuple[tuple[object, ...], ...]:
    rows = []
    for prime in (17, 31, 43, 59, 61):
        profile = raw_profile(ruzsa_core(prime))
        k, edge_count = profile[:2]
        rows.append(
            (
                prime,
                k,
                edge_count,
                profile[3],
                profile[4],
                profile[5],
                profile[6],
                profile[7],
                profile[8],
                profile[9],
                Fraction(profile[8], profile[9]),
            )
        )
    return tuple(rows)


def combined_profile() -> tuple[object, ...]:
    points, _, _, scalar = build_points()
    assert scalar == SCALAR * CORE_DILATION * CORE_DILATION
    profile = raw_profile(points, core_size=60)
    channels = dict(profile[-1])
    assert set(channels) == {("CCCC", "CCCC"), ("CCCC", "RRRR")}
    assert channels["CCCC", "CCCC"] == 172_851_320
    assert channels["CCCC", "RRRR"] == 71_680

    # Two signs, two core source pairs of codegrees 320 and 240 per sign,
    # and 64 rectangle records per sign.
    assert profile[10] == 2 * (320 + 240)
    assert profile[11] == 2 * 64
    assert channels["CCCC", "RRRR"] == 2 * (320 + 240) * 64
    assert profile[8] == 172_923_000
    assert profile[8] < profile[9]
    return profile


def square_budget_check() -> None:
    # Abstract planted components: one designated scalar channel per block.
    for sizes in ((8,), (2, 3, 5), (1, 1, 1, 12), tuple(range(1, 20))):
        total = sum(sizes)
        raw_records = sum(comb(size, 2) for size in sizes)
        assert raw_records <= total * total // 2


def main() -> None:
    square_budget_check()
    cores = core_profiles()
    expected_cores = (
        (17, 16, 120, 3_888, 62_740, 35, 7, 532, 11_302, 491_520, Fraction(5651, 245760)),
        (31, 30, 435, 82_746, 8_150_624, 604, 16, 6_068, 2_669_740, 11_745_000, Fraction(4603, 20250)),
        (43, 42, 861, 336_114, 68_512_724, 1_858, 22, 23_922, 24_551_018, 63_789_768, Fraction(12275509, 31894884)),
        (59, 58, 1_653, 1_251_486, 495_536_308, 4_691, 29, 85_896, 195_524_996, 322_520_136, Fraction(48881249, 80630034)),
        (61, 60, 1_770, 1_322_406, 514_820_252, 3_951, 26, 99_720, 172_851_320, 382_320_000, Fraction(4321283, 9558000)),
    )
    assert cores == expected_cores, (cores, expected_cores)
    combined = combined_profile()
    print("Ruzsa raw-scalar profiles", cores)
    print("core plus rectangle raw profile", combined[:-1])
    print("raw scalar Golomb planting square budget: PASS")


if __name__ == "__main__":
    main()
