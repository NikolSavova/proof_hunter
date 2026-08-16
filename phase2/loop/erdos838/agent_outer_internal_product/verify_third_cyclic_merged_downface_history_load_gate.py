#!/usr/bin/env python3
"""Exact audit for THIRD_CYCLIC_MERGED_DOWNFACE_HISTORY_LOAD_GATE."""

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
    is_convex,
)
from agent_geometry.audit_geometry import (  # noqa: E402
    cell,
    is_convex as oriented_is_convex,
    orient_table,
)
from agent_outer_internal_product.verify_two_sided_merged_downface_maximum_child_gate import (  # noqa: E402
    role_gadget,
    trie_factor,
)
from lexicographic_blowup import compose_orient  # noqa: E402


def linear_middle_block_audit():
    macro = orient_table(cell(3, 1))
    micro = orient_table(cell(3, 1))
    orient = compose_orient(macro, micro)
    checked = 0
    for mask in range(1 << 9):
        counts = [sum(bool(mask >> (3 * block + j) & 1) for j in range(3))
                  for block in range(3)]
        if min(counts[0], counts[2]) and counts[1] >= 2:
            subset = tuple(i for i in range(9) if mask >> i & 1)
            assert not oriented_is_convex(subset, orient)
            checked += 1
    assert checked == (7 * 4 * 7)
    return checked


def add_common_ear(points, seam, left_marks, right_marks, left_index,
                   right_index, role_count=3, alphabet=2):
    y = left_marks[0]
    z = right_marks[0]
    first = points[left_index[y]]
    second = points[right_index[z]]
    dx = second[0] - first[0]
    dy = second[1] - first[1]
    height = F(1, 100)
    denominator = role_count * (alphabet + 1) + 1
    roles = []
    for role in range(role_count):
        cloud = []
        for label in range(alphabet):
            t = F(1 + role * (alphabet + 1) + label, denominator)
            bump = height * t * (1 - t)
            cloud.append((
                first[0] + t * dx + bump * dy,
                first[1] + t * dy - bump * dx,
            ))
        roles.append(cloud)
    extended = points + [point for role in roles for point in role]
    for i, j, k in itertools.combinations(range(len(extended)), 3):
        assert rt.determinant(extended[i], extended[j], extended[k]) != 0
    indices = {
        point: len(points) + i
        for i, point in enumerate([point for role in roles for point in role])
    }
    return extended, roles, indices


def cyclic_geometry_and_load_audit():
    (points, left_roles, right_roles, left_marks, right_marks,
     left_index, right_index, seam) = role_gadget(3, 2)
    points, third_roles, third_index = add_common_ear(
        points, seam, left_marks, right_marks, left_index, right_index
    )
    y, a, blocker_left = left_marks
    z, b, blocker_right = right_marks
    left_words = tuple(itertools.product(*left_roles))
    right_words = tuple(itertools.product(*right_roles))
    third_words = tuple(itertools.product(*third_roles))

    source_faces = {}
    for left_word in left_words:
        left_source = {
            left_index[a], left_index[blocker_left],
            *(left_index[point] for point in left_word),
        }
        for right_word in right_words:
            right_source = {
                right_index[b], right_index[blocker_right],
                *(right_index[point] for point in right_word),
            }
            for third_word in third_words:
                third_source = {third_index[point] for point in third_word}
                source = frozenset(left_source | right_source | third_source)
                assert is_convex([points[index] for index in source])
                source_faces[left_word, right_word, third_word] = source
    assert len(source_faces) == 8**3 == 512

    # Every subset of all three selected words merges with the common seam.
    left_word = left_words[0]
    right_word = right_words[0]
    third_word = third_words[0]
    all_merged = set()
    for left_mask in range(1 << 3):
        left_subset = {
            left_index[left_word[i]] for i in range(3)
            if left_mask >> i & 1
        }
        for right_mask in range(1 << 3):
            right_subset = {
                right_index[right_word[i]] for i in range(3)
                if right_mask >> i & 1
            }
            for third_mask in range(1 << 3):
                third_subset = {
                    third_index[third_word[i]] for i in range(3)
                    if third_mask >> i & 1
                }
                merged = frozenset(seam | left_subset | right_subset
                                   | third_subset)
                assert is_convex([points[index] for index in merged])
                all_merged.add(merged)
    assert len(all_merged) == 1 << 9

    # History-faithful codimension-three shadow.  Retain each complete
    # selected word except for one role on each side.  The ordinary output
    # retains every variable tail except the three omitted binary labels.
    shadow_loads = Counter()
    shadow_incidences = 0
    for left_word in left_words:
        for right_word in right_words:
            for third_word in third_words:
                for i, j, k in itertools.product(range(3), repeat=3):
                    output = frozenset(
                        seam
                        | {
                            left_index[left_word[r]]
                            for r in range(3) if r != i
                        }
                        | {
                            right_index[right_word[r]]
                            for r in range(3) if r != j
                        }
                        | {
                            third_index[third_word[r]]
                            for r in range(3) if r != k
                        }
                    )
                    assert is_convex([points[index] for index in output])
                    shadow_loads[output] += 1
                    shadow_incidences += 1

    assert shadow_incidences == 512 * 27 == 13_824
    assert len(shadow_loads) == 1_728
    assert set(shadow_loads.values()) == {8}

    # Last-role marked maximum-child expansion. The complete source face X
    # stores the variable tails; the merged face G stores only fixed-prefix
    # subsets and therefore has large one-face load.
    merged_loads = Counter()
    pair_loads = Counter()
    expanded = 0
    q = 3
    for left_depth in range(1, q):
        for left_word in left_words:
            if any(left_word[i] != left_roles[i][0]
                   for i in range(left_depth)):
                continue
            for right_depth in range(1, q):
                for right_word in right_words:
                    if any(right_word[i] != right_roles[i][0]
                           for i in range(right_depth)):
                        continue
                    for third_depth in range(1, q):
                        for third_word in third_words:
                            if any(third_word[i] != third_roles[i][0]
                                   for i in range(third_depth)):
                                continue
                            source = source_faces[
                                left_word, right_word, third_word
                            ]
                            for left_mask in range(1 << (left_depth - 1)):
                                left_subset = {
                                    left_index[left_roles[i][0]]
                                    for i in range(left_depth - 1)
                                    if left_mask >> i & 1
                                }
                                left_subset.add(
                                    left_index[left_roles[left_depth - 1][0]]
                                )
                                for right_mask in range(1 << (right_depth - 1)):
                                    right_subset = {
                                        right_index[right_roles[i][0]]
                                        for i in range(right_depth - 1)
                                        if right_mask >> i & 1
                                    }
                                    right_subset.add(
                                        right_index[right_roles[right_depth - 1][0]]
                                    )
                                    for third_mask in range(1 << (third_depth - 1)):
                                        third_subset = {
                                            third_index[third_roles[i][0]]
                                            for i in range(third_depth - 1)
                                            if third_mask >> i & 1
                                        }
                                        third_subset.add(
                                            third_index[
                                                third_roles[third_depth - 1][0]
                                            ]
                                        )
                                        merged = frozenset(
                                            seam | left_subset | right_subset
                                            | third_subset
                                        )
                                        assert is_convex(
                                            [points[index] for index in merged]
                                        )
                                        merged_loads[merged] += 1
                                        pair_loads[source, merged] += 1
                                        expanded += 1

    assert expanded == 512
    assert len(merged_loads) == 27
    assert max(merged_loads.values()) == 64
    assert max(pair_loads.values()) == 1
    return (
        len(source_faces), len(all_merged), expanded,
        len(merged_loads), max(merged_loads.values()),
        shadow_incidences, len(shadow_loads),
        min(shadow_loads.values()), max(shadow_loads.values()),
    )


