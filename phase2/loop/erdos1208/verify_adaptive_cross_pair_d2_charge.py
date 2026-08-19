#!/usr/bin/env python3
"""Exact verifier for the adaptive cross-pair D^2 charge."""

from __future__ import annotations

from collections import Counter, defaultdict
import sys

from analyze_affine_costas_energy import is_distance_sidon, welch
from analyze_cross_endpoint_pair_charge import iter_records
from verify_determinant_prime_costas_resonance import ROWS, apply
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rich_fibres,
    subtract,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, int, int, int, int]


def inverse_linear(value: Point) -> Point:
    """Invert L=I+J on its integral image."""
    first, second = value
    assert (first + second) % 2 == 0
    assert (second - first) % 2 == 0
    return (first + second) // 2, (second - first) // 2


def route_profile(differences: set[Point]) -> Profile:
    fibres, support, _ = rich_fibres(differences, adaptive=True)
    loads: Counter[tuple[Point, Point]] = Counter()
    first_preimages: dict[
        tuple[Point, Point],
        list[tuple[Point, Point, Point, Point]],
    ] = defaultdict(list)
    mass = 0

    for fibre_label, q_forms, p_forms in iter_records(differences):
        base, ordinary_sum = fibre_label
        w_value = subtract(ordinary_sum, base)
        fixed_head = q_forms[0]
        fixed_opposite = p_forms[2]
        key = fixed_head, fixed_opposite
        loads[key] += 1

        # Recover the two shifts from the key inside the fixed fibre.
        q_value = subtract(fixed_head, base)
        p_value = inverse_linear(subtract(w_value, fixed_opposite))
        assert q_forms == (
            add(base, q_value),
            subtract(w_value, q_value),
            subtract(w_value, linear(q_value)),
        )
        assert p_forms == (
            add(base, p_value),
            subtract(w_value, p_value),
            subtract(w_value, linear(p_value)),
        )
        if len(first_preimages[key]) < 2:
            first_preimages[key].append(
                (base, w_value, q_value, p_value)
            )
        mass += 1

    assert mass == sum(
        len(fibre) * (len(fibre) - 1) for fibre in fibres.values()
    )

    # A fixed key is (b,y)=(a+q,w-Lp).  If two preimages differ by
    # delta=A-a and pi=P-p, then Q-q=-delta and W-w=Lpi.  The seven
    # D-form displacements are the list below.
    for preimages in first_preimages.values():
        if len(preimages) < 2:
            continue
        a_value, w_value, q_value, p_value = preimages[0]
        other_a, other_w, other_q, other_p = preimages[1]
        delta = subtract(other_a, a_value)
        pi_value = subtract(other_p, p_value)
        assert subtract(other_q, q_value) == (-delta[0], -delta[1])
        assert subtract(other_w, w_value) == linear(pi_value)

        def forms(a: Point, w: Point, q: Point, p: Point):
            return (
                a,
                add(a, q),
                add(a, p),
                subtract(w, q),
                subtract(w, p),
                subtract(w, linear(q)),
                subtract(w, linear(p)),
            )

        first_forms = forms(a_value, w_value, q_value, p_value)
        second_forms = forms(other_a, other_w, other_q, other_p)
        expected = (
            delta,
            (0, 0),
            add(delta, pi_value),
            add(delta, linear(pi_value)),
            (-pi_value[1], pi_value[0]),
            linear(add(delta, pi_value)),
            (0, 0),
        )
        actual = tuple(
            subtract(second, first)
            for first, second in zip(first_forms, second_forms)
        )
        assert actual == expected
        assert all(value in differences for value in first_forms)
        assert all(value in differences for value in second_forms)

    return (
        len(differences),
        support,
        mass,
        sum(value * value for value in loads.values()),
        max(loads.values(), default=0),
    )


def transformed_costas(prime: int, matrix=None) -> list[Point]:
    if matrix is None:
        matrix, _ = ROWS[prime]
    points = [apply(matrix, point) for point in welch(prime)]
    assert is_distance_sidon(points)
    return points


def main() -> None:
    families: list[tuple[str, set[Point], Profile]] = [
        (
            "closure-30",
            difference_set(POINTS[:30]),
            (871, 62_273, 1_420, 1_496, 2),
        ),
        (
            "closure-40",
            difference_set(POINTS[:40]),
            (1_561, 156_057, 370_516, 1_139_274, 26),
        ),
        (
            "Costas-23",
            difference_set(transformed_costas(23)),
            (463, 4_513, 498_674, 3_020_644, 24),
        ),
        (
            "Costas-31",
            difference_set(transformed_costas(31)),
            (871, 9_495, 765_102, 3_872_958, 33),
        ),
        (
            "radial-8",
            radial_set(8),
            (83, 431, 555_948, 59_454_358, 230),
        ),
    ]
    if "--extended" in sys.argv:
        families.extend(
            [
                (
                    "Costas-37",
                    difference_set(transformed_costas(37)),
                    (1_261, 13_917, 2_939_312, 18_630_176, 34),
                ),
                (
                    "Costas-41",
                    difference_set(transformed_costas(41)),
                    (1_561, 17_875, 4_629_690, 30_972_628, 44),
                ),
                (
                    "Costas-43",
                    difference_set(transformed_costas(43)),
                    (1_723, 19_819, 8_451_318, 71_515_362, 53),
                ),
                (
                    "Costas-47-low-support",
                    difference_set(
                        transformed_costas(47, (-10, 11, 3, -8))
                    ),
                    (2_071, 23_427, 25_194_336, 361_029_280, 71),
                ),
            ]
        )

    for name, differences, expected in families:
        actual = route_profile(differences)
        assert actual == expected, (name, actual, expected)
        number, support, mass, moment, maximum = actual
        adaptive_k = support / number
        print(
            name,
            actual,
            "moment/(K mass)",
            moment / (adaptive_k * mass) if mass else 0.0,
            "moment/S^2",
            moment / (support * support),
            "max",
            maximum,
        )

    print("ADAPTIVE CROSS-PAIR D^2 CHARGE: PASS")


if __name__ == "__main__":
    main()
