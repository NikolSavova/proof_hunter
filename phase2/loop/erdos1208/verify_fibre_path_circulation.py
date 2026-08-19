#!/usr/bin/env python3
"""Exact checks for the path--cycle structure of #1208 fibres."""

from __future__ import annotations

from collections import defaultdict

from search_rotated_support import is_distance_sidon
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Record = tuple[Point, Point, Point]


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def scale(multiplier: int, point: Point) -> Point:
    return multiplier * point[0], multiplier * point[1]


def point_sum(points) -> Point:
    answer = (0, 0)
    for point in points:
        answer = add(answer, point)
    return answer


def norm_squared(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def fibres(points: list[Point]) -> dict[Point, list[Record]]:
    answer: dict[Point, list[Record]] = defaultdict(list)
    for p in points:
        for r in points:
            for q in points:
                if r == q:
                    continue
                answer[add(p, rotate(subtract(r, q)))].append((p, r, q))
    return answer


def verify_fibre(output: Point, records: list[Record], side: int) -> tuple[int, int]:
    p_set = {record[0] for record in records}
    r_set = {record[1] for record in records}
    q_set = {record[2] for record in records}
    size = len(records)
    assert len(p_set) == len(r_set) == len(q_set) == size

    successors: dict[Point, tuple[Point, Point]] = {}
    predecessors: dict[Point, tuple[Point, Point]] = {}
    for p, r, q in records:
        assert q not in successors
        assert r not in predecessors
        successors[q] = (r, p)
        predecessors[r] = (q, p)

    starts = q_set - r_set
    ends = r_set - q_set
    defect = len(starts)
    assert len(ends) == defect

    left = scale(size, output)
    right = add(point_sum(p_set), rotate(subtract(point_sum(ends), point_sum(starts))))
    assert left == right

    centered = subtract(left, point_sum(p_set))
    assert norm_squared(centered) <= 2 * defect * defect * side * side

    used_tails: set[Point] = set()
    component_count = 0

    for start in starts:
        current = start
        labels: list[Point] = []
        while current in successors:
            assert current not in used_tails
            used_tails.add(current)
            current, label = successors[current]
            labels.append(label)
        assert current in ends
        component_count += 1
        path_left = scale(len(labels), output)
        path_right = add(point_sum(labels), rotate(subtract(current, start)))
        assert path_left == path_right

    for start in q_set:
        if start in used_tails:
            continue
        current = start
        labels = []
        while True:
            assert current in successors
            assert current not in used_tails
            used_tails.add(current)
            current, label = successors[current]
            labels.append(label)
            if current == start:
                break
        assert len(labels) >= 2
        component_count += 1
        assert scale(len(labels), output) == point_sum(labels)

    assert len(used_tails) == size
    assert component_count >= defect
    return size, size - defect


def main() -> None:
    points = POINTS[:20]
    assert is_distance_sidon(points)
    side = max(
        max(point[coordinate] for point in points)
        - min(point[coordinate] for point in points)
        for coordinate in (0, 1)
    )
    table = fibres(points)
    profile = [verify_fibre(output, records, side) for output, records in table.items()]

    circulation = sum(second for _, second in profile)
    size = len(points)
    assert circulation <= size * (size - 1) ** 2

    print(
        "fibre path circulation",
        (size, len(table), max(first for first, _ in profile), circulation),
    )
    print("fibre path circulation: PASS")


if __name__ == "__main__":
    main()
