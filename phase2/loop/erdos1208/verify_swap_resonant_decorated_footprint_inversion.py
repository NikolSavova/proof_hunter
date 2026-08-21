#!/usr/bin/env python3
"""Exact checks for decorated inversion of all three resonant footprints."""

from __future__ import annotations

from collections import defaultdict
from itertools import product
import random

from analyze_affine_costas_energy import welch
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]
Corner = tuple[Point, Point, Point]


def negate(value: Point) -> Point:
    return -value[0], -value[1]


def inverse_q(z: Point, d: Point, corner: Corner) -> tuple[Point, Point, Point, Point]:
    p1, x_value, ell = corner
    twice_y1 = (
        2 * (ell[0] + rotate(p1)[0]),
        2 * (ell[1] + rotate(p1)[1]),
    )
    t1 = add(subtract(z, twice_y1), linear(d))
    t2 = subtract(t1, d)
    q = subtract(p1, t1)
    c = add(x_value, q)
    return c, ell, t1, t2


def inverse_p(z: Point, d: Point, corner: Corner) -> tuple[Point, Point, Point, Point]:
    p, x1, ell = corner
    t2 = subtract(subtract(subtract(z, x1), ell), rotate(p))
    t1 = add(t2, d)
    q1 = subtract(p, t1)
    c = add(x1, q1)
    return c, ell, t1, t2


def inverse_z(z: Point, d: Point, corner: Corner) -> tuple[Point, Point, Point, Point]:
    q1, x1, w1 = corner
    fixed_z = add(w1, rotate(q1))
    t2 = add(subtract(fixed_z, z), x1)
    t1 = add(t2, d)
    c = add(x1, q1)
    ell = subtract(w1, linear(t1))
    return c, ell, t1, t2


def forward(c: Point, ell: Point, q: Point, t: Point) -> tuple[Point, Point, Point, Point, Point]:
    x_value = subtract(c, q)
    p = add(q, t)
    y = add(ell, rotate(p))
    w = add(ell, linear(t))
    z_value = add(w, rotate(q))
    assert z_value == add(y, t)
    return x_value, p, y, w, z_value


def verify_random_roundtrips() -> None:
    rng = random.Random(12081208)
    for _ in range(20000):
        c = rng.randrange(-20, 21), rng.randrange(-20, 21)
        ell = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t1 = rng.randrange(-12, 13), rng.randrange(-12, 13)
        t2 = rng.randrange(-12, 13), rng.randrange(-12, 13)
        d = subtract(t1, t2)

        # Fixed q.
        q = rng.randrange(-12, 13), rng.randrange(-12, 13)
        x1, p1, y1, _, _ = forward(c, ell, q, t1)
        _, _, _, _, z2 = forward(c, ell, q, t2)
        footprint = add(y1, z2)
        corner = p1, x1, ell
        assert inverse_q(footprint, d, corner) == (c, ell, t1, t2)
        companion = subtract(p1, d), x1, ell
        _, p2, _, _, _ = forward(c, ell, q, t2)
        assert companion == (p2, x1, ell)

        # Fixed p.
        p = rng.randrange(-12, 13), rng.randrange(-12, 13)
        q1 = subtract(p, t1)
        q2 = subtract(p, t2)
        x1, p_check, _, _, _ = forward(c, ell, q1, t1)
        _, _, _, _, z2 = forward(c, ell, q2, t2)
        assert p_check == p
        footprint = add(x1, z2)
        corner = p, x1, ell
        assert inverse_p(footprint, d, corner) == (c, ell, t1, t2)
        x2, _, _, _, _ = forward(c, ell, q2, t2)
        assert (p, subtract(x1, d), ell) == (p, x2, ell)

        # Fixed Z.  Solving X=-J(H-Z)+(I-J)t makes q vary with t.
        fixed_z = rng.randrange(-20, 21), rng.randrange(-20, 21)
        h_value = add(ell, rotate(c))
        # -J(H-Z) = J(Z-H).
        base = rotate(subtract(fixed_z, h_value))
        x1 = add(base, subtract(t1, rotate(t1)))
        x2 = add(base, subtract(t2, rotate(t2)))
        q1 = subtract(c, x1)
        q2 = subtract(c, x2)
        fx1, _, _, w1, check_z1 = forward(c, ell, q1, t1)
        fx2, _, y2, w2, check_z2 = forward(c, ell, q2, t2)
        assert fx1 == x1 and fx2 == x2
        assert check_z1 == fixed_z == check_z2
        footprint = add(x1, y2)
        corner = q1, x1, w1
        assert inverse_z(footprint, d, corner) == (c, ell, t1, t2)
        i_minus_j_d = subtract(d, rotate(d))
        companion = (
            add(q1, i_minus_j_d),
            subtract(x1, i_minus_j_d),
            subtract(w1, linear(d)),
        )
        assert companion == (q2, x2, w2)


