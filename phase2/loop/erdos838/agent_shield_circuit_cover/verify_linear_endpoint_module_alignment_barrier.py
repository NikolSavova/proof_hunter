#!/usr/bin/env python3
"""Exact regression for LINEAR_ENDPOINT_MODULE_ALIGNMENT_BARRIER.md."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations


Point = tuple[Q, Q]


def det(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def signs(points):
    out = {}
    for triple in combinations(range(len(points)), 3):
        value = det(*(points[i] for i in triple))
        assert value
        out[triple] = 1 if value > 0 else -1
    return out


def is_cap(points, trace):
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(det(word[i], word[j], word[k]) < 0
               for i, j, k in combinations(range(len(word)), 3))


def is_cup(points, trace):
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(det(word[i], word[j], word[k]) > 0
               for i, j, k in combinations(range(len(word)), 3))


def hull(points, trace):
    word = sorted((points[i], i) for i in trace)
    if len(word) <= 1:
        return [i for _, i in word]
    lower = []
    for p, idx in word:
        while len(lower) >= 2 and det(lower[-2][0], lower[-1][0], p) <= 0:
            lower.pop()
        lower.append((p, idx))
    upper = []
    for p, idx in reversed(word):
        while len(upper) >= 2 and det(upper[-2][0], upper[-1][0], p) <= 0:
            upper.pop()
        upper.append((p, idx))
    return [idx for _, idx in lower[:-1] + upper[:-1]]


def is_face(points, trace):
    return len(hull(points, trace)) == len(trace)


def profile(points):
    C = U = H = 0
    for mask in range(1, 1 << len(points)):
        trace = tuple(i for i in range(len(points)) if mask >> i & 1)
        C += is_cap(points, trace)
        U += is_cup(points, trace)
        H += is_face(points, trace)
    return C, U, H


def endpoint_module(points):
    order = sorted(range(len(points)), key=lambda i: points[i][0])
    endpoint = (order[0], order[-1])
    caps = []
    cups = []
    for mask in range(1, 1 << len(points)):
        trace = tuple(i for i in range(len(points)) if mask >> i & 1)
        if not set(endpoint) <= set(trace):
            continue
        local = sorted(trace, key=lambda i: points[i][0])
        if (local[0], local[-1]) != endpoint:
            continue
        if is_cap(points, trace):
            caps.append(frozenset(trace))
        if is_cup(points, trace):
            cups.append(frozenset(trace))
    unions = {cap | cup for cap in caps for cup in cups}
    assert len(unions) == len(caps) * len(cups)
    assert all(is_face(points, union) for union in unions)
    return endpoint, caps, cups


def root_slope(points):
    order = sorted(points)
    a, b = order[0], order[-1]
    return (b[1] - a[1]) / (b[0] - a[0])


def linear_glue(blocks, shears, epsilon=Q(1, 10**6)):
    """Direct rational q-role linear strong glue over a macro parabola."""
    assert len(blocks) == len(shears)
    points = []
    labels = []
    for role, (block, shear) in enumerate(zip(blocks, shears)):
        for x, y in block:
            points.append((
                Q(role) + epsilon * epsilon * x,
                Q(role * role) + epsilon * (y + shear * x),
            ))
            labels.append(role)
    assert [p[0] for p in points] == sorted(p[0] for p in points)

    # Full oriented block law: distinct roles are a cup; an internal pair
    # is steeper than every macro seam.
    for i, j, k in combinations(range(len(points)), 3):
        roles = (labels[i], labels[j], labels[k])
        value = det(points[i], points[j], points[k])
        assert value
        if roles[0] < roles[1] < roles[2]:
            assert value > 0
        elif roles[0] == roles[1] < roles[2]:
            assert value < 0
        elif roles[0] < roles[1] == roles[2]:
            assert value > 0
        else:
            assert roles[0] == roles[1] == roles[2]
    return points, labels


def exact_linear_audit(blocks, shears):
    parent, labels = linear_glue(blocks, shears)
    local_profiles = [profile(block) for block in blocks]
    q = len(blocks)
    expected = sum(row[2] for row in local_profiles)
    for i in range(q):
        for j in range(i + 1, q):
            term = local_profiles[i][0] * local_profiles[j][1]
            for role in range(i + 1, j):
                term *= 1 + len(blocks[role])
            expected += term

    actual = 0
    characterized = 0
    for mask in range(1, 1 << len(parent)):
        trace = tuple(i for i in range(len(parent)) if mask >> i & 1)
        face = is_face(parent, trace)
        occupied = sorted({labels[i] for i in trace})
        if len(occupied) == 1:
            role = occupied[0]
            local = tuple(i - sum(map(len, blocks[:role])) for i in trace)
            predicted = is_face(blocks[role], local)
        else:
            first, last = occupied[0], occupied[-1]
            offsets = [sum(map(len, blocks[:role])) for role in range(q)]
            first_trace = tuple(
                i - offsets[first] for i in trace if labels[i] == first
            )
            last_trace = tuple(
                i - offsets[last] for i in trace if labels[i] == last
            )
            predicted = (
                is_cap(blocks[first], first_trace)
                and is_cup(blocks[last], last_trace)
                and all(sum(labels[i] == role for i in trace) <= 1
                        for role in occupied[1:-1])
            )
        assert face == predicted
        actual += face
        characterized += predicted
    assert actual == characterized == expected
    return parent, labels, local_profiles, actual


if __name__ == "__main__":
    raw_blocks = [
        [(0, -4), (1, -3), (2, -3), (7, -2)],
        [(0, -4), (1, -3), (2, -4), (7, 4)],
        [(0, -4), (1, -4), (2, -3), (7, -3)],
    ]
    blocks = [[(Q(x), Q(y)) for x, y in block] for block in raw_blocks]
    assert all(len(signs(block)) == 4 for block in blocks)

    # Perfectly align the three distinguished endpoint chords.
    target = Q(20)
    aligned_shears = [target - root_slope(block) for block in blocks]
    aligned, labels, profiles, faces = exact_linear_audit(
        blocks, aligned_shears
    )
    aligned_slopes = []
    for role in range(len(blocks)):
        trace = [aligned[i] for i, value in enumerate(labels) if value == role]
        aligned_slopes.append(root_slope(trace))
    assert len(set(aligned_slopes)) == 1

    # An anti-aligned metric itinerary has the identical labeled chirotope.
    free_shears = [Q(13), Q(37), Q(23)]
    free, free_labels, free_profiles, free_faces = exact_linear_audit(
        blocks, free_shears
    )
    assert labels == free_labels
    assert signs(aligned) == signs(free)
    assert profiles == free_profiles and faces == free_faces
    free_slopes = []
    for role in range(len(blocks)):
        trace = [free[i] for i, value in enumerate(labels) if value == role]
        free_slopes.append(root_slope(trace))
    assert len(set(free_slopes)) == len(blocks)

    modules = [endpoint_module(block) for block in blocks]
    module_sizes = [(len(caps), len(cups)) for _, caps, cups in modules]
    print(
        "PASS: exact linear recurrence and trace classification, aligned and "
        "free endpoint-slope itineraries have identical chirotope; "
        f"profiles={profiles}, modules={module_sizes}, faces={faces}, "
        f"aligned_slope={aligned_slopes[0]}, free_slopes={free_slopes}"
    )
