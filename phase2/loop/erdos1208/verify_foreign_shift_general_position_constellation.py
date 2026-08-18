#!/usr/bin/env python3
"""Exact 137-point general-position stress test for the rich-triangle tail.

The core is the transformed p=127 Welch Costas array.  Eleven anchor
parameters have no three collinear, are vector-Sidon, and have difference
spectrum disjoint from the core.  Every one of their 165 triangles has at
least 1,709 translated copies in the core difference set.  The full
137-point configuration is distance-Sidon and has maximum collinearity four.
"""

from itertools import combinations
from math import comb, gcd


P = 127
G = 3
SHEAR = 93
STRETCH = 94
TRANSLATION = (101, 10_201)

ANCHOR_PARAMETERS = [
    (0, 0),
    (16, -23),
    (-30, -33),
    (-12, 25),
    (20, 0),
    (-8, 25),
    (29, -27),
    (-30, -24),
    (29, 18),
    (-34, 4),
    (20, 33),
]


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[0], x[1] - y[1]


def quarter_turn(x: tuple[int, int]) -> tuple[int, int]:
    return -x[1], x[0]


def transform(x: tuple[int, int]) -> tuple[int, int]:
    return x[0] + SHEAR * x[1], STRETCH * x[1]


def norm2(x: tuple[int, int]) -> int:
    return x[0] * x[0] + x[1] * x[1]


def determinant(u: tuple[int, int], v: tuple[int, int]) -> int:
    return u[0] * v[1] - u[1] * v[0]


def difference_set(points: list[tuple[int, int]]) -> set[tuple[int, int]]:
    return {sub(x, y) for x in points for y in points if x != y}


def assert_distance_sidon(points: list[tuple[int, int]]) -> None:
    assert len(set(points)) == len(points)
    seen: set[int] = set()
    for i, x in enumerate(points):
        for y in points[:i]:
            value = norm2(sub(x, y))
            assert value > 0
            assert value not in seen
            seen.add(value)
    assert len(seen) == comb(len(points), 2)


def maximum_collinearity(points: list[tuple[int, int]]) -> int:
    lines: set[tuple[int, int, int]] = set()
    for i, x in enumerate(points):
        for y in points[:i]:
            dx, dy = sub(x, y)
            divisor = gcd(abs(dx), abs(dy))
            dx //= divisor
            dy //= divisor
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy
            constant = dy * x[0] - dx * x[1]
            lines.add((dx, dy, constant))
    return max(
        sum(dy * x[0] - dx * x[1] == constant for x in points)
        for dx, dy, constant in lines
    )


def triple_correlation(
    differences: set[tuple[int, int]],
    u: tuple[int, int],
    v: tuple[int, int],
) -> int:
    return sum(
        add(x, u) in differences and add(x, v) in differences
        for x in differences
    )


def main() -> None:
    # 126 = 2 * 3^2 * 7, so these tests prove that G is primitive mod P.
    assert all(pow(G, (P - 1) // q, P) != 1 for q in (2, 3, 7))
    welch = [(i, pow(G, i, P)) for i in range(P - 1)]
    core = [transform(x) for x in welch]
    core_differences = difference_set(welch)
    assert len(core_differences) == 126 * 125

    anchor_differences = difference_set(ANCHOR_PARAMETERS)
    assert len(anchor_differences) == 11 * 10
    assert not (core_differences & anchor_differences)
    for a, b, c in combinations(ANCHOR_PARAMETERS, 3):
        assert determinant(sub(b, a), sub(c, a)) != 0

    transformed_parameters = [transform(u) for u in ANCHOR_PARAMETERS]
    anchor_offsets = [
        tuple(-coordinate for coordinate in quarter_turn(u))
        for u in transformed_parameters
    ]
    anchors = [add(TRANSLATION, offset) for offset in anchor_offsets]
    points = core + anchors

    assert len(points) == 137
    assert_distance_sidon(points)
    assert maximum_collinearity(points) == 4

    values: list[int] = []
    for i, j, k in combinations(range(len(ANCHOR_PARAMETERS)), 3):
        a = ANCHOR_PARAMETERS[i]
        u = sub(ANCHOR_PARAMETERS[j], a)
        v = sub(ANCHOR_PARAMETERS[k], a)
        value = triple_correlation(core_differences, u, v)
        values.append(value)

        anchor_a = anchors[i]
        assert quarter_turn(sub(anchors[j], anchor_a)) == transform(u)
        assert quarter_turn(sub(anchors[k], anchor_a)) == transform(v)

    assert len(values) == 165
    assert min(values) == 1_709
    assert max(values) == 3_457
    assert sum(values) == 424_918

    ordered_contribution = 6 * sum(values)
    assert ordered_contribution == 2_549_508

    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    print("points", len(points))
    print("unordered distances", comb(len(points), 2))
    print("maximum collinearity", maximum_collinearity(points))
    print("non-collinear anchor triangles", len(values))
    print("minimum/maximum codegree", min(values), max(values))
    print("ordered non-collinear moment contribution", ordered_contribution)
    print("contribution / points^3", ordered_contribution / len(points) ** 3)
    print("bounding box", min(xs), max(xs), min(ys), max(ys))


if __name__ == "__main__":
    main()
