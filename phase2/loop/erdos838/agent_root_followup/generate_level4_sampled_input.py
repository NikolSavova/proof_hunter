#!/usr/bin/env python3
"""Emit robust combinatorial input for explore_level4_sampled_spectrum.cpp.

The 134-point coordinates are exact rationals, but their smallest
determinants are far below long-double resolution.  We therefore emit the
orientation table from the certified strong-comb block signs, and use exact
rational projection probes to certify every sampled order.
"""

import argparse
import pickle
from decimal import Decimal, getcontext
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path

from generate_level3_parent_coordinates import build_level3, cert


BLOCK_SIZES = (1, 44, 44, 44, 1)


def block_map():
    out = []
    for block, size in enumerate(BLOCK_SIZES):
        for local in range(size):
            out.append((block, local))
    return out


def strong_comb_sign(i, j, k, mapping, selected_orders, parent_signs):
    """Orientation for natural-order indices i<j<k."""
    bi, li = mapping[i]
    bj, lj = mapping[j]
    bk, lk = mapping[k]
    if bi == bj == bk:
        assert bi in (1, 2, 3)
        order = selected_orders[bi - 1]
        return cert.menu.ordered_sign(
            parent_signs, order[li], order[lj], order[lk]
        )
    if bi == bj:
        return -1
    if bj == bk:
        return 1
    return -1


def exact_sample_orders(points, samples):
    # Quantile selection is deliberately floating point.  Its only purpose
    # is to propose directions; every resulting order is recomputed and
    # certified using exact rationals below.
    fp = [(float(x), float(y)) for x, y in points]
    walls = set()
    for i, j in combinations(range(len(points)), 2):
        dx = fp[j][0] - fp[i][0]
        dy = fp[j][1] - fp[i][1]
        if dy:
            walls.add(-dx / dy)
    walls = sorted(w for w in walls if w == w and abs(w) < float("inf"))
    probes = [walls[0] - 1 - abs(walls[0])]
    for k in range(samples):
        i = (k + 1) * len(walls) // (samples + 1)
        i = max(1, min(i, len(walls) - 1))
        probes.append((walls[i - 1] + walls[i]) / 2)
    probes.append(walls[-1] + 1 + abs(walls[-1]))

    getcontext().prec = 180

    def dec(q):
        return Decimal(q.numerator) / Decimal(q.denominator)

    dp = [(dec(x), dec(y)) for x, y in points]

    def exact_increasing(i, j, slope):
        """Sign of projection(j)-projection(i), without Fraction gcd work."""
        xi, yi = points[i]
        xj, yj = points[j]
        dxn = xj.numerator * xi.denominator - xi.numerator * xj.denominator
        dxd = xj.denominator * xi.denominator
        dyn = yj.numerator * yi.denominator - yi.numerator * yj.denominator
        dyd = yj.denominator * yi.denominator
        numerator = (
            dxn * slope.denominator * dyd
            + slope.numerator * dyn * dxd
        )
        return numerator > 0

    orders = []
    for floating_slope in probes:
        slope = Q.from_float(floating_slope)
        ds = dec(slope)
        approximate = [x + ds * y for x, y in dp]
        order = tuple(sorted(range(len(points)), key=approximate.__getitem__))
        assert all(exact_increasing(i, j, slope)
                   for i, j in zip(order, order[1:]))
        if order not in orders:
            orders.append(order)
    return len(walls), orders


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=128)
    parser.add_argument("--cache", type=Path,
                        help="optional temporary pickle for the exact W3 parent")
    args = parser.parse_args()
    if args.cache and args.cache.exists():
        with args.cache.open("rb") as stream:
            parent, points, selected, selected_orders = pickle.load(stream)
    else:
        parent, points, selected, selected_orders = build_level3()
        if args.cache:
            with args.cache.open("wb") as stream:
                pickle.dump((parent, points, selected, selected_orders), stream)
    assert len(points) == 134
    parent_signs = cert.menu.all_signs(parent)
    mapping = block_map()

    print(len(points))
    for i, j, k in combinations(range(len(points)), 3):
        print(strong_comb_sign(i, j, k, mapping, selected_orders, parent_signs))
    wall_count, orders = exact_sample_orders(points, args.samples)
    print(len(orders))
    for order in orders:
        print(*order)
    print(
        f"# chambers={selected} pair_walls={wall_count} "
        f"sampled_halfturn_orders={len(orders)}",
        file=__import__("sys").stderr,
    )


if __name__ == "__main__":
    main()
