#!/usr/bin/env python3
"""Exact verifier for ROLE_COLORED_PROFILE_DICHOTOMY.md."""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
from math import log2


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


def strict_inside_triangle(point, a, b, c):
    signs = (cross(a, b, point), cross(b, c, point), cross(c, a, point))
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def role_coloring_audit(n=6, rank=3):
    faces = tuple(combinations(range(n), rank))
    aligned_counts = []
    for coloring in product(range(rank), repeat=n):
        aligned_counts.append(
            sum(all(coloring[face[i]] == i for i in range(rank)) for face in faces)
        )
    # Sum over colourings can be counted face first: each face fixes t
    # colours and leaves n-t arbitrary.
    exact_sum = len(faces) * rank ** (n - rank)
    assert sum(aligned_counts) == exact_sum
    assert max(aligned_counts) * rank**n >= len(faces) * rank**n // rank**rank
    assert max(aligned_counts) >= len(faces) / rank**rank
    return {
        "points": n,
        "rank": rank,
        "faces": len(faces),
        "colourings": rank**n,
        "aligned_sum": exact_sum,
        "maximum_aligned": max(aligned_counts),
    }


def entropy(distribution):
    counts = Counter(distribution)
    total = len(distribution)
    return -sum((count / total) * log2(count / total) for count in counts.values())


def tc(words, indices):
    joint = [tuple(word[i] for i in indices) for word in words]
    return sum(entropy([word[i] for word in words]) for i in indices) - entropy(joint)


def transcript_tc_audit():
    # A correlated but nonproduct law on five binary coordinates.
    words = tuple(
        word for word in product(range(2), repeat=5)
        if (word[0] + word[1] + word[3]) % 2 == 0 or word[4] == word[2]
    )
    full_entropy = entropy(words)
    marginal_entropy = [entropy([word[i] for word in words]) for i in range(5)]
    total_correlation = sum(marginal_entropy) - full_entropy

    prefixes = []
    a = [0.0]
    for i in range(1, 5):
        prefix_entropy = entropy([word[:i] for word in words])
        extended_entropy = entropy([word[: i + 1] for word in words])
        conditional_entropy = extended_entropy - prefix_entropy
        a.append(marginal_entropy[i] - conditional_entropy)
    assert abs(sum(a) - total_correlation) < 1e-10

    predicates = ((0, 1, 2), (1, 2, 4), (0, 3, 4), (2, 3))
    degree = [0] * 5
    local_sum = 0.0
    for indices in predicates:
        local_sum += tc(words, indices)
        for index in sorted(indices)[1:]:
            degree[index] += 1
    delta = max(degree)
    assert local_sum <= delta * total_correlation + 1e-10
    return {
        "words": len(words),
        "total_correlation": total_correlation,
        "local_tc_sum": local_sum,
        "nonfirst_degree": degree,
        "Delta": delta,
    }


def bad_product_audit():
    # Four tiny affine copies of the nonconvex order type
    # (1,0),(2,4),(3,1),(4,0), generically perturbed.  The macro centres
    # form a diamond around the root.  All arithmetic is integral.
    root = (0, 0)
    clusters = (
        ((40112, 17), (40200, 417), (40298, 84), (40412, 8)),
        ((-19884, 30005), (-19781, 30397), (-19703, 30110), (-19599, 29995)),
        ((-39920, 12), (-39792, 417), (-39683, 80), (-39614, -13)),
        ((-19907, -30005), (-19809, -29594), (-19710, -29887), (-19580, -30012)),
    )
    points = (root,) + sum(clusters, ())
    assert all(cross(a, b, c) != 0 for a, b, c in combinations(points, 3))
    assert all(not convex(cluster) and len(hull(cluster)) == 3 for cluster in clusters)

    words = tuple(product(range(4), repeat=4))
    circuit_signatures = set()
    consecutive_signatures = set()
    for word in words:
        face = [clusters[i][word[i]] for i in range(4)]
        assert convex(face)
        assert strict_inside_triangle(root, face[0], face[1], face[3])
        assert not convex([root] + face)
        circuit_signatures.add(
            (
                cross(face[0], face[1], root) > 0,
                cross(face[1], face[3], root) > 0,
                cross(face[3], face[0], root) > 0,
            )
        )
        consecutive_signatures.add(
            (cross(face[0], face[1], face[2]) > 0,
             cross(face[1], face[2], face[3]) > 0)
        )
    assert len(circuit_signatures) == 1
    assert consecutive_signatures == {(True, True)}
    support_sizes = [len({word[i] for word in words}) for i in range(4)]
    box = 1
    for size in support_sizes:
        box *= size
    assert support_sizes == [4, 4, 4, 4]
    assert box == len(words) == 256  # R=0 exactly.
    return {
        "points_including_root": len(points),
        "child_order_types": 4,
        "each_child_nonconvex": True,
        "transversals": len(words),
        "support_box": box,
        "support_redundancy": 0,
        "consecutive_sign_patterns": len(consecutive_signatures),
        "fixed_root_circuit_patterns": len(circuit_signatures),
        "root_admissible_transversals": 0,
    }


def main():
    results = {
        "role_coloring": role_coloring_audit(),
        "bounded_degree_tc": transcript_tc_audit(),
        "bad_product": bad_product_audit(),
    }
    print("ROLE_COLORED_PROFILE_DICHOTOMY verifier: PASS")
    for name, result in results.items():
        print(f"{name}: {result}")


if __name__ == "__main__":
    main()
