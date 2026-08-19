#!/usr/bin/env python3
"""Exact checks for SAME_MIDPOINT_LITERAL_D2_COLLISION_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
import sys

from analyze_cross_endpoint_pair_charge import iter_records
from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_endpoint_cross_switched_collision_charge import (
    endpoint_decorations,
    endpoint_head_code,
    midpoint,
    recover_heads,
)
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import add, linear, subtract
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Profile = tuple[int, int, int, int, int, int, int]


def profile(differences: set[Point]) -> Profile:
    groups: dict[tuple[Point, Point], list[tuple[Point, ...]]] = defaultdict(list)
    mass = 0
    for (u_value, _), q_forms, p_forms in iter_records(differences):
        row = (
            u_value,
            q_forms[0],
            p_forms[0],
            q_forms[1],
            p_forms[1],
            q_forms[2],
            p_forms[2],
        )
        groups[(row[1], row[6])].append(row)
        mass += 1

    loads: Counter[tuple[Point, Point]] = Counter()
    collision_mass = 0
    for records in groups.values():
        collision_mass += len(records) ** 2
        for first in records:
            for second in records:
                loads[(first[0], second[3])] += 1

    sums = {add(left, right) for left in differences for right in differences}

    # Directly verify the matrix/overlap expansion (3.4).
    left_counts: dict[tuple[Point, Point], Counter[Point]] = {}
    right_counts: dict[tuple[Point, Point], Counter[Point]] = {}
    for cell, records in groups.items():
        left_counts[cell] = Counter(record[0] for record in records)
        right_counts[cell] = Counter(record[3] for record in records)

    cells = list(groups)
    second_moment = sum(value * value for value in loads.values())
    # The literal expansion over every ordered cell pair is quadratic in the
    # number of occupied cells.  Check it on all compact fixtures; the direct
    # load calculation above checks the same matrix product on the larger
    # stress rows without materialising a 10^10-pair loop.
    if len(cells) <= 2_000:
        overlap_total = 0
        for first_cell in cells:
            for second_cell in cells:
                left_overlap = sum(
                    value * left_counts[second_cell].get(point, 0)
                    for point, value in left_counts[first_cell].items()
                )
                right_overlap = sum(
                    value * right_counts[second_cell].get(point, 0)
                    for point, value in right_counts[first_cell].items()
                )
                overlap_total += left_overlap * right_overlap
        assert overlap_total == second_moment
    assert mass**2 <= len(differences) ** 2 * collision_mass
    assert collision_mass**2 <= len(differences) ** 2 * second_moment

    return (
        len(differences),
        len(sums),
        mass,
        collision_mass,
        len(loads),
        second_moment,
        max(loads.values(), default=0),
    )


def verify_endpoint_recovery(points: list[Point]) -> None:
    decorations = endpoint_decorations(points)
    for first_value, first_decoration in decorations.items():
        for second_value, second_decoration in decorations.items():
            midpoint_difference = subtract(
                midpoint(first_decoration),
                midpoint(second_decoration),
            )
            head_code = endpoint_head_code(first_decoration, second_decoration)
            first_head, second_head = recover_heads(head_code, decorations)
            tail_difference = subtract(
                midpoint_difference,
                subtract(first_head, second_head),
            )
            if tail_difference != (0, 0):
                first_tail, second_tail = decorations[tail_difference]
            else:
                first_tail = first_decoration[1]
                second_tail = second_decoration[1]
                assert first_tail == second_tail
            assert (first_head, first_tail) == first_decoration
            assert (second_head, second_tail) == second_decoration
            assert subtract(first_head, first_tail) == first_value
            assert subtract(second_head, second_tail) == second_value


def verify_displacements() -> None:
    b_value = (7, -3)
    ell_value = (-2, 5)
    t_value = (4, 6)
    e_value = (-5, 8)
    delta = (3, 9)
    epsilon = (-7, 2)
    eta = (6, -4)

    def roles(b: Point, ell: Point, t: Point, e: Point) -> tuple[Point, ...]:
        return (
            add(add(b, t), (-e[1], e[0])),
            b,
            add(b, t),
            add(add(ell, e), t),
            add(ell, e),
            add(ell, linear(t)),
            ell,
        )

    first = roles(b_value, ell_value, t_value, e_value)

    # Common R_0: tau=-delta-J eta.
    j_eta = (-eta[1], eta[0])
    tau_zero = (-delta[0] - j_eta[0], -delta[1] - j_eta[1])
    second_zero = roles(
        add(b_value, delta),
        add(ell_value, epsilon),
        add(t_value, tau_zero),
        add(e_value, eta),
    )
    actual_zero = tuple(subtract(right, left) for left, right in zip(first, second_zero))
    expected_zero = (
        (0, 0),
        delta,
        (-j_eta[0], -j_eta[1]),
        add(add(subtract(epsilon, delta), eta), (-j_eta[0], -j_eta[1])),
        add(epsilon, eta),
        add(subtract(epsilon, linear(delta)), (eta[0] + eta[1], eta[1] - eta[0])),
        epsilon,
    )
    assert actual_zero == expected_zero

    # Common R_3: tau=-epsilon-eta.
    tau_three = (-epsilon[0] - eta[0], -epsilon[1] - eta[1])
    second_three = roles(
        add(b_value, delta),
        add(ell_value, epsilon),
        add(t_value, tau_three),
        add(e_value, eta),
    )
    actual_three = tuple(subtract(right, left) for left, right in zip(first, second_three))
    expected_three = (
        add(subtract(delta, epsilon), (-eta[0] - eta[1], eta[0] - eta[1])),
        delta,
        subtract(subtract(delta, epsilon), eta),
        (0, 0),
        add(epsilon, eta),
        add((epsilon[1], -epsilon[0]), (-eta[0] + eta[1], -eta[0] - eta[1])),
        epsilon,
    )
    assert actual_three == expected_three


def main() -> None:
    verify_endpoint_recovery(transformed_costas(13))
    verify_displacements()

    families: list[tuple[str, set[Point], Profile]] = [
        (
            "closure-30",
            difference_set(POINTS[:30]),
            (871, 62_273, 1_420, 1_496, 1_438, 1_620, 3),
        ),
        (
            "Costas-11",
            difference_set(transformed_costas(11)),
            (91, 707, 2_264, 4_348, 1_852, 21_656, 22),
        ),
        (
            "Costas-13",
            difference_set(transformed_costas(13)),
            (133, 969, 3_450, 5_530, 2_894, 21_922, 21),
        ),
        (
            "radial-4",
            radial_set(4),
            (29, 121, 8_330, 111_622, 839, 20_001_502, 378),
        ),
    ]
    if "--extended" in sys.argv:
        families.extend(
            [
                (
                    "Costas-17",
                    difference_set(transformed_costas(17)),
                    (241, 2_299, 20_014, 46_212, 14_890, 405_768, 45),
                ),
                (
                    "Costas-19",
                    difference_set(transformed_costas(19)),
                    (307, 2_927, 127_002, 468_768, 63_670, 6_956_264, 69),
                ),
                (
                    "Costas-23",
                    difference_set(transformed_costas(23)),
                    (463, 4_513, 498_674, 3_020_644, 167_536, 139_264_360, 201),
                ),
                (
                    "radial-6",
                    radial_set(6),
                    (53, 253, 93_290, 4_120_768, 2_807, 8_212_347_978, 4_369),
                ),
            ]
        )
    if "--radial-8" in sys.argv:
        families.append(
            (
                "radial-8",
                radial_set(8),
                (
                    83,
                    431,
                    555_948,
                    59_454_358,
                    6_887,
                    719_698_871_404,
                    26_158,
                ),
            )
        )

    for name, differences, expected in families:
        actual = profile(differences)
        assert actual == expected, (name, actual, expected)
        number, support, _, collision_mass, _, second_moment, maximum = actual
        ratio = second_moment / ((support / number) * collision_mass) if collision_mass else 0.0
        print(name, actual, "moment/(K M)", ratio, "max", maximum)

    print("SAME-MIDPOINT LITERAL D2 COLLISION GATE: PASS")


if __name__ == "__main__":
    main()
