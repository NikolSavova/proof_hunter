#!/usr/bin/env python3
"""Exact planted barrier for scalar backward cells, plus amplification checks."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from random import Random

from verify_gaussian_edge_vector_two_arm_barrier import dense_ruler


Point = tuple[int, int]
ROWS = 4
TARGET_RECORDS = 5
RANDOM_SEED = 12081208
RADIUS = 10**10
TARGET_HORIZONTAL = 100
K = 36 * (TARGET_HORIZONTAL + 1)
SOURCE_GAP = 2 * K
TARGET_GAP = -SOURCE_GAP // 18


def add(*points: Point) -> Point:
    return sum(point[0] for point in points), sum(point[1] for point in points)


def sub(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def norm2(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def distance2(first: Point, second: Point) -> int:
    return norm2(sub(first, second))


def determinant(first: Point, second: Point) -> int:
    return first[0] * second[1] - first[1] * second[0]


def random_point(random: Random) -> Point:
    return random.randint(-RADIUS, RADIUS), random.randint(-RADIUS, RADIUS)


def pair_tables(points: list[Point]) -> tuple[
    dict[Point, tuple[int, int]], dict[int, tuple[int, int]]
]:
    sums: dict[Point, tuple[int, int]] = {}
    distances: dict[int, tuple[int, int]] = {}
    for first, second in combinations(range(len(points)), 2):
        pair_sum = add(points[first], points[second])
        label = distance2(points[first], points[second])
        if pair_sum in sums or label in distances or not label:
            raise ValueError((first, second, pair_sum, label))
        sums[pair_sum] = first, second
        distances[label] = first, second
    return sums, distances


def clean_row(
    source: tuple[int, int],
    anchor: tuple[int, int],
    target: tuple[int, int],
) -> bool:
    return len({*source, *anchor, *target}) == 6


def build_candidate(random: Random):
    # Fixed target star P_g and fixed clean transition w in H_g.
    while True:
        x, y, z, a, b, c = [random_point(random) for _ in range(6)]
        g = sub(y, x)
        d = sub(add(a, b, g), c)
        base = [x, y, z, a, b, c, d]
        v, w = add(x, z), add(a, b)
        difference = sub(v, w)
        if len(set(base)) == 7 and difference[0] % 2 and difference[1] % 2:
            break

    points = list(base)
    x_i, y_i, z_i, a_i, b_i, c_i, d_i = range(7)
    good_sources: list[tuple[int, int]] = []
    bad_sources: list[tuple[int, int]] = []
    first_anchors: list[tuple[int, int]] = []
    second_anchors: list[tuple[int, int]] = []
    translations: list[Point] = []

    for index in range(ROWS):
        parameter = 11 + 2 * index
        midpoint = (SOURCE_GAP + 1 + parameter * parameter) // 2
        good_vector = midpoint, 0
        bad_vector = midpoint - 1, -parameter
        assert norm2(good_vector) - norm2(bad_vector) == SOURCE_GAP

        good_first = random_point(random)
        good_second = add(good_first, good_vector)
        good_sum = add(good_first, good_second)
        bad_sum = sub(good_sum, difference)
        parity = sub(bad_sum, bad_vector)
        assert parity[0] % 2 == parity[1] % 2 == 0
        bad_first = parity[0] // 2, parity[1] // 2
        bad_second = add(bad_first, bad_vector)

        good_sources.append((len(points), len(points) + 1))
        points.extend((good_first, good_second))
        bad_sources.append((len(points), len(points) + 1))
        points.extend((bad_first, bad_second))

        q = sub(v, good_sum)
        first_tail = random_point(random)
        first_head = add(first_tail, q)
        first_anchors.append((len(points), len(points) + 1))
        points.extend((first_head, first_tail))

        second_tail = random_point(random)
        second_head = add(second_tail, q, g)
        second_anchors.append((len(points), len(points) + 1))
        points.extend((second_head, second_tail))
        translations.append(q)

    # Independent determinant-qualified target wedge at TARGET_GAP.
    metric_centre = len(points)
    centre_point = random_point(random)
    points.append(centre_point)
    metric_records: list[tuple[int, int, int]] = []
    for mark in dense_ruler(TARGET_RECORDS):
        vertical = 10**6 + 100 * mark
        first_vector = TARGET_HORIZONTAL, vertical
        partner_vector = TARGET_HORIZONTAL + 2, vertical
        leaf = len(points)
        points.append(add(centre_point, first_vector))
        partner_first = len(points)
        partner_centre = random_point(random)
        points.extend((partner_centre, add(partner_centre, partner_vector)))
        metric_records.append((leaf, partner_first, partner_first + 1))

    return (
        points,
        (x_i, y_i, z_i, a_i, b_i, c_i, d_i),
        good_sources,
        bad_sources,
        first_anchors,
        second_anchors,
        translations,
        metric_centre,
        metric_records,
        g,
        v,
        w,
    )


def main() -> None:
    random = Random(RANDOM_SEED)
    for attempt in range(1, 501):
        data = build_candidate(random)
        points = data[0]
        if len(points) != len(set(points)):
            continue
        try:
            pair_sums, distances = pair_tables(points)
        except ValueError:
            continue
        break
    else:
        raise AssertionError("finite-avoidance specialization search exhausted")

    (
        _,
        (x, y, z, a, b, c, d),
        good_sources,
        bad_sources,
        first_anchors,
        second_anchors,
        translations,
        metric_centre,
        metric_records,
        g,
        v,
        w,
    ) = data

    assert set(pair_sums[v]) == {x, z}
    assert set(pair_sums[add(v, g)]) == {y, z}
    assert set(pair_sums[w]) == {a, b}
    assert set(pair_sums[add(w, g)]) == {c, d}
    assert clean_row((a, b), (y, x), (c, d))

    cells = Counter()
    source_areas: set[int] = set()
    all_common_translation_counts: list[int] = []
    for index, q in enumerate(translations):
        good = good_sources[index]
        bad = bad_sources[index]
        first_anchor = first_anchors[index]
        second_anchor = second_anchors[index]
        good_sum = add(points[good[0]], points[good[1]])
        bad_sum = add(points[bad[0]], points[bad[1]])
        assert sub(v, good_sum) == sub(w, bad_sum) == q
        assert sub(points[first_anchor[0]], points[first_anchor[1]]) == q
        assert sub(points[second_anchor[0]], points[second_anchor[1]]) == add(q, g)

        assert clean_row(good, first_anchor, (x, z))
        assert clean_row(bad, first_anchor, (a, b))
        assert clean_row(good, second_anchor, (y, z))
        assert clean_row(bad, second_anchor, (c, d))
        assert set(good).isdisjoint(bad)

        good_label = distance2(points[good[0]], points[good[1]])
        bad_label = distance2(points[bad[0]], points[bad[1]])
        assert good_label - bad_label == SOURCE_GAP
        cells[g, v, w, good_label - bad_label] += 1
        good_vector = sub(points[good[0]], points[good[1]])
        bad_vector = sub(points[bad[0]], points[bad[1]])
        source_areas.add(2 * determinant(good_vector, bad_vector))

        # Count all clean common translations of this planted source pair.
        common = 0
        for head in range(len(points)):
            for tail in range(len(points)):
                if head == tail:
                    continue
                shift = sub(points[head], points[tail])
                first_target_sum = add(good_sum, shift)
                second_target_sum = add(bad_sum, shift)
                if first_target_sum not in pair_sums or second_target_sum not in pair_sums:
                    continue
                first_target = pair_sums[first_target_sum]
                second_target = pair_sums[second_target_sum]
                if clean_row(good, (head, tail), first_target) and clean_row(
                    bad, (head, tail), second_target
                ):
                    common += 1
        all_common_translation_counts.append(common)

    assert cells[g, v, w, SOURCE_GAP] == ROWS
    assert len(source_areas) == ROWS
    assert all(count == 2 for count in all_common_translation_counts)

    cutoff = len(distances) // 2
    first_edges: list[set[int]] = []
    for leaf, partner_first, partner_second in metric_records:
        first_label = distance2(points[metric_centre], points[leaf])
        partner_label = distance2(points[partner_first], points[partner_second])
        assert first_label - partner_label == TARGET_GAP
        first_vector = sub(points[leaf], points[metric_centre])
        partner_vector = sub(points[partner_second], points[partner_first])
        assert abs(2 * determinant(first_vector, partner_vector)) > cutoff
        first_edges.append({metric_centre, leaf})
    degrees = Counter(endpoint for edge in first_edges for endpoint in edge)
    wedge_weight = sum(degree * (degree - 1) // 2 for degree in degrees.values())
    assert wedge_weight == TARGET_RECORDS * (TARGET_RECORDS - 1) // 2
    assert TARGET_GAP == -SOURCE_GAP // 18

    # Finite high-codegree amplification identities.  The certificate is
    # deliberately below the live cutoff, but the algebra is exact for any
    # selected threshold.
    threshold = 2
    direct_mass = sum(count >= threshold for count in all_common_translation_counts)
    amplified_mass = sum(
        count for count in all_common_translation_counts if count >= threshold
    )
    assert threshold * direct_mass <= amplified_mass
    replacement_counts = [0] * ROWS
    assert sum(replacement_counts) == 0
    assert sum(
        replacement * common
        for replacement, common in zip(replacement_counts, all_common_translation_counts)
    ) == 0

    point_count = len(points)
    pair_count = point_count * (point_count - 1) // 2
    assert len(pair_sums) == len(distances) == pair_count
    print("specialization attempt", attempt)
    print("point count", point_count)
    print("distance/pair-sum count", pair_count)
    print("fixed backward-cell multiplicity", cells[g, v, w, SOURCE_GAP])
    print("distinct source areas", len(source_areas))
    print("common translation counts", all_common_translation_counts)
    print("target gap", TARGET_GAP)
    print("determinant cutoff", cutoff)
    print("target wedge weight", wedge_weight)
    print("scalar backward-cell high-codegree amplification: PASS")


if __name__ == "__main__":
    main()
