#!/usr/bin/env python3
"""Metric audit of anchor-wedge closure against common-translation wedges."""

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
    edge_at_sum: dict[Point, frozenset[int]] = {}
    label: dict[Point, int] = {}
    for first, second in combinations(range(k), 2):
        pair_sum = add(points[first], points[second])
        edge_at_sum[pair_sum] = frozenset((first, second))
        label[pair_sum] = norm(subtract(points[first], points[second]))
    assert len(edge_at_sum) == k * (k - 1) // 2
    assert len(set(label.values())) == len(label)

    anchor: dict[Point, tuple[int, int]] = {}
    for head in range(k):
        for tail in range(k):
            if head != tail:
                anchor[subtract(points[head], points[tail])] = (head, tail)
    assert len(anchor) == k * (k - 1)

    fibres = {
        translation: set(starts)
        for translation, starts in clean_start_fibres(points).items()
    }
    clean_mass = sum(map(len, fibres.values()))
    translations_at_start: dict[Point, list[Point]] = defaultdict(list)
    for translation, starts in fibres.items():
        for start in starts:
            translations_at_start[start].append(translation)

    label_values = set(label.values())
    scalar_wedge_cache: dict[int, int] = {}

    def scalar_wedges(first: Point, second: Point) -> int:
        source_gap = label[first] - label[second]
        if source_gap % 18:
            return 0
        target_gap = -source_gap // 18
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

    scalar_row_mass = {
        first: sum(
            scalar_wedges(first, second) + scalar_wedges(second, first)
            for second in label
            if first != second
        )
        for first in label
    }

    intersections: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for start, translations in translations_at_start.items():
        for first, second in combinations(translations, 2):
            intersections[tuple(sorted((first, second)))].append(start)

    geometry_good = Counter()
    geometry_one_role = Counter()
    geometry_metric = Counter()
    shared_head_weighted_exception = 0
    shared_head_complementary_fibre_mass = 0
    exception_second_moment = 0
    nonhead_failed_images = 0
    nonhead_failed_metric_mass = 0

    for (first_q, second_q), starts in intersections.items():
        first_anchor = anchor[first_q]
        second_anchor = anchor[second_q]
        if first_anchor[0] == second_anchor[0]:
            geometry = "head"
        elif first_anchor[1] == second_anchor[1]:
            geometry = "tail"
        elif (
            first_anchor[0] == second_anchor[1]
            and second_anchor[0] == first_anchor[1]
        ):
            geometry = "opposite"
        elif (
            first_anchor[0] == second_anchor[1]
            or second_anchor[0] == first_anchor[1]
        ):
            geometry = "cross"
        else:
            geometry = "disjoint"

        good = [
            start
            for start in starts
            if edge_at_sum[add(start, first_q)]
            & edge_at_sum[add(start, second_q)]
        ]
        good_set = set(good)
        bad = [start for start in starts if start not in good_set]
        geometry_good[geometry] += len(good)
        geometry_one_role[geometry] += 2 * len(good) * len(bad)
        geometry_metric[geometry] += sum(
            scalar_wedges(first, second) + scalar_wedges(second, first)
            for first in good
            for second in bad
        )

        if geometry == "head":
            # The closure theorem says precisely that good starts are its
            # exceptions; the weighted identity preserves the same start.
            head = first_anchor[0]
            first_leaf = first_anchor[1]
            second_leaf = second_anchor[1]
            gap = subtract(points[second_leaf], points[first_leaf])
            assert gap == subtract(first_q, second_q)
            for start in starts:
                clean_image = add(start, second_q) in fibres.get(gap, set())
                assert clean_image == (start not in good_set)
            shared_head_weighted_exception += sum(
                scalar_row_mass[start] for start in good
            )
            shared_head_complementary_fibre_mass += (
                len(good) * len(fibres.get(gap, set()))
            )
            exception_second_moment += len(good) * (len(good) - 1)
        elif good:
            # Applying shared-head closure to arbitrary fibre pairs is false.
            # Count bad starts for which even the natural H_(q-q') image fails.
            gap = subtract(first_q, second_q)
            assert gap in anchor
            failed = [
                start
                for start in bad
                if add(start, second_q) not in fibres.get(gap, set())
            ]
            nonhead_failed_images += len(failed)
            nonhead_failed_metric_mass += sum(
                scalar_wedges(first, second) + scalar_wedges(second, first)
                for first in good
                for second in failed
            )

    # The exceptional bijection preserves the source start, hence every
    # function of that start, not just the constant function one.
    weighted_clean_mass = sum(
        scalar_row_mass[start]
        for starts in fibres.values()
        for start in starts
    )
    assert geometry_good["head"] == clean_mass
    assert geometry_good["tail"] == 0
    assert shared_head_weighted_exception == weighted_clean_mass

    # Replacement-pencil moments.  rho(p) counts translations in which the
    # two target roles meet.  Shared-head pairs inside that pencil are exactly
    # ordered pairs of anchor-closure exceptions.
    codegrees: Counter[tuple[Point, Point]] = Counter()
    replacement_translations: dict[tuple[Point, Point], list[Point]] = defaultdict(list)
    for translation, starts in fibres.items():
        for first in starts:
            first_target = edge_at_sum[add(first, translation)]
            for second in starts:
                if first == second:
                    continue
                pair = (first, second)
                codegrees[pair] += 1
                if first_target & edge_at_sum[add(second, translation)]:
                    replacement_translations[pair].append(translation)

    replacement_first_moment = sum(map(len, replacement_translations.values()))
    replacement_second_moment = sum(
        len(translations) ** 2
        for translations in replacement_translations.values()
    )
    replacement_head_wedges = 0
    rigid_codegree_second_moment = 0
    for pair, translations in replacement_translations.items():
        head_degrees = Counter(anchor[translation][0] for translation in translations)
        replacement_head_wedges += sum(
            degree * (degree - 1) // 2
            for degree in head_degrees.values()
        )
        codegree = codegrees[pair]
        replacement = len(translations)
        if replacement * replacement * k >= codegree * codegree:
            rigid_codegree_second_moment += codegree * codegree

    exceptional_limit = (k - 3) // 2
    assert replacement_head_wedges == exception_second_moment
    assert replacement_head_wedges <= (exceptional_limit - 1) * clean_mass
    assert replacement_first_moment <= 2 * (k - 2) * clean_mass
    assert replacement_second_moment <= (
        2 * k * (k + exceptional_limit - 3) * clean_mass
    )
    assert rigid_codegree_second_moment <= (
        2 * k * k * (k + exceptional_limit - 3) * clean_mass
    )

    return (
        k,
        len(edge_at_sum),
        clean_mass,
        geometry_good["head"],
        geometry_good["tail"],
        geometry_good["cross"],
        geometry_good["opposite"],
        geometry_good["disjoint"],
        geometry_one_role["head"],
        sum(geometry_one_role.values()),
        geometry_metric["head"],
        sum(geometry_metric.values()),
        shared_head_complementary_fibre_mass,
        nonhead_failed_images,
        nonhead_failed_metric_mass,
        replacement_first_moment,
        replacement_second_moment,
        replacement_head_wedges,
        rigid_codegree_second_moment,
        shared_head_weighted_exception,
    )


