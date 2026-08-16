#!/usr/bin/env python3
"""Exact verifier for MINIMIZER_TWO_POINT_EXTENSION_INTERACTION_GATE."""

from __future__ import annotations

import json
import random
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402
from agent_outer_internal_product.verify_fixed_anchor_relocation_cancellation_gate import (  # noqa: E402
    convex,
    families,
)


Point = tuple[Fraction, Fraction]


def face_count(points: list[Point]) -> int:
    return len(families(points)[0])


def extension(base: list[Point], *anchors: Point) -> int:
    count = 0
    for mask in range(1 << len(base)):
        subset = [base[i] for i in range(len(base)) if mask >> i & 1]
        count += int(convex(subset + list(anchors)))
    return count


def extension_profile(base: list[Point], *anchors: Point):
    profile = {}
    for mask in range(1 << len(base)):
        subset = [base[i] for i in range(len(base)) if mask >> i & 1]
        if convex(subset + list(anchors)):
            profile[mask.bit_count()] = profile.get(mask.bit_count(), 0) + 1
    return profile


def general_position(points: list[Point]) -> bool:
    return all(rt.determinant(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def candidate_points(base: list[Point], seed: int, number: int = 4):
    random.seed(seed)
    maximum_x = max(int(point[0]) for point in base)
    maximum_y = max(int(point[1]) for point in base)
    scale = 100000
    result = []
    while len(result) < number:
        point = (
            Fraction(maximum_x + random.randint(-9, 9) * scale
                     + random.randint(1, 999), 97),
            Fraction(maximum_y + random.randint(-9, 9) * scale
                     + random.randint(1, 999), 89),
        )
        if general_position(base + [point]):
            result.append(point)
    return result


def rank_profile(points: list[Point]):
    profile = {}
    for mask in range(1, 1 << len(points)):
        subset = [points[i] for i in range(len(points)) if mask >> i & 1]
        if convex(subset):
            profile[mask.bit_count()] = profile.get(mask.bit_count(), 0) + 1
    return profile


def coefficientwise_check(points: list[Point], x_index: int, y_index: int):
    base = [point for index, point in enumerate(points)
            if index not in (x_index, y_index)]
    x = points[x_index]
    y = points[y_index]
    base_profile = {0: 1, **rank_profile(base)}
    full_profile = {0: 1, **rank_profile(base + [x, y])}
    left_profile = extension_profile(base, x)
    right_profile = extension_profile(base, y)
    interaction_profile = extension_profile(base, x, y)
    for rank in range(len(points) + 1):
        expected = (
            base_profile.get(rank, 0)
            + left_profile.get(rank - 1, 0)
            + right_profile.get(rank - 1, 0)
            + interaction_profile.get(rank - 2, 0)
        )
        assert full_profile.get(rank, 0) == expected


def pair_bound_and_moments(points: list[Point], expected_v: int,
                           require_minimal: bool = True):
    n = len(points)
    v = face_count(points)
    assert v == expected_v
    slacks = []
    left_moment = 0
    cap_deleted_sum = 0
    cup_deleted_sum = 0
    for x, y in combinations(range(n), 2):
        base = [point for index, point in enumerate(points)
                if index not in (x, y)]
        faces, caps, cups = families(base)
        deletion_loss = v - len(faces)
        branches = (
            3 + 3 * len(caps),
            3 + 3 * len(cups),
            3 + len(caps) + len(cups) + len(base),
        )
        slacks.append(min(branches) - deletion_loss)
        cap_deleted_sum += len(caps)
        cup_deleted_sum += len(cups)

    profile = rank_profile(points)
    for rank, count in profile.items():
        left_moment += count * (
            n * (n - 1) // 2 - (n - rank) * (n - rank - 1) // 2
        )
    pair_number = n * (n - 1) // 2
    right_sides = (
        3 * pair_number + 3 * cap_deleted_sum,
        3 * pair_number + 3 * cup_deleted_sum,
        (n + 1) * pair_number + cap_deleted_sum + cup_deleted_sum,
    )
    if require_minimal:
        assert all(left_moment <= right for right in right_sides)
    else:
        assert any(left_moment > right for right in right_sides)
    return min(slacks), max(slacks)


def hessian_audit(points: list[Point], pair_indices=None):
    n = len(points)
    v = face_count(points)
    if pair_indices is None:
        pair_indices = list(combinations(range(n), 2))
    hessians = []
    simultaneous = []
    separate = []
    for x_index, y_index in pair_indices:
        base = [point for index, point in enumerate(points)
                if index not in (x_index, y_index)]
        x = points[x_index]
        y = points[y_index]
        a_x = extension(base, x)
        a_y = extension(base, y)
        j_xy = extension(base, x, y)
        assert face_count(base) + a_x + a_y + j_xy == v
        assert j_xy <= face_count(base) + 1

        candidates = candidate_points(base, 100 * x_index + y_index)
        a_values = {point: extension(base, point) for point in candidates}
        j_to_y = {point: extension(base, point, y) for point in candidates}
        j_from_x = {point: extension(base, x, point) for point in candidates}
        j_pairs = {
            (u, w): extension(base, u, w)
            for u, w in combinations(candidates, 2)
        }
        for u, w in combinations(candidates, 2):
            delta_x = a_values[u] - a_x + j_to_y[u] - j_xy
            delta_y = a_values[w] - a_y + j_from_x[w] - j_xy
            delta_pair = (a_values[u] + a_values[w] + j_pairs[(u, w)]
                          - a_x - a_y - j_xy)
            hessian = (j_pairs[(u, w)] - j_to_y[u]
                       - j_from_x[w] + j_xy)
            assert delta_pair == delta_x + delta_y + hessian
            hessians.append(hessian)
            simultaneous.append(delta_pair)
            separate.extend((delta_x, delta_y))
    return (
        min(hessians),
        max(hessians),
        min(simultaneous),
        max(simultaneous),
        min(separate),
        max(separate),
    )


def five_points():
    return [
        (Fraction(6), Fraction(15)),
        (Fraction(18), Fraction(22)),
        (Fraction(13), Fraction(4)),
        (Fraction(12), Fraction(17)),
        (Fraction(20), Fraction(29)),
    ]


def nine_points():
    data = json.loads(
        (ERDOS / "agent_lex_minimizer_search"
         / "exact_realizable_n9.json").read_text()
    )
    return [(Fraction(x), Fraction(y))
            for x, y in data["coordinates_as_stored"]]


def pascal_wrapper():
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    return sorted(rt.strong_glue(q, q, Fraction(1, 16384)))


def main():
    p5 = five_points()
    p9 = nine_points()
    p12 = pascal_wrapper()
    assert general_position(p5)
    assert general_position(p9)
    assert general_position(p12)
    assert rank_profile(p9) == {1: 9, 2: 36, 3: 84, 4: 36, 5: 3}
    coefficientwise_check(p5, 0, 1)
    coefficientwise_check(p9, 0, 1)
    coefficientwise_check(p12, 0, 6)

    slack5 = pair_bound_and_moments(p5, 26)
    slack9 = pair_bound_and_moments(p9, 168)
    slack12 = pair_bound_and_moments(p12, 1061, require_minimal=False)
    assert slack5 == (0, 0)
    assert slack9 == (11, 20)
    assert slack12 == (-367, -261)

    hessian5 = hessian_audit(p5)
    hessian9 = hessian_audit(p9)
    hessian12 = hessian_audit(
        p12, [(0, 6), (1, 7), (2, 8), (5, 11)]
    )
    assert hessian5[0] < 0 < hessian5[1]
    assert hessian9[:2] == (-25, 47)
    assert hessian5[2] >= 0 and hessian5[4] >= 0
    assert hessian9[2] >= 0 and hessian9[4] >= 0
    assert hessian12[2] == -313

    print(
        "PASS: two-point minimizer gate; "
        "slack n5/n9/P12=%s/%s/%s; "
        "Hessian n5=%s n9=%s P12=%s"
        % (slack5, slack9, slack12, hessian5, hessian9, hessian12)
    )


if __name__ == "__main__":
    main()
