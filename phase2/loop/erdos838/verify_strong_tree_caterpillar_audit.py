#!/usr/bin/env python3
"""Exact checks for the fixed-rank strong-tree/caterpillar audit."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import factorial, log2


Tree = None | tuple["Tree", "Tree"]


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    n = max(len(a), len(b))
    return tuple(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(n)
    )


def shift_scale(a: tuple[int, ...], scale: int) -> tuple[int, ...]:
    return (0,) + tuple(scale * x for x in a)


def convolve(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


@lru_cache(None)
def size(tree: Tree) -> int:
    if tree is None:
        return 1
    return size(tree[0]) + size(tree[1])


@lru_cache(None)
def profiles(tree: Tree) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    """Return (cap, cup, ordinary-face) rank vectors, empty rank omitted."""
    if tree is None:
        base = (0, 1)
        return base, base, base
    left, right = tree
    a, b = size(left), size(right)
    c_l, u_l, v_l = profiles(left)
    c_r, u_r, v_r = profiles(right)
    cap = add(add(c_l, c_r), shift_scale(c_l, b))
    cup = add(add(u_l, u_r), shift_scale(u_r, a))
    face = add(add(v_l, v_r), convolve(c_l, u_r))
    return cap, cup, face


@lru_cache(None)
def rooted_caterpillars(tree: Tree) -> tuple[int, ...]:
    """Unordered rooted binary-caterpillar copies by leaf rank."""
    n = size(tree)
    if tree is None:
        return (0, 1)
    left, right = tree
    a, b = size(left), size(right)
    r_l, r_r = rooted_caterpillars(left), rooted_caterpillars(right)
    out = [0] * (n + 1)
    out[1] = n
    out[2] = n * (n - 1) // 2
    for k in range(3, n + 1):
        inherited = (r_l[k] if k < len(r_l) else 0) + (
            r_r[k] if k < len(r_r) else 0
        )
        cross = a * (r_r[k - 1] if k - 1 < len(r_r) else 0)
        cross += b * (r_l[k - 1] if k - 1 < len(r_l) else 0)
        out[k] = inherited + cross
    return tuple(out)


@lru_cache(None)
def unrooted_caterpillars(tree: Tree) -> tuple[int, ...]:
    """Copies whose suppressed underlying unrooted tree is a caterpillar."""
    n = size(tree)
    if tree is None:
        return (0, 1)
    left, right = tree
    q_l, q_r = unrooted_caterpillars(left), unrooted_caterpillars(right)
    r_l, r_r = rooted_caterpillars(left), rooted_caterpillars(right)
    out = list(add(q_l, q_r)) + [0] * (n + 1 - len(add(q_l, q_r)))
    cross = convolve(r_l, r_r)
    for k in range(2, min(len(cross), n + 1)):
        out[k] += cross[k]
    return tuple(out)


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


def dossou_b(k: int) -> Fraction:
    out = Fraction(1, 2)
    for j in range(1, k):
        out /= 2**j - 1
    return out


def dossou_lower(n: int, k: int) -> Fraction:
    return dossou_b(k) * n**k - Fraction(n ** (k - 1), factorial(k - 1))


def audit_small_trees() -> tuple[int, tuple[int, int, int, int]]:
    checks = 0
    strict = None
    for n in range(1, 10):
        for tree in trees(n):
            cap, cup, face = profiles(tree)
            rooted = rooted_caterpillars(tree)
            unrooted = unrooted_caterpillars(tree)
            assert len(face) <= n + 1
            for k in range(1, n + 1):
                c = cap[k] if k < len(cap) else 0
                u = cup[k] if k < len(cup) else 0
                v = face[k] if k < len(face) else 0
                assert c <= rooted[k]
                assert u <= rooted[k]
                assert v <= unrooted[k]
                if k >= 2:
                    assert Fraction(rooted[k], 1) >= dossou_lower(n, k)
                if strict is None and unrooted[k] > v:
                    strict = (n, k, unrooted[k], v)
                checks += 1
    assert strict is not None
    return checks, strict


def audit_recurrence_identities() -> int:
    checks = 0
    for n in range(2, 10):
        for tree in trees(n):
            left, right = tree
            a, b = size(left), size(right)
            rooted = rooted_caterpillars(tree)
            rl, rr = rooted_caterpillars(left), rooted_caterpillars(right)
            for k in range(3, n + 1):
                rhs = (rl[k] if k < len(rl) else 0) + (rr[k] if k < len(rr) else 0)
                rhs += a * (rr[k - 1] if k - 1 < len(rr) else 0)
                rhs += b * (rl[k - 1] if k - 1 < len(rl) else 0)
                assert rooted[k] == rhs
                checks += 1
    return checks


def audit_canonical_scale() -> list[tuple[int, float, float]]:
    rows = []
    for k in (12, 16, 24, 32):
        n_log = 2 * k
        main_log = log2(float(dossou_b(k))) + k * n_log
        error_log = (k - 1) * n_log - log2(factorial(k - 1))
        assert error_log > main_log
        rows.append((k, main_log, error_log))
    return rows


def main() -> None:
    checks, strict = audit_small_trees()
    recurrences = audit_recurrence_identities()
    rows = audit_canonical_scale()
    print(
        "PASS: strong-tree/caterpillar audit; "
        f"tree-rank checks={checks}, recurrences={recurrences}, "
        f"strict(unrooted,face)={strict}, "
        f"canonical-error-rows={[(k, round(m, 3), round(e, 3)) for k, m, e in rows]}"
    )


if __name__ == "__main__":
    main()
