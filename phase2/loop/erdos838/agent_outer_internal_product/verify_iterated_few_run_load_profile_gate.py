#!/usr/bin/env python3
"""Checks for ITERATED_FEW_RUN_LOAD_PROFILE_GATE."""

from fractions import Fraction
from itertools import combinations
from math import log2


def boundaries(mask, q):
    return {
        (i, (i + 1) % q)
        for i in range(q)
        if ((mask >> i) & 1) != ((mask >> ((i + 1) % q)) & 1)
    }


def components(mask, q):
    if mask == 0:
        return []
    if mask == (1 << q) - 1:
        return [q]
    starts = [
        i
        for i in range(q)
        if (mask >> i) & 1 and not ((mask >> ((i - 1) % q)) & 1)
    ]
    lengths = []
    for start in starts:
        length = 0
        while (mask >> ((start + length) % q)) & 1:
            length += 1
        lengths.append(length)
    return lengths


def mask_coalescence():
    chains = 0
    for q in range(4, 11):
        for final in range(1 << q):
            if final in (0, (1 << q) - 1):
                continue
            bits = [i for i in range(q) if final >> i & 1]
            orders = [bits, list(reversed(bits))]
            if len(bits) >= 3:
                orders.append(bits[::2] + bits[1::2])
            for order in orders:
                current = 0
                history = []
                for bit in order:
                    current |= 1 << bit
                    history.append(current)
                assert current == final
                terminal_boundary = boundaries(final, q)
                for earlier in history:
                    for edge in boundaries(earlier, q):
                        a, b = edge
                        inside = a if earlier >> a & 1 else b
                        outside = b if inside == a else a
                        if not (final >> outside & 1):
                            assert edge in terminal_boundary
                lengths = components(final, q)
                assert len(terminal_boundary) == 2 * len(lengths)
                assert max(lengths) * len(lengths) >= final.bit_count()
                chains += 1
    return chains


def projection_telescope():
    mass = Fraction(17, 5)
    context_counts = [3, 5, 2, 7]
    current = mass
    for count in context_counts:
        current /= count
    product_count = 1
    for count in context_counts:
        product_count *= count
    assert current == mass / product_count
    stationary = mass
    for _ in range(12):
        stationary /= 1
    assert stationary == mass
    return current


def phi(L, correction=2.0):
    return L * L / 2.0 - correction * L * log2(L)


def target_and_ambient_ledger():
    checked = 0
    for power in range(13, 20):
        L0 = float(2**power)
        levels = [L0]
        for _ in range(4):
            level = levels[-1]
            levels.append(level - log2(log2(level)))
        deltas = [phi(levels[i]) - phi(levels[i + 1]) for i in range(4)]
        total = sum(deltas)
        assert abs(total - (phi(levels[0]) - phi(levels[-1]))) < 1e-6 * total
        for fraction in (0.0, 0.25, 0.5, 0.75, 1.0):
            r = fraction * total
            source_log = phi(L0) - r
            child_log = phi(levels[-1])
            directional = (source_log + child_log) / 2.0
            assert directional <= source_log + 1e-8
            assert abs(
                directional - (phi(L0) - (r + total) / 2.0)
            ) < 1e-6 * total
            checked += 1
    return checked


def formal_ramps():
    checked = 0
    for q in (4, 6, 8, 10, 12):
        h = 4 * q
        assert (h - q) % 2 == 0
        b = (h - q) // 2
        for d in (8, 10, 12):
            D = 1 << d
            H = D**h
            caps = [D ** (b + i) for i in range(q)]
            cups = [D ** (h - b - i) for i in range(q)]
            assert all(caps[i] * cups[i] == H for i in range(q))
            assert len({(b + i) - i for i in range(q)}) == 1
            monomial_cross = 0
            exact_cross = 0
            for i, j in combinations(range(q), 2):
                term = caps[i] * cups[j] * D ** (j - i - 1)
                assert term == H // D
                monomial_cross += term
                exact_cross += caps[i] * cups[j] * (1 + D) ** (j - i - 1)
            recurrence = q * H + exact_cross
            assert exact_cross <= 2 * monomial_cross
            assert recurrence <= 2 * q * H
            checked += 1
    return checked


def macro_scale_gap():
    checked = 0
    for power in range(14, 21):
        L = float(2**power)
        L2 = log2(L)
        q = L2
        ell = log2(q)
        d = L - ell
        gap = phi(d + ell) - phi(d) - log2(2 * q)
        assert gap > 0.9 * L * ell
        assert gap < 1.1 * L * ell
        h = phi(d) / d
        assert h > 3 * q
        checked += 1
    return checked


if __name__ == "__main__":
    chains = mask_coalescence()
    terminal_mass = projection_telescope()
    ledger = target_and_ambient_ledger()
    ramps = formal_ramps()
    scale_gaps = macro_scale_gap()
    print(
        "PASS: mask chains=%d; projection terminal=%s; ledgers=%d; "
        "ramps=%d; macro-gaps=%d"
        % (chains, terminal_mass, ledger, ramps, scale_gaps)
    )
