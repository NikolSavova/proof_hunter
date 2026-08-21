#!/usr/bin/env python3
"""Exact checks for the role-projected completion reservoir gate."""

from __future__ import annotations

from collections import Counter
import random

from analyze_affine_costas_energy import welch
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import (
    add,
    linear,
    overlap_table,
    rich_fibres,
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


def verify_role_maps() -> None:
    rng = random.Random(120812083)
    for _ in range(50000):
        p = rng.randrange(-30, 31), rng.randrange(-30, 31)
        q = rng.randrange(-30, 31), rng.randrange(-30, 31)
        x_value = rng.randrange(-30, 31), rng.randrange(-30, 31)
        ell = rng.randrange(-30, 31), rng.randrange(-30, 31)
        u = rng.randrange(-20, 21), rng.randrange(-20, 21)

        # Moving-W role: retain the perpendicular half (r, B).
        z0 = add(ell, linear(p))
        b_value = subtract(z0, linear(q))
        r_value = subtract(q, u)
        cross = subtract(subtract(z0, q), rotate(u))
        assert cross == add(b_value, rotate(r_value))
        recovered_q = inverse_linear(subtract(z0, b_value))
        recovered_u = subtract(recovered_q, r_value)
        assert recovered_q == q and recovered_u == u
        a_value = add(x_value, u)
        assert add(a_value, r_value) == add(x_value, q)

        # Moving-V role: retain the parallel half (r, A).
        w_value = rng.randrange(-30, 31), rng.randrange(-30, 31)
        r0 = add(w_value, linear(q))
        ell_p = subtract(r0, linear(p))
        r_value = subtract(p, u)
        a_value = add(x_value, u)
        physical_v = add(x_value, p)
        assert add(a_value, r_value) == physical_v
        recovered_u = subtract(a_value, x_value)
        recovered_p = add(r_value, recovered_u)
        assert recovered_u == u and recovered_p == p
        cross = subtract(subtract(r0, p), rotate(u))
        assert cross == add(ell_p, rotate(r_value))


def verify_projection_sizes() -> None:
    for prime in (11, 13, 17):
        points = welch(prime)
        differences = difference_set(points)
        overlaps = overlap_table(differences)
        _, support, popular = rich_fibres(differences, adaptive=True)
        number = len(differences)
        assert popular

        parallel = {
            (shift, start)
            for shift in popular
            for start in overlaps[shift]
        }
        perpendicular = {
            (shift, start)
            for shift in popular
            for start in overlaps[rotate(shift)]
        }
        square = sum(
            len(overlaps[shift]) * len(overlaps[rotate(shift)])
            for shift in popular
        )
        assert len(parallel) == sum(len(overlaps[r]) for r in popular)
        assert len(perpendicular) == sum(
            len(overlaps[rotate(r)]) for r in popular
        )
        # K=support/number; avoid floating-point comparisons.
        assert len(parallel) * support < square * number
        assert len(perpendicular) * support < square * number


def verify_reuse_charges() -> None:
    rng = random.Random(271828183)
    for _ in range(5000):
        key_count = rng.randrange(1, 80)
        threshold = rng.randrange(1, 20)
        loads = [rng.randrange(0, 4 * threshold + 1) for _ in range(key_count)]
        low_mass = sum(load for load in loads if load < threshold)
        assert low_mass < threshold * key_count

        group_band = rng.randrange(1, 20)
        weights = [
            [rng.randrange(1, 2 * group_band) for _ in range(load)]
            for load in loads
        ]
        weighted_low = sum(
            sum(row)
            for load, row in zip(loads, weights)
            if load < threshold
        )
        assert weighted_low < 2 * group_band * threshold * key_count

        # Exact two-level row/column decomposition of a completion fibre.
        a_size = rng.randrange(1, 20)
        b_size = rng.randrange(1, 20)
        corner_threshold = rng.randrange(1, 10)
        table = {
            (a_index, b_index): rng.randrange(corner_threshold)
            for a_index in range(a_size)
            for b_index in range(b_size)
        }
        perpendicular_loads = Counter()
        parallel_loads = Counter()
        for (a_index, b_index), load in table.items():
            perpendicular_loads[b_index] += load
            parallel_loads[a_index] += load
        assert max(perpendicular_loads.values()) < corner_threshold * a_size
        assert max(parallel_loads.values()) < corner_threshold * b_size


def main() -> None:
    verify_role_maps()
    verify_projection_sizes()
    verify_reuse_charges()
    print("SWAP ROLE-PROJECTED COMPLETION RESERVOIR GATE: PASS")


if __name__ == "__main__":
    main()
