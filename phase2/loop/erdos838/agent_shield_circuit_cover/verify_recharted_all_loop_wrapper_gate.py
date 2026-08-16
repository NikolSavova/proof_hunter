#!/usr/bin/env python3
"""Exact audit of the recharted all-loop / two-cap-arc wrapper.

The certificate has four independent parts.

1. It checks the closed singleton formula for the two-cap-arc wrapper.
2. It checks the exact C,U,W recurrence on heterogeneous multi-point blocks.
3. It enumerates every projection chamber of the six-point Pascal cell
   T(4,2) and tests whether the chamber order admits an ordered strong-glue
   decomposition.
4. It takes one of the bad chambers, re-charts it by exact rational affine
   operations, and strongly glues the result to a new point.  Thus arbitrary
   chambers really can be used at the next wrapper level even though the old
   compatible decomposition has disappeared.

Only the Python standard library is used; all geometry is exact Fraction
arithmetic.
"""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import comb

Point = tuple[Q, Q]


def det(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def make_positive_slopes(points: list[Point]) -> list[Point]:
    """Shear vertically so x-order is unchanged and all pair slopes are >0."""
    points = sorted(points)
    if len(points) < 2:
        return points
    slopes = [(b[1] - a[1]) / (b[0] - a[0])
              for a, b in combinations(points, 2)]
    shift = max(Q(0), Q(1) - min(slopes))
    out = [(x, y + shift * x) for x, y in points]
    assert all(out[i][0] < out[i + 1][0]
               and out[i][1] < out[i + 1][1]
               for i in range(len(out) - 1))
    return out


def normalize(points: list[Point]) -> list[Point]:
    points = make_positive_slopes(points)
    if len(points) == 1:
        return [(Q(0), Q(0))]
    xmin, xmax = points[0][0], points[-1][0]
    ymin, ymax = points[0][1], points[-1][1]
    return [((x - xmin) / (xmax - xmin),
             (y - ymin) / (ymax - ymin)) for x, y in points]


def strong_glue(left: list[Point], right: list[Point]) -> list[Point]:
    """Explicit rational realization of A prec B."""
    left, right = normalize(left), normalize(right)
    slopes = []
    for block in (left, right):
        slopes.extend((b[1] - a[1]) / (b[0] - a[0])
                      for a, b in combinations(block, 2))
    if slopes:
        minimum = min(slopes)
        epsilon = min(Q(1, 4), minimum / (8 + 2 * minimum))
    else:
        epsilon = Q(1, 4)
    out = ([(epsilon * x, y) for x, y in left]
           + [(1 + epsilon * x, 2 + y) for x, y in right])
    assert all(out[i][0] < out[i + 1][0]
               and out[i][1] < out[i + 1][1]
               for i in range(len(out) - 1))
    check_top_split(out, len(left))
    return out


def check_top_split(points: list[Point], cut: int) -> None:
    n = len(points)
    for i, j in combinations(range(cut), 2):
        for k in range(cut, n):
            assert det(points[i], points[j], points[k]) < 0
    for i in range(cut):
        for j, k in combinations(range(cut, n), 2):
            assert det(points[i], points[j], points[k]) > 0


def orientation_table(points: list[Point]) -> list[list[list[int]]]:
    points = sorted(points)
    n = len(points)
    table = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i, j, k in combinations(range(n), 3):
        value = det(points[i], points[j], points[k])
        assert value
        table[i][j][k] = 1 if value > 0 else -1
    return table


def is_cap(indices: tuple[int, ...], orient: list[list[list[int]]]) -> bool:
    return all(orient[i][j][k] < 0 for i, j, k in combinations(indices, 3))


def is_cup(indices: tuple[int, ...], orient: list[list[list[int]]]) -> bool:
    return all(orient[i][j][k] > 0 for i, j, k in combinations(indices, 3))


def is_convex(indices: tuple[int, ...], orient: list[list[list[int]]]) -> bool:
    if len(indices) <= 3:
        return True
    lower: list[int] = []
    for p in indices:
        while len(lower) >= 2 and orient[lower[-2]][lower[-1]][p] < 0:
            lower.pop()
        lower.append(p)
    upper: list[int] = []
    for p in indices:
        while len(upper) >= 2 and orient[upper[-2]][upper[-1]][p] > 0:
            upper.pop()
        upper.append(p)
    return len(set(lower) | set(upper)) == len(indices)


def counts(points: list[Point]) -> tuple[int, int, int]:
    """Nonempty cap, cup, and convex-face counts in the current x-chart."""
    points = sorted(points)
    orient = orientation_table(points)
    cap = cup = face = 0
    for mask in range(1, 1 << len(points)):
        indices = tuple(i for i in range(len(points)) if mask >> i & 1)
        cap += is_cap(indices, orient)
        cup += is_cup(indices, orient)
        face += is_convex(indices, orient)
    return cap, cup, face


def comb_arc(blocks: list[list[Point]]) -> list[Point]:
    out = blocks[0]
    for block in blocks[1:]:
        out = strong_glue(out, block)
    return out


def singleton_wrapper(k: int, m: int) -> list[Point]:
    guards = comb_arc([[(Q(0), Q(0))] for _ in range(k)])
    locals_ = comb_arc([[(Q(0), Q(0))] for _ in range(m)])
    return strong_glue(guards, locals_)


@lru_cache(maxsize=None)
def pascal_cell(n: int, i: int) -> tuple[Point, ...]:
    if i == 0 or i == n:
        return ((Q(0), Q(0)),)
    return tuple(strong_glue(list(pascal_cell(n - 1, i - 1)),
                             list(pascal_cell(n - 1, i))))


def projection_chambers(points: list[Point]) -> list[tuple[Q, int, tuple[int, ...]]]:
    """All generic orders from f=x+s*y, plus their reversals.

    The sign is +1 for f and -1 for -f.  Multiplying both chart coordinates
    by the sign is orientation preserving.
    """
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
    out: list[tuple[Q, int, tuple[int, ...]]] = []
    seen = set()
    for slope in probes:
        order = tuple(sorted(range(len(points)),
                             key=lambda i: points[i][0] + slope * points[i][1]))
        for sign, candidate in ((1, order), (-1, order[::-1])):
            if candidate not in seen:
                seen.add(candidate)
                out.append((slope, sign, candidate))
    return out


def chamber_chain_counts(points: list[Point], order: tuple[int, ...]) -> tuple[int, int]:
    """Cap/cup totals by the last-two-points chain DP."""
    n = len(points)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cap[i][j] = cup[i][j] = 1
            for h in range(i):
                value = det(points[order[h]], points[order[i]], points[order[j]])
                if value < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def admits_ordered_strong_tree(points: list[Point], order: tuple[int, ...]) -> bool:
    """DP over interval splits for the exact ordered A prec B definition."""
    @lru_cache(maxsize=None)
    def solve(lo: int, hi: int) -> bool:
        if hi - lo <= 1:
            return True
        for cut in range(lo + 1, hi):
            good = True
            for i, j in combinations(range(lo, cut), 2):
                for k in range(cut, hi):
                    if det(points[order[i]], points[order[j]], points[order[k]]) >= 0:
                        good = False
            for i in range(lo, cut):
                for j, k in combinations(range(cut, hi), 2):
                    if det(points[order[i]], points[order[j]], points[order[k]]) <= 0:
                        good = False
            if good and solve(lo, cut) and solve(cut, hi):
                return True
        return False

    return solve(0, len(order))


def rechart(points: list[Point], slope: Q, sign: int,
            order: tuple[int, ...]) -> list[Point]:
    """Put a prescribed projection chamber into increasing x-order."""
    transformed = []
    for x, y in points:
        f = sign * (x + slope * y)
        g = sign * (-slope * x + y)
        transformed.append((f, g))
    actual = tuple(sorted(range(len(points)), key=lambda i: transformed[i][0]))
    assert actual == order
    return make_positive_slopes([transformed[i] for i in order])


def main() -> None:
    # Part 1: the exact singleton all-loop formula, including the empty set.
    k, m = 5, 6
    wrapper = singleton_wrapper(k, m)
    cap, cup, nonempty = counts(wrapper)
    predicted_with_empty = 2 ** m + (1 + m + comb(m, 2)) * (2 ** k - 1)
    assert nonempty + 1 == predicted_with_empty

    # Part 2: heterogeneous blocks.  The middle seeds include a four-point
    # one-interior order type, so this is not a singleton-mask check.
    seed_a = [(Q(0), Q(0)), (Q(1), Q(3)), (Q(2), Q(4))]
    seed_b = [(Q(0), Q(0)), (Q(1), Q(4)), (Q(2), Q(1)), (Q(4), Q(0))]
    seed_c = [(-x, y) for x, y in reversed(seed_b)]
    seed_d = [(Q(0), Q(0)), (Q(1), Q(2))]
    blocks = [make_positive_slopes(seed) for seed in (seed_a, seed_b, seed_c, seed_d)]
    profiles = [counts(block) for block in blocks]
    left = strong_glue(blocks[0], blocks[1])
    right = strong_glue(blocks[2], blocks[3])
    whole = strong_glue(left, right)
    c_left = profiles[1][0] + (len(blocks[1]) + 1) * profiles[0][0]
    u_left = profiles[0][1] + (len(blocks[0]) + 1) * profiles[1][1]
    w_left = profiles[0][2] + profiles[1][2] + profiles[0][0] * profiles[1][1]
    c_right = profiles[3][0] + (len(blocks[3]) + 1) * profiles[2][0]
    u_right = profiles[2][1] + (len(blocks[2]) + 1) * profiles[3][1]
    w_right = profiles[2][2] + profiles[3][2] + profiles[2][0] * profiles[3][1]
    assert counts(left) == (c_left, u_left, w_left)
    assert counts(right) == (c_right, u_right, w_right)
    predicted = (c_right + (len(right) + 1) * c_left,
                 u_left + (len(left) + 1) * u_right,
                 w_left + w_right + c_left * u_right)
    assert counts(whole) == predicted

    # Part 3: almost every projection chamber of an exact strong cell loses
    # every compatible ordered strong-decomposition tree.
    cell = list(pascal_cell(4, 2))
    chambers = projection_chambers(cell)
    compatible = [row for row in chambers
                  if admits_ordered_strong_tree(cell, row[2])]
    assert len(cell) == 6
    assert len(chambers) == 26
    assert len(compatible) == 2

    # Part 4: nevertheless one bad chamber can be put behind a fresh exact
    # strong seam.  The top recurrence uses its actual chamber profile.
    bad = next(row for row in chambers
               if not admits_ordered_strong_tree(cell, row[2]))
    slope, sign, order = bad
    bad_profile = chamber_chain_counts(cell, order)
    embedded = rechart(cell, slope, sign, order)
    assert not admits_ordered_strong_tree(embedded, tuple(range(len(embedded))))
    lifted = strong_glue(embedded, [(Q(0), Q(0))])
    assert not admits_ordered_strong_tree(lifted, tuple(range(len(lifted))))
    c0, u0, w0 = counts(embedded)
    assert (c0, u0) == bad_profile
    assert counts(lifted) == (1 + 2 * c0, u0 + (len(embedded) + 1),
                              w0 + 1 + c0)

    print("PASS: singleton wrapper n=%d V=%d C=%d U=%d; "
          "heterogeneous wrapper n=%d profile=%s; "
          "Pascal T(4,2) chambers=%d compatible=%d; "
          "bad chamber profile=%s and exact top re-glue verified"
          % (len(wrapper), nonempty + 1, cap, cup,
             len(whole), predicted, len(chambers), len(compatible), bad_profile))


if __name__ == "__main__":
    main()
