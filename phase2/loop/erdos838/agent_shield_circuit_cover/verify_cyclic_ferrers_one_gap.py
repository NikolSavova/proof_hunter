#!/usr/bin/env python3
"""Exact verifier for CYCLIC_FERRERS_ONE_GAP.md."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def general_position(points):
    return len(set(points)) == len(points) and all(
        cross(a, b, c) != 0 for a, b, c in combinations(points, 3)
    )


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points):
    if len(points) <= 2:
        return len(points) == len(set(points))
    return general_position(points) and len(hull(points)) == len(points)


def ferrers_bad_rectangle(rows, weights, columns, bad):
    """Dyadic rectangle from the proof of weighted Ferrers Lemma 2."""
    rows = tuple(row for row in rows if weights[row] > 0)
    assert rows
    # Every bad column neighborhood must be an initial row segment.
    thresholds = {}
    for col in columns:
        pattern = [bad(row, col) for row in rows]
        seen_good = False
        for value in pattern:
            if not value:
                seen_good = True
            else:
                assert not seen_good, (col, pattern)
        thresholds[col] = sum(pattern)

    prefix_weights = []
    running = 0
    for row in rows:
        running += weights[row]
        prefix_weights.append(running)
    W = running
    total_bad = sum(prefix_weights[thresholds[col] - 1] for col in columns
                    if thresholds[col] > 0)
    levels = W.bit_length()
    candidates = []
    for j in range(levels):
        level = 1 << j
        idx = next(i for i, value in enumerate(prefix_weights) if value >= level)
        chosen_columns = tuple(col for col in columns if thresholds[col] > idx)
        rectangle_weight = prefix_weights[idx] * len(chosen_columns)
        assert all(bad(row, col) for row in rows[: idx + 1] for col in chosen_columns)
        candidates.append((rectangle_weight, idx + 1, chosen_columns))
    best = max(candidates)
    assert total_bad <= levels * best[0]
    return {
        "row_weight_W": W,
        "total_bad_R": total_bad,
        "dyadic_levels": levels,
        "rectangle_weight": best[0],
        "rectangle_rows": best[1],
        "rectangle_columns": len(best[2]),
    }


def cyclic_transfer_audit():
    k = 4
    alphabets = [tuple(range(3, 7)) for _ in range(k)]
    thresholds = (8, 8, 8, 8)

    def compatible(i, left, right):
        return left + right >= thresholds[i]

    selected = tuple(
        word for word in product(*alphabets)
        if all(compatible(i, word[i], word[(i + 1) % k]) for i in range(k))
    )
    M = len(selected)
    assert M == 137
    g = 0
    partials = tuple(sorted(set(word[1:] for word in selected)))
    Qg = len(partials)
    mg = len({word[g] for word in selected})
    assert (Qg, mg) == (45, 4)
    assert M <= mg * Qg

    def gap_counts(reservoir):
        bank = left_bad = right_bad = 0
        for p in partials:
            right_endpoint = p[0]   # cell 1
            left_endpoint = p[-1]   # cell 3
            for face in reservoir:
                left_ok = compatible(3, left_endpoint, face)
                right_ok = compatible(0, face, right_endpoint)
                bank += left_ok and right_ok
                left_bad += not left_ok
                right_bad += not right_ok
        return bank, left_bad, right_bad

    low_reservoir = tuple(range(-5, 7))
    low_bank, low_left_bad, low_right_bad = gap_counts(low_reservoir)
    low_total = len(low_reservoir) * Qg
    assert (low_total, low_bank, low_left_bad, low_right_bad) == (540, 141, 374, 374)
    assert 2 * low_bank < low_total

    # Aggregate contextual path multiplicities by the left endpoint profile.
    weights = Counter(p[-1] for p in partials)
    rows = tuple(sorted(weights))
    bad_rectangle = ferrers_bad_rectangle(
        rows,
        weights,
        low_reservoir,
        lambda row, face: not compatible(3, row, face),
    )
    assert bad_rectangle["total_bad_R"] == low_left_bad
    # The theorem's contextual lower bound, cleared of denominators.
    levels_M = M.bit_length()
    K_num, K_den = len(low_reservoir), mg
    assert 4 * levels_M * bad_rectangle["rectangle_weight"] * K_den >= K_num * M

    high_reservoir = tuple(range(3, 10))
    high_bank, high_left_bad, high_right_bad = gap_counts(high_reservoir)
    high_total = len(high_reservoir) * Qg
    assert (high_total, high_bank, high_left_bad, high_right_bad) == (315, 272, 27, 27)
    assert 2 * high_bank >= high_total
    # Bank lower bound H*M/(2m), again with denominators cleared.
    assert 2 * mg * high_bank >= len(high_reservoir) * M

    return {
        "cells": k,
        "selected_valid_words_M": M,
        "gap_projection_m": mg,
        "partial_words_Q": Qg,
        "circuit_branch": {
            "reservoir_H": len(low_reservoir),
            "formal_substitutions": low_total,
            "compatible_bank": low_bank,
            "left_bad": low_left_bad,
            "right_bad": low_right_bad,
            "ferrers_rectangle": bad_rectangle,
        },
        "bank_branch": {
            "reservoir_H": len(high_reservoir),
            "formal_substitutions": high_total,
            "compatible_bank": high_bank,
            "left_bad": high_left_bad,
            "right_bad": high_right_bad,
        },
    }


def geometric_adjacent_ferrers_audit():
    base = [(-3, 0), (3, 0), (0, 4)]
    shared = (3, 0)
    left = [(-5, -14), (-5, -16), (-10, -17), (-14, -18), (-7, -8), (-7, -6)]
    right = [(8, 7), (9, 13), (11, 5), (7, 2), (9, 7), (12, 14), (10, 4)]
    assert general_position(base + left + right)
    assert all(convex(base + [point]) for point in left + right)

    neighborhoods = []
    good = bad = bad_four_circuits = singleton_guard_releases = 0
    for ell in left:
        neighborhood = set()
        for j, r in enumerate(right):
            turn_good = cross(ell, shared, r) > 0
            actual = convex(base + [ell, r])
            assert actual == turn_good
            if actual:
                good += 1
                neighborhood.add(j)
            else:
                bad += 1
                # Four-locality is checked directly in this five-point union.
                union = base + [ell, r]
                witnesses = [subset for subset in combinations(union, 4)
                             if not convex(list(subset))]
                assert witnesses
                bad_four_circuits += 1
                # Singleton ears always splice after deleting their shared
                # parent vertex.  The separate multi-ear audit below shows
                # why this is not an automatic theorem for arbitrary profiles.
                released = [point for point in base if point != shared] + [ell, r]
                assert convex(released)
                singleton_guard_releases += 1
        neighborhoods.append(frozenset(neighborhood))

    # Ferrers is equivalent to nested row neighborhoods.
    assert all(A <= B or B <= A for A in neighborhoods for B in neighborhoods)
    assert sorted(map(len, neighborhoods)) == [1, 1, 3, 4, 4, 5]
    assert (good, bad, bad_four_circuits, singleton_guard_releases) == (18, 24, 24, 24)
    return {
        "base_rank": len(base),
        "left_profiles": len(left),
        "right_profiles": len(right),
        "good_adjacent_pairs": good,
        "bad_adjacent_pairs": bad,
        "nested_neighborhood_sizes": sorted(map(len, neighborhoods)),
        "bad_pairs_with_four_circuit": bad_four_circuits,
        "bad_singleton_pairs_released_by_deleting_shared_vertex": singleton_guard_releases,
    }


def guard_release_counterexample():
    """A bad adjacent multi-ear pair which stays bad after deleting z."""
    base = [(-3, 0), (3, 0), (0, 4)]
    shared = (3, 0)
    left = [(-10, -16), (-9, -15)]
    right = [(8, 1)]
    all_points = base + left + right
    assert general_position(all_points)
    assert convex(base + left)
    assert convex(base + right)
    assert not convex(all_points)

    released = [point for point in base if point != shared] + left + right
    assert general_position(released)
    assert not convex(released)
    hidden = tuple(point for point in released if point not in hull(released))
    assert hidden == ((-9, -15),)

    # These are exactly the two new turns after z is deleted.  The first is
    # negative, so the released path cannot be convex.
    first_release_turn = cross(left[-2], left[-1], right[0])
    second_release_turn = cross(left[-1], right[0], (0, 4))
    assert first_release_turn == -1
    assert second_release_turn > 0
    return {
        "base": base,
        "shared_vertex_z": shared,
        "left_ear": left,
        "right_ear": right,
        "all_six_points_general_position": True,
        "individual_ears_convex": True,
        "full_union_convex": False,
        "released_union_convex": False,
        "hidden_after_release": hidden,
        "first_release_turn": first_release_turn,
        "second_release_turn": second_release_turn,
    }


def circle(t):
    return ((1 - t * t) / (1 + t * t), 2 * t / (1 + t * t))


def saturation_regression():
    k, s = 4, 3
    points = [circle(Q(i - 8, 3)) for i in range(k * (s + 1))]
    assert general_position(points) and convex(points)
    cyclic = hull(points)
    base = tuple(cyclic[i * (s + 1)] for i in range(k))
    cells = []
    for i in range(k):
        start = i * (s + 1)
        cells.append(tuple(cyclic[(start + j) % len(cyclic)] for j in range(1, s + 1)))
    assert set(base).isdisjoint(set().union(*(set(cell) for cell in cells)))

    alphabets = []
    for cell in cells:
        traces = []
        for mask in range(1, 1 << len(cell)):
            traces.append(tuple(cell[j] for j in range(len(cell)) if (mask >> j) & 1))
        alphabets.append(tuple(traces))
    m = (1 << s) - 1
    assert all(len(alphabet) == m for alphabet in alphabets)

    full_words = 0
    for word in product(*alphabets):
        output = list(base) + [point for trace in word for point in trace]
        assert convex(output)
        full_words += 1
    M = m**k
    assert full_words == M
    # H=m at every gap, so the exact one-gap bank is M and every seam is good.
    gap_banks = tuple(m * M // m for _ in range(k))
    assert gap_banks == (M,) * k
    return {
        "cells": k,
        "points_per_cell": s,
        "local_selected_m": m,
        "local_reservoir_H": m,
        "surplus_K": "1",
        "full_words_M": M,
        "one_gap_banks": gap_banks,
        "bad_seams": 0,
    }


def main():
    certificate = {
        "artifact": "CYCLIC_FERRERS_ONE_GAP",
        "arithmetic": "exact integers and rational coordinates",
        "cyclic_transfer": cyclic_transfer_audit(),
        "geometric_adjacent_ferrers": geometric_adjacent_ferrers_audit(),
        "guard_release_counterexample": guard_release_counterexample(),
        "saturation_regression": saturation_regression(),
        "status": "PASS",
    }
    out = Path(__file__).with_name("cyclic_ferrers_one_gap_certificate.json")
    out.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
