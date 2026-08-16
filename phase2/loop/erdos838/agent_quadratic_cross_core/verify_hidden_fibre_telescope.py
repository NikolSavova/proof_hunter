#!/usr/bin/env python3
"""Finite audit for the balanced hidden-fibre entropy/Cauchy telescope."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import ceil, comb, log2


def entropy(weights: list[int]) -> float:
    total = sum(weights)
    if total == 0:
        return 0.0
    return log2(total) - sum(w * log2(w) for w in weights if w) / total


def support_statistics(edges: frozenset[tuple[int, int]], left_n: int, right_n: int) -> tuple[float, float, float]:
    degree_l = [0] * left_n
    degree_r = [0] * right_n
    for x, y in edges:
        degree_l[x] += 1
        degree_r[y] += 1
    total = len(edges)
    h_l = entropy(degree_l)
    h_r = entropy(degree_r)
    mutual = h_l + h_r - log2(total)

    # Product-marginal support probability, exactly as a rational.
    support_num = sum(degree_l[x] * degree_r[y] for x, y in edges)
    support_q = Fraction(support_num, total * total)

    # Weighted C4 probability numerator.  Sample two right endpoints from
    # their edge marginals and two left endpoints from theirs.
    c4_num = 0
    for x1, x2, y1, y2 in product(range(left_n), range(left_n), range(right_n), range(right_n)):
        if all((x, y) in edges for x, y in ((x1, y1), (x1, y2), (x2, y1), (x2, y2))):
            c4_num += degree_l[x1] * degree_l[x2] * degree_r[y1] * degree_r[y2]
    c4 = Fraction(c4_num, total**8)
    # Marginal sampling has denominator total in each of four draws.
    c4 = Fraction(c4_num, total**4)
    assert float(support_q) + 1e-12 >= 2.0 ** (-mutual)
    assert c4 >= support_q**4
    return mutual, float(support_q), float(c4)


def entropy_c4_audit() -> dict[str, int]:
    checked = 0
    for left_n, right_n in ((2, 2), (2, 3), (3, 3)):
        universe = tuple(product(range(left_n), range(right_n)))
        for mask in range(1, 1 << len(universe)):
            edges = frozenset(universe[i] for i in range(len(universe)) if (mask >> i) & 1)
            support_statistics(edges, left_n, right_n)
            checked += 1
    return {"nonempty_bipartite_supports": checked}


def density_split_audit() -> dict[str, int]:
    # Exhaust small injective hidden families represented as binary words;
    # splitting the word in half is the canonical boundary-rank split.
    checked = 0
    for q in range(2, 7):
        ql = q // 2
        words = tuple(product((0, 1), repeat=q))
        for size in range(1, min(len(words), 7) + 1):
            # Deterministic sample of families; exhaustive through q=4.
            fams = combinations(words, size)
            limit = comb(len(words), size) if q <= 4 else min(800, comb(len(words), size))
            for idx, fam in enumerate(fams):
                if idx >= limit:
                    break
                family = tuple(fam)
                left_counts: dict[tuple[int, ...], int] = {}
                right_counts: dict[tuple[int, ...], int] = {}
                for word in family:
                    left_counts[word[:ql]] = left_counts.get(word[:ql], 0) + 1
                    right_counts[word[ql:]] = right_counts.get(word[ql:], 0) + 1
                h_l = entropy(list(left_counts.values()))
                h_r = entropy(list(right_counts.values()))
                mutual = h_l + h_r - log2(size)
                assert mutual >= -1e-10
                # With zeta=I/q, the nonsurplus implication is equality at
                # the information step and the support bound follows.
                edges = frozenset((word[:ql], word[ql:]) for word in family)
                prod_mass = sum(left_counts[l] * right_counts[r] for l, r in edges) / (size * size)
                assert prod_mass + 1e-12 >= 2.0 ** (-mutual)
                checked += 1
    return {"canonical_split_families": checked}


def product_and_depth_audit() -> dict[str, int]:
    product_rows = 0
    for q in range(2, 41):
        for m in range(2, 65):
            sources = m**q
            two_ended = comb(m, 2) ** 2 * m ** (q - 2)
            assert Fraction(two_ended, sources) == Fraction((m - 1) ** 2, 4)
            product_rows += 1

    depth_rows = 0
    for r in range(2, 4097):
        depth = ceil(log2(r))
        # A polynomial r^C loss per balanced level has O(log^2 r) bits.
        for c in (1, 2, 5, 10):
            loss_bits = c * depth * log2(r)
            assert loss_bits <= c * (log2(r) + 1) * log2(r) + 1e-12
            depth_rows += 1
    return {"two_ended_product_rows": product_rows, "balanced_depth_rows": depth_rows}


def main() -> None:
    print("WEIGHTED_C4", entropy_c4_audit())
    print("BALANCED_SPLIT", density_split_audit())
    print("PRODUCT_AND_DEPTH", product_and_depth_audit())
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
