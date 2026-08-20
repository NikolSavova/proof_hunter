#!/usr/bin/env python3
"""Exact fixed-endpoint-wedge weights for the low scalar band."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
from random import Random

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_ambient_cross_sum_energy_gate import ruler_points
from verify_dilated_internal_pair_sum_charge import transformed_parabola_43
from verify_gaussian_edge_vector_two_arm_barrier import dense_ruler
from verify_metric_scalar_endpoint_rich_tail import (
    POINTS,
    determinant,
    edge_data,
)
from verify_single_fibre_replacement_transition_barrier import add, pair_tables


Point = tuple[int, int]
RANDOM_SEED = 1208


def fixed_wedge_profile(points: list[Point], cutoff: int) -> tuple[int, ...]:
    edges = edge_data(points)
    gap_loads = Counter(
        first[0] - second[0] for first in edges for second in edges
    )
    endpoint_records: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    target_loads: Counter[int] = Counter()
    for first_index, first in enumerate(edges):
        for second_index, second in enumerate(edges):
            gap = first[0] - second[0]
            if not gap:
                continue
            if abs(2 * determinant(first[2], second[2])) <= cutoff:
                continue
            target_loads[gap] += 1
            for endpoint in first[1]:
                endpoint_records[gap, endpoint].append((first_index, second_index))

    fixed_weights: Counter[tuple[int, int, int]] = Counter()
    rich_fixed_weights: Counter[tuple[int, int, int]] = Counter()
    target_wedge_lifts = 0
    for (gap, endpoint), local_records in endpoint_records.items():
        assert len({first for first, _ in local_records}) == len(local_records)
        for (first, _), (second, _) in combinations(local_records, 2):
            physical_wedge = endpoint, *sorted((first, second))
            weight = gap_loads[-18 * gap]
            if weight:
                fixed_weights[physical_wedge] += weight
                if target_loads[gap] >= len(points):
                    rich_fixed_weights[physical_wedge] += weight
            target_wedge_lifts += 1

    joint_wedge_mass = sum(fixed_weights.values())
    return (
        len(points),
        len(edges),
        cutoff,
        len(fixed_weights),
        joint_wedge_mass,
        max(fixed_weights.values(), default=0),
        sum(weight * weight for weight in fixed_weights.values()),
        target_wedge_lifts,
        len(rich_fixed_weights),
        sum(rich_fixed_weights.values()),
        max(rich_fixed_weights.values(), default=0),
    )


def polynomial_sharp_candidate(size: int = 8) -> tuple[list[Point], int, int]:
    """A polynomial-height wedge with fixed weight exactly `size`."""
    horizontal = size**3 + 10
    first_mark = 18 * (horizontal + 1) + 1
    second_mark = 18 * (horizontal + 1) - 1
    source_gap = first_mark * first_mark - second_mark * second_mark
    target_gap = -4 * (horizontal + 1)
    assert source_gap == -18 * target_gap

    ruler = dense_ruler(size)
    ruler_scale = 5
    vertical_offset = 3 * first_mark
    while True:
        points = [
            (first_mark, 0),
            (second_mark, 0),
            *[(0, vertical_offset + ruler_scale * mark) for mark in ruler],
        ]
        try:
            pair_tables(points)
            break
        except ValueError:
            vertical_offset += 1

    random = Random(RANDOM_SEED)
    radius = 10**12
    for _ in range(100):
        candidate = list(points)
        star = (
            random.randint(-radius, radius),
            random.randint(-radius, radius),
        )
        candidate.append(star)
        for vertical in (1_000_123, 2_000_789):
            candidate.append(add(star, (horizontal, vertical)))
            centre = (
                random.randint(-radius, radius),
                random.randint(-radius, radius),
            )
            candidate.extend((centre, add(centre, (horizontal + 2, vertical))))
        try:
            pair_tables(candidate)
            return candidate, source_gap, target_gap
        except ValueError:
            continue
    raise AssertionError("finite-avoidance search exhausted")


def polynomial_sharp_profile() -> tuple[int, ...]:
    points, source_gap, target_gap = polynomial_sharp_candidate()
    edges = edge_data(points)
    cutoff = len(edges)
    gap_loads = Counter(
        first[0] - second[0] for first in edges for second in edges
    )

    endpoint_records: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    for first_index, first in enumerate(edges):
        for second_index, second in enumerate(edges):
            gap = first[0] - second[0]
            if gap != target_gap:
                continue
            if abs(2 * determinant(first[2], second[2])) <= cutoff:
                continue
            for endpoint in first[1]:
                endpoint_records[gap, endpoint].append((first_index, second_index))

    planted_wedges = [
        (endpoint, records)
        for (gap, endpoint), records in endpoint_records.items()
        if gap == target_gap and len(records) == 2
    ]
    assert len(planted_wedges) == 1
    assert gap_loads[source_gap] == 8
    full_profile = fixed_wedge_profile(points, cutoff)
    return (
        *full_profile,
        source_gap,
        target_gap,
        gap_loads[source_gap],
        len(planted_wedges[0][1]),
    )


def main() -> None:
    expected = {
        "closure-20": (
            20, 190, 190, 1_911, 37_904, 173, 1_623_596, 21_439,
            811, 10_542, 76,
        ),
        "Costas-22": (
            22, 231, 231, 1_893, 9_839, 34, 94_875, 12_114, 0, 0, 0,
        ),
        "parabola-43": (
            43, 903, 903, 184, 276, 5, 586, 3_928, 0, 0, 0,
        ),
        "ruler-40": (
            40, 780, 780, 894, 1_012, 21, 1_796, 145_881, 0, 0, 0,
        ),
    }
    families = [
        ("closure-20", POINTS[:20]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-43", transformed_parabola_43()),
        ("ruler-40", ruler_points()),
    ]
    for name, points in families:
        actual = fixed_wedge_profile(points, len(points) * (len(points) - 1) // 2)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)

    sharp = polynomial_sharp_profile()
    expected_sharp = (
        17,
        136,
        136,
        1,
        8,
        8,
        64,
        117,
        0,
        0,
        0,
        37_656,
        -2_092,
        8,
        2,
    )
    assert sharp == expected_sharp, (sharp, expected_sharp)
    print("polynomial-height sharp wedge", sharp)
    print("low-band fixed-wedge weight: PASS")


if __name__ == "__main__":
    main()
