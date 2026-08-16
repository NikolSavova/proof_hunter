#!/usr/bin/env python3
"""Exact verifier for the scalable weighted-C4 counterexample."""


def build_graph(n, t):
    """Return row bitmasks for K_{n,n} with t leaves at every core vertex."""
    q = n * (1 + t)
    rows = []

    # Core rows: all n core columns, followed by their private t leaves.
    core_mask = (1 << n) - 1
    for i in range(n):
        private = ((1 << t) - 1) << (n + i * t)
        rows.append(core_mask | private)

    # There are t row-side leaves at every core column.
    for j in range(n):
        rows.extend([1 << j] * t)

    assert len(rows) == n * (1 + t)
    return rows, q


def mask_degree_sum(mask, degrees):
    total = 0
    while mask:
        low = mask & -mask
        total += degrees[low.bit_length() - 1]
        mask -= low
    return total


def explicit_statistics(rows, q):
    p = len(rows)
    d = [row.bit_count() for row in rows]
    e = [sum((row >> j) & 1 for row in rows) for j in range(q)]
    m = sum(d)

    C = 0
    W = 0
    for i in range(p):
        for k in range(p):
            common = rows[i] & rows[k]
            c = common.bit_count()
            s = mask_degree_sum(common, e)
            C += c * c
            W += d[i] * d[k] * s * s

    return d, e, m, C, W


def explicit_decomposition(rows, q, d, e, m):
    p = len(rows)
    h = [mask_degree_sum(row, e) for row in rows]
    g = [sum(d[i] for i in range(p) if (rows[i] >> j) & 1)
         for j in range(q)]

    # Integer-scaled edge certificates: delta_num[e] = m^2 delta_e.
    Delta = 0
    for i, row in enumerate(rows):
        mask = row
        while mask:
            low = mask & -mask
            j = low.bit_length() - 1
            value = (d[i] * (m * m - h[i] * h[i])
                     + e[j] * (m * m - g[j] * g[j])
                     - m * m + d[i] * d[i] * e[j] * e[j])
            assert value >= 0
            Delta += value
            mask -= low

    # Sum genuine ordered rectangles by ordered row pair.
    genuine = 0
    genuine_count = 0
    for i in range(p):
        for k in range(p):
            if i == k:
                continue
            common = rows[i] & rows[k]
            c = common.bit_count()
            s1 = mask_degree_sum(common, e)
            s2 = 0
            mask = common
            while mask:
                low = mask & -mask
                ej = e[low.bit_length() - 1]
                s2 += ej * ej
                mask -= low
            genuine_count += c * (c - 1)
            genuine += (m * m * c * (c - 1)
                        - d[i] * d[k] * (s1 * s1 - s2))

    return Delta, genuine, genuine_count


def closed_forms(n, t):
    D = n + t
    m = n * (n + 2 * t)
    C = n**4 + 4 * n * n * t + 2 * n * t * t
    W = n * D * D * (n**3 * D * D + 4 * n * t * D + 2 * t * t)
    return m, C, W


def verify_explicit(n, t):
    rows, q = build_graph(n, t)
    d, e, m, C, W = explicit_statistics(rows, q)
    assert (m, C, W) == closed_forms(n, t)

    Delta, genuine, genuine_count = explicit_decomposition(rows, q, d, e, m)
    assert m * m * C - W == Delta + genuine
    assert genuine_count == n * n * (n - 1) * (n - 1)
    assert genuine == genuine_count * (m * m - (n + t)**4)
    return m, C, W, Delta, genuine


def main():
    # Independent adjacency-matrix checks over a parameter grid.
    for n in range(1, 8):
        for t in range(0, 10):
            verify_explicit(n, t)

    # A compact concrete witness.
    m, C, W, Delta, genuine = verify_explicit(7, 8)
    assert (m, C, W) == (161, 4865, 127044225)
    assert m * m * C - W == -938560

    # The scalable family t=n^2, checked both explicitly at n=7 and by
    # exact closed forms for a range of n.
    n = 7
    m, C, W, Delta, genuine = verify_explicit(n, n * n)
    P = n**5 - 4*n**4 - 18*n**3 - 4*n**2 + 12*n + 6
    assert P == 923
    assert m == n*n*(2*n + 1)
    assert C == n**4*(2*n + 5)
    assert W == n**7*(n + 1)**2*(n**3 + 2*n**2 + 5*n + 6)
    assert m*m*C - W == -n**7*P < 0
    assert genuine == -n**8*(n - 1)**2*(n*n + 4*n + 2)
    assert Delta == n**7*(6*n**4 + 13*n**3 + 4*n**2 - 10*n - 6)

    for n in range(7, 101):
        m, C, W = closed_forms(n, n*n)
        P = n**5 - 4*n**4 - 18*n**3 - 4*n**2 + 12*n + 6
        assert P > 0
        assert m*m*C - W == -n**7*P < 0

    print("PASS: exact G_{n,t} counts and signed decomposition")
    print("PASS: G_{7,8} has W-m^2 C = 938560")
    print("PASS: G_{n,n^2} violates the inequality for every 7 <= n <= 100")
    print("      and its exact ratio is asymptotic to n/8")


if __name__ == "__main__":
    main()
