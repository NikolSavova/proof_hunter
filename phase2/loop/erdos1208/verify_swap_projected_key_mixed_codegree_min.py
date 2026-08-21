#!/usr/bin/env python3
"""Checks the mixed W--V projected-key codegree normal form."""

from __future__ import annotations

from collections import Counter
from itertools import product
import random

from analyze_affine_costas_energy import welch
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    rotate,
    subtract,
)


Point = tuple[int, int]


def negate(value: Point) -> Point:
    return -value[0], -value[1]


def inverse_linear(value: Point) -> Point | None:
    if (value[0] + value[1]) % 2 or (value[1] - value[0]) % 2:
        return None
    return (
        (value[0] + value[1]) // 2,
        (value[1] - value[0]) // 2,
    )


def scale(sign: int, value: Point) -> Point:
    return sign * value[0], sign * value[1]


def norm_form(
    r_w: Point,
    b_value: Point,
    r_v: Point,
    a_value: Point,
) -> tuple[Point, Point, Point, Point, Point, Point, Point]:
    c_value = add(a_value, r_v)
    k_value = add(b_value, rotate(r_w))
    alpha = subtract(a_value, rotate(k_value))
    delta = subtract(rotate(r_v), k_value)
    chi = subtract(negate(r_w), rotate(k_value))
    gamma = add(rotate(r_v), c_value)
    phi = add(delta, c_value)
    return c_value, k_value, alpha, delta, chi, gamma, phi


def verify_random_identities() -> None:
    rng = random.Random(120812089)
    for _ in range(50000):
        c0 = rng.randrange(-20, 21), rng.randrange(-20, 21)
        ell = rng.randrange(-20, 21), rng.randrange(-20, 21)
        u_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        q_w = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t_w = rng.randrange(-20, 21), rng.randrange(-20, 21)
        p_v = rng.randrange(-20, 21), rng.randrange(-20, 21)
        t_v = rng.randrange(-20, 21), rng.randrange(-20, 21)

        r_w = subtract(q_w, u_value)
        b_value = add(ell, linear(t_w))
        r_v = subtract(p_v, u_value)
        c_value = add(c0, t_v)
        a_value = subtract(c_value, r_v)
        z_value = add(b_value, rotate(q_w))

        (
            recovered_c,
            k_value,
            alpha,
            delta,
            chi,
            gamma,
            phi,
        ) = norm_form(r_w, b_value, r_v, a_value)
        assert recovered_c == c_value
        assert z_value == add(k_value, rotate(u_value))
        assert u_value == negate(rotate(subtract(z_value, k_value)))

        # W occurrence.
        x_w = subtract(c0, q_w)
        y_w = z_value
        v_w = add(c0, t_w)
        e_w = ell
        f_w = subtract(z_value, t_w)
        g_w = subtract(k_value, t_w)

        # V occurrence.
        x_v = subtract(c_value, p_v)
        y_v = add(ell, rotate(p_v))
        c_v = c0
        w_v = add(ell, linear(t_v))
        f_v = add(y_v, t_v)
        g_v = add(add(ell, rotate(r_v)), t_v)

        assert inverse_linear(subtract(b_value, ell)) == t_w
        assert g_w == subtract(k_value, t_w)
        assert f_w == subtract(z_value, t_w)
        assert x_v == add(rotate(z_value), alpha)
        assert y_v == add(add(ell, z_value), delta)
        assert x_w == add(add(c0, rotate(z_value)), chi)
        assert v_w == add(c0, t_w)
        assert g_v == add(subtract(ell, c0), gamma)
        assert f_v == add(subtract(add(ell, z_value), c0), phi)
        assert w_v == add(subtract(ell, linear(c0)), linear(c_value))
        assert (e_w, y_w, c_v) == (ell, z_value, c0)

        # The three base coordinates recover the common group and both keys.
        recovered_u = negate(rotate(subtract(z_value, k_value)))
        recovered_tw = inverse_linear(subtract(b_value, ell))
        assert recovered_tw == t_w
        recovered_tv = subtract(c_value, c0)
        assert recovered_tv == t_v
        assert add(r_w, recovered_u) == q_w
        assert add(r_v, recovered_u) == p_v


