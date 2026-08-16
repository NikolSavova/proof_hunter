#!/usr/bin/env python3
"""Exact checks for CRITICAL_EDGE_DISPERSION_RECHART_LEDGER."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import log2


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def build(sequence):
        out = []
        for point in sequence:
            while (len(out) >= 2
                   and orient(out[-2], out[-1], point) <= 0):
                out.pop()
            out.append(point)
        return out

    lower = build(points)
    upper = build(reversed(points))
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(points) <= 3 or len(hull(points)) == len(points)


def directional_sign(points):
    if len(points) <= 2:
        return 0
    signs = {1 if orient(*triple) > 0 else -1
             for triple in combinations(sorted(points), 3)}
    return next(iter(signs)) if len(signs) == 1 else None


def insertion_edge(base, root):
    old_hull = hull(base)
    new_hull = hull(base + [root])
    if len(old_hull) != len(base) or len(new_hull) != len(base) + 1:
        return None
    old_edges = {frozenset((old_hull[i], old_hull[(i + 1) % len(old_hull)]))
                 for i in range(len(old_hull))}
    new_edges = {frozenset((new_hull[i], new_hull[(i + 1) % len(new_hull)]))
                 for i in range(len(new_hull))}
    missing = old_edges - new_edges
    return next(iter(missing)) if len(missing) == 1 else None


def root_to_infinity(point, root):
    x, y = point
    z0, height = root
    denominator = height - y
    assert denominator > 0
    return (x - z0) / denominator, Fraction(1) / denominator


def configuration():
    f = Fraction
    left, right = (f(-5), f(0)), (f(5), f(0))
    y_cloud = [
        (f(-1991, 1000), f(3019, 1000)),
        (f(-1997, 1000), f(2997, 1000)),
        (f(-503, 250), f(2991, 1000)),
    ]
    w_cloud = [
        (f(99, 50), f(3001, 1000)),
        (f(503, 250), f(3009, 1000)),
        (f(1009, 500), f(597, 200)),
    ]
    lower_cloud = [
        (f(1, 1000), f(-797, 200)),
        (f(19, 1000), f(-2009, 500)),
        (f(1, 250), f(-401, 100)),
    ]
    root_cloud = [
        (f(-1, 50), f(39701, 10000)),
        (f(0), f(4)),
        (f(1, 50), f(40301, 10000)),
    ]
    points = ([left, right] + y_cloud + w_cloud
              + lower_cloud + root_cloud)
    assert general_position(points)
    return left, right, y_cloud, w_cloud, lower_cloud, root_cloud


def geometric_audit():
    left, right, ys, ws, lowers, roots = configuration()
    carriers = []
    edge_counts = Counter()
    mixed = set()
    pair_failures = 0
    for y, w, lower in product(ys, ws, lowers):
        base = [left, y, w, right, lower]
        assert convex(base)
        assert directional_sign([left, y, w, right]) == -1
        assert directional_sign([left, lower, right]) == 1
        carriers.append(tuple(base))
        for root in roots:
            assert convex(base + [root])
            edge = insertion_edge(base, root)
            assert edge == frozenset((y, w))
            edge_counts[edge] += 1
            output = frozenset(base + [root])
            assert output not in mixed
            mixed.add(output)
        for first, second in combinations(roots, 2):
            assert not convex(base + [first, second])
            pair_failures += 1

    assert len(carriers) == 27
    assert len(edge_counts) == 9
    # Counts include all three roots: each edge has three lower choices
    # times three roots. The carrier fibre itself has size three.
    assert set(edge_counts.values()) == {9}
    assert len(mixed) == 81
    assert pair_failures == 81

    # One root-to-infinity chart normalizes all 27 varying-edge carriers.
    chart_signs = {}
    for root in roots:
        signs = set()
        for base in carriers:
            image = [root_to_infinity(point, root) for point in base]
            sign = directional_sign(image)
            assert sign in (-1, 1)
            signs.add(sign)
            # The varying physical cage edge becomes the extreme pair.
            ordered = sorted(zip(image, base))
            assert frozenset((ordered[0][1], ordered[-1][1])) == insertion_edge(
                list(base), root
            )
        assert len(signs) == 1
        chart_signs[root] = next(iter(signs))
    assert len(set(chart_signs.values())) == 1
    return len(carriers), len(edge_counts), len(mixed), pair_failures


def weighted_ledger_audit():
    # Exhaust every small multiplicity table. Records in a cell have the
    # same physical (B,z); distinct nonzero cells are distinct mixed faces.
    checked = 0
    for entries in product(range(5), repeat=6):
        weight = sum(entries)
        incidence = sum(value > 0 for value in entries)
        load = max(entries)
        if weight:
            assert incidence >= Fraction(weight, load)
        else:
            assert incidence == 0 and load == 0
        checked += 1
    return checked


def asymptotic_audit():
    a = log2(3)
    theta = 2 - a
    for d in [64, 128, 256, 512]:
        s = t = max(1, round(0.2 * log2(d)))
        carriers = d ** (s + t)
        edge_fibre = d ** (s + t - 2)
        mixed = d * carriers
        assert Fraction(edge_fibre, carriers) == Fraction(1, d * d)
        assert mixed // carriers == d
        n = (s + t + 1) * d + 2
        assert d ** -2 <= n ** (-theta)
    return theta


def main():
    carriers, edges, mixed, pair_failures = geometric_audit()
    ledger_tables = weighted_ledger_audit()
    theta = asymptotic_audit()
    print(
        "PASS: cap-cup carriers=%d varying-edges=%d singleton-mixed=%d "
        "root-pair-failures=%d ledger-tables=%d theta=%.9f"
        % (carriers, edges, mixed, pair_failures, ledger_tables, theta)
    )


if __name__ == "__main__":
    main()
