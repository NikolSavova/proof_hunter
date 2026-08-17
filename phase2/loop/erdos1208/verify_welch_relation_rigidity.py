#!/usr/bin/env python3
"""Exact modular certificates for rigidity of three Welch relation systems.

For a fixed difference d=p-q, every local relation

    z_u-z_v+i(z_x-z_y)=z_p-z_q

is a homogeneous Gaussian-linear equation in the point labels z_j.  The
constant vector and the Welch coordinate vector are always in its kernel, so
the rank is at most N-2.  A rank N-2 reduction modulo a Gaussian prime proves
that the characteristic-zero rank is exactly N-2.
"""

from __future__ import annotations

from analyze_affine_costas_energy import welch
from search_welch_transverse_subsets import full_difference_data


MODULUS = 65_537
SQRT_MINUS_ONE = 256

CASES = {
    31: {"d": (3, 1), "relations": 350},
    61: {"d": (3, -1), "relations": 1_480},
    127: {"d": (-4, 9), "relations": 6_887},
}


def relation_rows(points: list[tuple[int, int]], d: tuple[int, int]):
    edge, differences = full_difference_data(points)
    p, q = edge[d]
    rows: list[dict[int, int]] = []
    for e in differences:
        if e == (0, 0) or d[0] * e[0] + d[1] * e[1] == 0:
            continue
        f = d[0] + e[1], d[1] - e[0]
        if f not in edge:
            continue
        u, v = edge[f]
        x, y = edge[e]
        row: dict[int, int] = {}
        for index, coefficient in (
            (u, 1),
            (v, -1),
            (x, SQRT_MINUS_ONE),
            (y, -SQRT_MINUS_ONE),
            (p, -1),
            (q, 1),
        ):
            value = (row.get(index, 0) + coefficient) % MODULUS
            if value:
                row[index] = value
            else:
                row.pop(index, None)
        rows.append(row)
    return rows


def sparse_rank(rows: list[dict[int, int]]) -> int:
    basis: dict[int, dict[int, int]] = {}
    for source in rows:
        row = dict(source)
        while row:
            pivot = min(row)
            coefficient = row[pivot]
            if pivot not in basis:
                inverse = pow(coefficient, -1, MODULUS)
                basis[pivot] = {
                    index: value * inverse % MODULUS
                    for index, value in row.items()
                }
                break
            pivot_row = basis[pivot]
            for index, value in pivot_row.items():
                new_value = (row.get(index, 0) - coefficient * value) % MODULUS
                if new_value:
                    row[index] = new_value
                else:
                    row.pop(index, None)
    return len(basis)


def row_dot(row: dict[int, int], vector: list[int]) -> int:
    return sum(value * vector[index] for index, value in row.items()) % MODULUS


def main() -> None:
    assert SQRT_MINUS_ONE * SQRT_MINUS_ONE % MODULUS == MODULUS - 1
    for prime, expected in CASES.items():
        points = welch(prime)
        rows = relation_rows(points, expected["d"])
        assert len(rows) == expected["relations"]

        constants = [1] * len(points)
        coordinates = [
            (x + SQRT_MINUS_ONE * y) % MODULUS for x, y in points
        ]
        assert all(row_dot(row, constants) == 0 for row in rows)
        assert all(row_dot(row, coordinates) == 0 for row in rows)

        rank = sparse_rank(rows)
        assert rank == len(points) - 2
        print(prime, len(points), len(rows), rank)
    print("PASS")


if __name__ == "__main__":
    main()
