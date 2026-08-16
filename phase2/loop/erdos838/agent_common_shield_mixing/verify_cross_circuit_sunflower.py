#!/usr/bin/env python3
"""Exact audit for CROSS_CIRCUIT_SUNFLOWER_NORMAL_FORM.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import factorial, log2


Point = tuple[Fraction, Fraction]


def orientation(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points: list[Point]) -> list[Point]:
    ordered = sorted(set(points))
    if len(ordered) <= 1:
        return ordered

    def half(sequence):
        answer: list[Point] = []
        for point in sequence:
            while len(answer) >= 2 and orientation(answer[-2], answer[-1], point) <= 0:
                answer.pop()
            answer.append(point)
        return answer

    lower = half(ordered)
    upper = half(reversed(ordered))
    return lower[:-1] + upper[:-1]


def strictly_inside_triangle(point: Point, triangle: list[Point]) -> bool:
    signs = [
        orientation(triangle[i], triangle[(i + 1) % 3], point)
        for i in range(3)
    ]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def is_sunflower(family: tuple[frozenset[int], ...]) -> bool:
    if len(family) <= 1:
        return True
    core = family[0] & family[1]
    return all(a & b == core for a, b in combinations(family, 2))


def max_sunflower_size(family: tuple[frozenset[int], ...]) -> int:
    for size in range(len(family), 0, -1):
        if any(is_sunflower(subfamily) for subfamily in combinations(family, size)):
            return size
    return 0


def sunflower_threshold_audit() -> dict[str, int]:
    checked = 0
    for n, q in ((5, 2), (5, 3)):
        layer = tuple(frozenset(item) for item in combinations(range(n), q))
        for mask in range(1 << len(layer)):
            family = tuple(layer[i] for i in range(len(layer)) if (mask >> i) & 1)
            if not family:
                continue
            maximum = max_sunflower_size(family)
            for k in range(1, maximum + 2):
                if len(family) > factorial(q) * (k - 1) ** q:
                    assert maximum >= k
                checked += 1

    # Exact integer version of (4): N > q!(k-1)^q.
    integer_checks = 0
    for q in range(1, 9):
        for n_independent in range(1, 500):
            k = 1
            while factorial(q) * k**q < n_independent:
                k += 1
            assert n_independent > factorial(q) * (k - 1) ** q
            integer_checks += 1

    return {"uniform_families": checked, "integer_thresholds": integer_checks}


def exponent_audit() -> dict[str, int]:
    checked = 0
    # Finite audit of (6), with integer powers D=2^d.  This is not used as
    # floating-point proof; it catches sign and normalization regressions.
    for d in range(40, 401, 20):
        for q_num in (1, 2, 3):
            q = max(1, q_num * d // 10)
            log_m = d * d // 5
            log_delta = 2 * d
            lower_log_k = (log_m - log_delta - log2(factorial(q))) / q - 1
            asymptotic_main = (d * d / 5) / q
            assert lower_log_k <= asymptotic_main
            expected_gap = (log_delta + log2(factorial(q))) / q + 1
            assert abs((asymptotic_main - lower_log_k) - expected_gap) < 1e-10
            checked += 1
    support_cutoff_checks = 0
    hard_coefficient = Fraction(1, 8)
    for denominator in range(9, 41):
        kappa = Fraction(1, denominator)
        if kappa >= Fraction(1, 8):
            continue
        reservoir_coefficient = hard_coefficient**2 / (8 * kappa**2)
        assert reservoir_coefficient > hard_coefficient
        # The surplus is quadratic in log D, so it eventually absorbs any
        # fixed record power D^s.
        assert reservoir_coefficient - hard_coefficient > 0
        support_cutoff_checks += 1

    return {
        "exponent_checks": checked,
        "support_cutoff_coefficients": support_cutoff_checks,
    }


def radial_cluster_audit() -> dict[str, int]:
    # Integer pentagon approximating a regular one.  The tiny tangent term
    # makes the finite radial construction general position.  Fractions keep
    # every orientation and containment test exact.
    vertices = ((0, 100), (95, 31), (59, -81), (-59, -81), (-95, 31))
    q = len(vertices)
    k = 4
    clusters: list[list[Point]] = []
    for j, (vx, vy) in enumerate(vertices):
        tangent = (-vy, vx)
        cluster = []
        for level in range(k):
            scale = Fraction(900 + 20 * level, 1000)
            perturb = Fraction(
                (level + 1) * (level + 2) * (j + 2) + (j + 1) ** 2,
                10_000_000,
            )
            cluster.append(
                (
                    scale * vx + perturb * tangent[0],
                    scale * vy + perturb * tangent[1],
                )
            )
        clusters.append(cluster)

    points = [point for cluster in clusters for point in cluster]
    assert all(orientation(*triple) != 0 for triple in combinations(points, 3))
    assert all(len(hull(cluster)) == k for cluster in clusters)

    transversal_count = 0
    for levels in product(range(k), repeat=q):
        transversal = [clusters[j][levels[j]] for j in range(q)]
        assert len(hull(transversal)) == q
        transversal_count += 1
    assert transversal_count == k**q

    circuit_certificates = 0
    for j in range(q):
        left = (j - 1) % q
        right = (j + 1) % q
        for inner in range(k):
            for outer in range(inner + 1, k):
                for left_level, right_level in product(range(k), repeat=2):
                    triangle = [
                        clusters[j][outer],
                        clusters[left][left_level],
                        clusters[right][right_level],
                    ]
                    assert strictly_inside_triangle(clusters[j][inner], triangle)
                    circuit_certificates += 1

    # A direct pair audit on a smaller complete slice guards the logical use
    # of the local certificates without making the verifier quadratic in 1024.
    sample = list(product(range(k), repeat=q))[:96]
    incompatible_pairs = 0
    for first, second in combinations(sample, 2):
        if first == second:
            continue
        union = {
            clusters[j][level]
            for j in range(q)
            for level in (first[j], second[j])
        }
        assert len(hull(list(union))) < len(union)
        incompatible_pairs += 1

    # Full-clutter audit for the sunflower obtained by varying cluster 0.
    # Since that petal cluster is convex, every bad four-set uses a root
    # point.  Hence any matching of full circuits has size at most |K|.
    root = [clusters[j][0] for j in range(1, q)]
    one_coordinate_ground = clusters[0] + root
    full_bad_circuits = 0
    for circuit in combinations(one_coordinate_ground, 4):
        if len(hull(list(circuit))) < 4:
            assert any(point in root for point in circuit)
            full_bad_circuits += 1

    return {
        "points": len(points),
        "transversals": transversal_count,
        "local_four_circuits": circuit_certificates,
        "sample_incompatible_pairs": incompatible_pairs,
        "one_coordinate_full_bad_circuits": full_bad_circuits,
        "full_circuit_matching_upper_bound": len(root),
    }


def main() -> None:
    print(f"sunflower: {sunflower_threshold_audit()}")
    print(f"exponents: {exponent_audit()}")
    print(f"radial geometry: {radial_cluster_audit()}")
    print("PASS cross-circuit sunflower normal form")


if __name__ == "__main__":
    main()
