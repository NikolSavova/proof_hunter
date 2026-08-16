#!/usr/bin/env python3
"""Exact verifier for THREE_EAR_MINIMIZER_BARRIER_AND_ORDER_THREE_GATE."""

from __future__ import annotations

import json
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
from agent_outer_internal_product.verify_minimizer_two_point_extension_interaction_gate import (  # noqa: E402
    extension_profile,
    face_count,
    rank_profile,
)


Point = tuple[Fraction, Fraction]
Inequality = tuple[Fraction, Fraction, Fraction]


def nine_points():
    data = json.loads(
        (ERDOS / "agent_lex_minimizer_search"
         / "exact_realizable_n9.json").read_text()
    )
    return [(Fraction(x), Fraction(y))
            for x, y in data["coordinates_as_stored"]]


def five_points():
    return [
        (Fraction(6), Fraction(15)),
        (Fraction(18), Fraction(22)),
        (Fraction(13), Fraction(4)),
        (Fraction(12), Fraction(17)),
        (Fraction(20), Fraction(29)),
    ]


def pascal_wrapper():
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    return sorted(rt.strong_glue(q, q, Fraction(1, 16384)))


def general_position(points):
    return all(rt.determinant(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def hull_indices(points, indices):
    ordered = sorted(indices, key=lambda index: points[index])

    def chain(sequence):
        result = []
        for index in sequence:
            while (len(result) >= 2
                   and rt.determinant(points[result[-2]], points[result[-1]],
                                      points[index]) <= 0):
                result.pop()
            result.append(index)
        return result

    hull = chain(ordered)[:-1] + chain(list(reversed(ordered)))[:-1]
    area = sum(
        points[hull[i]][0] * points[hull[(i + 1) % len(hull)]][1]
        - points[hull[i]][1] * points[hull[(i + 1) % len(hull)]][0]
        for i in range(len(hull))
    )
    if area < 0:
        hull.reverse()
    return hull


def directed_line(points, first, second):
    ax, ay = points[first]
    bx, by = points[second]
    return (
        -(by - ay),
        bx - ax,
        (by - ay) * ax - (bx - ax) * ay,
    )


def ear_system(points, source, target_edge):
    hull = hull_indices(points, source)
    inequalities = []
    found = False
    for index in range(len(hull)):
        first = hull[index]
        second = hull[(index + 1) % len(hull)]
        a, b, c = directed_line(points, first, second)
        if {first, second} == set(target_edge):
            a, b, c = -a, -b, -c
            found = True
        inequalities.append((a, b, c))
    assert found
    return tuple(inequalities)


def fourier_motzkin(inequalities):
    """Return an exact strict-feasibility witness, or None."""
    lower = []
    upper = []
    x_conditions = []
    for a, b, c in inequalities:
        if b > 0:
            lower.append((-a / b, -c / b))
        elif b < 0:
            upper.append((-a / b, -c / b))
        else:
            x_conditions.append((a, c))
    for lower_slope, lower_offset in lower:
        for upper_slope, upper_offset in upper:
            x_conditions.append((
                upper_slope - lower_slope,
                upper_offset - lower_offset,
            ))

    lower_x = None
    upper_x = None
    for coefficient, constant in x_conditions:
        if coefficient == 0:
            if constant <= 0:
                return None
        elif coefficient > 0:
            bound = -constant / coefficient
            lower_x = bound if lower_x is None else max(lower_x, bound)
        else:
            bound = -constant / coefficient
            upper_x = bound if upper_x is None else min(upper_x, bound)
    if (lower_x is not None and upper_x is not None
            and lower_x >= upper_x):
        return None
    if lower_x is None and upper_x is None:
        x = Fraction(0)
    elif lower_x is None:
        x = upper_x - 1
    elif upper_x is None:
        x = lower_x + 1
    else:
        x = (lower_x + upper_x) / 2

    lower_y = max((slope * x + offset for slope, offset in lower),
                  default=None)
    upper_y = min((slope * x + offset for slope, offset in upper),
                  default=None)
    if lower_y is not None and upper_y is not None and lower_y >= upper_y:
        return None
    if lower_y is None and upper_y is None:
        y = Fraction(0)
    elif lower_y is None:
        y = upper_y - 1
    elif upper_y is None:
        y = lower_y + 1
    else:
        y = (lower_y + upper_y) / 2
    assert all(a * x + b * y + c > 0 for a, b, c in inequalities)
    return x, y


def generic_witness(points, deleted, inequalities):
    witness = fourier_motzkin(inequalities)
    assert witness is not None
    fixed = [point for index, point in enumerate(points) if index != deleted]
    for scale in (10 ** power for power in range(3, 20)):
        candidate = (
            witness[0] + Fraction(1, scale),
            witness[1] + Fraction(1, scale * scale),
        )
        if (all(a * candidate[0] + b * candidate[1] + c > 0
                for a, b, c in inequalities)
                and general_position(fixed + [candidate])):
            return candidate
    raise AssertionError("no generic point found inside open ear intersection")


def three_ear_check():
    points = nine_points()
    deleted = 2
    sources = (
        (0, 1, 6),
        (0, 1, 7),
        (1, 3, 8),
    )
    edges = ((6, 1), (7, 1), (3, 8))
    systems = tuple(
        ear_system(points, source, edge)
        for source, edge in zip(sources, edges)
    )
    for source in sources:
        assert convex([points[index] for index in source])
        hull = hull_indices(points, source + (deleted,))
        assert deleted not in hull
    for first, second in combinations(range(3), 2):
        combined = systems[first] + systems[second]
        witness = generic_witness(points, deleted, combined)
        assert convex([points[index] for index in sources[first]] + [witness])
        assert convex([points[index] for index in sources[second]] + [witness])
    assert fourier_motzkin(systems[0] + systems[1] + systems[2]) is None

    certificate = (systems[0][1], systems[1][2], systems[2][1])
    assert certificate == (
        (Fraction(-37889), Fraction(-47280), Fraction(2718566006)),
        (Fraction(-51607), Fraction(12012), Fraction(102579486)),
        (Fraction(37222), Fraction(9726), Fraction(-1005338594)),
    )
    multipliers = (158173391, 231891291, 482516938)
    assert sum(multipliers[i] * certificate[i][0]
               for i in range(3)) == 0
    assert sum(multipliers[i] * certificate[i][1]
               for i in range(3)) == 0
    assert sum(multipliers[i] * certificate[i][2]
               for i in range(3)) == -31300806765102400

    def ordinary_union(indices):
        return convex([points[index] for index in sorted(set(indices))])

    for first, second in combinations(range(3), 2):
        assert not ordinary_union(sources[first] + sources[second])
    assert not ordinary_union(sources[0] + sources[1] + sources[2])
    return tuple(len(system) for system in systems)


def coefficientwise_third_check(points, indices):
    anchors = [points[index] for index in indices]
    base = [point for index, point in enumerate(points) if index not in indices]
    full_profile = {0: 1, **rank_profile(base + anchors)}
    base_profile = {0: 1, **rank_profile(base)}
    profiles = {}
    for size in range(1, 4):
        for subset in combinations(range(3), size):
            profiles[subset] = extension_profile(
                base, *(anchors[index] for index in subset)
            )
    for rank in range(len(points) + 1):
        expected = base_profile.get(rank, 0)
        for subset, profile in profiles.items():
            expected += profile.get(rank - len(subset), 0)
        assert full_profile.get(rank, 0) == expected
    triple = profiles[(0, 1, 2)]
    assert sum(triple.values()) <= face_count(base) + 1


def triple_bound_and_moments(points, expected_v, require_minimal=True):
    n = len(points)
    v = face_count(points)
    assert v == expected_v
    slacks = []
    left_moment = 0
    cap_deleted_sum = 0
    cup_deleted_sum = 0
    branch_counts = [0, 0, 0, 0]
    for deleted in combinations(range(n), 3):
        base = [point for index, point in enumerate(points)
                if index not in deleted]
        faces, caps, cups = families(base)
        loss = v - len(faces)
        size = len(base)
        branches = (
            7 + 6 * len(caps),
            7 + 6 * len(cups),
            7 + 3 * len(caps) + len(cups) + 3 * size,
            7 + len(caps) + 3 * len(cups) + 3 * size,
        )
        minimum = min(branches)
        slacks.append(minimum - loss)
        branch_counts[branches.index(minimum)] += 1
        cap_deleted_sum += len(caps)
        cup_deleted_sum += len(cups)

    for rank, count in rank_profile(points).items():
        left_moment += count * (
            n * (n - 1) * (n - 2) // 6
            - (n - rank) * (n - rank - 1) * (n - rank - 2) // 6
        )
    triples = n * (n - 1) * (n - 2) // 6
    right_sides = (
        7 * triples + 6 * cap_deleted_sum,
        7 * triples + 6 * cup_deleted_sum,
        (3 * n - 2) * triples + 3 * cap_deleted_sum + cup_deleted_sum,
        (3 * n - 2) * triples + cap_deleted_sum + 3 * cup_deleted_sum,
    )
    if require_minimal:
        assert all(left_moment <= right for right in right_sides)
    else:
        assert any(left_moment > right for right in right_sides)
    return (min(slacks), max(slacks)), tuple(branch_counts)


def main():
    p5 = five_points()
    p9 = nine_points()
    p12 = pascal_wrapper()
    assert general_position(p5)
    assert general_position(p9)
    assert general_position(p12)
    assert rank_profile(p9) == {1: 9, 2: 36, 3: 84, 4: 36, 5: 3}

    systems = three_ear_check()
    coefficientwise_third_check(p5, (0, 1, 2))
    coefficientwise_third_check(p9, (0, 1, 2))
    coefficientwise_third_check(p12, (0, 6, 7))

    audit5 = triple_bound_and_moments(p5, 26)
    audit9 = triple_bound_and_moments(p9, 168)
    audit12 = triple_bound_and_moments(p12, 1061, require_minimal=False)
    assert audit5 == ((2, 2), (10, 0, 0, 0))
    assert audit9 == ((19, 34), (0, 0, 21, 63))
    assert audit12 == ((-434, -305), (0, 0, 110, 110))

    print(
        "PASS: three-ear minimizer barrier; ear inequalities=%s; "
        "triple audits n5/n9/P12=%s/%s/%s"
        % (systems, audit5, audit9, audit12)
    )


if __name__ == "__main__":
    main()
