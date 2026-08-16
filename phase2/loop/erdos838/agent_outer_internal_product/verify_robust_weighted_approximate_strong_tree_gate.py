#!/usr/bin/env python3
"""Exact checks for ROBUST_WEIGHTED_APPROXIMATE_STRONG_TREE_GATE."""

from fractions import Fraction
from itertools import product
from math import log2, sqrt


def trees(n):
    if n == 1:
        return (None,)
    out = []
    for a in range(1, n):
        b = n - a
        for left in trees(a):
            for right in trees(b):
                out.append((left, right))
    return tuple(out)


def size(tree):
    if tree is None:
        return 1
    return size(tree[0]) + size(tree[1])


def exact_state(tree):
    if tree is None:
        return (Fraction(1), Fraction(1), Fraction(1))
    left, right = tree
    a, b = size(left), size(right)
    xa, ya, ma = exact_state(left)
    xb, yb, mb = exact_state(right)
    return (max(xb, (b + 1) * xa),
            max(ya, (a + 1) * yb),
            max(ma, mb, xa * yb))


def approximate_state(tree, losses, path=()):
    """Losses are seven nonnegative integer base-two exponents per node."""
    if tree is None:
        one = Fraction(1)
        return (one, one, one, 0, 0, 0, 0)
    left, right = tree
    a, b = size(left), size(right)
    xa, ya, ma, gxa, gya, gma, ha = approximate_state(
        left, losses, path + (0,))
    xb, yb, mb, gxb, gyb, gmb, hb = approximate_state(
        right, losses, path + (1,))
    lx_b, lx_a, ly_a, ly_b, lm_a, lm_b, lm_x = losses[path]

    x = max(xb / 2**lx_b, Fraction((b + 1) * xa, 2**lx_a))
    y = max(ya / 2**ly_a, Fraction((a + 1) * yb, 2**ly_b))
    m = max(ma / 2**lm_a, mb / 2**lm_b,
            xa * yb / 2**lm_x)

    gx = max(gxb + lx_b, gxa + lx_a)
    gy = max(gya + ly_a, gyb + ly_b)
    gm = max(gma + lm_a, gmb + lm_b, gxa + gyb + lm_x)

    gamma = max(lx_b, lx_a, ly_a, ly_b, lm_a, lm_b, lm_x)
    h = gamma + max(ha, hb)
    return x, y, m, gx, gy, gm, h


def node_paths(tree, path=()):
    if tree is None:
        return []
    return ([path] + node_paths(tree[0], path + (0,))
            + node_paths(tree[1], path + (1,)))


def loss_assignments(tree, seed):
    """Deterministic varied losses; exhaustive binary patterns on small trees."""
    paths = node_paths(tree)
    if len(paths) <= 2:
        for bits in product((0, 1), repeat=7 * len(paths)):
            yield {p: tuple(bits[7 * i:7 * i + 7])
                   for i, p in enumerate(paths)}
    else:
        for trial in range(12):
            yield {
                p: tuple((seed + trial + 3 * i + 5 * j + len(p)) % 4
                         for j in range(7))
                for i, p in enumerate(paths)
            }


def comparison_audit():
    checked = 0
    for n in range(1, 8):
        for seed, tree in enumerate(trees(n)):
            x0, y0, m0 = exact_state(tree)
            for losses in loss_assignments(tree, seed):
                x, y, m, gx, gy, gm, h = approximate_state(tree, losses)
                assert x * 2**gx >= x0
                assert y * 2**gy >= y0
                assert m * 2**gm >= m0
                assert gx <= h
                assert gy <= h
                assert gm <= 2 * h
                checked += 1
    return checked


def guard_audit():
    rows = []
    for b in range(2, 80):
        for g in range(0, b // 2 + 1):
            factor = Fraction(b + 1, b - g + 1)
            assert Fraction(b + 1, 1) / factor == b - g + 1
            # log2(e)=1/ln(2); the displayed bound is 2g/((b+1)ln2).
            upper = 2 * g * log2(2.718281828459045) / (b + 1)
            assert log2(float(factor)) <= upper + 1e-14
        rows.append((b, float(Fraction(b + 1, b - b // 2 + 1))))
    return rows


def threshold_audit():
    rows = []
    for delta in (0.01, 0.05, 0.1, 0.2):
        epsilon = delta / 5
        alpha = sqrt(1 - 2 * delta) + epsilon
        allowance = 0.5 * alpha**2 - (0.5 - delta)
        assert allowance > 0
        rows.append((delta, alpha, allowance))
    return rows


def main():
    checked = comparison_audit()
    guards = guard_audit()
    thresholds = threshold_audit()
    print("PASS: robust weighted approximate strong-tree gate")
    print("  exact tree/loss systems:", checked)
    print("  guard rows:", guards[-3:])
    print("  fixed-gap thresholds:",
          [(d, round(a, 6), round(g, 8)) for d, a, g in thresholds])


if __name__ == "__main__":
    main()
