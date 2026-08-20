#!/usr/bin/env python3
"""Verify cocycle packing for partial parabolic derivative lines."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


MATCHING_F = [
    7432,
    17624,
    170957,
    101948,
    127007,
    102246,
    73129,
    165089,
    1007435,
    1017664,
    1171034,
    1102062,
    1127158,
    1102434,
    1073354,
    1165351,
]

SAME_SLOPE_F = [
    866653, 4112438, 4252663, 745977, 837720, 3486030, 2587304,
    2691354, 10866672, 14112494, 14252756, 10746107, 10837887,
    13486234, 4549837, 4011900, 162028, 4863074, 3578285, 2360524,
    816545, 24550388, 24012488, 20162653, 24863736, 23578984,
    22361260, 1757405,
]

SAME_SHIFT_F = [
    475689, 1127978, 6524683, 8128487, 6543756, 4680281,
    18428729, 19081055, 24477797, 46094012, 44509318, 42645880,
]


def distance_sidon(f: list[int]) -> bool:
    distances: dict[int, tuple[int, int]] = {}
    for first, second in combinations(range(len(f)), 2):
        value = (second - first) ** 2 + (f[second] - f[first]) ** 2
        if value in distances:
            return False
        distances[value] = (first, second)
    return True


def derivatives(f: list[int]) -> dict[int, dict[int, int]]:
    n = len(f)
    return {
        shift: {
            tail: f[tail + shift] - f[tail]
            for tail in range(n - shift)
        }
        for shift in range(1, n)
    }


def rich_lines(
    derivative: dict[int, int], minimum: int = 3
) -> dict[tuple[Fraction, Fraction], frozenset[int]]:
    points = list(derivative.items())
    keys: set[tuple[Fraction, Fraction]] = set()
    for (first_x, first_y), (second_x, second_y) in combinations(points, 2):
        slope = Fraction(second_y - first_y, second_x - first_x)
        if slope == 0:
            continue
        intercept = Fraction(first_y) - slope * first_x
        keys.add((slope, intercept))

    output: dict[tuple[Fraction, Fraction], frozenset[int]] = {}
    for slope, intercept in keys:
        tails = frozenset(
            tail
            for tail, value in points
            if Fraction(value) == intercept + slope * tail
        )
        if len(tails) >= minimum:
            output[(slope, intercept)] = tails
    return output


def verify_cocycle(f: list[int]) -> None:
    data = derivatives(f)
    n = len(f)
    for first_shift in range(1, n):
        for second_shift in range(1, n - first_shift):
            for tail in range(n - first_shift - second_shift):
                assert data[first_shift + second_shift][tail] == (
                    data[first_shift][tail]
                    + data[second_shift][tail + first_shift]
                )


def verify_patch_propagation(f: list[int]) -> tuple[int, ...]:
    assert distance_sidon(f)
    data = derivatives(f)
    lines = {
        shift: rich_lines(derivative)
        for shift, derivative in data.items()
    }
    line_count = sum(len(block) for block in lines.values())
    propagation_checks = 0
    equal_slope_checks = 0
    same_shift_checks = 0
    same_shift_parallel_checks = 0

    patches = [
        (shift, slope, intercept, tails)
        for shift, block in lines.items()
        for (slope, intercept), tails in block.items()
    ]
    for left, right in combinations(patches, 2):
        c, slope_c, intercept_c, tails_c = left
        d, slope_d, intercept_d, tails_d = right
        if c == d:
            # Distinct geometric lines meet in at most one graph point;
            # distinct parallel lines meet in none.
            assert len(tails_c & tails_d) <= 1
            if slope_c == slope_d:
                assert tails_c.isdisjoint(tails_d)
                same_shift_parallel_checks += 1
            same_shift_checks += 1
            continue
        if c < d:
            c, d = d, c
            slope_c, slope_d = slope_d, slope_c
            intercept_c, intercept_d = intercept_d, intercept_c
            tails_c, tails_d = tails_d, tails_c

        overlap = tails_c & tails_d
        if slope_c == slope_d:
            assert len(overlap) <= 1
            equal_slope_checks += 1

        child_slope = slope_c - slope_d
        child_intercept = (
            intercept_c - intercept_d - child_slope * d
        )
        for tail in overlap:
            child_tail = tail + d
            assert data[c - d][child_tail] == (
                child_intercept + child_slope * child_tail
            )
            propagation_checks += 1

    # Verify same-slope packing and the weighted slope-entropy bound for
    # the full rich-line family, including many lines at one shift.
    by_slope: dict[Fraction, list[frozenset[int]]] = defaultdict(list)
    for _, slope, _, tails in patches:
        by_slope[slope].append(tails)

    n = len(f)
    weighted_sum = 0
    for shift, _, _, tails in patches:
        weighted_sum += len(data[shift]) * len(tails) ** 2
    for slope_sets in by_slope.values():
        assert all(
            len(first & second) <= 1
            for first, second in combinations(slope_sets, 2)
        )
        assert sum(comb(len(tails), 2) for tails in slope_sets) <= comb(n, 2)
        assert sum(len(tails) ** 2 for tails in slope_sets) <= 3 * comb(n, 2)
    if by_slope:
        assert 2 * weighted_sum < 3 * len(by_slope) * n**3

    # Whenever the full family has pairwise tail intersections at most
    # two, every tail triple belongs to at most one rich line.  Check both
    # the support packing and the weighted T-rich consequence.
    triple_packable = all(
        len(first[3] & second[3]) <= 2
        for first, second in combinations(patches, 2)
    )
    triple_mass = sum(comb(len(tails), 3) for _, _, _, tails in patches)
    if triple_packable:
        assert triple_mass <= comb(n, 3)
        if patches:
            threshold = min(len(tails) for _, _, _, tails in patches)
            assert threshold >= 3
            if threshold >= 4:
                assert (threshold - 2) * weighted_sum < 2 * n**4

    return (
        line_count,
        propagation_checks,
        equal_slope_checks,
        same_shift_checks,
        same_shift_parallel_checks,
        len(by_slope),
        weighted_sum,
        int(triple_packable),
        triple_mass,
    )


def finite_inequalities() -> None:
    for L in range(3, 401):
        assert L <= comb(L, 2)
        assert L * L <= 3 * comb(L, 2)
    for T in range(4, 201):
        for L in range(T, 401):
            assert (T - 2) * L * L <= 12 * comb(L, 3)
    for k in range(1, 401):
        for L in range(1, k + 1):
            if L * L <= k:
                assert k * k * L * L <= k**3


def matching_profile() -> tuple[int, ...]:
    f = MATCHING_F
    assert len(f) == 16
    assert distance_sidon(f)
    data = derivatives(f)
    shift = 8
    assert data[shift] == {
        tail: 1000003 + 37 * tail for tail in range(8)
    }
    line = (Fraction(37), Fraction(1000003))
    lines = rich_lines(data[shift])
    assert lines[line] == frozenset(range(8))

    # Joining line tails at separation c=8 gives eight singleton
    # components: no two tails differ by the original shift.
    tails = lines[line]
    adjacency = [
        (first, second)
        for first, second in combinations(tails, 2)
        if abs(first - second) == shift
    ]
    assert adjacency == []
    assert len({
        (second - first, f[second] - f[first])
        for first in range(len(f))
        for second in range(len(f))
        if first != second
    }) == len(f) * (len(f) - 1)
    return (
        len(f),
        shift,
        len(tails),
        int(line[0]),
        max(f) + 1,
        comb(len(f), 2),
    )


def same_slope_profile() -> tuple[int, ...]:
    f = SAME_SLOPE_F
    assert len(f) == 28 and distance_sidon(f)
    data = derivatives(f)
    first_tails = frozenset(range(6))
    second_tails = frozenset(range(14, 20))
    assert all(data[8][tail] == 10000019 + 37 * tail for tail in first_tails)
    assert all(data[7][tail] == 20000033 + 37 * tail for tail in second_tails)
    assert first_tails.isdisjoint(second_tails)
    assert rich_lines(data[8])[(Fraction(37), Fraction(10000019))] >= first_tails
    assert rich_lines(data[7])[(Fraction(37), Fraction(20000033))] >= second_tails
    return len(f), len(first_tails), len(second_tails), 37


def same_shift_profile() -> tuple[int, ...]:
    f = SAME_SHIFT_F
    assert len(f) == 12 and distance_sidon(f)
    data = derivatives(f)
    first_tails = frozenset(range(3))
    second_tails = frozenset(range(3, 6))
    first_line = (Fraction(37), Fraction(17953040))
    second_line = (Fraction(37), Fraction(37965414))
    lines = rich_lines(data[6])
    assert lines[first_line] == first_tails
    assert lines[second_line] == second_tails
    assert first_tails.isdisjoint(second_tails)
    return len(f), 6, len(first_tails), len(second_tails), 37


def main() -> None:
    finite_inequalities()
    parabola_f = [value * value for value in range(18)]
    assert distance_sidon(parabola_f)
    verify_cocycle(parabola_f)
    verify_cocycle(MATCHING_F)
    verify_cocycle(SAME_SLOPE_F)
    verify_cocycle(SAME_SHIFT_F)
    parabola_profile = verify_patch_propagation(parabola_f)
    matching_line_profile = verify_patch_propagation(MATCHING_F)
    same_slope_patch_profile = verify_patch_propagation(SAME_SLOPE_F)
    same_shift_patch_profile = verify_patch_propagation(SAME_SHIFT_F)
    assert same_slope_patch_profile[2] > 0
    assert same_shift_patch_profile[3] > 0
    assert same_shift_patch_profile[4] > 0
    pure_matching = matching_profile()
    same_slope = same_slope_profile()
    same_shift = same_shift_profile()
    print(
        "PASS",
        {
            "parabola_patch_profile": parabola_profile,
            "matching_patch_profile": matching_line_profile,
            "same_slope_patch_profile": same_slope_patch_profile,
            "same_shift_patch_profile": same_shift_patch_profile,
            "pure_matching": pure_matching,
            "same_slope": same_slope,
            "same_shift": same_shift,
        },
    )


if __name__ == "__main__":
    main()
