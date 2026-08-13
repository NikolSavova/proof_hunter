#!/usr/bin/env python3
"""Exact tests of global hinged-history versus convex-subset counts.

The main test uses only orientation tables.  It also implements the exact
hinged-profile substitution rule for the directional composition S[Q].
All counting is integer; floating point is used only to print logarithms.
"""

from __future__ import annotations

from itertools import combinations, product
from math import comb, factorial, log2


def pascal_leaves(m: int, i: int, prefix: tuple[int, ...] = ()) -> list[tuple[int, ...]]:
    if i == 0 or i == m:
        return [prefix]
    return (pascal_leaves(m - 1, i - 1, prefix + (0,))
            + pascal_leaves(m - 1, i, prefix + (1,)))


def pascal_sign(a: tuple[int, ...], b: tuple[int, ...], c: tuple[int, ...]) -> int:
    common = 0
    while a[common] == b[common] == c[common]:
        common += 1
    if a[common] == b[common]:
        return -1
    assert b[common] == c[common]
    return 1


def orientation_table(m: int) -> list[list[list[int]]]:
    leaves = pascal_leaves(m, m // 2)
    n = len(leaves)
    table = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i, j, k in combinations(range(n), 3):
        table[i][j][k] = pascal_sign(leaves[i], leaves[j], leaves[k])
    return table


def monochromatic(vertices: tuple[int, ...], sign: int,
                  table: list[list[list[int]]]) -> bool:
    return all(table[i][j][k] == sign for i, j, k in combinations(vertices, 3))


def hinged(vertices: tuple[int, ...], table: list[list[list[int]]]) -> bool:
    return all(
        len({table[vertices[i]][vertices[i + 1]][vertices[j]]
             for j in range(i + 2, len(vertices))}) == 1
        for i in range(len(vertices) - 2)
    )


def convex(vertices: tuple[int, ...], table: list[list[list[int]]]) -> bool:
    if len(vertices) <= 2:
        return True
    first, last = vertices[0], vertices[-1]
    middle = vertices[1:-1]
    for mask in range(1 << len(middle)):
        cap = (first,) + tuple(middle[i] for i in range(len(middle)) if mask >> i & 1) + (last,)
        cup = (first,) + tuple(middle[i] for i in range(len(middle)) if not (mask >> i & 1)) + (last,)
        if monochromatic(cap, -1, table) and monochromatic(cup, 1, table):
            return True
    return False


def profiles(table: list[list[list[int]]]) -> tuple[list[int], list[int], list[int], list[int]]:
    n = len(table)
    caps = [0] * (n + 1)
    cups = [0] * (n + 1)
    convex_sets = [0] * (n + 1)
    histories = [0] * (n + 1)
    for size in range(1, n + 1):
        for subset in combinations(range(n), size):
            caps[size] += monochromatic(subset, -1, table)
            cups[size] += monochromatic(subset, 1, table)
            convex_sets[size] += convex(subset, table)
            histories[size] += hinged(subset, table)
    return caps, cups, convex_sets, histories


def direct_depth_two_history_prefix(table: list[list[list[int]]], cutoff: int) -> list[int]:
    """Direct orientation census in S[S] for small subset sizes."""
    r = len(table)

    def sign(i: int, j: int, k: int) -> int:
        ai, bi = divmod(i, r)
        aj, bj = divmod(j, r)
        ak, bk = divmod(k, r)
        if ai == aj == ak:
            return table[bi][bj][bk]
        if ai == aj:
            return -1
        if aj == ak:
            return 1
        return table[ai][aj][ak]

    result = [0] * (cutoff + 1)
    for size in range(1, cutoff + 1):
        for subset in combinations(range(r * r), size):
            if all(
                len({sign(subset[i], subset[i + 1], subset[j])
                     for j in range(i + 2, size)}) == 1
                for i in range(size - 2)
            ):
                result[size] += 1
    return result


def add(a: list[int], b: list[int], cutoff: int) -> list[int]:
    return [a[i] + b[i] for i in range(cutoff + 1)]


def multiply(a: list[int], b: list[int], cutoff: int) -> list[int]:
    out = [0] * (cutoff + 1)
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b[:cutoff + 1 - i]):
            if bj:
                out[i + j] += ai * bj
    return out


