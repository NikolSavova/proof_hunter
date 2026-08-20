#!/usr/bin/env python3
"""High-codegree completion by replacement records and one-role wedges."""

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


def tables(points: list[Point]) -> tuple[
    dict[Point, tuple[int, int]],
    dict[Point, int],
    dict[Point, tuple[int, int]],
]:
    edge_at_sum: dict[Point, tuple[int, int]] = {}
    label: dict[Point, int] = {}
    for first, second in combinations(range(len(points)), 2):
        pair_sum = add(points[first], points[second])
        edge_at_sum[pair_sum] = (first, second)
        label[pair_sum] = norm(subtract(points[first], points[second]))
    assert len(edge_at_sum) == len(points) * (len(points) - 1) // 2
    assert len(set(label.values())) == len(label)
    anchor = {
        subtract(points[head], points[tail]): (head, tail)
        for head in range(len(points))
        for tail in range(len(points))
        if head != tail
    }
    assert len(anchor) == len(points) * (len(points) - 1)
    return edge_at_sum, label, anchor


def pair_charge(
    points: list[Point],
    edge_at_sum: dict[Point, tuple[int, int]],
    anchor: dict[Point, tuple[int, int]],
    first: Point,
    second: Point,
    translations: list[Point],
) -> tuple[int, ...]:
    k = len(points)
    codegree = len(translations)
    records: list[tuple[set[int], set[int]]] = []
    replacements: list[Point] = []
    for translation in translations:
        first_edge = set(edge_at_sum[add(first, translation)])
        second_edge = set(edge_at_sum[add(second, translation)])
        records.append((first_edge, second_edge))
        if first_edge & second_edge:
            replacements.append(translation)

    replacement_count = len(replacements)
    first_wedges = 0
    second_wedges = 0
    simultaneous_wedges = 0
    for left, right in combinations(records, 2):
        first_overlap = bool(left[0] & right[0])
        second_overlap = bool(left[1] & right[1])
        first_wedges += first_overlap
        second_wedges += second_overlap
        simultaneous_wedges += first_overlap and second_overlap
    assert simultaneous_wedges == replacement_count * (replacement_count - 1) // 2
    one_role_wedges = first_wedges + second_wedges - 2 * simultaneous_wedges

    replacement_outdegree = Counter(anchor[q][0] for q in replacements)
    replacement_indegree = Counter(anchor[q][1] for q in replacements)
    assert max(replacement_outdegree.values(), default=0) <= 2
    assert max(replacement_indegree.values(), default=0) <= 2

    full_outdegree = Counter(anchor[q][0] for q in translations)
    full_indegree = Counter(anchor[q][1] for q in translations)
    nonreplacement_out_wedges = sum(
        degree * (degree - 1) // 2
        for degree in full_outdegree.values()
    ) - sum(
        degree * (degree - 1) // 2
        for degree in replacement_outdegree.values()
    )
    nonreplacement_in_wedges = sum(
        degree * (degree - 1) // 2
        for degree in full_indegree.values()
    ) - sum(
        degree * (degree - 1) // 2
        for degree in replacement_indegree.values()
    )
    assert 2 * k * nonreplacement_out_wedges >= (
        codegree * (codegree - k) - k * replacement_count
    )
    assert 2 * k * nonreplacement_in_wedges >= (
        codegree * (codegree - k) - k * replacement_count
    )

    # Star-constrained endpoint energy.  Each target role contains the
    # replacement_count-edge star supplied by the rigid pencil.
    if k * replacement_count <= 2 * codegree:
        assert k * one_role_wedges >= (
            4 * codegree * codegree
            - 2 * k * codegree
            - k * replacement_count * (replacement_count - 1)
        )
    else:
        remaining_degree = 2 * codegree - replacement_count
        assert (k - 1) * one_role_wedges >= (
            remaining_degree * remaining_degree
            - (k - 1) * remaining_degree
        )

    if codegree >= k:
        assert one_role_wedges >= codegree - replacement_count
        assert codegree <= replacement_count + one_role_wedges

    return (
        codegree,
        replacement_count,
        one_role_wedges,
        nonreplacement_out_wedges,
        nonreplacement_in_wedges,
    )


