#!/usr/bin/env python3
"""Exact checks for ENDPOINT_SWITCHED_TWO_MOMENT_CHARGE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict

from analyze_affine_costas_energy import welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_endpoint_midpoint_sidon_ruler_barrier import construction
from verify_orthogonal_two_support_gate import difference_set
from verify_popular_pair_rectangle_moment_gate import rectangle_data
from verify_radial_orthogonal_product_barrier import radial_set
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
                charge = (
                    subtract(midpoints[forms[0]], midpoints[forms[4]]),
                    subtract(midpoints[forms[1]], midpoints[forms[5]]),
                )
                assert charge[0] in support and charge[1] in support
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


def beta_profile(points_or_differences: list[Point] | set[Point]) -> BetaProfile:
    differences = (
        points_or_differences
        if isinstance(points_or_differences, set)
        else difference_set(points_or_differences)
    )
    loads: Counter[tuple[int, int, Point, Point]] = Counter()
    mass = 0
    for _, _, _, _, first, second in beta_configurations(differences):
        first_role = maximal_role(first)
        second_role = maximal_role(second)
        loads[first_role, second_role, first[first_role], second[second_role]] += 1
        mass += 1
    return mass, len(loads), sum(value * value for value in loads.values()), max(
        loads.values(), default=0
    )


def verify_fixed_key_form(points: list[Point]) -> None:
    """Check (4.8), fixed-z injectivity, and the collision offsets."""
    differences = difference_set(points)
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

        # For fixed z and roles, the charged pair recovers (base, translated).
        for first_role in range(4):
            for second_role in range(4):
                key = shift, other, first_role, second_role
                charged = first[first_role], second[second_role]
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
    assert closure_alpha == (2_744_348, 1_290_420, 8_846_328, 254)
    assert closure_beta == (104_948, 82_756, 320_912, 41)
    print("closure-40 alpha", closure_alpha, "beta", closure_beta)

    expected = {
        11: ((6_686, 3_092, 15_988, 14), (1_208, 956, 2_368, 10)),
        17: ((81_264, 36_904, 237_056, 74), (12_290, 9_544, 22_102, 13)),
        23: (
            (2_294_322, 954_020, 7_596_972, 242),
            (250_722, 147_832, 834_482, 45),
        ),
        31: (
            (3_212_542, 1_452_994, 8_240_740, 196),
            (464_578, 302_968, 1_213_686, 42),
        ),
    }
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

    radial = beta_profile(radial_set(8))
    assert radial == (336_612, 30_152, 13_215_740, 225)
    assert radial[2] * closure_beta[0] > 12 * radial[0] * closure_beta[2]
    print("radial-8 beta negative control", radial)
    print("ENDPOINT-SWITCHED TWO-MOMENT CHARGE GATE: PASS")


if __name__ == "__main__":
    main()
