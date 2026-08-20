#!/usr/bin/env python3
"""Verify the one-dimensional minimum gate and parabola barrier."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb


def distance_sidon_parabola(size: int) -> bool:
    seen: set[int] = set()
    for first, second in combinations(range(size), 2):
        norm = (second - first) ** 2 * (1 + (second + first) ** 2)
        if norm in seen:
            return False
        seen.add(norm)
    return True


def interval_difference_load(size: int, shift: int) -> int:
    return max(0, size - abs(shift))


def endpoint_correlation(size: int, shift: int) -> int:
    return sum(
        interval_difference_load(size, difference)
        * interval_difference_load(size, difference - shift)
        for difference in range(-(size - 1), size)
    )


def additive_energy_interval(size: int) -> int:
    return sum(
        interval_difference_load(size, difference) ** 2
        for difference in range(-(size - 1), size)
    )


def profile(root_size: int, check_distances: bool) -> tuple[int, ...]:
    richness = root_size
    size = root_size * root_size
    if check_distances:
        assert distance_sidon_parabola(size)

    # One full derivative line at each selected shift.
    selected_shifts = tuple(range(size - 2 * richness + 1, size - richness + 1))
    assert len(selected_shifts) == richness
    patch_load = {shift: 1 for shift in selected_shifts}
    for shift in selected_shifts:
        occupancy = interval_difference_load(size, shift)
        assert richness <= occupancy < 2 * richness
        assert comb(richness, 2) <= comb(occupancy, 2)

    parent_pair_load = {
        h: sum(
            patch_load.get(shift, 0) * patch_load.get(shift - h, 0)
            for shift in selected_shifts
        )
        for h in range(1, richness)
    }
    assert parent_pair_load == {
        h: richness - h for h in range(1, richness)
    }

    raw_endpoint_mass = 0
    actual_weighted_mass = 0
    minimum_weighted_mass = Fraction(0)
    for h in range(1, richness):
        q_value = endpoint_correlation(size, h)
        child_mass = comb(size - h, 3)
        parent_value = parent_pair_load[h]
        assert parent_value * (richness - 1) ** 2 <= q_value
        raw_endpoint_mass += q_value * child_mass
        actual_weighted_mass += parent_value * child_mass
        minimum_weighted_mass += min(
            Fraction(parent_value),
            Fraction(q_value, (richness - 1) ** 2),
        ) * child_mass
    assert minimum_weighted_mass == actual_weighted_mass

    # Exact elementary correlation and patch budgets.
    energy = additive_energy_interval(size)
    assert endpoint_correlation(size, 0) == energy
    assert energy <= size**3
    if size <= 256:
        assert sum(
            endpoint_correlation(size, h)
            for h in range(-2 * (size - 1), 2 * (size - 1) + 1)
        ) == size**4
    number_patches = sum(patch_load.values())
    assert number_patches == richness
    assert (
        number_patches
        <= Fraction(energy - size**2, richness * (richness - 1))
    )

    side_length = (size - 1) ** 2 + 1
    record_scale = size**3 + side_length**2
    corrected_target = Fraction(record_scale**2, size**3)
    raw_target = richness**2 * corrected_target
    assert actual_weighted_mass <= corrected_target

    # The raw Q_R T target eventually fails polynomially.  Quantitative
    # lower and upper comparisons record the sqrt(k)=root_size loss.
    if root_size >= 16:
        assert raw_endpoint_mass > raw_target
        failure_ratio = Fraction(raw_endpoint_mass, raw_target)
        assert failure_ratio >= Fraction(root_size, 100)
        assert failure_ratio <= 10 * root_size
    else:
        failure_ratio = Fraction(raw_endpoint_mass, raw_target)

    assert actual_weighted_mass >= size**4 // 100
    assert actual_weighted_mass <= size**4
    assert corrected_target >= size**5 // 10
    return (
        size,
        richness,
        side_length,
        raw_endpoint_mass,
        int(raw_target),
        int(failure_ratio * 10**9),
        actual_weighted_mass,
        int(corrected_target),
    )


def main() -> None:
    profiles = [
        profile(root_size, check_distances=root_size <= 16)
        for root_size in (4, 8, 16, 32, 64)
    ]
    print("PASS", {"profiles": profiles})


if __name__ == "__main__":
    main()
