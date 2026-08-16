#!/usr/bin/env python3
"""Exact certificate for SAME_PARENT_PROJECTION_PRODUCT_GATE.md.

The construction uses rational points on one circle and a [6,3,4]_7
Reed--Solomon code.  It checks:

* strict general position;
* the common five-point marked/tangent parent and blocked shield/tag;
* all 7^3 selected sources and all 7^6 ambient cross completions;
* canonical depth-three peeling;
* the exact rank-five endpoint baseline C=1 and likelihood arithmetic;
* the MDS distance and projection sizes;
* the full ambient projection square.
"""

from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path


PRIME = 7
DEPTH = 3


def circle(t):
    """Rational parametrization of x^2+y^2=1."""
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def strict_hull(points):
    """Monotone-chain hull; returns boundary vertices and rejects collinearity."""
    pts = sorted(points)
    if len(pts) <= 2:
        return pts
    lo = []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    hi = []
    for p in reversed(pts):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], p) <= 0:
            hi.pop()
        hi.append(p)
    return lo[:-1] + hi[:-1]


def convex_position(points):
    return len(strict_hull(points)) == len(points)


def inside_triangle_strict(p, tri):
    a, b, c = tri
    signs = (cross(a, b, p), cross(b, c, p), cross(c, a, p))
    return (all(s > 0 for s in signs) or all(s < 0 for s in signs))


def rs_words():
    """Degree <3 evaluations at 0,...,5 over F_7."""
    ans = []
    for coeff in product(range(PRIME), repeat=DEPTH):
        word = tuple(sum(coeff[k] * pow(x, k, PRIME) for k in range(DEPTH)) % PRIME
                     for x in range(2 * DEPTH))
        ans.append(word)
    return ans


def peel(points, rounds):
    remaining = list(points)
    for _ in range(rounds):
        remaining.sort(key=lambda p: p[0])
        remaining = remaining[1:-1]
    return set(remaining)


def gap_edge(parent, side):
    """Parent edge replaced by one x-separated side block."""
    hull = strict_hull(tuple(parent) + tuple(side))
    side_set = set(side)
    n = len(hull)
    start = next(i for i, z in enumerate(hull) if z in side_set)
    while hull[(start - 1) % n] in side_set:
        start = (start - 1) % n
    finish = start
    while hull[(finish + 1) % n] in side_set:
        finish = (finish + 1) % n
    assert sum(z in side_set for z in hull) == len(side)
    endpoints = frozenset((hull[(start - 1) % n], hull[(finish + 1) % n]))
    parent_hull = strict_hull(parent)
    i, j = (parent_hull.index(z) for z in endpoints)
    assert (i - j) % len(parent_hull) in (1, len(parent_hull) - 1)
    return endpoints


def adjacent_turn_good(parent, left, right):
    """The sole new turn when the two distinct gap edges share a vertex."""
    gl, gr = gap_edge(parent, left), gap_edge(parent, right)
    assert gl != gr and len(gl & gr) == 1
    z = next(iter(gl & gr))
    hp = strict_hull(parent)
    iz = hp.index(z)
    previous, following = hp[(iz - 1) % len(hp)], hp[(iz + 1) % len(hp)]

    def petal_neighbour(side):
        hs = strict_hull(tuple(parent) + tuple(side))
        i = hs.index(z)
        neighbours = (hs[(i - 1) % len(hs)], hs[(i + 1) % len(hs)])
        ans = [w for w in neighbours if w in set(side)]
        assert len(ans) == 1
        return ans[0]

    prev = petal_neighbour(left) if previous in gl else petal_neighbour(right)
    nxt = petal_neighbour(left) if following in gl else petal_neighbour(right)
    return cross(prev, z, nxt) > 0


