#!/usr/bin/env python3
"""Finite checks for PARABOLIC_LOCAL_MIN_FEW_FIBRE_GLOBAL_SUM.md."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, gcd


def local_min_sum(values):
    return sum(min(x * y, y * z, z * x)
               for x, y, z in combinations(values, 3))


def direction_envelope(a):
    """Exact clean envelope, with a indexed by consecutive integer levels."""
    n = len(a)
    total = 0
    for c in range(-(n - 1), n):
        if c:
            b = [a[r] * a[r + c]
                 for r in range(n)
                 if 0 <= r + c < n and a[r] and a[r + c]]
        else:
            b = [x * (x - 1) for x in a if x >= 2]
        total += local_min_sum(b)
    return total


def primitive(v):
    x, y = v
    d = gcd(abs(x), abs(y))
    x, y = x // d, y // d
    if x < 0 or (x == 0 and y < 0):
        x, y = -x, -y
    return x, y


def squared_distance(p, q):
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def is_distance_sidon(points):
    seen = set()
    for p, q in combinations(points, 2):
        d = squared_distance(p, q)
        if d in seen:
            return False
        seen.add(d)
    return True


def direction_energies(points):
    energies = Counter()
    for p, q in combinations(points, 2):
        energies[primitive((q[0] - p[0], q[1] - p[1]))] += 1
    return energies


def check_fixed_direction_bound():
    checked = 0
    worst = (0.0, None, None)
    for n in range(1, 8):
        for a in product(range(5), repeat=n):
            k = sum(a)
            if not k:
                continue
            s = direction_envelope(a)
            assert 6 * s <= k ** 4, (a, s, k ** 4)
            support = sum(x > 0 for x in a)
            e = sum(x * (x - 1) // 2 for x in a)
            if support and k >= 2 * support:
                assert 3 * s <= 8 * support * support * e * e
            ratio = 6 * s / k ** 4
            if ratio > worst[0]:
                worst = (ratio, a, s)
            checked += 1
    print(f"fixed-direction exact checks: PASS ({checked} arrays; "
          f"largest 6S/k^4={worst[0]:.6f})")


def check_parabola():
    for k in range(4, 31):
        points = [(i, i * i) for i in range(1, k + 1)]
        assert is_distance_sidon(points)
        a = [1] * k
        got = direction_envelope(a)
        want = 2 * comb(k, 4)
        assert got == want, (k, got, want)
    print("integer parabola distance-Sidon and 2*C(k,4) envelope: PASS")


def check_directional_golomb_budget():
    examples = []
    examples.append([(i, i * i) for i in range(1, 19)])
    # A short one-dimensional Golomb ruler embedded horizontally.
    examples.append([(x, 1) for x in (1, 2, 5, 11, 13, 18)])
    # Deterministic sparse search examples.
    for k in (8, 10):
        points = []
        for x in range(1, k * k + 1):
            p = (x, x * x)
            if p[1] <= k * k:
                points.append(p)
        if len(points) >= 3:
            examples.append(points)

    for points in examples:
        assert is_distance_sidon(points)
        width = max(max(x for x, _ in points) - min(x for x, _ in points),
                    max(y for _, y in points) - min(y for _, y in points))
        energies = direction_energies(points)
        for w, e in energies.items():
            assert e <= width // max(abs(w[0]), abs(w[1])), (points, w, e)
        harmonic = sum((Fraction(1, q) for q in range(1, width + 1)),
                       Fraction(0, 1))
        assert sum(e * e for e in energies.values()) <= 4 * width * width * harmonic
    print("directional Golomb capacities e_w <= M/||w||_inf: PASS")


def print_scaling_audit():
    print("few-fibre model (six equal rows):")
    for h in (4, 8, 16, 32):
        k = 6 * h
        e = 6 * comb(h, 2)
        local_three_level = h ** 4
        print(f"  h={h:2d}: k={k:3d}, e_w^2={e*e:10d}, "
              f"three-level min={local_three_level:8d}")


def main():
    check_fixed_direction_bound()
    check_parabola()
    check_directional_golomb_budget()
    print_scaling_audit()
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
