#!/usr/bin/env python3
"""Common-translation endpoint switching and replacement-pencil checks."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, ...]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def norm(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def profile(points: list[Point]) -> Profile:
    k = len(points)
    endpoint_edge: dict[Point, tuple[int, int]] = {}
    label: dict[Point, int] = {}
    for first, second in combinations(range(k), 2):
        pair_sum = add(points[first], points[second])
        endpoint_edge[pair_sum] = (first, second)
        label[pair_sum] = norm(subtract(points[first], points[second]))
    assert len(endpoint_edge) == k * (k - 1) // 2
    assert len(set(label.values())) == len(label)

    fibres = clean_start_fibres(points)
    common_translations: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    translations_at_start: dict[Point, list[Point]] = defaultdict(list)
    for translation, starts in fibres.items():
        for start in starts:
            translations_at_start[start].append(translation)
        for first in starts:
            for second in starts:
                if first != second:
                    common_translations[first, second].append(translation)

    total_first_wedges = 0
    total_simultaneous_wedges = 0
    total_one_role_wedges = 0
    total_weighted_one_role_wedges = 0
    total_replacement_records = 0
    total_weighted_replacement_records = 0
    maximum_codegree = 0
    maximum_replacement_core = 0
    core_count = 0
    wedge_count = 0
    scalar_wedge_cache: dict[int, int] = {}
    label_values = set(label.values())

    def scalar_wedges(first: Point, second: Point) -> int:
        source_gap = label[first] - label[second]
        if source_gap % 18:
            return 0
        target_gap = -source_gap // 18
        if target_gap not in scalar_wedge_cache:
            target_edges = [
                endpoint_edge[start]
                for start, value in label.items()
                if value - target_gap in label_values
            ]
            degrees = Counter(endpoint for edge in target_edges for endpoint in edge)
            scalar_wedge_cache[target_gap] = sum(
                degree * (degree - 1) // 2
                for degree in degrees.values()
            )
        return scalar_wedge_cache[target_gap]

    for (first, second), translations in common_translations.items():
        codegree = len(translations)
        maximum_codegree = max(maximum_codegree, codegree)
        shift = subtract(second, first)
        records: list[tuple[set[int], set[int]]] = []
        replacement_core = 0
        replacement_centres: set[tuple[int, int]] = set()

        for translation in translations:
            first_edge = set(endpoint_edge[add(first, translation)])
            second_edge = set(endpoint_edge[add(second, translation)])
            records.append((first_edge, second_edge))

            retained = first_edge & second_edge
            if len(retained) == 1:
                retained_endpoint = next(iter(retained))
                old_centre = next(iter(first_edge - {retained_endpoint}))
                new_centre = next(iter(second_edge - {retained_endpoint}))
                if subtract(points[new_centre], points[old_centre]) == shift:
                    replacement_core += 1
                    replacement_centres.add((old_centre, new_centre))

        first_wedges = 0
        second_wedges = 0
        simultaneous_wedges = 0
        for left, right in combinations(records, 2):
            first_overlap = bool(left[0] & right[0])
            second_overlap = bool(left[1] & right[1])
            first_wedges += first_overlap
            second_wedges += second_overlap
            simultaneous_wedges += first_overlap and second_overlap

        # Every simultaneous overlap is in one replacement pencil.
        assert len(replacement_centres) <= 1
        assert simultaneous_wedges == replacement_core * (replacement_core - 1) // 2
        assert replacement_core <= k - 2
        if replacement_core:
            old_centre, new_centre = next(iter(replacement_centres))
            first_source_edge = set(endpoint_edge[first])
            second_source_edge = set(endpoint_edge[second])
            assert first_source_edge.isdisjoint(second_source_edge)
            endpoint_degenerate = (
                new_centre in first_source_edge
                or old_centre in second_source_edge
            )
            assert endpoint_degenerate or first in fibres.get(shift, [])

        one_role_wedges = first_wedges + second_wedges - 2 * simultaneous_wedges
        assert 2 * k * first_wedges >= 4 * codegree * codegree - 2 * k * codegree
        assert 2 * k * second_wedges >= 4 * codegree * codegree - 2 * k * codegree
        assert one_role_wedges >= (
            4 * codegree * codegree / k
            - 2 * codegree
            - replacement_core * (replacement_core - 1)
            - 1e-9
        )

        if codegree >= k:
            if replacement_core * replacement_core >= codegree * codegree / k:
                core_count += 1
            else:
                wedge_count += 1
                assert one_role_wedges >= codegree * codegree / k - 1e-9

        total_first_wedges += first_wedges
        total_simultaneous_wedges += simultaneous_wedges
        total_one_role_wedges += one_role_wedges
        scalar_weight = scalar_wedges(first, second)
        total_weighted_one_role_wedges += one_role_wedges * scalar_weight
        total_replacement_records += replacement_core
        total_weighted_replacement_records += replacement_core * scalar_weight
        maximum_replacement_core = max(maximum_replacement_core, replacement_core)

    # Switch the same counts from ordered source pairs to unordered fibre pairs.
    intersection_size: Counter[tuple[Point, Point]] = Counter()
    endpoint_good_size: Counter[tuple[Point, Point]] = Counter()
    intersection_members: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    endpoint_good_members: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for start, translations in translations_at_start.items():
        for first_translation, second_translation in combinations(translations, 2):
            fibre_pair = tuple(sorted((first_translation, second_translation)))
            intersection_size[fibre_pair] += 1
            intersection_members[fibre_pair].append(start)
            first_target = set(endpoint_edge[add(start, first_translation)])
            second_target = set(endpoint_edge[add(start, second_translation)])
            if first_target & second_target:
                endpoint_good_size[fibre_pair] += 1
                endpoint_good_members[fibre_pair].append(start)

    switched_first = sum(
        endpoint_good_size[pair] * (size - 1)
        for pair, size in intersection_size.items()
    )
    switched_simultaneous = sum(
        endpoint_good_size[pair] * (endpoint_good_size[pair] - 1)
        for pair in intersection_size
    )
    switched_one_role = 2 * sum(
        endpoint_good_size[pair]
        * (size - endpoint_good_size[pair])
        for pair, size in intersection_size.items()
    )
    assert total_first_wedges == switched_first
    assert total_simultaneous_wedges == switched_simultaneous
    assert total_one_role_wedges == switched_one_role
    assert max(endpoint_good_size.values(), default=0) <= k - 2

    switched_weighted_one_role = 0
    for fibre_pair, members in intersection_members.items():
        good_members = endpoint_good_members[fibre_pair]
        good_set = set(good_members)
        bad_members = [member for member in members if member not in good_set]
        switched_weighted_one_role += sum(
            scalar_wedges(good, bad) + scalar_wedges(bad, good)
            for good in good_members
            for bad in bad_members
        )
    assert total_weighted_one_role_wedges == switched_weighted_one_role

    switched_replacement_records = 0
    switched_weighted_replacement_records = 0
    for translation, starts in fibres.items():
        for first in starts:
            first_target = set(endpoint_edge[add(first, translation)])
            for second in starts:
                if first == second:
                    continue
                second_target = set(endpoint_edge[add(second, translation)])
                if first_target & second_target:
                    switched_replacement_records += 1
                    switched_weighted_replacement_records += scalar_wedges(first, second)
    assert total_replacement_records == switched_replacement_records
    assert total_weighted_replacement_records == switched_weighted_replacement_records
    clean_mass = sum(map(len, fibres.values()))
    assert total_replacement_records <= 2 * (k - 2) * clean_mass

    return (
        k,
        len(endpoint_edge),
        len(fibres),
        sum(map(len, fibres.values())),
        len(common_translations),
        sum(map(len, common_translations.values())),
        total_first_wedges,
        total_simultaneous_wedges,
        total_one_role_wedges,
        maximum_codegree,
        maximum_replacement_core,
        core_count,
        wedge_count,
        max(endpoint_good_size.values(), default=0),
        total_weighted_one_role_wedges,
        total_replacement_records,
        total_weighted_replacement_records,
    )


def aligned_high_codegree_profile(points: list[Point]) -> Profile:
    """Exercise the actual scalar-aligned c(p)>=k branch on a large stress."""
    k = len(points)
    endpoint_edge: dict[Point, tuple[int, int]] = {}
    label: dict[Point, int] = {}
    for first, second in combinations(range(k), 2):
        pair_sum = add(points[first], points[second])
        endpoint_edge[pair_sum] = (first, second)
        label[pair_sum] = norm(subtract(points[first], points[second]))
    target_gaps = {
        first - second
        for first in label.values()
        for second in label.values()
    }

    fibres = clean_start_fibres(points)
    common_translations: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for translation, starts in fibres.items():
        for first in starts:
            for second in starts:
                source_gap = label[first] - label[second]
                if (
                    first != second
                    and source_gap % 18 == 0
                    and -source_gap // 18 in target_gaps
                ):
                    common_translations[first, second].append(translation)

    high_pairs = 0
    core_count = 0
    wedge_count = 0
    maximum_codegree = 0
    maximum_replacement_core = 0
    total_one_role_wedges = 0
    core_scalar_mass = 0
    core_weighted_replacement_records = 0
    wedge_scalar_mass = 0
    mixed_wedge_mass = 0
    scalar_wedge_cache: dict[int, int] = {}
    label_values = set(label.values())
    for (first, second), translations in common_translations.items():
        codegree = len(translations)
        maximum_codegree = max(maximum_codegree, codegree)
        if codegree < k:
            continue
        high_pairs += 1
        shift = subtract(second, first)
        records: list[tuple[set[int], set[int]]] = []
        replacement_core = 0
        replacement_centres: set[tuple[int, int]] = set()
        for translation in translations:
            first_edge = set(endpoint_edge[add(first, translation)])
            second_edge = set(endpoint_edge[add(second, translation)])
            records.append((first_edge, second_edge))
            retained = first_edge & second_edge
            if len(retained) == 1:
                retained_endpoint = next(iter(retained))
                old_centre = next(iter(first_edge - {retained_endpoint}))
                new_centre = next(iter(second_edge - {retained_endpoint}))
                if subtract(points[new_centre], points[old_centre]) == shift:
                    replacement_core += 1
                    replacement_centres.add((old_centre, new_centre))

        first_wedges = 0
        second_wedges = 0
        simultaneous_wedges = 0
        for left, right in combinations(records, 2):
            first_overlap = bool(left[0] & right[0])
            second_overlap = bool(left[1] & right[1])
            first_wedges += first_overlap
            second_wedges += second_overlap
            simultaneous_wedges += first_overlap and second_overlap
        assert len(replacement_centres) <= 1
        assert simultaneous_wedges == replacement_core * (replacement_core - 1) // 2
        if replacement_core:
            old_centre, new_centre = next(iter(replacement_centres))
            first_source_edge = set(endpoint_edge[first])
            second_source_edge = set(endpoint_edge[second])
            assert first_source_edge.isdisjoint(second_source_edge)
            endpoint_degenerate = (
                new_centre in first_source_edge
                or old_centre in second_source_edge
            )
            assert endpoint_degenerate or first in fibres.get(shift, [])
        one_role_wedges = first_wedges + second_wedges - 2 * simultaneous_wedges
        total_one_role_wedges += one_role_wedges
        maximum_replacement_core = max(maximum_replacement_core, replacement_core)
        source_gap = label[first] - label[second]
        assert source_gap % 18 == 0
        target_gap = -source_gap // 18
        if target_gap not in scalar_wedge_cache:
            target_edges = [
                endpoint_edge[start]
                for start, value in label.items()
                if value - target_gap in label_values
            ]
            degrees = Counter(endpoint for edge in target_edges for endpoint in edge)
            scalar_wedge_cache[target_gap] = sum(
                degree * (degree - 1) // 2
                for degree in degrees.values()
            )
        scalar_wedges = scalar_wedge_cache[target_gap]
        if replacement_core * replacement_core >= codegree * codegree / k:
            core_count += 1
            core_scalar_mass += codegree * scalar_wedges
            core_weighted_replacement_records += replacement_core * scalar_wedges
            assert codegree * scalar_wedges <= (
                k ** 0.5 * replacement_core * scalar_wedges + 1e-9
            )
        else:
            wedge_count += 1
            assert one_role_wedges >= codegree * codegree / k - 1e-9
            wedge_scalar_mass += codegree * scalar_wedges
            mixed_wedge_mass += one_role_wedges * scalar_wedges

    return (
        k,
        len(common_translations),
        high_pairs,
        core_count,
        wedge_count,
        maximum_codegree,
        maximum_replacement_core,
        total_one_role_wedges,
        core_scalar_mass,
        wedge_scalar_mass,
        mixed_wedge_mass,
        core_weighted_replacement_records,
    )


def main() -> None:
    families = [
        ("closure-20", POINTS[:20]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-19", transformed_parabola_43()[:19]),
        ("ruler-20", ruler_points()[:20]),
    ]
    expected: dict[str, Profile] = {
        "closure-20": (20, 190, 312, 648, 938, 1072, 137, 136, 2,
                       4, 4, 0, 0, 2, 0, 240, 932),
        "Costas-22": (22, 231, 462, 9342, 44036, 197676, 166055, 77478,
                      177154, 20, 14, 0, 0, 8, 35482, 38028, 8114),
        "parabola-19": (19, 171, 340, 2160, 9650, 13876, 3157, 2396,
                        1522, 7, 6, 0, 0, 4, 0, 2648, 0),
        "ruler-20": (20, 190, 376, 2430, 10644, 15492, 3303, 2368,
                     1870, 11, 6, 0, 0, 4, 1, 2816, 0),
    }
    for name, points in families:
        actual = profile(points)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)

    high = aligned_high_codegree_profile(transformed_parabola_43())
    assert high == (
        43, 39260, 7972, 4192, 3780, 86, 26, 2053352,
        41306, 36380, 193521, 10798,
    )
    print("parabola-43 aligned high-codegree", high)
    print("metric scalar weighted common-translation dichotomy: PASS")


if __name__ == "__main__":
    main()
