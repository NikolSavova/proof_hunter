#!/usr/bin/env python3
"""Exact finite certificate for the foreign-shift triangle counterexample.

The 126-point core is an integrally transformed Welch Costas array.  It is
distance-Sidon.  Three further points form an anchor triangle.  The same
anchor triangle occurs in 3,610 different fibres of A + J(A-A), showing that
a fixed non-collinear triangle can have quadratic-scale translate codegree.
"""

from math import comb


P = 127
G = 3
SHEAR = 93
STRETCH = 94
TRANSLATION = (100, 10_000)


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def sub(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[0], x[1] - y[1]


def quarter_turn(x: tuple[int, int]) -> tuple[int, int]:
    return -x[1], x[0]


def transform(x: tuple[int, int]) -> tuple[int, int]:
    return x[0] + SHEAR * x[1], STRETCH * x[1]


def norm2(x: tuple[int, int]) -> int:
    return x[0] * x[0] + x[1] * x[1]


def differences(points: list[tuple[int, int]]) -> set[tuple[int, int]]:
    return {sub(x, y) for x in points for y in points if x != y}


def assert_distance_sidon(points: list[tuple[int, int]]) -> None:
    assert len(set(points)) == len(points)
    seen: dict[int, tuple[int, int]] = {}
    for i, x in enumerate(points):
        for j, y in enumerate(points[:i]):
            value = norm2(sub(x, y))
            assert value > 0
            assert value not in seen, (i, j, seen[value], value)
            seen[value] = (i, j)
    assert len(seen) == comb(len(points), 2)


def main() -> None:
    # 3 is a primitive root modulo 127: these are the prime divisors of 126.
    assert all(pow(G, (P - 1) // q, P) != 1 for q in (2, 3, 7))

    welch = [(i, pow(G, i, P)) for i in range(P - 1)]
    core = [transform(x) for x in welch]
    assert len(core) == 126
    assert_distance_sidon(core)
    assert len(differences(core)) == 126 * 125

    # The untransformed shifts are (5,0) and (0,4).
    u = transform((5, 0))
    v = transform((0, 4))
    assert u == (5, 0)
    assert v == (372, 376)
    assert u[0] * v[1] - u[1] * v[0] != 0

    base = TRANSLATION
    anchor_b = sub(base, quarter_turn(u))
    anchor_c = sub(base, quarter_turn(v))
    anchors = [base, anchor_b, anchor_c]
    assert anchors == [(100, 10_000), (100, 9_995), (476, 9_628)]
    assert quarter_turn(sub(anchor_b, base)) == u
    assert quarter_turn(sub(anchor_c, base)) == v

    points = core + anchors
    assert len(points) == 129
    assert_distance_sidon(points)

    core_differences = differences(core)
    witnesses = {
        x
        for x in core_differences
        if add(x, u) in core_differences and add(x, v) in core_differences
    }
    assert len(witnesses) == 3_610

    # Every witness gives a distinct output z whose fibre contains all three
    # anchors, with edge labels x, x+u, x+v respectively.
    full_differences = differences(points)
    full_witnesses = {
        x
        for x in full_differences
        if add(x, u) in full_differences and add(x, v) in full_differences
    }
    assert full_witnesses == witnesses
    fibre_outputs = set()
    for x in full_witnesses:
        z = add(base, quarter_turn(x))
        assert sub(z, base) == quarter_turn(x)
        assert sub(z, anchor_b) == quarter_turn(add(x, u))
        assert sub(z, anchor_c) == quarter_turn(add(x, v))
        assert x in full_differences
        assert add(x, u) in full_differences
        assert add(x, v) in full_differences
        fibre_outputs.add(z)
    assert len(fibre_outputs) == 3_610

    print("points", len(points))
    print("unordered distances", comb(len(points), 2))
    print("anchor triangle fibre codegree", len(fibre_outputs))
    print("codegree / points^2", len(fibre_outputs) / len(points) ** 2)


if __name__ == "__main__":
    main()