def verify_exhaustive_key_injectivity() -> None:
    values = list(product(range(-1, 2), repeat=2))
    for branch in ("q", "p", "z"):
        seen: dict[tuple[Point, Point, Corner], tuple[Point, ...]] = {}
        for c, ell, fixed, t1, t2 in product(values, repeat=5):
            d = subtract(t1, t2)
            if branch == "q":
                q = fixed
                x1, p1, y1, _, _ = forward(c, ell, q, t1)
                _, _, _, _, z2 = forward(c, ell, q, t2)
                footprint = add(y1, z2)
                corner = p1, x1, ell
                recovered = inverse_q(footprint, d, corner)
            elif branch == "p":
                p = fixed
                q1, q2 = subtract(p, t1), subtract(p, t2)
                x1, _, _, _, _ = forward(c, ell, q1, t1)
                _, _, _, _, z2 = forward(c, ell, q2, t2)
                footprint = add(x1, z2)
                corner = p, x1, ell
                recovered = inverse_p(footprint, d, corner)
            else:
                fixed_z = fixed
                h_value = add(ell, rotate(c))
                base = rotate(subtract(fixed_z, h_value))
                x1 = add(base, subtract(t1, rotate(t1)))
                x2 = add(base, subtract(t2, rotate(t2)))
                q1, q2 = subtract(c, x1), subtract(c, x2)
                _, _, _, w1, check1 = forward(c, ell, q1, t1)
                _, _, y2, _, check2 = forward(c, ell, q2, t2)
                assert check1 == fixed_z == check2
                footprint = add(x1, y2)
                corner = q1, x1, w1
                recovered = inverse_z(footprint, d, corner)
            assert recovered == (c, ell, t1, t2)
            key = footprint, d, corner
            identity = c, ell, t1, t2
            previous = seen.setdefault(key, identity)
            assert previous == identity


def verify_off_diagonal_support() -> None:
    points = [(3 * x + y, x + 4 * y) for x, y in welch(17)]
    rng = random.Random(27182818)
    for size in range(4, 13):
        for _ in range(100):
            values = rng.sample(points, size)
            rows = (
                lambda first, second: add(rotate(first), linear(second)),
                lambda first, second: add(first, second),
                lambda first, second: add(
                    subtract(first, rotate(first)), negate(second)
                ),
            )
            for footprint_map in rows:
                full = {
                    footprint_map(first, second)
                    for first in values
                    for second in values
                }
                off_diagonal = {
                    footprint_map(first, second)
                    for first in values
                    for second in values
                    if first != second
                }
                assert len(off_diagonal) >= len(full) - size
                assert 4 * len(off_diagonal) >= size * size


