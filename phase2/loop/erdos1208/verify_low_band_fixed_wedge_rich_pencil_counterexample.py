#!/usr/bin/env python3
"""Polynomial-height rich-pencil obstruction to the fixed-wedge gate."""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from verify_gaussian_edge_vector_two_arm_barrier import dense_ruler
from verify_low_band_fixed_wedge_weight import fixed_wedge_profile
from verify_metric_scalar_endpoint_rich_tail import (
    determinant,
    edge_data,
)
from verify_single_fibre_replacement_transition_barrier import pair_tables


Point = tuple[int, int]
VERTICAL_PATTERN = (10, 24, 26, 35, 55)


def is_golomb(marks: set[int] | list[int]) -> bool:
    differences: set[int] = set()
    for first, second in combinations(sorted(marks), 2):
        difference = second - first
        if difference in differences:
            return False
        differences.add(difference)
    return True


def vertical_identity_ruler(copy_count: int) -> tuple[list[int], list[int]]:
    """Greedily pack homothetic copies of the five-mark identity gadget."""
    marks = {0}
    parameters: list[int] = []
    for _ in range(copy_count):
        for parameter in range(1, 2_000_000):
            candidate = marks | {
                coefficient * parameter for coefficient in VERTICAL_PATTERN
            }
            if len(candidate) == len(marks) + len(VERTICAL_PATTERN) and is_golomb(
                candidate
            ):
                marks = candidate
                parameters.append(parameter)
                break
        else:
            raise AssertionError("vertical finite-avoidance search exhausted")
    return sorted(marks), parameters


def perpendicular_rich_candidate(
    copy_count: int = 3,
) -> tuple[list[Point], list[int], list[int], list[int], int, int]:
    """Build the two-axis family, choosing its two free scales by avoidance."""
    horizontal_count = 6 * copy_count
    vertical_marks, parameters = vertical_identity_ruler(copy_count)
    horizontal_ruler = dense_ruler(horizontal_count)

    vertical_differences = {
        second - first for first, second in combinations(vertical_marks, 2)
    }
    horizontal_differences = {
        second - first for first, second in combinations(horizontal_ruler, 2)
    }
    horizontal_scale = next(
        scale
        for scale in range(1, 2_000_000)
        if not any(
            scale * difference in vertical_differences
            for difference in horizontal_differences
        )
    )

    point_count = horizontal_count + len(vertical_marks)
    edge_count = point_count * (point_count - 1) // 2
    horizontal_offset = max(
        edge_count + 1,
        max(vertical_marks) + 1,
        horizontal_scale * max(horizontal_ruler) + 1,
    )
    for _ in range(2_000_000):
        horizontal_marks = [
            horizontal_offset + horizontal_scale * mark
            for mark in horizontal_ruler
        ]
        points = [
            *((mark, 0) for mark in horizontal_marks),
            *((0, mark) for mark in vertical_marks),
        ]
        try:
            pair_tables(points)
            return (
                points,
                horizontal_marks,
                vertical_marks,
                parameters,
                horizontal_scale,
                horizontal_offset,
            )
        except ValueError:
            horizontal_offset += 1
    raise AssertionError("horizontal finite-avoidance search exhausted")


