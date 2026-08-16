#!/usr/bin/env python3
"""Exact audit for SAME_TYPE_POSITIVE_FRACTION_POCKET_COEXISTENCE_GATE."""

from __future__ import annotations

import itertools
import math
from fractions import Fraction as F


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for point in points:
        while len(lower) >= 2 and det(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and det(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(points) == len(set(points)) == len(hull(points))


def barycentric(point, triangle):
    a, b, c = triangle
    denominator = det(a, b, c)
    return (
        det(point, b, c) / denominator,
        det(a, point, c) / denominator,
        det(a, b, point) / denominator,
    )


def avoids(first, second):
    for a, b in itertools.combinations(first, 2):
        signs = [det(a, b, point) for point in second]
        if min(signs) < 0 < max(signs):
            return False
    return True


def mutually_avoiding_rank_four_audit():
    first = ((3, 2), (4, 1), (1, 1))
    second = ((2, -6), (-5, -6), (-1, -5))
    points = first + second
    assert all(det(*triple) != 0 for triple in itertools.combinations(points, 3))
    assert avoids(first, second) and avoids(second, first)
    assert len(hull(points)) == 5 < 6
    four_faces = 0
    for pair_first in itertools.combinations(first, 2):
        for pair_second in itertools.combinations(second, 2):
            assert convex(pair_first + pair_second)
            four_faces += 1
    assert four_faces == 9
    return len(hull(points)), four_faces


def pocket_and_clouds(m=14, alphabet=3):
    delta = F(1, 100 * m * m)
    pocket = tuple(
        (F(2) - delta * t * t, -F(1, 5) + delta * t)
        for t in range(1, m + 1)
    )
    centers = ((F(4), F(0)), (F(0), F(4)), (F(0), F(0)))
    offsets = (
        ((2, 7), (-10, 7), (15, 22)),
        ((25, -12), (-26, 2), (-2, 28)),
        ((6, 15), (-5, 9), (-13, -13)),
    )
    epsilon = F(1, 10**7)
    clouds = tuple(
        tuple(
            (center[0] + epsilon * dx, center[1] + epsilon * dy)
            for dx, dy in cloud_offsets[:alphabet]
        )
        for center, cloud_offsets in zip(centers, offsets)
    )
    return pocket, clouds


def repeated_block_pocket_barrier():
    pocket, clouds = pocket_and_clouds()
    all_points = pocket + tuple(itertools.chain.from_iterable(clouds))
    assert all(
        det(*triple) != 0 for triple in itertools.combinations(all_points, 3)
    )

    # Every one-from-each-block transversal has one common convex type.
    type_vectors = set()
    transversals = 0
    for point, b, c, a in itertools.product(pocket, *clouds):
        word = (point, b, c, a)
        vector = tuple(
            1 if det(word[i], word[j], word[k]) > 0 else -1
            for i, j, k in itertools.combinations(range(4), 3)
        )
        assert vector == (1, 1, 1, 1)
        assert convex(word)
        type_vectors.add(vector)
        transversals += 1
    assert type_vectors == {(1, 1, 1, 1)}
    assert transversals == 14 * 3**3

    # Every pocket triple is killed by every choice in the guard cloud.
    containments = 0
    guard_cloud = clouds[1]
    for i, j, k in itertools.combinations(range(len(pocket)), 3):
        for guard in guard_cloud:
            coordinates = barycentric(
                pocket[j], (pocket[i], pocket[k], guard)
            )
            assert sum(coordinates, F()) == 1
            assert all(value > 0 for value in coordinates)
            containments += 1
    assert containments == math.comb(14, 3) * 3

    pocket_faces = (1 << 14) - 1
    compatible_rank_at_most_two = 1 + 14 + math.comb(14, 2)
    external_full_words = 3**3
    formal_product = pocket_faces * external_full_words
    mixed_upper = compatible_rank_at_most_two * external_full_words
    assert mixed_upper < formal_product // 100
    return (
        transversals, containments, pocket_faces,
        external_full_words, mixed_upper, formal_product,
    )


def extraction_arithmetic():
    rows = []
    # A completely explicit conservative pipeline: ES(k)<=4^k and the
    # planar Bukh--Vasileuski fraction 2^-400 m^-4 after partitioning into m
    # input parts.  The sharp ES(k)=2^(k+o(k)) only improves the lower-order
    # term.
    for ell in (1024, 1536, 2048, 3072, 4096):
        n = 1 << ell
        k = int(math.log2(ell))
        input_parts = 1 << (2 * k)
        denominator = (1 << 400) * input_parts**5
        block = n // denominator
        assert block > 1
        log_bank = k * math.log2(1 + block)
        assert log_bank >= 0.45 * k * ell
        rows.append((ell, k, input_parts, block.bit_length(), log_bank))
    return rows


def mirzaei_suk_capacity_arithmetic():
    rows = []
    # Ignore the absolute theorem constant and use s=n/k^4.  Its immediate
    # hereditary convex guarantee is the 2+2 bank, of polynomial rank four.
    for ell in (32, 48, 64, 96, 128):
        n = 1 << ell
        k = ell
        block = n // k**4
        rank_four = math.comb(k, 2) ** 2 * block**4
        log_rank_four = math.log2(rank_four)
        assert log_rank_four < 4 * ell
        assert 4 * ell - log_rank_four < 20 * math.log2(ell)
        rows.append((ell, k, block.bit_length(), rank_four.bit_length()))
    return rows


def conditional_splice_arithmetic():
    pocket_faces = 37
    role_sizes = (3, 5, 7, 11)
    multiplier = math.prod(1 + size for size in role_sizes)
    outputs = pocket_faces * multiplier
    encoded = {
        (face, choices)
        for face in range(pocket_faces)
        for choices in itertools.product(
            *(range(size + 1) for size in role_sizes)
        )
    }
    assert len(encoded) == outputs
    return pocket_faces, multiplier, outputs


def main():
    avoiding = mutually_avoiding_rank_four_audit()
    barrier = repeated_block_pocket_barrier()
    extraction = extraction_arithmetic()
    mirzaei = mirzaei_suk_capacity_arithmetic()
    splice = conditional_splice_arithmetic()
    print(
        "PASS: same-type/positive-fraction pocket gate; avoiding=%s; "
        "barrier=%s; extraction L=%d..%d; Mirzaei L=%d..%d; splice=%s"
        % (
            avoiding, barrier, extraction[0][0], extraction[-1][0],
            mirzaei[0][0], mirzaei[-1][0], splice,
        )
    )


if __name__ == "__main__":
    main()