def verify_off_diagonal_aggregate() -> None:
    points = [(3 * x + y, x + 4 * y) for x, y in welch(17)]
    rng = random.Random(31415926)
    for branch in range(3):
        for _ in range(1000):
            lower = rng.randrange(4, 8)
            band = rng.randrange(1, 20)
            supports: list[set[Point]] = []
            sizes: list[int] = []
            weights: list[int] = []
            for _ in range(rng.randrange(1, 15)):
                size = rng.randrange(lower, min(2 * lower, len(points) + 1))
                values = rng.sample(points, size)
                translation = (
                    rng.randrange(-30, 31),
                    rng.randrange(-30, 31),
                )
                if branch == 0:
                    footprint_map = lambda first, second: add(
                        rotate(first), linear(second)
                    )
                elif branch == 1:
                    footprint_map = add
                else:
                    footprint_map = lambda first, second: add(
                        subtract(first, rotate(first)), negate(second)
                    )
                support = {
                    add(translation, footprint_map(first, second))
                    for first in values
                    for second in values
                    if first != second
                }
                supports.append(support)
                sizes.append(size)
                weights.append(rng.randrange(1, 2 * band))
            depth: dict[Point, int] = defaultdict(int)
            for support in supports:
                for value in support:
                    depth[value] += 1
            maximum_depth = max(depth.values())
            ambient_support = len(depth)
            assert sum(size * size for size in sizes) <= (
                4 * maximum_depth * ambient_support
            )
            contribution = sum(
                weight * size for weight, size in zip(weights, sizes)
            )
            assert contribution <= (
                8 * band * maximum_depth * ambient_support // lower
            )


def prune_bipartite(
    edges: set[tuple[int, int]], left_minimum: int, right_minimum: int
) -> tuple[set[tuple[int, int]], int]:
    remaining = set(edges)
    removed = 0
    while True:
        left_degree: dict[int, int] = defaultdict(int)
        right_degree: dict[int, int] = defaultdict(int)
        for left, right in remaining:
            left_degree[left] += 1
            right_degree[right] += 1
        doomed_left = {
            vertex for vertex, degree in left_degree.items() if degree < left_minimum
        }
        doomed_right = {
            vertex for vertex, degree in right_degree.items() if degree < right_minimum
        }
        if not doomed_left and not doomed_right:
            break
        old_size = len(remaining)
        remaining = {
            edge
            for edge in remaining
            if edge[0] not in doomed_left and edge[1] not in doomed_right
        }
        removed += old_size - len(remaining)
    return remaining, removed


def verify_pruning_dichotomy() -> None:
    rng = random.Random(161803398)
    for _ in range(10000):
        left_size = rng.randrange(1, 20)
        right_size = rng.randrange(1, 20)
        edges = {
            (left, right)
            for left in range(left_size)
            for right in range(right_size)
            if rng.randrange(4) == 0
        }
        left_minimum = rng.randrange(1, 6)
        right_minimum = rng.randrange(1, 6)
        core, removed = prune_bipartite(edges, left_minimum, right_minimum)
        assert removed <= left_minimum * left_size + right_minimum * right_size
        if core:
            left_degree: dict[int, int] = defaultdict(int)
            right_degree: dict[int, int] = defaultdict(int)
            for left, right in core:
                left_degree[left] += 1
                right_degree[right] += 1
            assert min(left_degree.values()) >= left_minimum
            assert min(right_degree.values()) >= right_minimum


def verify_genuine_costas_23_constant_z() -> None:
    c = 14, -11
    ell = 50, 33
    rows = (
        ((-9, -11), (-69, 23), (27, -13), (-42, 10)),
        ((37, -57), (-23, 23), (-19, -13), (-42, 10)),
    )
    x1, t1, _, fixed_z = rows[0]
    x2, t2, y2, check_z = rows[1]
    assert fixed_z == check_z
    d = subtract(t1, t2)
    q1 = subtract(c, x1)
    q2 = subtract(c, x2)
    w1 = subtract(fixed_z, rotate(q1))
    w2 = subtract(fixed_z, rotate(q2))
    footprint = add(x1, y2)
    corner = q1, x1, w1
    assert inverse_z(footprint, d, corner) == (c, ell, t1, t2)
    i_minus_j_d = subtract(d, rotate(d))
    assert (
        add(q1, i_minus_j_d),
        subtract(x1, i_minus_j_d),
        subtract(w1, linear(d)),
    ) == (q2, x2, w2)


def main() -> None:
    verify_random_roundtrips()
    verify_exhaustive_key_injectivity()
    verify_off_diagonal_support()
    verify_off_diagonal_aggregate()
    verify_pruning_dichotomy()
    verify_genuine_costas_23_constant_z()
    print("SWAP RESONANT DECORATED-FOOTPRINT INVERSION GATE: PASS")


if __name__ == "__main__":
    main()
