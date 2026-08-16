#!/usr/bin/env python3
"""Exact audits for PLANAR_ANTI_INCIDENCE.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement, permutations
from math import ceil, comb, log2


def tangent_point(left: int, right: int) -> tuple[Fraction, Fraction]:
    """Inverse of (ell,r) in the normalized upper wedge."""
    total = left + right
    return Fraction(left - right, total), Fraction(2, total)


def orient(a, b, c) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (
        b[1] - a[1]
    ) * (c[0] - a[0])


def in_triangle_strict(z, u, v, p) -> bool:
    signs = (orient(u, v, z), orient(v, p, z), orient(p, u, z))
    boundary = (orient(u, v, p), orient(v, p, u), orient(p, u, v))
    return all(x * y > 0 for x, y in zip(signs, boundary))


def verify_tangent_dominance() -> int:
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    checks = 0
    for lp in range(1, 8):
        for rp in range(1, 8):
            p = tangent_point(lp, rp)
            for lz in range(1, 8):
                for rz in range(1, 8):
                    if (lp, rp) == (lz, rz):
                        continue
                    z = tangent_point(lz, rz)
                    geometric = in_triangle_strict(z, u, v, p)
                    dominance = lz > lp and rz > rp
                    # Equality is a root collinearity and is excluded by
                    # planar general position; strict cases are exact.
                    if lz != lp and rz != rp:
                        assert geometric == dominance
                        checks += 1
    return checks


def dominance_neighborhoods(perm: tuple[int, ...]) -> tuple[int, ...]:
    """All distinct northeast-orthant traces on a permutation point set."""
    n = len(perm)
    traces = set()
    # Point i has x-rank i and y-rank perm[i].
    for x_cut in range(n + 1):
        for y_cut in range(n + 1):
            mask = 0
            for i, y in enumerate(perm):
                if i >= x_cut and y >= y_cut:
                    mask |= 1 << i
            traces.add(mask)
    return tuple(sorted(traces))


def edges(masks: tuple[int, ...]) -> int:
    return sum(mask.bit_count() for mask in masks)


def max_pair_codegree(masks: tuple[int, ...]) -> int:
    result = 0
    for i in range(len(masks)):
        for j in range(i + 1, len(masks)):
            result = max(result, (masks[i] & masks[j]).bit_count())
    return result


def verify_orthant_bound() -> int:
    checks = 0
    # Exhaustive over all point orders and multisets of at most four
    # orthants.  Repeated traces are allowed, so the codegree condition is
    # tested exactly rather than assuming distinct geometric thresholds.
    for n in range(1, 6):
        depth = ceil(log2(n)) + 1
        for perm in permutations(range(n)):
            traces = dominance_neighborhoods(perm)
            for b in range(1, 5):
                for family in combinations_with_replacement(traces, b):
                    lam = max(1, max_pair_codegree(family))
                    assert edges(family) <= (n + lam * b) * depth
                    checks += 1
    return checks


def projective_parameters(q: int) -> tuple[int, int, int]:
    n = q * q + q + 1
    degree = q + 1
    return n, degree, n * degree


def verify_projective_exclusion() -> list[tuple[int, int, int]]:
    rows = []
    for q in (2, 3, 5, 31, 61, 127):
        n, degree, incidence = projective_parameters(q)
        bound = 2 * n * (ceil(log2(n)) + 1)
        if q >= 31:
            assert incidence > bound
        rows.append((q, incidence, bound))
    return rows


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def next_prime(value: int) -> int:
    while not is_prime(value):
        value += 1
    return value


def verify_tensor_reuse() -> list[tuple[int, int, int, int]]:
    rows = []
    for h in range(2, 9):
        q = next_prime(2**h)
        n, d, base_edges = projective_parameters(q)
        # Give the hypothetical realization the generous parameters used
        # in the report: ambient labels 2hN, rank K=2h+2.
        ambient = 2 * h * n
        depth = ceil(log2(ambient)) + 1
        rank = 2 * h + 2
        occurrences = h * base_edges**h
        advertised_faces = n**h
        denominator = 2 * depth * rank * (rank - 1) * advertised_faces
        forced_reuse = (occurrences + denominator - 1) // denominator
        elementary = (h * d**h + 2 * depth * rank * (rank - 1) - 1) // (
            2 * depth * rank * (rank - 1)
        )
        assert forced_reuse == elementary
        assert forced_reuse >= 1
        rows.append((h, q, forced_reuse, forced_reuse.bit_length() - 1))
    return rows


def verify_star_partition_deficit() -> list[tuple[int, int, int, int]]:
    """Cell IDs are retained point words, but neighbor words remain d^h."""
    rows = []
    for q in (2, 3, 5, 7, 11):
        n, d, base_edges = projective_parameters(q)
        assert base_edges == n * d
        for h in (1, 2, 3, 4):
            point_words = n**h
            cell_sequences = point_words
            edge_words = base_edges**h
            conditional_words = edge_words // cell_sequences
            assert conditional_words == d**h
            rows.append((q, h, cell_sequences, conditional_words))
    return rows


def main() -> None:
    tangent = verify_tangent_dominance()
    orthant = verify_orthant_bound()
    projective = verify_projective_exclusion()
    tensor = verify_tensor_reuse()
    stars = verify_star_partition_deficit()
    print(f"tangent dominance: {tangent} exact strict comparisons PASS")
    print(f"orthant theorem: {orthant} exhaustive families PASS")
    print("projective rows (q, incidences, orthant bound):")
    for row in projective:
        print(" ", row)
    print("tensor rows (h, q, forced reuse, floor(log2 reuse)):")
    for row in tensor:
        print(" ", row)
    print(
        "star cell-ID audit: "
        f"{len(stars)} exact (q,h) instances, conditional words=d^h PASS"
    )
    print("PLANAR ANTI-INCIDENCE AUDIT PASS")


if __name__ == "__main__":
    main()
