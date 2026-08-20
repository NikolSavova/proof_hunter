#!/usr/bin/env python3
"""Exact/symbolic checks for PROPER_COLORING_EUCLIDEAN_REALIZATION_BARRIER.md."""

from fractions import Fraction
from math import gcd, pi, sin


def sqdist(p, q):
    return sum((x - y) ** 2 for x, y in zip(p, q))


def check_centroid_identity():
    point_sets = [
        [(0, 0), (1, 0), (0, 2), (3, -1)],
        [(-3, 1), (2, 5), (7, -4), (0, 0), (8, 3)],
        [(Fraction(1, 2), Fraction(2, 3)),
         (Fraction(-4, 5), Fraction(7, 3)),
         (Fraction(9, 4), Fraction(-1, 6))],
    ]
    for pts in point_sets:
        n = len(pts)
        centroid = tuple(sum(p[d] for p in pts) / n for d in range(2))
        qmoment = sum(sqdist(p, centroid) for p in pts)
        for p in pts:
            lhs = sum(sqdist(p, q) for q in pts)
            rhs = n * sqdist(p, centroid) + qmoment
            assert lhs == rhs


def shift_matrix(n):
    # S e_j = e_{j+1} (indices modulo n).
    S = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        S[(j + 1) % n][j] = 1
    return S


def cyclic_matrices(weights):
    n = len(weights)
    H = [[weights[(i + j) % n] for j in range(n)] for i in range(n)]
    Delta = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Delta[i][i] = weights[(2 * i) % n]
    return H, matrix_sub(H, Delta), Delta


def matrix_mul(a, b):
    rows, mid, cols = len(a), len(b), len(b[0])
    assert len(a[0]) == mid
    return [
        [sum(a[i][k] * b[k][j] for k in range(mid)) for j in range(cols)]
        for i in range(rows)
    ]


def matrix_sub(a, b):
    return [
        [a[i][j] - b[i][j] for j in range(len(a[0]))]
        for i in range(len(a))
    ]


def matrix_neg(a):
    return [[-entry for entry in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def exact_rank(matrix):
    """Gaussian-elimination rank over Q, with no optional dependencies."""
    a = [[Fraction(entry) for entry in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        a[rank] = [entry / pivot_value for entry in a[rank]]
        for r in range(rows):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [a[r][j] - factor * a[rank][j]
                        for j in range(cols)]
        rank += 1
        if rank == rows:
            break
    return rank


def check_cyclic_displacement():
    for n in range(3, 21):
        # Positive, nonperiodic, and exact.  The theorem itself only needs
        # nonzero weights, not distinctness.
        weights = [j * j + 3 * j + 7 for j in range(n)]
        H, D, Delta = cyclic_matrices(weights)
        S = shift_matrix(n)
        Sinv = transpose(S)
        assert matrix_mul(S, H) == matrix_mul(H, Sinv)
        K = matrix_sub(matrix_mul(S, D), matrix_mul(D, Sinv))
        rhs = matrix_sub(matrix_neg(matrix_mul(S, Delta)),
                         matrix_neg(matrix_mul(Delta, Sinv)))
        assert K == rhs
        expected = n - gcd(n, 2)
        rank_k = exact_rank(K)
        rank_d = exact_rank(D)
        assert rank_k >= expected, (n, rank_k, expected)
        assert expected <= 2 * rank_d
        assert rank_d >= (expected + 1) // 2


def is_additive_sidon(values):
    sums = {}
    for i, a in enumerate(values):
        for j in range(i, len(values)):
            s = a + values[j]
            assert s not in sums, (s, sums[s], (i, j))
            sums[s] = (i, j)
    return True


def check_sidon_chords():
    # A small Golomb/Sidon set, scaled into an arc of width < pi/2.
    raw = [0, 1, 4, 10]
    assert is_additive_sidon(raw)
    scale = (pi / 3) / max(raw)
    angles = [scale * x for x in raw]
    seen = {}
    for i in range(len(angles)):
        for j in range(i + 1, len(angles)):
            chord2 = 4.0 * sin(abs(angles[i] - angles[j]) / 2.0) ** 2
            for old, pair in seen.items():
                assert abs(chord2 - old) > 1e-12, (pair, (i, j))
            seen[chord2] = (i, j)


def main():
    check_centroid_identity()
    check_cyclic_displacement()
    check_sidon_chords()
    print("PASS: centroid/circle, cyclic displacement-rank, and chord-Sidon checks")


if __name__ == "__main__":
    main()
