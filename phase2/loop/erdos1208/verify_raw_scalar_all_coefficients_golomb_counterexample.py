#!/usr/bin/env python3
"""Exact C=3 profiles for the all-coefficient dense-Golomb scalar kill."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_raw_scalar_golomb_planting_square_budget import ruzsa_core


def coefficient_profile(prime: int, coefficient: int = 3) -> tuple[object, ...]:
    points = ruzsa_core(prime)
    labels = pair_labels(points)
    pair_sums = list(labels)
    distances = [labels[pair_sum] for pair_sum in pair_sums]
    edge_count = len(distances)
    fibres = clean_start_fibres(points)
    index = {pair_sum: position for position, pair_sum in enumerate(pair_sums)}

    membership = [0] * edge_count
    for fibre_index, starts in enumerate(fibres.values()):
        bit = 1 << fibre_index
        for start in starts:
            membership[index[start]] |= bit

    source_records: list[tuple[int, int]] = []
    query_gaps: set[int] = set()
    for first, first_distance in enumerate(distances):
        first_membership = membership[first]
        for second, second_distance in enumerate(distances):
            if first == second:
                continue
            codegree = (first_membership & membership[second]).bit_count()
            numerator = second_distance - first_distance
            if codegree == 0 or numerator % coefficient:
                continue
            gap = numerator // coefficient
            query_gaps.add(gap)
            source_records.append((codegree, gap))

    target_loads: Counter[int] = Counter()
    for first_distance in distances:
        for second_distance in distances:
            gap = first_distance - second_distance
            if gap in query_gaps:
                target_loads[gap] += 1

    off_diagonal = sum(
        codegree * target_loads[gap]
        for codegree, gap in source_records
    )
    total_h = sum(map(len, fibres.values()))
    sum_h_squared = sum(len(starts) ** 2 for starts in fibres.values())
    source_off = sum(codegree for codegree, _ in source_records)
    # Scale six makes every squared label divisible by 36, hence every
    # off-diagonal source gap is divisible by C=3.
    if coefficient == 3:
        assert source_off == sum_h_squared - total_h

    k = len(points)
    target = edge_count * k**3
    return (
        prime,
        k,
        edge_count,
        len(fibres),
        total_h,
        sum_h_squared,
        source_off,
        max(target_loads.values(), default=0),
        len(target_loads),
        off_diagonal,
        target,
        Fraction(off_diagonal, target),
    )


def support_scale_check() -> None:
    # Finite version of the inert-prime obstruction for x^2+3y^2.
    bound = 10_000
    represented = {
        x * x + 3 * y * y
        for x in range(1, 101)
        for y in range(1, 101)
        if x * x + 3 * y * y <= bound
    }
    for value in represented:
        remainder = value
        prime = 2
        while prime * prime <= remainder:
            exponent = 0
            while remainder % prime == 0:
                remainder //= prime
                exponent += 1
            if prime % 3 == 2:
                assert exponent % 2 == 0
            prime += 1
        if remainder > 1 and remainder % 3 == 2:
            # The final prime has exponent one, which cannot occur.
            raise AssertionError((value, remainder))
    assert len(represented) < bound // 2


def main() -> None:
    support_scale_check()
    actual = tuple(coefficient_profile(prime) for prime in (31, 59, 83))
    expected = (
        (
            31, 30, 435, 870, 82_746, 8_233_370, 8_150_624,
            16, 47_566, 10_564_022, 11_745_000,
            Fraction(5_282_011, 5_872_500),
        ),
        (
            59, 58, 1_653, 3_306, 1_251_486, 496_787_794, 495_536_308,
            29, 635_586, 666_321_296, 322_520_136,
            Fraction(83_290_162, 40_315_017),
        ),
        (
            83, 82, 3_321, 6_642, 5_263_452, 4_373_119_600,
            4_367_856_148, 34, 2_537_728, 6_432_929_994, 1_831_093_128,
            Fraction(3_216_464_997, 915_546_564),
        ),
    )
    assert actual == expected, (actual, expected)
    print("C=3 dense-Golomb raw scalar profiles", actual)
    print("all fixed positive scalar coefficients: ASYMPTOTIC COUNTEREXAMPLE PASS")


if __name__ == "__main__":
    main()
