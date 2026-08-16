#!/usr/bin/env python3
"""Exact checks for MULTIROLE_ENDPOINT_POCKET_TRANSFER.md."""

from fractions import Fraction as Q
from itertools import combinations, product
from math import comb, log2
from random import Random

from verify_mixed_seam_vertex_cover_pi2 import convex


def geometric_ear_audit():
    base = [(-3, -3), (3, -3), (3, 3), (-3, 3)]
    menus = {
        0: [(-2, -5), (0, -6), (2, -5)],
        1: [(5, -2), (6, 0), (5, 2)],
        2: [(2, 5), (0, 6), (-2, 5)],
        3: [(-5, 2), (-6, 0), (-5, -2)],
    }
    for menu in menus.values():
        assert all(convex(base + [point]) for point in menu)

    counts = []
    for active in ((0, 2), (1, 3)):
        outputs = set()
        for choices in product(range(3), repeat=2):
            points = [menus[active[j]][choices[j]] for j in range(2)]
            assert convex(base + points)
            outputs.add(frozenset(base + points))
        assert len(outputs) == 3 ** len(active)
        counts.append(len(outputs))
    return counts


def rooted_reservoir_audit():
    # Every subset of each three-label menu is a rooted ear.  Arbitrary
    # rooted subsets on opposite (hence nonincident) square edges commute.
    base = [(-3, -3), (3, -3), (3, 3), (-3, 3)]
    menus = {
        0: [(-2, -5), (0, -6), (2, -5)],
        1: [(5, -2), (6, 0), (5, 2)],
        2: [(2, 5), (0, 6), (-2, 5)],
        3: [(-5, 2), (-6, 0), (-5, -2)],
    }
    complexes = {}
    for gap, menu in menus.items():
        complexes[gap] = []
        for mask in range(1 << len(menu)):
            rooted = tuple(menu[i] for i in range(len(menu)) if mask >> i & 1)
            assert convex(base + list(rooted))
            complexes[gap].append(rooted)
        assert len(complexes[gap]) == 8

    products = []
    for left, right in ((0, 2), (1, 3)):
        outputs = set()
        for first in complexes[left]:
            for second in complexes[right]:
                assert convex(base + list(first) + list(second))
                outputs.add(frozenset(base + list(first) + list(second)))
        assert len(outputs) == len(complexes[left]) * len(complexes[right]) == 64
        products.append(len(outputs))

    # Pairwise rooted compatibility does not characterize the complex.
    u, b, v = (Q(-1), Q(0)), (Q(0), Q(-2)), (Q(1), Q(0))
    x = (Q(-3, 40), Q(7, 8))
    z = (Q(3, 40), Q(7, 8))
    y = (Q(2, 15), Q(8, 9))
    rooted_base = [u, b, v]
    endpoints = [x, z, y]
    for rank in (0, 1, 2):
        assert all(convex(rooted_base + list(subset))
                   for subset in combinations(endpoints, rank))
    assert not convex(rooted_base + endpoints)
    weights = (Q(3, 244), Q(13, 61), Q(189, 244))
    assert sum(weights) == 1 and all(weight > 0 for weight in weights)
    assert tuple(weights[0] * u[i] + weights[1] * x[i] + weights[2] * y[i]
                 for i in range(2)) == z
    rooted_complex = [subset for rank in range(4)
                      for subset in combinations(endpoints, rank)
                      if convex(rooted_base + list(subset))]
    assert len(rooted_complex) == 7
    return products, len(rooted_complex)


