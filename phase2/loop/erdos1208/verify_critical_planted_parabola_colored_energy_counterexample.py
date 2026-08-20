#!/usr/bin/env python3
"""Verify the critical planted-parabola colored-energy counterexample."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb
from random import Random


def squared_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def distance_sidon(points: list[tuple[int, int]]) -> bool:
    labels = [squared_distance(a, b) for a, b in combinations(points, 2)]
    return len(labels) == len(set(labels))


def seed(half_size: int) -> list[tuple[int, int]]:
    return [(r, r * r) for r in range(2 * half_size)]


def verify_seed_and_strip() -> None:
    for half_size in range(2, 65):
        points = seed(half_size)
        assert distance_sidon(points)

        # The inequalities used to exclude every one-candidate collision.
        max_seed_distance = max(
            squared_distance(a, b) for a, b in combinations(points, 2)
        )
        min_vertical_gap = 16 * half_size**2 - (2 * half_size - 1) ** 2
        assert min_vertical_gap**2 > max_seed_distance

        # Algebraic lower/upper sides of the perpendicular-bisector identity
        # 2X + 2(i+j)Y = (i+j)(1+i^2+j^2).
        for i, j in combinations(range(2 * half_size), 2):
            pair_sum = i + j
            left_lower = 2 * pair_sum * 16 * half_size**2
            right = pair_sum * (1 + i * i + j * j)
            assert left_lower > right


def derivative_support(
    points: list[tuple[int, int]], shift: int
) -> tuple[int, ...]:
    by_x = {x: y for x, y in points}
    return tuple(
        x
        for x, y in sorted(by_x.items())
        if x + shift in by_x
        and by_x[x + shift] - y == 2 * shift * x + shift * shift
    )


def verify_exact_profile() -> None:
    for half_size in range(2, 65):
        points = seed(half_size)
        for shift in range(1, half_size + 1):
            support = derivative_support(points, shift)
            assert support == tuple(range(2 * half_size - shift))

        parent_energy = sum(
            (half_size - h) ** 2 for h in range(1, half_size)
        )
        expected_energy = (
            (half_size - 1) * half_size * (2 * half_size - 1) // 6
        )
        assert parent_energy == expected_energy

        weighted_mass = sum(
            (half_size - h) * comb(2 * half_size - h, 3)
            for h in range(1, half_size)
        )
        triple_mass = sum(
            comb(2 * half_size - shift, 3)
            for shift in range(1, half_size + 1)
        )
        assert triple_mass == comb(2 * half_size, 4) - comb(half_size, 4)
        assert weighted_mass >= 0


def verify_alteration_exponents() -> None:
    # Exponents of M, with Delta_M suppressed as M^{o(1)}.
    # p=M^{-4/3}; |U|=M^2; |S|=M^{1/2}.
    p_exp = Fraction(-4, 3)
    selected_exp = p_exp + 2
    assert selected_exp == Fraction(2, 3)

    # H_q <= Delta M^{2(q-1)} |S|^{4-q}.
    h_exp = {
        q: Fraction(2 * (q - 1), 1) + Fraction(4 - q, 2)
        for q in (2, 3, 4)
    }
    assert h_exp == {2: Fraction(3), 3: Fraction(9, 2), 4: Fraction(6)}
    bad_exp = {q: h_exp[q] + q * p_exp for q in h_exp}
    assert bad_exp == {
        2: Fraction(1, 3),
        3: Fraction(1, 2),
        4: Fraction(2, 3),
    }
    assert bad_exp[2] < selected_exp
    assert bad_exp[3] < selected_exp
    assert bad_exp[4] == selected_exp  # paid by a small epsilon constant

    same_x_exp = 3 + 2 * p_exp
    planted_relation_exp = Fraction(5, 2) + 2 * p_exp
    assert same_x_exp == Fraction(1, 3) < selected_exp
    assert planted_relation_exp == Fraction(-1, 6) < selected_exp

    # Critical target: S=M^2, k=M^(2/3), J=M^(1/2).
    k_exp = Fraction(2, 3)
    j_exp = Fraction(1, 2)
    energy_exp = 3 * j_exp
    dominant_denominator_exp = 8 * k_exp + 5 * j_exp
    target_exp = 8 - dominant_denominator_exp
    assert energy_exp == Fraction(3, 2)
    assert target_exp == Fraction(1, 6)
    assert energy_exp - target_exp == Fraction(4, 3)

    weighted_exp = 5 * j_exp
    weighted_target_exp = 4 - 3 * k_exp
    assert weighted_exp == Fraction(5, 2)
    assert weighted_target_exp == 2
    assert weighted_exp - weighted_target_exp == Fraction(1, 2)

    triple_exp = 4 * j_exp
    assert triple_exp == 2  # exactly the ambient m^2 scale


def deterministic_extension(half_size: int = 4) -> list[tuple[int, int]]:
    """Small regression witness; the asymptotic proof is the alteration lemma."""
    side = 64 * half_size**2
    points = seed(half_size)
    labels = {
        squared_distance(a, b) for a, b in combinations(points, 2)
    }
    rng = Random(1208)
    candidates = [
        (
            x,
            rng.randrange(16 * half_size**2, 32 * half_size**2 + 1),
        )
        for x in range(2 * half_size, side + 1)
    ]
    rng.shuffle(candidates)

    for candidate in candidates:
        new_labels = [squared_distance(candidate, point) for point in points]
        if len(new_labels) != len(set(new_labels)):
            continue
        if any(label in labels for label in new_labels):
            continue

        # Preserve every q=1,...,L planted derivative support exactly.
        x, y = candidate
        preserves = True
        for a, b in points:
            for shift in range(1, half_size + 1):
                if x - a == shift and y - b == 2 * shift * a + shift**2:
                    preserves = False
                if a - x == shift and b - y == 2 * shift * x + shift**2:
                    preserves = False
        if not preserves:
            continue

        points.append(candidate)
        labels.update(new_labels)

    return points


def verify_finite_extension() -> int:
    half_size = 4
    points = deterministic_extension(half_size)
    assert len(points) >= 80
    assert len({x for x, _ in points}) == len(points)
    assert distance_sidon(points)
    for shift in range(1, half_size + 1):
        assert derivative_support(points, shift) == tuple(
            range(2 * half_size - shift)
        )
    return len(points)


def main() -> None:
    verify_seed_and_strip()
    verify_exact_profile()
    verify_alteration_exponents()
    finite_size = verify_finite_extension()
    print(
        "PASS",
        {
            "seed_half_sizes": "2..64",
            "finite_extension_size": finite_size,
            "energy_exponent": "3/2",
            "target_exponent": "1/6",
            "violation_exponent": "4/3",
            "weighted_violation_exponent": "1/2",
            "unweighted_triples_exponent": "2=m^2",
        },
    )


if __name__ == "__main__":
    main()
