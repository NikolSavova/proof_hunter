#!/usr/bin/env python3
"""Exact finite certificate for the eight-corner product barrier.

The accompanying note proves a generic-product lemma.  This verifier checks
all finite inputs used by that proof:

* the six integer base points form a transverse relation and are
  distance-Sidon;
* for each of the eight corners there is a clean transverse completion in
  the exact 60-point distance-Sidon witness;
* the nine mixed quadratic matrices for two independent completion blocks
  distinguish all ordered pairs of endpoint roles, for every pair of corner
  types;
* every coordinate projection is onto and every within-block difference is
  nonconstant;
* the exploratory 120-point closure remains exactly distance-Sidon and has
  the claimed corner degrees.

All arithmetic in this script is integral.
"""

from __future__ import annotations

from search_rotated_support import is_distance_sidon
from search_transverse_eight_corner_closure import (
    BASE_RELATION,
    EXTENSION_101_TO_120,
    EXTENSION_TO_100,
    completion_degrees,
    corner_key,
    is_transverse_relation,
)
from verify_transverse_closure_witness import POINTS


Point = tuple[int, int]
Matrix = tuple[tuple[int, ...], ...]


SEED_RELATIONS = (
    ((37, 25), (36, 22), (9, 10)),
    ((25, 6), (36, 47), (9, 38)),
    ((37, 10), (17, 5), (9, 33)),
    ((0, 6), (21, 5), (9, 3)),
    ((37, 16), (36, 10), (21, 19)),
    ((39, 6), (36, 15), (10, 19)),
    ((37, 32), (31, 5), (41, 19)),
    ((43, 6), (23, 5), (31, 19)),
)


def add(x: Point, y: Point) -> Point:
    return x[0] + y[0], x[1] + y[1]


def subtract(x: Point, y: Point) -> Point:
    return x[0] - y[0], x[1] - y[1]


def rotate(x: Point) -> Point:
    return -x[1], x[0]


def relation_identity(points: list[Point], roles: tuple[tuple[int, int], ...]) -> bool:
    d = subtract(points[roles[0][0]], points[roles[0][1]])
    f = subtract(points[roles[1][0]], points[roles[1][1]])
    e = subtract(points[roles[2][0]], points[roles[2][1]])
    return d == add(f, rotate(e))


def matrix_scale(value: int, matrix: Matrix) -> Matrix:
    return tuple(tuple(value * entry for entry in row) for row in matrix)


def horizontal(left: Matrix, right: Matrix) -> Matrix:
    return tuple(left[row] + right[row] for row in range(len(left)))


def transpose_multiply(left: Matrix, right: Matrix) -> Matrix:
    assert len(left) == len(right) == 2
    return tuple(
        tuple(
            sum(left[row][i] * right[row][j] for row in range(2))
            for j in range(len(right[0]))
        )
        for i in range(len(left[0]))
    )


def subtract_matrix(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a - b for a, b in zip(left_row, right_row))
        for left_row, right_row in zip(left, right)
    )


def rank_two(matrix: Matrix) -> bool:
    assert len(matrix) == 2
    columns = len(matrix[0])
    return any(
        matrix[0][i] * matrix[1][j] - matrix[0][j] * matrix[1][i] != 0
        for i in range(columns)
        for j in range(i + 1, columns)
    )


def nonzero(matrix: Matrix) -> bool:
    return any(entry != 0 for row in matrix for entry in row)


def linear_maps(mask: int) -> tuple[Matrix, Matrix, Matrix]:
    """Linear parts of the three moving complementary endpoints.

    With free deviations u and v in roles 1 and 2, the role-0 deviation is
    alpha*u + beta*J*v, where alpha,beta are signs determined by the corner.
    """

    epsilon = tuple((mask >> role) & 1 for role in range(3))
    s0 = 2 * epsilon[0] - 1
    s1 = 1 - 2 * epsilon[1]
    s2 = 1 - 2 * epsilon[2]
    alpha = -s1 * s0
    beta = -s2 * s0

    identity: Matrix = ((1, 0), (0, 1))
    zero: Matrix = ((0, 0), (0, 0))
    quarter_turn: Matrix = ((0, -1), (1, 0))
    return (
        horizontal(matrix_scale(alpha, identity), matrix_scale(beta, quarter_turn)),
        horizontal(identity, zero),
        horizontal(zero, identity),
    )


def verify_base_and_seeds() -> None:
    points = list(POINTS[:60])
    assert is_distance_sidon(points)
    assert relation_identity(points, BASE_RELATION)
    assert is_transverse_relation(points, BASE_RELATION)

    base_indices = {index for pair in BASE_RELATION for index in pair}
    assert len(base_indices) == 6
    assert is_distance_sidon([points[index] for index in sorted(base_indices)])

    for mask, roles in enumerate(SEED_RELATIONS):
        assert relation_identity(points, roles)
        assert is_transverse_relation(points, roles)
        assert corner_key(roles, mask) == corner_key(BASE_RELATION, mask)
        complements = tuple(roles[role][1 - ((mask >> role) & 1)] for role in range(3))
        assert len(set(complements)) == 3
        assert not (set(complements) & base_indices)
        local_indices = sorted(base_indices | set(complements))
        assert len(local_indices) == 9
        assert is_distance_sidon([points[index] for index in local_indices])
        print("seed", mask, "corner", corner_key(BASE_RELATION, mask), "complements", complements)


def verify_linear_algebra() -> None:
    maps = [linear_maps(mask) for mask in range(8)]
    for mask in range(8):
        for role in range(3):
            assert rank_two(maps[mask][role])
        for first in range(3):
            for second in range(first + 1, 3):
                assert nonzero(subtract_matrix(maps[mask][first], maps[mask][second]))

    # If two edges join the same two independent completion blocks, the
    # mixed quadratic coefficient L_r^T L'_s identifies (r,s) uniquely.
    for first_mask in range(8):
        for second_mask in range(8):
            seen: dict[Matrix, tuple[int, int]] = {}
            for first_role in range(3):
                for second_role in range(3):
                    mixed = transpose_multiply(
                        maps[first_mask][first_role],
                        maps[second_mask][second_role],
                    )
                    assert mixed not in seen, (
                        first_mask,
                        second_mask,
                        seen.get(mixed),
                        (first_role, second_role),
                    )
                    seen[mixed] = (first_role, second_role)
            assert len(seen) == 9
    print("mixed-matrix checks", 8 * 8 * 9)


def verify_finite_closure() -> None:
    points = list(POINTS[:60]) + EXTENSION_TO_100 + EXTENSION_101_TO_120
    assert len(points) == 120
    assert is_distance_sidon(points)
    degrees = completion_degrees(points, BASE_RELATION)
    assert degrees == [43, 56, 54, 43, 43, 54, 56, 43]
    print("closure points", len(points))
    print("closure degrees", degrees)
    print("closure minimum", min(degrees))


def main() -> None:
    verify_base_and_seeds()
    verify_linear_algebra()
    verify_finite_closure()
    print("all exact eight-corner product-barrier checks passed")


if __name__ == "__main__":
    main()
