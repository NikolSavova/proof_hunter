#!/usr/bin/env python3
"""Exact verifier for the decorated two-mark inversion dichotomy."""

from __future__ import annotations

import importlib.util
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "menu", HERE / "verify_two_direction_four_point_wrapper.py")
assert SPEC and SPEC.loader
menu = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(menu)


def chamber_records(word):
    points, _ = menu.configuration(word)
    signs = menu.all_signs(points)
    points = menu.generic_perturb(points, signs)
    critical = sorted({-(points[j][0] - points[i][0])
                       / (points[j][1] - points[i][1])
                       for i, j in combinations(range(14), 2)
                       if points[j][1] != points[i][1]})
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)
    records = []
    seen = set()
    for slope in probes:
        order = tuple(sorted(range(14),
                             key=lambda i: points[i][0] + slope * points[i][1]))
        for sign, candidate in ((1, order), (-1, order[::-1])):
            if candidate in seen:
                continue
            seen.add(candidate)
            functional = (Q(sign), Q(sign) * slope)
            records.append((functional,
                            menu.chain_counts(signs, candidate), candidate))
    assert len(records) == 182
    return points, records


def normalized_values(points, functional):
    values = [functional[0] * x + functional[1] * y for x, y in points]
    lo, hi = min(values), max(values)
    return [(value - lo) / (hi - lo) for value in values]


def inversions(first_order, second_order):
    position = {point: i for i, point in enumerate(first_order)}
    word = [position[point] for point in second_order]
    return sum(word[i] > word[j]
               for i, j in combinations(range(len(word)), 2))


def cover_to_monotone(first_order, second_order):
    """At most min(I,N) deletions leave increasing or decreasing order."""
    position = {point: i for i, point in enumerate(first_order)}
    word = [position[point] for point in second_order]
    pairs = list(combinations(range(len(word)), 2))
    inversion_edges = [(i, j) for i, j in pairs if word[i] > word[j]]
    noninversion_edges = [(i, j) for i, j in pairs if word[i] < word[j]]
    increasing = len(inversion_edges) <= len(noninversion_edges)
    edges = inversion_edges if increasing else noninversion_edges
    # Selecting the first endpoint of every offending edge is a vertex cover
    # of size at most the number of edges.
    deleted = {i for i, _ in edges}
    remaining = [word[i] for i in range(len(word)) if i not in deleted]
    if increasing:
        assert all(a < b for a, b in zip(remaining, remaining[1:]))
    else:
        assert all(a > b for a, b in zip(remaining, remaining[1:]))
    return deleted


def build_bichart_parent():
    """Realize three positive-handed assembly/reset pairs simultaneously."""
    # Assembly rows are the unique W2-minimizing states.  The reset rows are
    # the exact positive-handed choice minimizing the formal reverse/opposite
    # comb profile.  The point of the test is that this formal profile is not
    # the actual parent profile once internal inversions are retained.
    specs = (
        ((7, 0, 0), 43, 45, (183, 1975), (193, 1826)),
        ((0, 1, 7), 11, 29, (342, 414), (251, 539)),
        ((7, 0, 0), 42, 44, (1975, 183), (1826, 193)),
    )
    macro_slope = Q(20)
    delta = Q(1, 10**6)
    blocks = [[(Q(0), Q(0), None)]]
    order_pairs = []

    for role, (word, assembly_index, reset_index,
               assembly_profile, reset_profile) in enumerate(specs, 1):
        points, records = chamber_records(word)
        f, got_assembly, f_order = records[assembly_index]
        h, got_reset, h_order = records[reset_index]
        assert got_assembly == assembly_profile
        assert got_reset == reset_profile
        assert f[0] * h[1] - f[1] * h[0] > 0

        f_values = normalized_values(points, f)
        h_values = normalized_values(points, h)
        ratios = [abs((h_values[j] - h_values[i])
                      / (f_values[j] - f_values[i]))
                  for i, j in combinations(range(14), 2)]
        kappa = Q(1, 10 * (1 + max(ratios)))
        epsilon = delta * kappa
        block = []
        for point in range(14):
            x = Q(role) + delta * f_values[point]
            y = (macro_slope * x - Q(role * role)
                 + epsilon * h_values[point])
            block.append((x, y, point))
        block.sort()  # f-order, hence assembly order
        blocks.append(block)
        order_pairs.append((f_order, h_order))

    blocks.append([(Q(4), macro_slope * 4 - 16, None)])
    points = [(x, y) for block in blocks for x, y, _ in block]
    block_labels = [i for i, block in enumerate(blocks) for _ in block]
    signs = menu.all_signs(points)

    # The assembly order is the displayed concatenation and has the exact
    # strong-comb cross signs.
    assembly = tuple(range(44))
    assert menu.chain_counts(signs, assembly) == (103311, 16109)
    for triple, value in signs.items():
        pattern = tuple(block_labels[i] for i in triple)
        if len(set(pattern)) == 1:
            continue
        if pattern[0] == pattern[1]:
            assert value < 0
        if pattern[1] == pattern[2]:
            assert value > 0

    # H=Y-SX gives every selected h-order internally and reverses the five
    # macro blocks.
    reset_value = lambda point: point[1] - macro_slope * point[0]
    reset = tuple(sorted(range(44), key=lambda i: reset_value(points[i])))
    reset_labels = [block_labels[i] for i in reset]
    assert reset_labels == ([4] + [3] * 14 + [2] * 14 + [1] * 14 + [0])
    assert menu.chain_counts(signs, reset) == (14537, 106989)

    inversion_counts = [inversions(first, second)
                        for first, second in order_pairs]
    assert inversion_counts == [1, 9, 1]

    # For every external point, the two possible cross signs occur exactly
    # I and C(14,2)-I times.  This is the geometric inversion identity.
    reset_position = {point: i for i, point in enumerate(reset)}
    mixed = 0
    starts = (1, 15, 29)
    for start, inversion_count in zip(starts, inversion_counts):
        child = list(range(start, start + 14))
        external = [i for i in range(44) if i not in child]
        for outside in external:
            counts = {-1: 0, 1: 0}
            for first, second in combinations(child, 2):
                ordered = sorted((first, second, outside),
                                 key=reset_position.__getitem__)
                value = menu.ordered_sign(signs, *ordered)
                counts[value] += 1
            assert sorted(counts.values()) == [inversion_count,
                                                91 - inversion_count]
            mixed += min(counts.values())
    assert mixed == 330
    return order_pairs


def main():
    # Exhaustively verify the deletion statement for every permutation up to
    # seven labels; the proof in the report works for arbitrary size.
    for size in range(2, 8):
        identity = tuple(range(size))
        for permutation in permutations(identity):
            deleted = cover_to_monotone(identity, permutation)
            count = inversions(identity, permutation)
            assert len(deleted) <= min(count, size * (size - 1) // 2 - count)

    order_pairs = build_bichart_parent()
    assert [len(cover_to_monotone(first, second))
            for first, second in order_pairs] == [1, 4, 1]
    print("PASS: permutation deletion exhaustive through n=7; "
          "exact 44-point bi-chart parent assembly=(103311,16109), "
          "reset=(14537,106989), inversion counts=(1,9,1), "
          "mixed cross triples=330")


if __name__ == "__main__":
    main()
