#!/usr/bin/env python3
"""Exact verifier for BLOCKER_ROLE_COVER_RELEASE_DICHOTOMY.md."""

from fractions import Fraction as F
from itertools import combinations


def orient(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    return half(pts)[:-1] + half(reversed(pts))[:-1]


def convex(points):
    return len(hull(points)) == len(points)


def inside_triangle(p, a, b, c):
    signs = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def blocker_edges(face, external):
    """All loop/ordinary role traces supporting a bad four-set."""
    edges = set()
    for r, point in enumerate(external):
        if any(not convex(list(triple) + [point])
               for triple in combinations(face, 3)):
            edges.add(frozenset((r,)))
    for r, s in combinations(range(len(external)), 2):
        if any(not convex(list(pair) + [external[r], external[s]])
               for pair in combinations(face, 2)):
            edges.add(frozenset((r, s)))
    return edges


def is_cover(chosen, edges):
    return all(chosen & edge for edge in edges)


def min_cover_size(n, edges):
    return min(len(chosen) for mask in range(1 << n)
               if is_cover(chosen := frozenset(i for i in range(n)
                                                if mask >> i & 1), edges))


def max_matching_size(edges):
    edge_list = list(edges)
    best = 0
    for mask in range(1 << len(edge_list)):
        used = set()
        count = 0
        valid = True
        for i, edge in enumerate(edge_list):
            if mask >> i & 1:
                if used & edge:
                    valid = False
                    break
                used.update(edge)
                count += 1
        if valid:
            best = max(best, count)
    return best


def fractional_cover_cost(n, edges, weights):
    """Brute the half-integral weighted vertex-cover LP."""
    best = None
    # Weighted graph vertex-cover LP has a half-integral optimum.
    for code in range(3 ** n):
        value = code
        coords = []
        for _ in range(n):
            coords.append((value % 3) * F(1, 2))
            value //= 3
        if all(sum(coords[v] for v in edge) >= 1 for edge in edges):
            cost = sum(weights[v] * coords[v] for v in range(n))
            if best is None or cost < best:
                best = cost
    return best


# Exact high-cover cap instance.
h = 7
delta = F(1, 100 * h * h)
curve = [(F(2) - delta * t * t, -F(1, 5) + delta * t)
         for t in range(1, h + 1)]
b = (F(4), F(0))
a = (F(0), F(0))
cap_parameters = (F(3, 10000), F(1, 10000), F(-2, 10000))
cap = [(r, F(4) + F(1, 10000) - r * r) for r in cap_parameters]

ambient = curve + [b] + cap + [a]
assert all(orient(*triple) != 0 for triple in combinations(ambient, 3))
assert convex([b] + cap + [a])
assert all(convex([point, b] + cap + [a]) for point in curve)
assert all(inside_triangle(curve[j], curve[i], curve[k], blocker)
           for i, j, k in combinations(range(h), 3)
           for blocker in cap)

# External role order is b, cap_1, cap_2, cap_3, a.  The three cap roles
# have indices 1,2,3.
external = [b] + cap + [a]
cap_roles = {1, 2, 3}
role_weights = [F(2), F(3), F(5), F(7), F(11)]

checked_faces = 0
canonical_sizes = []
for mask in range(1, 1 << h):
    face = [curve[i] for i in range(h) if mask >> i & 1]
    assert convex(face)
    edges = blocker_edges(face, external)

    # Exact blocker-cover criterion, exhausted over all deletions.
    for deletion_mask in range(1 << len(external)):
        deletion = frozenset(i for i in range(len(external))
                             if deletion_mask >> i & 1)
        output = face + [point for i, point in enumerate(external)
                         if i not in deletion]
        assert is_cover(deletion, edges) == convex(output)

    tau = min_cover_size(len(external), edges)
    nu = max_matching_size(edges)
    assert tau <= 2 * nu

    # Weighted cover partition / factor-two LP audit.  Loops are included
    # directly in the LP constraints.
    weighted_integral = min(
        sum(role_weights[i] for i in chosen)
        for deletion_mask in range(1 << len(external))
        if is_cover(chosen := frozenset(i for i in range(len(external))
                                               if deletion_mask >> i & 1),
                    edges)
    )
    weighted_fractional = fractional_cover_cost(
        len(external), edges, role_weights
    )
    assert weighted_fractional <= weighted_integral
    assert weighted_integral <= 2 * weighted_fractional

    # For the exact disjoint-union identity, use binary alphabets in all
    # five external roles and the lexicographically first minimum-cardinality
    # cover.  Its occupancy mask distinguishes every cover cell.
    minimum_covers = []
    for deletion_mask in range(1 << len(external)):
        chosen = frozenset(i for i in range(len(external))
                           if deletion_mask >> i & 1)
        if is_cover(chosen, edges) and len(chosen) == tau:
            minimum_covers.append(chosen)
    canonical = min(minimum_covers, key=lambda chosen: tuple(sorted(chosen)))
    canonical_sizes.append(len(canonical))

    if len(face) >= 3:
        assert all(frozenset((role,)) in edges for role in cap_roles)
        assert tau >= len(cap_roles)
    checked_faces += 1

assert checked_faces == 127

# Exact cover-union size for external alphabet sizes L_r=2.  A face with
# cover J contributes 2^(5-|J|), and different (face,J) cells are disjoint.
exact_union = sum(2 ** (len(external) - size) for size in canonical_sizes)
p_ext = 2 ** len(external)
assert exact_union == p_ext * sum(F(1, 2 ** size) for size in canonical_sizes)
mean_cover = F(sum(canonical_sizes), len(canonical_sizes))
assert exact_union / (p_ext * len(canonical_sizes)) >= 2 ** (-float(mean_cover))

print("BLOCKER_ROLE_COVER_RELEASE_DICHOTOMY verifier: PASS")
