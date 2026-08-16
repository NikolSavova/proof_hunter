#!/usr/bin/env python3
"""Checks for NEAR_AMBIENT_LIVE_CONTEXT_COEFFICIENT_AUDIT."""

from fractions import Fraction
from math import log2


def weighted_context_identity():
    # Exact rational source weights grouped by geometric projection.
    fibres = {
        "s0": [Fraction(1, 7), Fraction(2, 7)],
        "s1": [Fraction(3, 11)],
        "s2": [Fraction(1, 13), Fraction(2, 13), Fraction(3, 13)],
    }
    mass = sum((sum(v) for v in fibres.values()), Fraction(0))
    load = max(sum(v) for v in fibres.values())
    source_weights = [x for values in fibres.values() for x in values]
    source_cap = max(source_weights)
    assert len(source_weights) * source_cap >= mass
    assert mass <= len(fibres) * load
    # Equality calibration.
    equal = {i: [Fraction(5, 17)] for i in range(9)}
    equal_mass = sum((sum(v) for v in equal.values()), Fraction(0))
    equal_load = max(sum(v) for v in equal.values())
    assert equal_mass == len(equal) * equal_load
    return mass, load


def phi(L, correction=3.0):
    return L * L / 2.0 - correction * L * log2(L)


def asymptotic_audit():
    checked = 0
    for power in range(13, 22, 2):
        L = float(2**power)
        L2 = log2(L)
        L3 = log2(L2)
        a = L3
        target = phi(L)
        child = phi(L - a)
        delta = target - child
        assert delta > 0
        assert delta < 2 * L * L3

        # A live mass can lose an arbitrary fixed O(L L2) normalization.
        norm = 9.0 * L * L2
        live_log = child - norm
        sparse_context_log = 5.0 * L * L3
        assert live_log > sparse_context_log + norm

        # If projection load is quasipolynomial, the context family itself
        # has coefficient one half; if contexts are sparse, the load does.
        low_load = norm
        context_lower = live_log - low_load
        assert context_lower > sparse_context_log
        high_load_lower = live_log - sparse_context_log
        assert high_load_lower > norm

        # Complete balanced role products contradict alpha>c.
        r = delta / 2.0
        log_v = target - r
        c = log_v / (L * L)
        eps = 0.03
        alpha = c + eps
        s = alpha * L
        log_p0 = s * (L - log2(s))
        assert log_p0 - log_v > eps * L * L / 2.0

        # The active O(L3)-role trace stays sparse and therefore falls into
        # the high projection-load alternative.
        active_trace_log = 5.0 * L * L3
        assert active_trace_log < live_log
        checked += 1
    return checked


def residual_ledger():
    # Work with exact rational logarithmic units: Phi=10000, Delta=600.
    Phi = Fraction(10000)
    Delta = Fraction(600)
    checked = 0
    for numerator in range(0, 13):
        r = Delta * Fraction(numerator, 12)
        source = Phi - r
        child = Phi - Delta
        directional = Phi - (r + Delta) / 2
        pair_records = 2 * Phi - r - Delta
        assert child <= source
        assert directional <= source
        assert pair_records <= 2 * source
        # The gaps are exact.
        assert source - directional == (Delta - r) / 2
        assert 2 * source - pair_records == Delta - r
        checked += 1
    return checked


if __name__ == "__main__":
    mass, load = weighted_context_identity()
    scales = asymptotic_audit()
    ledger = residual_ledger()
    print(
        "PASS: exact projection grouping mass=%s load=%s; scales=%d; "
        "residual-ledger=%d" % (mass, load, scales, ledger)
    )
