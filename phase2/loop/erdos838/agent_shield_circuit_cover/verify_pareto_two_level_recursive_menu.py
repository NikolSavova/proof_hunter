#!/usr/bin/env python3
"""Exact global-menu and two-level strong-comb audit.

The default run does four things.

1. Exhausts the 512 rooted four-point wrapper words and all 180 genuine
   reset chambers of each word.
2. Computes the coordinatewise Pareto frontier of the resulting (C,U,W)
   states and minimizes the next three-child recurrence exactly.
3. Builds the minimizing 44-point parent by an exact rational strong comb
   and exhausts every projection chamber of that realization.
4. Optimizes one further scalar recurrence over the full 44-point profile
   menu.

``--gauges`` also checks a second metric gauge with the same strong-comb
order type and all eight choices obtained by reflecting child order types
while retaining the same three scalar assembly profiles.  It is slower.
Only Python's standard library and exact Fraction arithmetic are used.
"""

from __future__ import annotations

import argparse
import importlib.util
from bisect import bisect_right
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


menu = load("four_point_menu", "verify_two_direction_four_point_wrapper.py")
glue = load("strong_glue", "verify_recharted_all_loop_wrapper_gate.py")


TARGETS = (
    ((7, 0, 0), 43, (183, 1975, 1992)),
    ((0, 1, 7), 11, (342, 414, 1986)),
    ((7, 0, 0), 42, (1975, 183, 1992)),
)

TARGET_ORDERS = (
    (5, 6, 7, 8, 9, 10, 11, 12, 13, 4, 3, 2, 1, 0),
    (5, 6, 7, 8, 9, 1, 10, 2, 11, 3, 12, 4, 13, 0),
    (0, 1, 2, 3, 4, 13, 12, 11, 10, 9, 8, 7, 6, 5),
)


def pareto3(states):
    """Coordinatewise minima in O(N log N), with exact tie handling."""
    u_values = sorted({u for _, u, _ in states})
    u_index = {u: i + 1 for i, u in enumerate(u_values)}
    infinity = 10**100
    tree = [infinity] * (len(u_values) + 1)

    def query(index):
        answer = infinity
        while index:
            answer = min(answer, tree[index])
            index -= index & -index
        return answer

    def update(index, value):
        while index < len(tree):
            tree[index] = min(tree[index], value)
            index += index & -index

    frontier = []
    for state in sorted(states):
        c, u, w = state
        # A prior distinct state has c'<=c and u'<=u.  Equality in the
        # queried W already gives coordinatewise domination.
        if query(u_index[u]) > w:
            frontier.append(state)
        update(u_index[u], w)
    return frontier


def line_hull(states, slope_at, intercept_at):
    """Lower envelope of integer lines, returned with rational starts."""
    by_slope = {}
    for state in states:
        slope = slope_at(state)
        intercept = intercept_at(state)
        if slope not in by_slope or intercept < by_slope[slope][0]:
            by_slope[slope] = (intercept, state)
    lines = [(slope, row[0], row[1])
             for slope, row in sorted(by_slope.items(), reverse=True)]
    hull = []
    starts = []
    for slope, intercept, state in lines:
        while hull:
            old_slope, old_intercept, _ = hull[-1]
            crossing = Q(intercept - old_intercept, old_slope - slope)
            if crossing <= starts[-1]:
                hull.pop()
                starts.pop()
            else:
                break
        start = (Q(-10**100) if not hull else
                 Q(intercept - hull[-1][1], hull[-1][0] - slope))
        hull.append((slope, intercept, state))
        starts.append(start)
    return hull, starts


def query_hull(hull, starts, x):
    index = bisect_right(starts, x) - 1
    slope, intercept, state = hull[index]
    return slope * x + intercept, state


def wrapper_value(states, size):
    """Exact five-block recurrence with singleton endpoint blocks."""
    blocks = [(1, 1, 1, 1)]
    blocks.extend((size, c, u, w) for c, u, w in states)
    blocks.append((1, 1, 1, 1))
    total = sum(row[3] for row in blocks)
    for i in range(len(blocks)):
        middle = 1
        for j in range(i + 1, len(blocks)):
            total += blocks[i][1] * blocks[j][2] * middle
            middle *= 1 + blocks[j][0]
    return total