def full_parabola_complementary_mass() -> tuple[int, int, int]:
    """Stress the tempting but false hope that sum e*h_g is near H."""
    points = transformed_parabola_43()
    k = len(points)
    edge_at_sum = {
        add(points[first], points[second]): frozenset((first, second))
        for first, second in combinations(range(k), 2)
    }
    fibres = {
        translation: set(starts)
        for translation, starts in clean_start_fibres(points).items()
    }
    clean_mass = sum(map(len, fibres.values()))
    complementary_mass = 0
    for head in range(k):
        leaves = [leaf for leaf in range(k) if leaf != head]
        for first_leaf, second_leaf in combinations(leaves, 2):
            first_q = subtract(points[head], points[first_leaf])
            second_q = subtract(points[head], points[second_leaf])
            gap = subtract(points[second_leaf], points[first_leaf])
            intersection = fibres.get(first_q, set()) & fibres.get(second_q, set())
            exceptional = sum(
                bool(
                    edge_at_sum[add(start, first_q)]
                    & edge_at_sum[add(start, second_q)]
                )
                for start in intersection
            )
            complementary_mass += exceptional * len(fibres.get(gap, set()))
    return k, clean_mass, complementary_mass


def costas_weighted_nonhead_witness() -> tuple[object, ...]:
    """A mixed scalar record to which shared-head closure does not extend."""
    points = transformed_costas(23)
    edge_at_sum: dict[Point, frozenset[int]] = {}
    label: dict[Point, int] = {}
    for first, second in combinations(range(len(points)), 2):
        pair_sum = add(points[first], points[second])
        edge_at_sum[pair_sum] = frozenset((first, second))
        label[pair_sum] = norm(subtract(points[first], points[second]))
    anchor = {
        subtract(points[head], points[tail]): (head, tail)
        for head in range(len(points))
        for tail in range(len(points))
        if head != tail
    }
    fibres = {
        translation: set(starts)
        for translation, starts in clean_start_fibres(points).items()
    }
    label_values = set(label.values())

    def scalar_wedges(first: Point, second: Point) -> int:
        source_gap = label[first] - label[second]
        if source_gap % 18:
            return 0
        target_gap = -source_gap // 18
        target_edges = [
            edge_at_sum[start]
            for start, value in label.items()
            if value - target_gap in label_values
        ]
        degrees = Counter(endpoint for edge in target_edges for endpoint in edge)
        return sum(
            degree * (degree - 1) // 2
            for degree in degrees.values()
        )

    first_q = (-20, -27)
    second_q = (24, 37)
    gap = subtract(first_q, second_q)
    good = (-167, -153)
    bad = (-182, -156)
    assert set(anchor[first_q]).isdisjoint(anchor[second_q])
    assert good in fibres[first_q] & fibres[second_q]
    assert bad in fibres[first_q] & fibres[second_q]
    assert edge_at_sum[add(good, first_q)] & edge_at_sum[add(good, second_q)]
    assert not (
        edge_at_sum[add(bad, first_q)] & edge_at_sum[add(bad, second_q)]
    )
    assert gap in anchor
    assert add(bad, second_q) not in fibres.get(gap, set())
    weights = scalar_wedges(good, bad), scalar_wedges(bad, good)
    assert weights == (3, 4)
    return (
        first_q,
        second_q,
        gap,
        good,
        bad,
        anchor[first_q],
        anchor[second_q],
        anchor[gap],
        weights,
    )


