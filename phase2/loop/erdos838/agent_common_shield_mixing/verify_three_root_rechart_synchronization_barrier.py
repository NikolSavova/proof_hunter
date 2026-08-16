#!/usr/bin/env python3
"""Exact checks for THREE_ROOT_RECHART_SYNCHRONIZATION_BARRIER."""

from fractions import Fraction
from itertools import combinations, product

from verify_critical_edge_dispersion_rechart_ledger import (
    configuration,
    convex,
    general_position,
    insertion_edge,
    orient,
    root_to_infinity,
)


def chart_compatibility_audit():
    left, right, ys, ws, lowers, roots = configuration()
    assert general_position(roots)
    assert orient(roots[0], roots[1], roots[2]) != 0

    # The audited root charts use the horizontal separating line through
    # each root. Their exact projective line coordinates (0,1,-h) differ.
    chart_lines = [(Fraction(0), Fraction(1), -root[1]) for root in roots]
    assert len(set(chart_lines)) == 3

    # No alternative line can contain all roots, so no projective map can
    # send all three roots to its single line at infinity.
    determinant = orient(roots[0], roots[1], roots[2])
    assert determinant != 0

    # Each separate chart remains valid for all varying-edge carriers.
    for root in roots:
        signs = set()
        for y, w, lower in product(ys, ws, lowers):
            base = [left, y, w, right, lower]
            image = [root_to_infinity(point, root) for point in base]
            ordered = sorted(zip(image, base))
            assert frozenset((ordered[0][1], ordered[-1][1])) == frozenset(
                (y, w)
            )
            triple_signs = {
                1 if orient(*triple) > 0 else -1
                for triple in combinations(sorted(image), 3)
            }
            assert len(triple_signs) == 1
            signs.update(triple_signs)
        assert len(signs) == 1
    return determinant


def cage_and_shield_audit():
    left, right, ys, ws, lowers, roots = configuration()
    points = [left, right] + ys + ws + lowers + roots
    index = {point: i for i, point in enumerate(points)}
    y_indices = {index[point] for point in ys}
    w_indices = {index[point] for point in ws}
    root_indices = {index[point] for point in roots}

    carriers = []
    singleton_outputs = set()
    pair_failures = 0
    for y, w, lower in product(ys, ws, lowers):
        base = [left, y, w, right, lower]
        carriers.append(base)
        for root in roots:
            assert convex(base + [root])
            assert insertion_edge(base, root) == frozenset((y, w))
            output = frozenset(base + [root])
            assert output not in singleton_outputs
            singleton_outputs.add(output)
        for first, second in combinations(roots, 2):
            assert not convex(base + [first, second])
            pair_failures += 1
    assert len(carriers) == 27
    assert len(singleton_outputs) == 81
    assert pair_failures == 81

    # Exhaust the full face complex and verify the global two-shield cover:
    # every ordinary face with >=2 roots omits Y or omits W.
    ordinary = multi_root = 0
    routed_left = routed_right = 0
    for mask in range(1, 1 << len(points)):
        subset_indices = {i for i in range(len(points)) if mask >> i & 1}
        subset = [points[i] for i in subset_indices]
        if not convex(subset):
            continue
        ordinary += 1
        if len(subset_indices & root_indices) < 2:
            continue
        multi_root += 1
        omits_y = not (subset_indices & y_indices)
        omits_w = not (subset_indices & w_indices)
        assert omits_y or omits_w
        routed_left += omits_y
        routed_right += omits_w
    assert ordinary > 1000 and multi_root > 0
    return ordinary, multi_root, routed_left, routed_right


def weighted_history_audit():
    checked = 0
    for table in product(range(4), repeat=6):
        total = sum(table)
        incidences = sum(value > 0 for value in table)
        load = max(table)
        if total:
            assert incidences * load >= total
        else:
            assert incidences == 0
        checked += 1
    return checked


def main():
    determinant = chart_compatibility_audit()
    ordinary, multi, left, right = cage_and_shield_audit()
    tables = weighted_history_audit()
    print(
        "PASS: incompatible-root determinant=%s ordinary=%d "
        "multi-root=%d delete-Y=%d delete-W=%d history-tables=%d"
        % (determinant, ordinary, multi, left, right, tables)
    )


if __name__ == "__main__":
    main()
