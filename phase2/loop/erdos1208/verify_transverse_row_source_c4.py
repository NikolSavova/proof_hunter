#!/usr/bin/env python3
"""Exact checks for TRANSVERSE_ROW_SOURCE_C4_GATE.md.

The default run checks the targeted 45-point source-degree certificate and
the row--source C4 table through k=40.  ``--extended`` additionally evaluates
the full 122-point row moment; that check is deliberately optional because it
takes roughly half a minute in pure Python.
"""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations

from search_rotated_support import is_distance_sidon
from verify_transverse_closure_witness import POINTS as HEAVY_POINTS
from verify_transverse_local_gate import differences


Point = tuple[int, int]


SOURCE_POINTS: list[Point] = [
    (0, 2), (2, 31), (8, 0), (13, 12), (17, 25), (18, 19),
    (20, 18), (24, 29), (29, 40), (35, 7), (36, 8), (39, 9),
    (41, 9), (46, 0), (46, 1), (50, 25), (21, -11), (-9, -15),
    (28, -42), (-33, 29), (86, 30), (34, -76), (90, 40),
    (94, 44), (-23, 81), (102, 12), (84, -88), (66, -78),
    (36, -109), (97, 78), (145, 69), (100, -103), (7, 117),
    (115, 27), (122, 39), (-73, -60), (-33, -150), (-73, -86),
    (-81, -24), (86, 174), (132, 166), (97, -105), (37, -149),
    (-47, -25), (211, 82),
]

FIXED_V = 14
FIXED_Y = 7
EXTENSION = [(799, 435), (472, -756)]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def edge_map(points: list[Point]) -> dict[Point, tuple[int, int]]:
    return {
        subtract(points[i], points[j]): (i, j)
        for i in range(len(points))
        for j in range(len(points))
    }


def row_sources(points: list[Point]) -> dict[Point, set[int]]:
    """Return the exact K_A neighbourhood of every realized row.

    A source v+Jy is encoded by the integer ``v*k+y``.  Directness of A+JA
    makes this encoding faithful.
    """

    k = len(points)
    edges = edge_map(points)
    labels = set(edges)
    answer: dict[Point, set[int]] = {}
    for row in labels:
        sources: set[int] = set()
        for edge, (x, y) in edges.items():
            if edge == (0, 0) or row[0] * edge[0] + row[1] * edge[1] == 0:
                continue
            image = subtract(row, rotate(edge))
            if image not in edges:
                continue
            _, v = edges[image]
            sources.add(v * k + y)
        answer[row] = sources
    return answer


def source_degree(points: list[Point], v: int, y: int) -> int:
    source = v * len(points) + y
    return sum(source in neighbours for neighbours in row_sources(points).values())


def four_cycles_from_rows(rows: dict[Point, set[int]]) -> int:
    common: Counter[int] = Counter()
    right_size = 1 + max((source for values in rows.values() for source in values), default=0)
    for sources in rows.values():
        for left, right in combinations(sorted(sources), 2):
            common[left * right_size + right] += 1
    return sum(value * (value - 1) // 2 for value in common.values())


def verify_source_certificate() -> None:
    assert len(SOURCE_POINTS) == 45
    assert is_distance_sidon(SOURCE_POINTS)
    assert SOURCE_POINTS[FIXED_V] == (46, 1)
    assert SOURCE_POINTS[FIXED_Y] == (24, 29)
    assert source_degree(SOURCE_POINTS, FIXED_V, FIXED_Y) == 250
    print("source certificate", len(SOURCE_POINTS), 250)


def verify_c4_table() -> None:
    expected = {
        16: 3_349,
        20: 33_067,
        30: 716_180,
        40: 4_284_047,
    }
    for k, target in expected.items():
        points = HEAVY_POINTS[:k]
        assert is_distance_sidon(points)
        value = four_cycles_from_rows(row_sources(points))
        assert value == target
        print("row-source C4", k, value)


def verify_extended_profile() -> None:
    points = HEAVY_POINTS + EXTENSION
    assert len(points) == 122
    assert is_distance_sidon(points)
    label_set = differences(points)
    labels = list(label_set)
    rotated = [rotate(edge) for edge in labels]
    total = 0
    moment = 0
    maximum = 0
    for row in labels:
        degree = sum(
            edge != (0, 0)
            and row[0] * edge[0] + row[1] * edge[1] != 0
            and subtract(row, turned) in label_set
            for edge, turned in zip(labels, rotated)
        )
        total += degree
        moment += degree * degree
        maximum = max(maximum, degree)
    wedge = (moment - total) // 2
    assert len(label_set) == 14_763
    assert (total, moment, maximum, wedge) == (
        2_925_748,
        770_269_576,
        971,
        383_671_914,
    )
    print("extended profile", len(points), total, moment, maximum, wedge)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extended", action="store_true")
    args = parser.parse_args()
    verify_source_certificate()
    verify_c4_table()
    if args.extended:
        verify_extended_profile()
    print("PASS")


if __name__ == "__main__":
    main()
