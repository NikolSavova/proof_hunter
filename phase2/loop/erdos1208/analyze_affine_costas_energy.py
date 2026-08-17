#!/usr/bin/env python3
"""Stress-test rotated energy on anisotropically stretched Welch Costas sets.

A Costas permutation has unique directed difference vectors but generally not
unique Euclidean lengths.  We find the smallest integral vertical stretch
that separates all squared lengths, then compute the exact energy of A+JA.
This probes whether dense distinct-difference configurations can falsify the
conjectural fifth-power bound after metric separation.
"""

from collections import Counter


def prime_factors(n: int) -> set[int]:
    out: set[int] = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError("no primitive root")


def welch(p: int) -> list[tuple[int, int]]:
    g = primitive_root(p)
    return [(i, pow(g, i, p)) for i in range(p - 1)]


def is_distance_sidon(a: list[tuple[int, int]]) -> bool:
    norms: set[int] = set()
    for i, x in enumerate(a):
        for y in a[:i]:
            norm = (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
            if norm in norms:
                return False
            norms.add(norm)
    return True


def smallest_transform(
    a: list[tuple[int, int]], limit: int = 1000
) -> tuple[int, int]:
    """Return a small integral shear/stretch (x,y)->(x+h*y,s*y)."""
    for size in range(1, limit + 1):
        for shear in range(-size, size + 1):
            stretch = size
            transformed = [(x + shear * y, stretch * y) for x, y in a]
            if is_distance_sidon(transformed):
                return shear, stretch
    raise AssertionError("transform search limit exhausted")


def energy_cross_sum(a: list[tuple[int, int]]) -> tuple[int, int]:
    b = [(x1 - y2, x2 + y1) for x1, x2 in a for y1, y2 in a]
    assert len(set(b)) == len(b)
    differences: Counter[tuple[int, int]] = Counter()
    for x in b:
        for y in b:
            differences[(x[0] - y[0], x[1] - y[1])] += 1
    nonzero_peak = max(
        value for difference, value in differences.items() if difference != (0, 0)
    )
    return sum(value * value for value in differences.values()), nonzero_peak


if __name__ == "__main__":
    for prime in [7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        original = welch(prime)
        shear, stretch = smallest_transform(original)
        a = [(x + shear * y, stretch * y) for x, y in original]
        energy, peak = energy_cross_sum(a)
        k = len(a)
        print(
            "p", prime,
            "k", k,
            "shear", shear,
            "stretch", stretch,
            "energy/k^5", round(energy / k**5, 6),
            "peak/k", round(peak / k, 6),
        )
