#!/usr/bin/env python3
"""Exact checks for the growing-scale rounding/tiling analysis.

The script is deliberately finite and does not certify an asymptotic result.
It exhausts the interval-factorization theorem for q=2,3,4, verifies the
canonical cyclotomic factorizations for further primes, checks the alteration
pair-capacity inequality on all small sets, and records diffuse-rounding lower
bounds for representative quadratic regimes.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path


def sumset(a: tuple[int, ...], b: tuple[int, ...]) -> set[int]:
    return {x + y for x in a for y in b}


def exhaustive_factorizations(q: int) -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    interval = set(range(q * q))
    subsets = [(0,) + tail for tail in combinations(range(1, q * q), q - 1)]
    answers = []
    for x in subsets:
        for y in subsets:
            if sumset(x, y) == interval:
                answers.append((x, y))
    return answers


def canonical_factorization(q: int) -> bool:
    fine = tuple(range(q))
    coarse = tuple(q * j for j in range(q))
    return sumset(fine, coarse) == set(range(q * q))


def repair_capacity_checks(max_coordinate: int = 7) -> int:
    """Check |(A+X) union (X+X)| <= |A||X|+r(r+1)/2."""
    universe = range(max_coordinate + 1)
    checked = 0
    all_sets = []
    for size in range(max_coordinate + 2):
        all_sets.extend(combinations(universe, size))
    for a in all_sets:
        for x in all_sets:
            lhs = len(sumset(a, x) | sumset(x, x))
            r = len(x)
            rhs = len(a) * r + r * (r + 1) // 2
            assert lhs <= rhs
            checked += 1
    return checked


def diffuse_bound(c: Fraction, eta: Fraction) -> float:
    """Finite-form lower fraction from Theorem 2.1, ignoring an o(1) core."""
    return float((1 - eta) * math.exp(-1 / (2 * float(c) * (1 - float(eta) ** 2))))


def block_absorber_check(limit: int = 80) -> int:
    checked = 0
    for n in range(limit + 1):
        for length in range(1, n + 2):
            p = set(range(length))
            blocks = [set(range(start, min(start + length, n + 1)))
                      for start in range(0, n + 1, length)]
            # Use alternating blocks as an arbitrary bad-block pattern.
            bad = blocks[::2]
            starts = {min(block) for block in bad if block}
            repaired = sumset(tuple(p), tuple(starts))
            assert set().union(*bad) <= repaired
            checked += 1
    return checked


def growing_modulus_rows() -> list[dict]:
    rows = []
    for root in (10, 20, 30, 40, 50):
        m_total = root * root
        q = root
        macro_bins = 8
        table = [[0] * q for _ in range(macro_bins)]
        for n in range(m_total):
            table[(macro_bins * n) // m_total][n % q] += 1
        expected = Fraction(m_total, macro_bins * q)
        l1 = sum(abs(Fraction(value) - expected)
                 for row in table for value in row)
        rows.append({
            "M": m_total,
            "q_floor_sqrt_M": q,
            "macro_bins": macro_bins,
            "normalized_l1_cell_discrepancy": float(l1 / m_total),
            "general_upper_order": "O(m*q/M)",
        })
    return rows


def main() -> None:
    factorizations = {}
    for q in (2, 3, 4):
        found = exhaustive_factorizations(q)
        canonical = {
            (tuple(range(q)), tuple(q * j for j in range(q))),
            (tuple(q * j for j in range(q)), tuple(range(q))),
        }
        if q in (2, 3):
            assert set(found) == canonical
        # For composite q there can be further cyclotomic allocations, but
        # normalization still gives a unique partner and no self-partner.
        partners: dict[tuple[int, ...], set[tuple[int, ...]]] = {}
        for x, y in found:
            partners.setdefault(x, set()).add(y)
        assert all(len(values) == 1 for values in partners.values())
        assert all(x not in values for x, values in partners.items())
        factorizations[str(q)] = {
            "normalized_pairs_checked": math.comb(q * q - 1, q - 1) ** 2,
            "number_of_factorizations": len(found),
            "factorizations": found,
        }

    primes = (2, 3, 5, 7, 11, 13, 17, 19)
    assert all(canonical_factorization(q) for q in primes)

    rows = []
    for c in (Fraction(1, 4), Fraction(85, 294), Fraction(2, 5), Fraction(9, 20)):
        rows.append({
            "c": str(c),
            "eta": "1/100",
            "certified_expected_hole_fraction_lower_bound": diffuse_bound(c, Fraction(1, 100)),
            "limiting_eta_to_zero_bound": math.exp(-1 / (2 * float(c))),
        })

    output = {
        "status": "PASS",
        "scope": "finite theorem checks only",
        "exhaustive_interval_factorizations": factorizations,
        "canonical_factorization_primes_checked": primes,
        "repair_capacity_set_pairs_checked": repair_capacity_checks(),
        "block_absorber_parameter_pairs_checked": block_absorber_check(),
        "diffuse_rounding_bounds": rows,
        "growing_modulus_target_equidistribution": growing_modulus_rows(),
    }
    target = Path(__file__).with_name("GROWING_SCALE_CHECKS.json")
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
