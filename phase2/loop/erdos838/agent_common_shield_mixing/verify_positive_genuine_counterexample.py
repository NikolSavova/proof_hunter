#!/usr/bin/env python3
"""Exact counterexample to positive-part genuine rectangle charging."""


def main():
    A = [0b1111, 0b1111, 0b1111, 0b0001]
    p = q = 4
    d = [row.bit_count() for row in A]
    e = [sum((A[i] >> j) & 1 for i in range(p)) for j in range(q)]
    m = sum(d)
    edges = [(i, j) for i in range(p) for j in range(q)
             if (A[i] >> j) & 1]
    assert m == 13
    assert d == [4, 4, 4, 1]
    assert e == [4, 3, 3, 3]

    h = [sum(e[j] for j in range(q) if (A[i] >> j) & 1)
         for i in range(p)]
    g = [sum(d[i] for i in range(p) if (A[i] >> j) & 1)
         for j in range(q)]
    assert h == [13, 13, 13, 4]
    assert g == [13, 12, 12, 12]

    delta_num = {}
    for i, j in edges:
        delta_num[i, j] = (d[i] * (m * m - h[i] * h[i])
                           + e[j] * (m * m - g[j] * g[j])
                           - m * m + d[i] * d[i] * e[j] * e[j])
        assert delta_num[i, j] >= 0
    assert [delta_num[i, 0] for i in range(3)] == [87, 87, 87]
    assert all(delta_num[i, j] == 50
               for i in range(3) for j in range(1, 4))
    assert delta_num[3, 0] == 0
    assert sum(delta_num.values()) == 711

    C = W = positive_excess = helpful_deficit = genuine_count = 0
    for i, j in edges:
        for k, l in edges:
            if ((A[i] >> l) & 1) and ((A[k] >> j) & 1):
                C += 1
                product_num = d[i] * e[j] * d[k] * e[l]
                W += product_num
                if i != k and j != l:
                    genuine_count += 1
                    if product_num > m * m:
                        positive_excess += product_num - m * m
                    else:
                        helpful_deficit += m * m - product_num

    assert genuine_count == 72
    assert positive_excess == 828
    assert helpful_deficit == 900
    assert positive_excess > sum(delta_num.values())

    assert (C, W) == (151, 24736)
    signed_genuine_residual = helpful_deficit - positive_excess
    assert signed_genuine_residual == 72
    assert m * m * C - W == sum(delta_num.values()) + signed_genuine_residual
    assert m * m * C - W == 783

    print("PASS: positive genuine excess 828 exceeds delta budget 711")
    print("PASS: helpful genuine deficit is 900; signed residual is +72")
    print("PASS: original inequality survives with m^2 C-W=783")


if __name__ == "__main__":
    main()

