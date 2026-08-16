#!/usr/bin/env python3
"""Exact verifier for SHARED_ENDPOINT_SATURATION_BARRIER.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


Point = tuple[Fraction, Fraction]
Root = tuple[int, int]


def points(n: int) -> tuple[Point, ...]:
    delta = Fraction(1, 10 * n**4)
    return tuple((Fraction(i), Fraction(i * i) + delta * i**3) for i in range(n))


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def slope(a: Point, b: Point) -> Fraction:
    return (b[1] - a[1]) / (b[0] - a[0])


def root_order_and_word(q: tuple[Point, ...]) -> tuple[tuple[Root, ...], tuple[int, ...]]:
    n = len(q)
    decorated = sorted(
        (slope(q[i], q[j]), i, j) for i, j in combinations(range(n), 2)
    )
    assert len({entry[0] for entry in decorated}) == len(decorated)
    roots = tuple((i, j) for _, i, j in decorated)

    wires = list(range(n))
    word = []
    for i, j in roots:
        left = wires.index(i)
        right = wires.index(j)
        assert abs(left - right) == 1
        generator = min(left, right)
        assert wires[generator] < wires[generator + 1]
        word.append(generator)
        wires[generator], wires[generator + 1] = (
            wires[generator + 1],
            wires[generator],
        )
    assert wires == list(reversed(range(n)))
    assert len(word) == n * (n - 1) // 2
    return roots, tuple(word)


def product(n: int, roots: tuple[Root, ...], activity: Fraction) -> list[list[Fraction]]:
    matrix = [
        [Fraction(int(row == column)) for column in range(n)] for row in range(n)
    ]
    for i, j in roots:
        matrix[j] = [
            left + activity * right for left, right in zip(matrix[j], matrix[i])
        ]
    return matrix


def audit(n: int) -> dict[str, Fraction | int]:
    q = points(n)
    assert all(orient(q[i], q[j], q[k]) > 0 for i, j, k in combinations(range(n), 3))
    roots, word = root_order_and_word(q)
    assert len(word) == n * (n - 1) // 2

    one = Fraction(1)
    half = Fraction(1, 2)
    forward_one = product(n, roots, one)
    backward_one = product(n, tuple(reversed(roots)), one)
    forward_half = product(n, roots, half)
    backward_half = product(n, tuple(reversed(roots)), half)

    total_half = Fraction(0)
    vertex_half = [Fraction(0) for _ in range(n)]
    vertex_area = [0 for _ in range(n)]
    nested_half = Fraction(0)
    nested_alpha_sum = Fraction(0)

    for u, v in combinations(range(n), 2):
        distance = v - u - 1
        expected_r_one = 1 << distance
        expected_b_one = 1
        expected_r_half = half * Fraction(3, 2) ** distance
        expected_b_half = half

        assert forward_one[v][u] == expected_r_one
        assert backward_one[v][u] == expected_b_one
        assert forward_half[v][u] == expected_r_half
        assert backward_half[v][u] == expected_b_half

        g_half = forward_half[v][u] * backward_half[v][u]
        x_alpha = Fraction(3, 2) ** distance
        assert g_half == Fraction(1, 4) * x_alpha

        total_half += g_half
        vertex_half[v] += g_half
        vertex_area[v] = max(vertex_area[v], expected_r_one * expected_b_one)
        if u == 0:
            nested_half += g_half
            nested_alpha_sum += x_alpha

    for v in range(1, n):
        assert vertex_area[v] == 1 << (v - 1)
        assert vertex_half[v] == Fraction(1, 2) * (Fraction(3, 2) ** v - 1)

    expected_total_half = Fraction(3, 2) ** n - 1 - Fraction(n, 2)
    assert total_half == expected_total_half
    assert nested_half == Fraction(1, 4) * nested_alpha_sum
    assert nested_half == Fraction(1, 2) * (Fraction(3, 2) ** (n - 1) - 1)

    f_one = 1 + n + sum(
        forward_one[v][u] * backward_one[v][u]
        for u, v in combinations(range(n), 2)
    )
    f_half = 1 + Fraction(n, 2) + total_half
    assert f_one == 1 << n
    assert f_half == Fraction(3, 2) ** n

    return {
        "n": n,
        "word_length": len(word),
        "F_one": f_one,
        "F_half": f_half,
        "offdiagonal_half": total_half,
        "nested_half": nested_half,
    }


def main() -> None:
    rows = [audit(n) for n in (8, 16, 24, 32, 48)]
    print("shared-endpoint saturation barrier: PASS")
    for row in rows:
        print(
            f"n={row['n']:2d} word_length={row['word_length']:4d} "
            f"F(1)={row['F_one']} F(1/2)={row['F_half']} "
            f"nested_half={row['nested_half']}"
        )


if __name__ == "__main__":
    main()
