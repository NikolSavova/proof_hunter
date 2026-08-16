#!/usr/bin/env python3
"""Exact arithmetic checks for STABLE_CROSS_CIRCUIT_TOURNAMENT_CORE.md."""

from fractions import Fraction
from itertools import product
from math import comb


def stable_gap(L: int) -> Fraction:
    """Twice psi(L-5L2/2) minus Phi_3(L), with integer L2 samples."""
    L2 = L.bit_length() - 1
    return (
        Fraction(1, 2) * L * L2
        - L
        + Fraction(25, 8) * L2 * L2
        + Fraction(5, 2) * L2
    )


def tournament_outdegree(bits, t):
    out = [0] * t
    z = 0
    for i in range(t):
        for j in range(i + 1, t):
            if bits[z]:
                out[i] += 1
            else:
                out[j] += 1
            z += 1
    return max(out)


def check_type_pigeonhole(R=2, dmax=5):
    cases = 0
    for d in range(2 * R, dmax + 1):
        for rows in range(1, 4):
            for flat in product(range(R), repeat=rows * d):
                matrix = [flat[r * d:(r + 1) * d] for r in range(rows)]
                k = 1
                best = 0
                for typ in range(R):
                    for I in range(d):
                        best = max(best, sum(row[I] == typ for row in matrix))
                assert best * R * (2 * R) ** k >= rows
                cases += 1
    return cases


def check_binomial_bound():
    rows = []
    for R in range(2, 13):
        for d in range(4 * R, 20 * R + 1):
            for k in range(1, d // (2 * R) + 1):
                lhs = Fraction(comb(d // R, k), comb(d, k))
                rhs = Fraction(1, (2 * R) ** k)
                assert lhs >= rhs
                rows.append((R, d, k))
    return rows


def main():
    gaps = [(L, stable_gap(L)) for L in (64, 256, 1024, 4096)]
    assert all(g > 0 for _, g in gaps)

    tournaments = 0
    for t in range(2, 7):
        for bits in product((0, 1), repeat=comb(t, 2)):
            assert tournament_outdegree(bits, t) >= (t - 1) // 2
            tournaments += 1

    binom_rows = check_binomial_bound()
    type_cases = check_type_pigeonhole()
    print("PASS")
    print("  stable gaps:", [(L, float(g)) for L, g in gaps])
    print("  tournaments:", tournaments)
    print("  binomial rows:", len(binom_rows))
    print("  type systems:", type_cases)


if __name__ == "__main__":
    main()