def rich_pencil_profile(copy_count: int = 3) -> tuple[int, ...]:
    (
        points,
        horizontal_marks,
        vertical_marks,
        parameters,
        horizontal_scale,
        horizontal_offset,
    ) = perpendicular_rich_candidate(copy_count)
    pair_sums, distances = pair_tables(points)
    edges = edge_data(points)
    point_count = len(points)
    edge_count = len(edges)
    horizontal_count = len(horizontal_marks)
    origin = horizontal_count + vertical_marks.index(0)

    edge_index = {tuple(sorted(edge[1])): index for index, edge in enumerate(edges)}
    gap_loads = Counter(
        first[0] - second[0] for first in edges for second in edges
    )
    target_loads: Counter[int] = Counter()
    for first in edges:
        for second in edges:
            gap = first[0] - second[0]
            if gap and abs(2 * determinant(first[2], second[2])) > edge_count:
                target_loads[gap] += 1

    first_edge_indices = [
        edge_index[tuple(sorted((horizontal, origin)))]
        for horizontal in range(horizontal_count)
    ]
    fixed_first, fixed_second = first_edge_indices[:2]
    first_data = edges[fixed_first]
    second_data = edges[fixed_second]
    fixed_gap = first_data[0] - second_data[0]

    exact_fixed_weight = 0
    for partner_first in edges:
        for partner_second in edges:
            if partner_first[0] - partner_second[0] != fixed_gap:
                continue
            if (
                abs(2 * determinant(first_data[2], partner_first[2]))
                <= edge_count
                or abs(2 * determinant(second_data[2], partner_second[2]))
                <= edge_count
            ):
                continue
            shift = first_data[0] - partner_first[0]
            if target_loads[shift] >= point_count:
                exact_fixed_weight += gap_loads[-18 * shift]

    source_loads: list[int] = []
    target_richness: list[int] = []
    for parameter in parameters:
        y_mark = 10 * parameter
        low_mark = 24 * parameter
        high_mark = 26 * parameter
        source_high_mark = 55 * parameter
        source_low_mark = 35 * parameter
        shift = -(y_mark * y_mark)
        source_gap = -18 * shift
        assert low_mark * low_mark - high_mark * high_mark == shift
        assert (
            source_high_mark * source_high_mark
            - source_low_mark * source_low_mark
            == source_gap
        )

        for horizontal in range(horizontal_count):
            natural_first = edges[
                edge_index[tuple(sorted((horizontal, origin)))]
            ]
            y_vertex = horizontal_count + vertical_marks.index(y_mark)
            natural_second = edges[
                edge_index[tuple(sorted((horizontal, y_vertex)))]
            ]
            low_vertex = horizontal_count + vertical_marks.index(low_mark)
            high_vertex = horizontal_count + vertical_marks.index(high_mark)
            second_channel_first = edges[
                edge_index[tuple(sorted((horizontal, low_vertex)))]
            ]
            second_channel_second = edges[
                edge_index[tuple(sorted((horizontal, high_vertex)))]
            ]
            assert natural_first[0] - natural_second[0] == shift
            assert second_channel_first[0] - second_channel_second[0] == shift
            assert abs(2 * determinant(natural_first[2], natural_second[2])) > edge_count
            assert (
                abs(
                    2
                    * determinant(
                        second_channel_first[2], second_channel_second[2]
                    )
                )
                > edge_count
            )

            source_high_vertex = horizontal_count + vertical_marks.index(
                source_high_mark
            )
            source_low_vertex = horizontal_count + vertical_marks.index(
                source_low_mark
            )
            source_first = edges[
                edge_index[tuple(sorted((horizontal, source_high_vertex)))]
            ]
            source_second = edges[
                edge_index[tuple(sorted((horizontal, source_low_vertex)))]
            ]
            assert source_first[0] - source_second[0] == source_gap

        source_loads.append(gap_loads[source_gap])
        target_richness.append(target_loads[shift])

    assert min(source_loads) >= horizontal_count
    assert min(target_richness) >= 2 * horizontal_count >= point_count
    planted_fixed_lower_bound = copy_count * horizontal_count
    assert exact_fixed_weight >= planted_fixed_lower_bound

    full_profile = fixed_wedge_profile(points, edge_count)
    global_planted_lower_bound = (
        horizontal_count
        * (horizontal_count - 1)
        // 2
        * planted_fixed_lower_bound
    )
    assert full_profile[9] >= global_planted_lower_bound

    return (
        copy_count,
        point_count,
        edge_count,
        horizontal_scale,
        horizontal_offset,
        max(max(abs(x), abs(y)) for x, y in points),
        len(pair_sums),
        len(distances),
        min(source_loads),
        min(target_richness),
        planted_fixed_lower_bound,
        exact_fixed_weight,
        global_planted_lower_bound,
        *full_profile,
    )


def main() -> None:
    actual = rich_pencil_profile()
    expected = (
        3,
        34,
        561,
        17,
        11_051,
        22_101,
        561,
        561,
        19,
        36,
        54,
        57,
        8_262,
        34,
        561,
        561,
        1_639,
        38_162,
        57,
        1_081_840,
        77_000,
        1_638,
        36_936,
        57,
    )
    assert actual == expected, (actual, expected)
    print("polynomial rich perpendicular pencil", actual)
    print("low-band fixed-wedge rich-pencil counterexample: PASS")


if __name__ == "__main__":
    main()
