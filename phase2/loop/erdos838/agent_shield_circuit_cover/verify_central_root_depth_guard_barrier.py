#!/usr/bin/env python3
"""Exact verifier for CENTRAL_ROOT_DEPTH_GUARD_BARRIER.md."""

from __future__ import annotations

from itertools import combinations, product
from math import comb


ROOT = (137, 251)
CLUSTERS = (
    ((100058, -71), (99971, 63)),
    ((76558, 64237), (76675, 64282)),
    ((17322, 98540), (17267, 98459)),
    ((-49979, 86506), (-49971, 86505)),
    ((-94063, 34283), (-93986, 34113)),
    ((-93871, -34144), (-94046, -34251)),
    ((-49927, -86516), (-49977, -86536)),
    ((17360, -98456), (17376, -98408)),
    ((76652, -64268), (76681, -64190)),
)


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(points) == len(set(points)) and len(hull(points)) == len(points)


def strict_inside(point, points):
    boundary = hull(points)
    if len(boundary) < 3:
        return False
    signs = [cross(boundary[i], boundary[(i + 1) % len(boundary)], point)
             for i in range(len(boundary))]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def geometry_audit():
    t = len(CLUSTERS)
    m = (t - 1) // 2
    alphabet = len(CLUSTERS[0])
    points = (ROOT,) + sum(CLUSTERS, ())
    assert (t, m, alphabet, len(points)) == (9, 4, 2, 19)
    assert all(cross(a, b, c) != 0 for a, b, c in combinations(points, 3))

    words = tuple(product(range(alphabet), repeat=t))
    fixed_circuit_signs = set()
    for word in words:
        face = [CLUSTERS[i][word[i]] for i in range(t)]
        assert convex(face)
        assert strict_inside(ROOT, face)
        assert not convex([ROOT] + face)
        # Roles 0,3,6 are a uniform 1+3 witness.
        triangle = [face[i] for i in (0, 3, 6)]
        assert strict_inside(ROOT, triangle)
        fixed_circuit_signs.add(
            tuple(cross(triangle[i], triangle[(i + 1) % 3], ROOT) > 0
                  for i in range(3))
        )

        # Every deletion of at most m-1 roles retains at least m+2 roles.
        # It is enough to check every exact (m+2)-role subset.
        for active in combinations(range(t), m + 2):
            assert strict_inside(ROOT, [face[i] for i in active])

        # Deleting the complementary m roles releases each consecutive block.
        for start in range(t):
            active = [(start + offset) % t for offset in range(m + 1)]
            assert convex([ROOT] + [face[i] for i in active])
    assert len(fixed_circuit_signs) == 1

    # Exhaust every partial transversal.  Symbol 0 omits a role; 1 and 2
    # select its two labels.  Detached words are always convex.  Rooted
    # words are convex exactly for masks contained in a five-role block.
    rooted_by_rank = [0] * (t + 1)
    rooted_total = 0
    detached_total = 0
    for word in product(range(alphabet + 1), repeat=t):
        active = {i for i, symbol in enumerate(word) if symbol}
        face = [CLUSTERS[i][word[i] - 1] for i in active]
        assert convex(face)
        detached_total += 1
        in_block = any(
            active <= {(start + offset) % t for offset in range(m + 1)}
            for start in range(t)
        )
        rooted = convex([ROOT] + face)
        if not active:
            rooted = True
        assert rooted == (in_block or not active)
        if rooted and active:
            rooted_by_rank[len(active)] += 1
            rooted_total += 1

    assert detached_total == (alphabet + 1) ** t == 19683
    assert rooted_by_rank == [0, 18, 144, 432, 576, 288, 0, 0, 0, 0]
    assert rooted_total == 1458

    # Independent mask count reproduces the rooted total.
    admissible_masks = set()
    for start in range(t):
        block = {(start + offset) % t for offset in range(m + 1)}
        for rank in range(1, m + 2):
            admissible_masks.update(frozenset(mask) for mask in combinations(block, rank))
    assert sum(alphabet ** len(mask) for mask in admissible_masks) == rooted_total

    return {
        "parameters": {"t": t, "m": m, "A": alphabet},
        "points": len(points),
        "general_position": True,
        "full_transversals": len(words),
        "fixed_circuit_role_patterns": len(fixed_circuit_signs),
        "minimum_guard_deletions": m,
        "detached_partial_transversals": detached_total,
        "rooted_partial_transversals_nonempty": rooted_total,
        "rooted_rank_vector": rooted_by_rank,
    }


def counting_audit():
    rows = []
    for t, alphabet, contexts in ((5, 7, 11), (9, 101, 1000), (13, 4096, 10**6)):
        m = (t - 1) // 2
        mass = alphabet**t
        detached = (alphabet + 1) ** t
        rooted_upper = t * (alphabet + 1) ** (m + 1)
        combined_capacity = detached + contexts * rooted_upper
        congestion_numerator = contexts * mass
        assert mass <= detached
        assert t * alphabet ** (m + 1) <= rooted_upper
        # At most g deletions gives the exact detached downshadow count.
        for g in range(m):
            shadow = sum(comb(t, d) * alphabet ** (t - d) for d in range(g + 1))
            assert shadow <= detached
            assert congestion_numerator >= contexts * shadow * mass // detached
        rows.append(
            {
                "t": t,
                "A": alphabet,
                "K": contexts,
                "M": mass,
                "detached": detached,
                "rooted_upper": rooted_upper,
                "congestion_floor": congestion_numerator // combined_capacity,
            }
        )
    return rows


def main():
    geometry = geometry_audit()
    counting = counting_audit()
    print("CENTRAL_ROOT_DEPTH_GUARD_BARRIER verifier: PASS")
    print("geometry:", geometry)
    print("counting:", counting)


if __name__ == "__main__":
    main()
