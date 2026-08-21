#!/usr/bin/env python3
"""Checks for the three-channel projected-key codegree bounds."""

from __future__ import annotations

from collections import Counter
from itertools import product
import random

from analyze_affine_costas_energy import welch
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    overlap_table,
    rotate,
    subtract,
)


Point = tuple[int, int]


def negate(value: Point) -> Point:
    return -value[0], -value[1]


def inverse_linear(value: Point) -> Point:
    assert (value[0] + value[1]) % 2 == 0
    assert (value[1] - value[0]) % 2 == 0
    return (
        (value[0] + value[1]) // 2,
        (value[1] - value[0]) // 2,
    )


def optional_inverse_linear(value: Point) -> Point | None:
    if (value[0] + value[1]) % 2 or (value[1] - value[0]) % 2:
        return None
    return (
        (value[0] + value[1]) // 2,
        (value[1] - value[0]) // 2,
    )


def verify_random_recovery() -> None:
    rng = random.Random(120812087)
    for _ in range(50000):
        s = rng.randrange(-15, 16), rng.randrange(-15, 16)
        d = rng.randrange(-15, 16), rng.randrange(-15, 16)
        r = rng.randrange(-15, 16), rng.randrange(-15, 16)
        b_value = rng.randrange(-15, 16), rng.randrange(-15, 16)
        q = rng.randrange(-15, 16), rng.randrange(-15, 16)
        t = rng.randrange(-15, 16), rng.randrange(-15, 16)
        c = rng.randrange(-15, 16), rng.randrange(-15, 16)

        # Moving-W pair in one group.
        x_value = subtract(c, q)
        y_value = add(b_value, rotate(q))
        v_value = add(c, t)
        e_value = subtract(b_value, linear(t))
        f_value = subtract(y_value, t)
        g_value = subtract(add(b_value, rotate(r)), t)
        w_shift = add(rotate(s), linear(d))
        j_shift = rotate(add(s, d))
        first = (
            subtract(x_value, s),
            add(y_value, w_shift),
            add(v_value, d),
            e_value,
            add(f_value, j_shift),
            add(g_value, j_shift),
        )
        b_first = add(b_value, linear(d))
        q_first = add(q, s)
        t_first = add(t, d)
        assert first == (
            subtract(c, q_first),
            add(b_first, rotate(q_first)),
            add(c, t_first),
            subtract(b_first, linear(t_first)),
            subtract(add(b_first, rotate(q_first)), t_first),
            subtract(add(b_first, rotate(add(r, s))), t_first),
        )

        recovered_q = negate(rotate(subtract(y_value, b_value)))
        recovered_c = add(x_value, recovered_q)
        recovered_t = subtract(v_value, recovered_c)
        assert (recovered_q, recovered_c, recovered_t) == (q, c, t)

        recovered_q = inverse_linear(
            add(subtract(subtract(f_value, b_value), x_value), v_value)
        )
        assert recovered_q == q
        assert add(x_value, recovered_q) == c
        assert subtract(v_value, c) == t

        assert subtract(y_value, f_value) == t
        assert subtract(v_value, t) == c
        assert negate(rotate(subtract(y_value, b_value))) == q

        # Moving-V pair in one group.
        p = rng.randrange(-15, 16), rng.randrange(-15, 16)
        c = rng.randrange(-15, 16), rng.randrange(-15, 16)
        b_value = rng.randrange(-15, 16), rng.randrange(-15, 16)
        x_value = subtract(c, p)
        y_value = add(b_value, rotate(p))
        c0_value = subtract(c, t)
        w_value = add(b_value, linear(t))
        f_value = add(y_value, t)
        g_value = add(add(b_value, rotate(r)), t)
        first = (
            add(x_value, subtract(d, s)),
            add(y_value, rotate(s)),
            c0_value,
            add(w_value, linear(d)),
            add(f_value, add(rotate(s), d)),
            add(g_value, add(rotate(s), d)),
        )
        p_first = add(p, s)
        t_first = add(t, d)
        c_first = add(c, d)
        assert first == (
            subtract(c_first, p_first),
            add(b_value, rotate(p_first)),
            subtract(c_first, t_first),
            add(b_value, linear(t_first)),
            add(add(b_value, rotate(p_first)), t_first),
            add(add(b_value, rotate(add(r, s))), t_first),
        )

        recovered_p = subtract(c, x_value)
        recovered_b = subtract(y_value, rotate(recovered_p))
        recovered_t = inverse_linear(subtract(w_value, recovered_b))
        assert (recovered_p, recovered_b, recovered_t) == (p, b_value, t)

        recovered_p = subtract(c, x_value)
        recovered_t = rotate(
            subtract(subtract(f_value, w_value), rotate(recovered_p))
        )
        assert recovered_t == t
        assert subtract(w_value, linear(recovered_t)) == b_value

        assert subtract(f_value, y_value) == t
        recovered_b = subtract(w_value, linear(t))
        assert negate(rotate(subtract(y_value, recovered_b))) == p


