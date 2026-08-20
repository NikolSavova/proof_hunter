#!/usr/bin/env python3
"""Verify the higher-pooling synchronized-parallelogram gate and barrier."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial

import verify_high_codegree_transverse_equal_area_rank_flat_barrier as base


ZERO_POOL = [
    (942, -90),
    (726, -70),
    (445, -43),
    (-20, 2),
    (438, -42),
    (-111, 11),
    (139, -13),
    (-178, 18),
    (117, -11),
    (-526, 50),
    (-695, 67),
    (-416, 40),
    (843, -81),
    (1340, -128),
    (555, -53),
    (-741, 71),
]

assert len(ZERO_POOL) == len(set(ZERO_POOL)) == 16
assert set(ZERO_POOL) <= set(base.transverse)
assert base.exposed_count(ZERO_POOL) == 0
assert all(base.exposed_count(subpool) == 0 for size in range(1, 17) for subpool in [ZERO_POOL[:size]])

# Every pair in the pool satisfies all three synchronized four-sum
# parallelograms, with the deformed anchors and actual target endpoints.
identity_count = 0
for old_q, old_r in combinations(ZERO_POOL, 2):
    q, r = base.new_q[old_q], base.new_q[old_r]
    Aq, Bq = base.DIFF_EDGE[q]
    Ar, Br = base.DIFF_EDGE[r]
    Eq, Fq = base.target_s[old_q]
    Er, Fr = base.target_s[old_r]
    Iq, Jq = base.target_t[old_q]
    Ir, Jr = base.target_t[old_r]

    assert base.sum_many(
        base.POINTS[Eq], base.POINTS[Fq], base.POINTS[Ir], base.POINTS[Jr]
    ) == base.sum_many(
        base.POINTS[Er], base.POINTS[Fr], base.POINTS[Iq], base.POINTS[Jq]
    )
    assert base.sum_many(
        base.POINTS[Eq], base.POINTS[Fq], base.POINTS[Bq], base.POINTS[Ar]
    ) == base.sum_many(
        base.POINTS[Er], base.POINTS[Fr], base.POINTS[Aq], base.POINTS[Br]
    )
    assert base.sum_many(
        base.POINTS[Iq], base.POINTS[Jq], base.POINTS[Bq], base.POINTS[Ar]
    ) == base.sum_many(
        base.POINTS[Ir], base.POINTS[Jr], base.POINTS[Aq], base.POINTS[Br]
    )
    identity_count += 1

assert identity_count == comb(16, 2) == 120

# Bit-mask exposure reproduces the exact zero-pool counts without repeatedly
# rebuilding endpoint sets.
base_mask = sum(1 << endpoint for endpoint in base.base_endpoints)
translation_masks = {
    old_q: sum(
        1 << endpoint
        for endpoint in (
            set(base.template_anchor[old_q])
            | base.first_edges[old_q]
            | base.second_edges[old_q]
        )
    )
    for old_q in base.transverse
}
area_masks = [
    sum(1 << endpoint for endpoint in set(first + second))
    for first, second, _ in base.area_pairs
]


def mask_exposure(pool):
    endpoint_mask = base_mask
    for old_q in pool:
        endpoint_mask |= translation_masks[old_q]
    return sum(not (area_mask & ~endpoint_mask) for area_mask in area_masks)


assert mask_exposure(ZERO_POOL) == 0
expected_zero_counts = {
    1: 31,
    2: 404,
    3: 2466,
    4: 8358,
    5: 18486,
    6: 29577,
}
actual_zero_counts = {}
for size, expected in expected_zero_counts.items():
    profile = Counter(
        mask_exposure(pool) for pool in combinations(base.transverse, size)
    )
    actual_zero_counts[size] = profile[0]
    assert profile[0] == expected

# Exact finite form of the binomial amplification.  Fractions avoid any
# floating-point issue.  The general proof is (3.4); this exhaustive range
# checks its constants and the sharper ell=2 statement at all boundary
# values relevant to the stored and asymptotic formulations.
for k in range(8, 161):
    for T in range((k + 1) // 2, 3 * k + 1):
        assert Fraction(4 * comb(T, 2), k - 2) >= T
        for ell in range(2, min(16, k // 4) + 1):
            right = (
                Fraction(factorial(ell) * 4 ** (ell - 1), k ** (ell - 1))
                * comb(T, ell)
            )
            assert right >= T, (k, T, ell, right)

print(
    "PASS",
    {
        "k": base.k,
        "codegree": len(base.Q_p),
        "transverse": len(base.transverse),
        "scalar_weights": (1, 1),
        "zero_pool_size": len(ZERO_POOL),
        "synchronized_pair_identities": identity_count,
        "zero_pool_counts": actual_zero_counts,
        "global_geometric_area_pairs": len(base.area_pairs),
    },
)
