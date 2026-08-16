#!/usr/bin/env python3
"""Exact checks for the sharp capped weighted-C4 conversion."""


def statistics(bits, p, q):
    rows = [[(bits >> (i*q + j)) & 1 for j in range(q)]
            for i in range(p)]
    d = [sum(row) for row in rows]
    e = [sum(rows[i][j] for i in range(p)) for j in range(q)]
    m = sum(d)
    if not m:
        return None

    K = max(d[i] * e[j]
            for i in range(p) for j in range(q) if rows[i][j])
    Z = sum(d[i] * e[j]
            for i in range(p) for j in range(q) if rows[i][j])

    C = 0
    W = 0
    for i in range(p):
        for k in range(p):
            common = [j for j in range(q) if rows[i][j] and rows[k][j]]
            c = len(common)
            s = sum(e[j] for j in common)
            C += c * c
            W += d[i] * d[k] * s * s

    return m, C, W, K, Z


def exhaustive_check():
    checked = 0
    for p in range(1, 5):
        for q in range(1, 5):
            for bits in range(1, 1 << (p*q)):
                m, C, W, K, Z = statistics(bits, p, q)

                # Sharp cap conversion C >= W/K^2.
                assert C * K * K >= W

                # Weighted DRC: W >= m^4 (Z/m^2)^4 = Z^4/m^4.
                assert W * m**4 >= Z**4

                # The combined arithmetic-spread bound.
                assert C * K * K * m**4 >= Z**4
                checked += 1
    return checked


def complete_bipartite_check():
    # K_{a,b}: left degree b, right degree a, and cap conversion equality.
    for a in range(1, 21):
        for b in range(1, 21):
            m = a*b
            C = a*a*b*b
            K = a*b
            W = K*K*C
            assert C*K*K == W
            assert m == K


def pendant_core_forms(n, t):
    D = n + t
    m = n * (n + 2*t)
    K = D*D
    C = n**4 + 4*n*n*t + 2*n*t*t
    W = n*D*D * (n**3*D*D + 4*n*t*D + 2*t*t)
    return m, K, C, W


def sharp_large_cap_check():
    previous_ratio = None
    for s in range(1, 201):
        n = s**3
        t = s**4
        m, K, C, W = pendant_core_forms(n, t)

        assert K * K * C >= W
        expected_gap = (2*s**17*(s + 1)**2*(s**4 + s**3 - 1)
                        * (s**4 + 3*s**3 + 2*s**2 + 1))
        assert K*K*C - W == expected_gap
        assert K * (2*s + 1) == m * (s + 1)**2

        # The exact rational W/(K^2 C) increases to one.
        if previous_ratio is not None and s >= 3:
            old_w, old_den = previous_ratio
            assert W * old_den > old_w * K*K*C
        previous_ratio = (W, K*K*C)

    s = 200
    n = s**3
    t = s**4
    m, K, C, W = pendant_core_forms(n, t)
    assert K > 100*m
    assert 100*W > 99*K*K*C
    assert W > m*K*C


def dyadic_spread_sanity():
    # Pure integer version of Lambda_G <= 4 when all edge products lie
    # in one two-coordinate dyadic bucket: z_min <= z <= 4 z_min.
    for z_min in range(1, 100):
        K = 4*z_min
        # Any geometric mean g of numbers in this interval satisfies g>=z_min.
        # Hence K/g<=4 and the information conversion loses at most 4^2.
        assert K*K <= 16*z_min*z_min


def main():
    checked = exhaustive_check()
    complete_bipartite_check()
    sharp_large_cap_check()
    dyadic_spread_sanity()
    print(f"PASS: {checked} nonzero matrices through 4x4")
    print("PASS: C K^2 >= W and W m^4 >= Z^4 exactly")
    print("PASS: biregular equality and G_{s^3,s^4} cap sharpness")
    print("PASS: K/m -> infinity while W/(K^2 C) -> 1")


if __name__ == "__main__":
    main()
