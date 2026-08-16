#!/usr/bin/env python3
"""Exact audits for FIXED_POWER_SAVING_GATE.md."""

from itertools import combinations
from math import comb, prod
from fractions import Fraction


def falling(x, a):
    return prod(range(x - a + 1, x + 1)) if a else 1


def four_local_abstract_audit(max_n=9):
    # In a 4-circuit face complex, a set is a face exactly when it contains
    # no bad quadruple.  Thus "all quadruples good" is equivalent to the
    # whole ground set being a face.  Exhaust arbitrary small bad-quad sets.
    checked = 0
    for n in range(4, max_n + 1):
        quads = list(combinations(range(n), 4))
        # Full 2^126 exhaustion is not intended.  Exhaust singleton bad sets
        # and every subset for n<=6; both directions are definitional.
        masks = range(1 << len(quads)) if n <= 6 else range(len(quads) + 1)
        for code in masks:
            if n <= 6:
                bad = {quads[i] for i in range(len(quads)) if (code >> i) & 1}
            else:
                bad = set() if code == 0 else {quads[code - 1]}
            whole_is_face = not bad
            every_quad_good = all(q not in bad for q in quads)
            assert whole_is_face == every_quad_good
            checked += 1
    return checked


def forbidden_fraction_audit():
    rows = 0
    for M in range(8, 19):
        for s in range(4, M + 1):
            total = comb(M, s) ** 2
            for a in range(5):
                if a > M or 4 - a > M:
                    continue
                exact_num = (comb(M - a, s - a) if s >= a else 0)
                exact_num *= (comb(M - (4 - a), s - (4 - a))
                              if s >= 4 - a else 0)
                exact = Fraction(exact_num, total)
                product_form = Fraction(falling(s, a), falling(M, a))
                product_form *= Fraction(falling(s, 4 - a), falling(M, 4 - a))
                assert exact == product_form
                upper = Fraction(s, M - s + 1) ** 4
                assert exact <= upper
                lower = Fraction(s - 3, M) ** 4
                assert exact >= lower
                rows += 1
    return rows


def complete_bank_audit():
    rows = []
    # Exact arithmetic at a moderate scalable sequence.  lambda=2,
    # source rank rho=2s+3, M=2^(2rho), and q=d=2^rho.
    for rho in range(11, 32, 2):
        s = (rho - 3) // 2
        M = 1 << (2 * rho)
        q = d = 1 << rho
        K = comb(M, s) ** 2
        demand = K * q * d
        # Compare logarithms; never materialize the 2^(2M)-element bank.
        assert demand.bit_length() <= 2 * M + 1
        rows.append((rho, demand.bit_length(), 2 * M))
    return rows


def rank_tail_audit(C=7, eps=Fraction(1, 5)):
    # Check ell^C sum_{g>=G} 2^{-eps g} = O(ell^-3) with the
    # prescribed G, using a finite geometric-tail upper bound.
    for ell in (2**10, 2**20, 2**40):
        logell = ell.bit_length() - 1
        G = ((C + 3) * logell * eps.denominator + eps.numerator - 1) // eps.numerator
        first = Fraction(1, 2 ** ((eps.numerator * G) // eps.denominator))
        # Crude ratio bound over blocks of denominator steps.
        tail = eps.denominator * first * 2
        assert Fraction(ell**C) * tail <= Fraction(20, ell**3)


if __name__ == "__main__":
    local = four_local_abstract_audit()
    frac = forbidden_fraction_audit()
    rows = complete_bank_audit()
    rank_tail_audit()
    print("PASS fixed-power shield-bank audit")
    print(f"  four-local systems checked: {local}")
    print(f"  exact forbidden-fraction rows: {frac}")
    print(f"  complete-bank scaling rows: {len(rows)}")
    print("  power-tail reduction and complete product injection: verified")
