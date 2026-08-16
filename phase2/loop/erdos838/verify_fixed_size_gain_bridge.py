#!/usr/bin/env python3
"""Exact arithmetic checks for FIXED_SIZE_GAIN_BRIDGE_20260815.md."""

from fractions import Fraction
from math import comb, floor, log2


def check_double_count_identity() -> int:
    rows = 0
    for n in range(2, 35):
        for k in range(1, n + 1):
            for m in range(k, n + 1):
                lhs = comb(n, m) * comb(m, k)
                rhs = comb(n, k) * comb(n - k, m - k)
                assert lhs == rhs
                rows += 1
    return rows


def coefficient(rho: Fraction, sigma: Fraction, beta: Fraction) -> Fraction:
    return beta - (rho - sigma) * beta * beta


def check_half_scale_formula() -> int:
    rows = 0
    rho = Fraction(2)
    for eta_num in range(1, 10):
        eta = Fraction(eta_num, 20)
        sigma = 1 + eta
        beta = Fraction(1, 2)
        assert coefficient(rho, sigma, beta) == (1 + eta) / 4
        # The unconstrained vertex lies to the right of 1/2 when eta>0,
        # so beta=1/2 is the constrained maximizer.
        vertex = Fraction(1, 2) / (rho - sigma)
        assert vertex > beta
        rows += 1
    return rows


def check_canonical_rounding() -> int:
    rows = 0
    for n in range(2, 5000):
        ell = log2(n)
        k = floor(ell / 2)
        m = 4**k
        assert m <= n
        assert abs(k - ell / 2) <= 1
        rows += 1
    return rows


if __name__ == "__main__":
    identities = check_double_count_identity()
    formulas = check_half_scale_formula()
    rounding = check_canonical_rounding()
    print(
        "PASS: fixed-size gain bridge; "
        f"identities={identities}, formulas={formulas}, rounding={rounding}"
    )
