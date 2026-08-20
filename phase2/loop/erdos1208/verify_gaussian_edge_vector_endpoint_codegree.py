#!/usr/bin/env python3
"""Exact checks for GAUSSIAN_EDGE_VECTOR_ENDPOINT_CODEGREE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations

from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_dilated_internal_pair_sum_charge import (
    clean_start_fibres,
    transformed_parabola_43,
)
from verify_gaussian_edge_vector_charge import add, dilation, subtract
from verify_gaussian_edge_vector_two_arm_barrier import (
    choose_translation,
    dense_ruler,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
EndpointPair = tuple[Point, Point]
CleanDecoration = tuple[Point, Point, Point, Point]
CollisionRow = tuple[Point, ...]
Pattern = tuple[int, ...]
Profile = tuple[int, int, int, int, int, int]


COEFFICIENTS: tuple[Point, ...] = (
    (1, 0),
    (-1, 0),
    (0, 0),
    (0, 0),
    (-1, 0),
    (1, 0),
    (0, 0),
    (0, 0),
    (3, 3),
    (-3, -3),
    (-3, -3),
    (3, 3),
)


def pair_sum_map(points: list[Point]) -> dict[Point, EndpointPair]:
    output: dict[Point, EndpointPair] = {}
    for first, second in combinations(points, 2):
        left, right = sorted((first, second))
        pair_sum = add(left, right)
        assert pair_sum not in output
        output[pair_sum] = left, right
    return output


def edge_vector(edge: EndpointPair) -> Point:
    return subtract(edge[0], edge[1])


def equality_pattern(row: CollisionRow) -> Pattern:
    block_by_label: dict[Point, int] = {}
    pattern = []
    for label in row:
        if label not in block_by_label:
            block_by_label[label] = len(block_by_label)
        pattern.append(block_by_label[label])
    return tuple(pattern)


def active_blocks(pattern: Pattern) -> tuple[int, ...]:
    totals: dict[int, Point] = defaultdict(lambda: (0, 0))
    for block, coefficient in zip(pattern, COEFFICIENTS):
        totals[block] = add(totals[block], coefficient)
    assert add_all(totals.values()) == (0, 0)
    return tuple(block for block, total in totals.items() if total != (0, 0))


def add_all(values) -> Point:
    total = (0, 0)
    for value in values:
        total = add(total, value)
    return total


def verify_pair_linearity(decorations: list[CleanDecoration]) -> None:
    for first_role, second_role in combinations(range(4), 2):
        seen: dict[tuple[Point, Point], CleanDecoration] = {}
        for decoration in decorations:
            key = decoration[first_role], decoration[second_role]
            assert key not in seen or seen[key] == decoration
            seen[key] = decoration


def resonant_two_arm(side_size: int) -> list[Point]:
    marks = dense_ruler(2 * side_size)
    first_arm, second_arm = marks[:side_size], marks[side_size:]
    translation = choose_translation(first_arm, second_arm)
    return (
        [(mark, 0) for mark in first_arm]
        + [
            (translation[0] - mark, translation[1] - mark)
            for mark in second_arm
        ]
    )


def profile(points: list[Point]) -> Profile:
    k = len(points)
    pair_by_sum = pair_sum_map(points)
    fibres = clean_start_fibres(points)
    q_value = max(fibres, key=lambda value: len(fibres[value]))
    starts = fibres[q_value]
    h = len(starts)

    decorations: list[CleanDecoration] = []
    for start in starts:
        c_value, d_value = pair_by_sum[start]
        e_value, f_value = pair_by_sum[add(start, q_value)]
        decoration = c_value, d_value, e_value, f_value
        assert len(set(decoration)) == 4
        decorations.append(decoration)
    verify_pair_linearity(decorations)

    arbitrary_edges = list(pair_by_sum.values())
    records_by_key: dict[
        Point,
        list[tuple[int, int]],
    ] = defaultdict(list)
    for source_index, decoration in enumerate(decorations):
        source_vector = subtract(decoration[0], decoration[1])
        for target_index, target_edge in enumerate(arbitrary_edges):
            key = add(source_vector, dilation(edge_vector(target_edge)))
            records_by_key[key].append((source_index, target_index))

    rows: list[CollisionRow] = []
    simultaneous_overlap = 0
    difference_set = {
        subtract(first, second)
        for first in points
        for second in points
    }

    for records in records_by_key.values():
        assert len({source for source, _ in records}) == len(records)
        assert len({target for _, target in records}) == len(records)
        for first_record in records:
            for second_record in records:
                if first_record == second_record:
                    continue
                source, target = first_record
                other_source, other_target = second_record
                c_value, d_value, e_value, f_value = decorations[source]
                other_c, other_d, other_e, other_f = decorations[other_source]
                x_value, y_value = arbitrary_edges[target]
                other_x, other_y = arbitrary_edges[other_target]
                row = (
                    c_value,
                    d_value,
                    e_value,
                    f_value,
                    other_c,
                    other_d,
                    other_e,
                    other_f,
                    x_value,
                    y_value,
                    other_x,
                    other_y,
                )
                rows.append(row)

                alpha = subtract(c_value, other_c)
                beta = subtract(d_value, other_d)
                eta = subtract(e_value, other_e)
                theta = subtract(f_value, other_f)
                gamma = subtract(x_value, other_x)
                delta = subtract(y_value, other_y)
                assert add(alpha, beta) == add(eta, theta)
                assert subtract(alpha, beta) == tuple(
                    -coordinate
                    for coordinate in dilation(subtract(gamma, delta))
                )
                assert all(
                    vector in difference_set
                    for vector in (alpha, beta, eta, theta, gamma, delta)
                )

                source_overlap = c_value == other_c or d_value == other_d
                target_overlap = x_value == other_x or y_value == other_y
                if source_overlap and target_overlap:
                    simultaneous_overlap += 1

    off_diagonal = sum(
        len(records) * (len(records) - 1)
        for records in records_by_key.values()
    )
    assert off_diagonal == len(rows)
    assert simultaneous_overlap <= 4 * k * (k - 2) * h

    rows_by_pattern: dict[Pattern, list[CollisionRow]] = defaultdict(list)
    for row in rows:
        pattern = equality_pattern(row)
        assert len(active_blocks(pattern)) >= 3
        rows_by_pattern[pattern].append(row)

    maximum_codegree = 0
    for pattern, pattern_rows in rows_by_pattern.items():
        blocks = active_blocks(pattern)
        # Check every active role-pair, not merely the pair used in the
        # pigeonhole proof of Theorem 6.1.
        representative_role = {
            block: pattern.index(block)
            for block in blocks
        }
        for first_block, second_block in combinations(blocks, 2):
            first_role = representative_role[first_block]
            second_role = representative_role[second_block]
            codegrees = Counter(
                (row[first_role], row[second_role])
                for row in pattern_rows
            )
            maximum_codegree = max(maximum_codegree, max(codegrees.values()))

    return (
        k,
        h,
        off_diagonal,
        len(rows_by_pattern),
        maximum_codegree,
        simultaneous_overlap,
    )


def main() -> None:
    families: list[tuple[str, list[Point], Profile]] = [
        ("closure-30", POINTS[:30], (30, 14, 90, 41, 11, 0)),
        ("closure-40", POINTS[:40], (40, 23, 936, 276, 32, 0)),
        ("closure-80", POINTS[:80], (80, 63, 8_424, 678, 116, 0)),
        (
            "closure-120",
            POINTS[:120],
            (120, 127, 45_960, 995, 436, 236),
        ),
        (
            "Costas-22",
            transformed_costas(23),
            (22, 34, 0, 0, 0, 0),
        ),
        (
            "parabola-image-43",
            transformed_parabola_43(),
            (43, 171, 4_778, 800, 142, 0),
        ),
        (
            "resonant-two-arm-50",
            resonant_two_arm(50),
            (100, 114, 769_052, 470, 5_778, 2_042),
        ),
    ]

    for name, points, expected in families:
        actual = profile(points)
        assert actual == expected, (name, actual, expected)
        print(name, actual)

    print("Gaussian endpoint-codegree gate: PASS")


if __name__ == "__main__":
    main()
