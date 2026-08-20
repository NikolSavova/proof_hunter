#!/usr/bin/env python3
"""Translation-excess reduction and a one-fibre obstruction."""

from __future__ import annotations

from collections import Counter
from itertools import combinations
from random import Random

from verify_dilated_internal_pair_sum_charge import clean_start_fibres
from verify_gaussian_edge_vector_two_arm_barrier import dense_ruler
from verify_low_band_isolated_matching_rank_barrier import profile as closure_profile
from verify_metric_scalar_endpoint_rich_tail import determinant, edge_data
from verify_single_fibre_replacement_transition_barrier import pair_tables
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
PAIR_RECORDS = 3
RANDOM_SEED = 120_812_081
RANDOM_RADIUS = 10**12
VERTICAL_MARKS = (0, 10, 24, 26, 35, 55)


def add(first: Point, second: Point) -> Point:
    return first[0] + second[0], first[1] + second[1]


def subtract(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def distance2(first: Point, second: Point) -> int:
    difference = subtract(first, second)
    return difference[0] * difference[0] + difference[1] * difference[1]


def random_point(random: Random) -> Point:
    return (
        random.randint(-RANDOM_RADIUS, RANDOM_RADIUS),
        random.randint(-RANDOM_RADIUS, RANDOM_RADIUS),
    )


def is_golomb(marks: list[int] | tuple[int, ...]) -> bool:
    differences = [second - first for first, second in combinations(sorted(marks), 2)]
    return len(differences) == len(set(differences))


def perpendicular_base(horizontal_count: int, final_point_count: int) -> list[Point]:
    """Build the determinant-rich two-axis subsystem at its final cutoff."""
    assert is_golomb(VERTICAL_MARKS)
    horizontal_ruler = dense_ruler(horizontal_count)
    vertical_differences = {
        second - first for first, second in combinations(VERTICAL_MARKS, 2)
    }
    horizontal_differences = {
        second - first for first, second in combinations(horizontal_ruler, 2)
    }
    scale = next(
        candidate
        for candidate in range(1, 2_000_000)
        if all(
            candidate * difference not in vertical_differences
            for difference in horizontal_differences
        )
    )
    final_edge_count = final_point_count * (final_point_count - 1) // 2
    offset = max(
        final_edge_count + 1,
        max(VERTICAL_MARKS) + 1,
        scale * max(horizontal_ruler) + 1,
    )
    for _ in range(2_000_000):
        horizontal_marks = [offset + scale * mark for mark in horizontal_ruler]
        points = [
            *((mark, 0) for mark in horizontal_marks),
            *((0, mark) for mark in VERTICAL_MARKS),
        ]
        try:
            pair_tables(points)
            return points
        except ValueError:
            offset += 1
    raise AssertionError("perpendicular finite-avoidance search exhausted")


def planted_candidate(random: Random, external_point_count: int = 0) -> tuple:
    horizontal_count = 8 * PAIR_RECORDS + 8 + external_point_count
    component_point_count = 16 * PAIR_RECORDS + 16 + external_point_count
    final_point_count = component_point_count + external_point_count
    points = perpendicular_base(horizontal_count, final_point_count)

    first_anchor = len(points)
    anchor_head = random_point(random)
    anchor_tail = random_point(random)
    points.extend((anchor_head, anchor_tail))
    q = subtract(anchor_head, anchor_tail)

    source_pairs: list[tuple[tuple[int, int], tuple[int, int]]] = []
    target_pairs: list[tuple[tuple[int, int], tuple[int, int]]] = []
    half_source_gap = 900
    for record in range(PAIR_RECORDS):
        parameter = 17 + 7 * record
        high_vector = half_source_gap - parameter, parameter + 1
        low_vector = half_source_gap - parameter - 1, parameter
        assert distance2(high_vector, (0, 0)) - distance2(low_vector, (0, 0)) == 1_800

        role_sources: list[tuple[int, int]] = []
        role_targets: list[tuple[int, int]] = []
        for vector in (high_vector, low_vector):
            centre = random_point(random)
            source = (len(points), len(points) + 1)
            points.extend((centre, add(centre, vector)))
            source_sum = add(points[source[0]], points[source[1]])

            target_endpoint = random_point(random)
            target = (len(points), len(points) + 1)
            points.extend((target_endpoint, subtract(add(source_sum, q), target_endpoint)))
            role_sources.append(source)
            role_targets.append(target)
        source_pairs.append((role_sources[0], role_sources[1]))
        target_pairs.append((role_targets[0], role_targets[1]))

    assert len(points) == component_point_count
    return points, first_anchor, source_pairs, target_pairs, horizontal_count


def planted_profile() -> tuple[int, ...]:
    random = Random(RANDOM_SEED)
    for attempt in range(1, 101):
        data = planted_candidate(random)
        points = data[0]
        if len(points) != len(set(points)):
            continue
        try:
            pair_sums, distances = pair_tables(points)
        except ValueError:
            continue
        break
    else:
        raise AssertionError("one-fibre finite-avoidance search exhausted")

    points, first_anchor, source_pairs, target_pairs, horizontal_count = data
    k = len(points)
    edge_count = len(distances)
    anchor = (first_anchor, first_anchor + 1)
    q = subtract(points[anchor[0]], points[anchor[1]])
    target_gap = -100
    source_gap = -18 * target_gap

    fibres = clean_start_fibres(points)
    source_starts: list[tuple[Point, Point]] = []
    for source_pair in source_pairs:
        starts = tuple(
            add(points[edge[0]], points[edge[1]]) for edge in source_pair
        )
        source_starts.append(starts)
        common_translations = {
            translation
            for translation, fibre in fibres.items()
            if starts[0] in fibre and starts[1] in fibre
        }
        assert common_translations == {q}
        assert distance2(points[source_pair[0][0]], points[source_pair[0][1]]) - distance2(
            points[source_pair[1][0]], points[source_pair[1][1]]
        ) == source_gap

    assert q in fibres
    assert set(sum(source_starts, ())) <= set(fibres[q])
    prescribed_fibre_size = 2 * PAIR_RECORDS
    assert len(fibres[q]) == prescribed_fibre_size

    pair_sum_edges = {pair_sum: tuple(edge) for pair_sum, edge in pair_sums.items()}
    for starts, targets in zip(source_starts, target_pairs):
        for start, target in zip(starts, targets):
            assert set(pair_sum_edges[add(start, q)]) == set(target)
            assert len({*anchor, *pair_sum_edges[start], *target}) == 6
        assert set(targets[0]).isdisjoint(targets[1])

    # Exact determinant-qualified richness from the two perpendicular
    # channels attached to every horizontal point.
    edges = edge_data(points)
    target_load: Counter[int] = Counter()
    for first in edges:
        for second in edges:
            gap = first[0] - second[0]
            if gap and abs(2 * determinant(first[2], second[2])) > edge_count:
                target_load[gap] += 1
    assert target_load[target_gap] >= 2 * horizontal_count == k

    origin = horizontal_count + VERTICAL_MARKS.index(0)
    vertical_ten = horizontal_count + VERTICAL_MARKS.index(10)
    fixed_first = tuple(sorted((origin, 0)))
    fixed_second = tuple(sorted((origin, 1)))
    partner_first = tuple(sorted((vertical_ten, 0)))
    partner_second = tuple(sorted((vertical_ten, 1)))
    fixed_shift_first = distance2(points[fixed_first[0]], points[fixed_first[1]]) - distance2(
        points[partner_first[0]], points[partner_first[1]]
    )
    fixed_shift_second = distance2(points[fixed_second[0]], points[fixed_second[1]]) - distance2(
        points[partner_second[0]], points[partner_second[1]]
    )
    assert fixed_shift_first == fixed_shift_second == target_gap
    fixed_gap = distance2(points[fixed_first[0]], points[fixed_first[1]]) - distance2(
        points[fixed_second[0]], points[fixed_second[1]]
    )
    partner_gap = distance2(points[partner_first[0]], points[partner_first[1]]) - distance2(
        points[partner_second[0]], points[partner_second[1]]
    )
    assert fixed_gap == partner_gap

    for fixed, partner in (
        (fixed_first, partner_first),
        (fixed_second, partner_second),
    ):
        fixed_vector = subtract(points[fixed[0]], points[fixed[1]])
        partner_vector = subtract(points[partner[0]], points[partner[1]])
        assert abs(2 * determinant(fixed_vector, partner_vector)) > edge_count

    # In the singleton collection Q={q}, every planted source pair has one
    # isolated anchor and is selected by the displayed physical wedge.
    isolated_mass = PAIR_RECORDS
    translation_excess = isolated_mass - 1
    one_free_rich_lift = translation_excess * target_load[target_gap]
    adaptive_quota = k * k
    adaptive_tail = max(0, isolated_mass - adaptive_quota)
    assert prescribed_fibre_size < k

    return (
        attempt,
        k,
        edge_count,
        horizontal_count,
        len(fibres[q]),
        isolated_mass,
        translation_excess,
        target_load[target_gap],
        one_free_rich_lift,
        adaptive_quota,
        adaptive_tail,
        target_gap,
        source_gap,
        max(max(abs(x), abs(y)) for x, y in points),
    )


def closure_excess_profile(size: int) -> tuple[int, ...]:
    detailed = closure_profile(POINTS[:size], detailed=True)
    # Base tuple has 14 entries.  The detailed suffix records the one-free
    # and adaptive-quota decompositions of the isolated translation mass.
    (
        active_translations,
        excess,
        maximum_load,
        active_mass,
        failures,
        maximum_scaled,
        excess_rich_lift,
        adaptive_quota_total,
        adaptive_tail_count,
        adaptive_tail_lift,
    ) = detailed[14:]
    return (
        size,
        detailed[1],
        detailed[3],
        active_translations,
        excess,
        maximum_load,
        active_mass,
        failures,
        maximum_scaled,
        excess_rich_lift,
        adaptive_quota_total,
        adaptive_tail_count,
        adaptive_tail_lift,
    )


def main() -> None:
    expected_closure = {
        20: (20, 648, 8, 5, 3, 2, 15, 3, 10_000_000, 60, 12, 0, 0),
        30: (
            30, 3_816, 57, 48, 9, 2, 344, 9, 5_000_000, 416, 107, 0, 0,
        ),
        40: (
            40, 12_420, 224, 172, 52, 4, 2_211, 42, 13_333_333,
            3_157, 367, 9, 523,
        ),
        50: (
            50, 26_532, 523, 420, 103, 4, 6_880, 83, 8_823_529,
            7_503, 842, 15, 1_073,
        ),
    }
    for size, wanted in expected_closure.items():
        actual = closure_excess_profile(size)
        assert actual == wanted, (size, actual, wanted)
        print(f"closure-{size} translation excess", actual)

    planted = planted_profile()
    expected_planted = (
        1, 64, 2_016, 32, 6, 3, 2, 64, 128, 4_096, 0,
        -100, 1_800, 3_390_400_526_073,
    )
    assert planted == expected_planted, (planted, expected_planted)
    print("one-q isolated scalar pencil", planted)
    print("low-band isolated translation-excess gate: PASS")


if __name__ == "__main__":
    main()
