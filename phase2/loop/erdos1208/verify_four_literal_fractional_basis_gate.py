#!/usr/bin/env python3
"""Exact checks for FOUR_LITERAL_FRACTIONAL_BASIS_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import prod

from analyze_cross_endpoint_pair_charge import iter_records
from verify_adaptive_cross_pair_d2_charge import transformed_costas
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    conjugate_linear,
    linear,
    overlap_table,
    rich_fibres,
    rotate,
    scale,
    subtract,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Gaussian = tuple[int, int]
Form = tuple[Gaussian, ...]

ZERO: Gaussian = (0, 0)
ONE: Gaussian = (1, 0)
MINUS_ONE: Gaussian = (-1, 0)
I_VALUE: Gaussian = (0, 1)
MINUS_I: Gaussian = (0, -1)
ONE_PLUS_I: Gaussian = (1, 1)
ONE_MINUS_I: Gaussian = (1, -1)
MINUS_ONE_PLUS_I: Gaussian = (-1, 1)
MINUS_ONE_MINUS_I: Gaussian = (-1, -1)


FORMS: dict[str, Form] = {
    "P": (ZERO, ZERO, ZERO, ZERO, ONE, ZERO),
    "Q": (ZERO, ZERO, ZERO, ZERO, ZERO, ONE),
    "Pp": (MINUS_I, MINUS_I, I_VALUE, I_VALUE, ONE, MINUS_I),
    "Qp": (
        ONE_MINUS_I,
        MINUS_I,
        I_VALUE,
        MINUS_ONE_PLUS_I,
        ONE,
        ONE_MINUS_I,
    ),
    "V0": (ONE, ZERO, ZERO, ZERO, ZERO, ONE),
    "V1": (ONE, ZERO, ZERO, ZERO, ONE, ZERO),
    "V2": (ZERO, ZERO, ONE, ZERO, ONE, MINUS_ONE),
    "V3": (ZERO, ZERO, ONE, ZERO, ONE, MINUS_ONE_MINUS_I),
    "V4": (ZERO, ZERO, ONE, ZERO, MINUS_I, ZERO),
    "V5": (I_VALUE, I_VALUE, MINUS_I, ONE_MINUS_I, MINUS_ONE, I_VALUE),
    "V6": (ONE, ONE, ZERO, MINUS_ONE, ZERO, ONE),
    "V7": (
        MINUS_ONE_MINUS_I,
        ZERO,
        ONE,
        ONE_PLUS_I,
        MINUS_I,
        MINUS_ONE_MINUS_I,
    ),
}

POPULAR_NAMES = ("P", "Q", "Pp", "Qp")
HIGH_NAMES = ("V0", "V1", "V5")
LOW_NAMES = ("V2", "V3", "V4", "V7")
ALL_LOW_NAMES = ("V2", "V3", "V4", "V6", "V7")


def real_rows(form: Form) -> list[list[int]]:
    rows = [[0] * 12 for _ in range(2)]
    for index, (real, imaginary) in enumerate(form):
        rows[0][2 * index] = real
        rows[0][2 * index + 1] = -imaginary
        rows[1][2 * index] = imaginary
        rows[1][2 * index + 1] = real
    return rows


def bareiss_determinant(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    size = len(work)
    assert all(len(row) == size for row in work)
    sign = 1
    previous = 1
    for column in range(size - 1):
        pivot = next(
            (row for row in range(column, size) if work[row][column]), None
        )
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        for row in range(column + 1, size):
            for other_column in range(column + 1, size):
                numerator = (
                    work[row][other_column] * pivot_value
                    - work[row][column] * work[column][other_column]
                )
                assert numerator % previous == 0
                work[row][other_column] = numerator // previous
        previous = pivot_value
        for row in range(column + 1, size):
            work[row][column] = 0
    return sign * work[-1][-1]


def determinant(names: tuple[str, ...]) -> int:
    matrix: list[list[int]] = []
    for name in names:
        matrix.extend(real_rows(FORMS[name]))
    return bareiss_determinant(matrix)


def verify_rank_graph() -> None:
    variable_names = tuple(f"V{index}" for index in range(8))
    valid: set[tuple[str, str]] = set()
    for left, right in combinations(variable_names, 2):
        value = determinant(POPULAR_NAMES + (left, right))
        if value:
            assert abs(value) == 1
            valid.add((left, right))
    expected = {
        tuple(sorted((left, right)))
        for left in HIGH_NAMES
        for right in ALL_LOW_NAMES
    }
    assert valid == expected

    edges = tuple(product(HIGH_NAMES, LOW_NAMES))
    assert len(edges) == 12
    weights = {edge: Fraction(1, 12) for edge in edges}
    assert sum(weights.values()) == 1
    for name in HIGH_NAMES:
        assert sum(weight for edge, weight in weights.items() if name in edge) == Fraction(1, 3)
    for name in LOW_NAMES:
        assert sum(weight for edge, weight in weights.items() if name in edge) == Fraction(1, 4)

    # The maximum exponent after V0,V6 are merged cannot be below 1/3.
    # At theta=1/3 the displayed K_(3,4) weighting attains equality.
    theta = Fraction(1, 3)
    assert 1 - 2 * theta == theta


def grouped_records(
    differences: set[Point],
) -> dict[tuple[Point, Point], list[tuple[Point, ...]]]:
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


def literal_preimages(
    differences: set[Point],
) -> tuple[
    int,
    dict[tuple[Point, Point, Point, Point], list[tuple[Point, Point, Point, Point]]],
    set[Point],
]:
    groups = grouped_records(differences)
    _, _, popular = rich_fibres(differences, adaptive=True)
    preimages: dict[
        tuple[Point, Point, Point, Point],
        list[tuple[Point, Point, Point, Point]],
    ] = defaultdict(list)
    collision_mass = 0
    for records in groups.values():
        collision_mass += len(records) ** 2
        for first in records:
            p_value = subtract(first[2], first[0])
            q_value = subtract(first[1], first[0])
            assert p_value in popular and q_value in popular
            for second in records:
                p_prime = subtract(second[2], second[0])
                q_prime = subtract(second[1], second[0])
                assert p_prime in popular and q_prime in popular
                key = (first[0], second[3], first[4], second[2])
                preimages[key].append((p_value, q_value, p_prime, q_prime))

    assert sum(len(values) for values in preimages.values()) == collision_mass
    for values in preimages.values():
        assert len({(p_value, q_value) for p_value, q_value, _, _ in values}) == len(values)
    return collision_mass, preimages, popular


def d_displacements(r_value: Point, s_value: Point) -> tuple[tuple[Point, ...], tuple[Point, ...]]:
    high = (
        s_value,
        r_value,
        subtract(rotate(s_value), r_value),
    )
    low = (
        subtract(r_value, s_value),
        subtract(r_value, linear(s_value)),
        scale(-1, rotate(r_value)),
        scale(-1, add(rotate(r_value), linear(s_value))),
    )
    return high, low


def audit_family(
    name: str,
    points: list[Point],
    expected: tuple[int, int, int, int, int] | None = None,
) -> tuple[int, int, int, int, int]:
    differences = difference_set(points)
    collision_mass, preimages, popular = literal_preimages(differences)
    d_overlaps = overlap_table(differences)
    p_overlaps = overlap_table(popular)
    offsets: Counter[tuple[Point, Point]] = Counter()

    literal_moment = sum(len(values) ** 2 for values in preimages.values())
    for values in preimages.values():
        for first_index, first in enumerate(values):
            for second_index, second in enumerate(values):
                if first_index == second_index:
                    continue
                r_value = subtract(second[0], first[0])
                s_value = subtract(second[1], first[1])
                assert (r_value, s_value) != ((0, 0), (0, 0))
                assert subtract(second[2], first[2]) == subtract(
                    r_value, rotate(s_value)
                )
                assert subtract(second[3], first[3]) == add(
                    r_value, conjugate_linear(s_value)
                )
                offsets[(r_value, s_value)] += 1

    assert sum(offsets.values()) == literal_moment - collision_mass
    worst_numerator = 0
    worst_denominator = 1
    occupied_minimum_sum = 0
    for (r_value, s_value), count in offsets.items():
        popular_shifts = (
            r_value,
            s_value,
            subtract(r_value, rotate(s_value)),
            add(r_value, conjugate_linear(s_value)),
        )
        popular_sizes = [len(p_overlaps.get(shift, ())) for shift in popular_shifts]
        assert all(popular_sizes)
        popular_product = prod(popular_sizes)

        high_shifts, low_shifts = d_displacements(r_value, s_value)
        high_sizes = [len(d_overlaps.get(shift, ())) for shift in high_shifts]
        low_sizes = [len(d_overlaps.get(shift, ())) for shift in low_shifts]
        assert all(high_sizes) and all(low_sizes)

        minimum_bound = popular_product * min(
            high_size * low_size
            for high_size in high_sizes
            for low_size in low_sizes
        )
        assert count <= minimum_bound
        occupied_minimum_sum += minimum_bound
        power_bound = (
            popular_product**12
            * prod(value**4 for value in high_sizes)
            * prod(value**3 for value in low_sizes)
        )
        assert count**12 <= power_bound
        if count * worst_denominator > worst_numerator * minimum_bound:
            worst_numerator = count
            worst_denominator = minimum_bound

    profile = (
        collision_mass,
        literal_moment,
        len(offsets),
        max(offsets.values(), default=0),
        occupied_minimum_sum,
    )
    if expected is not None:
        assert profile == expected, (name, profile, expected)
    print(
        name,
        profile,
        "offdiag",
        literal_moment - collision_mass,
        "worst/min-basis",
        f"{worst_numerator}/{worst_denominator}",
        "occupied-min/M",
        f"{occupied_minimum_sum}/{collision_mass}",
    )
    return profile


def main() -> None:
    verify_rank_graph()
    print("rank graph and fractional weights: PASS")

    audit_family(
        "closure-40",
        POINTS[:40],
        (1_139_274, 1_161_442, 1_414, 670, 1_215_966_079_722),
    )
    audit_family(
        "Costas-17",
        transformed_costas(17),
        (46_212, 51_896, 160, 556, 12_952_750_200),
    )
    audit_family(
        "Costas-23",
        transformed_costas(23),
        (3_020_644, 4_188_520, 1_730, 29_298, 37_450_787_292_824),
    )
    print("FOUR-LITERAL FRACTIONAL-BASIS GATE: PASS")


if __name__ == "__main__":
    main()
