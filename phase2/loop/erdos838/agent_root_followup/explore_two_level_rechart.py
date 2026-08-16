#!/usr/bin/env python3
"""Exact two-level common-guard rechart exploration.

This is an exploratory certificate, not a theorem.  It builds the exact
14-point mutation-minimal common-guard wrapper, selects three projection
chambers minimizing the next scalar wrapper count, re-embeds the three
copies behind a fresh guard, and enumerates every projection chamber of the
resulting 44-point order type.  Convex-face counts at level two are obtained
from the proved exact block recurrence; cap/cup profiles use exact rational
chain DP.
"""

from fractions import Fraction as Q
from itertools import combinations

from verify_common_guard_all_direction import (
    chain_totals,
    configuration,
    orient,
    projection_orders,
)

# The exact strong-comb embedding is imported from the independent wrapper
# verifier.  Merely feeding a desired chart into the nonlinear tangent-pocket
# parametrization need not preserve that chart as the ambient x-chart.
import sys
from pathlib import Path

SHIELD_DIR = Path(__file__).resolve().parents[1] / "agent_shield_circuit_cover"
sys.path.insert(0, str(SHIELD_DIR))
from verify_recharted_all_loop_wrapper_gate import comb_arc  # noqa: E402


def rechart(points, order):
    """Orientation-preserving affine chart realizing ``order`` as x-order."""
    # Recover a rational projection functional that induces the order.
    critical = []
    for i, j in combinations(range(len(points)), 2):
        dx = points[j][0] - points[i][0]
        dy = points[j][1] - points[i][1]
        if dy:
            critical.append(-dx / dy)
    critical = sorted(set(critical))
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)
    chosen = None
    sign = 1
    for slope in probes:
        candidate = tuple(sorted(range(len(points)),
                                 key=lambda i: points[i][0] + slope * points[i][1]))
        if candidate == order:
            chosen = slope
            sign = 1
            break
        if tuple(reversed(candidate)) == order:
            chosen = slope
            sign = -1
            break
    assert chosen is not None

    raw = []
    for x, y in points:
        first = sign * (x + chosen * y)
        second = sign * (-chosen * x + y)
        raw.append((first, second))
    assert tuple(sorted(range(len(raw)), key=lambda i: raw[i][0])) == order

    # Independent positive coordinate rescaling preserves the order type.
    fmin = min(x for x, _ in raw)
    fmax = max(x for x, _ in raw)
    gmin = min(y for _, y in raw)
    gmax = max(y for _, y in raw)
    fspan = fmax - fmin
    gspan = gmax - gmin
    if not gspan:
        gspan = Q(1)
    return [((x - fmin) / fspan * 4, (y - gmin) / gspan * 4)
            for x, y in raw]


def wrapper_count(n, w, profiles):
    """Nonempty face count for singleton endpoints and three child blocks."""
    blocks = [(1, 1, 1, 1)]
    blocks.extend((n, c, u, w) for c, u in profiles)
    blocks.append((1, 1, 1, 1))
    total = sum(row[3] for row in blocks)
    for i in range(len(blocks)):
        middle = 1
        for j in range(i + 1, len(blocks)):
            total += blocks[i][1] * blocks[j][2] * middle
            middle *= 1 + blocks[j][0]
    return total


def best_three(profiles, n, w):
    """Dynamic programming for the exact three-child scalar minimum."""
    best = None
    best_rows = None
    for first in profiles:
        for second in profiles:
            # The third dependence is affine in C3 and U3, so scanning all
            # profiles is still only about five million exact integer rows.
            for third in profiles:
                value = wrapper_count(n, w, (first, second, third))
                if best is None or value < best:
                    best = value
                    best_rows = (first, second, third)
    return best, best_rows


