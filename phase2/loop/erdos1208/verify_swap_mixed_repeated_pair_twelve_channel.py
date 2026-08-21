#!/usr/bin/env python3
"""Verify the twelve-channel repeated mixed-key normal form."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from random import Random

Point = tuple[int, int]
J: tuple[Point, Point] = ((0, -1), (1, 0))
L: tuple[Point, Point] = ((1, -1), (1, 1))


def add(*points: Point) -> Point:
    return sum(point[0] for point in points), sum(point[1] for point in points)


def neg(point: Point) -> Point:
    return -point[0], -point[1]


def sub(first: Point, second: Point) -> Point:
    return first[0] - second[0], first[1] - second[1]


def apply(matrix: tuple[Point, Point], point: Point) -> Point:
    return (
        matrix[0][0] * point[0] + matrix[0][1] * point[1],
        matrix[1][0] * point[0] + matrix[1][1] * point[1],
    )


def linv(point: Point) -> Point | None:
    x, y = point
    if (x + y) % 2 or (y - x) % 2:
        return None
    return (x + y) // 2, (y - x) // 2


def forms(
    e: Point,
    z: Point,
    c: Point,
    *,
    b: Point,
    k0: Point,
    alpha: Point,
    delta: Point,
    chi: Point,
    gamma: Point,
    phi: Point,
    big_c: Point,
) -> tuple[Point, ...] | None:
    t = linv(sub(b, e))
    if t is None:
        return None
    return (
        e,
        z,
        sub(k0, t),
        sub(z, t),
        add(apply(J, z), alpha),
        add(e, z, delta),
        c,
        add(c, apply(J, z), chi),
        add(c, t),
        add(e, neg(c), gamma),
        add(e, z, neg(c), phi),
        add(e, apply(L, big_c), neg(apply(L, c))),
    )


def recover(
    row: int,
    selected: tuple[Point, Point, Point],
    *,
    b: Point,
    k0: Point,
    alpha: Point,
    chi: Point,
    gamma: Point,
    phi: Point,
    big_c: Point,
) -> tuple[Point, Point, Point] | None:
    first, second, third = selected
    if row == 0:
        return first, second, third
    if row == 1:
        t = sub(k0, first)
        return sub(b, apply(L, t)), second, third
    if row == 2:
        e = first
        z = apply(J, neg(sub(second, alpha)))
        c = sub(third, add(apply(J, z), chi))
        return e, z, c
    if row == 3:
        e, z = first, second
        c = sub(add(e, gamma), third)
        return e, z, c
    if row == 4:
        e, z = first, second
        lc = sub(add(e, apply(L, big_c)), third)
        c = linv(lc)
        return None if c is None else (e, z, c)
    if row == 5:
        c = first
        z = apply(J, neg(sub(second, add(c, chi))))
        t = sub(third, c)
        return sub(b, apply(L, t)), z, c
    if row == 6:
        u = sub(first, gamma)
        z = sub(second, add(u, phi))
        c = third
        return add(u, c), z, c
    if row == 7:
        u = sub(first, gamma)
        z = sub(second, add(u, phi))
        jc = sub(add(u, apply(L, big_c)), third)
        c = apply(J, neg(jc))
        return add(u, c), z, c
    raise AssertionError(row)


ROWS = (
    (0, 1, 6),
    (2, 1, 6),
    (0, 4, 7),
    (0, 1, 9),
    (0, 1, 11),
    (6, 7, 8),
    (9, 10, 6),
    (9, 10, 11),
)


def expected_differences(h: Point, s: Point, a: Point) -> tuple[Point, ...]:
    lam = linv(h)
    assert lam is not None
    return (
        h,
        s,
        lam,
        add(s, lam),
        apply(J, s),
        add(h, s),
        a,
        add(a, apply(J, s)),
        sub(a, lam),
        sub(h, a),
        sub(add(h, s), a),
        sub(h, apply(L, a)),
    )


def random_identities() -> None:
    rng = Random(1208)
    for _ in range(50_000):
        def point() -> Point:
            return rng.randrange(-20, 21), rng.randrange(-20, 21)

        b, k0, alpha, delta, chi, gamma, phi, big_c = (point() for _ in range(8))
        t1, t2, z1, z2, c1, c2 = (point() for _ in range(6))
        e1 = sub(b, apply(L, t1))
        e2 = sub(b, apply(L, t2))
        f1 = forms(
            e1, z1, c1, b=b, k0=k0, alpha=alpha, delta=delta,
            chi=chi, gamma=gamma, phi=phi, big_c=big_c,
        )
        f2 = forms(
            e2, z2, c2, b=b, k0=k0, alpha=alpha, delta=delta,
            chi=chi, gamma=gamma, phi=phi, big_c=big_c,
        )
        assert f1 is not None and f2 is not None
        h, s, a = sub(e1, e2), sub(z1, z2), sub(c1, c2)
        assert tuple(sub(first, second) for first, second in zip(f1, f2)) == (
            expected_differences(h, s, a)
        )
        for row_index, indices in enumerate(ROWS):
            selected = tuple(f1[index] for index in indices)
            assert recover(
                row_index,
                selected,  # type: ignore[arg-type]
                b=b, k0=k0, alpha=alpha, chi=chi, gamma=gamma,
                phi=phi, big_c=big_c,
            ) == (e1, z1, c1)


def overlap(d_set: set[Point], shift: Point) -> int:
    return sum(add(point, shift) in d_set for point in d_set)


def finite_cells() -> None:
    rng = Random(1210)
    box = [(x, y) for x in range(-2, 3) for y in range(-2, 3)]
    for trial in range(120):
        d_set = {
            point for point in box
            if trial < 20 or rng.randrange(4) != 0
        }
        b = rng.choice(box)
        constants = [rng.choice(box) for _ in range(7)]
        k0, alpha, delta, chi, gamma, phi, big_c = constants
        groups = []
        for t, z, c in product(box, repeat=3):
            e = sub(b, apply(L, t))
            row = forms(
                e, z, c, b=b, k0=k0, alpha=alpha, delta=delta,
                chi=chi, gamma=gamma, phi=phi, big_c=big_c,
            )
            if row is not None and all(value in d_set for value in row):
                groups.append((e, z, c, row))
        difference_load = Counter()
        for first, second in combinations(groups, 2):
            h = sub(first[0], second[0])
            s = sub(first[1], second[1])
            a = sub(first[2], second[2])
            difference_load[h, s, a] += 1
        for (h, s, a), load in difference_load.items():
            shifts = expected_differences(h, s, a)
            products = [
                overlap(d_set, shifts[i])
                * overlap(d_set, shifts[j])
                * overlap(d_set, shifts[k])
                for i, j, k in ROWS
            ]
            assert load <= min(products)


def main() -> None:
    random_identities()
    finite_cells()
    print("SWAP MIXED REPEATED-PAIR TWELVE-CHANNEL GATE: PASS")


if __name__ == "__main__":
    main()