def power(a: list[int], exponent: int, cutoff: int) -> list[int]:
    out = [1] + [0] * cutoff
    for _ in range(exponent):
        out = multiply(out, a, cutoff)
    return out


def acceptable_macro_types(subset: tuple[int, ...], multiple: tuple[bool, ...],
                           table: list[list[list[int]]]) -> bool:
    """Check macro hinges; multiple[t] records size >=2 in occupied block t."""
    for pos in range(len(subset) - 2):
        signs = {table[subset[pos]][subset[pos + 1]][subset[later]]
                 for later in range(pos + 2, len(subset))}
        if multiple[pos + 1]:
            if signs != {1}:
                return False
        elif len(signs) != 1:
            return False
    return True


def compose_history_profile(
    table: list[list[list[int]]],
    cap_profile: list[int],
    history_profile: list[int],
    point_count: int,
    cutoff: int,
) -> list[int]:
    """Exact q-profile of hinged subsets in S[Q], truncated at cutoff.

    A nonfinal occupied block is a cap of Q.  The final occupied block is a
    hinged subset of Q.  If an occupied block after a macro hinge has at
    least two selected points, its internal future point forces that hinge
    and every later macro point to have positive sign.
    """
    r = len(table)
    single = [0] * (cutoff + 1)
    single[1] = point_count
    cap_many = cap_profile[:cutoff + 1]
    hist_many = history_profile[:cutoff + 1]
    cap_many[1] -= point_count
    hist_many[1] -= point_count
    out = [0] * (cutoff + 1)
    for occupied_count in range(1, min(r, cutoff) + 1):
        for subset in combinations(range(r), occupied_count):
            for multiple in product((False, True), repeat=occupied_count):
                if not acceptable_macro_types(subset, multiple, table):
                    continue
                term = [1] + [0] * cutoff
                for pos in range(occupied_count - 1):
                    term = multiply(term, cap_many if multiple[pos] else single, cutoff)
                term = multiply(term, hist_many if multiple[-1] else single, cutoff)
                out = add(out, term, cutoff)
    return out


def compose_cap_profile(template_cap: list[int], cap_profile: list[int],
                        point_count: int, cutoff: int) -> list[int]:
    # A macro cap with j blocks: first block is an arbitrary cap; the other
    # j-1 blocks are singletons.
    out = [0] * (cutoff + 1)
    for j, number in enumerate(template_cap):
        if not number:
            continue
        shift = j - 1
        for size, count in enumerate(cap_profile):
            target = size + shift
            if target <= cutoff:
                out[target] += number * count * point_count ** shift
    return out


def compose_total_convex(template_convex: list[int], point_count: int,
                         block_count: int, cap_total: int, cup_total: int,
                         convex_total: int) -> int:
    macro = sum(template_convex[j] * point_count ** (j - 2)
                for j in range(2, len(template_convex)))
    return block_count * convex_total + cap_total * cup_total * macro


def cap_spine_monomial(depth: int, size: int) -> int:
    """One explicit monomial lower bound for c_{depth,size}(Q_depth)."""
    degree_one_factors = size - 1
    assert 0 <= degree_one_factors <= depth
    # c_d(z)=z product_{ell=0}^{d-1}(6+15*6^ell*z+10*6^(2ell)*z^2).
    # Select degree one in the latest size-1 factors and degree zero before.
    return (6 ** (depth - degree_one_factors)
            * 15 ** degree_one_factors
            * 6 ** sum(range(depth - degree_one_factors, depth)))


def explicit_spine_lower(depth: int, q: int) -> int:
    """Explicit history family: sqrt(depth) cap branches along one spine."""
    branches = max(1, int(depth ** 0.5))
    quotient, remainder = divmod(q - 1, branches)
    sizes = [quotient + (i < remainder) for i in range(branches)]
    assert all(size >= 2 and size - 1 <= depth - i - 1
               for i, size in enumerate(sizes))
    total = 6 ** (depth - branches)  # terminal singleton
    for i, size in enumerate(sizes):
        total *= cap_spine_monomial(depth - i - 1, size)
    return total


