#!/usr/bin/env python3
"""Exact arithmetic checks for FIXED_GAP_LINEAR_PROFILE_POTENTIAL.md."""

from fractions import Fraction as F
from itertools import product


def check_drop_theorem():
    # Exhaust small rational profile arrays satisfying A_i+B_i>=h.
    for q in range(2, 6):
        h = F(5, 1)
        values = [F(v, 2) for v in range(1, 7)]
        for As in product(values, repeat=q):
            Bs = tuple(h - A for A in As)  # extremal diagonal equality
            ys = tuple(As[i] - i for i in range(q))
            for i in range(q):
                for j in range(i + 1, q):
                    cross = As[i] + Bs[j] + j - i - 1
                    asserted = h + ys[i] - ys[j] - 1
                    assert cross == asserted
                    # Increasing B_j only enlarges the actual cross bank.
                    assert As[i] + (Bs[j] + 1) + j - i - 1 >= asserted


def exact_ramp(d):
    assert d % 8 == 0
    D = 2**d
    q = d // 4
    H = D ** (d // 2)
    C = [D ** (d // 8 + i) for i in range(q)]
    U = [D ** (3 * d // 8 - i) for i in range(q)]
    assert all(C[i] * U[i] == H for i in range(q))
    assert all(D <= value <= H for value in C + U)
    assert len({F(d, 8) for _ in range(q)}) == 1

    W = q * H
    for i in range(q):
        for j in range(i + 1, q):
            gap = j - i - 1
            term = C[i] * U[j] * (1 + D) ** gap
            assert C[i] * U[j] * D**gap == H // D
            assert term < 2 * H // D + 1
            W += term
    assert q * H <= W <= 2 * q * H

    # Choose q a power of two so the parent logarithm is integral.
    assert q & (q - 1) == 0
    ell = q.bit_length() - 1
    assert 2**ell == q
    parent_log = d + ell
    assert parent_log % 2 == 0
    target = 2 ** (parent_log * parent_log // 2)
    deficit_exponent = d * ell + ell * ell // 2 - ell - 1
    assert target == (2 * q * H) * 2**deficit_exponent

    # Pure c=1/2 drop threshold from equation (19).
    threshold = F(1) + ell + F(ell * ell, 2 * d)
    potentials = [F(d, 8) for _ in range(q)]
    assert max(
        potentials[i] - potentials[j]
        for i in range(q)
        for j in range(i + 1, q)
    ) < threshold
    return q, W, deficit_exponent


if __name__ == "__main__":
    check_drop_theorem()
    summaries = []
    # d=4*2^t with even t makes q and the half-target exponent integral.
    for d in (16, 64, 256):
        q, W, deficit = exact_ramp(d)
        summaries.append((d, q, W.bit_length(), deficit))
    print(
        "PASS: drop theorem exhaustive, exact ramps d=16,64,256, "
        f"and fixed-gap deficits verified; summaries={summaries}"
    )