def best_variable_three(states):
    """O(p^2 log p) minimum for size-14 children with variable W."""
    hull, starts = line_hull(states, lambda z: z[1], lambda z: z[2] + z[0])
    best = None
    witness = None
    for first in states:
        c1, u1, w1 = first
        for second in states:
            c2, u2, w2 = second
            coefficient = 225 + 15 * c1 + c2
            third_value, third = query_hull(hull, starts, coefficient)
            value = (3377 + w1 + w2 + u1 + 15 * u2 + c1 * u2
                     + 225 * c1 + 15 * c2 + third_value)
            if best is None or value < best:
                best = value
                witness = (first, second, third)
    assert best == wrapper_value(witness, 14)
    return best, witness


def best_fixed_three(profiles, size, faces):
    """Exact next recurrence when every child has one fixed face count."""
    states = [(c, u, faces) for c, u in profiles]
    # General version of the same lower-envelope calculation, written in
    # block form to avoid relying on a size-14 expansion.
    a = 1 + size
    hull, starts = line_hull(states, lambda z: z[1], lambda z: z[2] + z[0])
    best = None
    witness = None
    for first in states:
        c1, u1, w1 = first
        for second in states:
            c2, u2, w2 = second
            coefficient = a * a + a * c1 + c2
            third_value, third = query_hull(hull, starts, coefficient)
            # This is the five-block recurrence after collecting the terms
            # involving the third state into the queried line.
            value = (2 + a**3 + w1 + w2 + u1 + a * u2 + c1 * u2
                     + a * a * c1 + a * c2 + third_value)
            if best is None or value < best:
                best = value
                witness = (first, second, third)
    assert best == wrapper_value(witness, size)
    return best, tuple((c, u) for c, u, _ in witness)


def chamber_seed(points, order):
    """Root convention: independent axis normalization, then positive shear."""
    critical = sorted({-(points[j][0] - points[i][0])
                       / (points[j][1] - points[i][1])
                       for i, j in combinations(range(len(points)), 2)
                       if points[j][1] != points[i][1]})
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)
    chosen = None
    sign = None
    for slope in probes:
        candidate = tuple(sorted(range(len(points)),
                                 key=lambda i: points[i][0] + slope * points[i][1]))
        if candidate == order:
            chosen, sign = slope, 1
            break
        if candidate[::-1] == order:
            chosen, sign = slope, -1
            break
    assert chosen is not None and sign is not None
    raw = [(sign * (x + chosen * y), sign * (-chosen * x + y))
           for x, y in points]
    f0, f1 = min(x for x, _ in raw), max(x for x, _ in raw)
    g0, g1 = min(y for _, y in raw), max(y for _, y in raw)
    raw = [((x - f0) / (f1 - f0), (y - g0) / (g1 - g0))
           for x, y in raw]
    raw = [raw[i] for i in order]
    return glue.make_positive_slopes(raw)


def build_child(word, chamber_index, expected, mirror=False):
    points, clusters = menu.configuration(word)
    signs = menu.all_signs(points)
    faces = menu.wrapper_faces([menu.local_profile(cluster) for cluster in clusters])
    points = menu.generic_perturb(points, signs)
    orders = menu.projection_orders(points)
    if not mirror:
        order = orders[chamber_index]
        seed = chamber_seed(points, order)
    else:
        # Reflect a reverse-profile chamber.  Reflection swaps C and U while
        # leaving W fixed, hence retains the requested scalar assembly state.
        reverse_index = {42: 43, 43: 42, 11: 10}[chamber_index]
        order = orders[reverse_index]
        seed = chamber_seed(points, order)
        seed = [(x, -y) for x, y in seed]
        seed = glue.make_positive_slopes(seed)
    profile = menu.chain_counts(menu.all_signs(seed), tuple(range(14)))
    assert (*profile, faces) == expected
    return seed


def build_parent(mirrors=(False, False, False)):
    blocks = [[(Q(0), Q(0))]]
    for mirror, (word, chamber_index, expected) in zip(mirrors, TARGETS):
        blocks.append(build_child(word, chamber_index, expected, mirror))
    blocks.append([(Q(0), Q(0))])
    parent = glue.comb_arc(blocks)
    assert len(parent) == 44
    return parent


def parent_spectrum(parent):
    signs = menu.all_signs(parent)
    orders = menu.projection_orders(parent)
    natural = tuple(sorted(range(44), key=lambda i: parent[i][0]))
    profiles = [menu.chain_counts(signs, order) for order in orders]
    assert menu.chain_counts(signs, natural) == (103311, 16109)
    return orders, profiles


