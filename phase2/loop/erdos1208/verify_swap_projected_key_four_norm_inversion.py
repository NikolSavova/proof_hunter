#!/usr/bin/env python3
"""Exact checks for four-norm inversion over projected completion keys."""

from __future__ import annotations

from itertools import product
import random

from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def negate(value: Point) -> Point:
    return -value[0], -value[1]


def norm(value: Point) -> int:
    return value[0] * value[0] + value[1] * value[1]


def signs(value: Point) -> tuple[Point, ...]:
    return tuple(sorted({value, negate(value)}))


def verify_moving_w() -> None:
    rng = random.Random(120812085)
    for _ in range(50000):
        r = rng.randrange(-20, 21), rng.randrange(-20, 21)
        a_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        b_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        q = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t = rng.randrange(-20, 21), rng.randrange(-20, 21)
        c = add(a_value, r)
        x_value = subtract(c, q)
        y_value = add(b_value, rotate(q))
        v_value = add(c, t)
        e_value = subtract(b_value, linear(t))
        f_value = subtract(y_value, t)
        g_value = subtract(add(b_value, rotate(r)), t)

        left = subtract(
            subtract(add(e_value, linear(v_value)), linear(x_value)),
            subtract(y_value, rotate(y_value)),
        )
        assert left == rotate(b_value)

        recovered = []
        for candidate_x, candidate_y, candidate_v, candidate_e in product(
            signs(x_value), signs(y_value), signs(v_value), signs(e_value)
        ):
            candidate_q = negate(rotate(subtract(candidate_y, b_value)))
            candidate_c = add(candidate_x, candidate_q)
            candidate_t = subtract(candidate_v, candidate_c)
            if candidate_e != subtract(b_value, linear(candidate_t)):
                continue
            recovered.append(
                (
                    candidate_q,
                    candidate_t,
                    subtract(candidate_c, r),
                    subtract(candidate_q, r),
                )
            )
        assert (q, t, a_value, subtract(q, r)) in recovered
        assert len(recovered) <= 16

        # The remaining two variable vectors are recovered as well.
        assert f_value == subtract(add(b_value, rotate(q)), t)
        assert g_value == subtract(add(b_value, rotate(r)), t)


def verify_moving_v() -> None:
    rng = random.Random(314159269)
    for _ in range(50000):
        r = rng.randrange(-20, 21), rng.randrange(-20, 21)
        a_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        b_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        p = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t = rng.randrange(-20, 21), rng.randrange(-20, 21)
        c = add(a_value, r)
        x_value = subtract(c, p)
        y_value = add(b_value, rotate(p))
        c0_value = subtract(c, t)
        w_value = add(b_value, linear(t))
        f_value = add(y_value, t)
        g_value = add(add(b_value, rotate(r)), t)

        left = add(
            subtract(subtract(w_value, y_value), rotate(x_value)),
            linear(c0_value),
        )
        assert left == c

        recovered = []
        for candidate_x, candidate_y, candidate_c0, candidate_w in product(
            signs(x_value), signs(y_value), signs(c0_value), signs(w_value)
        ):
            candidate_p = subtract(c, candidate_x)
            candidate_t = subtract(c, candidate_c0)
            candidate_b = subtract(candidate_y, rotate(candidate_p))
            if candidate_w != add(candidate_b, linear(candidate_t)):
                continue
            recovered.append(
                (
                    candidate_p,
                    candidate_t,
                    candidate_b,
                    subtract(candidate_p, r),
                )
            )
        assert (p, t, b_value, subtract(p, r)) in recovered
        assert len(recovered) <= 16
        assert f_value == add(add(b_value, rotate(p)), t)
        assert g_value == add(add(b_value, rotate(r)), t)


def verify_pair_directions() -> None:
    rng = random.Random(161803399)
    for _ in range(50000):
        b_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        c1 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        c2 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        r = rng.randrange(-20, 21), rng.randrange(-20, 21)
        q1 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        q2 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t1 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t2 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        first = (
            subtract(c1, q1),
            add(b_value, rotate(q1)),
            add(c1, t1),
            subtract(b_value, linear(t1)),
            subtract(add(b_value, rotate(q1)), t1),
            subtract(add(b_value, rotate(r)), t1),
        )
        second = (
            subtract(c2, q2),
            add(b_value, rotate(q2)),
            add(c2, t2),
            subtract(b_value, linear(t2)),
            subtract(add(b_value, rotate(q2)), t2),
            subtract(add(b_value, rotate(r)), t2),
        )
        h = subtract(c1, c2)
        s = subtract(q1, q2)
        d = subtract(t1, t2)
        expected = (
            subtract(h, s),
            rotate(s),
            add(h, d),
            negate(linear(d)),
            subtract(rotate(s), d),
            negate(d),
        )
        assert tuple(subtract(a, b) for a, b in zip(first, second)) == expected

        # Dual moving-V pair: c is fixed, while B moves along the
        # complementary perpendicular fibre.
        c = rng.randrange(-20, 21), rng.randrange(-20, 21)
        b1 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        b2 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        p1 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        p2 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        first = (
            subtract(c, p1),
            add(b1, rotate(p1)),
            subtract(c, t1),
            add(b1, linear(t1)),
            add(add(b1, rotate(p1)), t1),
            add(add(b1, rotate(r)), t1),
        )
        second = (
            subtract(c, p2),
            add(b2, rotate(p2)),
            subtract(c, t2),
            add(b2, linear(t2)),
            add(add(b2, rotate(p2)), t2),
            add(add(b2, rotate(r)), t2),
        )
        h = subtract(b1, b2)
        s = subtract(p1, p2)
        expected = (
            negate(s),
            add(h, rotate(s)),
            negate(d),
            add(h, linear(d)),
            add(add(h, rotate(s)), d),
            add(h, d),
        )
        assert tuple(subtract(a, b) for a, b in zip(first, second)) == expected


def main() -> None:
    verify_moving_w()
    verify_moving_v()
    verify_pair_directions()
    print("SWAP PROJECTED-KEY FOUR-NORM INVERSION GATE: PASS")


if __name__ == "__main__":
    main()
