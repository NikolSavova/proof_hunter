#!/usr/bin/env python3
"""Exact checks for ROOT_AWARE_FIXED_EDGE_SEMIALGEBRAIC_EXTRACTION_GATE.md."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
import math


def det(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def sign(x):
    return (x > 0) - (x < 0)


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and det(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and det(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def ordinary(points):
    return len(set(points)) == len(points) and len(hull(points)) == len(points)


def order_type(points):
    return tuple(
        sign(det(points[i], points[j], points[l]))
        for i, j, l in combinations(range(len(points)), 3)
    )


def check_positive_anchored_chain():
    # The edge uv is replaced by an increasing lower-parabola chain.
    u, v, w = (Q(-4), Q(0)), (Q(4), Q(0)), (Q(0), Q(8))

    def p(x):
        return (x, x * x - 16)

    roles = [
        [p(Q(-3)), p(Q(-5, 2))],
        [p(Q(-3, 2)), p(Q(-1))],
        [p(Q(1, 2)), p(Q(1))],
        [p(Q(5, 2)), p(Q(3))],
    ]
    base = [u, v, w]
    assert ordinary(base)
    all_points = base + [x for role in roles for x in role]
    assert all(det(*triple) != 0 for triple in combinations(all_points, 3))
    for role in roles:
        for x in role:
            assert ordinary(base + [x])
    for xs in product(*roles):
        assert ordinary(base + list(xs))
    # Hereditary partial-role bank: product_i(1+|X_i|)=3^4.
    outputs = set()
    choices = [[None] + role for role in roles]
    for xs in product(*choices):
        face = tuple(sorted(base + [x for x in xs if x is not None]))
        assert ordinary(list(face))
        outputs.add(face)
    assert len(outputs) == 3**4


def nested_instance(k=4, D=3):
    q = k * D
    delta = Q(1, 100 * q * q)
    u, v, w = (Q(-2), Q(0)), (Q(2), Q(0)), (Q(0), Q(6))
    m, n, d = (Q(1), Q(3)), (Q(3), Q(1)), (Q(-2), Q(6))

    def add(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def scale(c, a):
        return (c * a[0], c * a[1])

    A = []
    for t in range(1, q + 1):
        A.append(add(add(m, scale(t, n)), scale(delta * t * t, d)))
    blocks = [A[i * D : (i + 1) * D] for i in range(k)]
    return (u, v, w), m, n, d, delta, A, blocks


def check_nested_barrier():
    k, D = 4, 3
    B, m, n, d, delta, A, blocks = nested_instance(k, D)
    u, v, w = B
    q = len(A)

    # Full general position and singleton insertion at the common edge vw.
    assert all(det(*triple) != 0 for triple in combinations(list(B) + A, 3))
    assert ordinary(list(B))
    assert all(ordinary(list(B) + [a]) for a in A)

    # Exact barycentric nesting and the displayed determinant identities.
    for s in range(1, q + 1):
        a_s = A[s - 1]
        for t in range(s + 1, q + 1):
            a_t = A[t - 1]
            b_st = (
                m[0] - delta * s * t * d[0],
                m[1] - delta * s * t * d[1],
            )
            lam = -delta * s * t
            assert Q(-1, 2) < lam < Q(1, 2)
            assert b_st == (
                m[0] + lam * d[0],
                m[1] + lam * d[1],
            )
            rhs = (
                Q(s, t) * a_t[0] + (1 - Q(s, t)) * b_st[0],
                Q(s, t) * a_t[1] + (1 - Q(s, t)) * b_st[1],
            )
            assert a_s == rhs
            # Strict interior follows from positive barycentric weights:
            # b_st is itself a strict convex combination of v and w.
            theta = lam + Q(1, 2)
            weights = (
                Q(s, t),
                (1 - Q(s, t)) * (1 - theta),
                (1 - Q(s, t)) * theta,
            )
            assert all(x > 0 for x in weights)
            assert sum(weights) == 1
            reconstructed = (
                weights[0] * a_t[0]
                + weights[1] * v[0]
                + weights[2] * w[0],
                weights[0] * a_t[1]
                + weights[1] * v[1]
                + weights[2] * w[1],
            )
            assert reconstructed == a_s

            assert det(u, a_s, a_t) == (t - s) * (
                -6 + delta * (24 * (s + t) + 20 * s * t)
            )
            assert det(v, a_s, a_t) == (t - s) * (
                -10 + 20 * delta * s * t
            )
            assert det(w, a_s, a_t) == (t - s) * (
                10 + 20 * delta * s * t
            )
            assert det(u, a_s, a_t) < 0
            assert det(v, a_s, a_t) < 0
            assert det(w, a_s, a_t) > 0
            assert not ordinary(list(B) + [a_s, a_t])

    for t, a_t in enumerate(A, 1):
        assert det(u, v, a_t) == 4 * (3 + t + 6 * delta * t * t)
        assert det(v, w, a_t) == -20 * t
        assert det(w, u, a_t) == 12 + 16 * t - 24 * delta * t * t
        assert det(u, v, a_t) > 0
        assert det(v, w, a_t) < 0
        assert det(w, u, a_t) > 0

    for r, s, t in combinations(range(1, q + 1), 3):
        lhs = det(A[r - 1], A[s - 1], A[t - 1])
        rhs = 20 * delta * (s - r) * (t - r) * (t - s)
        assert lhs == rhs > 0

    # All 3^4 rooted transversals have one full labelled order type and
    # precisely four hull vertices.
    types, hull_sizes = set(), set()
    for xs in product(*blocks):
        rooted = list(B) + list(xs)
        types.add(order_type(rooted))
        hull_sizes.add(len(hull(rooted)))
        assert not ordinary(rooted)
        assert set(hull(rooted)) == set(B) | {xs[-1]}
    assert len(types) == 1
    assert hull_sizes == {4}

    # Complete fixed-edge cross-role rectangle.
    cross_pairs = 0
    for i, j in combinations(range(k), 2):
        for a_s in blocks[i]:
            for a_t in blocks[j]:
                assert not ordinary(list(B) + [a_s, a_t])
                cross_pairs += 1
    assert cross_pairs == math.comb(k, 2) * D * D == 54

    # External support is a Boolean face reservoir.
    assert len(hull(A)) == q
    for mask in range(1 << q):
        subset = [A[i] for i in range(q) if mask >> i & 1]
        if len(subset) >= 3:
            assert ordinary(subset)
    assert 1 << q == 4096

    # Exact B-retaining ledger: only the empty and singleton A traces.
    rooted_count = 0
    for mask in range(1 << q):
        subset = [A[i] for i in range(q) if mask >> i & 1]
        if ordinary(list(B) + subset):
            rooted_count += 1
    assert rooted_count == q + 1 == 13


def check_semialgebraic_arithmetic():
    alpha, Bexp, Cexp = 0.25, 3, 2
    for L in (1024, 2048, 4096, 8192, 16384, 32768, 65536):
        logL = math.log2(L)
        k = max(2, int(alpha * logL))
        r = 2 * L
        complexity = (r + k) ** 2
        # log2 of the FPS lower bound for one extracted block.
        block_log = (
            L
            - Bexp * logL
            - 3 * Cexp * logL
            - 40 * k * math.log2(3)
            - 2 * math.log2(complexity)
        )
        assert block_log > 0
        bank_lower_log = k * block_log
        assert bank_lower_log > 0.1 * L * logL
        # Optional pigeonhole over at most k! rooted chain orders.
        order_loss = 3 * k * math.lgamma(k + 1) / math.log(2)
        assert bank_lower_log - order_loss > 0.09 * L * logL


def check_weighted_load_identity():
    # Two copies of the same rooted context with weights 2 and 3.
    base = frozenset({"f0", "f1", "f2"})
    roles = (("a", "b"), ("c",))
    weights = (Q(2), Q(3))
    loads = defaultdict(Q)
    total = Q(0)
    for wt in weights:
        for choices in product(*[([None] + list(role)) for role in roles]):
            output = base | frozenset(x for x in choices if x is not None)
            loads[output] += wt
            total += wt
    expected_per_context = (1 + len(roles[0])) * (1 + len(roles[1]))
    assert total == sum(weights) * expected_per_context == 30
    Lambda = max(loads.values())
    assert Lambda == 5
    assert len(loads) == expected_per_context == 6
    assert Q(len(loads)) == total / Lambda


def main():
    check_positive_anchored_chain()
    check_nested_barrier()
    check_semialgebraic_arithmetic()
    check_weighted_load_identity()
    print(
        "PASS: root-aware FPS extraction arithmetic, fixed-edge "
        "homogeneous nested-ear barrier, and exact weighted load"
    )


if __name__ == "__main__":
    main()
