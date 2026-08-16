#!/usr/bin/env python3
"""Exact all-projection audit for the 14-point common-guard wrapper."""

from fractions import Fraction as Q
from itertools import combinations, product


def orient(a, b, c):
    value = ((b[0] - a[0]) * (c[1] - a[1])
             - (b[1] - a[1]) * (c[0] - a[0]))
    return (value > 0) - (value < 0)


def pocket_point(left, right):
    return ((left - right) / (left + right), -Q(2) / (left + right))


def configuration(seeds=None):
    interior = [(Q(0), Q(0)), (Q(1), Q(4)),
                (Q(2), Q(1)), (Q(4), Q(0))]
    if seeds is None:
        seeds = [interior] * 3
    epsilon = Q(1, 1000)
    clusters = []
    for parameter, seed in zip((Q(4), Q(1), Q(1, 4)), seeds):
        cluster = []
        for first, transverse in seed:
            left = (Q(1) / parameter + epsilon * first
                    + epsilon * epsilon * transverse)
            right = (parameter + epsilon * first
                     - epsilon * epsilon * transverse)
            cluster.append(pocket_point(left, right))
        clusters.append(cluster)
    points = [(Q(-1), Q(0))] + sum(clusters, []) + [(Q(1), Q(0))]
    return points, clusters


def convex(points):
    if len(points) <= 3:
        return True
    ordered = sorted(points)

    def half(sequence):
        chain = []
        for point in sequence:
            while len(chain) >= 2 and orient(chain[-2], chain[-1], point) <= 0:
                chain.pop()
            chain.append(point)
        return chain

    hull = half(ordered)[:-1] + half(reversed(ordered))[:-1]
    return len(hull) == len(ordered)


def projection_orders(points):
    # Every nonvertical projection direction is represented by x+t*y.
    # Pair ties occur at exact rational t.  Midpoints of consecutive tie
    # values give all chambers in one half-turn; reversing gives the other.
    critical = set()
    for i, j in combinations(range(len(points)), 2):
        dx = points[j][0] - points[i][0]
        dy = points[j][1] - points[i][1]
        if dy:
            critical.add(-dx / dy)
    critical = sorted(critical)
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)

    orders = []
    for slope in probes:
        order = tuple(sorted(range(len(points)),
                             key=lambda i: points[i][0] + slope * points[i][1]))
        assert len({points[i][0] + slope * points[i][1]
                    for i in range(len(points))}) == len(points)
        if order not in orders:
            orders.append(order)
        reverse = tuple(reversed(order))
        if reverse not in orders:
            orders.append(reverse)
    return orders


def chain_totals(points, order):
    n = len(points)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cap[i][j] = cup[i][j] = 1
            for h in range(i):
                sign = orient(points[order[h]], points[order[i]], points[order[j]])
                if sign < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def main():
    points, clusters = configuration()
    assert len(points) == 14
    assert all(orient(*triple) for triple in combinations(points, 3))

    transversals = 0
    for labels in product(range(4), repeat=3):
        face = [points[0]]
        face.extend(clusters[i][labels[i]] for i in range(3))
        face.append(points[-1])
        assert convex(face)
        transversals += 1
    assert transversals == 64

    faces = 0
    for mask in range(1, 1 << len(points)):
        face = [points[i] for i in range(len(points)) if mask >> i & 1]
        faces += convex(face)
    assert faces == 1914

    orders = projection_orders(points)
    profiles = [chain_totals(points, order) for order in orders]
    assert len(orders) == 174
    assert len(set(profiles)) == 174
    low = min(profiles, key=lambda row: row[0] * row[1])
    high = max(profiles, key=lambda row: row[0] * row[1])
    assert low in ((549, 286), (286, 549))
    assert low[0] * low[1] == 157014
    assert high[0] * high[1] == 289047
    assert min(max(row) for row in profiles) == 412

    cap = [(Q(i), -Q(i * i)) for i in range(4)]
    interior = [(Q(0), Q(0)), (Q(1), Q(4)),
                (Q(2), Q(1)), (Q(4), Q(0))]
    cup = [(Q(i), Q(i * i)) for i in range(4)]
    minimum_points, minimum_clusters = configuration([cap, interior, cup])
    assert all(orient(*triple)
               for triple in combinations(minimum_points, 3))
    minimum_faces = 0
    for mask in range(1, 1 << len(minimum_points)):
        face = [minimum_points[i] for i in range(len(minimum_points))
                if mask >> i & 1]
        minimum_faces += convex(face)
    assert minimum_faces == 1561
    minimum_orders = projection_orders(minimum_points)
    minimum_profiles = [chain_totals(minimum_points, order)
                        for order in minimum_orders]
    assert len(minimum_orders) == 174
    assert len(set(minimum_profiles)) == 172
    minimum_low = min(minimum_profiles,
                      key=lambda row: row[0] * row[1])
    minimum_high = max(minimum_profiles,
                       key=lambda row: row[0] * row[1])
    assert minimum_low in ((251, 539), (539, 251))
    assert minimum_low[0] * minimum_low[1] == 135289
    assert minimum_high[0] * minimum_high[1] == 231387
    assert min(max(row) for row in minimum_profiles) == 397

    print("PASS: interior-wrapper faces=1914, chambers=174, "
          "min CU=157014; mutation-minimizer faces=1561, chambers=174, "
          "min CU=135289")


if __name__ == "__main__":
    main()
