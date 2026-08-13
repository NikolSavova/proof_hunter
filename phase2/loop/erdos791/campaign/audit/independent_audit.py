#!/usr/bin/env python3
"""Independent finite checks for the #791 family and reflected tile lemmas."""

from __future__ import annotations

import random
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from verifier import prefix_length, tile_coverage  # noqa: E402


RECORD = Fraction(85, 294)


def add(left: set[int], right: set[int]) -> set[int]:
    return {x + y for x in left for y in right}


def family(h: int, b: int, n: int, r: int) -> tuple[set[int], set[int], set[int], int, int]:
    u = (h + 1) * n + 2 * h
    first = 2 * u + h * (b - h - 1)
    delta = u + h * b + 1
    i_set = {0, h} | {u + h * i for i in range(b)}
    j_set = {2 * h + (h + 1) * j for j in range(n)}
    k_set = set(range(h))
    for v in range(r):
        k_set.update(range(first + v * delta, first + v * delta + h + 1))
    ell = n + b + h + 2 + r * (h + 1)
    m = first + r * delta
    return i_set, j_set, k_set, ell, m


def check_family_box() -> None:
    equality: list[tuple[int, int, int, int, int, int]] = []
    checked = 0
    for h in range(1, 21):
        for r in range(10):
            for b in range(h + 1, 41):
                for n in range(h, 41):
                    i_set, j_set, k_set, ell, m = family(h, b, n, r)
                    actual = prefix_length(tile_coverage(i_set, j_set, k_set))
                    assert actual == m, (h, b, n, r, m, actual)
                    ratio = Fraction(m, ell * ell)
                    assert ratio <= RECORD, (h, b, n, r, ratio)
                    if ratio == RECORD:
                        equality.append((h, b, n, r, ell, m))
                    checked += 1
    assert equality == [(5, 6, 17, 2, 42, 510)], equality
    print(f"family: {checked} tuples pass; unique equality {equality[0]}")


def check_bounded_coin_box() -> None:
    checked = 0
    for h in range(1, 31):
        for b in range(h + 1, 51):
            for n in range(h, 51):
                values = {h * i + (h + 1) * j for i in range(b) for j in range(n)}
                low = h * (h - 1)
                high = h * (b - 1) + (h + 1) * (n - 1) - low
                assert set(range(low, high + 1)) <= values, (h, b, n)
                checked += 1
    print(f"bounded coin: {checked} parameter triples pass")


def shapes(t: int) -> dict[str, set[int]]:
    return {
        "V": set(range(t + 1)),
        "H": {i * t for i in range(t)},
        "S": {i * (t + 1) for i in range(t)},
        "T0": {i * (t - 1) for i in range(t + 1)},
        "T1": {i * (t - 1) + 1 for i in range(t + 1)},
    }


def conservative_coverage(p: dict[str, set[int]]) -> set[int]:
    ij = add(p["I"], p["J"])
    ik = add(p["I"], p["K"])
    il = add(p["I"], p["L0"])
    jk = add(p["J"], p["K"])
    jl = add(p["J"], p["L0"])
    kl0 = add(p["K"], p["L0"])
    kl1 = add(p["K"], p["L1"])
    candidates = ij | ik | il
    candidates |= {q for q in jk if q - 1 in jk}
    candidates |= {q for q in jl if q - 1 in jl}
    candidates |= {q for q in kl1 if q - 1 in kl0}
    candidates |= {q for q in kl0 if q - 1 in kl1}
    return candidates


def expand_four_tile(t: int, p: dict[str, set[int]]) -> set[int]:
    block = t * t
    e = shapes(t)
    return (
        {x + block * q for x in e["V"] for q in p["I"]}
        | {x + block * q for x in e["H"] for q in p["J"]}
        | {x + block * q for x in e["S"] for q in p["K"]}
        | {x + block * q for x in e["T0"] for q in p["L0"]}
        | {x + block * q for x in e["T1"] for q in p["L1"]}
    )


def check_reflected_random() -> None:
    rng = random.Random(791_04)
    checks = 0
    for t in range(2, 22, 2):
        block = t * t
        for _ in range(100):
            p = {
                name: set(rng.sample(range(13), rng.randrange(0, 6)))
                for name in ("I", "J", "K", "L0", "L1")
            }
            certified = conservative_coverage(p)
            basis = expand_four_tile(t, p)
            sums = add(basis, basis)
            for q in certified:
                assert set(range(q * block, (q + 1) * block)) <= sums, (t, p, q)
                checks += 1
    print(f"reflected tile: {checks} randomly certified squares pass literal expansion")


if __name__ == "__main__":
    check_bounded_coin_box()
    check_family_box()
    check_reflected_random()
