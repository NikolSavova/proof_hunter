#!/usr/bin/env python3
"""Exact finite checks for the guarded-template regularization obstruction."""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations, permutations
from math import comb, log2


Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    assert value != 0
    return 1 if value > 0 else -1


GUARD: tuple[Point, ...] = (
    (-10, -13),
    (-6, 5),
    (-2, -13),
    (1, -10),
    (14, -10),
    (18, 2),
)


def guard_sign(i: int, j: int, k: int) -> int:
    return orient(GUARD[i], GUARD[j], GUARD[k])


@lru_cache(maxsize=None)
def pascal_paths(m: int, i: int) -> tuple[str, ...]:
    """Leaf addresses of T_(m,i), in increasing x-order."""
    if i == 0 or i == m:
        return ("",)
    return tuple("L" + p for p in pascal_paths(m - 1, i - 1)) + tuple(
        "R" + p for p in pascal_paths(m - 1, i)
    )


def pascal_sign(paths: tuple[str, ...], i: int, j: int, k: int) -> int:
    """Orientation in the recursively strong-glued Pascal cell."""
    a, b, c = paths[i], paths[j], paths[k]
    depth = 0
    while True:
        letters = {a[depth], b[depth], c[depth]}
        if len(letters) > 1:
            # Ordered binary glue: L,L,R has sign -, and L,R,R has sign +.
            return -1 if a[depth] == b[depth] else 1
        depth += 1


def guarded_sign(paths: tuple[str, ...], i: int, j: int, k: int) -> int:
    """Sign in G[T,1,1,1,1,1], with T inflated at guard position zero."""
    n = len(paths)
    blocks = tuple(0 if x < n else x - n + 1 for x in (i, j, k))
    if blocks == (0, 0, 0):
        return pascal_sign(paths, i, j, k)
    if blocks[0] == blocks[1]:
        return -1
    if blocks[1] == blocks[2]:
        return 1
    return guard_sign(*blocks)


def longest_chain(n: int, sign, target: int) -> int:
    """Largest x-monotone cap (-) or cup (+), using the standard edge DP."""
    if n <= 2:
        return n
    dp = [[2] * n for _ in range(n)]
    answer = 2
    for k in range(n):
        for j in range(k):
            best = 2
            for i in range(j):
                if sign(i, j, k) == target:
                    best = max(best, dp[i][j] + 1)
            dp[j][k] = best
            answer = max(answer, best)
    return answer


def valid_top_split(n: int, sign, cut: int) -> bool:
    r"""Whether positions [0,cut) \prec [cut,n) satisfy all mixed signs."""
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if j < cut <= k and sign(i, j, k) != -1:
                    return False
                if i < cut <= j and sign(i, j, k) != 1:
                    return False
    return True


def decomposable_in_order(order: tuple[int, ...], sign) -> bool:
    """Recursive strong decomposition for one proposed leaf order."""
    if len(order) <= 1:
        return True

    def restricted_sign(i: int, j: int, k: int) -> int:
        return sign(order[i], order[j], order[k])

    for cut in range(1, len(order)):
        if valid_top_split(len(order), restricted_sign, cut):
            if decomposable_in_order(order[:cut], sign) and decomposable_in_order(order[cut:], sign):
                return True
    return False


def check_guard() -> None:
    census = []
    for size in range(1, 7):
        ordered = good_orders = good_subsets = 0
        for subset in combinations(range(6), size):
            subset_good = False
            for order in permutations(subset):
                ordered += 1
                if decomposable_in_order(order, guard_sign):
                    good_orders += 1
                    subset_good = True
            good_subsets += int(subset_good)
        census.append((size, ordered, good_orders, good_subsets))
    assert census == [
        (1, 6, 6, 6),
        (2, 30, 30, 15),
        (3, 120, 120, 20),
        (4, 360, 150, 15),
        (5, 720, 50, 6),
        (6, 720, 0, 0),
    ]
    print("guard recursive-order census:", census, "indecomposable: PASS")


def check_k(k: int) -> None:
    m, index = 2 * k - 4, k - 2
    paths = pascal_paths(m, index)
    base_n = len(paths)
    assert base_n == comb(m, index)
    psign = lambda i, j, ell: pascal_sign(paths, i, j, ell)
    base_cap = longest_chain(base_n, psign, -1)
    base_cup = longest_chain(base_n, psign, 1)
    assert (base_cap, base_cup) == (k - 1, k - 1)

    total = base_n + 5
    ssign = lambda i, j, ell: guarded_sign(paths, i, j, ell)
    cap = longest_chain(total, ssign, -1)
    cup = longest_chain(total, ssign, 1)
    expected_cup = max(k - 1, 4)
    assert cap == k + 1 and cup == expected_cup

    coefficient_bound = (k - 1) / log2(total) if k >= 5 else (cap + cup - 2) / (2 * log2(total))
    extraction_exponent = log2(total - 1) / log2(total)
    print(
        f"k={k:2d} |P_k|={base_n:5d} |S_k|={total:5d} "
        f"(a,b)=({cap},{cup}) coeff_exact={(cap + cup - 2)/(2*log2(total)):.8f} "
        f"coeff_bound={coefficient_bound:.8f} alpha={extraction_exponent:.10f} PASS"
    )


if __name__ == "__main__":
    check_guard()
    # k=7 already has 252 Pascal points; the O(n^3) exact DP remains quick.
    for parameter in range(3, 8):
        check_k(parameter)
