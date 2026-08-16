#!/usr/bin/env python3
"""Exact verifier for ALTERNATING_FERRERS_PLANAR_WRAPPER.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower, upper = [], []
    for point in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    for point in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def general_position(points):
    return len(set(points)) == len(points) and all(
        cross(a, b, c) != 0 for a, b, c in combinations(points, 3)
    )


def convex(points):
    if len(points) <= 2:
        return len(points) == len(set(points))
    return general_position(points) and len(hull(points)) == len(points)


def edge_point(u, v, left, right):
    """Affine image of ((L-R)/(L+R), -2/(L+R)) in edge uv's pocket."""
    tangent_coordinate = (left - right) / (left + right)
    depth_coordinate = Q(-2) / (left + right)
    midpoint = ((u[0] + v[0]) / 2, (u[1] + v[1]) / 2)
    tangent = ((v[0] - u[0]) / 2, (v[1] - u[1]) / 2)
    inward = (-(v[1] - u[1]) / 2, (v[0] - u[0]) / 2)
    return (
        midpoint[0] + tangent_coordinate * tangent[0] + depth_coordinate * inward[0],
        midpoint[1] + tangent_coordinate * tangent[1] + depth_coordinate * inward[1],
    )


def rational_instance():
    base = [(Q(-1), Q(-1)), (Q(1), Q(-1)), (Q(1), Q(1)), (Q(-1), Q(1))]
    child = ((1, 0), (2, 4), (3, 1), (4, 0))
    epsilon = Q(1, 100)
    coefficients = ((8, 2), (1, -7), (8, 6), (4, -1))
    cells = []
    for cell in range(4):
        points = []
        a, b = coefficients[cell]
        for f, g in child:
            if cell % 2 == 0:
                left = 1 - epsilon * (f - Q(1, 2)) + a * epsilon * epsilon * g
                right = 1 - epsilon * f + b * epsilon * epsilon * g
            else:
                left = 1 + epsilon * (f + Q(1, 2)) + a * epsilon * epsilon * g
                right = 1 + epsilon * f + b * epsilon * epsilon * g
            assert left > 0 and right > 0
            points.append(edge_point(base[cell], base[(cell + 1) % 4], left, right))
        cells.append(tuple(points))
    return tuple(base), tuple(cells)


def compatible(seam, left_label, right_label):
    return left_label <= right_label if seam % 2 == 0 else left_label >= right_label


def face_zeta(points):
    """All convex masks: upward closure of exact bad four-circuits."""
    n = len(points)
    bad = bytearray(1 << n)
    circuits = []
    for indices in combinations(range(n), 4):
        subset = [points[index] for index in indices]
        if not convex(subset):
            mask = sum(1 << index for index in indices)
            circuits.append(mask)
            bad[mask] = 1
    for bit_index in range(n):
        bit = 1 << bit_index
        block = bit << 1
        for start in range(0, 1 << n, block):
            for offset in range(bit):
                if bad[start + offset]:
                    bad[start + bit + offset] = 1
    faces = tuple(mask for mask, value in enumerate(bad) if not value)
    return circuits, faces


def geometry_audit():
    base, cells = rational_instance()
    points = base + sum(cells, ())
    assert len(points) == 20 and general_position(points)
    assert all(not convex(cell) and len(hull(cell)) == 3 for cell in cells)
    assert all(convex(list(base) + [point]) for point in sum(cells, ()))

    good_entries = bad_entries = 0
    for seam in range(4):
        for left_label, right_label in product(range(1, 5), repeat=2):
            actual = convex(
                list(base)
                + [cells[seam][left_label - 1], cells[(seam + 1) % 4][right_label - 1]]
            )
            expected = compatible(seam, left_label, right_label)
            assert actual == expected
            good_entries += actual
            bad_entries += not actual
    assert (good_entries, bad_entries) == (40, 24)

    words = tuple(
        word
        for word in product(range(1, 5), repeat=4)
        if all(compatible(i, word[i], word[(i + 1) % 4]) for i in range(4))
    )
    assert len(words) == 70
    assert all(
        convex(list(base) + [cells[i][word[i] - 1] for i in range(4)]) for word in words
    )

    def rich(cell, label):
        return label > 2 if cell % 2 == 0 else label <= 2

    rich_compatible_pairs = 0
    for seam in range(4):
        for left_label, right_label in product(range(1, 5), repeat=2):
            if compatible(seam, left_label, right_label):
                rich_compatible_pairs += rich(seam, left_label) and rich(
                    (seam + 1) % 4, right_label
                )
    assert rich_compatible_pairs == 0

    circuits, faces = face_zeta(points)
    assert len(circuits) == 1900
    assert len(faces) == 9722
    ranks = [0] * 21
    base_masks = [0] * 16
    detached_active = [0] * 16
    for mask in faces:
        ranks[mask.bit_count()] += 1
        base_masks[mask & 15] += 1
        if mask & 15 == 0:
            active = 0
            for cell in range(4):
                if mask & (15 << (4 + 4 * cell)):
                    active |= 1 << cell
            detached_active[active] += 1
    while ranks and ranks[-1] == 0:
        ranks.pop()
    assert ranks == [1, 20, 190, 1140, 2945, 3108, 1716, 528, 74]
    assert base_masks == [2047, 828, 828, 526, 828, 361, 515, 320,
                          828, 515, 361, 320, 526, 320, 320, 279]
    assert detached_active == [1, 14, 14, 143, 14, 169, 143, 196,
                               14, 143, 169, 216, 143, 196, 216, 256]

    # In each opposite pair, exactly 13 local traces on either side form a
    # complete Cartesian product.  This is the smallest visible forced bank.
    opposite_rectangles = []
    for first, second in ((0, 2), (1, 3)):
        matrix = []
        for left_mask in range(1, 16):
            row = []
            for right_mask in range(1, 16):
                subset = [cells[first][j] for j in range(4) if left_mask & (1 << j)]
                subset += [cells[second][j] for j in range(4) if right_mask & (1 << j)]
                row.append(convex(subset))
            matrix.append(row)
        row_degrees = [sum(row) for row in matrix]
        column_degrees = [sum(matrix[i][j] for i in range(15)) for j in range(15)]
        assert sorted(row_degrees) == [0, 0] + [13] * 13
        assert sorted(column_degrees) == [0, 0] + [13] * 13
        good_rows = [i for i, degree in enumerate(row_degrees) if degree]
        good_columns = [j for j, degree in enumerate(column_degrees) if degree]
        assert all(matrix[i][j] for i in good_rows for j in good_columns)
        opposite_rectangles.append({"cells": [first, second], "rows": 13, "columns": 13})

    one_gap = [detached_active[15 ^ (1 << gap)] for gap in range(4)]
    assert one_gap == [216, 196, 216, 196]
    return {
        "points": len(points),
        "general_position": True,
        "nonconvex_child_order_types": 4,
        "adjacent_matrix": {"good": good_entries, "bad": bad_entries},
        "valid_singleton_words": len(words),
        "compatible_rich_adjacent_pairs": rich_compatible_pairs,
        "bad_four_circuits": len(circuits),
        "total_faces": len(faces),
        "rank_vector": ranks,
        "faces_by_base_mask": base_masks,
        "detached_faces": base_masks[0],
        "detached_faces_by_active_cell_mask": detached_active,
        "one_gap_layers": one_gap,
        "opposite_complete_rectangles": opposite_rectangles,
    }


