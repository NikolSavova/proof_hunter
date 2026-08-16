#!/usr/bin/env python3
"""Exact audit for SEMIALGEBRAIC_CONSECUTIVE_TRIPLE_AUDIT.md."""

from __future__ import annotations

import json
from fractions import Fraction as Q
from itertools import product


Point = tuple[int, int]


def parabola(parameter: int) -> Point:
    return (parameter, parameter * parameter)


def orientation(a: Point, b: Point, c: Point) -> int:
    determinant = (b[0] - a[0]) * (c[1] - a[1]) - (
        b[1] - a[1]
    ) * (c[0] - a[0])
    return (determinant > 0) - (determinant < 0)


def coordinate_point(block: int, color: int, index: int, alphabet: int) -> Point:
    return parabola(3 * alphabet * block + 3 * index + color)


def primary_constant_audit() -> dict[str, object]:
    # FPS Corollary 1.2 with k=3,d=2,t=1,D=1 and epsilon=1/2.
    c0 = Q(1, 8 * 3**120)
    # The identity actually used is 2^(120 log_2 3)=3^120.
    assert c0.denominator == 8 * 3**120

    rows = []
    for rank in (12, 24, 48, 96):
        product_fraction = c0 ** (3 * rank)
        # Each coordinate appears in at most three processed triples.
        occurrence_counts = [
            sum(1 for start in range(rank - 2) if start <= i <= start + 2)
            for i in range(rank)
        ]
        assert max(occurrence_counts) <= 3
        assert sum(occurrence_counts) == 3 * (rank - 2)
        assert product_fraction > 0
        rows.append(
            {
                "rank": rank,
                "maximum_triple_occurrences": max(occurrence_counts),
                "loss_numerator_bits": product_fraction.numerator.bit_length(),
                "loss_denominator_bits": product_fraction.denominator.bit_length(),
            }
        )
    return {"c0_denominator": c0.denominator, "scales": rows}


def global_density_audit() -> dict[str, object]:
    rows = []
    for d in (2, 4, 8, 16):
        rank = 3 * d
        t = rank - 2
        family = 1 << (d * d)
        product_support = 1 << (3 * d * d)
        epsilon = Q(family, product_support)
        redundancy = 2 * d * d

        # FPS Corollary 1.2 at arity rank, dimension 2, t=rank-2.
        delta = epsilon**3 / (3 ** (40 * rank) * t**2)
        bank_lower = Q(product_support) * delta**rank
        expected = Q(family) / (
            (1 << ((3 * rank - 1) * redundancy))
            * 3 ** (40 * rank * rank)
            * t ** (2 * rank)
        )
        assert bank_lower == expected
        rows.append(
            {
                "d": d,
                "rank": rank,
                "log_family": d * d,
                "redundancy_bits": redundancy,
                "delta_num_bits": delta.numerator.bit_length(),
                "delta_den_bits": delta.denominator.bit_length(),
                "bank_num_bits": bank_lower.numerator.bit_length(),
                "bank_den_bits": bank_lower.denominator.bit_length(),
            }
        )
    return {"scales": rows}


def small_parabola_barrier_audit() -> dict[str, object]:
    d, alphabet = 2, 4
    rank = 3 * d
    words = tuple(product(range(alphabet), repeat=d))
    assert len(words) == alphabet**d == 16

    def source(word: tuple[int, ...]) -> tuple[Point, ...]:
        return tuple(
            coordinate_point(block, color, word[block], alphabet)
            for block in range(d)
            for color in range(3)
        )

    sources = {word: source(word) for word in words}
    assert len(set(sources.values())) == len(words)
    all_points = {
        coordinate_point(block, color, index, alphabet)
        for block in range(d)
        for color in range(3)
        for index in range(alphabet)
    }
    assert len(all_points) == rank * alphabet

    # All triples of distinct parabola points are noncollinear.
    ordered_points = sorted(all_points)
    for first in range(len(ordered_points)):
        for second in range(first + 1, len(ordered_points)):
            for third in range(second + 1, len(ordered_points)):
                assert orientation(
                    ordered_points[first],
                    ordered_points[second],
                    ordered_points[third],
                ) != 0

    # Every selected word is a positive consecutive chain.
    for points in sources.values():
        assert all(
            orientation(points[i], points[i + 1], points[i + 2]) > 0
            for i in range(rank - 2)
        )

    collisions_checked = 0
    for first_index, first_word in enumerate(words):
        for second_word in words[first_index + 1 :]:
            differing = next(
                block for block in range(d) if first_word[block] != second_word[block]
            )
            low = min(first_word[differing], second_word[differing])
            high = max(first_word[differing], second_word[differing])
            matching = tuple(
                coordinate_point(differing, color, high, alphabet)
                for color in range(3)
            )
            mixed = (
                coordinate_point(differing, 0, high, alphabet),
                coordinate_point(differing, 1, low, alphabet),
                coordinate_point(differing, 2, high, alphabet),
            )
            assert orientation(*matching) > 0
            assert orientation(*mixed) < 0

            # Exhaust the 2x2x2 cell generated by the two selected words;
            # it contains both orientation signs.
            cell_signs = {
                orientation(
                    coordinate_point(differing, 0, a, alphabet),
                    coordinate_point(differing, 1, b, alphabet),
                    coordinate_point(differing, 2, c, alphabet),
                )
                for a in (first_word[differing], second_word[differing])
                for b in (first_word[differing], second_word[differing])
                for c in (first_word[differing], second_word[differing])
            }
            assert cell_signs == {-1, 1}
            collisions_checked += 1
    assert collisions_checked == len(words) * (len(words) - 1) // 2

    return {
        "d": d,
        "alphabet": alphabet,
        "rank": rank,
        "ambient_points": len(all_points),
        "selected_words": len(words),
        "word_pairs_checked": collisions_checked,
    }


def scalable_barrier_audit() -> dict[str, object]:
    rows = []
    for d in (4, 8, 16, 32):
        alphabet = 1 << d
        rank = 3 * d
        ambient = rank * alphabet
        family = alphabet**d
        product_support = alphabet**rank
        assert ambient == 3 * d * (1 << d)
        assert family == 1 << (d * d)
        assert product_support == family**3
        assert Q(product_support, family) == family**2
        assert rank <= 3 * (ambient.bit_length() - 1)
        rows.append(
            {
                "d": d,
                "ambient_points": ambient,
                "log2_ambient_floor": ambient.bit_length() - 1,
                "rank": rank,
                "log2_family": family.bit_length() - 1,
                "support_redundancy_bits": (
                    (product_support // family).bit_length() - 1
                ),
                "minimum_homogeneous_cells_log2": family.bit_length() - 1,
            }
        )
    return {"scales": rows}


def main() -> None:
    result = {
        "primary_constants": primary_constant_audit(),
        "global_density": global_density_audit(),
        "small_parabola_barrier": small_parabola_barrier_audit(),
        "scalable_barrier": scalable_barrier_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: semialgebraic consecutive-triple audit verified")


if __name__ == "__main__":
    main()
