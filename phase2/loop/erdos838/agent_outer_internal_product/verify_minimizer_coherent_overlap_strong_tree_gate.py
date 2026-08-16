#!/usr/bin/env python3
"""Exact arithmetic checks for MINIMIZER_COHERENT_OVERLAP_STRONG_TREE_GATE."""

from fractions import Fraction
from math import comb, log2, sqrt


def add(a, b):
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def scale(a, c):
    return [c * x for x in a]


def shift_scaled_template(coefficients, n):
    """Return sum_j coefficients[j] (n z)^j."""
    return [value * n**j for j, value in enumerate(coefficients)]


def six_point_graded_audit(depth=14):
    # Q_0 is a singleton.  The balanced T(4,2) seed has
    # G_C=6+15x+10x^2 and G_V=15+20x+9x^2.
    cap = [0, 1]
    face = [0, 1]
    rows = []
    for d in range(1, depth + 1):
        n = 6 ** (d - 1)
        old_cap = cap
        old_face = face
        cap = mul(old_cap, shift_scaled_template([6, 15, 10], n))
        face = add(scale(old_face, 6),
                   mul(mul(old_cap, old_cap),
                       shift_scaled_template([15, 20, 9], n)))

        assert len(cap) - 1 == 2 * d + 1
        assert len(face) - 1 == 4 * d
        total = sum(face)
        top = face[-1]
        assert top > 1
        assert total < 40 * top

        q = 4 * d
        middle = sum(comb(q, t) for t in range((q + 2) // 3,
                                               (2 * q) // 3 + 1))
        # Incidence averaging plus V/top < 40.
        average_lower = Fraction(top * middle, total)
        assert average_lower > Fraction(middle, 40)
        # Distinct top-rank carriers have union rank at least q+1, while
        # len(face)-1=q is the exact ambient maximum face rank.  Thus a
        # terminal convex-union leaf contains at most one carrier, and the
        # same incidence lower bound applies to terminal Boolean-bank load.
        rows.append((d, q, total, top, float(total / top), middle))
    return rows


def balanced_coefficients():
    rows = []
    previous = None
    for k in [4, 8, 16, 32, 64, 128, 256, 512]:
        r = comb(2 * k - 4, k - 2)
        value = (k - 2) / log2(r)
        assert value > 0.5
        if previous is not None:
            assert value < previous
        previous = value
        rows.append((k, r, value))
    assert rows[-1][2] < 0.505
    return rows


def fixed_gap_thresholds():
    rows = []
    for delta in [0.01, 0.05, 0.10, 0.20]:
        epsilon = delta / 10
        alpha = sqrt(1 - 2 * delta) + epsilon
        surplus = 0.5 * alpha * alpha - (0.5 - delta)
        expected = epsilon * sqrt(1 - 2 * delta) + epsilon * epsilon / 2
        assert abs(surplus - expected) < 1e-14
        assert surplus > 0
        rows.append((delta, alpha, surplus))
    return rows


def main():
    graded = six_point_graded_audit()
    balanced = balanced_coefficients()
    thresholds = fixed_gap_thresholds()
    print("PASS: coherent overlap strong-tree gate")
    print("  six-point last row:", graded[-1])
    print("  balanced rho rows:", [(k, round(rho, 9))
                                    for k, _r, rho in balanced])
    print("  fixed-gap thresholds:", [(d, round(a, 6), round(s, 8))
                                       for d, a, s in thresholds])


if __name__ == "__main__":
    main()
