#!/usr/bin/env python3
"""Exact selected-p audit of the actual-codegree normalized switch."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_high_codegree_replacement_completion import add, tables
from verify_synchronized_fixed_wedge_dyadic_golomb_counterexample import (
    SOURCE_FIRST,
    SOURCE_SECOND,
)
from verify_synchronized_global_multi_wedge_golomb_counterexample import (
    COPY_COUNT,
    build_points,
)


def profile() -> tuple[object, ...]:
    points, _, _ = build_points()
    edge_at_sum, distance_at_sum, anchor_at_difference = tables(points)
    fibres = clean_start_fibres(points)
    source_first = add(points[SOURCE_FIRST[0]], points[SOURCE_FIRST[1]])
    source_second = add(points[SOURCE_SECOND[0]], points[SOURCE_SECOND[1]])
    translations = [
        translation
        for translation, starts in fibres.items()
        if source_first in starts and source_second in starts
    ]
    codegree = len(translations)
    anchors = [anchor_at_difference[q] for q in translations]
    first_edges = [edge_at_sum[add(source_first, q)] for q in translations]
    second_edges = [edge_at_sum[add(source_second, q)] for q in translations]
    anchor_sets = [set(edge) for edge in anchors]
    first_sets = [set(edge) for edge in first_edges]
    second_sets = [set(edge) for edge in second_edges]

    base_count = 0
    transverse_records = 0
    canonical_channel_records = [0] * 15
    rich_bases = 0
    synchronized_pair_numerator = 0

    for left, right in combinations(range(codegree), 2):
        first_meets = bool(first_sets[left] & first_sets[right])
        second_meets = bool(second_sets[left] & second_sets[right])
        if first_meets == second_meets:
            continue
        base_count += 1

        if first_meets:
            good_sets, bad_sets = first_sets, second_sets
        else:
            good_sets, bad_sets = second_sets, first_sets
        good_union = sorted(good_sets[left] | good_sets[right])
        bad_union = sorted(bad_sets[left] | bad_sets[right])
        assert len(good_union) == 3
        assert len(bad_union) == 4

        a_left, b_left = anchors[left]
        a_right, b_right = anchors[right]
        transverse_for_base = 0
        for third in range(codegree):
            a_third, b_third = anchors[third]
            predicates = [
                a_third == a_left,
                a_third == a_right,
                b_third == b_left,
                b_third == b_right,
                a_third == b_left,
                a_third == b_right,
                b_third == a_left,
                b_third == a_right,
            ]
            predicates.extend(
                endpoint in good_sets[third] for endpoint in good_union
            )
            predicates.extend(
                endpoint in bad_sets[third] for endpoint in bad_union
            )
            assert len(predicates) == 15
            if any(predicates):
                canonical_channel_records[predicates.index(True)] += 1
            else:
                transverse_for_base += 1
        transverse_records += transverse_for_base
        if 2 * transverse_for_base >= codegree:
            rich_bases += 1
            synchronized_pair_numerator += comb(transverse_for_base, 2)
            assert Fraction(transverse_for_base, 1) <= Fraction(
                4 * comb(transverse_for_base, 2), codegree - 2
            )

    local_records = sum(canonical_channel_records)
    assert transverse_records + local_records == base_count * codegree
    assert rich_bases == base_count

    symmetric_scalar_weight = COPY_COUNT
    direct_mass = base_count * symmetric_scalar_weight
    normalized_transverse_mass = Fraction(
        transverse_records * symmetric_scalar_weight, codegree
    )
    normalized_local_mass = Fraction(
        local_records * symmetric_scalar_weight, codegree
    )
    assert normalized_transverse_mass + normalized_local_mass == direct_mass
    assert direct_mass <= 2 * normalized_transverse_mass

    once_amplified_mass = transverse_records * symmetric_scalar_weight
    normalized_pair_mass = Fraction(
        synchronized_pair_numerator * symmetric_scalar_weight, codegree
    )
    assert once_amplified_mass <= Fraction(
        4 * codegree, codegree - 2
    ) * normalized_pair_mass

    return (
        len(points),
        codegree,
        base_count,
        transverse_records,
        local_records,
        tuple(canonical_channel_records),
        direct_mass,
        normalized_transverse_mass,
        normalized_local_mass,
        synchronized_pair_numerator,
        once_amplified_mass,
        normalized_pair_mass,
    )


def main() -> None:
    actual = profile()
    expected = (
        102,
        320,
        6_169,
        1_313_335,
        660_745,
        (
            41_275,
            42_293,
            31_897,
            33_026,
            31_515,
            35_775,
            32_009,
            31_811,
            62_088,
            67_657,
            50_894,
            46_233,
            53_395,
            54_268,
            46_609,
        ),
        37_014,
        Fraction(788_001, 32),
        Fraction(396_447, 32),
        139_373_896,
        7_880_010,
        Fraction(52_265_211, 20),
    )
    assert actual == expected, (actual, expected)
    print("actual-codegree normalized profile", actual)
    print("actual-codegree normalized three-translation switch: PASS")


if __name__ == "__main__":
    main()
