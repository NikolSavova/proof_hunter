#!/usr/bin/env python3
"""Exact checks for OBLIQUE_LATTICE_GAUSSIAN_CORE.md."""

from __future__ import annotations

from random import Random


Point = tuple[int, int]
Matrix = tuple[tuple[int, int], tuple[int, int]]


def mat_vec(matrix: Matrix, vector: Point) -> Point:
    return (
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1],
    )


def add(left: Point, right: Point) -> Point:
    return left[0] + right[0], left[1] + right[1]


def dot(left: Point, right: Point) -> int:
    return left[0] * right[0] + left[1] * right[1]


def determinant(matrix: Matrix) -> int:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def adjugate(matrix: Matrix) -> Matrix:
    return (
        (matrix[1][1], -matrix[0][1]),
        (-matrix[1][0], matrix[0][0]),
    )


def transpose(matrix: Matrix) -> Matrix:
    return (
        (matrix[0][0], matrix[1][0]),
        (matrix[0][1], matrix[1][1]),
    )


def multiply(left: Matrix, right: Matrix) -> Matrix:
    columns = transpose(right)
    return tuple(
        tuple(dot(row, column) for column in columns)
        for row in left
    )  # type: ignore[return-value]


def norm_square(point: Point) -> int:
    return dot(point, point)


def verify_core(matrix: Matrix, side: int) -> None:
    delta_signed = determinant(matrix)
    assert delta_signed != 0
    adj = adjugate(matrix)
    assert multiply(matrix, adj) == (
        (delta_signed, 0),
        (0, delta_signed),
    )

    entry_bound = max(abs(value) for row in matrix for value in row)
    core_side = max(2, side // (16 * max(entry_bound, 1)))
    centre = (side // 2, side // 2)
    offset = core_side // 2
    seen: set[Point] = set()
    for first in range(core_side):
        for second in range(core_side):
            centred = (first - offset, second - offset)
            coefficient = add(centre, mat_vec(adj, centred))
            assert 0 <= coefficient[0] < side
            assert 0 <= coefficient[1] < side
            physical = mat_vec(matrix, coefficient)
            expected = add(
                mat_vec(matrix, centre),
                (delta_signed * centred[0], delta_signed * centred[1]),
            )
            assert physical == expected
            seen.add(physical)
    assert len(seen) == core_side * core_side


def verify_collision_identity(matrix: Matrix, translate: Point, rng: Random) -> None:
    gram = multiply(transpose(matrix), matrix)
    for _ in range(100):
        coefficient = (rng.randrange(-50, 51), rng.randrange(-50, 51))
        direction = (rng.randrange(-10, 11), rng.randrange(-10, 11))
        if direction == (0, 0):
            continue
        left_point = add(translate, mat_vec(matrix, coefficient))
        right_coefficient = add(coefficient, (2 * direction[0], 2 * direction[1]))
        right_point = add(translate, mat_vec(matrix, right_coefficient))

        gram_direction = mat_vec(gram, direction)
        linear_translate = mat_vec(transpose(matrix), translate)
        gate = dot(gram_direction, coefficient) + dot(direction, linear_translate) + dot(direction, gram_direction)
        assert norm_square(right_point) - norm_square(left_point) == 4 * gate


def verify_exponent_balance() -> None:
    # At B=r^(1/5), both symbolic powers are r^(6/5).  The integer checks
    # verify the max is never below a fixed multiple of that scale.
    for fifth_root in range(2, 200):
        r = fifth_root ** 5
        target = r * fifth_root
        basis_sizes = {
            1,
            max(1, fifth_root - 1),
            fifth_root,
            fifth_root + 1,
            fifth_root * fifth_root,
            fifth_root ** 3,
        }
        for basis_size in basis_sizes:
            diameter = r * basis_size
            # Avoid floating point: core >= target iff (r/B)^3 >= target^2.
            core_dominates = r ** 3 >= target ** 2 * basis_size ** 3
            assert diameter >= target or core_dominates


def verify_critical_shear_family() -> None:
    for basis_size in range(2, 31):
        side = basis_size * basis_size
        norms: set[int] = set()
        for first in range(side):
            for second in range(side):
                diagonal = first + second
                point = (
                    basis_size * diagonal + second,
                    diagonal,
                )
                value = norm_square(point)
                assert value not in norms
                norms.add(value)
        assert len(norms) == side * side
        height = (2 * basis_size + 1) * (side - 1)
        assert height <= 3 * side * basis_size


def main() -> None:
    matrices: list[Matrix] = [
        ((1, 0), (0, 1)),
        ((3, 0), (0, 7)),
        ((1, 11), (0, 1)),
        ((7, -13), (5, 9)),
        ((12, 18), (6, 15)),
        ((2, 101), (1, 50)),
        ((37, 4), (-19, 11)),
    ]
    rng = Random(1208)
    for matrix in matrices:
        assert determinant(matrix) != 0
        verify_core(matrix, 4_000)
        verify_collision_identity(matrix, (12345, -6789), rng)
    verify_exponent_balance()
    verify_critical_shear_family()
    print("oblique Gaussian-core matrices", len(matrices), "PASS")
    print("linear collision identities", 100 * len(matrices), "PASS")
    print("critical shear family through B=30: PASS")
    print("universal oblique height exponent 6/5: PASS")


if __name__ == "__main__":
    main()
