#!/usr/bin/env python3
"""Exact checks for FIXED_RANK_BOOLEAN_SOURCE_MIDSHADOW_GATE."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, log2


def middle_faces(carrier, q):
    low = (q + 2) // 3
    high = 2 * q // 3
    carrier = tuple(carrier)
    return {
        frozenset(face)
        for t in range(low, high + 1)
        for face in combinations(carrier, t)
    }


def audit(carriers, q, r, weighted=False):
    carrier_faces = [middle_faces(carrier, q) for carrier in carriers]
    bq = sum(comb(q, t) for t in range((q + 2) // 3, 2 * q // 3 + 1))
    assert all(len(bank) == bq for bank in carrier_faces)

    codegree = Counter(face for bank in carrier_faces for face in bank)
    omega = max(codegree.values())
    union = set(codegree)
    assert len(carriers) * bq == sum(codegree.values())
    assert len(carriers) * bq <= omega * len(union)

    # Assign every rank-r source to each carrier.  In the overlapping test,
    # divide its weight by its actual carrier codegree, so every physical
    # source has total weight exactly one.
    source_degree = Counter(
        frozenset(source)
        for carrier in carriers
        for source in combinations(carrier, r)
    )
    source_weight = defaultdict(Fraction)
    W = Fraction()
    carrier_weight = []
    for carrier in carriers:
        Wq = Fraction()
        for source in combinations(carrier, r):
            source = frozenset(source)
            weight = Fraction(1, source_degree[source]) if weighted else Fraction(1)
            source_weight[source] += weight
            W += weight
            Wq += weight
        carrier_weight.append(Wq)
    if weighted:
        assert set(source_weight.values()) == {Fraction(1)}
    else:
        assert max(source_weight.values()) == 1

    assert W <= len(carriers) * comb(q, r)
    capacity = comb(q, r)
    weighted_load = Counter()
    for Wq, bank in zip(carrier_weight, carrier_faces):
        density = Wq / capacity
        assert 0 <= density <= 1
        for face in bank:
            weighted_load[face] += density
    weighted_lambda = max(weighted_load.values())
    assert weighted_lambda <= omega
    assert sum(weighted_load.values(), Fraction()) == W * bq / capacity

    # Equation (3), with the ordinary output universe restricted to the
    # explicitly generated middle bank, in both weighted and unweighted
    # forms.
    assert Fraction(len(union)) >= W * bq / (weighted_lambda * capacity)
    assert Fraction(len(union)) >= W * bq / (omega * comb(q, r))
    return bq, omega, weighted_lambda, len(union), W


def main():
    q, r, k = 12, 6, 3

    disjoint = [tuple(range(i * q, (i + 1) * q)) for i in range(k)]
    bq, omega, weighted_lambda, union, W = audit(disjoint, q, r)
    assert omega == 1 and union == k * bq
    assert weighted_lambda == 1
    assert W == k * comb(q, r)

    core = tuple(range(6))
    common_core = [core + tuple(range(6 + 6 * i, 12 + 6 * i)) for i in range(k)]
    bq2, omega2, weighted_lambda2, union2, W2 = audit(
        common_core, q, r, weighted=True
    )
    assert bq2 == bq and omega2 == k
    assert weighted_lambda2 <= omega2
    assert union2 * omega2 >= k * bq
    assert W2 <= k * comb(q, r)

    theta = 2 - log2(3)
    margin = Fraction(1, 2) - theta
    assert abs(margin - (log2(3) - Fraction(3, 2))) < 1e-14
    assert margin > 0

    print(
        "PASS: q=%d r=%d Bq=%d; disjoint omega=%d; "
        "common-core omega=%d; exponent margin=%.9f"
        % (q, r, bq, omega, omega2, margin)
    )


if __name__ == "__main__":
    main()
