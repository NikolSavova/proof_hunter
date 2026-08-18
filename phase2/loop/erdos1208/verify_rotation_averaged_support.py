#!/usr/bin/env python3
"""Exact checks for the rotation-averaged cubic-support lemma."""

from collections import Counter
from fractions import Fraction

from verify_adversarial_support_witnesses import WITNESSES


Point = tuple[int, int]
RationalPoint = tuple[Fraction, Fraction]
Rotation = tuple[Fraction, Fraction]


def is_distance_sidon(points: list[Point]) -> bool:
    norms: set[int] = set()
    for i, a in enumerate(points):
        for b in points[:i]:
            norm = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
            if norm in norms:
                return False
            norms.add(norm)
    return True


def rotate(rotation: Rotation, point: Point) -> RationalPoint:
    cosine, sine = rotation
    x, y = point
    return cosine * x - sine * y, sine * x + cosine * y


def fibre_profile(
    points: list[Point], rotation: Rotation
) -> tuple[int, int, int]:
    fibres: Counter[RationalPoint] = Counter()
    for a in points:
        for b in points:
            for c in points:
                difference = b[0] - c[0], b[1] - c[1]
                rx, ry = rotate(rotation, difference)
                fibres[Fraction(a[0]) + rx, Fraction(a[1]) + ry] += 1
    support = len(fibres)
    energy = sum(value * value for value in fibres.values())
    peak = max(fibres.values())
    return support, energy, peak


def main() -> None:
    points = WITNESSES[12]
    assert is_distance_sidon(points)
    rotations: list[Rotation] = [
        (Fraction(1), Fraction(0)),
        (Fraction(-1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(-1)),
        (Fraction(3, 5), Fraction(4, 5)),
        (Fraction(3, 5), Fraction(-4, 5)),
        (Fraction(-3, 5), Fraction(4, 5)),
        (Fraction(-3, 5), Fraction(-4, 5)),
        (Fraction(5, 13), Fraction(12, 13)),
        (Fraction(5, 13), Fraction(-12, 13)),
        (Fraction(-5, 13), Fraction(12, 13)),
        (Fraction(-5, 13), Fraction(-12, 13)),
    ]
    assert len(set(rotations)) == len(rotations)
    assert all(cosine * cosine + sine * sine == 1 for cosine, sine in rotations)

    profiles = [fibre_profile(points, rotation) for rotation in rotations]
    k = len(points)
    r = len(rotations)
    total_energy = sum(energy for _, energy, _ in profiles)
    theorem_bound = r * (2 * k**3 - k**2) + 2 * k**4
    assert total_energy <= theorem_bound
    for support, energy, _ in profiles:
        assert support * energy >= k**6

    best_support, best_energy, best_peak = min(
        profiles, key=lambda profile: profile[1]
    )
    average_bound = 2 * k**3 - k**2 + Fraction(2 * k**4, r)
    assert best_energy <= average_bound
    assert best_support * best_energy >= k**6
    assert best_support >= Fraction(k**6, average_bound)

    print("points", k, "rotations", r)
    print("total_energy", total_energy, "bound", theorem_bound)
    print("best", best_support, best_energy, best_peak)
    print("fixed_quarter_turn", profiles[2])
    print("PASS")


if __name__ == "__main__":
    main()
