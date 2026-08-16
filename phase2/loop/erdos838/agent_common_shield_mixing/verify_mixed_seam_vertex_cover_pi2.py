#!/usr/bin/env python3
"""Exact checks for MIXED_SEAM_VERTEX_COVER_PI2_GATE.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb, prod


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def half(sequence):
        out = []
        for point in sequence:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    return half(points)[:-1] + half(reversed(points))[:-1]


def convex(points):
    return len(points) == len(set(points)) == len(hull(points))


def face_profile(points):
    profile = [0] * (len(points) + 1)
    for mask in range(1, 1 << len(points)):
        chosen = [points[i] for i in range(len(points)) if mask >> i & 1]
        if convex(chosen):
            profile[len(chosen)] += 1
    return profile


def chain_counts(points, order):
    """Nonempty cap/cup counts in a prescribed projection order."""
    n = len(order)
    negative = [[0] * n for _ in range(n)]
    positive = [[0] * n for _ in range(n)]
    for right in range(1, n):
        for middle in range(right):
            negative[middle][right] = 1
            positive[middle][right] = 1
            for left in range(middle):
                sign = orient(points[order[left]], points[order[middle]],
                              points[order[right]])
                assert sign != 0
                if sign < 0:
                    negative[middle][right] += negative[left][middle]
                else:
                    positive[middle][right] += positive[left][middle]
    return (n + sum(map(sum, negative)),
            n + sum(map(sum, positive)))


def chamber_representatives(points):
    walls = sorted({
        -(points[j][0] - points[i][0]) / (points[j][1] - points[i][1])
        for i, j in combinations(range(len(points)), 2)
        if points[j][1] != points[i][1]
    })
    if not walls:
        return [F(0)]
    return [walls[0] - 1] + [
        (left + right) / 2 for left, right in zip(walls, walls[1:])
    ] + [walls[-1] + 1]


def build_instance():
    q = 4
    eta = F(1, 100 * q * q)
    epsilon = F(1, 10 ** 7)
    local = [(F(0), F(0)), (F(1), F(1)),
             (F(2), F(3)), (F(3), F(2))]
    blocks = []
    for index in range(q):
        center = (F(index), eta * index * index)
        blocks.append([(center[0] + epsilon * x,
                        center[1] + epsilon * y)
                       for x, y in local])
    points = sum(blocks, [])
    assert all(orient(*triple) != 0 for triple in combinations(points, 3))
    return blocks, points


def bad_pair_graphs(blocks):
    graphs = []
    for i, block in enumerate(blocks):
        edges = set()
        ordered = sorted(range(len(block)), key=lambda label: block[label][0])
        for first_position, second_position in combinations(range(len(ordered)), 2):
            first, second = ordered[first_position], ordered[second_position]
            bad = False
            for j, external in enumerate(blocks):
                if i == j:
                    continue
                if i < j:
                    if any(orient(block[first], block[second], point) >= 0
                           for point in external):
                        bad = True
                else:
                    if any(orient(point, block[first], block[second]) <= 0
                           for point in external):
                        bad = True
            if bad:
                edges.add(frozenset((first, second)))
        graphs.append(edges)
    return graphs


def local_reduced_profiles(block):
    """W,C,U after deleting the cover marker with local label 3."""
    block = block[:3]
    order = tuple(sorted(range(len(block)), key=lambda label: block[label][0]))
    w = c = u = 0
    for mask in range(1, 1 << len(block)):
        chosen_labels = [label for label in order if mask >> label & 1]
        chosen = [block[label] for label in chosen_labels]
        if convex(chosen):
            w += 1
        if len(chosen) <= 2 or all(
                orient(chosen[i], chosen[j], chosen[k]) < 0
                for i, j, k in combinations(range(len(chosen)), 3)):
            c += 1
        if len(chosen) <= 2 or all(
                orient(chosen[i], chosen[j], chosen[k]) > 0
                for i, j, k in combinations(range(len(chosen)), 3)):
            u += 1
    return w, c, u


def audit_fixed_gap_bootstrap():
    """Exact coefficient arithmetic and the matching contrapositive."""
    cases = 0
    coefficient = F(3, 8)
    for ell in range(128, 513):
        q = ell // 4
        retained = q // 2
        log_ell_ceiling = (ell - 1).bit_length()
        log_q_ceiling = (q - 1).bit_length()
        # Balanced A=n/q, followed by the survivor loss (log n)^3.
        log_s_lower = ell - log_q_ceiling - 3 * log_ell_ceiling
        assert log_s_lower > 0
        endpoint = coefficient * log_s_lower * log_s_lower - 2 * log_s_lower
        reset = min(endpoint - ell,
                    F(retained, retained + 1) * endpoint
                    - F(2 * ell, retained + 1))
        assert reset >= (coefficient * ell * ell
                         - 10 * ell * log_ell_ceiling)

        alphabet = 1 << ell
        survivors = alphabet // (ell ** 3)
        bad_roles = q - retained + 1
        matching = bad_roles * (alphabet - survivors) // 2
        total_labels = q * alphabet
        assert matching >= total_labels // 8
        cases += 1
    return cases


def main():
    blocks, points = build_instance()
    q = len(blocks)
    a = len(blocks[0])

    transversals = 0
    for labels in product(range(a), repeat=q):
        assert convex([blocks[i][labels[i]] for i in range(q)])
        transversals += 1
    assert transversals == a ** q == 256

    graphs = bad_pair_graphs(blocks)
    expected = {frozenset((2, 3))}
    assert all(graph == expected for graph in graphs)

    # Delete label 3 in every block.  The induced blocks have exact vertical
    # strong-glue signs for every ordered block pair.
    keep_global = [4 * i + label for i in range(q) for label in (0, 1, 2)]
    reduced = [points[index] for index in keep_global]
    for i, j in combinations(range(q), 2):
        left = [blocks[i][label] for label in (0, 1, 2)]
        right = [blocks[j][label] for label in (0, 1, 2)]
        assert max(point[0] for point in left) < min(point[0] for point in right)
        assert all(orient(left[r], left[s], point) < 0
                   for r, s in combinations(range(3), 2) for point in right)
        assert all(orient(point, right[r], right[s]) > 0
                   for point in left for r, s in combinations(range(3), 2))

    full_profile = face_profile(points)
    reduced_profile = face_profile(reduced)
    full_profile_with_empty = list(full_profile)
    reduced_profile_with_empty = list(reduced_profile)
    full_profile_with_empty[0] = 1
    reduced_profile_with_empty[0] = 1
    for rank in range(len(full_profile)):
        bound = sum(
            comb(q, j) * reduced_profile_with_empty[rank - j]
            for j in range(max(0, rank - len(reduced_profile_with_empty) + 1),
                           min(q, rank) + 1)
        )
        assert full_profile_with_empty[rank] <= bound
    assert 1 + sum(full_profile) <= 2 ** q * (1 + sum(reduced_profile))

    # Exact strong-composition recurrence for the repaired ordinary faces.
    profiles = [local_reduced_profiles(block) for block in blocks]
    recurrence = sum(row[0] for row in profiles)
    for i, j in combinations(range(q), 2):
        recurrence += (profiles[i][1] * profiles[j][2]
                       * prod(1 + 3 for k in range(i + 1, j)))
    assert recurrence == sum(reduced_profile)

    # The fixed deletion decoder works simultaneously in every direction.
    chambers = chamber_representatives(points)
    max_cap_ratio = max_cup_ratio = F(0)
    for amount in chambers:
        order = tuple(sorted(range(len(points)),
                             key=lambda i: points[i][0] + amount * points[i][1]))
        reduced_order_global = [index for index in order if index in keep_global]
        relabel = {global_label: local_label
                   for local_label, global_label in enumerate(keep_global)}
        reduced_order = tuple(relabel[index] for index in reduced_order_global)
        cap, cup = chain_counts(points, order)
        reduced_cap, reduced_cup = chain_counts(reduced, reduced_order)
        assert reduced_cap + 1 <= cap + 1 <= 2 ** q * (reduced_cap + 1)
        assert reduced_cup + 1 <= cup + 1 <= 2 ** q * (reduced_cup + 1)
        max_cap_ratio = max(max_cap_ratio, F(cap + 1, reduced_cap + 1))
        max_cup_ratio = max(max_cup_ratio, F(cup + 1, reduced_cup + 1))

    bootstrap_cases = audit_fixed_gap_bootstrap()
    print("PASS: q=4 A=4; singleton transversals=%d; bad graphs=%s; "
          "faces full/repaired=%d/%d; chambers=%d; max cap/cup ratios=%s/%s"
          "; fixed-gap cases=%d"
          % (transversals, [len(graph) for graph in graphs], sum(full_profile),
             sum(reduced_profile), len(chambers), max_cap_ratio, max_cup_ratio,
             bootstrap_cases))


if __name__ == "__main__":
    main()
