#!/usr/bin/env python3
"""Exact Pi_2 exhaustion for the first three-role common-guard wrapper.

There are eight realizable rooted four-point chirotopes in a fixed
increasing coordinate order.  This script puts each of the 8^3 words into
the exact rational pocket wrapper, makes all pair directions distinct by a
chirotope-preserving rational perturbation, and enumerates every generic
projection chamber.  Cap/cup counts use an independent last-two-points DP.
"""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations, product


# Representatives for all eight possible sign words
# (012,013,023,123) of four x-ordered points.
RAW_SEEDS = (
    ((0, -4), (1, -3), (2, -3), (7, -4)),
    ((0, -4), (1, -3), (2, -3), (7, -2)),
    ((0, -4), (1, -3), (2, -4), (7, -3)),
    ((0, -4), (1, -3), (2, -4), (7, 4)),
    ((0, -4), (1, -3), (2, -1), (7, -4)),
    ((0, -4), (1, -4), (2, -3), (7, -3)),
    ((0, -4), (1, -4), (2, -3), (7, 0)),
    ((0, -4), (1, -4), (2, -3), (7, 3)),
)
SEEDS = tuple(tuple((Q(x), Q(y)) for x, y in seed) for seed in RAW_SEEDS)


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def sign_word(points):
    return tuple(1 if det(*(points[i] for i in triple)) > 0 else -1
                 for triple in combinations(range(4), 3))


EXPECTED_WORDS = (
    (-1, -1, -1, -1), (-1, -1, -1, 1),
    (-1, -1, 1, 1), (-1, 1, 1, 1),
    (1, -1, -1, -1), (1, 1, -1, -1),
    (1, 1, 1, -1), (1, 1, 1, 1),
)


def pocket(left, right):
    return ((left - right) / (left + right), -Q(2) / (left + right))


def configuration(word):
    epsilon = Q(1, 1000)
    clusters = []
    for parameter, seed_index in zip((Q(4), Q(1), Q(1, 4)), word):
        cluster = []
        for first, transverse in SEEDS[seed_index]:
            left = (Q(1) / parameter + epsilon * first
                    + epsilon * epsilon * transverse)
            right = (parameter + epsilon * first
                     - epsilon * epsilon * transverse)
            cluster.append(pocket(left, right))
        clusters.append(cluster)
    return [(Q(-1), Q(0))] + sum(clusters, []) + [(Q(1), Q(0))], clusters


def all_signs(points):
    signs = {}
    for triple in combinations(range(len(points)), 3):
        value = det(*(points[i] for i in triple))
        assert value
        signs[triple] = 1 if value > 0 else -1
    return signs


def ordered_sign(signs, a, b, c):
    labels = [a, b, c]
    parity = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if labels[i] > labels[j]:
                parity = -parity
    return parity * signs[tuple(sorted(labels))]


def chain_counts(signs, order):
    """Nonempty cap and cup totals in one projection order."""
    n = len(order)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cap[i][j] = cup[i][j] = 1
            for h in range(i):
                if ordered_sign(signs, order[h], order[i], order[j]) < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def generic_perturb(points, original_signs):
    """Split every parallel pair direction without changing a triple sign."""
    eta = Q(1, 10 ** 30)
    perturbed = [(x + eta * 2 ** i, y + eta * 3 ** i)
                 for i, (x, y) in enumerate(points)]
    assert all_signs(perturbed) == original_signs
    slopes = {(perturbed[j][1] - perturbed[i][1])
              / (perturbed[j][0] - perturbed[i][0])
              for i, j in combinations(range(len(points)), 2)}
    assert len(slopes) == len(points) * (len(points) - 1) // 2
    return perturbed


def projection_orders(points):
    critical = sorted({-(points[j][0] - points[i][0])
                       / (points[j][1] - points[i][1])
                       for i, j in combinations(range(len(points)), 2)
                       if points[j][1] != points[i][1]})
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)
    orders = []
    seen = set()
    for slope in probes:
        order = tuple(sorted(range(len(points)),
                             key=lambda i: points[i][0] + slope * points[i][1]))
        for candidate in (order, order[::-1]):
            if candidate not in seen:
                seen.add(candidate)
                orders.append(candidate)
    return orders


def convex_four(points):
    lower = []
    for i in range(4):
        while len(lower) >= 2 and det(points[lower[-2]], points[lower[-1]], points[i]) < 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in range(4):
        while len(upper) >= 2 and det(points[upper[-2]], points[upper[-1]], points[i]) > 0:
            upper.pop()
        upper.append(i)
    return len(set(lower) | set(upper)) == 4


def local_profile(cluster):
    signs = all_signs(cluster)
    order = tuple(sorted(range(4), key=lambda i: cluster[i][0]))
    cap, cup = chain_counts(signs, order)
    return cap, cup, 15 if convex_four([cluster[i] for i in order]) else 14


def wrapper_faces(profiles):
    """Exact common-guard first-cap/last-cup recurrence."""
    sizes = [1, 4, 4, 4, 1]
    caps = [1] + [row[0] for row in profiles] + [1]
    cups = [1] + [row[1] for row in profiles] + [1]
    faces = [1] + [row[2] for row in profiles] + [1]
    total = sum(faces)
    for i in range(5):
        for j in range(i + 1, 5):
            term = caps[i] * cups[j]
            for h in range(i + 1, j):
                term *= 1 + sizes[h]
            total += term
    return total


def main():
    assert tuple(sign_word(seed) for seed in SEEDS) == EXPECTED_WORDS

    # The local profile depends only on the selected rooted chirotope.  Use
    # the first macro pocket to read it in the actual wrapper chart.
    local_profiles = []
    for index in range(8):
        _, clusters = configuration((index, index, index))
        local_profiles.append(local_profile(clusters[0]))
    assert sorted(set(local_profiles)) == [
        (10, 15, 15), (11, 13, 14), (12, 12, 15),
        (13, 11, 14), (15, 10, 15),
    ]

    rows = []
    for word in product(range(8), repeat=3):
        points, clusters = configuration(word)
        signs = all_signs(points)
        profiles = [local_profile(cluster) for cluster in clusters]
        faces = wrapper_faces(profiles)

        points = generic_perturb(points, signs)
        orders = projection_orders(points)
        assert len(orders) == 182
        natural = tuple(sorted(range(14), key=lambda i: points[i][0]))
        reverse = natural[::-1]
        assembly = chain_counts(signs, natural)
        reset_profiles = [chain_counts(signs, order) for order in orders
                          if order not in (natural, reverse)]
        reset = min(reset_profiles, key=lambda row: row[0] * row[1])
        rows.append((faces, assembly, reset, word))

    minimum_faces = min(row[0] for row in rows)
    minimum_reset = min(row[2][0] * row[2][1] for row in rows)
    minimum_ratio = min(Q(row[2][0] * row[2][1], row[0]) for row in rows)
    minimizing_words = [row for row in rows if row[0] == minimum_faces]
    minimizing_word_reset = min(row[2][0] * row[2][1]
                                for row in minimizing_words)

    assert minimum_faces == 1561
    assert minimum_reset == 134995
    assert minimum_ratio == Q(157113, 2546)
    assert minimizing_word_reset == 157113

    print("PASS: rooted types=8, words=512, chambers/word=182, "
          "min W=1561, min reset CU=134995, "
          "min reset CU/W=157113/2546, "
          "min reset CU among W-minimizers=157113")


if __name__ == "__main__":
    main()