def aligned_partial_rectangle(alphabet, cycle, gap):
    assert alphabet % 4 == 0 and cycle % 2 == 0
    bottom = tuple(range(1, alphabet // 4 + 1))
    second = tuple(range(alphabet // 4 + 1, alphabet // 2 + 1))
    third = tuple(range(alphabet // 2 + 1, 3 * alphabet // 4 + 1))
    top = tuple(range(3 * alphabet // 4 + 1, alphabet + 1))
    choices = []
    for cell in range(cycle):
        if cell == gap:
            choices.append((None,))
        elif gap % 2 == 1:
            choices.append(third if cell % 2 == 0 else top)
        else:
            choices.append(bottom if cell % 2 == 0 else second)
    words = tuple(product(*choices))
    for word in words:
        for seam in range(cycle):
            if word[seam] is None or word[(seam + 1) % cycle] is None:
                continue
            assert compatible(seam, word[seam], word[(seam + 1) % cycle])
        assert word[(gap - 1) % cycle] is not None
        assert word[(gap + 1) % cycle] is not None
        left_rich = word[(gap - 1) % cycle] > alphabet // 2 if (gap - 1) % 2 == 0 else word[(gap - 1) % cycle] <= alphabet // 2
        right_rich = word[(gap + 1) % cycle] > alphabet // 2 if (gap + 1) % 2 == 0 else word[(gap + 1) % cycle] <= alphabet // 2
        assert left_rich and right_rich
    assert len(words) == (alphabet // 4) ** (cycle - 1)
    return len(words)


def coefficient_audit():
    rectangles = []
    for alphabet, cycle in ((8, 4), (8, 6), (12, 4)):
        sizes = [aligned_partial_rectangle(alphabet, cycle, gap) for gap in range(cycle)]
        rectangles.append({"alphabet": alphabet, "cycle": cycle, "gap_rectangles": sizes})

    thresholds = []
    for beta in (Q(1), Q(2), Q(4), Q(8)):
        threshold = (1 + beta) / (1 + 2 * beta)
        half_reset = (1 + beta + Q(1, 2) * beta * beta) / (1 + beta) ** 2
        assert threshold > Q(1, 2)
        assert half_reset > Q(1, 2)
        assert half_reset - Q(1, 2) == Q(1, 2) / (1 + beta) ** 2
        thresholds.append({
            "beta": str(beta),
            "fixed_point_threshold": str(threshold),
            "one_half_maps_to": str(half_reset),
        })

    # Exact cyclic cancellation behind max_g R_(g-1) A_(g+1) >= GM(H_i).
    left = (2, 3, 5, 7, 11, 13)
    right = (17, 19, 23, 29, 31, 37)
    gap_factors = [right[(gap - 1) % 6] * left[(gap + 1) % 6] for gap in range(6)]
    product_gaps = 1
    product_local = 1
    for value in gap_factors:
        product_gaps *= value
    for a, r in zip(left, right):
        product_local *= a * r
    assert product_gaps == product_local
    return {
        "aligned_partial_rectangles": rectangles,
        "fixed_point_thresholds": thresholds,
        "cyclic_profile_product_identity": True,
    }


def main():
    certificate = {
        "artifact": "ALTERNATING_FERRERS_PLANAR_WRAPPER",
        "arithmetic": "exact integers and rational coordinates",
        "geometry": geometry_audit(),
        "scalable_algebra": coefficient_audit(),
        "status": "PASS",
    }
    output = Path(__file__).with_name("alternating_ferrers_planar_wrapper_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
