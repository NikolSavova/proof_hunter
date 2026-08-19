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


def half(point: Point) -> Point:
    assert point[0] % 2 == 0 and point[1] % 2 == 0
    return point[0] // 2, point[1] // 2


def verify_resonance_affine_copies() -> None:
    """Check the shared-tail/head affine formulas (6.6)--(6.8)."""
    x_zero = (4, 2)
    y_zero = (0, 0)
    w_value = (0, 0)
    fixed_midpoint_difference = (0, 0)
    parameter = (2, 4)
    common_midpoint = add(x_zero, y_zero)

    # Shared tail: c=(X_0+p)-Y_0, so m(c)=X_0+Y_0+p.
    tail_midpoint = subtract(
        add(common_midpoint, parameter), fixed_midpoint_difference
    )
    opposite = subtract(w_value, linear(parameter))
    tail_first = half(add(tail_midpoint, opposite))
    tail_second = half(subtract(tail_midpoint, opposite))
    tail_first_zero = half(
        add(subtract(common_midpoint, fixed_midpoint_difference), w_value)
    )
    tail_second_zero = half(
        subtract(subtract(common_midpoint, fixed_midpoint_difference), w_value)
    )
    assert tail_first == subtract(tail_first_zero, half(rotate(parameter)))
    assert tail_second == add(
        tail_second_zero, half(add(parameter, linear(parameter)))
    )

    # Shared head: c=X_0-(Y_0-p), so m(c)=X_0+Y_0-p.
    head_midpoint = subtract(
        subtract(common_midpoint, parameter), fixed_midpoint_difference
    )
    head_first = half(add(head_midpoint, opposite))
    head_second = half(subtract(head_midpoint, opposite))
    assert head_first == subtract(
        tail_first_zero, half(add(parameter, linear(parameter)))
    )
    assert head_second == add(tail_second_zero, half(rotate(parameter)))

    small = half(rotate(parameter))
    large = half(add(parameter, linear(parameter)))
    assert 4 * squared_norm(small) == squared_norm(parameter)
    assert 4 * squared_norm(large) == 5 * squared_norm(parameter)


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


