#!/usr/bin/env python3
"""Exact counterexample to the weak Ky--Fan strengthening."""

from fractions import Fraction


def counts(rows, q):
    p = len(rows)
    d = [r.bit_count() for r in rows]
    e = [sum((rows[i] >> j) & 1 for i in range(p)) for j in range(q)]
    m = sum(d)
    C = W = 0
    for i in range(p):
        for k in range(p):
            common = rows[i] & rows[k]
            c = common.bit_count()
            s = sum(e[j] for j in range(q) if (common >> j) & 1)
            C += c * c
            W += d[i] * d[k] * s * s
    return m, C, W


def double_star(n):
    rows = [1 << (n - 1) for _ in range(n - 1)]
    rows.append((1 << n) - 1)
    return rows


def main():
    n = 7
    r = n - 1
    m, C, W = counts(double_star(n), n)
    assert (m, C, W) == (13, 97, 14161)
    assert m * m * C == 16393
    assert W < m * m * C

    # A_7: lambda_+=(1+sqrt(1+4r))/2=3.
    assert 1 + 4 * r == 25
    lambda_plus = 3
    rhs = m * lambda_plus * lambda_plus
    assert rhs == 117

    # T_7: mu_+=(7+sqrt(217))/2.  The first-prefix inequality fails
    # iff 7*sqrt(217)>101, verified by positive integer squaring.
    discriminant = n * n + 4 * n * r
    assert discriminant == 217
    assert 49 * discriminant > 101 * 101

    ratio = Fraction(W, m * m * C)
    assert ratio == Fraction(14161, 16393)
    print("PASS: exact 7x7 double-star counterexample to Ky-Fan k=1")
    print("      s1(T)^2=(133+7*sqrt(217))/2 > 117=13*s1(A)^2")
    print("PASS: original W<=m^2 C survives with ratio", ratio)


if __name__ == "__main__":
    main()