def overlap_table(differences: set[Point]) -> Counter[Point]:
    return Counter(
        subtract(second, first)
        for first in differences
        for second in differences
    )


def affine_l_load(differences: set[Point], omega: Point) -> int:
    return sum(
        subtract(omega, linear(c_value)) in differences
        for c_value in differences
    )


def verify_mixed_min_bound() -> None:
    # The reduction is purely algebraic, so a symmetric box provides many
    # nonempty cells and checks substantially more than a sparse example.
    differences = {
        (first, second)
        for first in range(-3, 4)
        for second in range(-3, 4)
    }
    overlaps = overlap_table(differences)
    rng = random.Random(314159269)
    nonempty = 0

    for _ in range(240):
        r_w = rng.choice(tuple(differences))
        b_value = rng.choice(tuple(differences))
        r_v = rng.choice(tuple(differences))
        a_value = rng.choice(tuple(differences))
        (
            c_value,
            k_value,
            alpha,
            delta,
            chi,
            gamma,
            phi,
        ) = norm_form(r_w, b_value, r_v, a_value)

        actual = 0
        upper = 0
        for ell, z_value in product(differences, repeat=2):
            t_w = inverse_linear(subtract(b_value, ell))
            if t_w is None:
                continue
            if not {
                subtract(k_value, t_w),
                subtract(z_value, t_w),
                add(rotate(z_value), alpha),
                add(add(ell, z_value), delta),
            } <= differences:
                continue

            channel_loads = (
                overlaps[add(rotate(z_value), chi)],
                overlaps[t_w],
                overlaps[add(ell, gamma)],
                overlaps[add(add(ell, z_value), phi)],
                affine_l_load(
                    differences,
                    add(ell, linear(c_value)),
                ),
            )
            upper += min(channel_loads)

            for c0 in differences:
                vectors = {
                    add(add(c0, rotate(z_value)), chi),
                    add(c0, t_w),
                    subtract(add(ell, gamma), c0),
                    subtract(add(add(ell, z_value), phi), c0),
                    subtract(add(ell, linear(c_value)), linear(c0)),
                }
                if vectors <= differences:
                    actual += 1
                    u_value = negate(rotate(subtract(z_value, k_value)))
                    assert add(r_w, u_value) == add(
                        r_w,
                        negate(rotate(subtract(z_value, k_value))),
                    )
                    assert add(a_value, r_v) == c_value

        assert actual <= upper
        nonempty += bool(actual)

    assert nonempty >= 25


def verify_oriented_endpoint_factor() -> None:
    for prime in (7, 11, 17):
        points = welch(prime)
        k = len(points)
        for v_role, w_role in product((0, 1), (2, 3)):
            sigma_v = 1 if v_role == 0 else -1
            sigma_w = 1 if w_role == 2 else -1
            loads: Counter[Point] = Counter()
            for endpoint in points:
                for v_other in points:
                    if v_other == endpoint:
                        continue
                    for w_other in points:
                        if w_other in (endpoint, v_other):
                            continue
                        c_edge = (
                            subtract(endpoint, v_other)
                            if v_role == 0
                            else subtract(v_other, endpoint)
                        )
                        b_edge = (
                            subtract(endpoint, w_other)
                            if w_role == 2
                            else subtract(w_other, endpoint)
                        )
                        signed_difference = subtract(
                            scale(sigma_w, b_edge),
                            scale(sigma_v, c_edge),
                        )
                        assert signed_difference == subtract(v_other, w_other)
                        loads[signed_difference] += 1
            assert max(loads.values(), default=0) == k - 2


def main() -> None:
    verify_random_identities()
    verify_mixed_min_bound()
    verify_oriented_endpoint_factor()
    print("SWAP PROJECTED-KEY MIXED CODEGREE MIN GATE: PASS")


if __name__ == "__main__":
    main()
