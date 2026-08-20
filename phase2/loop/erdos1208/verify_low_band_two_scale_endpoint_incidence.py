#!/usr/bin/env python3
"""Exact endpoint/circle/line identities for the low-band two-scale sum."""

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
from verify_metric_scalar_gap_codegree_barrier import perpendicular_gap_family
from verify_single_fibre_replacement_transition_barrier import (
    add,
    pair_tables,
)


Point = tuple[int, int]
RANDOM_SEED = 1208


def two_scale_profile(points: list[Point], cutoff: int) -> tuple[int, ...]:
    edges = edge_data(points)
    gap_loads = Counter(
        first[0] - second[0] for first in edges for second in edges
    )
    records: dict[int, list[tuple[int, int]]] = defaultdict(list)
    endpoint_records: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
    target_loads: Counter[int] = Counter()

    for first_index, first in enumerate(edges):
        for second_index, second in enumerate(edges):
            gap = first[0] - second[0]
            if not gap:
                continue
            if abs(2 * determinant(first[2], second[2])) <= cutoff:
                continue
            records[gap].append((first_index, second_index))
            target_loads[gap] += 1
            for endpoint in first[1]:
                endpoint_records[gap, endpoint].append((first_index, second_index))

    wedge_loads: Counter[int] = Counter()
    weighted_line_lift = 0
    for (gap, common_endpoint), local_records in endpoint_records.items():
        # Projection to the first edge is injective for a fixed gap.
        assert len({first for first, _ in local_records}) == len(local_records)
        for (first, partner), (other_first, other_partner) in combinations(
            local_records, 2
        ):
            first_data = edges[first]
            other_first_data = edges[other_first]
            partner_data = edges[partner]
            other_partner_data = edges[other_partner]

            # Subtracting the two equal-gap equations gives the exact line
            # equation for the common endpoint.
            assert (
                first_data[0] - other_first_data[0]
                == partner_data[0] - other_partner_data[0]
            )
            first_other = next(
                vertex for vertex in first_data[1] if vertex != common_endpoint
            )
            second_other = next(
                vertex for vertex in other_first_data[1] if vertex != common_endpoint
            )
            x = points[common_endpoint]
            a = points[first_other]
            b = points[second_other]
            right_gap = partner_data[0] - other_partner_data[0]
            assert (
                2 * (x[0] * (b[0] - a[0]) + x[1] * (b[1] - a[1]))
                == right_gap - (a[0] * a[0] + a[1] * a[1])
                + (b[0] * b[0] + b[1] * b[1])
            )
            wedge_loads[gap] += 1
            weighted_line_lift += gap_loads[-18 * gap]

    scalar_mass = sum(
        gap_loads[-18 * gap] * load for gap, load in target_loads.items()
    )
    joint_wedge_mass = sum(
        gap_loads[-18 * gap] * load for gap, load in wedge_loads.items()
    )

    # Each first edge gives exactly its two endpoint-circle incidences.
    weighted_circle_incidence = sum(
        2 * gap_loads[-18 * gap] * len(gap_records)
        for gap, gap_records in records.items()
    )
    assert weighted_circle_incidence == 2 * scalar_mass
    assert weighted_line_lift == joint_wedge_mass

    return (
        len(points),
        len(edges),
        cutoff,
        max(target_loads.values(), default=0),
        len(target_loads),
        scalar_mass,
        joint_wedge_mass,
        max(wedge_loads.values(), default=0),
        sum(wedge_loads.values()),
    )


def sharp_pencil_candidate() -> tuple[list[Point], int, int, int]:
    """Combine a quadratic source gap with a determinant-rich target star."""
    length = 4
    target_records = 6
    source_points, base_gap, source_load = perpendicular_gap_family(length)
    points = [(12 * x, 12 * y) for x, y in source_points]
    source_gap = 144 * base_gap
    target_gap = -source_gap // 18
    assert target_gap == -8 * base_gap
    horizontal = 2 * base_gap - 1
    assert -4 * (horizontal + 1) == target_gap

    random = Random(RANDOM_SEED)
    radius = 10**6 * horizontal
    star = (
        random.randint(-radius, radius),
        random.randint(-radius, radius),
    )
    points.append(star)
    for mark in dense_ruler(target_records):
        vertical = 10 * horizontal + 101 * mark
        points.append(add(star, (horizontal, vertical)))
        centre = (
            random.randint(-radius, radius),
            random.randint(-radius, radius),
        )
        points.extend((centre, add(centre, (horizontal + 2, vertical))))

    pair_tables(points)
    return points, source_gap, target_gap, source_load


def sharp_pencil_profile() -> tuple[int, ...]:
    points, source_gap, target_gap, planted_source_load = sharp_pencil_candidate()
    edges = edge_data(points)
    cutoff = len(edges)
    gap_loads = Counter(
        first[0] - second[0] for first in edges for second in edges
    )
    target_records: list[int] = []
    for first, first_data in enumerate(edges):
        for second, second_data in enumerate(edges):
            if first_data[0] - second_data[0] != target_gap:
                continue
            if abs(2 * determinant(first_data[2], second_data[2])) > cutoff:
                target_records.append(first)

    assert gap_loads[source_gap] == planted_source_load == 32
    assert len(target_records) == 6
    degree = Counter(
        endpoint for first in target_records for endpoint in edges[first][1]
    )
    target_wedges = sum(value * (value - 1) // 2 for value in degree.values())
    assert target_wedges == 15
    aligned_scalar_mass = gap_loads[source_gap] * len(target_records)
    aligned_wedge_mass = gap_loads[source_gap] * target_wedges

    full_profile = two_scale_profile(points, cutoff)
    return (
        *full_profile,
        source_gap,
        target_gap,
        gap_loads[source_gap],
        len(target_records),
        target_wedges,
        aligned_scalar_mass,
        aligned_wedge_mass,
    )


def main() -> None:
    expected = {
        "closure-20": (20, 190, 190, 26, 6_672, 28_994, 37_904, 71, 21_439),
        "Costas-22": (22, 231, 231, 18, 23_026, 18_380, 9_839, 37, 12_114),
        "parabola-43": (43, 903, 903, 7, 382_400, 16_194, 276, 4, 3_928),
        "ruler-40": (40, 780, 780, 23, 500_450, 8_544, 1_012, 212, 145_881),
    }
    families = [
        ("closure-20", POINTS[:20]),
        ("Costas-22", transformed_costas(23)),
        ("parabola-43", transformed_parabola_43()),
        ("ruler-40", ruler_points()),
    ]
    for name, points in families:
        actual = two_scale_profile(points, len(points) * (len(points) - 1) // 2)
        assert actual == expected[name], (name, actual, expected[name])
        print(name, actual)

    sharp = sharp_pencil_profile()
    expected_sharp = (
        35,
        595,
        595,
        32,
        348_526,
        384,
        480,
        160,
        6_367,
        339_544_467_504,
        -18_863_581_528,
        32,
        6,
        15,
        192,
        480,
    )
    assert sharp == expected_sharp, (sharp, expected_sharp)
    print("sharp source-gap/target-pencil", sharp)
    print("low-band two-scale endpoint incidence: PASS")


if __name__ == "__main__":
    main()
