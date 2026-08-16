#!/usr/bin/env python3
"""Exact checks for ALL_LOOP_NONSTRONG_TRANSVERSAL_BARRIER.md."""

from fractions import Fraction as Q
from itertools import combinations, product


Point = tuple[Q, Q]


def det(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def same_side(a, b, points):
    values = [det(a, b, p) for p in points]
    assert all(values)
    return all(v > 0 for v in values) or all(v < 0 for v in values)


def inside_triangle(p, a, b, c):
    values = [det(a, b, p), det(b, c, p), det(c, a, p)]
    return all(v > 0 for v in values) or all(v < 0 for v in values)


def hull(points):
    word = sorted(points)
    if len(word) <= 1:
        return word
    lower = []
    for p in word:
        while len(lower) >= 2 and det(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(word):
        while len(upper) >= 2 and det(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def is_face(points):
    return len(hull(points)) == len(points)


def build(m=3, k=2, alphabet=2):
    R = Q(10)
    delta = Q(1, 10)
    eta = Q(1, 100 * m * m)
    epsilon = Q(1, 10**8)

    a = (-R, Q(0))
    b = (Q(0), Q(1))
    c = (R, Q(0))
    anchors = [a, b, c]

    d_macro = [
        (eta * i, Q(1) + delta + eta * i * i)
        for i in range(1, m + 1)
    ]
    t_values = [Q(-R, 3), Q(R, 3)][:k]
    u_macro = [
        (t, (t * t - R * R) / (R * R))
        for t in t_values
    ]

    d_clusters = []
    for role, (x, y) in enumerate(d_macro):
        cluster = []
        for label in range(alphabet):
            z = label + 1
            cluster.append((
                x + epsilon * Q(z + role, 1),
                y + epsilon * epsilon * Q((role + 2) * z * z + z, 1),
            ))
        d_clusters.append(cluster)

    u_clusters = []
    for role, (x, y) in enumerate(u_macro):
        cluster = []
        for label in range(alphabet):
            z = label + 1
            cluster.append((
                x + epsilon * Q(3 * z + role, 1),
                y + epsilon * epsilon * Q((role + 5) * z * z + 2 * z, 1),
            ))
        u_clusters.append(cluster)
    return anchors, d_clusters, u_clusters


if __name__ == "__main__":
    anchors, d_clusters, u_clusters = build()
    a, b, c = anchors
    all_points = anchors + sum(d_clusters, []) + sum(u_clusters, [])

    # Exact general position.
    assert all(
        det(all_points[i], all_points[j], all_points[k]) != 0
        for i, j, k in combinations(range(len(all_points)), 3)
    )

    d_words = [
        tuple(d_clusters[i][choice] for i, choice in enumerate(word))
        for word in product(range(2), repeat=len(d_clusters))
    ]
    u_words = [
        tuple(anchors + [u_clusters[i][choice]
                         for i, choice in enumerate(word)])
        for word in product(range(2), repeat=len(u_clusters))
    ]

    assert all(is_face(word) for word in d_words)
    assert all(is_face(word) for word in u_words)

    # Every label has the same signed loop: b is hidden by a,c,x.
    for cluster in d_clusters:
        for x in cluster:
            assert inside_triangle(b, a, c, x)

    # Every nonempty partial source transversal is incompatible with every
    # U word, witnessed by the same anchors and any retained source label.
    partials = []
    choices = [range(-1, len(cluster)) for cluster in d_clusters]
    for word in product(*choices):
        trace = tuple(
            d_clusters[i][choice]
            for i, choice in enumerate(word) if choice >= 0
        )
        if trace:
            partials.append(trace)
    assert all(
        not is_face(tuple(source) + tuple(target))
        for source in partials for target in u_words
    )

    # U straddles every line through labels from two distinct D roles.
    straddled = 0
    for i, j in combinations(range(len(d_clusters)), 2):
        for x in d_clusters[i]:
            for y in d_clusters[j]:
                assert not same_side(x, y, anchors)
                straddled += 1

    # Therefore no side-respecting strong-glue block can retain two source
    # roles. The entire full-word family would have to collapse to at most
    # one role.
    assert len(d_words) == 2 ** len(d_clusters)
    collapsed_partial_count = 1 + sum(map(len, d_clusters))
    assert collapsed_partial_count == 7

    print(
        "PASS: fixed signed all-loop rectangle with convex source/target "
        f"words; Dwords={len(d_words)}, Uwords={len(u_words)}, "
        f"partials={len(partials)}, bad_pairs={len(partials)*len(u_words)}, "
        f"straddled_cross_role_pairs={straddled}, "
        f"one-role_collapse={collapsed_partial_count}"
    )
