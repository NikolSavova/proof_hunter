#!/usr/bin/env python3
"""Exact arithmetic for PASCAL_WEIGHTED_INVERSION_LEX_SEAM_GATE.md."""

from math import comb, log, log2


def tables(dmax):
    caps = [[0] * (d + 1) for d in range(dmax + 1)]
    faces = [[0] * (d + 1) for d in range(dmax + 1)]
    caps[0][0] = faces[0][0] = 1
    for d in range(1, dmax + 1):
        caps[d][0] = caps[d][d] = 1
        faces[d][0] = faces[d][d] = 1
        for i in range(1, d):
            caps[d][i] = (caps[d - 1][i]
                          + (1 + comb(d - 1, i)) * caps[d - 1][i - 1])
        for i in range(1, d):
            faces[d][i] = (faces[d - 1][i - 1] + faces[d - 1][i]
                           + caps[d - 1][i - 1]
                           * caps[d - 1][d - 1 - i])
    return caps, faces


def dominant_path(d, i):
    value = 1
    for k in range(i):
        value *= 1 + comb(d - 1 - k, i - k)
    return value


def entropy(x):
    return (-x * log(x) - (1 - x) * log(1 - x)) / log(2)


def cap_right_cost(x):
    return (-log(1 - x) - x) / log(2)


def asymptotic_exponent():
    x = 1 / 4
    eta = 11 / 20
    guard_a = ((eta - x)
               * entropy((eta * (1 - x) - x) / (eta - x)))
    guard_b_minus = ((1 - eta * x)
                     * entropy(x / (1 - eta * x)))
    guard_b_plus = entropy(x)
    right_cost = eta * cap_right_cost(1 - x)
    phi = guard_a + guard_b_minus + guard_b_plus - right_cost
    exponent = phi / entropy(x)
    assert exponent > log2(3) + 0.08
    return guard_a, guard_b_minus, guard_b_plus, right_cost, exponent


def exact_rows():
    caps, faces = tables(320)
    rows = []
    for t in (80, 160, 240, 320):
        s = 11 * t // 20
        i = 3 * s // 4
        j = t // 4
        z = s - i
        a, b = comb(s, i), comb(t, j)

        # Prefix pools from the proof.
        guard_a = comb(s - (j + 1), i - (j + 1))
        guard_b_minus = comb(t - (z + 1), j)
        guard_b_plus = comb(t - 1, j - 1)
        cap_right = caps[s - 1][i]

        cap_a, cup_b = caps[s][i], caps[t][t - j]
        v = faces[s][i] + faces[t][j] + cap_a * cup_b
        bank_product = (guard_a * cup_b
                        * guard_b_minus * guard_b_plus * cap_right)
        exponent = (log2(bank_product) - log2(v)) / log2(a + b)

        dominant = dominant_path(s, i)
        assert dominant <= cap_a
        rows.append((t, exponent,
                     (log2(cap_a) - log2(dominant)) / s,
                     (log2(cap_a) - log2(cap_right)) / t))

    expected = [
        1.4894285647384522,
        1.5775021584213635,
        1.6069362654400212,
        1.6217836220972996,
    ]
    for row, value in zip(rows, expected):
        assert abs(row[1] - value) < 1e-12
    assert rows[2][1] > log2(3)
    assert rows[3][1] > rows[2][1]
    return rows


def main():
    constants = asymptotic_exponent()
    rows = exact_rows()
    print("PASS: lex-seam weighted inversion bank; "
          f"limit exponent={constants[-1]:.12f}; "
          "finite exponents="
          + ",".join(f"t{t}:{e:.12f}" for t, e, _, _ in rows))


if __name__ == "__main__":
    main()