def orientation(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def cup_cap_audit():
    # Reverse-dominance tangent-coordinate antichains.  On these systems,
    # rooted faces are exactly the negative-orientation caps; positive
    # cups are triple-bad.  Check the full complex and ES inequalities.
    rng = Random(838)
    base = [(Q(0), Q(0)), (Q(1, 2), Q(-2)), (Q(1), Q(0))]
    systems = 0
    extrema = []
    for size in range(4, 9):
        accepted = 0
        while accepted < 8:
            left = sorted(rng.sample(range(1, 160), size))
            right = sorted(rng.sample(range(1, 160), size), reverse=True)
            points = [(Q(l, l + r), Q(1, l + r))
                      for l, r in zip(left, right)]
            if any(orientation(*triple) == 0
                   for triple in combinations(base + points, 3)):
                continue
            assert all(convex(base + [point]) for point in points)
            assert all(convex(base + list(pair))
                       for pair in combinations(points, 2))

            rooted_count = 0
            cap_max = cup_max = 0
            for mask in range(1 << size):
                indices = [i for i in range(size) if mask >> i & 1]
                triples = list(combinations(indices, 3))
                cap = all(orientation(points[i], points[j], points[k]) < 0
                          for i, j, k in triples)
                cup = all(orientation(points[i], points[j], points[k]) > 0
                          for i, j, k in triples)
                rooted = convex(base + [points[i] for i in indices])
                assert rooted == cap
                rooted_count += rooted
                if cap:
                    cap_max = max(cap_max, len(indices))
                if cup:
                    cup_max = max(cup_max, len(indices))

            assert size <= comb(cap_max + cup_max - 2, cap_max - 1)
            assert rooted_count >= 2 ** cap_max
            assert cup_max * log2(2 * cap_max) + 1e-12 >= log2(size)
            extrema.append((size, cap_max, cup_max, rooted_count))
            accepted += 1
            systems += 1
    return systems, extrema[-1]


def max_cycle_independent(vertices, q):
    vertices = set(vertices)
    if len(vertices) == q:
        return q // 2
    start = next(i for i in range(q) if i not in vertices)
    best = 0
    run = 0
    for step in range(1, q + 1):
        point = (start + step) % q
        if point in vertices:
            run += 1
        else:
            best += (run + 1) // 2
            run = 0
    best += (run + 1) // 2
    return best


def cycle_audit():
    systems = 0
    for q in range(3, 13):
        for mask in range(1 << q):
            vertices = {i for i in range(q) if mask >> i & 1}
            assert 3 * max_cycle_independent(vertices, q) >= len(vertices)
            systems += 1
    return systems


def matching_audit():
    systems = 0
    poor = 0
    for m in range(1, 8):
        for values in product(range(3), repeat=m):
            compatible_endpoints = sum(values)
            zero_edges = sum(value == 0 for value in values)
            assert zero_edges >= m - compatible_endpoints
            for threshold in range(1, 6):
                if compatible_endpoints < threshold:
                    assert zero_edges >= m - threshold
                    poor += 1
            systems += 1
    return systems, poor


def product_threshold_audit():
    # A rich set of r gaps always has a canonical independent set of at
    # least ceil(r/3), hence K^floor(r/3) distinct endpoint words.
    cases = 0
    for q in range(3, 13):
        for mask in range(1 << q):
            rich = {i for i in range(q) if mask >> i & 1}
            independent = max_cycle_independent(rich, q)
            for alphabet in range(1, 6):
                count = alphabet ** independent
                assert count >= alphabet ** (len(rich) // 3)
                cases += 1
    return cases


def entropy_product_audit():
    # Use a fixed proper 3-coloring.  The largest color product cubed is at
    # least the total alphabet product, exactly the exponential form of
    # max color log-mass >= one third total log-mass.
    cases = 0
    for q in range(3, 9):
        if q % 2 == 0:
            colors = [i % 2 for i in range(q)]
        else:
            colors = [i % 2 for i in range(q - 1)] + [2]
        assert all(colors[i] != colors[(i + 1) % q] for i in range(q))
        for alphabets in product(range(1, 5), repeat=q):
            color_products = [1, 1, 1]
            for alphabet, color in zip(alphabets, colors):
                color_products[color] *= alphabet
            assert max(color_products) ** 3 >= product_value(alphabets)
            cases += 1
    return cases


def cyclic_runs(mask, q):
    deleted = {i for i in range(q) if mask >> i & 1}
    starts = [i for i in deleted if (i - 1) % q not in deleted]
    lengths = []
    for start in starts:
        length = 0
        point = start
        while point in deleted:
            length += 1
            point = (point + 1) % q
        lengths.append(length)
    return lengths


def mask_run_audit():
    systems = 0
    for q in range(3, 15):
        for mask in range(1, (1 << q) - 1):
            deleted = {i for i in range(q) if mask >> i & 1}
            retained = {i for i in range(q) if i not in deleted}
            if len(retained) < 3:
                continue
            runs = cyclic_runs(mask, q)
            assert len(runs) >= 1 and sum(runs) == len(deleted)
            assert max(runs) * len(runs) >= len(deleted)

            # A compressed gap is a retained label whose cyclic successor
            # after skipping deletions was not its original successor.
            compressed = 0
            for left in retained:
                right = (left + 1) % q
                while right in deleted:
                    right = (right + 1) % q
                if right != (left + 1) % q:
                    compressed += 1
            assert compressed == len(runs)
            systems += 1
    return systems


def product_value(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def main():
    geometric = geometric_ear_audit()
    rooted = rooted_reservoir_audit()
    cup_cap = cup_cap_audit()
    cycles = cycle_audit()
    matchings, poor = matching_audit()
    products = product_threshold_audit()
    entropy = entropy_product_audit()
    masks = mask_run_audit()
    print("PASS: geometric products=%s; rooted=%s; cup-cap=%s; "
          "cycle systems=%d; matching=%d "
          "poor=%d; product thresholds=%d entropy=%d masks=%d"
          % (geometric, rooted, cup_cap, cycles, matchings, poor,
             products, entropy, masks))


if __name__ == "__main__":
    main()
