#!/usr/bin/env python3
"""Exact checks for the uniform growing-rank caterpillar theorem."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb


Tree = None | tuple["Tree", "Tree"]


@lru_cache(None)
def size(tree: Tree) -> int:
    if tree is None:
        return 1
    return size(tree[0]) + size(tree[1])


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
def rooted(tree: Tree) -> tuple[int, ...]:
    n = size(tree)
    if tree is None:
        return (0, 1)
    left, right = tree
    a, b = size(left), size(right)
    rl, rr = rooted(left), rooted(right)
    out = [0] * (n + 1)
    out[1] = n
    out[2] = comb(n, 2)
    for k in range(3, n + 1):
        out[k] = (rl[k] if k < len(rl) else 0) + (
            rr[k] if k < len(rr) else 0
        )
        out[k] += a * (rr[k - 1] if k - 1 < len(rr) else 0)
        out[k] += b * (rl[k - 1] if k - 1 < len(rl) else 0)
    return tuple(out)


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    length = max(len(left), len(right))
    return tuple(
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(length)
    )


def convolve(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return tuple(out)


@lru_cache(None)
def ordinary_profiles(
    tree: Tree,
) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    if tree is None:
        base = (0, 1)
        return base, base, base
    left, right = tree
    a, b = size(left), size(right)
    cl, ul, vl = ordinary_profiles(left)
    cr, ur, vr = ordinary_profiles(right)
    cap = list(add(cl, cr)) + [0]
    cup = list(add(ul, ur)) + [0]
    for rank, value in enumerate(cl):
        if rank + 1 >= len(cap):
            cap.append(0)
        cap[rank + 1] += b * value
    for rank, value in enumerate(ur):
        if rank + 1 >= len(cup):
            cup.append(0)
        cup[rank + 1] += a * value
    face = add(add(vl, vr), convolve(cl, ur))
    return tuple(cap), tuple(cup), face


def annotated(tree: Tree, start: int = 0):
    if tree is None:
        return (start, start + 1, 1, None, None), start + 1
    left, cursor = annotated(tree[0], start)
    right, cursor = annotated(tree[1], cursor)
    return (start, cursor, cursor - start, left, right), cursor


def endpoint_blocks(node, x: int, y: int) -> tuple[int, ...]:
    _, _, _, left, right = node
    assert left is not None and right is not None
    if x < left[1] <= y:
        blocks = []
        current = left
        while current[2] > 1:
            child_left, child_right = current[3], current[4]
            assert child_left is not None and child_right is not None
            if x < child_left[1]:
                blocks.append(child_right[2])
                current = child_left
            else:
                current = child_right
        current = right
        while current[2] > 1:
            child_left, child_right = current[3], current[4]
            assert child_left is not None and child_right is not None
            if y >= child_right[0]:
                blocks.append(child_left[2])
                current = child_right
            else:
                current = child_left
        return tuple(blocks)
    if y < left[1]:
        return endpoint_blocks(left, x, y)
    return endpoint_blocks(right, x, y)


def elementary(values: tuple[int, ...], rank: int) -> int:
    profile = [1] + [0] * rank
    for value in values:
        for j in range(rank, 0, -1):
            profile[j] += value * profile[j - 1]
    return profile[rank]


def b_constant(k: int) -> Fraction:
    value = Fraction(1, 2)
    for j in range(2, k):
        value /= 2**j - 1
    return value


def shifted_bound(n: int, k: int) -> Fraction:
    return b_constant(k) * max(0, n - 2 ** (k - 2)) ** k


def audit_trees() -> int:
    checks = 0
    for n in range(1, 12):
        for tree in trees(n):
            values = rooted(tree)
            if tree is not None:
                left, right = tree
                a, b = size(left), size(right)
                rl, rr = rooted(left), rooted(right)
                for k in range(3, n + 1):
                    recurrence = (rl[k] if k < len(rl) else 0) + (
                        rr[k] if k < len(rr) else 0
                    )
                    recurrence += a * (
                        rr[k - 1] if k - 1 < len(rr) else 0
                    )
                    recurrence += b * (
                        rl[k - 1] if k - 1 < len(rl) else 0
                    )
                    assert values[k] == recurrence
                    checks += 1
            for k in range(2, n + 1):
                assert Fraction(values[k], 1) >= shifted_bound(n, k)
                checks += 1
    return checks


def audit_split_inequality() -> int:
    checks = 0
    for k in range(3, 50):
        coefficient = 2 ** (k - 1) - 1

        # The AM--GM coefficients of the two endpoint monomials are exact.
        left_numerator = sum(
            comb(k, j) * (k - 1 - j) for j in range(1, k)
        )
        right_numerator = sum(
            comb(k, j) * (j - 1) for j in range(1, k)
        )
        assert left_numerator == (k - 2) * coefficient
        assert right_numerator == (k - 2) * coefficient

        # Exact rational grid regression for the resulting homogeneous form.
        for x in range(0, 31):
            for y in range(0, 31):
                lhs = x**k + y**k + coefficient * (
                    x * y ** (k - 1) + y * x ** (k - 1)
                )
                assert lhs >= (x + y) ** k
                checks += 1
    return checks


def audit_small_child_case() -> int:
    checks = 0
    for k in range(3, 30):
        ratio = 2 ** (k - 1) - 1
        assert ratio >= k
        for x in range(0, 80):
            for a in range(0, 40):
                loss = x**k - max(0, x - a) ** k
                assert loss <= k * a * x ** (k - 1)
                assert loss <= ratio * a * x ** (k - 1)
                checks += 1
    return checks


def audit_endpoint_formula() -> int:
    checks = 0
    for n in range(2, 10):
        for tree in trees(n):
            node, cursor = annotated(tree)
            assert cursor == n
            face = ordinary_profiles(tree)[2]
            for k in range(2, n + 1):
                endpoint_sum = sum(
                    elementary(endpoint_blocks(node, x, y), k - 2)
                    for x in range(n)
                    for y in range(x + 1, n)
                )
                expected = face[k] if k < len(face) else 0
                assert endpoint_sum == expected
                checks += 1
    return checks


def alternating_comb(n: int) -> Tree:
    """A comb whose successive attachment sides alternate."""
    tree: Tree = None
    for step in range(1, n):
        tree = (None, tree) if step % 2 else (tree, None)
    return tree


def audit_plane_shifted_candidate() -> tuple[int, int, int]:
    """Exhaust the tempting plane bound, then certify its first saved kill."""
    checks = 0
    for n in range(2, 14):
        for tree in trees(n):
            face = ordinary_profiles(tree)[2]
            for k in range(2, n + 1):
                value = face[k] if k < len(face) else 0
                assert Fraction(value, 1) >= shifted_bound(n, k)
                checks += 1

    tree = alternating_comb(256)
    value = ordinary_profiles(tree)[2][4]
    bound = shifted_bound(256, 4)
    assert value == 86_709_504
    assert bound == 96_018_048
    assert Fraction(value, 1) < bound
    return checks, value, int(bound)


def audit_canonical_scale() -> list[tuple[int, Fraction, int]]:
    rows = []
    for k in (4, 8, 16, 24, 32):
        n = 4**k
        exact = shifted_bound(n, k)
        coarse = Fraction(2 ** ((3 * k * k) // 2), 2 ** (2 * k))
        assert exact >= coarse
        rows.append((k, exact, exact.numerator.bit_length() - exact.denominator.bit_length()))
    return rows


def main() -> None:
    tree_checks = audit_trees()
    split_checks = audit_split_inequality()
    child_checks = audit_small_child_case()
    endpoint_checks = audit_endpoint_formula()
    plane_checks, plane_value, plane_bound = audit_plane_shifted_candidate()
    rows = audit_canonical_scale()
    print(
        "PASS: uniform growing-rank rooted caterpillars; "
        f"tree_checks={tree_checks}; split_checks={split_checks}; "
        f"small_child_checks={child_checks}; endpoint_checks={endpoint_checks}; "
        f"plane_candidate_checks={plane_checks}; "
        f"plane_kill=({plane_value},{plane_bound}); "
        f"canonical_bits={[(k, bits) for k, _, bits in rows]}"
    )


if __name__ == "__main__":
    main()
