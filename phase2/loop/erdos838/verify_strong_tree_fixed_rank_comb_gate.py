#!/usr/bin/env python3
"""Exact checks for STRONG_TREE_FIXED_RANK_COMB_OR_SEAM_GATE.md."""

from __future__ import annotations

from functools import lru_cache
from itertools import product
from math import comb


def elementary(values: tuple[int, ...], rank: int) -> int:
    dp = [0] * (rank + 1)
    dp[0] = 1
    for value in values:
        for j in range(rank, 0, -1):
            dp[j] += value * dp[j - 1]
    return dp[rank]


def check_symmetric_lemma() -> int:
    rows = 0
    for length in range(1, 7):
        for values in product(range(1, 7), repeat=length):
            total = sum(values)
            for rank in range(1, length + 1):
                if max(values) * rank <= total:
                    # Avoid floating point: e_t >= (S/t)^t.
                    assert elementary(values, rank) * rank**rank >= total**rank
                    rows += 1
    return rows


Tree = tuple


@lru_cache(maxsize=None)
def trees(size: int) -> tuple[Tree, ...]:
    if size == 1:
        return (("x",),)
    out = []
    for left_size in range(1, size):
        for left in trees(left_size):
            for right in trees(size - left_size):
                out.append((left, right))
    return tuple(out)


def size(tree: Tree) -> int:
    if tree == ("x",):
        return 1
    return size(tree[0]) + size(tree[1])


def poly_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    length = max(len(a), len(b))
    return tuple(
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(length)
    )


def poly_shift_multiple(a: tuple[int, ...], factor: int) -> tuple[int, ...]:
    out = list(a) + [0]
    for i, value in enumerate(a):
        out[i + 1] += factor * value
    return tuple(out)


def poly_multiply(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


@lru_cache(maxsize=None)
def profiles(tree: Tree) -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    if tree == ("x",):
        return (0, 1), (0, 1), (0, 1)
    left, right = tree
    cap_left, cup_left, face_left = profiles(left)
    cap_right, cup_right, face_right = profiles(right)
    left_size, right_size = size(left), size(right)
    cap = poly_add(poly_shift_multiple(cap_left, right_size), cap_right)
    cup = poly_add(cup_left, poly_shift_multiple(cup_right, left_size))
    face = poly_add(
        poly_add(face_left, face_right),
        poly_multiply(cap_left, cup_right),
    )
    return cap, cup, face


def heavy_path_data(
    tree: Tree,
) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    """Return (sibling size, followed-child size) in the two orientations."""
    right_siblings = []
    left_siblings = []
    current = tree
    while current != ("x",):
        left, right = current
        left_size, right_size = size(left), size(right)
        if left_size >= right_size:
            right_siblings.append((right_size, left_size))
            current = left
        else:
            left_siblings.append((left_size, right_size))
            current = right
    return tuple(right_siblings), tuple(left_siblings)


def check_trees(max_size: int = 10) -> tuple[int, int]:
    tree_rows = 0
    dichotomy_rows = 0
    for n in range(2, max_size + 1):
        for tree in trees(n):
            cap, cup, face = profiles(tree)
            right_rows, left_rows = heavy_path_data(tree)
            right = tuple(row[0] for row in right_rows)
            left = tuple(row[0] for row in left_rows)
            assert sum(right) + sum(left) == n - 1
            assert all(sibling <= path_child for sibling, path_child in right_rows)
            assert all(sibling <= path_child for sibling, path_child in left_rows)
            for rank in range(0, len(right) + 1):
                assert cap[rank + 1] >= elementary(right, rank)
            for rank in range(0, len(left) + 1):
                assert cup[rank + 1] >= elementary(left, rank)
            tree_rows += 1

            for k in range(2, n + 1):
                rows = right_rows if sum(right) >= sum(left) else left_rows
                values = tuple(row[0] for row in rows)
                total = sum(values)
                t = k - 1
                if values and max(values) * t <= total:
                    assert face[k] * t**t >= total**t
                else:
                    # If the diffuse condition fails and the majority class
                    # is nonempty, its largest sibling and the path child at
                    # that node are both at least that sibling size.
                    if values:
                        largest = max(values)
                        assert largest * t > total
                        sibling, path_child = next(
                            row for row in rows if row[0] == largest
                        )
                        assert path_child >= sibling
                        assert sibling * 2 * t > n - 1
                dichotomy_rows += 1
    return tree_rows, dichotomy_rows


if __name__ == "__main__":
    symmetric = check_symmetric_lemma()
    tree_rows, dichotomy = check_trees()
    print(
        "PASS: strong-tree comb/seam gate; "
        f"symmetric={symmetric}, trees={tree_rows}, dichotomies={dichotomy}"
    )
