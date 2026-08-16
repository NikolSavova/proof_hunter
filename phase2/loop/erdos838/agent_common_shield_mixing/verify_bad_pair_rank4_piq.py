#!/usr/bin/env python3
"""Exact checks for BAD_PAIR_RANK4_PIQ_CLASSIFICATION.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb

from verify_mixed_seam_vertex_cover_pi2 import build_instance, convex, hull, orient


def interior_label(points):
    if convex(points):
        return None
    boundary = set(hull(points))
    hidden = [index for index, point in enumerate(points) if point not in boundary]
    assert len(hidden) == 1
    return hidden[0]


def inside_triangle(point, triangle):
    signs = [orient(triangle[i], triangle[(i + 1) % 3], point)
             for i in range(3)]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def rank_four_audit():
    blocks, _ = build_instance()
    records = []
    decoded = set()
    # The two internal roles have both canonical neighbors.
    for role in (1, 2):
        left = blocks[role - 1][0]
        first, second = blocks[role][2], blocks[role][3]
        right = blocks[role + 1][0]
        record = [left, first, second, right]
        hidden = interior_label(record)
        assert hidden in (0, 1, 2, 3)
        triangle = [record[index] for index in range(4) if index != hidden]
        assert inside_triangle(record[hidden], triangle)
        # Delete the left anchor: the ordinary output retains the full pair.
        output = frozenset((first, second, right))
        assert convex(list(output)) and output not in decoded
        decoded.add(output)
        records.append(hidden)

    # Local marked-pair records do not automatically multiply across roles.
    assert all(not convex(sum(([blocks[i][2], blocks[i][3]] for i in roles), []))
               for roles in combinations(range(len(blocks)), 3))

    # Explicit rational representatives of all four rooted circuit types
    # and one convex type, ordered as left,pair0,pair1,right.
    samples = [[(F(0), F(0)), (F(1), F(-1)),
                (F(2), F(-1)), (F(3), F(0))]]
    triangle = [(F(0), F(0)), (F(4), F(0)), (F(0), F(4))]
    interior = (F(1), F(1))
    for hidden in range(4):
        sample = []
        vertices = iter(triangle)
        for label in range(4):
            sample.append(interior if label == hidden else next(vertices))
        samples.append(sample)
    hidden_types = []
    for sample in samples:
        assert all(orient(*triple) != 0 for triple in combinations(sample, 3))
        hidden_types.append(interior_label(sample))
    assert set(hidden_types) == {None, 0, 1, 2, 3}

    # In an anchor-inner record, the rooted ray exits through the pair edge.
    anchor_sample = next(sample for sample in samples if interior_label(sample) == 0)
    left, a, b, right = anchor_sample
    # Solve right + t(left-right) = a + u(b-a); anchor-inner gives t>1 and 0<u<1.
    vx, vy = left[0] - right[0], left[1] - right[1]
    wx, wy = b[0] - a[0], b[1] - a[1]
    det = vx * (-wy) - vy * (-wx)
    rhsx, rhsy = a[0] - right[0], a[1] - right[1]
    t = (rhsx * (-wy) - rhsy * (-wx)) / det
    u = (vx * rhsy - vy * rhsx) / det
    assert t > 1 and 0 < u < 1
    return records, hidden_types, t, u


def mobius(matrix, value):
    a, b, c, d = matrix
    denominator = c * value + d
    if denominator == 0:
        return None
    return (a * value + b) / denominator


def cross_ratio(values):
    a, b, c, d = values
    assert None not in values
    return (a - c) * (b - d) / ((a - d) * (b - c))


def coherent_itinerary_audit():
    seed = [(F(0), F(0)), (F(1), F(2)), (F(2), F(-1)), (F(4), F(1))]
    walls = sorted({
        -(seed[j][0] - seed[i][0]) / (seed[j][1] - seed[i][1])
        for i, j in combinations(range(len(seed)), 2)
        if seed[j][1] != seed[i][1]
    })
    queries = (F(-3), F(-1), F(1), F(3))

    def chamber(value):
        if value is None:
            return len(walls)
        return sum(wall < value for wall in walls)

    itineraries = set()
    matrices = 0
    base_cross_ratio = cross_ratio(queries)
    for entries in product(range(-3, 4), repeat=4):
        a, b, c, d = map(F, entries)
        if a * d - b * c == 0:
            continue
        matrix = (a, b, c, d)
        transformed = tuple(mobius(matrix, value) for value in queries)
        if None in transformed or len(set(transformed)) < 4:
            continue
        assert cross_ratio(transformed) == base_cross_ratio
        itineraries.add(tuple(chamber(value) for value in transformed))
        matrices += 1

    h = len(queries) * len(walls)
    # A deliberately loose explicit cubic envelope for the exact sample;
    # the report's theorem is the symbolic arrangement bound.
    bound = 8 * (h + 1) ** 3
    assert len(itineraries) <= bound
    assert matrices > 1000 and len(itineraries) > 10
    return len(walls), matrices, len(itineraries), bound, base_cross_ratio


def main():
    records, types, ray_t, ray_u = rank_four_audit()
    walls, matrices, itineraries, bound, ratio = coherent_itinerary_audit()
    print("PASS: wrapper hidden records=%s; five types=%s; fan ray=(%s,%s); "
          "critical walls=%d; PGL2 matrices=%d; itineraries=%d<=%d; cross-ratio=%s"
          % (records, types, ray_t, ray_u, walls, matrices, itineraries, bound,
             ratio))


if __name__ == "__main__":
    main()
