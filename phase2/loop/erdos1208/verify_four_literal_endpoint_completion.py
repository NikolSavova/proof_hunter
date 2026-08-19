#!/usr/bin/env python3
"""Exact checks for FOUR_LITERAL_ENDPOINT_COMPLETION_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
import sys

from analyze_cross_endpoint_pair_charge import iter_records
from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_endpoint_cross_switched_collision_charge import endpoint_decorations
from verify_orthogonal_two_support_gate import difference_set
from verify_radial_orthogonal_product_barrier import radial_set
from verify_seven_incidence_opposite_endpoint_charge import add, linear, subtract


Point = tuple[int, int]
GenuineProfile = tuple[int, int, int, int, int]
RadialProfile = tuple[int, int, int]


def rotate(point: Point) -> Point:
    return -point[1], point[0]


def negate(point: Point) -> Point:
    return -point[0], -point[1]


def roles_from_literals(
    x_value: Point,
    y_value: Point,
    d_value: Point,
    f_value: Point,
    p_value: Point,
    q_value: Point,
) -> tuple[tuple[Point, ...], tuple[Point, ...], Point, Point]:
    constant = subtract(add(d_value, f_value), add(x_value, y_value))
    p_prime = add(p_value, rotate(subtract(constant, q_value)))
    q_prime = add(add(p_prime, x_value), subtract(q_value, f_value))

    first = (
        x_value,
        add(x_value, q_value),
        add(x_value, p_value),
        add(d_value, subtract(p_value, q_value)),
        d_value,
        add(d_value, subtract(p_value, linear(q_value))),
        subtract(d_value, rotate(p_value)),
    )
    second = (
        subtract(f_value, p_prime),
        add(x_value, q_value),
        f_value,
        y_value,
        subtract(add(add(x_value, y_value), q_value), f_value),
        subtract(y_value, rotate(q_prime)),
        subtract(d_value, rotate(p_value)),
    )
    return first, second, p_prime, q_prime


def verify_parametrization() -> None:
    x_value = (7, -3)
    y_value = (-11, 5)
    d_value = (4, 13)
    f_value = (-9, -2)
    p_value = (6, -8)
    q_value = (-5, 12)
    first, second, p_prime, q_prime = roles_from_literals(
        x_value,
        y_value,
        d_value,
        f_value,
        p_value,
        q_value,
    )
    assert first[0] == x_value
    assert first[4] == d_value
    assert second[3] == y_value
    assert second[2] == f_value
    assert first[1] == second[1]
    assert first[6] == second[6]
    assert subtract(first[2], first[0]) == p_value
    assert subtract(first[1], first[0]) == q_value
    assert subtract(second[2], second[0]) == p_prime
    assert subtract(second[1], second[0]) == q_prime

    r_value = (3, 9)
    s_value = (-7, 2)
    shifted_first, shifted_second, shifted_p_prime, shifted_q_prime = (
        roles_from_literals(
            x_value,
            y_value,
            d_value,
            f_value,
            add(p_value, r_value),
            add(q_value, s_value),
        )
    )
    first_displacements = tuple(
        subtract(right, left) for left, right in zip(first, shifted_first)
    )
    second_displacements = tuple(
        subtract(right, left) for left, right in zip(second, shifted_second)
    )
    assert first_displacements == (
        (0, 0),
        s_value,
        r_value,
        subtract(r_value, s_value),
        (0, 0),
        subtract(r_value, linear(s_value)),
        negate(rotate(r_value)),
    )
    assert second_displacements == (
        subtract(rotate(s_value), r_value),
        s_value,
        (0, 0),
        (0, 0),
        s_value,
        negate(add(rotate(r_value), linear(s_value))),
        negate(rotate(r_value)),
    )
    assert subtract(shifted_p_prime, p_prime) == subtract(
        r_value, rotate(s_value)
    )
    assert subtract(shifted_q_prime, q_prime) == add(
        r_value, subtract(s_value, rotate(s_value))
    )


def grouped_records(differences: set[Point]) -> dict[tuple[Point, Point], list[tuple[Point, ...]]]:
    groups: dict[tuple[Point, Point], list[tuple[Point, ...]]] = defaultdict(list)
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
    return groups


def verify_cell_injectivity(groups: dict[tuple[Point, Point], list[tuple[Point, ...]]]) -> None:
    for records in groups.values():
        left = {(record[0], record[4]) for record in records}
        right = {(record[3], record[2]) for record in records}
        assert len(left) == len(records)
        assert len(right) == len(records)


def literal_loads(
    groups: dict[tuple[Point, Point], list[tuple[Point, ...]]]
) -> tuple[int, Counter[tuple[Point, Point, Point, Point]]]:
    loads: Counter[tuple[Point, Point, Point, Point]] = Counter()
    collision_mass = 0
    for records in groups.values():
        collision_mass += len(records) ** 2
        for first in records:
            for second in records:
                loads[(first[0], second[3], first[4], second[2])] += 1
    return collision_mass, loads


def genuine_profile(points: list[Point]) -> GenuineProfile:
    differences = difference_set(points)
    decorations = endpoint_decorations(points)
    groups = grouped_records(differences)
    verify_cell_injectivity(groups)
    collision_mass, literal = literal_loads(groups)

    head_loads: Counter[tuple[Point, Point, Point, Point]] = Counter()
    tails: dict[tuple[Point, Point, Point, Point], set[tuple[Point, Point]]] = (
        defaultdict(set)
    )
    for (x_value, y_value, d_value, f_value), multiplicity in literal.items():
        head_key = (
            x_value,
            y_value,
            decorations[d_value][0],
            decorations[f_value][0],
        )
        head_loads[head_key] += multiplicity
        tails[head_key].add((d_value, f_value))

    literal_moment = sum(value * value for value in literal.values())
    head_moment = sum(value * value for value in head_loads.values())
    tail_weighted = sum(
        len(tails[(x_value, y_value, decorations[d_value][0], decorations[f_value][0])])
        * value
        * value
        for (x_value, y_value, d_value, f_value), value in literal.items()
    )
    assert head_moment <= tail_weighted
    return (
        collision_mass,
        literal_moment,
        tail_weighted,
        max(literal.values(), default=0),
        max((len(values) for values in tails.values()), default=0),
    )


def radial_profile(differences: set[Point]) -> RadialProfile:
    groups = grouped_records(differences)
    verify_cell_injectivity(groups)
    collision_mass, literal = literal_loads(groups)
    return (
        collision_mass,
        sum(value * value for value in literal.values()),
        max(literal.values(), default=0),
    )


def main() -> None:
    verify_parametrization()

    families: list[tuple[str, int, GenuineProfile]] = [
        ("Costas-11", 11, (4_348, 4_528, 4_987, 3, 3)),
        ("Costas-13", 13, (5_530, 5_770, 6_600, 3, 3)),
        ("Costas-17", 17, (46_212, 51_896, 64_670, 4, 7)),
        ("Costas-19", 19, (468_768, 554_424, 643_385, 6, 5)),
        ("Costas-23", 23, (3_020_644, 4_188_520, 5_881_823, 9, 8)),
    ]
    if "--extended" in sys.argv:
        families.extend(
            [
                ("Costas-29", 29, (11_791_516, 20_407_716, 28_848_423, 14, 8)),
                ("Costas-31", 31, (3_872_958, 6_992_486, 8_944_592, 17, 8)),
                ("Costas-37", 37, (18_630_176, 28_102_892, 33_355_193, 12, 5)),
            ]
        )

    for name, prime, expected in families:
        actual = genuine_profile(transformed_costas(prime))
        assert actual == expected, (name, actual, expected)
        collision_mass, literal_moment, tail_weighted, maximum, diversity = actual
        print(
            name,
            actual,
            "literal/M",
            literal_moment / collision_mass,
            "tail/literal",
            tail_weighted / literal_moment,
            "max",
            maximum,
            diversity,
        )

    radial_families: list[tuple[str, int, RadialProfile]] = [
        ("radial-4", 4, (111_622, 328_710, 12)),
        ("radial-6", 6, (4_120_768, 35_214_340, 36)),
    ]
    if "--radial-8" in sys.argv:
        radial_families.append(
            ("radial-8", 8, (59_454_358, 1_259_626_422, 92))
        )
    for name, side, expected in radial_families:
        actual = radial_profile(radial_set(side))
        assert actual == expected, (name, actual, expected)
        collision_mass, literal_moment, maximum = actual
        print(
            name,
            actual,
            "literal/M",
            literal_moment / collision_mass,
            "max",
            maximum,
        )

    print("FOUR-LITERAL ENDPOINT COMPLETION GATE: PASS")


if __name__ == "__main__":
    main()
