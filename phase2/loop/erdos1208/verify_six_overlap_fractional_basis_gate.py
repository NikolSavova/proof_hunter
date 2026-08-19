#!/usr/bin/env python3
"""Exact checks for SIX_OVERLAP_FRACTIONAL_BASIS_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import prod

from analyze_affine_costas_energy import welch
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    charge_profile,
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
Matrix = list[list[int]]


EXCLUDED = {(0, 2, 4, 5), (1, 2, 3, 4)}
VALID_BASES = [
    basis for basis in combinations(range(6), 4) if basis not in EXCLUDED
]
SPECIAL = {
    (0, 1, 2, 4),
    (0, 2, 3, 4),
    (1, 2, 4, 5),
    (2, 3, 4, 5),
}


def matrix_add(*matrices: Matrix) -> Matrix:
    return [
        [sum(matrix[row][column] for matrix in matrices) for column in range(8)]
        for row in range(2)
    ]


def matrix_negate(matrix: Matrix) -> Matrix:
    return [[-entry for entry in row] for row in matrix]


def matrix_rotate(matrix: Matrix) -> Matrix:
    return [[-entry for entry in matrix[1]], matrix[0][:]]


def rational_rank(matrix: Matrix) -> int:
    work = [[Fraction(entry) for entry in row] for row in matrix]
    row = 0
    for column in range(8):
        pivot = next(
            (index for index in range(row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        value = work[row][column]
        work[row] = [entry / value for entry in work[row]]
        for index in range(len(work)):
            if index == row or not work[index][column]:
                continue
            value = work[index][column]
            work[index] = [
                entry - value * pivot_entry
                for entry, pivot_entry in zip(work[index], work[row])
            ]
        row += 1
    return row


def six_form_matrices() -> list[Matrix]:
    forms: list[Matrix] = []
    for position in range(4):
        matrix = [[0] * 8 for _ in range(2)]
        matrix[0][2 * position] = 1
        matrix[1][2 * position + 1] = 1
        forms.append(matrix)
    a_value, b_value, c_value, d_value = forms
    e_value = matrix_add(d_value, b_value, matrix_negate(c_value))
    f_value = matrix_add(
        e_value,
        matrix_rotate(matrix_add(a_value, matrix_negate(c_value))),
    )
    return forms + [e_value, f_value]


def verify_fractional_bases() -> None:
    forms = six_form_matrices()
    actual_excluded: set[tuple[int, ...]] = set()
    for basis in combinations(range(6), 4):
        rank = rational_rank(sum((forms[index] for index in basis), []))
        if rank != 8:
            assert rank == 6
            actual_excluded.add(basis)
    assert actual_excluded == EXCLUDED

    weights = {
        basis: Fraction(1, 10) if basis in SPECIAL else Fraction(1, 15)
        for basis in VALID_BASES
    }
    assert sum(weights.values()) == 1
    for index in range(6):
        assert sum(
            weight for basis, weight in weights.items() if index in basis
        ) == Fraction(2, 3)

    a_value, b_value, c_value, _ = forms[:4]
    popular_first = matrix_add(b_value, matrix_negate(a_value))
    popular_second = matrix_add(c_value, matrix_negate(a_value))
    eight_forms = forms + [popular_first, popular_second]
    valid_pairs: set[tuple[int, int]] = set()
    for left, right in combinations(range(6), 2):
        rank = rational_rank(
            sum((eight_forms[index] for index in (left, right, 6, 7)), [])
        )
        if rank == 8:
            valid_pairs.add((left, right))
        else:
            assert rank == 6
    assert valid_pairs == {
        (left, right) for left in range(3) for right in range(3, 6)
    }
    for index in range(6):
        assert Fraction(
            sum(index in pair for pair in valid_pairs), len(valid_pairs)
        ) == Fraction(1, 3)


def all_preimages(
    differences: set[Point],
) -> tuple[dict[tuple[Point, Point], list[tuple[Point, Point]]], set[Point]]:
    fibres, _, popular = rich_fibres(differences, adaptive=True)
    preimages: dict[tuple[Point, Point], list[tuple[Point, Point]]] = defaultdict(list)
    for (start, ordinary_sum), fibre in fibres.items():
        other_label = subtract(ordinary_sum, start)
        for shift in fibre:
            fixed_v = subtract(other_label, linear(shift))
            b_value = add(start, shift)
            for other_shift in fibre:
                if shift == other_shift:
                    continue
                fixed_t = add(scale(2, start), other_shift)
                preimages[(fixed_v, fixed_t)].append((start, b_value))
    return preimages, popular


def displacement_list(delta: Point, epsilon: Point) -> tuple[Point, ...]:
    return (
        delta,
        epsilon,
        scale(-1, delta),
        rotate(subtract(epsilon, delta)),
        add(conjugate_linear(delta), linear(epsilon)),
        linear(add(delta, epsilon)),
    )


def audit_family(points: list[Point], expected: tuple[int, int, int]) -> None:
    differences = difference_set(points)
    overlaps = overlap_table(differences)
    preimages, popular = all_preimages(differences)
    popular_overlaps = overlap_table(popular)
    collision_offsets: Counter[tuple[Point, Point]] = Counter()

    for values in preimages.values():
        for first in values:
            for second in values:
                if first == second:
                    continue
                collision_offsets[
                    (subtract(second[0], first[0]), subtract(second[1], first[1]))
                ] += 1

    total = sum(collision_offsets.values())
    maximum = max(collision_offsets.values(), default=0)
    assert (total, len(collision_offsets), maximum) == expected

    profile = charge_profile(differences, adaptive=True)
    assert total == profile[3] - profile[0]

    worst_numerator = 0
    worst_denominator = 1
    refined_numerator = 0
    refined_denominator = 1
    for (delta, epsilon), count in collision_offsets.items():
        shifts = displacement_list(delta, epsilon)
        overlap_sizes = [len(overlaps.get(shift, ())) for shift in shifts]
        assert all(overlap_sizes)

        basis_bound = min(
            prod(overlap_sizes[index] for index in basis)
            for basis in VALID_BASES
        )
        assert count <= basis_bound

        cubed_bound = prod(value * value for value in overlap_sizes)
        assert count**3 <= cubed_bound

        if count * worst_denominator > worst_numerator * basis_bound:
            worst_numerator = count
            worst_denominator = basis_bound

        first_popular = len(popular_overlaps.get(subtract(epsilon, delta), ()))
        second_popular = len(popular_overlaps.get(scale(2, delta), ()))
        assert first_popular and second_popular
        refined_bound = min(
            first_popular
            * second_popular
            * overlap_sizes[left]
            * overlap_sizes[right]
            for left in range(3)
            for right in range(3, 6)
        )
        assert count <= refined_bound
        refined_cubed = (
            first_popular**3
            * second_popular**3
            * prod(overlap_sizes)
        )
        assert count**3 <= refined_cubed
        if count * refined_denominator > refined_numerator * refined_bound:
            refined_numerator = count
            refined_denominator = refined_bound

    print(
        "collision profile",
        expected,
        "worst minimum-basis ratio",
        f"{worst_numerator}/{worst_denominator}",
        "worst refined ratio",
        f"{refined_numerator}/{refined_denominator}",
    )


def main() -> None:
    verify_fractional_bases()
    print("fractional basis: PASS")

    audit_family(POINTS[:40], (104_596, 8_802, 1_224))

    matrix = (-5, -2, -1, -5)
    costas = [
        (
            matrix[0] * x + matrix[1] * y,
            matrix[2] * x + matrix[3] * y,
        )
        for x, y in welch(23)
    ]
    audit_family(costas, (759_844, 1_458, 19_908))
    print("SIX-OVERLAP FRACTIONAL-BASIS GATE: PASS")


if __name__ == "__main__":
    main()
