#!/usr/bin/env python3
"""Exact finite audit for C4_DEGREE_REGULARIZATION.md.

Exhausts all nonempty bipartite graphs through 3x3.  It checks the
degree-product information identity, the good-edge mass inequality, the
dyadic-bin size/product bounds, and the Cauchy--Schwarz C4 lower bound.
"""

from fractions import Fraction
from math import floor, log2, sqrt


def audit(nl: int, nr: int, mask: int) -> None:
    edges = [(i, j) for i in range(nl) for j in range(nr)
             if (mask >> (i * nr + j)) & 1]
    m = len(edges)
    dl = [0] * nl
    dr = [0] * nr
    for i, j in edges:
        dl[i] += 1
        dr[j] += 1

    # The exact product form of (1): 2^(mJ)=prod_e m/(d_x d_y).
    lhs_num = m ** m
    lhs_den = 1
    for i, j in edges:
        lhs_den *= dl[i] * dr[j]
    assert lhs_num > 0 and lhs_den > 0

    M = log2(m)
    J = log2(Fraction(lhs_num, lhs_den)) / m
    assert J >= -1e-12
    a = J + sqrt((J + 1.0) * M) if M else 0.0
    good = [(i, j) for i, j in edges
            if log2(m / (dl[i] * dr[j])) <= a + 1e-12]
    delta = len(good) / m
    if M:
        assert delta + 1e-12 >= (a - J) / (a + M)

    bins = {}
    for i, j in good:
        key = (floor(log2(dl[i])), floor(log2(dr[j])))
        bins.setdefault(key, []).append((i, j))
    assert bins
    chosen = max(bins.values(), key=len)
    assert len(chosen) * (floor(M) + 1) ** 2 >= len(good)

    left = sorted({i for i, _ in chosen})
    right = sorted({j for _, j in chosen})
    dmin = min(dl[i] for i in left)
    emin = min(dr[j] for j in right)
    assert len(left) * dmin <= m
    assert len(right) * emin <= m
    if M:
        assert dmin * emin + 1e-12 >= m * 2 ** (-a - 2)

    chosen_set = set(chosen)
    c4 = 0
    for i in left:
        for k in left:
            codeg = sum((i, j) in chosen_set and (k, j) in chosen_set
                         for j in right)
            c4 += codeg * codeg
    lower = Fraction(len(chosen) ** 4, len(left) ** 2 * len(right) ** 2)
    assert c4 >= lower


def main() -> None:
    checked = 0
    for nl in range(1, 4):
        for nr in range(1, 4):
            for mask in range(1, 1 << (nl * nr)):
                audit(nl, nr, mask)
                checked += 1
    print(f"PASS: {checked} nonempty bipartite graphs")


if __name__ == "__main__":
    main()
