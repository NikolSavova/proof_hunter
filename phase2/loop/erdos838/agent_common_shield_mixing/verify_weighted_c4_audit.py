#!/usr/bin/env python3
"""Exact verifier for WEIGHTED_C4_INEQUALITY_AUDIT.md."""

from itertools import product


def counts(rows, q):
    """Return (m,C,W,Z) for bitset rows and q right vertices."""
    p = len(rows)
    d = [r.bit_count() for r in rows]
    e = [sum((rows[i] >> j) & 1 for i in range(p)) for j in range(q)]
    m = sum(d)
    C = W = 0
    for i in range(p):
        for k in range(p):
            common = rows[i] & rows[k]
            c = common.bit_count()
            s = 0
            x = common
            while x:
                bit = x & -x
                s += e[bit.bit_length() - 1]
                x -= bit
            C += c * c
            W += d[i] * d[k] * s * s
    Z = sum(d[i] * e[j] for i in range(p) for j in range(q)
            if (rows[i] >> j) & 1)
    return m, C, W, Z


def exhaustive_through_4x4():
    checked = 0
    equality = 0
    for p in range(1, 5):
        for q in range(1, 5):
            for mask in range(1 << (p * q)):
                rows = []
                for i in range(p):
                    rows.append((mask >> (i * q)) & ((1 << q) - 1))
                m, C, W, _ = counts(rows, q)
                assert W <= m * m * C, (p, q, mask, m, C, W)
                checked += 1
                equality += (W == m * m * C)
    return checked, equality


def universal_private(a, b):
    # Universal row, then a singleton rows for each of b columns.
    rows = [(1 << b) - 1]
    for j in range(b):
        rows.extend([1 << j] * a)
    return rows


def check_structured_family():
    for a in range(1, 8):
        for b in range(1, 20):
            m, C, W, _ = counts(universal_private(a, b), b)
            assert m == b * (a + 1)
            assert C == b * (a * a + 2 * a + b)
            expected_W = (a + 1) ** 2 * ((a + b * b) ** 2 + (b - 1) * a * a)
            assert W == expected_W
            assert W <= m * m * C
    ratios = []
    for b in (10, 20, 50, 100, 200):
        m, C, W, _ = counts(universal_private(1, b), b)
        ratios.append(W / (m * m * C))
    assert all(x < y < 1 for x, y in zip(ratios, ratios[1:])), ratios
    return ratios


def kron(rows_a, qa, rows_b, qb):
    """Bit rows of the Kronecker product of two 0,1 matrices."""
    out = []
    for ra in rows_a:
        for rb in rows_b:
            row = 0
            for ja in range(qa):
                if (ra >> ja) & 1:
                    row |= rb << (ja * qb)
            out.append(row)
    return out, qa * qb


def check_tensor_multiplicativity():
    examples = [
        ([0b11, 0b01], 2),
        ([0b111, 0b101], 3),
        ([0b101, 0b011, 0b110], 3),
    ]
    for (a, qa), (b, qb) in product(examples, repeat=2):
        ma, ca, wa, _ = counts(a, qa)
        mb, cb, wb, _ = counts(b, qb)
        ab, qab = kron(a, qa, b, qb)
        m, c, w, _ = counts(ab, qab)
        assert (m, c, w) == (ma * mb, ca * cb, wa * wb)


def main():
    checked, equality = exhaustive_through_4x4()

    # Three-edge L: the desired inequality passes, two common shortcuts fail.
    m, C, W, Z = counts([0b11, 0b01], 2)
    assert (m, C, Z, W) == (3, 7, 8, 56)
    assert W <= m * m * C < Z * Z
    assert W * W > m * m * C * C * C  # W > m C^(3/2), squared exactly.

    ratios = check_structured_family()
    check_tensor_multiplicativity()

    print(f"PASS: exact inequality on {checked} matrices through 4x4")
    print(f"PASS: {equality} equality cases (including the empty graph)")
    print("PASS: L-shape shortcut obstructions are exact")
    print("PASS: universal-plus-private formulas; a=1 ratios:", ratios)
    print("PASS: tensor multiplicativity on deterministic examples")


if __name__ == "__main__":
    main()

