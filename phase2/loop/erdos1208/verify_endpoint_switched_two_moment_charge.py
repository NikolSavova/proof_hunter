#!/usr/bin/env python3
"""Exact checks for ENDPOINT_SWITCHED_TWO_MOMENT_CHARGE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
import sys

from analyze_affine_costas_energy import welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_endpoint_midpoint_sidon_ruler_barrier import construction
from verify_orthogonal_two_support_gate import difference_set
from verify_orthogonal_energy_product_ruler_barrier import erdos_turan
from verify_popular_pair_rectangle_moment_gate import rectangle_data
from verify_seven_incidence_opposite_endpoint_charge import (
    POINTS,
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]
AlphaProfile = tuple[int, int, int, int]
BetaProfile = tuple[int, int, int, int]


def norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def scale(value: int, point: Point) -> Point:
    return value * point[0], value * point[1]


def half(point: Point) -> Point:
    assert point[0] % 2 == 0 and point[1] % 2 == 0
    return point[0] // 2, point[1] // 2


def negate(point: Point) -> Point:
    return -point[0], -point[1]


def midpoint_table(points: list[Point]) -> dict[Point, Point]:
    """Canonical midpoint decoration, including one fixed diagonal at zero."""
    table = {(0, 0): scale(2, points[0])}
    for first in points:
        for second in points:
            if first == second:
                continue
            difference = subtract(first, second)
            midpoint = add(first, second)
            previous = table.setdefault(difference, midpoint)
            assert previous == midpoint
    assert len(table) == len(points) * (len(points) - 1) + 1
    return table


def alpha_profile(points: list[Point]) -> AlphaProfile:
    differences = difference_set(points)
    _, support_size, _, rectangles = rectangle_data(differences)
    midpoints = midpoint_table(points)
    loads: Counter[tuple[Point, Point]] = Counter()
    support = {subtract(left, right) for left in differences for right in differences}
    assert len(support) == support_size

    mass = 0
    for (shift, other), (first, _, _, _) in rectangles.items():
        for base in first:
            for translated in first:
                forms = (
                    base,
                    add(base, shift),
                    add(base, other),
                    translated,
                    add(translated, shift),
                    add(translated, other),
                )
                # The crossed four entries reconstruct the two omitted forms.
                assert forms[2] == add(forms[1], subtract(forms[5], forms[4]))
                assert forms[3] == add(forms[0], subtract(forms[4], forms[1]))
                assert forms[1] == add(forms[0], subtract(forms[4], forms[3]))
                assert forms[5] == add(forms[3], subtract(forms[2], forms[0]))
                assert forms[0] == add(forms[2], subtract(forms[3], forms[5]))
                assert forms[4] == add(forms[1], subtract(forms[5], forms[2]))
                cyclic = (
                    subtract(midpoints[forms[0]], midpoints[forms[4]]),
                    subtract(midpoints[forms[1]], midpoints[forms[5]]),
                    subtract(midpoints[forms[2]], midpoints[forms[3]]),
                )
                order = sorted(
                    range(3), key=lambda index: (-norm(cyclic[index]), index)
                )
                first_role, second_role = order[:2]
                cyclic_pairs = ((0, 4), (1, 5), (2, 3))
                switches = []
                switch_roles = []
                for cyclic_role in (first_role, second_role):
                    left, right = cyclic_pairs[cyclic_role]
                    displacement = subtract(forms[left], forms[right])
                    values = (
                        half(add(cyclic[cyclic_role], displacement)),
                        half(subtract(cyclic[cyclic_role], displacement)),
                    )
                    switches.append(values)
                    switch_roles.append(
                        max(
                            range(2),
                            key=lambda index: (norm(values[index]), -index),
                        )
                    )
                first_switch_role, second_switch_role = switch_roles
                first_degenerate = (
                    switches[0][1 - first_switch_role] == (0, 0)
                )
                second_degenerate = (
                    switches[1][1 - second_switch_role] == (0, 0)
                )
                if second_degenerate:
                    left, right = cyclic_pairs[second_role]
                    literal_role = max(
                        range(2),
                        key=lambda index: (
                            norm(forms[(left, right)[index]]),
                            -index,
                        ),
                    )
                    charge = (
                        2,
                        first_role,
                        second_role,
                        first_switch_role,
                        second_switch_role,
                        literal_role,
                        cyclic[first_role],
                        forms[(left, right)[literal_role]],
                    )
                elif first_degenerate:
                    left, right = cyclic_pairs[first_role]
                    literal_role = max(
                        range(2),
                        key=lambda index: (
                            norm(forms[(left, right)[index]]),
                            -index,
                        ),
                    )
                    charge = (
                        1,
                        first_role,
                        second_role,
                        first_switch_role,
                        second_switch_role,
                        literal_role,
                        switches[1][second_switch_role],
                        forms[(left, right)[literal_role]],
                    )
                else:
                    charge = (
                        0,
                        first_role,
                        second_role,
                        first_switch_role,
                        second_switch_role,
                        0,
                        cyclic[first_role],
                        switches[1][second_switch_role],
                    )
                assert charge[6] in support and charge[7] in differences
                loads[charge] += 1
                mass += 1

    assert mass == sum(
        len(first) ** 2 for first, _, _, _ in rectangles.values()
    )
    return mass, len(loads), sum(value * value for value in loads.values()), max(
        loads.values(), default=0
    )


def beta_configurations(
    differences: set[Point],
):
    """Yield z, its two bases, and the two translated four-point L-patterns."""
    _, _, _, rectangles = rectangle_data(differences)
    for (shift, other), (_, opposite, _, _) in rectangles.items():
        gap = subtract(shift, other)
        for base in opposite:
            first = (
                base,
                add(base, gap),
                subtract(add(base, gap), rotate(other)),
                subtract(base, rotate(shift)),
            )
            assert first[2] == add(first[3], linear(subtract(first[1], first[0])))
            for translated in opposite:
                displacement = subtract(translated, base)
                second = tuple(add(value, displacement) for value in first)
                yield shift, other, base, translated, first, second


def maximal_role(values: tuple[Point, ...]) -> int:
    """Largest norm, with the smallest role breaking an antipodal tie."""
    return max(range(4), key=lambda index: (norm(values[index]), -index))


def beta_charge(
    base: Point,
    translated: Point,
    first: tuple[Point, ...],
    second: tuple[Point, ...],
    midpoints: dict[Point, Point],
) -> tuple[bool, bool, int, int, Point, Point]:
    """Hybrid endpoint charge, with literal routing for a zero switch."""
    first_order = sorted(
        range(4), key=lambda index: (-norm(first[index]), index)
    )
    diagonal = base == translated
    if base == translated:
        first_role, second_role = first_order[:2]
        first_value = first[first_role]
        second_value = first[second_role]
        neighbor = first[(3, 2, 1, 0)[second_role]]
    else:
        first_role = first_order[0]
        second_role = maximal_role(second)
        first_value = first[first_role]
        second_value = second[second_role]
        neighbor = second[(3, 2, 1, 0)[second_role]]

    midpoint_difference = subtract(
        midpoints[second_value], midpoints[neighbor]
    )
    displacement = subtract(second_value, neighbor)
    degenerate = midpoint_difference in (displacement, negate(displacement))
    if not degenerate:
        switched = (
            half(add(midpoint_difference, displacement)),
            half(subtract(midpoint_difference, displacement)),
        )
        assert switched[0] != (0, 0) and switched[1] != (0, 0)
    last_value = second_value if degenerate else midpoint_difference
    return (
        diagonal,
        degenerate,
        first_role,
        second_role,
        first_value,
        last_value,
    )


def beta_profile(points: list[Point]) -> BetaProfile:
    differences = difference_set(points)
    midpoints = midpoint_table(points)
    loads: Counter[tuple[bool, bool, int, int, Point, Point]] = Counter()
    mass = 0
    for _, _, base, translated, first, second in beta_configurations(differences):
        loads[beta_charge(base, translated, first, second, midpoints)] += 1
        mass += 1
    return mass, len(loads), sum(value * value for value in loads.values()), max(
        loads.values(), default=0
    )


def verify_fixed_key_form(points: list[Point]) -> None:
    """Check (4.8), fixed-z injectivity, and the collision offsets."""
    differences = difference_set(points)
    midpoints = midpoint_table(points)
    by_fixed_key: dict[
        tuple[Point, Point], list[tuple[Point, Point, tuple[Point, ...]]]
    ] = defaultdict(list)
    by_shift_pair_role: dict[tuple[Point, Point, int, int], set[tuple[Point, Point]]] = (
        defaultdict(set)
    )

    for shift, other, base, translated, first, second in beta_configurations(
        differences
    ):
        r = subtract(shift, other)
        p = other
        u = first[0]
        v = second[2]
        expected = (
            u,
            add(u, r),
            subtract(add(u, r), rotate(p)),
            subtract(subtract(u, rotate(r)), rotate(p)),
            add(subtract(v, r), rotate(p)),
            add(v, rotate(p)),
            v,
            subtract(v, linear(r)),
        )
        actual = first + second
        assert actual == expected
        by_fixed_key[u, v].append((r, p, actual))

        # For fixed z and roles, every off-diagonal charged pair recovers
        # (base, translated).
        for first_role in range(4):
            for second_role in range(4):
                key = shift, other, first_role, second_role
                charged = first[first_role], second[second_role]
                assert charged not in by_shift_pair_role[key]
                by_shift_pair_role[key].add(charged)

        # The actual switched charge is also injective at fixed z.  In the
        # diagonal case its first charged vertex alone already recovers base.
        switched = beta_charge(base, translated, first, second, midpoints)
        key = shift, other, switched[0], switched[1], switched[2], switched[3]
        charged = switched[4], switched[5]
        assert charged not in by_shift_pair_role[key]
        by_shift_pair_role[key].add(charged)

    for entries in by_fixed_key.values():
        for first_index, (r, p, forms) in enumerate(entries):
            for rr, pp, other_forms in entries[first_index + 1 :]:
                rho = subtract(rr, r)
                pi = subtract(pp, p)
                expected_displacements = (
                    (0, 0),
                    rho,
                    subtract(rho, rotate(pi)),
                    subtract((0, 0), rotate(add(rho, pi))),
                    subtract(rotate(pi), rho),
                    rotate(pi),
                    (0, 0),
                    subtract((0, 0), linear(rho)),
                )
                assert tuple(
                    subtract(other_value, value)
                    for value, other_value in zip(forms, other_forms)
                ) == expected_displacements


def main() -> None:
    closure_alpha = alpha_profile(POINTS[:40])
    closure_beta = beta_profile(POINTS[:40])
    assert closure_alpha == (2_744_348, 2_524_398, 3_303_104, 16)
    assert closure_beta == (104_948, 96_590, 133_192, 11)
    print("closure-40 alpha", closure_alpha, "beta", closure_beta)

    expected = {
        11: ((6_686, 6_526, 7_022, 3), (1_208, 1_172, 1_288, 3)),
        17: ((81_264, 76_669, 91_210, 4), (12_290, 11_582, 13_882, 4)),
        23: (
            (2_294_322, 2_085_894, 2_763_502, 7),
            (250_722, 225_272, 310_190, 7),
        ),
        31: (
            (3_212_542, 3_031_587, 3_602_908, 6),
            (464_578, 417_066, 574_322, 7),
        ),
    }
    if "--extended" in sys.argv:
        expected.update(
            {
                37: (
                    (14_052_896, 12_866_893, 16_686_550, 7),
                    (2_015_584, 1_768_528, 2_599_728, 9),
                ),
                41: (
                    (21_034_648, 19_094_875, 25_402_326, 8),
                    (3_239_030, 2_802_672, 4_280_434, 9),
                ),
            }
        )
    for prime, target in expected.items():
        matrix, _ = ROWS[prime]
        points = [apply(matrix, point) for point in welch(prime)]
        profiles = alpha_profile(points), beta_profile(points)
        assert profiles == target
        print("Costas", prime, "alpha", profiles[0], "beta", profiles[1])
        if prime == 11:
            verify_fixed_key_form(points)

    # The old midpoint obstruction is removed by the support-adaptive cutoff.
    ruler_points = construction(8)[0]
    _, _, _, ruler_rectangles = rectangle_data(difference_set(ruler_points))
    assert not ruler_rectangles

    dense_ruler = erdos_turan(41, 40)
    perpendicular_ruler = [(value, 0) for value in dense_ruler[:20]] + [
        (0, value) for value in dense_ruler[20:]
    ]
    assert alpha_profile(perpendicular_ruler) == (0, 0, 0, 0)
    assert beta_profile(perpendicular_ruler) == (0, 0, 0, 0)

    print("ENDPOINT-SWITCHED TWO-MOMENT CHARGE GATE: PASS")


if __name__ == "__main__":
    main()
