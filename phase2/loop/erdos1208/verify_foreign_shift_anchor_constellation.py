#!/usr/bin/env python3
"""Exact 139-point stress test for the non-collinear rich-triangle tail.

The core is the transformed p=127 Welch Costas array.  Thirteen anchor
points form two principal lines.  Every one of their 231 non-collinear
triangles has at least 2,281 translated copies in the core difference set.
The full 139-point configuration is nevertheless distance-Sidon.
"""

from itertools import combinations
from math import comb, gcd


P = 127
G = 3
SHEAR = 93
STRETCH = 94
TRANSLATION = (100, 10_000)

ANCHOR_PARAMETERS = [
    (0, 0),
    (-29, 28),
    (-29, -11),
    (22, 0),
    (-29, 3),
    (24, 0),
    (-29, -6),
    (21, 0),
    (7, 0),
    (-29, 21),
    (30, 0),
    (-29, 27),
    (-29, -14),
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


def determinant(u: tuple[int, int], v: tuple[int, int]) -> int:
    return u[0] * v[1] - u[1] * v[0]


def triple_correlation(
    differences: set[tuple[int, int]],
    u: tuple[int, int],
    v: tuple[int, int],
) -> int:
    return sum(
        add(x, u) in differences and add(x, v) in differences
        for x in differences
    )


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


def main() -> None:
    assert all(pow(G, (P - 1) // q, P) != 1 for q in (2, 3, 7))
    welch = [(i, pow(G, i, P)) for i in range(P - 1)]
    core = [transform(x) for x in welch]
    core_differences_untransformed = difference_set(welch)
    assert len(core_differences_untransformed) == 126 * 125
    anchor_parameter_differences = difference_set(ANCHOR_PARAMETERS)
    assert len(anchor_parameter_differences) == 13 * 12
    assert not (core_differences_untransformed & anchor_parameter_differences)

    transformed_parameters = [transform(u) for u in ANCHOR_PARAMETERS]
    anchor_offsets = [
        tuple(-coordinate for coordinate in quarter_turn(u))
        for u in transformed_parameters
    ]
    anchors = [add(TRANSLATION, offset) for offset in anchor_offsets]
    points = core + anchors

    assert len(points) == 139
    assert_distance_sidon(points)
    assert maximum_collinearity(points) == 7

    noncollinear_values: list[int] = []
    collinear_values: list[int] = []
    for i, j, k in combinations(range(len(ANCHOR_PARAMETERS)), 3):
        a = ANCHOR_PARAMETERS[i]
        u = sub(ANCHOR_PARAMETERS[j], a)
        v = sub(ANCHOR_PARAMETERS[k], a)
        value = triple_correlation(core_differences_untransformed, u, v)
        target = (
            noncollinear_values if determinant(u, v) != 0 else collinear_values
        )
        target.append(value)

        # The transformed anchor triangle induces exactly the transformed
        # shifts u and v, so every core witness survives in the full set.
        anchor_a = anchors[i]
        assert quarter_turn(sub(anchors[j], anchor_a)) == transform(u)
        assert quarter_turn(sub(anchors[k], anchor_a)) == transform(v)

    assert len(noncollinear_values) == 231
    assert min(noncollinear_values) == 2_281
    assert max(noncollinear_values) == 3_464
    assert sum(noncollinear_values) == 653_108
    assert len(collinear_values) == 55
    assert min(collinear_values) == 3_102
    assert max(collinear_values) == 3_947
    assert sum(collinear_values) == 196_328

    ordered_noncollinear_contribution = 6 * sum(noncollinear_values)
    assert ordered_noncollinear_contribution == 3_918_648

    print("points", len(points))
    print("unordered distances", comb(len(points), 2))
    print("maximum collinearity", maximum_collinearity(points))
    print("non-collinear anchor triangles", len(noncollinear_values))
    print("minimum/maximum codegree", min(noncollinear_values), max(noncollinear_values))
    print("ordered non-collinear moment contribution", ordered_noncollinear_contribution)
    print(
        "contribution / points^3",
        ordered_noncollinear_contribution / len(points) ** 3,
    )


if __name__ == "__main__":
    main()
