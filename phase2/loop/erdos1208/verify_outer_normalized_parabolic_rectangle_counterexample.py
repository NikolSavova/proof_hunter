#!/usr/bin/env python3
"""Finite shadow of the outer-normalized parabolic-rectangle barrier."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb
from random import Random

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_high_codegree_replacement_completion import add, subtract, tables
from verify_metric_scalar_endpoint_rich_tail import determinant
from verify_single_fibre_replacement_transition_barrier import pair_tables
from verify_synchronized_fixed_wedge_dyadic_golomb_counterexample import (
    CORE_SCALE,
    CORE_TRANSLATION,
    GENERATOR,
    PRIME,
    SOURCE_FIRST,
    SOURCE_SECOND,
    masks,
    ruzsa_ruler,
)
from verify_synchronized_global_multi_wedge_golomb_counterexample import SCALAR


Point = tuple[int, int]
RECTANGLE_SIDE = 8
CORE_DILATION = 1_000
LAMBDA = 10
RANDOM_SEED = 1208


def parabolic_rectangle(
    side: int, stretch: int, scalar: int
) -> tuple[list[Point], list[tuple[int, int]], list[tuple[int, int]]]:
    assert scalar % 2 == 0
    points: list[Point] = []
    row_pairs = []
    for parameter in range(1, side + 1):
        horizontal = (
            2 * (stretch * stretch - 1) * parameter * parameter
            - 2 * parameter
        )
        first = len(points)
        points.append((scalar // 2 + horizontal, 1 + 2 * parameter))
        partner = len(points)
        points.append(
            (scalar // 2 - 1 + horizontal, 2 * stretch * parameter)
        )
        row_pairs.append((first, partner))

    column_pairs = []
    for parameter in range(side + 1, 2 * side + 1):
        horizontal = (
            2 * (stretch * stretch - 1) * parameter * parameter
            - 2 * stretch * parameter
        )
        first = len(points)
        points.append((horizontal, 2 * stretch * parameter))
        partner = len(points)
        points.append((horizontal, 2 * parameter))
        column_pairs.append((first, partner))
    return points, row_pairs, column_pairs


def squared_distance(first: Point, second: Point) -> int:
    return (first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2


def symbolic_distance_injectivity(side: int) -> int:
    """Interpolation certificate for distinct distance polynomials."""
    samples = [
        parabolic_rectangle(side, stretch, scalar)[0]
        for scalar in (0, 2, 4)
        for stretch in range(5)
    ]
    keys = set()
    point_count = 4 * side
    for left, right in combinations(range(point_count), 2):
        key = tuple(
            squared_distance(points[left], points[right])
            for points in samples
        )
        assert key not in keys
        keys.add(key)
    assert len(keys) == comb(point_count, 2)
    return len(keys)


def same_support_role_table() -> tuple[tuple[int, ...], ...]:
    """One specialization separating the four roles in every support type."""
    stretch = 2
    scalar = 2

    def row(parameter: int) -> tuple[Point, Point]:
        horizontal = 2 * (stretch * stretch - 1) * parameter**2 - 2 * parameter
        return (
            (scalar // 2 + horizontal, 1 + 2 * parameter),
            (scalar // 2 - 1 + horizontal, 2 * stretch * parameter),
        )

    def column(parameter: int) -> tuple[Point, Point]:
        horizontal = (
            2 * (stretch * stretch - 1) * parameter**2
            - 2 * stretch * parameter
        )
        return ((horizontal, 2 * stretch * parameter), (horizontal, 2 * parameter))

    def four(left: tuple[Point, Point], right: tuple[Point, Point]) -> tuple[int, ...]:
        return tuple(
            squared_distance(a, b)
            for a in left
            for b in right
        )

    first_row = row(1)
    second_row = row(3)
    first_column = column(1)
    second_column = column(3)
    table = (
        four(first_row, second_row),
        four(first_column, second_column),
        four(first_row, second_column),
    )
    expected = (
        (1952, 1930, 2034, 2000),
        (1664, 1604, 1700, 1616),
        (1450, 1378, 1508, 1448),
    )
    assert table == expected
    assert all(len(set(row)) == 4 for row in table)
    return table


def build_points() -> tuple[
    list[Point], list[tuple[int, int]], list[tuple[int, int]], int
]:
    scalar = SCALAR * CORE_DILATION * CORE_DILATION
    metric, row_pairs, column_pairs = parabolic_rectangle(
        RECTANGLE_SIDE, LAMBDA, scalar
    )
    pair_tables(metric)

    marks = ruzsa_ruler(PRIME, GENERATOR)
    core = [
        (
            CORE_TRANSLATION[0] + CORE_SCALE * CORE_DILATION * mark,
            CORE_TRANSLATION[1],
        )
        for mark in marks
    ]
    random = Random(RANDOM_SEED)
    translation = (
        random.randrange(10**14, 10**15),
        random.randrange(10**14, 10**15),
    )
    offset = len(core)
    points = core + [
        (x + translation[0], y + translation[1]) for x, y in metric
    ]
    pair_tables(points)
    shifted_rows = [(offset + left, offset + right) for left, right in row_pairs]
    shifted_columns = [
        (offset + left, offset + right) for left, right in column_pairs
    ]
    return points, shifted_rows, shifted_columns, scalar


def profile() -> tuple[object, ...]:
    same_support_role_table()
    for side in (2, 4, 8, 16, 32):
        symbolic_distance_injectivity(side)

    points, row_pairs, column_pairs, scalar = build_points()
    k = len(points)
    edge_count = comb(k, 2)
    edge_at_sum, distance_at_sum, anchor_at_difference = tables(points)
    fibres = clean_start_fibres(points)

    for first_row, partner_row in row_pairs:
        for first_column, partner_column in column_pairs:
            first_edge = (first_row, first_column)
            partner_edge = (partner_row, partner_column)
            assert (
                squared_distance(points[first_edge[0]], points[first_edge[1]])
                - squared_distance(
                    points[partner_edge[0]], points[partner_edge[1]]
                )
                == scalar
            )
            assert abs(
                2
                * determinant(
                    subtract(points[first_edge[1]], points[first_edge[0]]),
                    subtract(points[partner_edge[1]], points[partner_edge[0]]),
                )
            ) > edge_count

    source_first = add(points[SOURCE_FIRST[0]], points[SOURCE_FIRST[1]])
    source_second = add(points[SOURCE_SECOND[0]], points[SOURCE_SECOND[1]])
    assert (
        distance_at_sum[source_first] - distance_at_sum[source_second]
        == -18 * scalar
    )
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
    transverse_records = 0
    synchronized_pair_numerator = 0
    minimum_transverse = codegree
    maximum_transverse = 0
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
        if 2 * transverse >= codegree:
            rich_bases += 1
            transverse_records += transverse
            synchronized_pair_numerator += comb(transverse, 2)
            minimum_transverse = min(minimum_transverse, transverse)
            maximum_transverse = max(maximum_transverse, transverse)
    assert rich_bases == one_role

    edge_at_distance = {
        distance: edge_at_sum[pair_sum]
        for pair_sum, distance in distance_at_sum.items()
    }

    def edge_vector(edge: tuple[int, int]) -> Point:
        return subtract(points[edge[1]], points[edge[0]])

    def qualified_graph(gap: int) -> tuple[int, int]:
        eligible = []
        for distance, edge in edge_at_distance.items():
            partner = edge_at_distance.get(distance - gap)
            if partner is None:
                continue
            if abs(2 * determinant(edge_vector(edge), edge_vector(partner))) > edge_count:
                eligible.append(edge)
        degrees = Counter(endpoint for edge in eligible for endpoint in edge)
        return len(eligible), sum(comb(degree, 2) for degree in degrees.values())

    forward_graph = qualified_graph(scalar)
    reverse_graph = qualified_graph(-scalar)
    assert forward_graph == (
        RECTANGLE_SIDE**2,
        RECTANGLE_SIDE**2 * (RECTANGLE_SIDE - 1),
    )
    assert reverse_graph == forward_graph

    distance_labels = set(distance_at_sum.values())
    gap_multiplicity = sum(
        distance - scalar in distance_labels for distance in distance_labels
    )
    symmetric_wedge_weight = forward_graph[1] + reverse_graph[1]
    direct_mass = one_role * symmetric_wedge_weight
    outer_normalized_mass = Fraction(
        transverse_records * symmetric_wedge_weight, codegree
    )
    return (
        k,
        edge_count,
        len(fibres),
        sum(len(starts) for starts in fibres.values()),
        codegree,
        one_role,
        rich_bases,
        minimum_transverse,
        maximum_transverse,
        transverse_records,
        synchronized_pair_numerator,
        forward_graph,
        reverse_graph,
        gap_multiplicity,
        symmetric_wedge_weight,
        direct_mass,
        outer_normalized_mass,
        edge_count * k**3,
        edge_count * k**4,
        max(max(abs(x), abs(y)) for x, y in points),
    )


def main() -> None:
    actual = profile()
    expected = (
        92,
        4_186,
        3_676,
        1_322_550,
        320,
        6_169,
        6_169,
        182,
        245,
        1_313_335,
        139_373_896,
        (64, 448),
        (64, 448),
        64,
        896,
        5_527_424,
        Fraction(3_677_338, 1),
        3_259_587_968,
        299_882_093_056,
        537_866_126_862_120,
    )
    assert actual == expected, (actual, expected)
    print("outer-normalized parabolic rectangle profile", actual)
    print("direct outer Nk^3 gate: ASYMPTOTIC COUNTEREXAMPLE SHADOW PASS")


if __name__ == "__main__":
    main()
