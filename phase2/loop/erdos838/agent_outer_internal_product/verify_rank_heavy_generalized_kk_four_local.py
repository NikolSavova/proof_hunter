#!/usr/bin/env python3
"""Exact/finite checks for RANK_HEAVY_GENERALIZED_KK_AND_FOUR_LOCAL_BARRIER."""

from fractions import Fraction
from itertools import combinations
from math import comb, log2


def module_counts(t: int, q: int, D: int):
    R = t * q * D
    low = sum(comb(R, r) for r in range(4))
    low_inc = sum(r * comb(R, r) for r in range(4))
    local_low = sum(comb(q, r) * D**r for r in range(4))
    local_low_inc = sum(r * comb(q, r) * D**r for r in range(4))
    P = (D + 1) ** q - local_low
    P_inc = q * D * (D + 1) ** (q - 1) - local_low_inc
    Z = low + t * P
    I = low_inc + t * P_inc

    # Delete one fixed vertex in one fixed role of one module.
    low_del = sum(comb(R - 1, r) for r in range(4))
    affected_total = D * (D + 1) ** (q - 1)
    affected_low = 0
    for r in range(4):
        no_fixed_role = comb(q - 1, r) * D**r
        uses_fixed_role = 0 if r == 0 else (D - 1) * comb(q - 1, r - 1) * D ** (r - 1)
        affected_low += no_fixed_role + uses_fixed_role
    P_del = affected_total - affected_low
    Z_del = low_del + (t - 1) * P + P_del
    return R, Z, I, Z_del


def exact_count_and_deletion_check():
    for t in range(1, 7):
        for q in range(4, 9):
            for D in range(1, 6):
                R, Z, I, Z_del = module_counts(t, q, D)
                assert R * Z_del == R * Z - I
                assert Fraction(Z_del, Z) == 1 - Fraction(I, R * Z)


def brute_four_local_check():
    # q=4 is the smallest nontrivial instance with faces above rank three.
    t, q, D = 2, 4, 2
    R = t * q * D
    labels = list(range(R))

    def role(v):
        module_size = q * D
        return v // module_size, (v % module_size) // D

    def good(S):
        if len(S) <= 3:
            return True
        mr = [role(v) for v in S]
        mods = {m for m, _ in mr}
        if len(mods) != 1:
            return False
        roles = [r for _, r in mr]
        return len(set(roles)) == len(roles)

    good_masks = []
    for mask in range(1 << R):
        S = tuple(v for v in labels if mask & (1 << v))
        g = good(S)
        good_masks.append(g)
        if g:
            for v in S:
                assert good(tuple(x for x in S if x != v))
        if len(S) >= 4:
            all4 = all(good(T) for T in combinations(S, 4))
            assert g == all4

    R0, Z, _, _ = module_counts(t, q, D)
    assert R0 == R
    assert sum(good_masks) == Z

    # Two-cloud all-delete terminal: each cloud is one q=4,D=1 module.
    # A full rank-four face in cloud 1 is good, but adjoining any nonempty
    # trace from cloud 0 is cross-cloud bad.
    cloud0 = set(range(4))
    cloud1 = set(range(4, 8))

    def two_cloud_good(S):
        S = set(S)
        return len(S) <= 3 or S <= cloud0 or S <= cloud1

    assert two_cloud_good(cloud1)
    for r in range(1, 5):
        for A in combinations(cloud0, r):
            assert not two_cloud_good(set(A) | cloud1)


def constants_and_uniform_shadow_check():
    a = log2(3.0)
    theta = 2.0 - a
    kappa = 1.0 / a
    assert abs(a - 1.584962500721156) < 1e-14
    assert abs(theta - 0.415037499278844) < 1e-14
    assert abs(kappa - 0.6309297535714574) < 1e-14

    # Check the explicit bracket from (11).  The theorem is asymptotic;
    # d>=4096 is deliberately conservative for C<=20 and eta=0.05.
    C = 20.0
    eta = 0.05
    k0 = kappa - eta
    for d in (4096, 8192, 16384, 32768):
        # Beyond y=d the logarithmic term is monotone increasing, so a few
        # polynomially larger samples cover the second asymptotic range
        # without converting 2**d to a float.
        ys = [kappa, 1.0, 2.0, 4.0, 8.0, d / log2(d), d / 4, d / 2, d, 4 * d, d * d]
        for y in ys:
            if y < kappa:
                continue
            bracket = d / (2 * y) - C * log2(d) / y + log2(y / k0) - log2(2.718281828459045) - 2 / y
            assert bracket >= log2(d) / 5


def asymptotic_sequence_check():
    # Integer sequence illustrating log Z = d^2/2-C*d*log d+O(d)
    # and mean/q -> 1.  C=1, kappa=0.9 keeps q above kappa_* d.
    C = 1.0
    kappa = 0.9
    c = 1.0 / (2.0 * kappa)
    for m in (80, 120, 180, 260):
        D = 2 ** round(c * m)
        q = max(4, round(kappa * m - 2 * kappa * C * log2(m)))
        t = max(1, (2**m) // (q * D))
        R, Z, I, _ = module_counts(t, q, D)
        d = log2(R)
        phi = d * d / 2 - C * d * log2(d)
        scaled_error = abs(log2(Z) - phi) / d
        mu = I / Z
        assert q > (1 / log2(3)) * d
        assert abs(mu - q) < 1e-6
        # Integer rounding changes q by one, hence log Z by Theta(d); the
        # theorem claims an O(d), not a convergent normalized, error.
        assert scaled_error < 2.0


if __name__ == "__main__":
    exact_count_and_deletion_check()
    brute_four_local_check()
    constants_and_uniform_shadow_check()
    asymptotic_sequence_check()
    print("PASS: generalized-KK constants, exact deletion, four-locality, and asymptotics")
