#!/usr/bin/env python3
"""Exact audits for the weighted path-pair/bottleneck theorem."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import prod


Resource = tuple[int, int]


def disjoint_mass(paths: list[frozenset[Resource]], weights: list[Fraction]) -> Fraction:
    return sum(
        weights[i] * weights[j]
        for i in range(len(paths))
        for j in range(len(paths))
        if paths[i].isdisjoint(paths[j])
    )


def greedy_bottleneck(
    paths: list[frozenset[Resource]],
    weights: list[Fraction],
    length_bound: int,
    root_delta: Fraction,
) -> tuple[set[Resource], Fraction]:
    """The constructive proof of Theorem 1 for delta=root_delta**2."""
    assert sum(weights) == 1 and root_delta > 0
    threshold = root_delta / length_bound
    remaining = set(range(len(paths)))
    bottleneck: set[Resource] = set()
    universe = set().union(*paths)
    while True:
        loads = {
            x: sum(weights[i] for i in remaining if x in paths[i])
            for x in universe
        }
        x, load = max(loads.items(), key=lambda item: item[1])
        if load < threshold:
            break
        bottleneck.add(x)
        remaining = {i for i in remaining if x not in paths[i]}
        if not remaining:
            break
    residual = sum(weights[i] for i in remaining)
    assert len(bottleneck) * root_delta <= length_bound
    assert residual <= 2 * root_delta
    covered = 1 - residual
    return bottleneck, covered


def weighted_path_audit() -> dict[str, int]:
    cases = 0
    bottleneck_cases = 0
    for q in range(2, 8):
        words = list(product(range(2), repeat=q))
        paths = [frozenset((i, x) for i, x in enumerate(word)) for word in words]
        for skew in range(1, 42):
            raw = [1 + ((j * j + skew * j + 3 * skew) % 17) for j in range(len(words))]
            total = sum(raw)
            weights = [Fraction(x, total) for x in raw]
            delta_mass = disjoint_mass(paths, weights)
            # Square thresholds 1/k^2.  Audit every case in which the theorem
            # enters its bottleneck conclusion.
            for k in (2, 3, 4, 5, 8, 13):
                root = Fraction(1, k)
                if delta_mass < root * root:
                    bottleneck, covered = greedy_bottleneck(paths, weights, q, root)
                    assert len(bottleneck) <= q * k
                    assert covered >= 1 - 2 * root
                    bottleneck_cases += 1
            cases += 1
    assert cases == 246
    return {"weighted_laws": cases, "bottleneck_conclusions": bottleneck_cases}


def is_forward(x: tuple[int, ...], y: tuple[int, ...]) -> bool:
    if x == y:
        return False
    if y < x:
        x, y = y, x
    j = next(i for i in range(len(x)) if x[i] != y[i])
    return any(x[k] > y[k] for k in range(j + 1, len(x)))


def product_counts(sizes: tuple[int, ...], brute: bool) -> tuple[int, Fraction, Fraction]:
    n = prod(sizes)
    resource_disjoint = Fraction(prod(m - 1 for m in sizes), n)
    coordinate_increasing = prod(m * (m + 1) // 2 for m in sizes)
    nonnested = Fraction(n * n - (2 * coordinate_increasing - n), n * n)
    assert nonnested >= 1 - 2 * Fraction(3, 4) ** len(sizes)
    if brute:
        words = list(product(*(range(m) for m in sizes)))
        paths = [frozenset((i, x) for i, x in enumerate(word)) for word in words]
        uniform = [Fraction(1, n)] * n
        assert disjoint_mass(paths, uniform) == resource_disjoint
        brute_nonnested = Fraction(
            sum(is_forward(x, y) for x in words for y in words), n * n
        )
        assert brute_nonnested == nonnested
    return n, resource_disjoint, nonnested


def product_endpoint_audit() -> dict[str, int]:
    cases = 0
    brute_cases = 0
    for q in range(1, 7):
        for base in range(2, 7):
            for tilt in range(5):
                sizes = tuple(2 + ((base + tilt * i + i * i) % 4) for i in range(q))
                brute = prod(sizes) <= 240
                product_counts(sizes, brute)
                cases += 1
                brute_cases += int(brute)
    assert cases == 150
    return {"product_dags": cases, "brute_force_dags": brute_cases}


def nested_parabola_audit(limit: int = 512) -> dict[str, int]:
    for s in range(1, limit + 1):
        paths = [frozenset((0, j) for j in range(i + 1)) for i in range(s)]
        weights = [Fraction(1, s)] * s
        assert disjoint_mass(paths, weights) == 0
        common = set.intersection(*(set(path) for path in paths))
        assert (0, 0) in common
        assert 4 * (s + 1) ** 2 <= 9 * (1 << s)
    return {"depths": limit, "common_bottleneck_size": 1}


def ramp_exponents(h: int) -> tuple[int, ...]:
    ell = 1 << h
    left = tuple(1 << j for j in range(h))
    return left + (ell,) * (ell // 2) + tuple(reversed(left))


def ramp_audit() -> dict[str, int]:
    profiles = 0
    largest_bits = 0
    for h in range(3, 8):
        exponents = ramp_exponents(h)
        sizes = tuple(1 << a for a in exponents)
        n, disjoint, nonnested = product_counts(sizes, brute=False)
        assert 0 < disjoint < 1 and 0 < nonnested < 1
        largest_bits = max(largest_bits, n.bit_length() - 1)
        profiles += 1
    return {"profiles": profiles, "largest_log2_path_count": largest_bits}


def main() -> None:
    weighted = weighted_path_audit()
    nested = nested_parabola_audit()
    products = product_endpoint_audit()
    ramps = ramp_audit()
    print("WEIGHTED_BOTTLENECK", weighted)
    print("NESTED_PARABOLA", nested)
    print("PRODUCT_ENDPOINT_BLOCKS", products)
    print("RAMP_PLATEAU_PATHS", ramps)
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