def audit_edge_splice():
    """Exact rational witnesses for all three edge-splice branches."""
    # Vertex-disjoint gaps on a rational cyclic hexagon.
    hexagon = tuple(circle(t) for t in
                    (Q(-3), Q(-1), Q(-1, 3), Q(1, 3), Q(1), Q(3)))
    left_disjoint = ((Q(-2593, 1370), Q(1, 149)),)
    right_disjoint = ((Q(553, 685), Q(-442, 745)),)
    assert convex_position(hexagon + left_disjoint)
    assert convex_position(hexagon + right_disjoint)
    assert gap_edge(hexagon, left_disjoint).isdisjoint(gap_edge(hexagon, right_disjoint))
    assert convex_position(hexagon + left_disjoint + right_disjoint)

    # Adjacent gaps can pass or fail, exactly according to the shared turn.
    triangle = ((Q(-1), Q(0)), (Q(0), Q(1)), (Q(1), Q(0)))
    left_adjacent = ((Q(-821, 137), Q(-1489, 149)),)
    right_fail = ((Q(1101, 685), Q(1, 149)),)
    right_pass = ((Q(1512, 685), Q(1346, 745)),)
    for right in (right_fail, right_pass):
        assert convex_position(triangle + left_adjacent)
        assert convex_position(triangle + right)
        assert len(gap_edge(triangle, left_adjacent) & gap_edge(triangle, right)) == 1
        assert convex_position(triangle + left_adjacent + right) == adjacent_turn_good(
            triangle, left_adjacent, right
        )
    assert not convex_position(triangle + left_adjacent + right_fail)
    assert convex_position(triangle + left_adjacent + right_pass)

    # Same-edge localization has both a positive and a negative witness.
    right_same_pass = ((Q(138, 137), Q(-1489, 149)),)
    assert gap_edge(triangle, left_adjacent) == gap_edge(triangle, right_same_pass)
    assert convex_position(triangle + left_adjacent + right_same_pass)

    left_same_fail = (
        (Q(-9, 5), Q(-477463, 99700)),
        (Q(-211, 50), Q(-27911, 4985)),
    )
    right_same_fail = (
        (Q(26, 5), Q(-553869, 99100)),
        (Q(68, 25), Q(-615311, 99100)),
    )
    assert convex_position(triangle + left_same_fail)
    assert convex_position(triangle + right_same_fail)
    common_gap = gap_edge(triangle, left_same_fail)
    assert common_gap == gap_edge(triangle, right_same_fail)
    whole = convex_position(triangle + left_same_fail + right_same_fail)
    child = convex_position(tuple(common_gap) + left_same_fail + right_same_fail)
    assert whole == child == False
    return {
        "disjoint_gap_pass": True,
        "adjacent_turn_pass_and_fail": True,
        "same_edge_positive_and_negative": True,
    }


