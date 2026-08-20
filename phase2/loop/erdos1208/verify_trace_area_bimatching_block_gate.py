#!/usr/bin/env python3
"""Exact checks for TRACE_AREA_BIMATCHING_BLOCK_GATE.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import floor, sqrt

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_adaptive_trace_area_endpoint_charge import adaptive_profile
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import add, oriented_edge_vectors
from verify_matching_block_translation_leverage import distance_sidon
from verify_metric_scalar_fourier_endpoint_no_go import two_arm_instance
from verify_metric_scalar_squareclass_transverse import endpoint_map
from verify_metric_trace_area_hybrid_audit import determinant, norm2
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Edge = tuple[Point, Point]
Record = tuple[Point, Edge, Edge]


def translate(point: Point, shift: Point) -> Point:
    return point[0] + shift[0], point[1] + shift[1]


def star_family(length: int, base: int = 10) -> tuple[
    list[Point], Point, list[Edge], list[Edge]
]:
    """The infinite genuine source-star/target-matching family."""
    assert length >= 1 and base >= 10
    q_scalar, center = 1, base
    values = [0, q_scalar, center]
    source: list[tuple[int, int]] = []
    target: list[tuple[int, int]] = []
    for index in range(length):
        d_value = base ** (2 * index + 2)
        e_value = base ** (2 * index + 3)
        f_value = q_scalar + center + d_value - e_value
        values.extend((d_value, e_value, f_value))
        source.append((center, d_value))
        target.append((e_value, f_value))

    shift = -min(values)
    points = [(value + shift, 0) for value in values]
    source_edges = [
        tuple(sorted(((left + shift, 0), (right + shift, 0))))
        for left, right in source
    ]
    target_edges = [
        tuple(sorted(((left + shift, 0), (right + shift, 0))))
        for left, right in target
    ]
    return points, (1, 0), source_edges, target_edges


def star_check(length: int) -> tuple[int, int, int, int]:
    points, q_value, source, target = star_family(length)
    assert len(points) == 3 * length + 3
    assert len(points) == len(set(points))
    assert distance_sidon(points)
    assert len(set(vertex for edge in target for vertex in edge)) == 2 * length

    source_starts = {add(*edge) for edge in source}
    target_starts = {add(*edge) for edge in target}
    assert {add(start, q_value) for start in source_starts} == target_starts
    fibres = clean_start_fibres(points)
    assert set(fibres[q_value]) == source_starts
    assert len(fibres[q_value]) == length

    center = set(source[0]).intersection(source[1]) if length > 1 else set(source[0])
    if length > 1:
        assert len(center) == 1
        assert all(center <= set(edge) for edge in source)
    # The source-star records form a clique in the role-conflict graph.
    minimum_blocks = length
    return len(points), len(fibres[q_value]), minimum_blocks, max(map(len, fibres.values()))


def role_records(points: list[Point], starts: list[Point], q_value: Point) -> list[Record]:
    endpoints = endpoint_map(points)
    records: list[Record] = []
    for start in starts:
        assert start in endpoints and add(start, q_value) in endpoints
        records.append((start, endpoints[start], endpoints[add(start, q_value)]))
    return records


def conflict_graph(records: list[Record]) -> list[set[int]]:
    adjacency = [set() for _ in records]
    for first, second in combinations(range(len(records)), 2):
        source_conflict = bool(set(records[first][1]).intersection(records[second][1]))
        target_conflict = bool(set(records[first][2]).intersection(records[second][2]))
        # This is the source-star-to-target-matching theorem and its dual.
        assert not (source_conflict and target_conflict)
        if source_conflict or target_conflict:
            adjacency[first].add(second)
            adjacency[second].add(first)
    return adjacency


def dsatur_blocks(records: list[Record]) -> tuple[list[list[Point]], int]:
    adjacency = conflict_graph(records)
    colors: dict[int, int] = {}
    while len(colors) < len(records):
        uncolored = [index for index in range(len(records)) if index not in colors]
        chosen = max(
            uncolored,
            key=lambda index: (
                len({colors[neighbor] for neighbor in adjacency[index] if neighbor in colors}),
                len(adjacency[index]),
                -index,
            ),
        )
        forbidden = {
            colors[neighbor]
            for neighbor in adjacency[chosen]
            if neighbor in colors
        }
        color = 0
        while color in forbidden:
            color += 1
        colors[chosen] = color

    number = max(colors.values(), default=-1) + 1
    blocks = [
        [records[index][0] for index in range(len(records)) if colors[index] == color]
        for color in range(number)
    ]
    for block in blocks:
        chosen = [record for record in records if record[0] in block]
        assert len({vertex for record in chosen for vertex in record[1]}) == 2 * len(block)
        assert len({vertex for record in chosen for vertex in record[2]}) == 2 * len(block)
    return blocks, max((len(neighbors) for neighbors in adjacency), default=0)


def role_degree(records: list[Record]) -> int:
    source = Counter(vertex for record in records for vertex in record[1])
    target = Counter(vertex for record in records for vertex in record[2])
    return max((*source.values(), *target.values()), default=0)


def block_profile(
    points: list[Point], starts: list[Point] | None = None,
    q_value: Point | None = None, vectors: dict[Point, Point] | None = None,
) -> tuple[int, int, int, int, int, int, int]:
    fibres = clean_start_fibres(points)
    if starts is None:
        q_value = max(fibres, key=lambda value: len(fibres[value]))
        starts = fibres[q_value]
    elif q_value is None:
        exact = [value for value, fibre in fibres.items() if set(fibre) == set(starts)]
        assert len(exact) == 1
        q_value = exact[0]
    assert q_value is not None

    records = role_records(points, starts, q_value)
    delta = role_degree(records)
    blocks, maximum_conflict_degree = dsatur_blocks(records)
    assert maximum_conflict_degree <= 4 * (delta - 1)
    assert len(blocks) <= 4 * delta - 3
    assert len(blocks) >= delta
    assert len(blocks) >= (len(starts) + len(points) // 2 - 1) // (len(points) // 2)

    if vectors is None:
        vectors = oriented_edge_vectors(points)
    all_vectors = list(vectors.values())
    envelope = selected = 0
    for block in blocks:
        profile = adaptive_profile([vectors[start] for start in block], all_vectors)
        envelope += profile[6]
        selected += profile[7]
    assert selected <= envelope
    return (
        len(points), len(starts), len(all_vectors), len(blocks), delta,
        envelope, selected,
    )


K33_POINTS: list[Point] = [
    (0, 0), (-62844, -124406),
    (330478260, 47388196), (330478060, 47388196),
    (330511582, 47450799), (330507582, 47449999),
    (614581493, 333961874), (614578093, 333961874),
    (614612815, 334025277), (614609615, 334022877),
    (892974475, 601933862), (892967075, 601933862),
    (893003597, 601997265), (893000797, 601994865),
    (459336301, 1975128952), (459335901, 1975128952),
    (459370023, 1975191355), (459365023, 1975190955),
    (205815148, 885472768), (205808348, 885472768),
    (205845470, 885535571), (205840870, 885534371),
    (242740076, 82878138), (242725276, 82878138),
    (242765798, 82940941), (242762398, 82939741),
    (891138064, 1037977992), (891137264, 1037977992),
    (891172586, 1038040295), (891165586, 1038040095),
    (688573727, 1225123738), (688560127, 1225123738),
    (688601449, 1225186241), (688595249, 1225185641),
    (1770488384, 180130627), (1770458784, 180130627),
    (1770505106, 180193130), (1770504906, 180192530),
]


def genuine_k33_check() -> tuple[int, int, tuple[int, ...], tuple[int, ...]]:
    points = K33_POINTS
    q_value = (62844, 124406)
    assert distance_sidon(points)
    fibres = clean_start_fibres(points)
    assert len(fibres[q_value]) == 9 == max(map(len, fibres.values()))
    vectors = oriented_edge_vectors(points)

    traces: list[int] = []
    areas: list[int] = []
    source_norms: list[int] = []
    target_norms: list[int] = []
    for index in range(9):
        source_left, source_right, target_left, target_right = points[
            2 + 4 * index:6 + 4 * index
        ]
        source_start = add(source_left, source_right)
        target_start = add(target_left, target_right)
        assert add(source_start, q_value) == target_start
        assert source_start in fibres[q_value]
        source_vector, target_vector = vectors[source_start], vectors[target_start]
        traces.append(norm2(source_vector) + 18 * norm2(target_vector))
        areas.append(determinant(source_vector, target_vector))
        source_norms.append(norm2(source_vector))
        target_norms.append(norm2(target_vector))

    assert len(set(source_norms)) == len(source_norms)
    assert len(set(target_norms)) == len(target_norms)
    assert set(source_norms).isdisjoint(target_norms)
    trace_values = tuple(sorted(set(traces)))
    area_values = tuple(sorted(set(areas)))
    assert trace_values == (299_560_000, 453_040_000, 883_360_000)
    assert area_values == (160_000, 8_160_000, 17_760_000)
    assert Counter(zip(traces, areas)) == Counter(
        (trace, area) for trace in trace_values for area in area_values
    )
    return len(points), len(fibres[q_value]), trace_values, area_values


def abstract_heavy_role_system(prime: int) -> tuple[int, int, int, float]:
    """Check the role-only heavy obstruction at one finite prime."""
    assert prime % 2 == 1
    dense: list[tuple[tuple[str, int], tuple[str, int], tuple[str, int], tuple[str, int]]] = []
    for first in range(prime):
        for second in range(prime):
            dense.append((
                ("R", first), ("C", second),
                ("U", (first + second) % prime),
                ("V", (first + 2 * second) % prime),
            ))
    for left, right in combinations(dense, 2):
        source_conflict = left[0] == right[0] or left[1] == right[1]
        target_conflict = left[2] == right[2] or left[3] == right[3]
        assert not (source_conflict and target_conflict)

    degree = prime * floor(sqrt(prime))
    k_value = 4 * prime + 3 * degree + 1
    h_value = prime * prime + degree
    delta = degree
    # The added source star is a clique of this order in every
    # bi-matching coloring.
    ratio_lower_bound = delta * k_value / h_value
    return k_value, h_value, delta, ratio_lower_bound


def projective_plane_check(prime: int) -> tuple[int, int, int, int]:
    """Incidence graph of PG(2,p): regular and C4-free."""
    assert prime in (3, 5, 7)

    def canonical(vector: tuple[int, int, int]) -> tuple[int, int, int]:
        for value in vector:
            if value % prime:
                inverse = pow(value, -1, prime)
                return tuple((entry * inverse) % prime for entry in vector)
        raise AssertionError("zero vector")

    objects = {
        canonical((first, second, third))
        for first in range(prime)
        for second in range(prime)
        for third in range(prime)
        if (first, second, third) != (0, 0, 0)
    }
    points = sorted(objects)
    lines = sorted(objects)
    neighbors = {
        point: {
            line for line in lines
            if sum(point[index] * line[index] for index in range(3)) % prime == 0
        }
        for point in points
    }
    order = prime * prime + prime + 1
    assert len(points) == len(lines) == order
    assert {len(values) for values in neighbors.values()} == {prime + 1}
    maximum_codegree = max(
        len(neighbors[first].intersection(neighbors[second]))
        for first, second in combinations(points, 2)
    )
    assert maximum_codegree == 1
    edges = sum(map(len, neighbors.values()))
    return 2 * order, edges, prime + 1, maximum_codegree


def main() -> None:
    star_expected = {
        2: (9, 2, 2, 2),
        5: (18, 5, 5, 5),
        8: (27, 8, 8, 8),
    }
    for length, expected in star_expected.items():
        actual = star_check(length)
        assert actual == expected, (length, actual, expected)
        print("genuine-star", length, actual)

    heavy = abstract_heavy_role_system(11)
    assert heavy[:3] == (144, 154, 33)
    assert heavy[3] > 30
    print("abstract-heavy-role", heavy)

    k33 = genuine_k33_check()
    assert k33 == (
        38, 9,
        (299_560_000, 453_040_000, 883_360_000),
        (160_000, 8_160_000, 17_760_000),
    )
    print("genuine-K33", k33)

    plane = projective_plane_check(5)
    assert plane == (62, 186, 6, 1)
    print("projective-plane-support", plane)

    genuine = [
        ("closure-40", POINTS[:40], None, None, None),
        ("closure-120", POINTS[:120], None, None, None),
        ("Costas-22", transformed_costas(23), None, None, None),
        ("parabola-image-43", transformed_parabola_43(), None, None, None),
    ]
    expected = {
        "closure-40": (40, 23, 780, 4, 4, 18_244, 18_080),
        "closure-120": (120, 127, 7_140, 6, 6, 918_041, 912_624),
        "Costas-22": (22, 34, 231, 7, 7, 7_898, 7_896),
        "parabola-image-43": (43, 171, 903, 14, 14, 154_575, 154_573),
    }
    for name, points, starts, q_value, vectors in genuine:
        actual = block_profile(points, starts, q_value, vectors)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual, "envelope/mass", actual[5] / (actual[1] * actual[2]))

    points, starts, vectors = two_arm_instance(50)
    two_arm = block_profile(points, starts, vectors=vectors)
    expected_two_arm = (100, 114, 4_950, 10, 9, 564_335, 564_330)
    assert two_arm == expected_two_arm, (two_arm, expected_two_arm)
    print("two-arm-50", two_arm, "envelope/mass", two_arm[5] / (two_arm[1] * two_arm[2]))

    print("trace-area bi-matching block gate: PASS")


if __name__ == "__main__":
    main()