def verify_product_channels() -> None:
    rng = random.Random(271828189)
    differences = difference_set(welch(7))
    overlaps = overlap_table(differences)
    shifts = [shift for shift, starts in overlaps.items() if starts]

    def starts(shift: Point) -> list[Point]:
        return overlaps.get(shift, [])

    for _ in range(80):
        s = rng.choice(shifts)
        d = rng.choice([value for value in shifts if value != (0, 0)])
        b_value = rng.choice(tuple(differences))
        r = rng.choice(tuple(differences))
        w_shift = add(rotate(s), linear(d))
        j_shift = rotate(add(s, d))
        groups: set[tuple[Point, Point, Point]] = set()
        projection_xfv = set()
        projection_yfv = set()
        for x_value, y_value, v_value in product(
            starts(negate(s)), starts(w_shift), starts(d)
        ):
            q = negate(rotate(subtract(y_value, b_value)))
            c = add(x_value, q)
            t = subtract(v_value, c)
            e_value = subtract(b_value, linear(t))
            f_value = subtract(y_value, t)
            g_value = subtract(add(b_value, rotate(r)), t)
            if not {
                e_value,
                f_value,
                add(f_value, j_shift),
                g_value,
                add(g_value, j_shift),
            } <= differences:
                continue
            group = c, subtract(b_value, linear(t)), subtract(q, r)
            groups.add(group)
            projection_xfv.add((x_value, f_value, v_value))
            projection_yfv.add((y_value, f_value, v_value))
        count = len(groups)
        assert len(projection_xfv) == count
        assert len(projection_yfv) == count
        bounds = (
            len(starts(negate(s))) * len(starts(w_shift)) * len(starts(d)),
            len(starts(negate(s))) * len(starts(j_shift)) * len(starts(d)),
            len(starts(w_shift)) * len(starts(j_shift)) * len(starts(d)),
        )
        assert count <= min(bounds)

        # Dual V channel.
        c = rng.choice(tuple(differences))
        a_shift = subtract(d, s)
        b_shift = rotate(s)
        e_shift = add(rotate(s), d)
        groups = set()
        projection_xfw = set()
        projection_yfw = set()
        for x_value, y_value, w_value in product(
            starts(a_shift), starts(b_shift), starts(linear(d))
        ):
            p = subtract(c, x_value)
            b_value = subtract(y_value, rotate(p))
            t = optional_inverse_linear(subtract(w_value, b_value))
            if t is None:
                continue
            c0_value = subtract(c, t)
            f_value = add(y_value, t)
            g_value = add(add(b_value, rotate(r)), t)
            if not {
                c0_value,
                f_value,
                add(f_value, e_shift),
                g_value,
                add(g_value, e_shift),
            } <= differences:
                continue
            group = subtract(c, t), b_value, subtract(p, r)
            groups.add(group)
            projection_xfw.add((x_value, f_value, w_value))
            projection_yfw.add((y_value, f_value, w_value))
        count = len(groups)
        assert len(projection_xfw) == count
        assert len(projection_yfw) == count
        bounds = (
            len(starts(a_shift)) * len(starts(b_shift)) * len(starts(linear(d))),
            len(starts(a_shift)) * len(starts(e_shift)) * len(starts(linear(d))),
            len(starts(b_shift)) * len(starts(e_shift)) * len(starts(linear(d))),
        )
        assert count <= min(bounds)


def verify_physical_endpoint_factor() -> None:
    for prime in (7, 11, 17):
        points = welch(prime)
        k = len(points)
        head_counts: Counter[Point] = Counter()
        tail_counts: Counter[Point] = Counter()
        for endpoint in points:
            others = [point for point in points if point != endpoint]
            for first in others:
                for second in others:
                    if first == second:
                        continue
                    head_first = subtract(endpoint, first)
                    head_second = subtract(endpoint, second)
                    head_counts[subtract(head_first, head_second)] += 1
                    tail_first = subtract(first, endpoint)
                    tail_second = subtract(second, endpoint)
                    tail_counts[subtract(tail_first, tail_second)] += 1
        assert max(head_counts.values(), default=0) <= k
        assert max(tail_counts.values(), default=0) <= k


def main() -> None:
    verify_random_recovery()
    verify_product_channels()
    verify_physical_endpoint_factor()
    print("SWAP PROJECTED-KEY PAIR CODEGREE MIN GATE: PASS")


if __name__ == "__main__":
    main()
