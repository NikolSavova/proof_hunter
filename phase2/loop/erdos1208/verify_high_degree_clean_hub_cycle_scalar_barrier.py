#!/usr/bin/env python3
"""Exact certificate for HIGH_DEGREE_CLEAN_HUB_CYCLE_SCALAR_BARRIER.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from math import isqrt
from random import Random

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_third_additive_energy_barrier import parabola, transform


Point = tuple[int, int]
CORE_PRIME = 61
HUB_DEGREE = 250
RANDOM_SEED = 1208
RADIUS = 10**12
SCALAR_VALUE = 340


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def sub(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def scale(multiplier: int, point: Point) -> Point:
    return multiplier * point[0], multiplier * point[1]


def norm2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def distance2(first: Point, second: Point) -> int:
    return norm2(sub(first, second))


def pair_tables(points: list[Point]) -> tuple[dict[Point, tuple[int, int]], dict[int, tuple[int, int]]]:
    sums: dict[Point, tuple[int, int]] = {}
    distances: dict[int, tuple[int, int]] = {}
    for first, second in combinations(range(len(points)), 2):
        pair_sum = add(points[first], points[second])
        distance = distance2(points[first], points[second])
        assert pair_sum not in sums, (pair_sum, sums.get(pair_sum), (first, second))
        assert distance > 0
        assert distance not in distances, (distance, distances.get(distance), (first, second))
        sums[pair_sum] = first, second
        distances[distance] = first, second
    return sums, distances


def find_oriented_edge(points: list[Point], difference: Point) -> tuple[int, int]:
    matches = [
        (first, second)
        for first in range(len(points))
        for second in range(len(points))
        if first != second and sub(points[first], points[second]) == difference
    ]
    assert len(matches) == 1
    return matches[0]


def build_core() -> tuple[list[Point], Point, int, tuple[int, int], list[Point]]:
    # The factor two makes q even, which is convenient for the symmetric
    # scalar rows appended below.
    points = [scale(2, point) for point in transform(parabola(CORE_PRIME))]
    pair_tables(points)
    fibres = clean_start_fibres(points)
    q = max(fibres, key=lambda difference: len(fibres[difference]))
    starts = fibres[q]
    anchors = find_oriented_edge(points, q)
    assert q == (312, 138)
    assert len(starts) == 336
    return points, q, len(starts), anchors, starts


def random_point(random: Random, radius: int) -> Point:
    return random.randint(-radius, radius), random.randint(-radius, radius)


def append_cycle_hub(
    core: list[Point], q: Point, degree: int
) -> tuple[list[Point], int, list[int], list[int]]:
    random = Random(RANDOM_SEED)
    for attempt in range(1, 101):
        center = random_point(random, RADIUS)
        leaves = [random_point(random, RADIUS) for _ in range(degree)]
        targets = [
            add(add(center, q), sub(leaves[index], leaves[(index + 1) % degree]))
            for index in range(degree)
        ]
        candidate = core + [center] + leaves + targets
        if len(candidate) != len(set(candidate)):
            continue
        try:
            pair_tables(candidate)
        except AssertionError:
            continue
        center_index = len(core)
        leaf_indices = list(range(center_index + 1, center_index + 1 + degree))
        target_indices = list(range(leaf_indices[-1] + 1, leaf_indices[-1] + 1 + degree))
        return candidate, attempt, leaf_indices, target_indices
    raise AssertionError("cycle-hub specialization search exhausted")


def representations_as_two_squares(value: int) -> list[Point]:
    output: set[Point] = set()
    for first in range(isqrt(value) + 1):
        second_squared = value - first * first
        second = isqrt(second_squared)
        if second * second != second_squared:
            continue
        for x, y in ((first, second), (second, first)):
            for sign_x in (-1, 1):
                for sign_y in (-1, 1):
                    output.add((sign_x * x, sign_y * y))
    return sorted(output)


def scalar_pairs() -> list[tuple[int, int]]:
    values = [
        value
        for value in range(1, 201)
        if representations_as_two_squares(value)
    ]
    bucket = [(first, second) for first in values for second in values if first + 18 * second == SCALAR_VALUE]
    assert bucket == [
        (16, 18),
        (34, 17),
        (52, 16),
        (106, 13),
        (160, 10),
        (178, 9),
        (196, 8),
    ]
    # Remove (16,18), because its first label collides with the second label
    # in (52,16).  The remaining twelve controlled labels are all distinct.
    bucket = bucket[1:]
    assert len({value for pair in bucket for value in pair}) == 2 * len(bucket)
    return bucket


def internal_row(
    center: Point, q: Point, dilation: int, source: Point, target: Point
) -> list[Point]:
    half_q = q[0] // 2, q[1] // 2
    return [
        add(center, scale(dilation, source)),
        sub(center, scale(dilation, source)),
        add(add(center, half_q), scale(dilation, target)),
        sub(add(center, half_q), scale(dilation, target)),
    ]


def append_scalar_bucket(
    points: list[Point], q: Point
) -> tuple[list[Point], int, list[tuple[tuple[int, int], int]]]:
    random = Random(RANDOM_SEED + 1)
    bucket = scalar_pairs()

    # The controlled source/target squared distances are 4*S^2*a and
    # 4*S^2*b.  Find a common S for which six complete four-point offset
    # patterns can be chosen with globally distinct internal distances.
    for dilation in range(10**7, 10**7 + 1000):
        _, old_distances = pair_tables(points)
        occupied = set(old_distances)
        choices: list[tuple[Point, Point]] = []
        possible = True
        for source_label, target_label in bucket:
            chosen: tuple[Point, Point] | None = None
            for source in representations_as_two_squares(source_label):
                for target in representations_as_two_squares(target_label):
                    offsets = internal_row((0, 0), q, dilation, source, target)
                    labels = [distance2(offsets[i], offsets[j]) for i, j in combinations(range(4), 2)]
                    if len(labels) == 6 and not (set(labels) & occupied):
                        chosen = source, target
                        occupied.update(labels)
                        break
                if chosen is not None:
                    break
            if chosen is None:
                possible = False
                break
            choices.append(chosen)
        if possible:
            break
    else:
        raise AssertionError("no scalar offset specialization found")

    rows: list[tuple[tuple[int, int], int]] = []
    for row_number, ((source_label, target_label), (source, target)) in enumerate(zip(bucket, choices)):
        for attempt in range(1, 10_001):
            center = random_point(random, 10**15)
            row = internal_row(center, q, dilation, source, target)
            candidate = points + row
            if len(candidate) != len(set(candidate)):
                continue
            try:
                pair_tables(candidate)
            except AssertionError:
                continue
            start = add(row[0], row[1])
            assert add(start, q) == add(row[2], row[3])
            assert distance2(row[0], row[1]) + 18 * distance2(row[2], row[3]) == 4 * dilation * dilation * SCALAR_VALUE
            points = candidate
            rows.append(((len(points) - 4, len(points) - 3), attempt))
            break
        else:
            raise AssertionError(("scalar-center specialization search exhausted", row_number))
    return points, dilation, rows


def verify_walsh_rectangle(
    points: list[Point], center: int, leaves: list[int], target_points: list[int]
) -> None:
    # Check the exact four-cross-distance Walsh identities for one pair of
    # spokes.  The paper proves the displayed formulas for every pair.
    first, second = 0, 1
    delta = sub(points[leaves[first]], points[leaves[second]])
    edge_first = sub(points[leaves[(first + 1) % len(leaves)]], points[target_points[first]])
    edge_second = sub(points[leaves[(second + 1) % len(leaves)]], points[target_points[second]])
    labels: dict[tuple[int, int], int] = {}
    for sign_first in (-1, 1):
        for sign_second in (-1, 1):
            vector = add(delta, add(scale(sign_first, edge_first), scale(sign_second, edge_second)))
            assert vector[0] % 2 == 0 and vector[1] % 2 == 0
            labels[sign_first, sign_second] = norm2((vector[0] // 2, vector[1] // 2))
    actual_cross_labels = {
        distance2(points[first_endpoint], points[second_endpoint])
        for first_endpoint in (leaves[first + 1], target_points[first])
        for second_endpoint in (leaves[second + 1], target_points[second])
    }
    assert set(labels.values()) == actual_cross_labels
    assert len(set(labels.values())) == 4
    assert sum(labels.values()) == norm2(delta) + norm2(edge_first) + norm2(edge_second)
    assert sum(sign_first * value for (sign_first, _), value in labels.items()) == 2 * (
        delta[0] * edge_first[0] + delta[1] * edge_first[1]
    )
    assert sum(sign_second * value for (_, sign_second), value in labels.items()) == 2 * (
        delta[0] * edge_second[0] + delta[1] * edge_second[1]
    )
    assert sum(sign_first * sign_second * value for (sign_first, sign_second), value in labels.items()) == 2 * (
        edge_first[0] * edge_second[0] + edge_first[1] * edge_second[1]
    )
    assert center not in leaves and center not in target_points


def main() -> None:
    core, q, core_fibre, anchors, core_starts = build_core()
    points, hub_attempt, leaves, target_points = append_cycle_hub(core, q, HUB_DEGREE)
    center = len(core)

    alpha, beta = anchors
    certified_starts = set(core_starts)
    for index in range(HUB_DEGREE):
        next_index = (index + 1) % HUB_DEGREE
        source_start = add(points[center], points[leaves[index]])
        target_start = add(points[leaves[next_index]], points[target_points[index]])
        assert add(source_start, q) == target_start
        assert len({alpha, beta, center, leaves[index], leaves[next_index], target_points[index]}) == 6
        assert source_start not in certified_starts
        certified_starts.add(source_start)

    # The target edges form a matching, while every source leaf occurs in
    # exactly the next target edge: the endpoint-overlap digraph is one cycle.
    target_edges = [
        {leaves[(index + 1) % HUB_DEGREE], target_points[index]}
        for index in range(HUB_DEGREE)
    ]
    assert all(first.isdisjoint(second) for first, second in combinations(target_edges, 2))
    assert {next(iter(edge & set(leaves))) for edge in target_edges} == set(leaves)

    # Generic specialization can, and here does, make every controlled
    # source/target edge direction different.  Thus determinant richness
    # does not rescue the hub argument.
    controlled_vectors: list[Point] = []
    for index in range(HUB_DEGREE):
        controlled_vectors.append(sub(points[center], points[leaves[index]]))
        controlled_vectors.append(
            sub(points[leaves[(index + 1) % HUB_DEGREE]], points[target_points[index]])
        )
    assert all(
        determinant(first, second) != 0
        for first, second in combinations(controlled_vectors, 2)
    )
    verify_walsh_rectangle(points, center, leaves, target_points)

    points, dilation, scalar_rows = append_scalar_bucket(points, q)
    for (source_indices, _) in scalar_rows:
        first_index = source_indices[0]
        first = points[first_index]
        second = points[first_index + 1]
        start = add(first, second)
        assert add(start, q) == add(points[first_index + 2], points[first_index + 3])
        assert len({alpha, beta, first_index, first_index + 1, first_index + 2, first_index + 3}) == 6
        assert start not in certified_starts
        certified_starts.add(start)

    sums, distances = pair_tables(points)
    point_count = len(points)
    pair_count = point_count * (point_count - 1) // 2
    assert len(sums) == pair_count == len(distances)
    assert len(certified_starts) == core_fibre + HUB_DEGREE + len(scalar_rows)
    assert len(certified_starts) > point_count
    assert HUB_DEGREE / point_count > 0.42

    scalar_charge = 4 * dilation * dilation * SCALAR_VALUE
    scalar_loads = Counter()
    for source_indices, _ in scalar_rows:
        first_index = source_indices[0]
        source_distance = distance2(points[first_index], points[first_index + 1])
        target_distance = distance2(points[first_index + 2], points[first_index + 3])
        scalar_loads[source_distance + 18 * target_distance] += 1
    assert scalar_loads == Counter({scalar_charge: 6})

    maximum_coordinate = max(abs(coordinate) for point in points for coordinate in point)
    print("q", q)
    print("core clean fibre", core_fibre)
    print("cycle hub attempt", hub_attempt)
    print("hub degree", HUB_DEGREE)
    print("scalar dilation", dilation)
    print("scalar row center attempts", [attempt for _, attempt in scalar_rows])
    print("point count", point_count)
    print("unordered distances", pair_count)
    print("certified same-q clean starts", len(certified_starts))
    print("hub degree / point count", HUB_DEGREE / point_count)
    print("scalar bucket load", max(scalar_loads.values()))
    print("maximum absolute coordinate", maximum_coordinate)
    print("all exact high-degree clean-hub barrier checks passed")


if __name__ == "__main__":
    main()