def endpoint_history_test(table: list[list[list[int]]], histories: list[int]) -> None:
    n = len(table)
    red = [[0] * n for _ in range(n)]
    blue = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in range(u + 1, n):
            red[u][v] = 1 + sum(red[t][u] for t in range(u) if table[t][u][v] == 1)
            blue[u][v] = 1 + sum(blue[t][u] for t in range(u) if table[t][u][v] == -1)
    # This tempting expression is a split-path-pair count, not the number of
    # convex subsets.  T_{4,2} is the exact six-point counterexample 44 != 50.
    split_path_pairs = n + sum(red[u][v] * blue[u][v]
                               for u in range(n) for v in range(u + 1, n))
    convex_total = sum(profiles(table)[2])
    if n == 6:
        assert split_path_pairs == 44 and convex_total == 50
    for q in range(3, n + 1):
        ending = [[0] * n for _ in range(n)]
        for subset in combinations(range(n), q):
            if hinged(subset, table):
                ending[subset[-2]][subset[-1]] += 1
        assert sum(map(sum, ending)) == histories[q]
        # Empirical candidate, deliberately asserted only for audited tables.
        assert all(ending[u][v] <= factorial(q) * red[u][v] * blue[u][v]
                   for u in range(n) for v in range(u + 1, n))


def main() -> None:
    cutoff = 100
    for m, max_depth in ((4, 25),):
        table = orientation_table(m)
        tc, tu, tv, th = profiles(table)
        endpoint_history_test(table, th)
        r = len(table)
        cap = tc + [0] * (cutoff + 1 - len(tc))
        cup = tu + [0] * (cutoff + 1 - len(tu))
        hist = th + [0] * (cutoff + 1 - len(th))
        points = r
        cap_total, cup_total, convex_total = sum(tc), sum(tu), sum(tv)
        direct_prefix = direct_depth_two_history_prefix(table, 5)
        predicted_prefix = compose_history_profile(table, cap, hist, r, 5)
        assert direct_prefix == predicted_prefix
        print(f"central Pascal template m={m}, r={r}")
        for depth in range(1, max_depth + 1):
            if depth > 1:
                old_cap_total, old_cup_total = cap_total, cup_total
                hist = compose_history_profile(table, cap, hist, points, cutoff)
                cap = compose_cap_profile(tc, cap, points, cutoff)
                cup = compose_cap_profile(tu, cup, points, cutoff)
                convex_total = compose_total_convex(
                    tv, points, r, old_cap_total, old_cup_total, convex_total
                )
                cap_total = old_cap_total * sum(tc[j] * points ** (j - 1)
                                                for j in range(1, len(tc)))
                cup_total = old_cup_total * sum(tu[j] * points ** (j - 1)
                                                for j in range(1, len(tu)))
                points *= r
            q = min(cutoff, round(log2(points)))
            ratio = hist[q] / convex_total
            print(
                f"  depth={depth} n={points} q={q} "
                f"logH={log2(hist[q]):.6f} logV={log2(convex_total):.6f} "
                f"log(H/V)={log2(ratio):.6f}"
            )
            # The formerly tempting q! fibre estimate is already false at
            # depth 18.  Record its first failure; this does not by itself
            # refute a bound with an arbitrary constant in O(q log q).
            factorial_bound = log2(factorial(q))
            status = "FAIL" if log2(ratio) > factorial_bound else "pass"
            print(f"    q! comparison: {status}; log2(q!)={factorial_bound:.6f}")
            floor_q = int(log2(points))
            if depth >= 9:
                spine = explicit_spine_lower(depth, floor_q)
                assert hist[floor_q] >= spine
                print(
                    f"    explicit sqrt(d)-spine at q={floor_q}: "
                    f"log lower={log2(spine):.6f}"
                )
    print("all global-history tests: PASS")


if __name__ == "__main__":
    main()
