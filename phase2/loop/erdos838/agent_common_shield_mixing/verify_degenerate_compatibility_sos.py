#!/usr/bin/env python3
"""Exact verifier for DEGENERATE_COMPATIBILITY_SOS.md."""


def data(rows, q):
    p = len(rows)
    d = [r.bit_count() for r in rows]
    e = [sum((rows[i] >> j) & 1 for i in range(p)) for j in range(q)]
    m = sum(d)
    edges = [(i, j) for i in range(p) for j in range(q)
             if (rows[i] >> j) & 1]
    h = [sum(e[j] for j in range(q) if (rows[i] >> j) & 1)
         for i in range(p)]
    g = [sum(d[i] for i in range(p) if (rows[i] >> j) & 1)
         for j in range(q)]
    return p, d, e, m, edges, h, g


def verify_one(rows, q):
    p, d, e, m, edges, h, g = data(rows, q)
    if m == 0:
        return True, 0, 0, 0

    # delta_num[e] = m^2 delta_e.
    delta = {}
    for i, j in edges:
        num = (d[i] * (m * m - h[i] * h[i])
               + e[j] * (m * m - g[j] * g[j])
               - m * m + d[i] * d[i] * e[j] * e[j])
        assert num >= 0, (rows, q, i, j, num)
        # Also check the only set inequality used in the proof.
        assert h[i] + g[j] <= m + d[i] * e[j]
        delta[(i, j)] = num

    C0 = sum(z * z for z in d) + sum(z * z for z in e) - m
    X0_num = (sum(d[i] * d[i] * h[i] * h[i] for i in range(p))
              + sum(e[j] * e[j] * g[j] * g[j] for j in range(q))
              - sum(d[i] * d[i] * e[j] * e[j] for i, j in edges))
    assert m * m * C0 - X0_num == sum(delta.values())

    C = 0
    X_num = 0
    genuine_count = 0
    genuine_residual_num = 0
    for i, j in edges:
        for k, l in edges:
            if ((rows[i] >> l) & 1) and ((rows[k] >> j) & 1):
                C += 1
                X_num += d[i] * e[j] * d[k] * e[l]
                if i != k and j != l:
                    genuine_count += 1
                    genuine_residual_num += (m * m
                                             - d[i] * e[j] * d[k] * e[l])

    assert m * m * C - X_num == sum(delta.values()) + genuine_residual_num
    no_genuine = genuine_count == 0
    if no_genuine:
        assert X_num <= m * m * C
    return no_genuine, C, X_num, sum(delta.values())


def exhaustive():
    checked = c4_free = 0
    for p in range(1, 5):
        for q in range(1, 5):
            for mask in range(1 << (p * q)):
                rows = [((mask >> (i * q)) & ((1 << q) - 1))
                        for i in range(p)]
                no_genuine, _, _, _ = verify_one(rows, q)
                checked += 1
                c4_free += no_genuine
    return checked, c4_free


def universal_private(a, b):
    rows = [(1 << b) - 1]
    for j in range(b):
        rows.extend([1 << j] * a)
    return rows


def double_star(n):
    return [1 << (n - 1) for _ in range(n - 1)] + [(1 << n) - 1]


def kron(rows_a, qa, rows_b, qb):
    out = []
    for ra in rows_a:
        for rb in rows_b:
            row = 0
            for ja in range(qa):
                if (ra >> ja) & 1:
                    row |= rb << (ja * qb)
            out.append(row)
    return out, qa * qb


def stress():
    # L, double stars, and universal-plus-private graphs are C4-free.
    assert verify_one([0b11, 0b01], 2)[0]
    for n in range(2, 30):
        assert verify_one(double_star(n), n)[0]
    for a in range(1, 6):
        for b in range(1, 30):
            assert verify_one(universal_private(a, b), b)[0]

    # Tensor products may have genuine rectangles; the exact identity
    # must continue to hold (verify_one asserts it internally).
    examples = [([0b11, 0b01], 2),
                ([0b111, 0b001, 0b010], 3),
                (double_star(4), 4)]
    for a, qa in examples:
        for b, qb in examples:
            ab, q = kron(a, qa, b, qb)
            verify_one(ab, q)

    # The genuine-rectangle contribution is negative here and must be
    # paid by the nonnegative degenerate certificate.
    residual = [0b1011, 0b0111, 0b0001]
    no_genuine, C, X_num, delta_sum = verify_one(residual, 4)
    assert not no_genuine
    assert delta_sum == 324
    assert 7 * 7 * C - X_num == 304


def main():
    checked, c4_free = exhaustive()
    stress()
    print(f"PASS: {checked} matrices through 4x4; edgewise deltas and identities exact")
    print(f"PASS: C4-free theorem on {c4_free} enumerated supports")
    print("PASS: L, double-star, universal-private, and tensor stress families")


if __name__ == "__main__":
    main()