def main():
    edge_splice = audit_edge_splice()
    # Three disjoint left x-blocks and three disjoint right x-blocks.
    left_centres = (Q(13, 10), Q(12, 10), Q(11, 10))
    right_centres = (Q(5, 10), Q(4, 10), Q(3, 10))
    offsets = tuple(Q(i - 3, 1000) for i in range(PRIME))
    clusters = [tuple(circle(c + u) for u in offsets) for c in left_centres]
    clusters += [tuple(circle(c + u) for u in offsets) for c in right_centres]

    # Cyclic order on the empty central conic arc is a,u,p,v,b.  Removing
    # p makes uv an edge; adding p is the fixed exterior repair insertion.
    a, u, p, v, b = (circle(t) for t in
                     (Q(3, 5), Q(7, 10), Q(4, 5), Q(9, 10), Q(1)))
    # A generic rational strict convex combination inside triangle b,p,a.
    x = tuple(Q(1, 5) * b[i] + Q(1, 3) * p[i] + Q(7, 15) * a[i]
              for i in range(2))
    parent = (a, u, p, v, b)
    endpoint = (b, a)
    interval_tag = (p, x)
    all_points = [p for block in clusters for p in block] + list(parent) + [x]

    # Exact general position.
    assert all(cross(a, b, c) != 0 for a, b, c in combinations(all_points, 3))
    assert convex_position(parent)
    assert inside_triangle_strict(x, (b, p, a))
    assert convex_position(interval_tag)
    assert not convex_position(endpoint + interval_tag)

    # Exactly u,p,v,x lie in the open x-interval of the endpoint pair.
    ex0, ex1 = sorted((b[0], a[0]))
    between = [p for p in all_points if ex0 < p[0] < ex1]
    assert set(between) == {u, p, v, x}
    rank5_baseline = [endpoint + subset for subset in combinations(between, 3)
                      if convex_position(endpoint + subset)]
    assert rank5_baseline == [endpoint + (u, p, v)]

    endpoint_counts = []
    for size in range(len(between) + 1):
        endpoint_counts.append(sum(
            convex_position(endpoint + subset)
            for subset in combinations(between, size)
        ))
    assert endpoint_counts == [1, 4, 4, 1, 0]

    words = rs_words()
    assert len(words) == PRIME ** DEPTH
    assert len(set(words)) == len(words)
    distances = [sum(a != b for a, b in zip(s, t)) for s, t in combinations(words, 2)]
    min_distance = min(distances)
    assert min_distance == DEPTH + 1

    selected_sources = []
    for word in words:
        source = parent + tuple(clusters[i][word[i]] for i in range(2 * DEPTH))
        assert convex_position(source)
        assert peel(source, DEPTH) == set(parent)
        hull = strict_hull(source)
        ia, iu, ip, iv, ib = (hull.index(z) for z in (a, u, p, v, b))
        neighbours = lambda i: {hull[(i - 1) % len(hull)], hull[(i + 1) % len(hull)]}
        assert neighbours(ip) == {u, v}
        assert p in neighbours(iu) and a in neighbours(iu)
        assert p in neighbours(iv) and b in neighbours(iv)
        without_mark = tuple(z for z in source if z != p)
        hull_without_mark = strict_hull(without_mark)
        ju = hull_without_mark.index(u)
        assert v in {hull_without_mark[(ju - 1) % len(hull_without_mark)],
                     hull_without_mark[(ju + 1) % len(hull_without_mark)]}
        assert not convex_position(source + (x,))
        selected_sources.append(source)

    # All cross-combinations of the two projection alphabets are genuine
    # ordinary faces.  Here each projection is the full F_7^3 alphabet.
    left_projection = {word[:DEPTH] for word in words}
    right_projection = {word[DEPTH:] for word in words}
    assert len(left_projection) == len(right_projection) == PRIME ** DEPTH
    cross_count = 0
    for left in left_projection:
        for right in right_projection:
            word = left + right
            source = parent + tuple(clusters[i][word[i]] for i in range(2 * DEPTH))
            assert convex_position(source)
            cross_count += 1
    assert cross_count == PRIME ** (2 * DEPTH)

    # Exact same-rank arithmetic.  Endpoint rank five has the unique parent;
    # the whole compatible endpoint law has rank counts 1,4,4,1,0.
    n_selected = len(words)
    c_rank5 = len(rank5_baseline)
    raw_density = Q(n_selected, c_rank5)
    endpoint_half_weight = sum(Q(count, 2 ** (size + 2))
                               for size, count in enumerate(endpoint_counts))
    h = Q(n_selected, 32 * (4 ** DEPTH)) / endpoint_half_weight
    assert endpoint_half_weight == Q(33, 32)
    assert h == Q(n_selected, 33 * (4 ** DEPTH))
    assert (4 ** DEPTH) * h == Q(1, 33) * raw_density

    cert = {
        "field": PRIME,
        "depth": DEPTH,
        "points": len(all_points),
        "selected_sources": n_selected,
        "ambient_cross_bank": cross_count,
        "rs_min_distance": min_distance,
        "left_projection": len(left_projection),
        "right_projection": len(right_projection),
        "repair_cell": "a,u,p,v,b",
        "rank5_endpoint_baseline": c_rank5,
        "endpoint_rank_counts": endpoint_counts,
        "raw_density": str(raw_density),
        "endpoint_half_weight": str(endpoint_half_weight),
        "h": str(h),
        "four_to_j_h": str((4 ** DEPTH) * h),
        "repair_insertion_verified": True,
        "marked_shield_verified": True,
        "blocked_interval_tag": True,
        "general_position": True,
        "edge_splice_audit": edge_splice,
    }
    out = Path(__file__).with_name("same_parent_projection_product_gate_certificate.json")
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