def binary_cube_formula_audit():
    rows = []
    for q in range(2, 17):
        records = 1 << (3 * q)
        expanded = (1 << (3 * q - 3)) * (q - 1) ** 3
        outputs = ((1 << (q - 1)) - 1) ** 3
        maximum_load = 1 << (3 * q - 3)
        shadow_incidences = records * q**3
        shadow_outputs = records * q**3 // 8
        average = F(expanded, outputs)
        assert expanded == records * (q - 1) ** 3 // 8
        assert outputs < records // 8
        assert average >= (q - 1) ** 3
        assert maximum_load == records // 8
        assert shadow_incidences == 8 * shadow_outputs
        rows.append((q, records, expanded, outputs, maximum_load, average,
                     shadow_incidences, shadow_outputs))
    return rows


def unequal_alphabet_shadow_formula_audit():
    checked = 0
    for dims1 in ((2, 2), (2, 3, 2), (3, 4)):
        for dims2 in ((2, 2), (3, 2, 2)):
            for dims3 in ((2, 3), (2, 2, 2)):
                mass = math.prod(dims1) * math.prod(dims2) * math.prod(dims3)
                incidences = mass * len(dims1) * len(dims2) * len(dims3)
                outputs = sum(
                    mass // (a * b * c)
                    for a in dims1 for b in dims2 for c in dims3
                )
                formula = (
                    mass
                    * sum(F(1, a) for a in dims1)
                    * sum(F(1, b) for b in dims2)
                    * sum(F(1, c) for c in dims3)
                )
                assert outputs == formula
                assert incidences >= outputs
                checked += 1
    return checked


def fixed_gap_three_role_audit():
    rows = []
    for ell in (32, 40, 48, 64, 80, 96, 128):
        ambient = 1 << ell
        a = ell
        b = ell // 4
        alphabet = ambient // ell**6
        side = (1 << a) * alphabet**b
        # The third physical history word has L binary roles. It changes only
        # the O(L) term, while its maximum-child prefix supplies the third L.
        records = side * side * (1 << ell)
        shadow_bank = records * ell**3 // 8
        log_records = math.log2(records)
        target = .5 * ell * ell - 3 * ell * math.log2(ell) + 3 * ell
        assert abs(log_records - target) < 1
        left_full, left_marked = trie_factor([2] * a + [alphabet] * b)
        third_full, third_marked = trie_factor([2] * ell)
        assert left_full * left_full * third_full <= (ell + 2) ** 3
        assert left_marked * left_marked * third_marked > (ell - 2) ** 3 / 8
        support = 2 * (2 * a + b * alphabet + 3) + 2 * ell
        assert support * ell**4 < ambient
        assert shadow_bank * 8 == records * ell**3
        assert abs(math.log2(shadow_bank / records)
                   - (3 * math.log2(ell) - 3)) < 1e-12
        rows.append((ell, alphabet, support, left_full, third_full,
                     shadow_bank.bit_length()))
    return rows


def main():
    linear = linear_middle_block_audit()
    cyclic = cyclic_geometry_and_load_audit()
    formulas = binary_cube_formula_audit()
    unequal = unequal_alphabet_shadow_formula_audit()
    fixed_gap = fixed_gap_three_role_audit()
    print(
        "PASS: third cyclic merged-downface gate; linear=%d; cyclic=%s; "
        "binary q=%d..%d; unequal=%d; fixed-gap L=%d..%d"
        % (linear, cyclic, formulas[0][0], formulas[-1][0],
           unequal, fixed_gap[0][0], fixed_gap[-1][0])
    )


if __name__ == "__main__":
    main()
