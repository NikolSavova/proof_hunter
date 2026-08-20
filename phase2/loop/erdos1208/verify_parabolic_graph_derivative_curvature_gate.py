#!/usr/bin/env python3
"""Checks for PARABOLIC_GRAPH_DERIVATIVE_CURVATURE_GATE.md."""

from collections import defaultdict
from itertools import combinations
from math import comb
from random import Random


def is_distance_sidon(points):
    seen = set()
    for p, q in combinations(points, 2):
        d = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
        if d in seen:
            return False
        seen.add(d)
    return True


def derivative_points(f, c):
    return [(r, f[r + c] - f[r])
            for r in sorted(f) if r + c in f]


def collinear(p, q, r):
    return ((q[0] - p[0]) * (r[1] - p[1])
            == (q[1] - p[1]) * (r[0] - p[0]))


def line_key(p, q):
    # Integer normalized ax+by=d.
    a = q[1] - p[1]
    b = p[0] - q[0]
    d = a * p[0] + b * p[1]
    from math import gcd
    g = gcd(gcd(abs(a), abs(b)), abs(d))
    if g:
        a, b, d = a // g, b // g, d // g
    if a < 0 or (a == 0 and b < 0):
        a, b, d = -a, -b, -d
    return a, b, d


def max_line_and_triples(points):
    lines = defaultdict(set)
    for i, j in combinations(range(len(points)), 2):
        lines[line_key(points[i], points[j])].update((i, j))
    sizes = [len(v) for v in lines.values()]
    triples = sum(comb(t, 3) for t in sizes if t >= 3)
    return max(sizes, default=1), triples


def check_quadratic_family():
    for k in range(6, 30):
        f = {r: r * r for r in range(1, k + 1)}
        points = [(r, f[r]) for r in f]
        assert is_distance_sidon(points)
        cell_total = 0
        slopes = []
        for c in range(1, k):
            p = derivative_points(f, c)
            if len(p) >= 2:
                slope = p[1][1] - p[0][1]
                assert slope == 2 * c
                assert all(y == 2 * c * r + c * c for r, y in p)
                slopes.append(slope)
            cell_total += comb(len(p), 3)
        assert len(slopes) == len(set(slopes))
        assert cell_total == comb(k, 4)
    print("quadratic derivative lines and C(k,4) positive-shift total: PASS")


def check_second_difference_height():
    rng = Random(1208)
    for _ in range(500):
        length = rng.randrange(2, 25)
        D = rng.choice([i for i in range(-12, 13) if i])
        B = rng.randrange(-100, 101)
        C = rng.randrange(-100, 101)
        x = [C + B * j + D * j * (j - 1) // 2
             for j in range(length + 1)]
        span = max(x) - min(x)
        s = length // 2
        assert 2 * span >= abs(D) * s * s
        assert x[2 * s] - 2 * x[s] + x[0] == D * s * s
    print("constant-second-difference height inequality: PASS")


def check_incidence_budget():
    rng = Random(20260820)
    for k in range(4, 30):
        levels = sorted(rng.sample(range(1, 20 * k), k))
        counts = defaultdict(int)
        for a in levels:
            for b in levels:
                if a != b:
                    counts[b - a] += 1
        assert sum(counts.values()) == k * (k - 1)
        assert sum(n * n for n in counts.values()) <= k ** 3
    print("projection correlation budgets sum n_c=k(k-1), sum n_c^2<=k^3: PASS")


def check_distinct_full_slopes():
    # Exact quadratic distance-Sidon examples have every positive cell full.
    # The slope collision assertion is then visible without numerical fitting.
    for k in (8, 12, 18, 24):
        f = {r: 10 * r * r + 3 * r + 7 for r in range(1, k + 1)}
        points = [(r, f[r]) for r in f]
        assert is_distance_sidon(points)
        slopes = {}
        for c in range(1, k // 2 + 1):
            p = derivative_points(f, c)
            slope = p[1][1] - p[0][1]
            assert slope and slope not in slopes
            slopes[slope] = c
        assert len(slopes) == k // 2
    print("full-cell slopes distinct on distance-Sidon quadratic stresses: PASS")


def check_matching_rectangle_cocycle():
    rng = Random(1938)
    for t in range(3, 25):
        # A quadratic block, with arbitrary affine terms, saturates the theorem.
        B = rng.choice([i for i in range(-9, 10) if i])
        A = rng.randrange(-50, 51)
        C = rng.randrange(-50, 51)
        f = {r: B * r * (r - 1) // 2 + A * r + C
             for r in range(0, 3 * t + 1)}

        recovered = []
        for c in range(t, 2 * t + 1):
            p = [(r, f[r + c] - f[r]) for r in range(t)]
            slope = p[1][1] - p[0][1]
            assert all(y == p[0][1] + slope * r for r, y in p)
            recovered.append((c, slope))

        # Adjacent-cell subtraction recovers the same affine first derivative.
        g = [f[s + 1] - f[s] for s in range(t, 3 * t - 1)]
        assert all(g[j + 1] - g[j] == B for j in range(len(g) - 1))
        assert B

        # Every individual planted cell is a matching between disjoint blocks.
        for c, _ in recovered:
            tails = set(range(t))
            heads = set(range(c, c + t))
            assert tails.isdisjoint(heads)
        assert (t + 1) * comb(t, 3) <= (t + 1) * t ** 3 // 6
    print("matching-rectangle cocycle and quadratic block: PASS")


def check_generic_derivative_counts():
    rng = Random(57)
    for k in range(7, 18):
        # No metric assertion here: this checks the exact derivative/line count.
        f = {r: rng.randrange(-10 * k, 10 * k + 1)
             for r in range(1, k + 1)}
        total = 0
        for c in range(1, k):
            p = derivative_points(f, c)
            ell, triples = max_line_and_triples(p)
            assert ell <= len(p)
            brute = sum(collinear(*triple) for triple in combinations(p, 3))
            assert triples == brute
            total += triples
        assert total >= 0
    print("derivative collinear-triple enumeration: PASS")


def main():
    check_quadratic_family()
    check_second_difference_height()
    check_incidence_budget()
    check_distinct_full_slopes()
    check_matching_rectangle_cocycle()
    check_generic_derivative_counts()
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