def decimal_gauge_parent():
    """A second strong-comb gauge with the same child and cross signs."""
    blocks = [[(Q(0), Q(0))]]
    for word, chamber_index, expected in TARGETS:
        blocks.append(build_child(word, chamber_index, expected))
    blocks.append([(Q(0), Q(0))])

    def normalize(points):
        points = glue.make_positive_slopes(points)
        if len(points) == 1:
            return [(Q(0), Q(0))]
        x0, x1 = points[0][0], points[-1][0]
        y0, y1 = points[0][1], points[-1][1]
        return [((x - x0) / (x1 - x0), (y - y0) / (y1 - y0))
                for x, y in points]

    def decimal_glue(left, right):
        left, right = normalize(left), normalize(right)
        epsilon = Q(1, 10)
        while True:
            out = ([(epsilon * x, y) for x, y in left]
                   + [(1 + epsilon * x, 2 + y) for x, y in right])
            try:
                glue.check_top_split(out, len(left))
                return out
            except AssertionError:
                epsilon /= 10

    out = blocks[0]
    for block in blocks[1:]:
        out = decimal_glue(out, block)
    return out


def exhaust_menu():
    states = set()
    pairs = set()
    witnesses = {}
    for word in product(range(8), repeat=3):
        points, clusters = menu.configuration(word)
        signs = menu.all_signs(points)
        faces = menu.wrapper_faces([menu.local_profile(cluster)
                                    for cluster in clusters])
        points = menu.generic_perturb(points, signs)
        orders = menu.projection_orders(points)
        natural = tuple(sorted(range(14), key=lambda i: points[i][0]))
        for index, order in enumerate(orders):
            if order in (natural, natural[::-1]):
                continue
            c, u = menu.chain_counts(signs, order)
            state = (c, u, faces)
            states.add(state)
            pairs.add((c, u))
            if state in {row[2] for row in TARGETS}:
                witnesses.setdefault(state, []).append((word, index, order))
    return states, pairs, witnesses


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gauges", action="store_true",
                        help="also exhaust the slower gauge/reflection variants")
    args = parser.parse_args()

    states, pairs, witnesses = exhaust_menu()
    frontier = pareto3(states)
    assert len(pairs) == 20671
    assert len(states) == 42766
    assert len(frontier) == 575
    for target, expected_order in zip((row[2] for row in TARGETS), TARGET_ORDERS):
        assert witnesses[target] == [(next(row[0] for row in TARGETS
                                            if row[2] == target),
                                      next(row[1] for row in TARGETS
                                           if row[2] == target),
                                      expected_order)]

    best, chosen = best_variable_three(frontier)
    assert best == 747670
    assert chosen == tuple(row[2] for row in TARGETS)

    parent = build_parent()
    orders, profiles = parent_spectrum(parent)
    low = min(profiles, key=lambda row: row[0] * row[1])
    low_max = min(profiles, key=lambda row: max(row))
    assert len(orders) == 1884
    assert low == (18275, 49645)
    assert low[0] * low[1] == 907262375
    assert low_max == (39673, 39777)
    profile_set = set(profiles)
    pareto_profiles = [x for x in profile_set
                       if not any(y != x and y[0] <= x[0] and y[1] <= x[1]
                                  for y in profile_set)]
    assert len(pareto_profiles) == 202
    assert (15121, 102449) in pareto_profiles
    assert (102449, 15121) in pareto_profiles

    level_three, next_chosen = best_fixed_three(profile_set, 44, best)
    assert next_chosen == ((15121, 102449),
                           (44728, 21566),
                           (102449, 15121))
    assert level_three == 11358202734

    if args.gauges:
        decimal = decimal_gauge_parent()
        decimal_orders, decimal_profiles = parent_spectrum(decimal)
        decimal_low = min(decimal_profiles, key=lambda row: row[0] * row[1])
        assert len(decimal_orders) == 1884
        assert decimal_low == (18431, 49408)

        table = {}
        for mirrors in product((False, True), repeat=3):
            orders_m, profiles_m = parent_spectrum(build_parent(mirrors))
            low_m = min(profiles_m, key=lambda row: row[0] * row[1])
            max_m = min(profiles_m, key=lambda row: max(row))
            assert len(orders_m) == 1884
            table[mirrors] = (low_m, max_m)
        assert table[(True, False, True)][0] == (16699, 52138)
        assert table[(True, False, True)][1] == (37295, 37098)

    print("PASS: reset (C,U) pairs=20671, (C,U,W) states=42766, "
          "Pareto=575, W2=747670; 44-point chambers=1884, "
          "min CU=907262375, Pareto profiles=202, W3=11358202734"
          + ("; gauge/reflection variants checked" if args.gauges else ""))


if __name__ == "__main__":
    main()
