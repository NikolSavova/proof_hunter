#!/usr/bin/env python3
"""Exact checks for the common-r support/collision dichotomy."""

from __future__ import annotations

from collections import Counter
from itertools import product
import sys

from analyze_swap_optimal_nested_cores import profile, transformed_costas
from verify_closed_fibre_q_height_layered_barrier import (
    lifted_residue_parabola,
)
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rich_fibres,
    rotate,
    subtract,
)


Point = tuple[int, int]


def edge_base(
    ordinary_sum: Point,
    component: Point,
    first: Point,
    second: Point,
) -> Point:
    return rotate(
        subtract(
            subtract(
                subtract(ordinary_sum, component),
                linear(first),
            ),
            linear(second),
        )
    )


def verify_symbolic_normal_forms() -> None:
    b_value = (7, -3)
    c_value = (-4, 11)
    u_value = (5, 8)
    v_value = (-9, 6)
    component = (13, -2)
    sum_bu = (17, 21)
    sum_cu = (-6, 14)
    sum_bv = (9, -5)
    r_value = subtract(sum_bu, sum_cu)
    sum_cv = subtract(sum_bv, r_value)

    displacement = subtract(c_value, b_value)
    base_bu = edge_base(sum_bu, component, b_value, u_value)
    base_cu = edge_base(sum_cu, component, c_value, u_value)
    assert subtract(base_bu, base_cu) == rotate(
        add(r_value, linear(displacement))
    )

    # The three coupled D-D differences carried by one common-neighbour
    # extension.
    assert subtract(
        subtract(sum_bu, u_value),
        subtract(sum_cu, u_value),
    ) == r_value
    assert subtract(
        subtract(sum_bu, b_value),
        subtract(sum_cu, c_value),
    ) == add(r_value, displacement)

    # A second centre with the same r gives the repeated-r five-direction
    # collision.
    delta = subtract(v_value, u_value)
    height = subtract(sum_bv, sum_bu)
    assert height == subtract(sum_cv, sum_cu)
    base_bv = edge_base(sum_bv, component, b_value, v_value)
    base_cv = edge_base(sum_cv, component, c_value, v_value)
    eta = rotate(subtract(height, linear(delta)))
    assert subtract(base_bv, base_bu) == eta
    assert subtract(base_cv, base_cu) == eta
    assert subtract(
        subtract(sum_bv, v_value),
        subtract(sum_bu, u_value),
    ) == subtract(height, delta)
    assert subtract(
        subtract(sum_cv, v_value),
        subtract(sum_cu, u_value),
    ) == subtract(height, delta)
    assert subtract(
        add(component, linear(v_value)),
        add(component, linear(u_value)),
    ) == linear(delta)


def verify_support_collision_inequality() -> None:
    # Exhaust every selected-r assignment through six centres and four
    # possible labels.  Cauchy is exact in the form
    # n^2 <= X(n+2C), where C counts equal-r centre pairs.
    for number in range(1, 7):
        for assignment in product(range(4), repeat=number):
            loads = Counter(assignment)
            support = len(loads)
            collisions = sum(value * (value - 1) // 2 for value in loads.values())
            assert number * number <= support * (
                number + 2 * collisions
            )


def verify_costas_profiles() -> None:
    expected = {
        17: (
            (('copy_pairs', 139),
             ('fixed_opposite_r_copy_load', 2),
             ('fixed_opposite_r_centre_load', 1),
             ('fixed_zdr_copy_load', 2),
             ('fixed_zdr_centre_load', 1),
             ('maximum_opposite_r_support', 6)),
            0,
            0,
            0,
        ),
        23: (
            (('copy_pairs', 79_925),
             ('fixed_opposite_r_copy_load', 6),
             ('fixed_opposite_r_centre_load', 4),
             ('fixed_zdr_copy_load', 10),
             ('fixed_zdr_centre_load', 6),
             ('maximum_opposite_r_support', 25)),
            1_492,
            828,
            50,
        ),
    }
    for prime, target in expected.items():
        points, differences = transformed_costas(prime)
        _, summary, _ = profile(differences, points)
        rows = summary['matching_c4_r_overlap']
        actual = (
            summary['matching_common_extension_profile'],
            sum(value for _, value in rows),
            sum(value for (key, value) in rows if key[1] == 0),
            sum(value for (key, value) in rows if key == (16, 0)),
        )
        assert actual == target, (prime, actual, target)


def verify_lifted_parabola_equality_model() -> None:
    expected = {
        17: (8, 2, 0, 0),
        23: (8, 3, 2, 0),
        31: (8, 3, 3, 0),
        43: (8, 3, 3, 0),
    }
    for prime, target in expected.items():
        points = lifted_residue_parabola(prime)
        differences = difference_set(points)
        fibres, _, popular = rich_fibres(differences, adaptive=True)
        _, summary, _ = profile(differences, points)
        component = dict(summary['matching_component_profile'])
        c4 = dict(summary['matching_c4_profile'])
        actual = (
            len(popular),
            max(map(len, fibres.values()), default=0),
            component['maximum_vertices'],
            c4['four_cycles'],
        )
        assert actual == target, (prime, actual, target)


def verify_larger_costas_profile() -> None:
    points, differences = transformed_costas(37)
    _, summary, _ = profile(differences, points)
    rows = summary['matching_c4_r_overlap']
    assert summary['matching_common_extension_profile'] == (
        ('copy_pairs', 1_457_951),
        ('fixed_opposite_r_copy_load', 9),
        ('fixed_opposite_r_centre_load', 5),
        ('fixed_zdr_copy_load', 25),
        ('fixed_zdr_centre_load', 16),
        ('maximum_opposite_r_support', 27),
    )
    assert sum(value for _, value in rows) == 63_119
    assert sum(value for (key, value) in rows if key[1] == 0) == 29_811
    assert sum(value for (key, value) in rows if key[0] == 16) == 16_786
    assert sum(value for (key, value) in rows if key == (16, 0)) == 8_004


def main() -> None:
    verify_symbolic_normal_forms()
    verify_support_collision_inequality()
    verify_costas_profiles()
    verify_lifted_parabola_equality_model()
    if '--larger' in sys.argv:
        verify_larger_costas_profile()
    print('SWAP MATCHING COMMON-R SUPPORT/COLLISION: PASS')


if __name__ == '__main__':
    main()
