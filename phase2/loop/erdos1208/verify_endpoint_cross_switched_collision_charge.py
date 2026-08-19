#!/usr/bin/env python3
"""Exact checks for ENDPOINT_CROSS_SWITCHED_COLLISION_CHARGE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
import sys

from analyze_cross_endpoint_pair_charge import iter_records
from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import add, subtract
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Decoration = tuple[Point, Point]
Profile = tuple[int, int, int, int, int, int, int, int, int]


def endpoint_decorations(points: list[Point]) -> dict[Point, Decoration]:
    """The unique directed endpoint decoration, with one fixed zero anchor."""
    answer: dict[Point, Decoration] = {(0, 0): (points[0], points[0])}
    for left in points:
        for right in points:
            if left == right:
                continue
            value = subtract(left, right)
            previous = answer.setdefault(value, (left, right))
            assert previous == (left, right)
    return answer


def midpoint(decoration: Decoration) -> Point:
    return add(*decoration)


def endpoint_head_code(
    left: Decoration,
    right: Decoration,
) -> tuple[int, Point]:
    """Encode and recover the two heads, including their common-head route."""
    left_head = left[0]
    right_head = right[0]
    value = subtract(left_head, right_head)
    if value != (0, 0):
        return 0, value
    assert left_head == right_head
    return 1, left_head


def recover_heads(
    code: tuple[int, Point],
    decorations: dict[Point, Decoration],
) -> tuple[Point, Point]:
    route, value = code
    if route == 0:
        assert value != (0, 0)
        return decorations[value]
    assert route == 1
    return value, value


def charge_profile(points: list[Point]) -> Profile:
    differences = difference_set(points)
    decorations = endpoint_decorations(points)
    assert set(decorations) == differences
    sums = {add(left, right) for left in differences for right in differences}

    groups: dict[tuple[Point, Point], list[tuple[Point, ...]]] = defaultdict(list)
    off_diagonal_mass = 0
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
        first_stage_key = row[1], row[6]
        groups[first_stage_key].append(row)
        off_diagonal_mass += 1

    loads: Counter[tuple[Point, tuple[int, Point]]] = Counter()
    collision_mass = 0
    within_excess = 0
    within_maximum = 0

    for (fixed_head, fixed_opposite), records in groups.items():
        local: Counter[tuple[Point, tuple[int, Point]]] = Counter()
        for first in records:
            for second in records:
                first_midpoint = midpoint(decorations[first[0]])
                second_midpoint = midpoint(decorations[second[3]])
                midpoint_difference = subtract(first_midpoint, second_midpoint)
                assert midpoint_difference in sums

                head_code = endpoint_head_code(
                    decorations[first[4]],
                    decorations[second[2]],
                )
                recovered = recover_heads(head_code, decorations)
                assert recovered == (
                    decorations[first[4]][0],
                    decorations[second[2]][0],
                )

                key = midpoint_difference, head_code
                loads[key] += 1
                local[key] += 1
                collision_mass += 1

                # Check the fixed-cell normal form from equation (3.2).
                b_value = fixed_head
                ell_value = fixed_opposite
                t_value = subtract(first[2], b_value)
                e_value = subtract(first[4], ell_value)
                assert first == (
                    add(add(b_value, t_value), (-e_value[1], e_value[0])),
                    b_value,
                    add(b_value, t_value),
                    add(add(ell_value, e_value), t_value),
                    add(ell_value, e_value),
                    add(ell_value, (t_value[0] - t_value[1],
                                    t_value[0] + t_value[1])),
                    ell_value,
                )

        within_excess += sum(value - 1 for value in local.values())
        within_maximum = max(
            within_maximum,
            max(local.values(), default=0),
        )

    assert collision_mass == sum(len(records) ** 2 for records in groups.values())
    assert off_diagonal_mass ** 2 <= len(differences) ** 2 * collision_mass
    assert len(loads) <= len(sums) * (len(differences) - 1 + len(points))

    return (
        len(differences),
        len(sums),
        off_diagonal_mass,
        collision_mass,
        len(loads),
        sum(value * value for value in loads.values()),
        max(loads.values(), default=0),
        within_excess,
        within_maximum,
    )


def main() -> None:
    families: list[tuple[str, list[Point], Profile]] = [
        (
            "closure-30",
            POINTS[:30],
            (871, 62_273, 1_420, 1_496, 1_491, 1_506, 2, 0, 1),
        ),
        (
            "Costas-11",
            transformed_costas(11),
            (91, 707, 2_264, 4_348, 3_411, 7_146, 8, 64, 3),
        ),
        (
            "Costas-13",
            transformed_costas(13),
            (133, 969, 3_450, 5_530, 4_680, 7_934, 9, 108, 3),
        ),
    ]
    if "--extended" in sys.argv:
        families.extend(
            [
                (
                    "closure-40",
                    POINTS[:40],
                    (
                        1_561,
                        156_057,
                        370_516,
                        1_139_274,
                        982_126,
                        1_854_278,
                        83,
                        11_660,
                        7,
                    ),
                ),
                (
                    "Costas-17",
                    transformed_costas(17),
                    (
                        241,
                        2_299,
                        20_014,
                        46_212,
                        33_670,
                        97_938,
                        25,
                        803,
                        4,
                    ),
                ),
                (
                    "Costas-23",
                    transformed_costas(23),
                    (
                        463,
                        4_513,
                        498_674,
                        3_020_644,
                        970_328,
                        18_156_836,
                        148,
                        75_757,
                        6,
                    ),
                ),
                (
                    "Costas-31",
                    transformed_costas(31),
                    (
                        871,
                        9_495,
                        765_102,
                        3_872_958,
                        1_736_150,
                        19_427_362,
                        256,
                        79_730,
                        12,
                    ),
                ),
            ]
        )

    for name, points, expected in families:
        actual = charge_profile(points)
        assert actual == expected, (name, actual, expected)
        _, _, _, collision_mass, _, second_moment, maximum, excess, local_max = actual
        print(
            name,
            actual,
            "size-biased load",
            second_moment / collision_mass if collision_mass else 0.0,
            "global max",
            maximum,
            "within",
            (excess, local_max),
        )

    print("ENDPOINT CROSS-SWITCHED COLLISION CHARGE: PASS")


if __name__ == "__main__":
    main()
