#!/usr/bin/env python3
"""Exact checks for FINITE_GAP_STRONG_COMB_RAMP_BARRIER.md."""

from itertools import product
from math import ceil, comb, log2


def ramp(h, q):
    assert h >= 2 and q >= 2
    if q <= h:
        return (1,) + tuple(range(1, q))
    p = q - h + 2
    return (1,) * p + tuple(range(2, h))


def pair_safe_ramp(h, q):
    assert h >= 4 and 2 <= q <= h - 2
    return (2,) + tuple(range(2, q + 1))


def exponent_terms(h, q, x):
    assert len(x) == q
    assert all(1 <= z <= h - 1 for z in x)
    terms = [h, q]
    terms.extend(h - x[j] + j for j in range(q))
    terms.extend(x[i] + q - i - 1 for i in range(q))
    terms.extend(
        h + x[i] - x[j] + j - i - 1
        for i in range(q)
        for j in range(i + 1, q)
    )
    return terms


def envelope(h, q, x):
    return max(exponent_terms(h, q, x))


def recurrence(R, h, q, x):
    # Equation (13), including the two local singleton guard faces.
    ans = 2 + q * R**h + R**q
    ans += sum(R ** (h - x[j] + j) for j in range(q))
    ans += sum(R ** (x[i] + q - i - 1) for i in range(q))
    ans += sum(
        R ** (h + x[i] - x[j] + j - i - 1)
        for i in range(q)
        for j in range(i + 1, q)
    )
    return ans


def defect(x):
    return max(
        0,
        max(
            (j - i) - (x[j] - x[i])
            for i in range(len(x))
            for j in range(i + 1, len(x))
        ),
    )


def check_minimax():
    # Exhaustive small audit, including both q <= h and q > h.
    for h in range(2, 8):
        for q in range(2, 8):
            best = min(
                envelope(h, q, x)
                for x in product(range(1, h), repeat=q)
            )
            assert best == max(h, q), (h, q, best)
            xr = ramp(h, q)
            assert len(xr) == q
            assert envelope(h, q, xr) == max(h, q)

    # The geometric cap/cup profiles contain every pair, so their baseline
    # exponent is two.  The shifted live-range ramp still has value h.
    for h in range(4, 10):
        for q in range(2, h - 1):
            xr = pair_safe_ramp(h, q)
            assert all(2 <= z <= h - 2 for z in xr)
            assert envelope(h, q, xr) == h
            if h <= 7:
                best = min(
                    envelope(h, q, x)
                    for x in product(range(2, h - 1), repeat=q)
                )
                assert best == h


def check_exact_recurrence():
    for R in (2, 3, 5, 11):
        for h in range(2, 9):
            for q in range(2, 10):
                x = ramp(h, q)
                E = max(h, q)
                value = recurrence(R, h, q, x)
                assert R**E <= value
                assert value <= (q + 3) ** 2 * R**E
                # Every scalar child obeys all baseline constraints (3).
                D = R - 1
                for z in x:
                    C, U, W = R**z, R ** (h - z), R**h
                    assert C >= D and U >= D
                    assert C <= W and U <= W and C * U == W

                if q <= h - 2:
                    xp = pair_safe_ramp(h, q)
                    value_p = recurrence(R, h, q, xp)
                    assert R**h <= value_p <= (q + 3) ** 2 * R**h
                    K2 = 1 + D + comb(D, 2)
                    for z in xp:
                        C, U, W = R**z, R ** (h - z), R**h
                        assert C >= K2 and U >= K2
                        assert C <= W and U <= W and C * U == W


def check_defect_and_menu():
    for h in range(2, 7):
        for q in range(2, 7):
            for x in product(range(1, h), repeat=q):
                Delta = defect(x)
                raw_delta = max(
                    (j - i) - (x[j] - x[i])
                    for i in range(q)
                    for j in range(i + 1, q)
                )
                internal_max = max(
                    h + x[i] - x[j] + j - i - 1
                    for i in range(q)
                    for j in range(i + 1, q)
                )
                assert internal_max == h + raw_delta - 1
                K = len(set(x))
                assert Delta >= ceil(q / K) - 1
                assert max(h, internal_max) >= h + ceil(q / K) - 2


def check_rank_two_and_scale():
    for m in range(1, 100):
        K2 = 1 + m + comb(m, 2)
        assert K2 <= (m + 1) ** 2

    for d in (64, 96, 128, 192, 256):
        D = 2**d
        R = D + 1
        q = d // 4
        h = d // 2
        E = max(h, q)
        recurrence_log_upper = E * log2(R) + 2 * log2(q + 3)
        parent_log = log2((q + 2) * D)
        half_target = 0.5 * parent_log * parent_log
        missing = half_target - recurrence_log_upper
        assert missing > 0.8 * d * log2(q)
        # Even two rank-two cloud factors of size at most D leave a
        # Theta(d log q) deficit.
        if d >= 192:
            assert missing - 4 * d > 0.25 * d * log2(q)


if __name__ == "__main__":
    check_minimax()
    check_exact_recurrence()
    check_defect_and_menu()
    check_rank_two_and_scale()
    print(
        "PASS: strong-comb minimax, profile defect/menu bound, "
        "and half-scale loss"
    )
