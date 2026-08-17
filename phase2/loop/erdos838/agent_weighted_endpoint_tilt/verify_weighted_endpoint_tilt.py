#!/usr/bin/env python3
"""Exact/high-precision checks for the weighted endpoint tilt theorem."""

from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction
from functools import lru_cache


getcontext().prec = 90
LN2 = Decimal(2).ln()


def log2_decimal(value: Decimal) -> Decimal:
    return value.ln() / LN2


def phi(value: Decimal) -> Decimal:
    return value * (value - 1) / 2


def scalar_grid() -> tuple[int, Decimal]:
    checks = 0
    minimum = Decimal("Infinity")
    activities = tuple(sorted({Fraction(p, q) for q in range(1, 12) for p in range(1, q + 1)}))
    for a in range(1, 100):
        for b in range(1, a + 1):
            for activity in activities:
                t = Decimal(activity.numerator) / Decimal(activity.denominator)
                left = log2_decimal(1 + Decimal(b) * t)
                old = log2_decimal(1 + Decimal(a) * t)
                new = log2_decimal(1 + Decimal(a + b) * t)
                slack = left - (phi(new) - phi(old))
                assert slack >= Decimal("-1e-75")
                minimum = min(minimum, slack)
                checks += 1
    return checks, minimum


Tree = None | tuple["Tree", "Tree"]


@lru_cache(None)
def trees(n: int) -> tuple[Tree, ...]:
    if n == 1:
        return (None,)
    return tuple(
        (left, right)
        for a in range(1, n)
        for left in trees(a)
        for right in trees(n - a)
    )


@lru_cache(None)
def size(tree: Tree) -> int:
    if tree is None:
        return 1
    return size(tree[0]) + size(tree[1])


def endpoint_values(tree: Tree, t: Fraction) -> tuple[Fraction, Fraction]:
    if tree is None:
        return Fraction(1), Fraction(1)
    left, right = tree
    a, b = size(left), size(right)
    xl, yl = endpoint_values(left, t)
    xr, yr = endpoint_values(right, t)
    return max((1 + b * t) * xl, xr), max(yl, (1 + a * t) * yr)


def tree_census() -> tuple[int, Decimal]:
    checks = 0
    minimum = Decimal("Infinity")
    activities = (Fraction(1, 16), Fraction(1, 7), Fraction(1, 3), Fraction(1, 2), Fraction(1))
    for n in range(1, 11):
        for tree in trees(n):
            for t in activities:
                x, y = endpoint_values(tree, t)
                lhs = log2_decimal(Decimal(x.numerator) / Decimal(x.denominator))
                lhs += log2_decimal(Decimal(y.numerator) / Decimal(y.denominator))
                td = Decimal(t.numerator) / Decimal(t.denominator)
                rhs = phi(log2_decimal(1 + Decimal(n) * td))
                slack = lhs - rhs
                assert slack >= Decimal("-1e-75")
                minimum = min(minimum, slack)
                checks += 1
    return checks, minimum


def rank_barrier() -> tuple[int, Decimal]:
    checks = 0
    minimum = Decimal("Infinity")
    for k in range(8, 129):
        n = 4**k
        d = (k - 1) // 2
        q = (n - 1) // d
        assert 1 + d * q <= n
        assert d < k
        t = Decimal(2) ** Decimal(-k)
        weighted = Decimal(d) * log2_decimal(1 + Decimal(q) * t)
        floor = Decimal(k * k) / 2 - Decimal(k) * log2_decimal(Decimal(k)) - 2 * Decimal(k)
        slack = weighted - floor
        assert slack >= 0
        minimum = min(minimum, slack)
        # (1+qz)^d has no coefficient above degree d.
        coefficient_k = 0 if k > d else None
        assert coefficient_k == 0
        checks += 1
    return checks, minimum


def main() -> None:
    scalar_checks, scalar_minimum = scalar_grid()
    tree_checks, tree_minimum = tree_census()
    barrier_checks, barrier_minimum = rank_barrier()
    print(
        "PASS: weighted endpoint tilt and rank-extraction barrier; "
        f"scalar={scalar_checks} min={scalar_minimum}; "
        f"trees={tree_checks} min={tree_minimum}; "
        f"barrier={barrier_checks} min={barrier_minimum}"
    )


if __name__ == "__main__":
    main()