def lower_line_hull(profiles):
    """Lower hull of lines U+C*x; return (C,U,profile) in slope order."""
    by_slope = {}
    for profile in profiles:
        c, u = profile
        if c not in by_slope or u < by_slope[c][0]:
            by_slope[c] = (u, profile)
    # Queries have positive x.  Descending slopes makes breakpoint queries
    # monotone from small to large x.
    lines = [(c, row[0], row[1])
             for c, row in sorted(by_slope.items(), reverse=True)]
    hull = []
    starts = []
    for c, u, profile in lines:
        start = None
        while hull:
            pc, pu, _ = hull[-1]
            # New line wins for x >= (u-pu)/(pc-c).
            cross = Q(u - pu, pc - c)
            if cross <= starts[-1]:
                hull.pop()
                starts.pop()
            else:
                start = cross
                break
        if not hull:
            start = Q(-10**100)
        hull.append((c, u, profile))
        starts.append(start)
    return hull, starts


def query_hull(hull, starts, x):
    lo, hi = 0, len(starts)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if starts[mid] <= x:
            lo = mid
        else:
            hi = mid
    c, u, profile = hull[lo]
    return u + c * x, profile


def best_three_fast(profiles, n, w):
    """O(p^2 log p) exact minimization of the three-child recurrence."""
    hull, starts = lower_line_hull(profiles)
    a = 1 + n
    constant = 3 * w + 2 + a ** 3
    best = None
    best_rows = None
    for second in profiles:
        c2, u2 = second
        for third in profiles:
            c3, u3 = third
            coefficient = u2 + a * u3 + a * a
            first_value, first = query_hull(hull, starts, coefficient)
            value = (constant + first_value + a * u2 + c2 * u3
                     + a * c2 + a * a * u3 + c3)
            if best is None or value < best:
                best = value
                best_rows = (first, second, third)
    assert best == wrapper_count(n, w, best_rows)
    return best, best_rows


def orientation_cube(points):
    n = len(points)
    signs = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i, j, k in combinations(range(n), 3):
        value = orient(points[i], points[j], points[k])
        assert value
        signs[i][j][k] = signs[j][k][i] = signs[k][i][j] = value
        signs[j][i][k] = signs[i][k][j] = signs[k][j][i] = -value
    return signs


def fast_chain_totals(order, signs):
    n = len(order)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cap[i][j] = cup[i][j] = 1
            oi, oj = order[i], order[j]
            for h in range(i):
                if signs[order[h]][oi][oj] < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def main():
    cap = [(Q(i), -Q(i * i)) for i in range(4)]
    interior = [(Q(0), Q(0)), (Q(1), Q(4)),
                (Q(2), Q(1)), (Q(4), Q(0))]
    cup = [(Q(i), Q(i * i)) for i in range(4)]
    points, _ = configuration([cap, interior, cup])
    orders = projection_orders(points)
    rows = [(chain_totals(points, order), order) for order in orders]
    profiles = [row[0] for row in rows]
    assert len(points) == 14 and len(rows) == 174

    predicted, chosen_profiles = best_three(profiles, 14, 1561)
    assert best_three_fast(list(set(profiles)), 14, 1561)[0] == predicted
    chosen_orders = []
    remaining = list(rows)
    for profile in chosen_profiles:
        index = next(i for i, row in enumerate(remaining) if row[0] == profile)
        chosen_orders.append(remaining[index][1])

    seeds = [rechart(points, order) for order in chosen_orders]
    singleton = [(Q(0), Q(0))]
    level_two = comb_arc([singleton] + seeds + [singleton])
    assert len(level_two) == 44
    level_two_orders = projection_orders(level_two)
    signs = orientation_cube(level_two)
    level_two_profiles = [fast_chain_totals(order, signs)
                          for order in level_two_orders]
    low = min(level_two_profiles, key=lambda row: row[0] * row[1])
    low_max = min(max(row) for row in level_two_profiles)
    print("level1 chosen profiles:", chosen_profiles)
    print("level2 n=44 predicted nonempty W=", predicted)
    print("level2 chambers=", len(level_two_orders))
    print("level2 min CU=", low, low[0] * low[1])
    print("level2 min max(C,U)=", low_max)
    level_three, chosen_level_two = best_three_fast(
        list(set(level_two_profiles)), 44, predicted)
    print("level2 chosen profiles for level3:", chosen_level_two)
    print("level3 n=134 predicted nonempty W=", level_three)


if __name__ == "__main__":
    main()