def moderate_profile(points: list[Point]) -> Profile:
    edge_at_sum, _, anchor = tables(points)
    common: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for translation, starts in clean_start_fibres(points).items():
        for first in starts:
            for second in starts:
                if first != second:
                    common[first, second].append(translation)

    high_pairs = 0
    maximum_codegree = 0
    maximum_replacement = 0
    total_one_role = 0
    total_anchor_nonreplacement = 0
    for (first, second), translations in common.items():
        charge = pair_charge(
            points, edge_at_sum, anchor, first, second, translations
        )
        codegree, replacement, one_role, out_wedges, in_wedges = charge
        high_pairs += codegree >= len(points)
        maximum_codegree = max(maximum_codegree, codegree)
        maximum_replacement = max(maximum_replacement, replacement)
        total_one_role += one_role
        total_anchor_nonreplacement += out_wedges + in_wedges
    return (
        len(points),
        len(common),
        high_pairs,
        maximum_codegree,
        maximum_replacement,
        total_one_role,
        total_anchor_nonreplacement,
    )


def aligned_parabola_profile() -> Profile:
    points = transformed_parabola_43()
    k = len(points)
    edge_at_sum, label, anchor = tables(points)
    target_gaps = {
        first - second
        for first in label.values()
        for second in label.values()
    }
    common: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for translation, starts in clean_start_fibres(points).items():
        for first in starts:
            for second in starts:
                if first == second:
                    continue
                source_gap = label[first] - label[second]
                if source_gap % 18 == 0 and -source_gap // 18 in target_gaps:
                    common[first, second].append(translation)

    label_values = set(label.values())
    scalar_wedge_cache: dict[int, int] = {}

    def scalar_wedges(first: Point, second: Point) -> int:
        target_gap = -(label[first] - label[second]) // 18
        if target_gap not in scalar_wedge_cache:
            target_edges = [
                edge_at_sum[start]
                for start, value in label.items()
                if value - target_gap in label_values
            ]
            degrees = Counter(endpoint for edge in target_edges for endpoint in edge)
            scalar_wedge_cache[target_gap] = sum(
                degree * (degree - 1) // 2
                for degree in degrees.values()
            )
        return scalar_wedge_cache[target_gap]

    high_pairs = 0
    maximum_codegree = 0
    maximum_replacement = 0
    minimum_completion_slack: int | None = None
    weighted_codegree = 0
    weighted_replacement = 0
    weighted_one_role = 0
    weighted_anchor_nonreplacement = 0
    for (first, second), translations in common.items():
        if len(translations) < k:
            continue
        high_pairs += 1
        charge = pair_charge(
            points, edge_at_sum, anchor, first, second, translations
        )
        codegree, replacement, one_role, out_wedges, in_wedges = charge
        completion_slack = replacement + one_role - codegree
        minimum_completion_slack = (
            completion_slack
            if minimum_completion_slack is None
            else min(minimum_completion_slack, completion_slack)
        )
        maximum_codegree = max(maximum_codegree, codegree)
        maximum_replacement = max(maximum_replacement, replacement)
        weight = scalar_wedges(first, second)
        weighted_codegree += codegree * weight
        weighted_replacement += replacement * weight
        weighted_one_role += one_role * weight
        weighted_anchor_nonreplacement += (out_wedges + in_wedges) * weight

    assert weighted_codegree <= weighted_replacement + weighted_one_role
    return (
        k,
        len(common),
        high_pairs,
        maximum_codegree,
        maximum_replacement,
        minimum_completion_slack or 0,
        weighted_codegree,
        weighted_replacement,
        weighted_one_role,
        weighted_anchor_nonreplacement,
    )


def main() -> None:
    cases = (
        ("closure-20", list(POINTS[:20])),
        ("Costas-22", transformed_costas(23)),
        ("parabola-19", transformed_parabola_43()[:19]),
        ("ruler-20", ruler_points()[:20]),
    )
    expected: dict[str, Profile] = {
        "closure-20": (20, 938, 0, 4, 4, 2, 0),
        "Costas-22": (22, 44036, 0, 20, 14, 177154, 74230),
        "parabola-19": (19, 9650, 0, 7, 6, 1522, 616),
        "ruler-20": (20, 10644, 0, 11, 6, 1870, 876),
    }
    for name, points in cases:
        actual = moderate_profile(points)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)
    aligned = aligned_parabola_profile()
    assert aligned == (
        43, 39260, 7972, 86, 26, 82,
        77686, 11578, 377808, 127488,
    )
    print("parabola-43 aligned", aligned)
    print("high-codegree replacement completion: PASS")


if __name__ == "__main__":
    main()
