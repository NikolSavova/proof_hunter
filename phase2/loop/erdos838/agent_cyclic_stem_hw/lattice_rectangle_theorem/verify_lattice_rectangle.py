#!/usr/bin/env python3
"""Exact regression for the planar two-ended lattice rectangle theorem.

Only integer orientations, bit masks, and finite exhaustive checks are used.
The script is deliberately independent of the other Erdős 838 verifiers.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import cmp_to_key
from itertools import combinations, product


Point = tuple[int, int]


POINTS: tuple[Point, ...] = (
    (12, 17),
    (0, 17),
    (-2, -16),
    (12, 8),
    (19, -3),
    (-3, 10),
    (1, -5),
    (-20, 12),
    (17, -20),
)


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def assert_general_position(points: tuple[Point, ...]) -> None:
    for i, j, k in combinations(range(len(points)), 3):
        assert orient(points[i], points[j], points[k]) != 0


def convex_hull(mask: int, points: tuple[Point, ...]) -> tuple[int, ...]:
    ids = [i for i in range(len(points)) if mask >> i & 1]
    if len(ids) <= 1:
        return tuple(ids)
    ordered = sorted(ids, key=lambda i: points[i])

    lower: list[int] = []
    for i in ordered:
        while len(lower) >= 2 and orient(
            points[lower[-2]], points[lower[-1]], points[i]
        ) <= 0:
            lower.pop()
        lower.append(i)

    upper: list[int] = []
    for i in reversed(ordered):
        while len(upper) >= 2 and orient(
            points[upper[-2]], points[upper[-1]], points[i]
        ) <= 0:
            upper.pop()
        upper.append(i)
    return tuple(lower[:-1] + upper[:-1])


def is_convex(mask: int, points: tuple[Point, ...]) -> bool:
    return len(convex_hull(mask, points)) == mask.bit_count()


def affine_closure(mask: int, points: tuple[Point, ...]) -> int:
    hull = convex_hull(mask, points)
    if len(hull) <= 1:
        return mask
    if len(hull) == 2:
        a, b = (points[hull[0]], points[hull[1]])
        out = 0
        for i, p in enumerate(points):
            if orient(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(
                a[0], b[0]
            ) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]):
                out |= 1 << i
        return out
    out = 0
    for i, p in enumerate(points):
        if all(
            orient(points[hull[j]], points[hull[(j + 1) % len(hull)]], p)
            >= 0
            for j in range(len(hull))
        ):
            out |= 1 << i
    return out


def other_hull_neighbor(mask: int, root: int, chord_end: int) -> int:
    hull = convex_hull(mask, POINTS)
    j = hull.index(root)
    neighbours = {hull[(j - 1) % len(hull)], hull[(j + 1) % len(hull)]}
    assert chord_end in neighbours and len(neighbours) == 2
    return next(iter(neighbours - {chord_end}))


def rooted_arcs(u: int, v: int, sign: int) -> list[int]:
    n = len(POINTS)
    uv = (1 << u) | (1 << v)
    allowed = [
        i
        for i in range(n)
        if i not in (u, v) and sign * orient(POINTS[u], POINTS[v], POINTS[i]) > 0
    ]
    arcs: list[int] = []
    for bits in range(1, 1 << len(allowed)):
        mask = uv
        for j, i in enumerate(allowed):
            if bits >> j & 1:
                mask |= 1 << i
        if is_convex(mask, POINTS):
            hull = convex_hull(mask, POINTS)
            if (hull.index(u) - hull.index(v)) % len(hull) in (1, len(hull) - 1):
                arcs.append(mask)
    return arcs


def tangent_compatible(positive: int, negative: int, u: int, v: int) -> bool:
    pu = other_hull_neighbor(positive, u, v)
    pv = other_hull_neighbor(positive, v, u)
    nu = other_hull_neighbor(negative, u, v)
    nv = other_hull_neighbor(negative, v, u)
    return orient(POINTS[pu], POINTS[u], POINTS[nu]) > 0 and orient(
        POINTS[nv], POINTS[v], POINTS[pv]
    ) > 0


def lca_depth(a: int, b: int, height: int) -> int:
    """Depth of the lowest separating binary node for distinct ranks."""
    assert a != b and 0 <= a < 1 << height and 0 <= b < 1 << height
    common = height - (a ^ b).bit_length()
    return common


def direction_ranks(vectors: dict[tuple[str, int], Point]) -> dict[tuple[str, int], int]:
    """Order non-collinear vectors lying in one open half-plane."""

    def compare(x: tuple[str, int], y: tuple[str, int]) -> int:
        a, b = vectors[x], vectors[y]
        turn = a[0] * b[1] - a[1] * b[0]
        assert turn != 0
        return -1 if turn > 0 else 1

    ordered = sorted(vectors, key=cmp_to_key(compare))
    return {x: j for j, x in enumerate(ordered)}


def tangent_ranks(
    u: int,
    v: int,
    positives: list[int],
    negatives: list[int],
) -> tuple[dict[tuple[str, int], int], dict[tuple[str, int], int]]:
    """Exact linear tangent orders making compatibility two inequalities.

    At ``u`` reflect negative rays through the root.  At ``v`` reflect
    positive rays.  Each transformed family lies in one open half-plane,
    so determinants give a strict linear angular order.
    """

    pos_u = {other_hull_neighbor(a, u, v) for a in positives}
    neg_u = {other_hull_neighbor(a, u, v) for a in negatives}
    pos_v = {other_hull_neighbor(a, v, u) for a in positives}
    neg_v = {other_hull_neighbor(a, v, u) for a in negatives}
    u_vectors: dict[tuple[str, int], Point] = {}
    v_vectors: dict[tuple[str, int], Point] = {}
    for x in pos_u:
        u_vectors[("p", x)] = (
            POINTS[x][0] - POINTS[u][0],
            POINTS[x][1] - POINTS[u][1],
        )
    for x in neg_u:
        u_vectors[("n", x)] = (
            POINTS[u][0] - POINTS[x][0],
            POINTS[u][1] - POINTS[x][1],
        )
    for x in neg_v:
        v_vectors[("n", x)] = (
            POINTS[x][0] - POINTS[v][0],
            POINTS[x][1] - POINTS[v][1],
        )
    for x in pos_v:
        v_vectors[("p", x)] = (
            POINTS[v][0] - POINTS[x][0],
            POINTS[v][1] - POINTS[x][1],
        )
    return direction_ranks(u_vectors), direction_ranks(v_vectors)


def dyadic_node(rank: int, depth: int, height: int) -> tuple[int, int]:
    return depth, rank >> (height - depth)


def planar_audit() -> dict[str, int]:
    assert_general_position(POINTS)
    n = len(POINTS)
    fixed_seen: dict[tuple[int, int, int], tuple[int, int]] = {}
    global_fibres: defaultdict[int, set[tuple[int, int, int, int]]] = defaultdict(set)
    compatible_count = 0
    incompatible_count = 0
    arc_count = 0
    dyadic = Counter()
    height = (n - 1).bit_length()

    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            positives = rooted_arcs(u, v, +1)
            negatives = rooted_arcs(u, v, -1)
            arc_count += len(positives) + len(negatives)

            rank_u, rank_v = tangent_ranks(u, v, positives, negatives)
            chord_rectangles: defaultdict[
                tuple[tuple[int, int], tuple[int, int]],
                tuple[set[int], set[int]],
            ] = defaultdict(lambda: (set(), set()))

            for positive, negative in product(positives, negatives):
                criterion = tangent_compatible(positive, negative, u, v)
                union = positive | negative
                actual = is_convex(union, POINTS)
                assert criterion == actual
                if not criterion:
                    incompatible_count += 1
                    continue
                compatible_count += 1
                closed = affine_closure(union, POINTS)
                assert set(convex_hull(closed, POINTS)) == {
                    i for i in range(n) if union >> i & 1
                }

                key = (u, v, closed)
                old = fixed_seen.setdefault(key, (positive, negative))
                assert old == (positive, negative)
                global_fibres[closed].add((u, v, positive, negative))

                # The target is intermediate between cl{u,v} and the closure
                # of the carrier consisting of the two half-plane arc pools.
                carrier = 0
                for a in positives + negatives:
                    carrier |= a
                bottom = affine_closure((1 << u) | (1 << v), POINTS)
                top = affine_closure(carrier, POINTS)
                assert bottom & ~closed == 0 and closed & ~top == 0

                # Every compatible pair has a unique pair of lowest separating
                # dyadic nodes in the two exact tangent orders.
                pu = other_hull_neighbor(positive, u, v)
                nu = other_hull_neighbor(negative, u, v)
                pv = other_hull_neighbor(positive, v, u)
                nv = other_hull_neighbor(negative, v, u)
                rup, run = rank_u[("p", pu)], rank_u[("n", nu)]
                rvn, rvp = rank_v[("n", nv)], rank_v[("p", pv)]
                assert rup < run and rvn < rvp
                du = lca_depth(rup, run, height)
                dv = lca_depth(rvn, rvp, height)
                dyadic[(du, dv)] += 1
                signature = (
                    dyadic_node(rup, du, height),
                    dyadic_node(rvn, dv, height),
                )
                chord_rectangles[signature][0].add(positive)
                chord_rectangles[signature][1].add(negative)

            # Every lowest-node class is a complete compatibility rectangle.
            for positives_box, negatives_box in chord_rectangles.values():
                for positive, negative in product(positives_box, negatives_box):
                    assert tangent_compatible(positive, negative, u, v)

    max_fibre = 0
    for closed, descriptions in global_fibres.items():
        rank = len(convex_hull(closed, POINTS))
        max_fibre = max(max_fibre, len(descriptions))
        assert len(descriptions) <= rank * (rank - 1)
    assert sum(dyadic.values()) == compatible_count
    assert len(dyadic) <= height * height
    return {
        "points": n,
        "rooted_arc_occurrences": arc_count,
        "compatible_pairs": compatible_count,
        "incompatible_pairs": incompatible_count,
        "distinct_target_closed_sets": len(global_fibres),
        "maximum_global_fibre": max_fibre,
        "dyadic_depth_pairs_used": len(dyadic),
    }


def ideal_closure(mask: int, k: int, ell: int) -> int:
    lower = (1 << k) - 1
    upper = ((1 << ell) - 1) << k
    if mask & upper:
        return mask | lower
    return mask


def meet_distributive_counterexample(k: int = 4, ell: int = 4) -> dict[str, int]:
    n = k + ell
    full = (1 << n) - 1
    lower_mask = (1 << k) - 1
    closed = [m for m in range(1 << n) if ideal_closure(m, k, ell) == m]
    closed_set = set(closed)

    # Closure axioms and anti-exchange.
    for a in range(1 << n):
        ca = ideal_closure(a, k, ell)
        assert a & ~ca == 0
        assert ideal_closure(ca, k, ell) == ca
        for b in range(1 << n):
            if a & ~b == 0:
                assert ideal_closure(a, k, ell) & ~ideal_closure(b, k, ell) == 0
        outside = [x for x in range(n) if not (ca >> x & 1)]
        for x, y in combinations(outside, 2):
            x_from_y = ideal_closure(a | (1 << y), k, ell) >> x & 1
            y_from_x = ideal_closure(a | (1 << x), k, ell) >> y & 1
            assert not (x_from_y and y_from_x)

    # The ideal lattice is distributive; verify both laws exhaustively.
    def meet(a: int, b: int) -> int:
        return a & b

    def join(a: int, b: int) -> int:
        return ideal_closure(a | b, k, ell)

    for a, b, c in product(closed, repeat=3):
        assert meet(a, join(b, c)) == join(meet(a, b), meet(a, c))
        assert join(a, meet(b, c)) == meet(join(a, b), join(a, c))
        assert meet(a, b) in closed_set and join(a, b) in closed_set

    lowers = list(range(1 << k))
    uppers = [lower_mask | (s << k) for s in range(1 << ell)]
    for a, b in product(lowers, uppers):
        assert a & ~b == 0

    expected_closed = (1 << k) + (1 << ell) - 1
    expected_rectangle = 1 << (k + ell)
    assert len(closed) == expected_closed
    assert len(lowers) * len(uppers) == expected_rectangle
    assert full in closed_set
    return {
        "ground_rank": n,
        "lower_family": len(lowers),
        "upper_family": len(uppers),
        "comparability_rectangle": expected_rectangle,
        "all_closed_sets": expected_closed,
    }


def main() -> None:
    planar = planar_audit()
    abstract = meet_distributive_counterexample()
    print("PLANAR_TWO_ENDED_AUDIT", planar)
    print("MEET_DISTRIBUTIVE_COUNTEREXAMPLE", abstract)
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
