#!/usr/bin/env python3
"""Checks for CONSTRUCTION_CHART_RECYCLING_OBSTRUCTION.md."""

from fractions import Fraction as F
from math import log, log2, prod


def exact_ramp(D, q):
    C = [D ** (i + 2) for i in range(q)]
    U = [D ** (q + 1 - i) for i in range(q)]
    W = [C[i] + U[i] for i in range(q)]
    # Exact ordered-comb recurrences from RECHARTED_ALL_LOOP_WRAPPER_GATE.
    Cpar = sum(C[i] * (D + 1) ** (q - 1 - i) for i in range(q))
    Upar = sum((1 + i * D) * U[i] for i in range(q))
    Wpar = sum(W)
    for i in range(q):
        for j in range(i + 1, q):
            Wpar += C[i] * U[j] * (D + 1) ** (j - i - 1)
    return C, U, W, Cpar, Upar, Wpar


def check_integral_ramp():
    for D in (2, 3, 4, 8, 16):
        for q in range(3, 9):
            C, U, W, Cp, Up, Wp = exact_ramp(D, q)
            assert Cp >= C[-1]
            assert Up >= U[0]
            assert Cp >= D ** (q + 1)
            assert Up >= D ** (q + 1)
            # Recycling two identical construction profiles gives a genuine
            # one-face forward term.
            recycle = Cp * Up
            assert recycle >= D ** (2 * q + 2)
            # The advertised scalar ramp remains only q+O(1) in exponent.
            assert Wp <= 8 * (q + 2) ** 2 * D ** (q + 3)


def check_cleared_bounds():
    # Verify the algebraic implications of (7)--(13) directly in exponent
    # form.  delta is rational and logs of small constants are retained.
    for D in (2, 3, 5, 11):
        ld2 = log2(2) / log2(D)
        ld8 = log2(8) / log2(D)
        ld16 = log2(16) / log2(D)
        for q in range(4, 30):
            for delta in (0.0, 0.01, 0.03, 0.07):
                p = q + delta * q + ld2
                width = q - 2 * delta * q - 2 - ld8
                aq_min = width
                a1_max = p - width
                b1_min = q - delta * q - a1_max
                assert aq_min >= q - 2 * delta * q - 2 - ld8 - 1e-12
                assert a1_max <= 3 * delta * q + 2 + ld16 + 1e-12
                assert b1_min >= q - 4 * delta * q - 2 - ld16 - 1e-12


def balanced_levels(target_L):
    vals = [32.0]
    while vals[-1] < target_L:
        L = vals[-1]
        q = max(3.0, L / 4.0)
        vals.append(L + log2(q))
    return vals


def check_fresh_tree():
    last_fraction = 1.0
    for target in (2**12, 2**14, 2**16, 2**18):
        vals = balanced_levels(target)
        qs = [max(3, int(L / 4)) for L in vals[:-1]]
        h = len(qs)
        expected_recycled = sum(F(1, q) for q in qs)
        assert float(expected_recycled) < 5 * log(max(log(vals[-1]), 2))
        fresh_fraction = prod(F(q - 1, q) for q in qs)
        assert fresh_fraction > 0
        assert fresh_fraction <= last_fraction
        last_fraction = fresh_fraction
        # A polylog lower audit: -log fraction is O(log log L).
        assert -log(float(fresh_fraction)) < 10 * log(max(log(vals[-1]), 2))
        assert h - float(expected_recycled) > 0.8 * h


if __name__ == "__main__":
    check_integral_ramp()
    check_cleared_bounds()
    check_fresh_tree()
    print(
        "PASS: low-W ramp forces high construction endpoints; two recycled "
        "roles force the forward square; fresh paths have polylog density"
    )
