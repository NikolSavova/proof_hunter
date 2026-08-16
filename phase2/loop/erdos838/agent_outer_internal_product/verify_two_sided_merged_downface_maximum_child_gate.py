#!/usr/bin/env python3
"""Exact audit for TWO_SIDED_MERGED_DOWNFACE_MAXIMUM_CHILD_GATE."""

from __future__ import annotations

import itertools
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402
from agent_common_shield_mixing.verify_two_anchor_double_circuit_elimination_gate import (  # noqa: E402
    is_chain,
    is_convex,
)


Point = tuple[F, F]


def role_gadget(role_count: int = 3, alphabet: int = 2):
    """A rational full-prefix-compatible double-bad strong-glue gadget."""
    height = F(2)
    y, a, blocker_left = (F(-1), height), (F(0), F(0)), (F(1), F(-1))
    z, b, blocker_right = (F(-1), -height), (F(0), F(0)), (F(1), F(1))

    left_roles: list[list[Point]] = []
    right_roles: list[list[Point]] = []
    for role in range(role_count):
        left_role = []
        right_role = []
        for label in range(alphabet):
            x = F(4 + 3 * role) + F(label, alphabet + 1)
            left_role.append((x, -x * x))
            right_role.append((x, x * x))
        left_roles.append(left_role)
        right_roles.append(right_role)

    # A positive shear makes both child coordinate lists increasing in x and
    # y, as required by the explicit rational strong-glue realization. It
    # preserves every determinant.
    def shear(point: Point) -> Point:
        return point[0], point[1] + 30 * point[0]

    left_original = sorted([y, a, blocker_left]
                           + [p for role in left_roles for p in role])
    right_original = sorted([z, b, blocker_right]
                            + [p for role in right_roles for p in role])
    left = [shear(point) for point in left_original]
    right = [shear(point) for point in right_original]
    assert all(left[i][1] < left[i + 1][1]
               for i in range(len(left) - 1))
    assert all(right[i][1] < right[i + 1][1]
               for i in range(len(right) - 1))
    points = rt.strong_glue(left, right, F(1, 10**6))

    left_index = {point: i for i, point in enumerate(left_original)}
    right_index = {
        point: len(left) + i for i, point in enumerate(right_original)
    }
    seam = frozenset((left_index[y], left_index[a],
                      right_index[z], right_index[b]))
    assert is_convex([points[index] for index in seam])
    return (
        points, left_roles, right_roles,
        (y, a, blocker_left), (z, b, blocker_right),
        left_index, right_index, seam,
    )


def geometric_factorization_audit():
    (points, left_roles, right_roles, left_marks, right_marks,
     left_index, right_index, seam) = role_gadget()
    y, a, blocker_left = left_marks
    z, b, blocker_right = right_marks

    left_words = tuple(itertools.product(*left_roles))
    right_words = tuple(itertools.product(*right_roles))
    checked = 0
    rank_counts = Counter()
    predicted_rank_counts = Counter()
    for left_word in left_words:
        left_source = frozenset(
            (left_index[a], left_index[blocker_left],
             *(left_index[point] for point in left_word))
        )
        assert is_chain([a, blocker_left, *left_word], -1)
        assert not is_chain([y, a, blocker_left, *left_word], -1)
        for right_word in right_words:
            right_source = frozenset(
                (right_index[b], right_index[blocker_right],
                 *(right_index[point] for point in right_word))
            )
            assert is_chain([b, blocker_right, *right_word], +1)
            assert not is_chain([z, b, blocker_right, *right_word], +1)
            assert is_convex(
                [points[index] for index in left_source | right_source]
            )

            # Exhaust every pair of downfaces of the complete selected word.
            left_profile = Counter()
            right_profile = Counter()
            for left_mask in range(1 << len(left_word)):
                left_subset_points = [
                    left_word[i] for i in range(len(left_word))
                    if left_mask >> i & 1
                ]
                left_good = is_chain([y, a, *left_subset_points], -1)
                assert left_good  # the rooted left downset is a full cube
                left_profile[len(left_subset_points)] += 1
                left_subset = frozenset(left_index[p]
                                        for p in left_subset_points)
                for right_mask in range(1 << len(right_word)):
                    right_subset_points = [
                        right_word[i] for i in range(len(right_word))
                        if right_mask >> i & 1
                    ]
                    right_good = is_chain([z, b, *right_subset_points], +1)
                    assert right_good
                    right_subset = frozenset(right_index[p]
                                             for p in right_subset_points)
                    actual = is_convex(
                        [points[index]
                         for index in seam | left_subset | right_subset]
                    )
                    assert actual == (left_good and right_good)
                    rank_counts[4 + len(left_subset) + len(right_subset)] += 1
                    checked += 1
            for right_mask in range(1 << len(right_word)):
                right_rank = right_mask.bit_count()
                right_profile[right_rank] += 1
            for left_rank, left_count in left_profile.items():
                for right_rank, right_count in right_profile.items():
                    predicted_rank_counts[4 + left_rank + right_rank] += (
                        left_count * right_count
                    )

    # There are 64 source rectangles, each contributing 4^3 merged faces.
    assert checked == 64 * 64
    assert rank_counts == predicted_rank_counts
    return len(left_words), len(right_words), checked, tuple(sorted(rank_counts.items()))


