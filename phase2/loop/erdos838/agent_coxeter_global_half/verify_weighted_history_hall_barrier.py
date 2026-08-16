#!/usr/bin/env python3
"""Exact verifier for WEIGHTED_ROOTED_HISTORY_HALL_BARRIER.md."""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb

from verify_rooted_fan_complement import (
    add_coherent_root,
    cup_cap_lengths,
    cup_cap_set,
    genericize,
    orient,
    root_order,
)
from verify_saturation_bank_dichotomy import product


Profile = tuple[int, Q, Q, Q]  # number of points, cap, cup, ordinary


def es_profile(r: int, s: int, activity: Q) -> Profile:
    """Exact separated-composition profile at one activity."""
    cache: dict[tuple[int, int], Profile] = {}

    def go(rr: int, ss: int) -> Profile:
        if rr == 2 or ss == 2:
            return 1, activity, activity, activity
        key = rr, ss
        if key not in cache:
            na, ca, ua, va = go(rr, ss - 1)
            nb, cb, ub, vb = go(rr - 1, ss)
            cache[key] = (
                na + nb,
                ca * (1 + nb * activity) + cb,
                ua + ub * (1 + na * activity),
                va + vb + ca * ub,
            )
        return cache[key]

    return go(r, s)


def enumerate_cup_polynomial(points) -> tuple[int, ...]:
    """Cup f-vector; the ES rank bound avoids a 2^m enumeration."""
    cup_rank, _ = cup_cap_lengths(points)
    counts = [0] * (cup_rank + 1)
    for rank in range(1, cup_rank + 1):
        for subset in combinations(range(len(points)), rank):
            if all(
                orient(points[subset[index]], points[subset[index + 1]], points[subset[index + 2]]) > 0
                for index in range(rank - 2)
            ):
                counts[rank] += 1
    return tuple(counts)


def evaluate(coefficients: tuple[int, ...], activity: Q) -> Q:
    return sum((coefficient * activity**rank for rank, coefficient in enumerate(coefficients)), Q(0))


def matrix_history_check(k: int) -> dict[str, object]:
    base = genericize(cup_cap_set(k, k))
    assert cup_cap_lengths(base) == (k - 1, k - 1)
    # The symmetric construction has equally many cup and cap triples; use
    # the positive coherent root.
    positive = sum(
        orient(*(base[index] for index in triple)) > 0
        for triple in combinations(range(len(base)), 3)
    )
    assert positive * 2 == comb(len(base), 3)
    points = add_coherent_root(base, 1)
    roots = root_order(points)

    results = {}
    for activity in (Q(1), Q(1, 2)):
        forward = product(len(points), roots, activity)
        reverse = product(len(points), tuple(reversed(roots)), activity)
        rooted_mass = sum(
            (forward[v][0] * reverse[v][0] for v in range(1, len(points))),
            Q(0),
        )
        _, _, cups, _ = es_profile(k, k, activity)
        assert rooted_mass == activity * cups
        results[activity] = rooted_mass

    if k <= 5:
        coefficients = enumerate_cup_polynomial(base)
        for activity in (Q(1), Q(1, 2)):
            assert evaluate(coefficients, activity) == es_profile(k, k, activity)[2]
    return {
        "k": k,
        "m": len(base),
        "rooted_one": results[Q(1)],
        "rooted_half": results[Q(1, 2)],
    }


def symbolic_row(k: int) -> dict[str, object]:
    one = es_profile(k, k, Q(1))
    half = es_profile(k, k, Q(1, 2))
    m, caps_one, cups_one, faces_one = one
    other_m, caps_half, cups_half, _ = half
    assert other_m == m
    assert caps_one == cups_one
    assert caps_half == cups_half
    assert m == comb(2 * k - 4, k - 2)

    history_lower = Q(1, 2)
    for r in range(3, k + 1):
        history_lower *= 1 + Q(comb(r + k - 5, r - 2), 2)
    assert cups_half >= history_lower
    assert cups_one <= k * m ** (k - 1)

    # Exact full-cut load when both signs are pooled, with their overlap
    # deliberately ignored to give the decoder extra capacity.
    hall_load = Q(m + 1) * cups_half / (4 * cups_one)
    rank_load = Q(m + 1, 1 << (k + 1))
    assert cups_half * (1 << (k - 1)) >= cups_one
    assert hall_load >= rank_load
    assert (1 << (2 * k - 4)) <= (2 * k - 3) * m

    # Squared form of rank_load >= sqrt(m)/(8 sqrt(2k-3)).
    assert rank_load * rank_load * 64 * (2 * k - 3) >= m
    return {
        "k": k,
        "m": m,
        "cups_one": cups_one,
        "cups_half": cups_half,
        "faces_one": faces_one,
        "activity_ratio": cups_one / cups_half,
        "hall_load": hall_load,
        "mixed_capacity_ratio": faces_one / cups_one,
    }


def main() -> None:
    geometric = [matrix_history_check(k) for k in (4, 5, 6)]
    rows = [symbolic_row(k) for k in range(4, 21)]
    expected = {
        6: (17.907119299063865, 0.991225875226504, 178.0963428201474),
        8: (85.27314871573175, 2.7118735907231425, 8422733.290439991),
        10: (374.79172440373173, 8.585435030934107, 301071857261275.5),
        12: (1585.2402756332986, 29.137065661259164, 9.32867186057448e24),
    }
    for row in rows:
        if row["k"] in expected:
            observed = (
                float(row["activity_ratio"]),
                float(row["hall_load"]),
                float(row["mixed_capacity_ratio"]),
            )
            assert all(
                abs(got - want) <= 1e-12 * max(1.0, abs(want))
                for got, want in zip(observed, expected[row["k"]])
            )

    print("weighted rooted-history Hall barrier: PASS")
    for row in geometric:
        print(
            f"geometry E({row['k']},{row['k']}) m={row['m']:2d} "
            f"rooted(1,1/2)=({row['rooted_one']},{row['rooted_half']})"
        )
    for k in (6, 8, 10, 12, 16, 20):
        row = rows[k - 4]
        print(
            f"symbolic k={k:2d} m={row['m']:10d} "
            f"U1/Uhalf={float(row['activity_ratio']):10.4f} "
            f"Hall-load={float(row['hall_load']):10.4f} "
            f"V1/U1={float(row['mixed_capacity_ratio']):.4e}"
        )


if __name__ == "__main__":
    main()
