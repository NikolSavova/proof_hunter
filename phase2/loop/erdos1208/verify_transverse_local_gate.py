#!/usr/bin/env python3
"""Exact checks for TRANSVERSE_LOCAL_GATE.md.

The script uses only integer arithmetic.  It verifies the local/global edge
identity, the quarter-turn identity, the parallel-line cover bound, and the
stored transverse four-cycle counts.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from search_rotated_support import perpendicular_seed
from verify_adversarial_support_witnesses import EXPECTED, WITNESSES


Point = tuple[int, int]


EXPECTED_LOCAL = {
    12: (17, 2416),
    16: (24, 6315),
    20: (35, 19733),
    24: (38, 25280),
    28: (38, 35326),
}


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def subtract(left: Point, right: Point) -> Point:
    return left[0] - right[0], left[1] - right[1]


def differences(points: list[Point]) -> set[Point]:
    return {subtract(left, right) for left in points for right in points}


def transverse_graph(points: list[Point]) -> tuple[list[Point], list[set[int]]]:
    labels = sorted(differences(points))
    label_set = set(labels)
    adjacency = [set() for _ in labels]
    for right, d_prime in enumerate(labels):
        for left, d in enumerate(labels[:right]):
            delta = subtract(d_prime, d)
            if rotate(delta) not in label_set:
                continue
            if d[0] * d_prime[1] - d[1] * d_prime[0] == 0:
                continue
            adjacency[left].add(right)
            adjacency[right].add(left)
    return labels, adjacency


def four_cycles(adjacency: list[set[int]]) -> int:
    common_pair_counts: Counter[tuple[int, int]] = Counter()
    for neighbours in adjacency:
        for pair in combinations(sorted(neighbours), 2):
            common_pair_counts[pair] += 1
    # Choosing two common neighbours counts a C4 once for each of its two
    # pairs of opposite vertices.
    return sum(value * (value - 1) // 2 for value in common_pair_counts.values()) // 2


def local_overlap(d: Point, label_set: set[Point]) -> int:
    answer = 0
    for e in label_set:
        if e == (0, 0) or d[0] * e[0] + d[1] * e[1] == 0:
            continue
        je = rotate(e)
        if (d[0] - je[0], d[1] - je[1]) in label_set:
            answer += 1
    return answer


def primitive_direction(vector: Point) -> Point:
    from math import gcd

    divisor = gcd(abs(vector[0]), abs(vector[1]))
    x, y = vector[0] // divisor, vector[1] // divisor
    if x < 0 or (x == 0 and y < 0):
        x, y = -x, -y
    return x, y


def verify_line_cover_bound(points: list[Point]) -> int:
    label_set = differences(points)
    maximum_overlap = max(
        sum(
            1
            for e in label_set
            if e != (0, 0)
            and (
                d[0] - rotate(e)[0],
                d[1] - rotate(e)[1],
            )
            in label_set
        )
        for d in label_set
    )
    directions = {
        primitive_direction(subtract(points[i], points[j]))
        for i in range(len(points))
        for j in range(i)
    }
    checks = 0
    for vx, vy in directions:
        heights = {vx * y - vy * x for x, y in points}
        height_differences = {left - right for left in heights for right in heights}
        bound = len(height_differences) ** 2
        assert maximum_overlap <= bound
        checks += 1
    return checks


def verify_instance(points: list[Point], expected_e: int, expected_local: int, expected_c4: int) -> int:
    labels, adjacency = transverse_graph(points)
    label_set = set(labels)
    edge_count = sum(map(len, adjacency)) // 2
    local_values = [local_overlap(d, label_set) for d in labels]
    assert sum(local_values) == 2 * edge_count
    assert edge_count == expected_e
    assert max(local_values) == expected_local
    assert four_cycles(adjacency) == expected_c4

    for d in labels:
        for e in labels:
            je = rotate(e)
            d_prime = d[0] - je[0], d[1] - je[1]
            determinant = d[0] * d_prime[1] - d[1] * d_prime[0]
            dot_product = d[0] * e[0] + d[1] * e[1]
            assert determinant == -dot_product

            value = e
            for _ in range(4):
                jvalue = rotate(value)
                value = d[0] - jvalue[0], d[1] - jvalue[1]
            assert value == e

    return verify_line_cover_bound(points)


def main() -> None:
    line_checks = 0
    for k, points in WITNESSES.items():
        expected_e = EXPECTED[k][2]
        expected_local, expected_c4 = EXPECTED_LOCAL[k]
        line_checks += verify_instance(points, expected_e, expected_local, expected_c4)
        print(k, expected_e, expected_local, expected_c4)

    for k in (8, 12, 16, 20):
        points = perpendicular_seed(k)
        labels = differences(points)
        assert max(local_overlap(d, labels) for d in labels) == 0

    print("line-cover checks", line_checks)
    print("PASS")


if __name__ == "__main__":
    main()