def hybrid_profile(
    points: list[Point], expect_no_fallback: bool = False
) -> Profile:
    differences = difference_set(points)
    midpoints = midpoint_table(points)
    fibres, _, popular = rich_fibres(differences, adaptive=True)
    loads: Counter[tuple[int, int, Point, Point]] = Counter()
    first_preimages: dict[
        tuple[int, int, Point, Point],
        list[tuple[Point, Point, Point, Point]],
    ] = defaultdict(list)
    normal_edges: list[
        tuple[
            tuple[Point, Point],
            Point,
            Point,
            Point,
            Point,
            Point,
            Point,
            Point,
            Point,
        ]
    ] = []
    normal_degrees: Counter[tuple[int, int, Point, Point]] = Counter()
    fibre_local_keys: dict[
        tuple[Point, Point], set[tuple[int, int, Point, Point]]
    ] = defaultdict(set)
    fibre_expected_counts: dict[tuple[Point, Point], int] = {}
    mass = 0
    resonance_fallback_mass = 0

    for (base, ordinary_sum), fibre in fibres.items():
        fibre_label = base, ordinary_sum
        w_value = subtract(ordinary_sum, base)
        local_keys = fibre_local_keys[fibre_label]
        fibre_expected_counts[fibre_label] = len(fibre) * (len(fibre) - 1)
        configurations = []
        degenerate_midpoint_counts: Counter[
            tuple[int, int, Point, Point]
        ] = Counter()

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
                if degenerate:
                    shared_endpoint_bit = midpoint_difference == displacement
                    fixed_x = add(base, shift)
                    other_opposite = subtract(
                        w_value, linear(other_shift)
                    )
                    opposite_midpoint = subtract(
                        midpoints[other_endpoint], midpoints[other_opposite]
                    )
                    midpoint_charge = (
                        2,
                        2 * int(shared_endpoint_bit)
                        + int(antipodal_sign(other_opposite)),
                        fixed_x,
                        opposite_midpoint,
                    )
                    degenerate_midpoint_counts[midpoint_charge] += 1
                else:
                    shared_endpoint_bit = False
                    fixed_x = (0, 0)
                    other_opposite = (0, 0)
                    midpoint_charge = None

                configurations.append(
                    (
                        shift,
                        other_shift,
                        other_endpoint,
                        midpoint_difference,
                        displacement,
                        degenerate,
                        shared_endpoint_bit,
                        fixed_v,
                        fixed_x,
                        other_opposite,
                        midpoint_charge,
                    )
                )

        local_resonances: dict[
            tuple[int, int, Point, Point],
            list[tuple[Point, Point, Point]],
        ] = defaultdict(list)
        for configuration in configurations:
            shift = configuration[0]
            other_shift = configuration[1]
            other_opposite = configuration[9]
            midpoint_charge = configuration[10]
            if midpoint_charge is not None:
                local_resonances[midpoint_charge].append(
                    (shift, other_shift, other_opposite)
                )
        for midpoint_charge, resonant in local_resonances.items():
            if len(resonant) < 2:
                continue
            first_q, first_p, first_y = resonant[0]
            for second_q, second_p, second_y in resonant[1:]:
                # The common fibre and fixed x force q to agree.  Hence the
                # changes in r=q-p and y=w-Lp are -pi and -Lpi.
                assert second_q == first_q
                pi = subtract(second_p, first_p)
                assert pi != (0, 0)
                assert pi in differences
                first_r = subtract(first_q, first_p)
                second_r = subtract(second_q, second_p)
                assert subtract(second_r, first_r) == negate(pi)
                assert subtract(second_y, first_y) == negate(linear(pi))

                first_c = add(base, first_p)
                second_c = add(base, second_p)
                midpoint_change = subtract(
                    midpoints[second_c], midpoints[first_c]
                )
                shared_endpoint_bit = bool(midpoint_charge[1] // 2)
                assert midpoint_change == (
                    pi if shared_endpoint_bit else negate(pi)
                )
                y_change = subtract(second_y, first_y)
                assert all(
                    value % 2 == 0
                    for value in (
                        midpoint_change[0] + y_change[0],
                        midpoint_change[1] + y_change[1],
                        midpoint_change[0] - y_change[0],
                        midpoint_change[1] - y_change[1],
                    )
                )
                y_switches = (
                    (
                        (midpoint_change[0] + y_change[0]) // 2,
                        (midpoint_change[1] + y_change[1]) // 2,
                    ),
                    (
                        (midpoint_change[0] - y_change[0]) // 2,
                        (midpoint_change[1] - y_change[1]) // 2,
                    ),
                )
                assert all(value in differences for value in y_switches)
                switch_norms = sorted(squared_norm(value) for value in y_switches)
                pi_norm = squared_norm(pi)
                assert 4 * switch_norms[0] == pi_norm
                assert 4 * switch_norms[1] == 5 * pi_norm

        for (
            shift,
            other_shift,
            other_endpoint,
            midpoint_difference,
            displacement,
            degenerate,
            shared_endpoint_bit,
            fixed_v,
            fixed_x,
            other_opposite,
            midpoint_charge,
        ) in configurations:
            if degenerate:
                assert midpoint_charge is not None
                if degenerate_midpoint_counts[midpoint_charge] == 1:
                    charge = midpoint_charge
                else:
                    # A repeated local midpoint key is routed to the two
                    # literal anchors.  This retains fibrewise injectivity
                    # and records an internal affine-resonance witness.
                    charge = (
                        3,
                        int(shared_endpoint_bit),
                        add(base, shift),
                        subtract(w_value, linear(other_shift)),
                    )
                    resonance_fallback_mass += 1
            else:
                fixed_right = subtract(w_value, shift)
                normal_key = (
                    int(antipodal_sign(other_endpoint)),
                    midpoint_difference,
                )
                normal_edges.append(
                    (
                        fibre_label,
                        base,
                        w_value,
                        shift,
                        other_shift,
                        other_endpoint,
                        midpoint_difference,
                        fixed_v,
                        fixed_right,
                    )
                )
                normal_degrees[(0, *normal_key, fixed_v)] += 1
                normal_degrees[(1, *normal_key, fixed_right)] += 1
                charge = None

            if charge is not None:
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

            if charge is not None:
                loads[charge] += 1
                if len(first_preimages[charge]) < 2:
                    first_preimages[charge].append(
                        (base, w_value, shift, other_shift)
                    )
            mass += 1

    balanced_degree_moment = 0
    for (
        fibre_label,
        base,
        w_value,
        shift,
        other_shift,
        other_endpoint,
        midpoint_difference,
        fixed_left,
        fixed_right,
    ) in normal_edges:
        normal_key = (
            int(antipodal_sign(other_endpoint)),
            midpoint_difference,
        )
        left_degree = normal_degrees[(0, *normal_key, fixed_left)]
        right_degree = normal_degrees[(1, *normal_key, fixed_right)]
        balanced_degree_moment += min(left_degree, right_degree)
        if left_degree <= right_degree:
            charge = (0, normal_key[0], fixed_left, normal_key[1])
        else:
            charge = (1, normal_key[0], fixed_right, normal_key[1])

        local_keys = fibre_local_keys[fibre_label]
        assert charge not in local_keys
        local_keys.add(charge)
        loads[charge] += 1
        if len(first_preimages[charge]) < 2:
            first_preimages[charge].append(
                (base, w_value, shift, other_shift)
            )

    for fibre_label, expected_count in fibre_expected_counts.items():
        assert len(fibre_local_keys[fibre_label]) == expected_count

    assert mass == sum(
        len(fibre) * (len(fibre) - 1) for fibre in fibres.values()
    )
    if expect_no_fallback:
        assert resonance_fallback_mass == 0

    normal_charge_second_moment = sum(
        value * value
        for charge, value in loads.items()
        if charge[0] in (0, 1)
    )
    assert normal_charge_second_moment <= balanced_degree_moment

    # Check the normal collision displacement list (5.5), and the sharper
    # common-endpoint list from Section 6.
    for charge, preimages in first_preimages.items():
        if len(preimages) < 2:
            continue
        (
            (base, w_value, shift, other_shift),
            (second_base, second_w, second_shift, second_other),
        ) = preimages
        if charge[0] == 3:
            first_p = other_shift
            first_r = subtract(shift, other_shift)
            second_p = second_other
            second_r = subtract(second_shift, second_other)
            pi = subtract(second_p, first_p)
            tau = subtract(second_r, first_r)

            def degenerate_forms(p_value: Point, r_value: Point):
                fixed_x, fixed_y = charge[2], charge[3]
                return (
                    subtract(subtract(fixed_x, p_value), r_value),
                    subtract(fixed_x, r_value),
                    fixed_x,
                    subtract(add(fixed_y, rotate(p_value)), r_value),
                    add(fixed_y, rotate(p_value)),
                    subtract(fixed_y, linear(r_value)),
                    fixed_y,
                )

            first_forms = degenerate_forms(first_p, first_r)
            second_forms = degenerate_forms(second_p, second_r)
            expected = (
                negate(add(pi, tau)),
                negate(tau),
                (0, 0),
                subtract(rotate(pi), tau),
                rotate(pi),
                negate(linear(tau)),
                (0, 0),
            )
            actual = tuple(
                subtract(second, first)
                for first, second in zip(first_forms, second_forms)
            )
            assert actual == expected
            assert all(value in differences for value in first_forms)
            assert all(value in differences for value in second_forms)
            continue

        if charge[0] == 2:
            first_p = other_shift
            first_r = subtract(shift, other_shift)
            first_y = subtract(w_value, linear(first_p))
            second_p = second_other
            second_r = subtract(second_shift, second_other)
            second_y = subtract(second_w, linear(second_p))
            pi = subtract(second_p, first_p)
            tau = subtract(second_r, first_r)
            kappa = subtract(second_y, first_y)

            def midpoint_degenerate_forms(
                p_value: Point, r_value: Point, y_value: Point
            ):
                fixed_x = charge[2]
                return (
                    subtract(subtract(fixed_x, p_value), r_value),
                    subtract(fixed_x, r_value),
                    fixed_x,
                    subtract(add(y_value, rotate(p_value)), r_value),
                    add(y_value, rotate(p_value)),
                    subtract(y_value, linear(r_value)),
                    y_value,
                )

            first_forms = midpoint_degenerate_forms(
                first_p, first_r, first_y
            )
            second_forms = midpoint_degenerate_forms(
                second_p, second_r, second_y
            )
            expected = (
                negate(add(pi, tau)),
                negate(tau),
                (0, 0),
                subtract(add(kappa, rotate(pi)), tau),
                add(kappa, rotate(pi)),
                subtract(kappa, linear(tau)),
                kappa,
            )
            actual = tuple(
                subtract(second, first)
                for first, second in zip(first_forms, second_forms)
            )
            assert actual == expected
            assert all(value in differences for value in first_forms)
            assert all(value in differences for value in second_forms)
            continue

        if charge[0] == 1:
            fixed_right = charge[2]

            def right_forms(
                a_value: Point, q_value: Point, p_value: Point
            ):
                r_value = subtract(q_value, p_value)
                return (
                    a_value,
                    add(a_value, q_value),
                    add(a_value, p_value),
                    fixed_right,
                    add(fixed_right, r_value),
                    subtract(fixed_right, rotate(q_value)),
                    subtract(add(fixed_right, r_value), rotate(p_value)),
                )

            first_forms = right_forms(base, shift, other_shift)
            second_forms = right_forms(
                second_base, second_shift, second_other
            )
            eta = subtract(second_base, base)
            rho = subtract(second_shift, shift)
            pi = subtract(second_other, other_shift)
            expected = (
                eta,
                add(eta, rho),
                add(eta, pi),
                (0, 0),
                subtract(rho, pi),
                negate(rotate(rho)),
                subtract(rho, linear(pi)),
            )
            actual = tuple(
                subtract(second, first)
                for first, second in zip(first_forms, second_forms)
            )
            assert actual == expected
            assert all(value in differences for value in first_forms)
            assert all(value in differences for value in second_forms)
            continue

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
    verify_resonance_affine_copies()
    expected: dict[str, Profile] = {
        "closure-30": (1_420, 1_420, 1_420, 1),
        "closure-40": (370_516, 367_809, 376_018, 4),
        "Costas-11": (2_264, 2_254, 2_284, 2),
        "Costas-17": (20_014, 19_710, 20_622, 2),
        "Costas-23": (498_674, 469_697, 558_688, 4),
        "Costas-31": (765_102, 712_180, 883_150, 5),
    }
    families: list[tuple[str, list[Point]]] = [
        ("closure-30", POINTS[:30]),
        ("closure-40", POINTS[:40]),
    ]
    primes = [11, 17, 23, 31]
    if "--extended" in sys.argv:
        families.append(("closure-80", POINTS[:80]))
        expected["closure-80"] = (357_094, 356_860, 357_566, 3)
        primes += [37, 41, 43]
        expected.update(
            {
                "Costas-37": (2_939_312, 2_716_744, 3_415_740, 5),
                "Costas-41": (4_629_690, 4_197_631, 5_604_596, 7),
                "Costas-43": (8_451_318, 7_606_952, 10_330_054, 7),
            }
        )
    for prime in primes:
        matrix, _ = ROWS[prime]
        points = [apply(matrix, point) for point in welch(prime)]
        families.append((f"Costas-{prime}", points))

    for name, points in families:
        profile = hybrid_profile(points, expect_no_fallback=True)
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
