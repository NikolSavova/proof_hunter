#!/usr/bin/env python3
"""Exact checks for HYBRID_ENDPOINT_OPPOSITE_CHARGE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
import sys

from analyze_affine_costas_energy import welch
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_endpoint_switched_two_moment_charge import midpoint_table, negate
from verify_orthogonal_energy_product_ruler_barrier import erdos_turan
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    POINTS,
    add,
    linear,
    rich_fibres,
    rotate,
    subtract,
)


Point = tuple[int, int]
Profile = tuple[int, int, int, int]


def antipodal_sign(point: Point) -> bool:
    """A fixed bit distinguishing every nonzero pair {d,-d}."""
    return point[0] < 0 or (point[0] == 0 and point[1] < 0)


def squared_norm(point: Point) -> int:
    return point[0] * point[0] + point[1] * point[1]


def maximal_literal_profile(points: list[Point]) -> Profile:
    """Stress the failed replacement of the midpoint by a largest literal."""
    differences = difference_set(points)
    fibres, _, _ = rich_fibres(differences, adaptive=True)
    loads: Counter[tuple[int, Point, Point]] = Counter()
    mass = 0

    for (base, ordinary_sum), fibre in fibres.items():
        w_value = subtract(ordinary_sum, base)
        local_keys: set[tuple[int, Point, Point]] = set()
        for shift in fibre:
            fixed_v = subtract(w_value, linear(shift))
            for other_shift in fibre:
                if shift == other_shift:
                    continue
                literals = (
                    add(base, other_shift),
                    subtract(w_value, other_shift),
                    subtract(w_value, linear(other_shift)),
                )
                role = max(
                    range(3),
                    key=lambda index: (
                        squared_norm(literals[index]),
                        literals[index],
                        index,
                    ),
                )
                charge = role, fixed_v, literals[role]
                assert charge not in local_keys
                local_keys.add(charge)
                loads[charge] += 1
                mass += 1

    return (
        mass,
        len(loads),
        sum(value * value for value in loads.values()),
        max(loads.values(), default=0),
    )


def hybrid_profile(points: list[Point]) -> Profile:
    differences = difference_set(points)
    midpoints = midpoint_table(points)
    fibres, _, popular = rich_fibres(differences, adaptive=True)
    loads: Counter[tuple[bool, bool, Point, Point]] = Counter()
    first_preimages: dict[
        tuple[bool, bool, Point, Point],
        list[tuple[Point, Point, Point]],
    ] = defaultdict(list)
    mass = 0

    for (base, ordinary_sum), fibre in fibres.items():
        w_value = subtract(ordinary_sum, base)
        local_keys: set[tuple[bool, bool, Point, Point]] = set()
        for shift in fibre:
            fixed_v = subtract(w_value, linear(shift))
            for other_shift in fibre:
                if shift == other_shift:
                    continue
                other_endpoint = add(base, other_shift)
                midpoint_difference = subtract(
                    midpoints[base], midpoints[other_endpoint]
                )
                displacement = subtract(base, other_endpoint)
                degenerate = midpoint_difference in (
                    displacement,
                    negate(displacement),
                )
                route_bit = (
                    midpoint_difference == displacement
                    if degenerate
                    else antipodal_sign(other_endpoint)
                )
                last_value = (
                    other_endpoint if degenerate else midpoint_difference
                )
                charge = (
                    degenerate,
                    route_bit,
                    fixed_v,
                    last_value,
                )

                # Proposition 3.1: no collision inside one fibre.
                assert charge not in local_keys
                local_keys.add(charge)

                if not degenerate:
                    assert all(
                        value % 2 == 0
                        for value in (
                            midpoint_difference[0] + displacement[0],
                            midpoint_difference[1] + displacement[1],
                            midpoint_difference[0] - displacement[0],
                            midpoint_difference[1] - displacement[1],
                        )
                    )
                    switch_plus = (
                        (midpoint_difference[0] + displacement[0]) // 2,
                        (midpoint_difference[1] + displacement[1]) // 2,
                    )
                    switch_minus = (
                        (midpoint_difference[0] - displacement[0]) // 2,
                        (midpoint_difference[1] - displacement[1]) // 2,
                    )
                    assert switch_plus in differences
                    assert switch_minus in differences
                    assert switch_plus != (0, 0) and switch_minus != (0, 0)

                # Verify the six-form fixed-key system (5.3).
                six_values = (
                    base,
                    add(base, shift),
                    other_endpoint,
                    add(fixed_v, rotate(shift)),
                    subtract(
                        add(fixed_v, add(base, linear(shift))),
                        other_endpoint,
                    ),
                    add(fixed_v, linear(subtract(shift, other_shift))),
                )
                assert all(value in differences for value in six_values)
                assert shift in popular and other_shift in popular

                loads[charge] += 1
                if len(first_preimages[charge]) < 2:
                    first_preimages[charge].append(
                        (base, shift, other_shift)
                    )
                mass += 1

        assert len(local_keys) == len(fibre) * (len(fibre) - 1)

    assert mass == sum(
        len(fibre) * (len(fibre) - 1) for fibre in fibres.values()
    )

    # Check the collision displacement list (5.5).
    for charge, preimages in first_preimages.items():
        if len(preimages) < 2:
            continue
        (base, shift, other_shift), (second_base, second_shift, second_other) = (
            preimages
        )
        fixed_v = charge[2]

        def forms(a_value: Point, q_value: Point, p_value: Point):
            c_value = add(a_value, p_value)
            return (
                a_value,
                add(a_value, q_value),
                c_value,
                add(fixed_v, rotate(q_value)),
                subtract(
                    add(fixed_v, add(a_value, linear(q_value))),
                    c_value,
                ),
                add(fixed_v, linear(subtract(q_value, p_value))),
            )

        first_forms = forms(base, shift, other_shift)
        second_forms = forms(second_base, second_shift, second_other)
        eta = subtract(second_base, base)
        rho = subtract(second_shift, shift)
        pi = subtract(second_other, other_shift)
        expected = (
            eta,
            add(eta, rho),
            add(eta, pi),
            rotate(rho),
            subtract(linear(rho), pi),
            linear(subtract(rho, pi)),
        )
        actual = tuple(
            subtract(second, first)
            for first, second in zip(first_forms, second_forms)
        )
        assert actual == expected

    return (
        mass,
        len(loads),
        sum(value * value for value in loads.values()),
        max(loads.values(), default=0),
    )


def main() -> None:
    expected: dict[str, Profile] = {
        "closure-30": (1_420, 1_418, 1_424, 2),
        "closure-40": (370_516, 345_170, 427_350, 7),
        "Costas-11": (2_264, 2_130, 2_536, 3),
        "Costas-17": (20_014, 18_102, 24_280, 4),
        "Costas-23": (498_674, 389_232, 774_012, 7),
        "Costas-31": (765_102, 614_528, 1_153_986, 8),
    }
    families: list[tuple[str, list[Point]]] = [
        ("closure-30", POINTS[:30]),
        ("closure-40", POINTS[:40]),
    ]
    primes = [11, 17, 23, 31]
    if "--extended" in sys.argv:
        primes += [37, 41, 43]
        expected.update(
            {
                "Costas-37": (2_939_312, 2_252_512, 4_758_468, 9),
                "Costas-41": (4_629_690, 3_473_144, 7_754_472, 12),
                "Costas-43": (8_451_318, 6_115_394, 14_984_178, 12),
            }
        )
    for prime in primes:
        matrix, _ = ROWS[prime]
        points = [apply(matrix, point) for point in welch(prime)]
        families.append((f"Costas-{prime}", points))

    for name, points in families:
        profile = hybrid_profile(points)
        assert profile == expected[name]
        print(name, profile, "size-biased load", profile[2] / profile[0])

    # The dense perpendicular-ruler obstruction has empty adaptive tail.
    ruler = erdos_turan(41, 40)
    ruler_points = [(value, 0) for value in ruler[:20]] + [
        (0, value) for value in ruler[20:]
    ]
    assert hybrid_profile(ruler_points) == (0, 0, 0, 0)

    if "--literal-max" in sys.argv:
        matrix, _ = ROWS[23]
        points = [apply(matrix, point) for point in welch(23)]
        literal_profile = maximal_literal_profile(points)
        assert literal_profile == (498_674, 80_916, 30_378_306, 326)
        print(
            "FAILED MAXIMAL LITERAL Costas-23",
            literal_profile,
            "size-biased load",
            literal_profile[2] / literal_profile[0],
        )

    print("HYBRID ENDPOINT OPPOSITE CHARGE GATE: PASS")


if __name__ == "__main__":
    main()