def trie_factor(sizes):
    prefix_product = 1
    full = F(0)
    marked = F(0)
    for depth, size in enumerate(sizes):
        alpha = F(1, prefix_product)
        full += (1 << depth) * alpha
        if depth:
            # Require the last prefix role to occur. The output then recovers
            # the depth and keeps exactly half of the prefix cube.
            marked += (1 << (depth - 1)) * alpha
        prefix_product *= size
    return full, marked


def abstract_maximum_child_audit():
    sizes = [2] * 6 + [16] * 3
    full, marked = trie_factor(sizes)
    assert full == F(457, 64)
    assert marked == F(393, 128) == (full - 1) / 2
    assert full * full == F(208849, 4096)
    assert marked * marked == F(154449, 16384)

    # Exact maximum-child expansion for three binary roles on each side.
    q = 3
    merged_loads = Counter()
    pair_loads = Counter()
    expanded = 0
    marked_expanded = 0
    marked_pair_loads = Counter()
    for left_depth in range(q):
        for left_word in itertools.product(range(2), repeat=q):
            if any(left_word[i] for i in range(left_depth)):
                continue
            for right_depth in range(q):
                for right_word in itertools.product(range(2), repeat=q):
                    if any(right_word[i] for i in range(right_depth)):
                        continue
                    source = left_word, right_word
                    for left_mask in range(1 << left_depth):
                        left_subset = tuple(
                            i for i in range(left_depth)
                            if left_mask >> i & 1
                        )
                        for right_mask in range(1 << right_depth):
                            right_subset = tuple(
                                i for i in range(right_depth)
                                if right_mask >> i & 1
                            )
                            merged = left_subset, right_subset
                            merged_loads[merged] += 1
                            pair_loads[source, merged] += 1
                            expanded += 1
                            if (left_depth and right_depth
                                    and left_mask >> (left_depth - 1) & 1
                                    and right_mask >> (right_depth - 1) & 1):
                                marked_expanded += 1
                                marked_pair_loads[source, merged] += 1

    assert expanded == 64 * q * q == 576
    assert max(merged_loads.values()) == 196
    assert max(pair_loads.values()) == q * q == 9
    # Last-role marking recovers both depths, hence the pair load is one.
    assert marked_expanded == 64
    assert max(marked_pair_loads.values()) == 1
    return full, marked, expanded, max(merged_loads.values()), max(pair_loads.values()), marked_expanded


def fixed_gap_entropy_audit():
    rows = []
    for ell in (32, 40, 48, 64, 80, 96, 128):
        ambient = 1 << ell
        binary_roles = ell
        large_roles = ell // 4
        alphabet = ambient // ell**6
        assert alphabet >= 4
        side_sources = (1 << binary_roles) * alphabet**large_roles
        record_mass = side_sources * side_sources
        log_mass = math.log2(record_mass)
        target = F(1, 2) * ell * ell - 3 * ell * math.log2(ell)
        # The binary roles contribute the displayed +2L lower-order term;
        # flooring D changes this by less than one bit in the tested range.
        assert abs(log_mass - float(target) - 2 * ell) < 1
        support = 2 * (2 * binary_roles + large_roles * alphabet + 3)
        assert support * ell**4 < ambient
        rank = binary_roles + large_roles + 2
        assert rank <= 2 * ell
        full, marked = trie_factor(
            [2] * binary_roles + [alphabet] * large_roles
        )
        assert ell <= full <= ell + 2
        assert marked == (full - 1) / 2
        assert full * full <= (ell + 2) ** 2
        rows.append((ell, alphabet, support, rank, full, marked))
    return rows


def main():
    geometry = geometric_factorization_audit()
    trie = abstract_maximum_child_audit()
    fixed_gap = fixed_gap_entropy_audit()
    print(
        "PASS: two-sided merged downfaces; geometry=%s; "
        "trie=(%s/%s,%s/%s,%s,%s,%s,%s); fixed-gap L=%s..%s"
        % (
            geometry,
            trie[0].numerator, trie[0].denominator,
            trie[1].numerator, trie[1].denominator,
            trie[2], trie[3], trie[4], trie[5],
            fixed_gap[0][0], fixed_gap[-1][0],
        )
    )


if __name__ == "__main__":
    main()
