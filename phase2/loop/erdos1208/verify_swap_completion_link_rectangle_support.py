#!/usr/bin/env python3
"""Exact checks for support growth in completion-link rectangles."""

from __future__ import annotations

from collections import Counter
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


def inverse_linear(value: Point) -> Point:
    assert (value[0] + value[1]) % 2 == 0
    assert (value[1] - value[0]) % 2 == 0
    return (
        (value[0] + value[1]) // 2,
        (value[1] - value[0]) // 2,
    )


def verify_link_normal_form() -> None:
    rng = random.Random(120812081)
    for _ in range(50000):
        p = rng.randrange(-20, 21), rng.randrange(-20, 21)
        x_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        ell = rng.randrange(-20, 21), rng.randrange(-20, 21)
        u = rng.randrange(-15, 16), rng.randrange(-15, 16)
        q = rng.randrange(-15, 16), rng.randrange(-15, 16)
        z0 = add(ell, linear(p))
        w_q = add(ell, linear(subtract(p, q)))
        z_q = add(w_q, rotate(q))
        assert z_q == subtract(z0, q)
        corners = (
            (p, x_value, ell),
            (subtract(p, u), add(x_value, u), ell),
            (q, x_value, w_q),
            (subtract(q, u), add(x_value, u), w_q),
        )
        assert corners[1][0][0] + corners[1][1][0] == p[0] + x_value[0]
        assert corners[1][0][1] + corners[1][1][1] == p[1] + x_value[1]
        first_output = subtract(q, u)
        second_output = subtract(z_q, rotate(u))
        recovered_u = inverse_linear(
            subtract(subtract(z0, first_output), second_output)
        )
        recovered_q = add(first_output, recovered_u)
        assert recovered_u == u and recovered_q == q

        # Dual pivot at the q-corner: p is now the moving coordinate.
        w_value = rng.randrange(-20, 21), rng.randrange(-20, 21)
        r0 = add(w_value, linear(q))
        ell_p = subtract(w_value, linear(subtract(p, q)))
        assert add(ell_p, linear(subtract(p, q))) == w_value
        dual_first = subtract(p, u)
        dual_second = subtract(subtract(r0, p), rotate(u))
        recovered_u = inverse_linear(
            subtract(subtract(r0, dual_first), dual_second)
        )
        recovered_p = add(dual_first, recovered_u)
        assert recovered_u == u and recovered_p == p
        assert add(ell_p, rotate(subtract(p, u))) == dual_second


def assert_vector_sidon(values: list[Point]) -> None:
    seen: set[Point] = set()
    for first, second in product(values, repeat=2):
        if first == second:
            continue
        difference = subtract(first, second)
        assert difference not in seen
        seen.add(difference)


def verify_rectangle_energy() -> None:
    source = [(4 * x + y, x + 5 * y) for x, y in welch(23)]
    rng = random.Random(161803399)
    for q_size in range(1, 15):
        for u_size in range(1, 15):
            for _ in range(40):
                q_values = rng.sample(source, q_size)
                assert_vector_sidon(q_values)
                u_values = [
                    (rng.randrange(-20, 21), rng.randrange(-20, 21))
                    for _ in range(u_size)
                ]
                # Sets suffice; remove accidental duplicate rows.
                u_values = sorted(set(u_values))
                if not u_values:
                    continue
                loads = Counter(
                    add(q_value, rotate(u_value))
                    for q_value, u_value in product(q_values, u_values)
                )
                energy = sum(load * load for load in loads.values())
                a, b = len(q_values), len(u_values)
                assert energy <= a * b + b * (b - 1)
                support = len(loads)
                assert support * (a * b + b * b) >= a * a * b * b
                assert a * min(a, b) <= 2 * support

                # The same estimate holds for an arbitrary occupied
                # subgraph G of U x Q; no rectangle extraction is needed.
                all_edges = list(product(q_values, u_values))
                sparse_edges = [
                    edge for edge in all_edges if rng.randrange(4) != 0
                ]
                if not sparse_edges:
                    sparse_edges = [rng.choice(all_edges)]
                sparse_loads = Counter(
                    add(q_value, rotate(u_value))
                    for q_value, u_value in sparse_edges
                )
                edge_count = len(sparse_edges)
                sparse_energy = sum(
                    load * load for load in sparse_loads.values()
                )
                assert sparse_energy <= edge_count + b * (b - 1)
                assert sparse_energy <= b * (a + b)
                assert len(sparse_loads) * b * (a + b) >= edge_count**2


def main() -> None:
    verify_link_normal_form()
    verify_rectangle_energy()
    print("SWAP COMPLETION-LINK RECTANGLE SUPPORT GATE: PASS")


if __name__ == "__main__":
    main()
