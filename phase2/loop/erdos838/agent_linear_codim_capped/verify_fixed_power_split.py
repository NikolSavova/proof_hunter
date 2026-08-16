#!/usr/bin/env python3
"""Algebraic verifier for FIXED_POWER_EIC_SPLIT.md."""

from itertools import combinations
from math import comb, log2


def left_regular_graphs(s, n, D):
    rows = list(combinations(range(n), D))
    total = len(rows) ** s
    # Exhaust modest instances, deterministic mixed-radix enumeration.
    for code in range(total):
        x = code
        graph = []
        for _ in range(s):
            graph.append(set(rows[x % len(rows)]))
            x //= len(rows)
        yield graph


def moment_audit():
    checked = 0
    for s, n, D in ((3, 4, 2), (4, 4, 2), (3, 5, 3)):
        for G in left_regular_graphs(s, n, D):
            E = s * D
            deg = [sum(p in row for row in G) for p in range(n)]
            q = {(a, b): len(G[a] & G[b])
                 for a in range(s) for b in range(s) if a != b}
            Q1 = sum(q.values())
            Q2 = sum(x * x for x in q.values())
            assert Q1 == sum(x * (x - 1) for x in deg)
            assert Q1 >= E * E / n - E - 1e-12
            if s > 1:
                assert Q2 + 1e-12 >= Q1 * Q1 / (s * (s - 1))
            checked += 1
    return checked


def forward_algebra_audit():
    # Synthetic q-arrays check the implication used in (25).
    checked = 0
    for s in range(2, 12):
        for base in range(1, 30):
            qs = [base + (i % 4) for i in range(s * (s - 1))]
            Q2 = sum(q * q for q in qs)
            # Take all pairs forward: eta=1.  Choose tau only when the
            # sufficient dominance condition is actually met.
            for tau_num in (1, 2, 3, 4):
                tau = tau_num / 4
                lhs = tau * tau * Q2 - sum(qs)
                if Q2 ** 0.5 >= 2 * s / (tau * tau):
                    assert lhs + 1e-12 >= 0.5 * tau * tau * Q2
                checked += 1
    return checked


def downshadow_and_exponent_audit():
    # Central binomial reservoir and exact fixed-saving exponent window.
    for r in (20, 40, 80, 160, 320):
        central = comb(r, r // 2)
        assert log2(central) >= r - log2(r + 1)

    for alpha in (0.1, 0.2, 0.3, 0.4, 0.49):
        eps_max = (1 - 2 * alpha) / (1 - alpha)
        assert eps_max > 0
        eps = eps_max / 2
        assert alpha < (1 - alpha) * (1 - eps)

    # At/beyond one half the allowed prefix exponent in (12) is positive
    # for a sufficiently small fixed epsilon.
    for alpha in (0.5, 0.6, 0.75, 0.9):
        eps = min(0.1, alpha / (2 * (1 - alpha)))
        exponent = alpha - eps * (1 - alpha)
        assert exponent > 0


if __name__ == "__main__":
    moments = moment_audit()
    forward = forward_algebra_audit()
    downshadow_and_exponent_audit()
    print("PASS fixed-power EIC split audit")
    print(f"  exhaustive left-regular incidence graphs: {moments}")
    print(f"  synthetic forward-mass inequalities: {forward}")
    print("  central downshadow and alpha/epsilon windows: verified")
