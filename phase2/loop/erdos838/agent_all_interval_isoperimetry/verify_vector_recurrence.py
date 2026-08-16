#!/usr/bin/env python3
"""Exact checks for the tangent-vector spend/reset theorem and gadgets."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (
        b[1] - a[1]
    ) * (c[0] - a[0])


def hull(points):
    pts = sorted(points)
    lower = []
    for p in pts:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def is_convex(points):
    return len(hull(points)) == len(points)


def tangent(neighbor_u, neighbor_v):
    return (
        neighbor_u[0] / neighbor_u[1],
        (neighbor_v[0] - 1) / neighbor_v[1],
    )


def compatible(upper_type, lower_type):
    return upper_type[0] > lower_type[0] and upper_type[1] < lower_type[1]


def audit_weighted_partition():
    # Exhaust all 0/1/2 weight arrays on a 2 by 2 tangent grid on each side.
    cells = list(product(range(2), repeat=2))
    checked = 0
    for alpha in product(range(3), repeat=len(cells)):
        if not any(alpha):
            continue
        for beta in product(range(3), repeat=len(cells)):
            if not any(beta):
                continue
            good = left = right = 0
            for x, ax in zip(cells, alpha):
                for y, by in zip(cells, beta):
                    w = ax * by
                    if x[0] > y[0] and x[1] < y[1]:
                        good += w
                    elif x[0] <= y[0]:
                        left += w
                    else:
                        assert x[1] >= y[1]
                        right += w
            total = sum(alpha) * sum(beta)
            assert total == good + left + right
            assert max(good, left, right) * 3 >= total
            checked += 1
    return checked


def audit_rational_gadget(q=8, s=4):
    u = (F(0), F(0))
    v = (F(1), F(0))

    au = (F(1, 4), F(3, 16))
    av = (F(3, 4), F(3, 16))
    xs = [F(1, 4) + F(i + 1, q + 1) * F(1, 2) for i in range(q)]
    upper_optional = [(x, x * (1 - x)) for x in xs]

    bu = (F(-3), F(-1))
    bv = (F(4), F(-1))
    xb = [F(-3) + F(i + 1, q + 1) * 7 for i in range(q)]
    bad_optional = [(x, (x - F(1, 2)) ** 2 - F(53, 4)) for x in xb]

    gu = (F(1, 4), F(-3, 16))
    gv = (F(3, 4), F(-3, 16))
    good_optional = [(x, -x * (1 - x)) for x in xs]

    upper_type = tangent(au, av)
    bad_type = tangent(bu, bv)
    good_type = tangent(gu, gv)
    assert upper_type == (F(4, 3), F(-4, 3))
    assert bad_type == (F(3), F(-3))
    assert good_type == (F(-4, 3), F(4, 3))
    assert not compatible(upper_type, bad_type)
    assert compatible(upper_type, good_type)

    uppers = list(combinations(upper_optional, s))
    bads = list(combinations(bad_optional, s))
    goods = list(combinations(good_optional, s))
    assert len(uppers) == len(bads) == len(goods)

    for chain in uppers:
        assert is_convex([u, v, au, av, *chain])
    for chain in bads:
        assert is_convex([u, v, bu, bv, *chain])
    for chain in goods:
        assert is_convex([u, v, gu, gv, *chain])

    incompatible_pairs = compatible_pairs = 0
    for upper in uppers:
        for bad in bads:
            assert not is_convex([u, v, au, av, bu, bv, *upper, *bad])
            incompatible_pairs += 1
        for good in goods:
            assert is_convex([u, v, au, av, gu, gv, *upper, *good])
            compatible_pairs += 1

    M = len(uppers)
    assert incompatible_pairs == compatible_pairs == M * M
    return M, incompatible_pairs


def audit_nested_acp_gadget(q=8):
    u = (F(0), F(0))
    v = (F(1), F(0))
    # A fixed upper rooted chain R.
    R = [
        u,
        v,
        (F(1, 4), F(3, 16)),
        (F(1, 2), F(1, 4)),
        (F(3, 4), F(3, 16)),
    ]
    denominator = 100 * q * q
    Z = [
        (F(1, 2) + F(j * j, denominator), -F(1 << (j + 1)))
        for j in range(q)
    ]
    for z in Z:
        assert is_convex([*R, z])

    records = 0
    for i in range(q):
        for j in range(i + 1, q):
            # z_j is outward from z_i at the terminal prefix vertex u.
            assert orient(u, Z[i], Z[j]) < 0
            h = hull([*R, Z[i], Z[j]])
            # The outer successor z_j survives and hides exactly z_i.
            assert Z[j] in h and Z[i] not in h
            assert set(h) == set([*R, Z[j]])
            records += 1

    # No alternative successor is addable to a source R+z_i.
    for i in range(q):
        for j in range(q):
            if i == j:
                continue
            assert not is_convex([*R, Z[i], Z[j]])
    assert records == q * (q - 1) // 2
    return records


def audit_quadratic_hidden_entropy():
    checked = 0
    for r in (32, 48, 64, 96):
        # alpha=1/2, beta=1/2, so alpha>beta/2.
        b = r // 2
        log_m = r // 2
        M = 1 << log_m
        sources = M**b
        records = sources * M
        down = (M + 1) ** b
        two_ended = comb(M, 2) ** 2 * M ** (b - 2)
        assert records == M ** (b + 1)
        assert two_ended >= records
        # Absolute coefficient-1/2 exponent is below known source entropy.
        # Ignore the lower-order log b term exactly as in (50)--(51).
        assert 2 * b * log_m > log_m * log_m
        # Thinning/down-closure misses the blocker factor.
        assert down < records
        checked += 1
    return checked


def main():
    arrays = audit_weighted_partition()
    M, pairs = audit_rational_gadget()
    nested = audit_nested_acp_gadget()
    hidden = audit_quadratic_hidden_entropy()
    print(f"weighted tangent partitions checked: {arrays} PASS")
    print(f"rational fixed-cell families: M={M}, cross pairs={pairs} PASS")
    print(f"ACP nested successor records: {nested} PASS")
    print(f"quadratic hidden-entropy regimes: {hidden} PASS")
    print("ALL VECTOR RECURRENCE CHECKS PASS")


if __name__ == "__main__":
    main()
