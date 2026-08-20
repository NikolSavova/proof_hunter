#!/usr/bin/env python3
"""Exact large-area scalar-channel barrier to target-C4 charging."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_metric_scalar_squareclass_transverse import squarefree_kernel


Point = tuple[int, int]
Row = tuple[Point, Point, Point, Point, Point, Point]

Q_VALUE = (1_000_003, 1_000_033)
ROWS: list[Row] = [
    ((-853849335408, -142500538904), (-853849325808, -142500527104),
     (68703388185, -388439442246), (-1776401049398, 103439376271),
     (387038474075, 43390319738), (387038474475, 43390320138)),
    ((127320577647, -609390922196), (127320587647, -609390910796),
     (-81386048713, 596786101373), (336028214010, -1815566934332),
     (972786421287, -200969169073), (972786421487, -200969168473)),
    ((201768136667, -85298380047), (201768147167, -85298369147),
     (-450496789126, 396762161489), (854034072963, -567357910650),
     (-521169829595, 236750313082), (-521169829295, 236750313682)),
    ((-244428175152, 311459936213), (-244428165552, 311459947813),
     (-955962392422, -979351452541), (467107051721, 1602272336600),
     (-894084829169, 610726794017), (-894084828869, 610726794717)),
    ((206029802008, -738700005204), (206029811108, -738699993504),
     (-381448397240, -649968006207), (793509010359, -827430992468),
     (-712546452604, -906124618076), (-712546452204, -906124617176)),
    ((-240866657871, -246478331105), (-240866647971, -246478320205),
     (356877058973, 330322421339), (-838609364812, -823278072616),
     (273969148391, -802696556031), (273969149091, -802696555231)),
    ((149575839355, 938313149439), (149575848255, 938313161139),
     (-128045061067, 564382005140), (427197748680, 1312245305471),
     (-725194169114, 426793305023), (-725194168514, 426793305923)),
    ((8379104855, -808688995715), (8379114655, -808688984915),
     (769240871050, -718266065344), (-752481651537, -899110915253),
     (-683530441485, -973557048689), (-683530440885, -973557047689)),
    ((529744424503, -248257955045), (529744434403, -248257944345),
     (-167279917999, -531271539457), (1226769776908, 34756640100),
     (146749133243, 235947758789), (146749133643, 235947759889)),
    ((-649339823186, 860389591825), (-649339814986, 860389603825),
     (-407649215340, -163929948344), (-891029422829, 1884710144027),
     (482678811817, -150147975793), (482678811817, -150147974593)),
    ((-732159093261, 916800868162), (-732159084161, 916800879262),
     (-432902652487, -994256611946), (-1031414524932, 2827859359403),
     (194876665491, 131385188643), (194876665691, 131385189943)),
    ((-767614925520, -953890052209), (-767614917120, -953890040609),
     (405650283633, -811123372313), (-1940879126270, -1096655720472),
     (-618191007361, -151138766643), (-618191007061, -151138765343)),
]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def squared_norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def pair_sum(first: Point, second: Point) -> Point:
    return add(first, second)


def edge_label(first: Point, second: Point) -> int:
    return squared_norm(subtract(first, second))


def endpoint_map(points: list[Point]) -> dict[Point, tuple[Point, Point]]:
    output: dict[Point, tuple[Point, Point]] = {}
    for first, second in combinations(points, 2):
        value = pair_sum(first, second)
        assert value not in output
        output[value] = (first, second)
    return output


def matching(edges: list[tuple[Point, Point]]) -> bool:
    vertices = [vertex for edge in edges for vertex in edge]
    return len(vertices) == len(set(vertices))


def main() -> None:
    anchors = [(0, 0), Q_VALUE]
    points = anchors + [point for row in ROWS for point in row]
    assert len(points) == 74
    assert len(points) == len(set(points))

    distances = [edge_label(first, second) for first, second in combinations(points, 2)]
    assert len(distances) == 2_701
    assert len(distances) == len(set(distances))
    endpoints = endpoint_map(points)
    assert len(endpoints) == 2_701

    source_edges = [(row[0], row[1]) for row in ROWS]
    clean_target_edges = [(row[2], row[3]) for row in ROWS]
    charge_target_edges = [(row[4], row[5]) for row in ROWS]
    assert matching(source_edges)
    assert matching(clean_target_edges)
    assert matching(charge_target_edges)
    role_sets = [
        {vertex for edge in edges for vertex in edge}
        for edges in (source_edges, clean_target_edges, charge_target_edges)
    ]
    assert all(
        role_sets[first].isdisjoint(role_sets[second])
        for first, second in combinations(range(3), 2)
    )

    source_sums = [pair_sum(*edge) for edge in source_edges]
    clean_target_sums = [pair_sum(*edge) for edge in clean_target_edges]
    charge_target_sums = [pair_sum(*edge) for edge in charge_target_edges]
    for source, target in zip(source_sums, clean_target_sums):
        assert target == add(source, Q_VALUE)

    fibres = clean_start_fibres(points)
    assert set(fibres[Q_VALUE]) == set(source_sums)
    assert len(fibres[Q_VALUE]) == 12

    source_labels = [edge_label(*edge) for edge in source_edges]
    target_labels = [edge_label(*edge) for edge in charge_target_edges]
    charges = [
        source + 18 * target
        for source, target in zip(source_labels, target_labels)
    ]
    assert set(charges) == {237_160_000}
    assert len(source_labels) == len(set(source_labels))
    assert len(target_labels) == len(set(target_labels))
    assert len({squarefree_kernel(value) for value in target_labels}) == 12

    # The displayed bucket is the entire charge fibre at its key.
    labels = {
        value: edge_label(*edge)
        for value, edge in endpoints.items()
    }
    records = [
        (source, target)
        for source in fibres[Q_VALUE]
        for target in endpoints
        if labels[source] + 18 * labels[target] == charges[0]
    ]
    assert set(records) == set(zip(source_sums, charge_target_sums))
    assert len(records) == 12

    edge_count = len(endpoints)
    cutoff = edge_count // len(fibres[Q_VALUE])
    assert cutoff == 225
    minimum_doubled_area = min(
        abs(2 * determinant(
            subtract(*charge_target_edges[first]),
            subtract(*charge_target_edges[second]),
        ))
        for first, second in combinations(range(12), 2)
    )
    assert minimum_doubled_area == 20_000
    assert minimum_doubled_area > cutoff

    # Both endpoint graphs are matchings.  Hence every one of the 12*11
    # ordered large-area transverse collisions evades wedges and C4s.
    source_wedges = 0
    clean_target_wedges = 0
    for edges, expected in ((source_edges, source_wedges),
                            (clean_target_edges, clean_target_wedges)):
        degree = Counter(vertex for edge in edges for vertex in edge)
        assert sum(value * (value - 1) // 2 for value in degree.values()) == expected
    assert source_wedges == clean_target_wedges == 0
    ordered_off_diagonal = len(records) * (len(records) - 1)
    assert ordered_off_diagonal == 132

    # There is no nontrivial parallelogram among the twelve source pair sums.
    pair_totals = Counter(
        add(source_sums[first], source_sums[second])
        for first, second in combinations(range(12), 2)
    )
    assert max(pair_totals.values()) == 1

    print("points, edges, h, cutoff", len(points), edge_count, len(records), cutoff)
    print("charge, off-diagonal, minimum doubled area",
          charges[0], ordered_off_diagonal, minimum_doubled_area)
    print("source wedges, clean-target wedges, source parallelograms", 0, 0, 0)
    print("metric scalar target-C4 barrier: PASS")


if __name__ == "__main__":
    main()