def main() -> None:
    cases = (
        ("closure-20", list(POINTS[:20])),
        ("Costas-22", transformed_costas(23)),
        ("parabola-19", transformed_parabola_43()[:19]),
        ("ruler-20", ruler_points()[:20]),
    )
    expected: dict[str, Profile] = {
        "closure-20": (
            20, 190, 648, 648, 0, 36, 0, 204, 0, 2, 0, 0, 1086,
            0, 0, 240, 512, 120, 522, 537816,
        ),
        "Costas-22": (
            22, 231, 9342, 9342, 0, 3444, 117, 34467, 36910, 177154,
            7715, 35482, 175761, 5652, 4405, 38028, 192984, 19014,
            658914, 939954,
        ),
        "parabola-19": (
            19, 171, 2160, 2160, 0, 268, 11, 2369, 466, 1522, 0, 0,
            12606, 66, 0, 2648, 7440, 1324, 10370, 51,
        ),
        "ruler-20": (
            20, 190, 2430, 2430, 0, 364, 12, 2440, 632, 1870, 0, 1,
            14730, 80, 0, 2816, 7552, 1408, 11474, 204,
        ),
    }
    for name, points in cases:
        actual = profile(points)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)

    full_stress = full_parabola_complementary_mass()
    assert full_stress == (43, 190278, 19181793)
    print("parabola-43 complementary mass", full_stress)
    witness = costas_weighted_nonhead_witness()
    print("Costas weighted nonhead witness", witness)
    print("clean-fibre anchor-wedge metric audit: PASS")


if __name__ == "__main__":
    main()
