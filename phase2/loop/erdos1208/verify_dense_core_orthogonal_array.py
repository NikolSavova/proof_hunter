#!/usr/bin/env python3
"""Exact checks for the dense-core orthogonal-array gate.

The mathematical OA proof is the variance identity in the accompanying note.
This verifier independently constructs the cyclic transversal designs of
orders 3, 5, and 7, checks pair-linearity/orthogonality, and row-reduces the
real fixed-row equations over the rationals.  The only solutions have constant
coordinates inside each of the four roles.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def rref(matrix: list[list[int]]) -> tuple[list[list[Fraction]], list[int]]:
    work = [[Fraction(value) for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0])
    pivots: list[int] = []
    pivot_row = 0
    for column in range(columns):
        chosen = next(
            (row for row in range(pivot_row, rows) if work[row][column]),
            None,
        )
        if chosen is None:
            continue
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        scale = work[pivot_row][column]
        work[pivot_row] = [value / scale for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                work[row][index] - scale * work[pivot_row][index]
                for index in range(columns)
            ]
        pivots.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    return work, pivots


def nullspace(matrix: list[list[int]]) -> tuple[list[list[Fraction]], int]:
    reduced, pivots = rref(matrix)
    columns = len(reduced[0])
    free = [column for column in range(columns) if column not in pivots]
    basis: list[list[Fraction]] = []
    for free_column in free:
        vector = [Fraction(0)] * columns
        vector[free_column] = Fraction(1)
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column]
        basis.append(vector)
    return basis, len(pivots)


def cyclic_design(order: int, multiplier: int):
    return [
        (a, b, (a + b) % order, (a + multiplier * b) % order)
        for a in range(order)
        for b in range(order)
    ]


def verify_pairwise_orthogonality(edges, order: int) -> None:
    for first, second in combinations(range(4), 2):
        projection = {(edge[first], edge[second]) for edge in edges}
        assert len(projection) == order * order
        left_degree = {}
        right_degree = {}
        for left, right in projection:
            left_degree[left] = left_degree.get(left, 0) + 1
            right_degree[right] = right_degree.get(right, 0) + 1
        frobenius_squared = sum(
            Fraction(1, left_degree[left] * right_degree[right])
            for left, right in projection
        )
        # Complete bipartite projections have no nontrivial singular mass.
        assert frobenius_squared == 1


def equation_matrix(order: int, edges) -> list[list[int]]:
    # Two real coordinates for each of 4*order role labels, followed by d_x,d_y.
    point_variables = 4 * order
    columns = 2 * point_variables + 2
    d_x = 2 * point_variables
    d_y = d_x + 1
    matrix: list[list[int]] = []

    def point_index(role: int, label: int) -> int:
        return role * order + label

    def add_complex_multiple(rows, role, label, multiplier):
        base = 2 * point_index(role, label)
        if multiplier == 1:
            rows[0][base] += 1
            rows[1][base + 1] += 1
        elif multiplier == -1:
            rows[0][base] -= 1
            rows[1][base + 1] -= 1
        elif multiplier == "J":
            rows[0][base + 1] -= 1
            rows[1][base] += 1
        elif multiplier == "-J":
            rows[0][base + 1] += 1
            rows[1][base] -= 1
        else:
            raise AssertionError(multiplier)

    for u, v, x, y in edges:
        rows = [[0] * columns for _ in range(2)]
        add_complex_multiple(rows, 0, u, 1)
        add_complex_multiple(rows, 1, v, -1)
        add_complex_multiple(rows, 2, x, "J")
        add_complex_multiple(rows, 3, y, "-J")
        rows[0][d_x] -= 1
        rows[1][d_y] -= 1
        matrix.extend(rows)
    return matrix


def verify_rigidity(order: int, multiplier: int) -> None:
    edges = cyclic_design(order, multiplier)
    assert len(edges) == order * order
    verify_pairwise_orthogonality(edges, order)

    matrix = equation_matrix(order, edges)
    basis, rank = nullspace(matrix)
    variables = 8 * order + 2
    assert rank == variables - 8
    assert len(basis) == 8

    # Every null vector has identical real and imaginary coordinates within a
    # role.  The remaining eight real freedoms are the four constant complex
    # role values subject to the shared definition of d.
    for role in range(4):
        for label in range(1, order):
            first = 2 * (role * order)
            current = 2 * (role * order + label)
            for vector in basis:
                assert vector[first] == vector[current]
                assert vector[first + 1] == vector[current + 1]


def prune_core(edges, part_size: int):
    """Implement the exact r/(8k) deletion used in the pruning lemma."""

    surviving = set(range(len(edges)))
    threshold = Fraction(len(edges), 8 * part_size)
    while True:
        degrees = {}
        for index in surviving:
            for role, label in enumerate(edges[index]):
                degrees[(role, label)] = degrees.get((role, label), 0) + 1
        low = next(
            (vertex for vertex, degree in degrees.items() if degree < threshold),
            None,
        )
        if low is None:
            break
        role, label = low
        surviving = {
            index for index in surviving if edges[index][role] != label
        }
    assert len(surviving) * 2 >= len(edges)
    return surviving, threshold


def verify_pruning() -> None:
    # A deliberately irregular four-partite linear example: start with the
    # cyclic design and append degree-one leaves.  The lemma is checked from
    # the actual deletion procedure, independently of the rigidity assertion.
    core = cyclic_design(17, 2)
    leaves = [
        (17 + index, 17 + index, 17 + index, 17 + index)
        for index in range(20)
    ]
    edges = core + leaves
    for first, second in combinations(range(4), 2):
        assert len({(edge[first], edge[second]) for edge in edges}) == len(edges)
    surviving, threshold = prune_core(edges, part_size=37)
    assert len(surviving) == len(core)
    assert threshold == Fraction(len(edges), 8 * 37) > 1


def main() -> None:
    verify_pruning()
    for order, multiplier in ((3, 2), (5, 2), (7, 2)):
        verify_rigidity(order, multiplier)
        print(f"cyclic OA({order ** 2},4,{order},2): pairwise complete, rigid")
    print("dense-core pruning and orthogonal-array rigidity: PASS")


if __name__ == "__main__":
    main()
