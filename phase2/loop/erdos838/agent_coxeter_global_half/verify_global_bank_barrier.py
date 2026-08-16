#!/usr/bin/env python3
"""Exact verifier for GLOBAL_BANK_AMPLIFICATION_BARRIER.md."""

from __future__ import annotations

import json
import math
from fractions import Fraction as Q
from itertools import combinations

from verify_saturation_bank_dichotomy import (
    N58_CERTIFICATE,
    check_sign_family,
    longest_temporal_ranks,
    product,
    rich_polynomial,
)


def one_exception_exact(n: int) -> dict[str, object]:
    # This call independently constructs coordinates, checks the reduced word,
    # and replays every cell against the temporal-path formulas.
    check_sign_family(n, alternating=False)

    fan_x = Q(n * (n - 1), 2)
    fan_g = Q((n - 1) * (n + 2), 16)
    fan_b = 2 * n - 3
    fan_gb4 = fan_x + n - 2
    assert Q(n) * fan_g / fan_x == Q(n + 2, 8)
    assert fan_x / fan_g == Q(8 * n, n + 2)

    external_x = (1 << (n - 1)) - n
    external_g = Q(3, 2) ** (n - 1) - 1 - Q(n - 1, 2)
    f_one = 1 + n + fan_x + external_x
    f_half = 1 + Q(n, 2) + fan_g + external_g
    total_bank = fan_b + external_x

    assert f_one == (1 << (n - 1)) + 1 + fan_x
    assert f_half == Q(3, 2) ** (n - 1) + Q(1, 2) + fan_g
    assert total_bank == (1 << (n - 1)) + n - 3
    assert fan_gb4 / fan_x == Q(fan_x + n - 2, fan_x)
    return {
        "n": n,
        "fan_X": fan_x,
        "fan_G": fan_g,
        "fan_B": fan_b,
        "fan_H": Q(n) * fan_g / fan_x,
        "full_F_one": f_one,
        "full_F_half": f_half,
        "full_H": Q(n) * f_half / f_one,
        "total_bank": total_bank,
    }


def alternating_exact(n: int) -> dict[str, object]:
    check_sign_family(n, alternating=True)
    total_x = Q(0)
    total_g = Q(0)
    total_b = 0
    total_gb = Q(0)
    sum_sqrt_x = 0.0
    for distance in range(1, n):
        multiplicity = n - distance
        x = rich_polynomial(distance, Q(1), True)
        g = Q(1, 2) * rich_polynomial(distance, Q(1, 2), True)
        bank = 1 << (distance // 2)
        assert 4 * g * bank >= x
        total_x += multiplicity * x
        total_g += multiplicity * g
        total_b += multiplicity * bank
        total_gb += multiplicity * g * bank
        sum_sqrt_x += multiplicity * math.sqrt(float(x))

    assert total_x <= 4 * total_gb
    assert sum_sqrt_x**2 <= 4 * float(total_g) * total_b + 1e-6
    f_one = 1 + n + total_x
    f_half = 1 + Q(n, 2) + total_g
    return {
        "n": n,
        "bank_fraction": Q(total_b, total_x),
        "dilation": total_x / (4 * total_g),
        "H": Q(n) * f_half / f_one,
    }


def n58_exact() -> dict[str, object]:
    saved = json.loads(N58_CERTIFICATE.read_text())["finite_braid_record"]
    n = int(saved["n"])
    wires = list(range(n))
    roots = []
    for generator in map(int, saved["word_zero_based"]):
        i, j = wires[generator : generator + 2]
        assert i < j
        roots.append((i, j))
        wires[generator], wires[generator + 1] = j, i
    assert wires == list(reversed(range(n)))
    roots = tuple(roots)
    positions = {root: index for index, root in enumerate(roots)}
    forward_rank = longest_temporal_ranks(n, positions, True)
    reverse_rank = longest_temporal_ranks(n, positions, False)
    forward_one = product(n, roots, Q(1))
    reverse_one = product(n, tuple(reversed(roots)), Q(1))
    forward_half = product(n, roots, Q(1, 2))
    reverse_half = product(n, tuple(reversed(roots)), Q(1, 2))

    total_x = Q(0)
    total_g = Q(0)
    total_b = 0
    total_gb = Q(0)
    sum_sqrt_x = 0.0
    small_x = Q(0)
    small_g = Q(0)
    maximum_dimension = 0
    for u, v in combinations(range(n), 2):
        x = forward_one[v][u] * reverse_one[v][u]
        g = forward_half[v][u] * reverse_half[v][u]
        dimension = forward_rank[(u, v)] + reverse_rank[(u, v)]
        bank = 1 << dimension
        assert 4 * g * bank >= x
        total_x += x
        total_g += g
        total_b += bank
        total_gb += g * bank
        sum_sqrt_x += math.sqrt(float(x))
        maximum_dimension = max(maximum_dimension, dimension)
        if dimension <= 6:
            small_x += x
            small_g += g

    assert total_x == 1059609
    assert total_g == Q(18721123, 512)
    assert total_b == 55221
    assert maximum_dimension == 8
    assert total_x <= 4 * total_gb
    assert sum_sqrt_x**2 <= 4 * float(total_g) * total_b + 1e-6
    assert float(small_g / total_g) > 0.86548
    return {
        "n": n,
        "X": total_x,
        "G": total_g,
        "B": total_b,
        "dilation": total_x / (4 * total_g),
        "offdiagonal_H": Q(n) * total_g / total_x,
        "small_bank_mass_fraction": small_g / total_g,
        "small_bank_H": Q(n) * small_g / small_x,
    }


def main() -> None:
    one_rows = [one_exception_exact(n) for n in (16, 32, 48)]
    alternating_rows = [alternating_exact(n) for n in (16, 32, 48)]
    n58 = n58_exact()

    print("global endpoint-bank barrier: PASS")
    for row in one_rows:
        print(
            f"one-exception n={row['n']:2d} fan(X,G,B)="
            f"({row['fan_X']},{row['fan_G']},{row['fan_B']}) "
            f"fan_H={float(row['fan_H']):.6f} full_H={float(row['full_H']):.6f}"
        )
    for row in alternating_rows:
        print(
            f"alternating   n={row['n']:2d} B/X={float(row['bank_fraction']):.6f} "
            f"dilation={float(row['dilation']):.6f} H={float(row['H']):.6f}"
        )
    print(
        f"n58 (X,G,B)=({n58['X']},{n58['G']},{n58['B']}) "
        f"dilation={float(n58['dilation']):.6f} "
        f"small-bank-mass={float(n58['small_bank_mass_fraction']):.6f} "
        f"small-bank-H={float(n58['small_bank_H']):.6f}"
    )


if __name__ == "__main__":
    main()
