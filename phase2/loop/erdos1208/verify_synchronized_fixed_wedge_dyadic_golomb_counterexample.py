#!/usr/bin/env python3
"""Exact high-codegree counterexample to the fixed-wedge dyadic gate."""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, permutations
from math import comb

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_high_codegree_replacement_completion import add, subtract, tables
from verify_metric_scalar_endpoint_rich_tail import determinant
from verify_single_fibre_replacement_transition_barrier import pair_tables


Point = tuple[int, int]
PRIME = 61
GENERATOR = 2
CORE_SCALE = 6
CORE_TRANSLATION = (10_000_000, 0)
WEDGE_ORIGIN = (0, 10_000_000)
PARTNER_CENTRES = ((130_444_132, 172_190_609), (800_242_298, 517_579_759))
SOURCE_FIRST = (2, 58)
SOURCE_SECOND = (4, 54)


def norm2(vector: Point) -> int:
    return vector[0] * vector[0] + vector[1] * vector[1]


def distance2(first: Point, second: Point) -> int:
    return norm2(subtract(first, second))


def ruzsa_ruler(prime: int = PRIME, generator: int = GENERATOR) -> list[int]:
    """Ruzsa's dense cyclic Sidon set, lifted to a Golomb ruler."""
    assert all(
        pow(generator, (prime - 1) // factor, prime) != 1
        for factor in (2, 3, 5)
    )
    modulus = prime * (prime - 1)
    marks = sorted({
        (index * prime - pow(generator, index, prime) * (prime - 1)) % modulus
        for index in range(1, prime)
    })
    assert len(marks) == prime - 1
    modular_differences = [
        (first - second) % modulus
        for first, second in permutations(marks, 2)
    ]
    assert len(modular_differences) == len(set(modular_differences))
    positive_differences = [
        second - first for first, second in combinations(marks, 2)
    ]
    assert len(positive_differences) == len(set(positive_differences))
    return marks


def build_points() -> tuple[list[Point], int]:
    marks = ruzsa_ruler()
    core = [
        (
            CORE_TRANSLATION[0] + CORE_SCALE * mark,
            CORE_TRANSLATION[1],
        )
        for mark in marks
    ]
    _, core_distances = pair_tables(core)
    unscaled_first = (marks[SOURCE_FIRST[1]] - marks[SOURCE_FIRST[0]]) ** 2
    unscaled_second = (marks[SOURCE_SECOND[1]] - marks[SOURCE_SECOND[0]]) ** 2
    unscaled_gap = unscaled_first - unscaled_second
    assert unscaled_gap == 1_336_800
    source_gap = CORE_SCALE * CORE_SCALE * unscaled_gap
    assert source_gap not in core_distances
    scalar = -source_gap // 18
    assert source_gap % 18 == 0 and scalar == -2_673_600
    assert scalar % 2 == 0

    verticals = (1, 3)
    fixed_horizontal = tuple(
        (scalar + vertical * vertical + 1) // 2 for vertical in verticals
    )
    partner_horizontal = tuple(
        (scalar + vertical * vertical - 1) // 2 for vertical in verticals
    )
    assert fixed_horizontal == (-1_336_799, -1_336_795)
    assert partner_horizontal == (-1_336_800, -1_336_796)
    for fixed, partner, vertical in zip(
        fixed_horizontal, partner_horizontal, verticals
    ):
        assert fixed * fixed - partner * partner - vertical * vertical == scalar

    points = [
        *core,
        WEDGE_ORIGIN,
        *((WEDGE_ORIGIN[0] + fixed, WEDGE_ORIGIN[1]) for fixed in fixed_horizontal),
    ]
    for centre, horizontal, vertical in zip(
        PARTNER_CENTRES, partner_horizontal, verticals
    ):
        points.extend((centre, (centre[0] + horizontal, centre[1] + vertical)))
    assert len(points) == 67
    pair_tables(points)
    return points, scalar


def masks(edges: list[set[int]]) -> list[int]:
    return [
        sum(1 << index for index, other in enumerate(edges) if edge & other)
        for edge in edges
    ]


def profile() -> tuple[int, ...]:
    points, scalar = build_points()
    k = len(points)
    edge_count = comb(k, 2)
    edge_at_sum, distance_at_sum, anchor_at_difference = tables(points)
    fibres = clean_start_fibres(points)

    source_first = add(points[SOURCE_FIRST[0]], points[SOURCE_FIRST[1]])
    source_second = add(points[SOURCE_SECOND[0]], points[SOURCE_SECOND[1]])
    assert source_first == (20_022_560, 0)
    assert source_second == (20_021_684, 0)
    source_gap = distance_at_sum[source_first] - distance_at_sum[source_second]
    assert source_gap == -18 * scalar == 48_124_800

    translations = [
        translation
        for translation, starts in fibres.items()
        if source_first in starts and source_second in starts
    ]
    codegree = len(translations)
    anchor_edges = [set(anchor_at_difference[q]) for q in translations]
    first_edges = [set(edge_at_sum[add(source_first, q)]) for q in translations]
    second_edges = [set(edge_at_sum[add(source_second, q)]) for q in translations]
    anchor_masks = masks(anchor_edges)
    first_masks = masks(first_edges)
    second_masks = masks(second_edges)

    one_role = 0
    rich_bases = 0
    minimum_transverse = codegree
    maximum_transverse = 0
    synchronized_pair_mass = 0
    for left, right in combinations(range(codegree), 2):
        if bool(first_edges[left] & first_edges[right]) == bool(
            second_edges[left] & second_edges[right]
        ):
            continue
        one_role += 1
        forbidden = (
            anchor_masks[left]
            | anchor_masks[right]
            | first_masks[left]
            | first_masks[right]
            | second_masks[left]
            | second_masks[right]
        )
        transverse = codegree - forbidden.bit_count()
        minimum_transverse = min(minimum_transverse, transverse)
        maximum_transverse = max(maximum_transverse, transverse)
        if 2 * transverse >= codegree:
            rich_bases += 1
            synchronized_pair_mass += comb(transverse, 2)

    assert one_role == rich_bases
    assert codegree - minimum_transverse < 15 * k - 36
    assert codegree * codegree * rich_bases <= 16 * synchronized_pair_mass
    assert synchronized_pair_mass < 2 * codegree * codegree * rich_bases

    # Exact physical metric wedge and its unique displayed partner pair.
    origin = 60
    fixed_edges = ((origin, 61), (origin, 62))
    partner_edges = ((63, 64), (65, 66))
    fixed_shifts = []
    doubled_determinants = []
    for fixed, partner in zip(fixed_edges, partner_edges):
        fixed_vector = subtract(points[fixed[1]], points[fixed[0]])
        partner_vector = subtract(points[partner[1]], points[partner[0]])
        fixed_shifts.append(
            distance2(points[fixed[0]], points[fixed[1]])
            - distance2(points[partner[0]], points[partner[1]])
        )
        doubled_determinants.append(
            abs(2 * determinant(fixed_vector, partner_vector))
        )
    assert fixed_shifts == [scalar, scalar]
    assert min(doubled_determinants) > edge_count
    assert (
        distance2(points[origin], points[61])
        - distance2(points[origin], points[62])
        == distance2(points[63], points[64])
        - distance2(points[65], points[66])
    )

    # The core itself realizes the exact clean-mass/codegree mechanism used
    # in the asymptotic proof.
    start_masks: dict[Point, int] = defaultdict(int)
    for index, (translation, starts) in enumerate(fibres.items()):
        bit = 1 << index
        for start in starts:
            start_masks[start] |= bit
    maximum_codegree = max(
        (first & second).bit_count()
        for first, second in combinations(start_masks.values(), 2)
    )
    total_fibre_mass = sum(len(starts) for starts in fibres.values())
    fibre_second_moment = sum(len(starts) ** 2 for starts in fibres.values())
    offdiagonal_codegree_mass = fibre_second_moment - total_fibre_mass
    assert maximum_codegree == codegree

    band_start = k
    while not band_start <= codegree < 2 * band_start:
        band_start *= 2
    assert rich_bases * band_start * band_start > 20 * k**4
    assert synchronized_pair_mass > 6 * k**4

    return (
        k,
        edge_count,
        len(fibres),
        total_fibre_mass,
        fibre_second_moment,
        offdiagonal_codegree_mass,
        maximum_codegree,
        codegree,
        one_role,
        rich_bases,
        minimum_transverse,
        maximum_transverse,
        synchronized_pair_mass,
        band_start,
        scalar,
        min(doubled_determinants),
        max(doubled_determinants),
        max(max(abs(x), abs(y)) for x, y in points),
    )


def main() -> None:
    actual = profile()
    expected = (
        67,
        2_211,
        3_540,
        1_322_406,
        516_142_658,
        514_820_252,
        320,
        320,
        6_169,
        6_169,
        182,
        245,
        139_373_896,
        268,
        -2_673_600,
        2_673_598,
        8_020_770,
        800_242_298,
    )
    assert actual == expected, (actual, expected)
    print("synchronized fixed-wedge Golomb profile", actual)
    print("synchronized fixed-wedge dyadic gate: COUNTEREXAMPLE PASS")


if __name__ == "__main__":
    main()
