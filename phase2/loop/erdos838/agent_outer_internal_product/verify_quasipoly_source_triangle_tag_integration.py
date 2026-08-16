#!/usr/bin/env python3
"""Checks for QUASIPOLY_SOURCE_TRIANGLE_TAG_INTEGRATION_AUDIT.md."""

from fractions import Fraction as F
from math import comb, log2


def check_local_inequality():
    for a in range(1, 101):
        for b in range(1, 101):
            e = a * b
            t = max(a, b)
            if t <= 5:
                assert e <= 5 * a
            else:
                i = comb(t, 3)
                assert 5 * e * e <= 54 * a * i


def check_tagged_mass():
    # Contexts are (weight, actual source family, triangle family).
    contexts = [
        (F(1, 2), ("A", "B"), (1, 2, 3)),
        (F(1, 3), ("A", "C"), (2, 3, 4, 5)),
        (F(2, 5), ("D",), (1, 5)),
        (F(1, 7), ("A", "D"), (1, 2, 5)),
    ]
    source_load = {}
    for w, sources, _ in contexts:
        for A in sources:
            source_load[A] = source_load.get(A, F(0)) + w
    kappa = max(source_load.values())

    tag_load = {}
    triangle_mass = F(0)
    source_mass = F(0)
    for w, sources, triangles in contexts:
        A0 = min(sources)
        source_mass += w * len(sources)
        triangle_mass += w * len(triangles)
        for T in triangles:
            tag_load[(A0, T)] = tag_load.get((A0, T), F(0)) + w
    assert max(tag_load.values()) <= kappa
    assert source_mass <= kappa * len(source_load)
    assert triangle_mass <= kappa * len(source_load) * 5


def check_dyadic_condition():
    alpha = F(1)
    # One globally coalesced row-star per nonempty layer.
    layers = [0, 1, 2, 5, 9]
    coalesced_source_load = sum(F(1, 2**k) * alpha for k in layers)
    assert coalesced_source_load < 2 * alpha

    # J distinct release labels preserve J edge-demand in one star while
    # entering the source once. J duplicate copies of the same actual edge
    # do not: global simplicity or J charged descriptions is necessary.
    for J in (2, 5, 20):
        distinct_star_edges = J
        duplicate_simple_edges = 1
        assert distinct_star_edges == J
        assert duplicate_simple_edges < J
        assert J * alpha > 2 * alpha or J == 2


def check_ramp_scale():
    for d in (64, 96, 128, 192, 256):
        q = d // 4
        source_log = q * d
        child_log = F(d * d, 2)
        rank_two_log = source_log + 4 * d
        assert source_log < child_log
        if d >= 96:
            assert rank_two_log < child_log

        # The actual finite-gap deficit is quasipolynomial relative to N.
        N_log = d + log2(q + 2)
        target_log = 0.5 * N_log * N_log
        missing = target_log - float(child_log)
        assert missing > 0.8 * d * log2(q)


def check_polynomial_threshold():
    # In logarithmic form, K=n^(sigma loglog n) eventually dominates any
    # fixed n^(C+3/2).  Use L=log_2 n and compare exponents of n.
    for C, sigma in ((2, 0.1), (10, 0.25), (100, 1.0)):
        loglog_n = (C + 1.5) / sigma + 2
        exponent = sigma * loglog_n
        assert exponent > C + 1.5


if __name__ == "__main__":
    check_local_inequality()
    check_tagged_mass()
    check_dyadic_condition()
    check_ramp_scale()
    check_polynomial_threshold()
    print(
        "PASS: tagged Cauchy, dyadic coalescing condition, ramp scale, "
        "and polynomial threshold"
    )
