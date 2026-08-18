#!/usr/bin/env python3
"""Exact six-biclique obstruction to the longest-book moment gate.

The exact symbolic part checks that the generic affine construction has no
forced equality between two edge norms.  The numerical part instantiates the
construction at s=8 and verifies distance-Sidonicity, the six simultaneous
K_{8,8} projection subgraphs, and the resulting charge profiles.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import random

from analyze_fixed_row_cycle_longest_charge import profile as charge_profile
from search_biclique_realization import first_distance_collision
from search_transverse_closure import (
    add,
    divide_by_role,
    scale_by_role,
    subtract,
)
from verify_transverse_fixed_row_c4 import (
    ROLE_PAIRS,
    fixed_row_relations,
    projection_cycles,
)


Gaussian = tuple[int, int]
Expression = dict[tuple[object, ...], Gaussian]

UNITS: tuple[Gaussian, ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


def gaussian_add(left: Gaussian, right: Gaussian) -> Gaussian:
    return left[0] + right[0], left[1] + right[1]


def gaussian_multiply(left: Gaussian, right: Gaussian) -> Gaussian:
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def inverse_unit(value: Gaussian) -> Gaussian:
    return value[0], -value[1]


def expression_scale(expression: Expression, scalar: Gaussian) -> Expression:
    answer = {
        variable: gaussian_multiply(scalar, coefficient)
        for variable, coefficient in expression.items()
    }
    return {variable: coefficient for variable, coefficient in answer.items() if coefficient != (0, 0)}


def expression_add(left: Expression, right: Expression) -> Expression:
    answer = dict(left)
    for variable, coefficient in right.items():
        answer[variable] = gaussian_add(answer.get(variable, (0, 0)), coefficient)
        if answer[variable] == (0, 0):
            del answer[variable]
    return answer


def expression_subtract(left: Expression, right: Expression) -> Expression:
    return expression_add(left, expression_scale(right, (-1, 0)))


def symbolic_six_gadgets(side: int) -> list[Expression]:
    """Return the affine coefficient vectors of all construction points."""

    fixed_difference: Expression = {("d",): (1, 0)}
    points: list[Expression] = [fixed_difference, {}]
    for gadget, (first, second) in enumerate(ROLE_PAIRS):
        third, fourth = [role for role in range(4) if role not in (first, second)]
        left = [
            {("left", gadget, index): (1, 0)}
            for index in range(side)
        ]
        right = [
            {("right", gadget, index): (1, 0)}
            for index in range(side)
        ]
        points.extend(left)
        points.extend(right)
        for i in range(side):
            for j in range(side):
                free = {("cell", gadget, i, j): (1, 0)}
                points.append(free)
                total = expression_add(
                    expression_add(
                        expression_scale(left[i], UNITS[first]),
                        expression_scale(right[j], UNITS[second]),
                    ),
                    expression_scale(free, UNITS[third]),
                )
                solved = expression_scale(
                    expression_subtract(fixed_difference, total),
                    inverse_unit(UNITS[fourth]),
                )
                points.append(solved)
    return points


def norm_signature(expression: Expression):
    """Canonical signature modulo multiplication by a complex unit phase."""

    support = tuple(sorted(expression))
    assert support
    first = expression[support[0]]
    norm = first[0] * first[0] + first[1] * first[1]
    ratios = []
    for variable in support:
        real, imag = expression[variable]
        ratios.append(
            (
                Fraction(real * first[0] + imag * first[1], norm),
                Fraction(imag * first[0] - real * first[1], norm),
            )
        )
    return support, norm, tuple(ratios)


def verify_symbolic_genericity() -> None:
    # Any equality between two edge norms uses at most four endpoints and
    # therefore at most four indices of each gadget coordinate.  Hence side 4
    # contains every equality pattern that can occur for arbitrary side.
    points = symbolic_six_gadgets(4)
    assert len(points) == 242
    signatures = {}
    for first in range(len(points)):
        for second in range(first):
            difference = expression_subtract(points[first], points[second])
            assert difference
            signature = norm_signature(difference)
            assert signature not in signatures, (
                signatures[signature],
                (first, second),
            )
            signatures[signature] = (first, second)
    assert len(signatures) == 242 * 241 // 2 == 29_161


def numerical_six_gadgets(side: int, seed: int, bits: int = 160):
    rng = random.Random(seed)
    fixed_difference = (1, 0)
    points = [fixed_difference, (0, 0)]
    point_set = set(points)

    def fresh():
        while True:
            point = (
                rng.randrange(-(1 << bits), 1 << bits),
                rng.randrange(-(1 << bits), 1 << bits),
            )
            if point not in point_set:
                point_set.add(point)
                points.append(point)
                return point

    for first, second in ROLE_PAIRS:
        third, fourth = [role for role in range(4) if role not in (first, second)]
        left = [fresh() for _ in range(side)]
        right = [fresh() for _ in range(side)]
        for left_point in left:
            for right_point in right:
                free = fresh()
                total = add(
                    add(
                        scale_by_role(first, left_point),
                        scale_by_role(second, right_point),
                    ),
                    scale_by_role(third, free),
                )
                solved = divide_by_role(
                    fourth,
                    subtract(fixed_difference, total),
                )
                assert solved not in point_set
                point_set.add(solved)
                points.append(solved)
    return points, fixed_difference


def verify_numerical_instance() -> None:
    points, row = numerical_six_gadgets(8, 1_600_800)
    assert len(points) == 866
    assert first_distance_collision(points) is None

    relations = fixed_row_relations(points, row)
    assert len(relations) == 384
    cycle_counts = [
        len(projection_cycles(relations, *projection))
        for projection in ROLE_PAIRS
    ]
    assert cycle_counts == [784] * 6

    expected = [
        (784, 42, 17_184),
        (784, 49, 18_094),
        (784, 49, 18_744),
        (784, 49, 18_030),
        (784, 49, 18_812),
        (784, 49, 17_330),
    ]
    profiles = [tuple(item[:3]) for item in charge_profile(points, row)]
    assert profiles == expected


def main() -> None:
    verify_symbolic_genericity()
    verify_numerical_instance()
    print("symbolic side-4 edge signatures: 29161 distinct")
    print("numerical side-8 points: 866, distance-Sidon")
    print("fixed-row relations: 384")
    print("six projection C4 counts: 784 each")
    print("six-biclique longest-book obstruction: PASS")


if __name__ == "__main__":
    main()
