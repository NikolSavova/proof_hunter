#!/usr/bin/env python3
"""Checks for STAR_HEAVY_ENDPOINT_BARRIER_AND_PARTIAL_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from random import Random

from verify_adaptive_trace_area_endpoint_charge import adaptive_profile
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import add, dilation, oriented_edge_vectors
from verify_matching_block_translation_leverage import distance_sidon
from verify_metric_scalar_fourier_endpoint_no_go import two_arm_instance
from verify_metric_scalar_squareclass_transverse import endpoint_map
from verify_metric_trace_area_hybrid_audit import determinant, norm2


Point = tuple[int, int]
Edge = tuple[Point, Point]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def direct_clean_fibre(points: list[Point], q_value: Point) -> list[Point]:
    """Compute H_q directly from its unique distinguished endpoint pair."""
    pairs = {
        add(points[first], points[second]): (first, second)
        for first, second in combinations(range(len(points)), 2)
    }
    anchors = [
        (first, second)
        for first in range(len(points))
        for second in range(len(points))
        if first != second and subtract(points[first], points[second]) == q_value
    ]
    assert len(anchors) == 1
    anchor_a, anchor_b = anchors[0]

    output: list[Point] = []
    for start, (first, second) in pairs.items():
        target = add(start, q_value)
        if target not in pairs:
            continue
        third, fourth = pairs[target]
        if len({anchor_a, anchor_b, first, second, third, fourth}) == 6:
            output.append(start)
    return output


def augmented_heavy_fibre(degree: int = 20) -> tuple[
    list[Point], Point, Point, list[Point], int
]:
    """Deterministic finite instance of the polynomial-avoidance extension."""
    points = transformed_parabola_43()
    fibres = clean_start_fibres(points)
    q_value = max(fibres, key=lambda value: len(fibres[value]))
    old_starts = set(fibres[q_value])
    assert q_value == (396, -38) and len(old_starts) == 171
    assert set(direct_clean_fibre(points, q_value)) == old_starts

    random = Random(120838)
    radius = 10**12
    while True:
        center = (
            random.randrange(-radius, radius),
            random.randrange(-radius, radius),
        )
        if distance_sidon(points + [center]):
            points.append(center)
            break

    new_starts: list[Point] = []
    attempts = 0
    for _ in range(degree):
        while True:
            attempts += 1
            leaf = (
                random.randrange(-radius, radius),
                random.randrange(-radius, radius),
            )
            target_left = (
                random.randrange(-radius, radius),
                random.randrange(-radius, radius),
            )
            target_right = (
                center[0] + leaf[0] + q_value[0] - target_left[0],
                center[1] + leaf[1] + q_value[1] - target_left[1],
            )
            candidate = points + [leaf, target_left, target_right]
            if len(candidate) != len(set(candidate)) or not distance_sidon(candidate):
                continue
            start = add(center, leaf)
            wanted = old_starts | set(new_starts) | {start}
            if set(direct_clean_fibre(candidate, q_value)) != wanted:
                continue
            points = candidate
            new_starts.append(start)
            break

    assert attempts == degree
    assert len(points) == 44 + 3 * degree
    assert distance_sidon(points)
    exact_fibres = clean_start_fibres(points)
    assert set(exact_fibres[q_value]) == old_starts | set(new_starts)
    assert len(exact_fibres[q_value]) == 171 + degree

    endpoints = endpoint_map(points)
    source_edges = [endpoints[start] for start in new_starts]
    target_edges = [endpoints[add(start, q_value)] for start in new_starts]
    assert all(center in edge for edge in source_edges)
    assert len({vertex for edge in target_edges for vertex in edge}) == 2 * degree
    return points, q_value, center, new_starts, attempts


STAR_K33_POINTS: list[Point] = [
    (9171893, 15542298), (-9201267, -3777082), (0, 0),
    (-92, -346), (9186306, 9655873), (9186762, 9663161),
    (3706, 4828), (9188473, 9665684), (9188393, 9658524),
    (12802, 3404), (9194851, 9664112), (9191111, 9658672),
    (-568, 436), (9190064, 9657467), (9182528, 9662349),
    (4556, 11288), (9188313, 9661114), (9189403, 9669554),
    (-26344, 2812), (9176548, 9661841), (9170268, 9660351),
    (-152, -1424), (9186991, 9665227), (9186017, 9652729),
    (-272, 24344), (9186919, 9677417), (9185969, 9666307),
    (-36112, 38776), (9168253, 9678581), (9168795, 9679575),
]


def star_k33_profile() -> tuple[int, ...]:
    points = STAR_K33_POINTS
    q_value = (18_373_160, 19_319_380)
    center = (0, 0)
    assert distance_sidon(points)
    fibres = clean_start_fibres(points)
    assert len(fibres[q_value]) == 9 == max(map(len, fibres.values()))
    endpoints = endpoint_map(points)
    vectors = oriented_edge_vectors(points)

    starts = fibres[q_value]
    assert all(center in endpoints[start] for start in starts)
    targets = [add(start, q_value) for start in starts]
    assert len({vertex for target in targets for vertex in endpoints[target]}) == 18

    traces: list[int] = []
    areas: list[int] = []
    source_norms: list[int] = []
    target_norms: list[int] = []
    for start, target in zip(starts, targets):
        source_vector, target_vector = vectors[start], vectors[target]
        traces.append(norm2(source_vector) + 18 * norm2(target_vector))
        areas.append(determinant(source_vector, target_vector))
        source_norms.append(norm2(source_vector))
        target_norms.append(norm2(target_vector))

    trace_values = tuple(sorted(set(traces)))
    area_values = tuple(sorted(set(areas)))
    assert trace_values == (959_940_020, 1_451_766_680, 2_830_727_120)
    assert area_values == (512_720, 26_148_720, 56_911_920)
    assert Counter(zip(traces, areas)) == Counter(
        (trace, area) for trace in trace_values for area in area_values
    )
    assert len(set(source_norms)) == len(source_norms)
    assert len(set(target_norms)) == len(target_norms)
    assert set(source_norms).isdisjoint(target_norms)

    restricted = adaptive_profile(
        [vectors[start] for start in starts],
        [vectors[target] for target in targets],
    )
    assert restricted == (
        9, 9, 81, 99, 99, 81, 99, 99, 1, 81, 99, 99, 3,
    )
    return (
        len(points), len(starts), len(trace_values), len(area_values),
        restricted[2], restricted[6], restricted[7],
    )


def largest_source_star(
    points: list[Point], starts: list[Point], q_value: Point,
) -> tuple[Point, list[Point]]:
    endpoints = endpoint_map(points)
    incident: dict[Point, list[Point]] = defaultdict(list)
    for start in starts:
        for endpoint in endpoints[start]:
            incident[endpoint].append(start)
    center = max(incident, key=lambda value: len(incident[value]))
    return center, incident[center]


def gaussian_star_profile(
    points: list[Point], starts: list[Point], q_value: Point,
    vectors: dict[Point, Point] | None = None,
) -> tuple[int, int, int, int, tuple[int, ...]]:
    """Split orientations and classify ordered off-diagonal collisions."""
    if vectors is None:
        vectors = oriented_edge_vectors(points)
    endpoints = endpoint_map(points)
    center, star = largest_source_star(points, starts, q_value)
    halves: dict[bool, list[Point]] = defaultdict(list)
    for start in star:
        source_edge = endpoints[start]
        leaf = source_edge[0] if source_edge[1] == center else source_edge[1]
        center_minus_leaf = subtract(center, leaf)
        halves[vectors[start] == center_minus_leaf].append(start)

    diagonal = intersecting = disjoint = energy = 0
    for half in halves.values():
        loads: dict[Point, list[tuple[Point, Point]]] = defaultdict(list)
        for start in half:
            for target in vectors:
                key = add(vectors[start], dilation(vectors[target]))
                loads[key].append((start, target))
        mass = len(half) * len(vectors)
        diagonal += mass
        for records in loads.values():
            energy += len(records) * len(records)
            for first in records:
                for second in records:
                    if first == second:
                        continue
                    if set(endpoints[first[1]]).intersection(endpoints[second[1]]):
                        intersecting += 1
                    else:
                        disjoint += 1
    assert energy == diagonal + intersecting + disjoint
    assert intersecting <= 8 * len(points) * sum(
        len(half) * len(half) for half in halves.values()
    )
    return diagonal, intersecting, disjoint, energy, tuple(sorted(map(len, halves.values()), reverse=True))


def main() -> None:
    points, q_value, center, new_starts, attempts = augmented_heavy_fibre()
    vectors = oriented_edge_vectors(points)
    adaptive = adaptive_profile(
        [vectors[start] for start in new_starts], list(vectors.values())
    )
    assert adaptive == (
        20, 5_356, 107_120, 107_120, 110_602, 107_120,
        107_120, 107_120, 1, 107_120, 107_120, 107_120, 1,
    )
    heavy = (
        len(points), len(direct_clean_fibre(points, q_value)),
        len(new_starts), attempts, adaptive[6],
    )
    assert heavy == (104, 191, 20, 20, 107_120)
    print("genuine-heavy-star-augmentation", heavy, "center", center)

    k33 = star_k33_profile()
    assert k33 == (30, 9, 3, 3, 81, 99, 99)
    print("genuine-source-star-K33", k33)

    # Benign genuine stresses have no off-diagonal star-Gaussian collision
    # after the necessary orientation split.
    parabola = transformed_parabola_43()
    parabola_fibres = clean_start_fibres(parabola)
    parabola_q = max(parabola_fibres, key=lambda value: len(parabola_fibres[value]))
    parabola_profile = gaussian_star_profile(
        parabola, parabola_fibres[parabola_q], parabola_q
    )
    assert parabola_profile == (12_642, 0, 0, 12_642, (9, 5))
    print("parabola-star-Gaussian", parabola_profile)

    # The resonant two-arm family activates almost entirely the remaining
    # four-distinct ordinary-edge branch.
    two_arm_points, two_arm_starts, two_arm_vectors = two_arm_instance(50)
    two_arm_fibres = clean_start_fibres(two_arm_points)
    exact_q = [
        value for value, fibre in two_arm_fibres.items()
        if set(fibre) == set(two_arm_starts)
    ]
    assert exact_q == [(607, 607)]
    two_arm_profile = gaussian_star_profile(
        two_arm_points, two_arm_starts, exact_q[0], two_arm_vectors
    )
    assert two_arm_profile == (44_550, 124, 4_208, 48_882, (7, 2))
    print("two-arm-star-Gaussian", two_arm_profile)

    print("star-heavy endpoint barrier and partial gate: PASS")


if __name__ == "__main__":
    main()
