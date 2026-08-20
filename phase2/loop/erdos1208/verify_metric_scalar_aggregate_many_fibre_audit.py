#!/usr/bin/env python3
"""Exact identities and graph-only countermodel for the aggregate scalar gate."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_metric_scalar_pair_sum_charge import pair_labels
from verify_metric_scalar_squareclass_transverse import (
    endpoint_map,
    squarefree_kernel,
)
from verify_third_additive_energy_barrier import parabola, transform
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, ...]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def determinant(left: Point, right: Point) -> int:
    return left[0] * right[1] - left[1] * right[0]


def aggregate_profile(points: list[Point]) -> Profile:
    labels = pair_labels(points)
    endpoints = endpoint_map(points)
    vectors = {
        pair_sum: subtract(edge[0], edge[1])
        for pair_sum, edge in endpoints.items()
    }
    kernels = {
        pair_sum: squarefree_kernel(label)
        for pair_sum, label in labels.items()
    }
    fibres = clean_start_fibres(points)
    edge_sums = list(endpoints)
    n_edges = len(edge_sums)

    difference_loads: Counter[int] = Counter(
        labels[first] - labels[second]
        for first in edge_sums
        for second in edge_sums
    )

    total_h = sum(map(len, fibres.values()))
    total_mass = total_h * n_edges
    total_energy = 0
    codegree_energy = 0
    diagonal = 0
    repeated = 0
    resonant = 0
    transverse_low_area = 0
    transverse_large_area = 0
    maximum_source_degree = 0

    anchor_by_difference = {
        subtract(points[first], points[second]): (points[first], points[second])
        for first in range(len(points))
        for second in range(len(points))
        if first != second
    }

    # The exact codegree expansion
    # sum_(s,s') c(s,s') r_(D-D)((delta(s')-delta(s))/18).
    codegrees: Counter[tuple[Point, Point]] = Counter()
    for starts in fibres.values():
        for first in starts:
            for second in starts:
                codegrees[first, second] += 1
    for (first, second), multiplicity in codegrees.items():
        numerator = labels[second] - labels[first]
        if numerator % 18 == 0:
            codegree_energy += multiplicity * difference_loads[numerator // 18]

    for q_value, starts in fibres.items():
        h = len(starts)
        threshold = n_edges // h
        anchors = set(anchor_by_difference[q_value])
        source_stars: dict[Point, list[Point]] = defaultdict(list)
        for start in starts:
            for vertex in endpoints[start]:
                source_stars[vertex].append(start)
        for center, star in source_stars.items():
            maximum_source_degree = max(maximum_source_degree, len(star))
            used_target_vertices: set[Point] = set()
            for start in star:
                target_edge = endpoints[add(start, q_value)]
                assert not (set(target_edge) & anchors)
                assert center not in target_edge
                assert not (set(target_edge) & used_target_vertices)
                used_target_vertices.update(target_edge)
            assert 2 * len(star) <= len(points) - 3
        records: dict[int, list[tuple[Point, Point]]] = defaultdict(list)
        for start in starts:
            for target in edge_sums:
                records[labels[start] + 18 * labels[target]].append((start, target))
        total_energy += sum(len(bucket) ** 2 for bucket in records.values())

        for bucket in records.values():
            for first_record in bucket:
                for second_record in bucket:
                    start, target = first_record
                    other_start, other_target = second_record
                    if first_record == second_record:
                        diagonal += 1
                        continue
                    if len({start, target, other_start, other_target}) < 4:
                        repeated += 1
                        continue
                    if (
                        kernels[start] == kernels[other_start]
                        and kernels[target] == kernels[other_target]
                    ):
                        resonant += 1
                        continue
                    doubled_area = abs(
                        2 * determinant(vectors[target], vectors[other_target])
                    )
                    if doubled_area <= threshold:
                        transverse_low_area += 1
                    else:
                        transverse_large_area += 1

    assert total_energy == codegree_energy
    assert diagonal == total_mass
    assert total_energy == sum((
        diagonal,
        repeated,
        resonant,
        transverse_low_area,
        transverse_large_area,
    ))
    # Aggregate versions of the already-proved easy estimates use only
    # sum h_q^2 <= N sum h_q.
    sum_h_squared = sum(len(starts) ** 2 for starts in fibres.values())
    assert sum_h_squared <= n_edges * total_h
    assert repeated <= 4 * sum_h_squared

    return (
        len(points),
        len(fibres),
        total_h,
        n_edges,
        total_mass,
        total_energy,
        diagonal,
        repeated,
        resonant,
        transverse_low_area,
        transverse_large_area,
        sum_h_squared,
        max(map(len, fibres.values())),
        maximum_source_degree,
    )


def one_factorization(vertex_count: int) -> list[list[tuple[int, int]]]:
    assert vertex_count % 2 == 0 and vertex_count >= 4
    modulus = vertex_count - 1
    infinity = modulus
    factors: list[list[tuple[int, int]]] = []
    for center in range(modulus):
        factor = [tuple(sorted((infinity, center)))]
        for offset in range(1, vertex_count // 2):
            factor.append(
                tuple(sorted(((center + offset) % modulus,
                              (center - offset) % modulus)))
            )
        assert len({vertex for edge in factor for vertex in edge}) == vertex_count
        factors.append(sorted(factor))
    flattened = [edge for factor in factors for edge in factor]
    assert len(flattened) == vertex_count * (vertex_count - 1) // 2
    assert len(set(flattened)) == len(flattened)
    return factors


def weighted_sidon(size: int, coefficient: int) -> list[int]:
    """Greedy polynomial-size set with a+C b unique for ordered pairs."""
    values: list[int] = []
    occupied: set[int] = set()
    candidate = 0
    while len(values) < size:
        while True:
            new = [candidate + coefficient * old for old in values]
            new += [old + coefficient * candidate for old in values]
            new.append((coefficient + 1) * candidate)
            if len(new) == len(set(new)) and not (set(new) & occupied):
                break
            candidate += 1
        for old in values:
            occupied.add(candidate + coefficient * old)
            occupied.add(old + coefficient * candidate)
        occupied.add((coefficient + 1) * candidate)
        values.append(candidate)
        candidate += 1
    assert len({a + coefficient * b for a, b in product(values, repeat=2)}) == size * size
    return values


def matching_block_countermodel(
    vertex_count: int = 64, coefficient: int = 18, source_factor_count: int = 9
) -> Profile:
    factors = one_factorization(vertex_count)
    block_size = vertex_count // 2
    centers = weighted_sidon(len(factors), coefficient)
    scale = (coefficient + 1) * block_size + 1

    labels: dict[tuple[int, int], int] = {}
    block_of: dict[tuple[int, int], int] = {}
    for block, (factor, center) in enumerate(zip(factors, centers)):
        for position, edge in enumerate(factor):
            labels[edge] = scale * center + position
            block_of[edge] = block
    assert len(labels) == vertex_count * (vertex_count - 1) // 2
    assert len(set(labels.values())) == len(labels)

    source_edges = [
        edge
        for factor in factors[:source_factor_count]
        for edge in factor
    ]
    loads = Counter(
        labels[source] + coefficient * labels[target]
        for source in source_edges
        for target in labels
    )
    energy = sum(load * load for load in loads.values())

    interval_loads = Counter(
        x + coefficient * y
        for x in range(block_size)
        for y in range(block_size)
    )
    interval_energy = sum(load * load for load in interval_loads.values())
    assert energy == source_factor_count * len(factors) * interval_energy

    # Greedily install an abstract clean partner.  It is injective, each
    # target is disjoint from its source, and targets of two source edges
    # sharing a vertex are disjoint.  These are the immediate graph-theoretic
    # consequences of one genuine clean translate.
    all_edges = list(labels)
    partner: dict[tuple[int, int], tuple[int, int]] = {}
    used_targets: set[tuple[int, int]] = set()
    for edge in source_edges:
        adjacent_targets = [
            target
            for previous, target in partner.items()
            if set(previous) & set(edge)
        ]
        target = next(
            candidate
            for candidate in all_edges
            if candidate not in used_targets
            and set(candidate).isdisjoint(edge)
            and all(set(candidate).isdisjoint(old) for old in adjacent_targets)
        )
        partner[edge] = target
        used_targets.add(target)
    assert len(set(partner.values())) == len(partner)
    for first, second in combinations(source_edges, 2):
        if set(first) & set(second):
            assert set(partner[first]).isdisjoint(partner[second])

    edge_count = len(labels)
    source_count = len(source_edges)
    records = source_count * edge_count
    weak_target = edge_count * (source_count + vertex_count + 2)
    return (
        vertex_count + 2,  # include two abstract q anchors
        source_count,
        edge_count,
        len(factors),
        source_factor_count,
        block_size,
        max(centers),
        records,
        len(loads),
        energy,
        max(loads.values()),
        interval_energy,
        weak_target,
    )


def main() -> None:
    expected = {
        "closure-20": (20, 312, 648, 190, 123_120, 124_562,
                       123_120, 22, 0, 190, 1_230, 1_720, 5, 2),
        "parabola-image-17": (17, 272, 2_088, 136, 283_968, 284_024,
                              283_968, 0, 0, 0, 56, 17_768, 14, 4),
    }
    families = [
        ("closure-20", POINTS[:20]),
        ("parabola-image-17", transform(parabola(17))),
    ]
    for name, points in families:
        actual = aggregate_profile(points)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)

    abstract = matching_block_countermodel()
    assert abstract == (
        66, 288, 2_016, 63, 9, 32, 980, 580_608, 334_530,
        1_072_764, 2, 1_892, 713_664,
    ), abstract
    print("matching-block-countermodel", abstract)
    # It already violates the abstract weak target, while every structured
    # source block is a perfect matching and the clean partner is disjoint.
    assert abstract[9] > abstract[12]
    print("metric scalar aggregate many-fibre audit: PASS")


if __name__ == "__main__":
    main()
