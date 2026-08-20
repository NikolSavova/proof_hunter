#!/usr/bin/env python3
"""Exact certificate for the replacement-transition planted barrier."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from random import Random

from verify_gaussian_edge_vector_two_arm_barrier import dense_ruler


Point = tuple[int, int]
SOURCE_PAIRS = 3
TRANSLATIONS = 7
TARGET_RECORDS = 8
TARGET_HORIZONTAL = 1_000
RANDOM_SEED = 1208
RADIUS = 10**12


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


def pair_tables(points: list[Point]) -> tuple[dict[Point, tuple[int, int]], dict[int, tuple[int, int]]]:
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


def source_vectors() -> tuple[list[Point], list[tuple[int, int]], int]:
    gap = -4 * (TARGET_HORIZONTAL + 1)
    half_source_gap = 36 * (TARGET_HORIZONTAL + 1)
    vectors: list[Point] = []
    aligned_pairs: list[tuple[int, int]] = []
    for index in range(SOURCE_PAIRS):
        parameter = 10 + 3 * index
        low = (half_source_gap - parameter - 1, parameter)
        high = (half_source_gap - parameter, parameter + 1)
        assert norm2(high) - norm2(low) == -18 * gap
        aligned_pairs.append((len(vectors), len(vectors) + 1))
        vectors.extend((high, low))
    assert len({norm2(vector) for vector in vectors}) == len(vectors)
    return vectors, aligned_pairs, gap


def build_candidate(random: Random) -> tuple[
    list[Point],
    list[tuple[int, int]],
    list[int],
    list[tuple[int, int]],
    list[int],
    int,
    list[tuple[int, int]],
    int,
    list[tuple[int, int]],
]:
    vectors, aligned_pairs, target_gap = source_vectors()
    free_shift = random_point(random)
    points: list[Point] = []
    source_edges: list[tuple[int, int]] = []
    source_starts: list[Point] = []
    outer_indices: list[int] = []

    for vector in vectors:
        centre = random_point(random)
        first = centre
        second = add(centre, vector)
        start = add(first, second)
        source_edges.append((len(points), len(points) + 1))
        points.extend((first, second))
        source_starts.append(start)
        outer_indices.append(len(points))
        points.append(sub(start, free_shift))

    anchor_edges: list[tuple[int, int]] = []
    centre_indices: list[int] = []
    translations: list[Point] = []
    for _ in range(TRANSLATIONS):
        first_anchor = random_point(random)
        second_anchor = random_point(random)
        translation = sub(first_anchor, second_anchor)
        anchor_edges.append((len(points), len(points) + 1))
        points.extend((first_anchor, second_anchor))
        centre_indices.append(len(points))
        points.append(add(translation, free_shift))
        translations.append(translation)

    # A separate target-gap star.  Every first edge shares star_centre;
    # its partner edge has the same vertical coordinate and horizontal
    # coordinate increased by two.
    star_centre = len(points)
    star_point = random_point(random)
    points.append(star_point)
    marks = dense_ruler(TARGET_RECORDS)
    verticals = [10**6 + 100 * mark for mark in marks]
    target_records: list[tuple[int, int]] = []
    for vertical in verticals:
        first_vector = TARGET_HORIZONTAL, vertical
        second_vector = TARGET_HORIZONTAL + 2, vertical
        leaf = len(points)
        points.append(add(star_point, first_vector))
        partner_first = len(points)
        partner_centre = random_point(random)
        points.extend((partner_centre, add(partner_centre, second_vector)))
        partner_second = partner_first + 1
        target_records.append((leaf, partner_first))
        assert (
            distance2(points[star_centre], points[leaf])
            - distance2(points[partner_first], points[partner_second])
            == target_gap
        )
        assert abs(2 * determinant(first_vector, second_vector)) == 4 * vertical

    return (
        points,
        source_edges,
        outer_indices,
        anchor_edges,
        centre_indices,
        star_centre,
        target_records,
        target_gap,
        aligned_pairs,
    )


def main() -> None:
    random = Random(RANDOM_SEED)
    for attempt in range(1, 101):
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
        points,
        source_edges,
        outer_indices,
        anchor_edges,
        centre_indices,
        star_centre,
        target_records,
        target_gap,
        aligned_pairs,
    ) = data
    source_starts = [add(points[first], points[second]) for first, second in source_edges]
    translations = [sub(points[first], points[second]) for first, second in anchor_edges]

    # Every translation has the same controlled source set; its targets
    # form a star with centre X_q and outer vertices U_i.
    certified_rows = 0
    for translation_index, translation in enumerate(translations):
        anchor = set(anchor_edges[translation_index])
        target_centre = centre_indices[translation_index]
        for source_index, start in enumerate(source_starts):
            target_sum = add(start, translation)
            expected_edge = {target_centre, outer_indices[source_index]}
            assert set(pair_sums[target_sum]) == expected_edge
            assert anchor.isdisjoint(source_edges[source_index])
            assert anchor.isdisjoint(expected_edge)
            assert set(source_edges[source_index]).isdisjoint(expected_edge)
            certified_rows += 1
    assert certified_rows == len(source_edges) * TRANSLATIONS

    # Each aligned source pair is a full replacement pencil: c=rho=Q.
    replacement_records = 0
    nested_rows = 0
    for first_source, second_source in aligned_pairs:
        first_start = source_starts[first_source]
        second_start = source_starts[second_source]
        first_label = distance2(*[points[index] for index in source_edges[first_source]])
        second_label = distance2(*[points[index] for index in source_edges[second_source]])
        assert first_label - second_label == -18 * target_gap
        replacement_centres = {
            (outer_indices[first_source], outer_indices[second_source])
        }
        for translation_index in range(TRANSLATIONS):
            first_target = {
                centre_indices[translation_index], outer_indices[first_source]
            }
            second_target = {
                centre_indices[translation_index], outer_indices[second_source]
            }
            assert len(first_target & second_target) == 1
            replacement_records += 1
        assert len(replacement_centres) == 1

        # The replacement pair is itself a clean transition in the nested
        # fibre g=U_j-U_i=s_j-s_i.
        old_centre = outer_indices[first_source]
        new_centre = outer_indices[second_source]
        nested_translation = sub(points[new_centre], points[old_centre])
        assert nested_translation == sub(second_start, first_start)
        assert set(pair_sums[add(first_start, nested_translation)]) == set(
            source_edges[second_source]
        )
        assert len({
            old_centre,
            new_centre,
            *source_edges[first_source],
            *source_edges[second_source],
        }) == 6
        nested_rows += 1

    assert replacement_records == SOURCE_PAIRS * TRANSLATIONS
    assert nested_rows == SOURCE_PAIRS

    # The target first-edge graph is one star, so its determinant-qualified
    # wedge weight at target_gap is exactly choose(TARGET_RECORDS,2).
    target_first_edges: list[set[int]] = []
    cutoff = len(distances) // len(source_edges)
    for leaf, partner_first in target_records:
        partner_second = partner_first + 1
        first_label = distance2(points[star_centre], points[leaf])
        partner_label = distance2(points[partner_first], points[partner_second])
        assert first_label - partner_label == target_gap
        first_vector = sub(points[leaf], points[star_centre])
        partner_vector = sub(points[partner_second], points[partner_first])
        assert abs(2 * determinant(first_vector, partner_vector)) > cutoff
        target_first_edges.append({star_centre, leaf})

    degrees = Counter(vertex for edge in target_first_edges for vertex in edge)
    wedge_weight = sum(degree * (degree - 1) // 2 for degree in degrees.values())
    assert wedge_weight == TARGET_RECORDS * (TARGET_RECORDS - 1) // 2
    weighted_replacement_mass = replacement_records * wedge_weight

    point_count = len(points)
    pair_count = point_count * (point_count - 1) // 2
    assert len(pair_sums) == len(distances) == pair_count
    maximum_coordinate = max(abs(coordinate) for point in points for coordinate in point)
    print("specialization attempt", attempt)
    print("point count", point_count)
    print("distance/pair-sum count", pair_count)
    print("controlled clean mass", certified_rows)
    print("replacement records", replacement_records)
    print("nested transition rows", nested_rows)
    print("target gap", target_gap)
    print("determinant cutoff", cutoff)
    print("target wedge weight", wedge_weight)
    print("weighted replacement mass", weighted_replacement_mass)
    print("maximum absolute coordinate", maximum_coordinate)
    print("single-fibre replacement transition barrier: PASS")


if __name__ == "__main__":
    main()
