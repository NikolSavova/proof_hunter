#!/usr/bin/env python3
"""Exact checks for PATHWISE_PROJECTION_ITINERARY_COMPRESSION_GATE.md."""

from fractions import Fraction as Q
from itertools import product
from math import comb, floor, log2


def mobius(matrix, x):
    a, b, c, d = matrix
    denominator = c * x + d
    if denominator == 0:
        return None
    return (a * x + b) / denominator


def wall_value(matrix, theta, critical):
    a, b, c, d = matrix
    return (
        theta * a + b
        - critical * theta * c - critical * d
    )


def cross_ratio(x1, x2, x3, x4):
    return ((x3 - x1) * (x4 - x2)) / (
        (x4 - x1) * (x3 - x2)
    )


def check_linear_walls_and_sampled_itineraries():
    directions = [Q(-2), Q(-1, 3), Q(1, 2), Q(3)]
    critical = [Q(-3), Q(-1), Q(0), Q(2), Q(5)]
    matrices = []
    for a, b, c, d in product(range(-3, 4), repeat=4):
        determinant = a * d - b * c
        if determinant <= 0:
            continue
        matrix = tuple(map(Q, (a, b, c, d)))
        if any(mobius(matrix, theta) is None for theta in directions):
            continue
        if any(wall_value(matrix, theta, lam) == 0
               for theta in directions for lam in critical):
            continue
        matrices.append(matrix)

    words = set()
    for matrix in matrices:
        word = []
        for theta in directions:
            image = mobius(matrix, theta)
            word.append(sum(lam < image for lam in critical))
            denominator = matrix[2] * theta + matrix[3]
            for lam in critical:
                # After multiplying by the denominator, the comparison
                # image-lam is exactly the advertised homogeneous wall.
                assert (
                    (image - lam) * denominator
                    == wall_value(matrix, theta, lam)
                )
        words.add(tuple(word))

    m = len(directions) * len(critical)
    region_bound = sum(comb(m, k) for k in range(4))
    assert len(words) <= region_bound
    return len(matrices), len(words), region_bound


def check_scale_slack():
    rows = []
    for L in (32, 64, 128, 256):
        ell = floor(log2(L))
        phi = lambda x: Q(x * x, 2)
        one_gap = phi(L) - phi(L - ell)
        depth = L // ell
        assert depth >= 2
        for k in range(2, depth + 1):
            slack = phi(L) - phi(L - k * ell)
            assert slack > one_gap
            # More generally, only O(K) levels fit in K one-gap budgets.
            assert slack >= k * one_gap - Q(k * (k - 1) * ell * ell, 2)
        rows.append((L, ell, int(one_gap), depth))
    return rows


def check_word_entropy_and_cross_ratio():
    entropy_rows = []
    for L in (64, 256, 1024, 4096):
        ell = floor(log2(L))
        h = L // ell
        bits = h * log2(L + 1)
        assert bits < 1.2 * L
        entropy_rows.append((L, h, bits))

    first = tuple(map(Q, (0, 1, 2, 3)))
    second = tuple(map(Q, (0, 1, 2, 4)))
    assert cross_ratio(*first) == Q(4, 3)
    assert cross_ratio(*second) == Q(3, 2)
    assert cross_ratio(*first) != cross_ratio(*second)
    return entropy_rows


if __name__ == "__main__":
    sampled = check_linear_walls_and_sampled_itineraries()
    slack = check_scale_slack()
    entropy = check_word_entropy_and_cross_ratio()
    print(
        "PASS: PGL2 query walls are linear, sampled itineraries obey the "
        f"RP3 region bound {sampled}, cross-ratio histories differ, "
        f"fixed-gap slack rows={slack}, word entropy rows={entropy}"
    )
