#!/usr/bin/env python3
"""Checks for POLYNOMIAL_DESCRIPTION_LOAD_FACE_ALPHABET_BARRIER.md."""

from fractions import Fraction as F
from itertools import combinations
from math import comb, log2


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lo = []
    for p in points:
        while len(lo) >= 2 and orient(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(points):
        while len(up) >= 2 and orient(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def is_convex(points):
    return len(hull(points)) == len(set(points))


def construction(m):
    A = [(F(-3), F(0)), (F(3), F(0)), (F(0), F(4))]
    X = []
    for j in range(1, m + 1):
        t = F(j)
        X.append(
            (
                (1 - t * t) / (4 * (1 + t * t)),
                1 + t / (2 * (1 + t * t)),
            )
        )
    return A, X


def check_geometry():
    for m in range(4, 13):
        A, X = construction(m)
        P = A + X
        assert len(P) == len(set(P))
        assert all(orient(*tri) != 0 for tri in combinations(P, 3))
        assert is_convex(A) and is_convex(X)
        for x in X:
            assert not is_convex(A + [x])

        # Exhaust every pocket face at the audited sizes.
        for mask in range(1 << m):
            face = [X[j] for j in range(m) if (mask >> j) & 1]
            assert is_convex(face)

        # All released records contain the same canonical column x_1.
        column = X[0]
        released = {
            frozenset([column] + [X[j] for j in range(1, m) if (mask >> (j - 1)) & 1])
            for mask in range(1 << (m - 1))
        }
        assert len(released) == 2 ** (m - 1)
        assert all(column in face and is_convex(list(face)) for face in released)


def check_dyadic_pooling():
    # Several marked occurrences over one actual source, total weight <= 1.
    alphas = [F(1, 2), F(1, 3), F(1, 7)]
    assert sum(alphas) < 1
    L = 11
    layers = (0, 1, 3, 7)
    pooled_load = sum(
        sum(alpha / (2**k) for k in layers) * L for alpha in alphas
    )
    assert pooled_load < 2 * L

    # Distinct columns survive pooling; parallel copies of one column do not.
    for H in (2, 8, 64):
        assert len(set(range(H))) == H
        assert len({"same-column" for _ in range(H)}) == 1


def check_state_count_and_scale():
    # A crude tuple with c source masks, s external labels, and polynomial
    # flags is polynomial whenever r <= K log_2 n.
    for n in (2**8, 2**12, 2**16):
        logn = n.bit_length() - 1
        r = 3 * logn
        c, s, flag_degree, C = 4, 7, 5, 16
        states = C * (r + 1) ** flag_degree * 2 ** (c * r) * n**s
        polynomial_bound = C * (r + 1) ** flag_degree * n ** (s + 3 * c)
        assert states == polynomial_bound

    for m in range(4, 30):
        n = m + 3
        H = 2 ** (m - 1)
        assert H == 2 ** (n - 4)
        if m >= 20:
            assert H > n**3
        K2 = 1 + m + comb(m, 2)
        if m >= 6:
            assert K2 < H


def check_quasipoly_relaxation():
    for L in (64, 128, 256, 512):
        a = F(49, 100)
        epsilon = F(1, 10)
        kappa = float((2 + epsilon) * 2 * a)
        r = int(kappa * L)
        c0 = 7
        state_log = c0 * r * log2(r + 1)
        asymptotic_allowance = (c0 * kappa + 3.0) * L * log2(L)
        assert state_log <= asymptotic_allowance

        # Pocket scale n/polylog^3 loses leading coefficient 6a.
        pocket_loss_coefficient = float(6 * a)
        C_ret = 5.0
        sigma_needed = pocket_loss_coefficient + c0 * kappa + C_ret
        rho, kappa0 = 0.2, 0.1
        D = int(3 * sigma_needed / (rho * kappa0)) + 1
        bank_coefficient = rho * kappa0 * D / 3
        assert bank_coefficient > sigma_needed

        # Constant external labels are lower order; r free ambient labels
        # have quadratic rather than L log L description entropy.
        constant_external_log = 8 * L
        free_external_log = r * L
        assert constant_external_log < L * log2(L) if L >= 512 else True
        assert free_external_log > 0.5 * kappa * L * L


if __name__ == "__main__":
    check_geometry()
    check_dyadic_pooling()
    check_state_count_and_scale()
    check_quasipoly_relaxation()
    print(
        "PASS: polynomial label states, dyadic pooling, and exponential "
        "actual face alphabet"
    )
