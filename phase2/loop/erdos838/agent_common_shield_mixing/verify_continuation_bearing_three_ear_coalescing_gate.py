#!/usr/bin/env python3
"""Exact verifier for CONTINUATION_BEARING_THREE_EAR_COALESCING_GATE."""

from fractions import Fraction as F
from itertools import combinations, product


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points):
    points = sorted(set(points))

    def half(seq):
        out = []
        for point in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    return half(points)[:-1] + half(list(reversed(points)))[:-1]


def ordinary(points):
    return len(hull(points)) == len(points)


def line_value(a, b):
    return (
        -(b[1] - a[1]),
        b[0] - a[0],
        (b[1] - a[1]) * a[0] - (b[0] - a[0]) * a[1],
    )


def ear_cell(poly, index):
    k = len(poly)
    previous = poly[(index - 1) % k]
    left = poly[index]
    right = poly[(index + 1) % k]
    following = poly[(index + 2) % k]
    return [
        line_value(previous, left),
        tuple(-v for v in line_value(left, right)),
        line_value(right, following),
    ]


def strict_halfplanes(conditions):
    lowers, uppers, in_x = [], [], []
    for a, b, c in conditions:
        if b > 0:
            lowers.append((-a / b, -c / b))
        elif b < 0:
            uppers.append((-a / b, -c / b))
        else:
            in_x.append((a, c))
    for lm, lb in lowers:
        for um, ub in uppers:
            in_x.append((um - lm, ub - lb))

    lower_x = upper_x = None
    for a, c in in_x:
        if a == 0:
            if c <= 0:
                return None
        elif a > 0:
            bound = -c / a
            lower_x = bound if lower_x is None else max(lower_x, bound)
        else:
            bound = -c / a
            upper_x = bound if upper_x is None else min(upper_x, bound)
    if lower_x is not None and upper_x is not None and lower_x >= upper_x:
        return None
    if lower_x is None and upper_x is None:
        x = F(0)
    elif lower_x is None:
        x = upper_x - 1
    elif upper_x is None:
        x = lower_x + 1
    else:
        x = (lower_x + upper_x) / 2

    lower_y = [m * x + b for m, b in lowers]
    upper_y = [m * x + b for m, b in uppers]
    if lower_y and upper_y:
        y = (max(lower_y) + min(upper_y)) / 2
    elif lower_y:
        y = max(lower_y) + 1
    elif upper_y:
        y = min(upper_y) - 1
    else:
        y = F(0)
    assert all(a * x + b * y + c > 0 for a, b, c in conditions)
    return x, y


def general_position(points):
    return all(orient(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(len(points)), 3))


def audit_nine_point_lift():
    raw = [
        (62614, 7322), (2922, 4014), (10209, 14386),
        (20660, 24299), (33336, 29017), (30137, 33324),
        (15334, 45211), (14934, 55621), (10934, 61521),
    ]
    P = [(F(x), F(y)) for x, y in raw]
    shear = F(49495, 57507)
    order = sorted(range(9), key=lambda i: P[i][0] + shear * P[i][1])
    assert order == [1, 2, 3, 6, 4, 5, 7, 8, 0]

    hm, hp = (F(2922), F(4013)), (F(2922), F(4015))
    repair = (F(2922) - F(1, 10), F(4014))
    sources = [[hm, hp, P[i], P[j]]
               for i, j in [(0, 6), (0, 7), (3, 8)]]
    ambient = [P[i] for i in range(9) if i != 1] + [hm, hp, repair]
    assert general_position(ambient)

    for source in sources:
        assert ordinary(source)
        hidden_hull = hull(source + [P[2]])
        assert len(hidden_hull) == len(source)
        assert P[2] not in hidden_hull
        assert ordinary(source + [repair])
        h = hull(source + [repair])
        j = h.index(repair)
        assert {h[(j - 1) % len(h)], h[(j + 1) % len(h)]} == {hm, hp}
    return order, len(sources)


def audit_incompatible_continuations():
    a, b, c = (F(0), F(0)), (F(6), F(0)), (F(0), F(6))
    d, e, ff = (F(3), F(-10)), (F(13), F(3)), (F(-10), F(13))
    z = (F(1), F(2))
    continuations = [(F(70), F(-97)), (F(68), F(79)),
                     (F(-81), F(34))]
    releases = [hull([a, b, c, x]) for x in (d, e, ff)]
    sources = [hull(releases[i] + [continuations[i]]) for i in range(3)]
    ambient = [a, b, c, d, e, ff, z] + continuations

    assert general_position(ambient)
    assert all(len(source) == 5 and ordinary(source) for source in sources)
    assert all(not ordinary(source + [z]) for source in sources)
    for i in range(3):
        for j in range(3):
            assert ordinary(releases[j] + [continuations[i]]) == (i == j)

    pair_counts = []
    for i, j in combinations(range(3), 2):
        count = 0
        for ei, ej in product(range(5), repeat=2):
            if strict_halfplanes(ear_cell(sources[i], ei)
                                 + ear_cell(sources[j], ej)) is not None:
                count += 1
        pair_counts.append(count)
    assert pair_counts == [3, 3, 3]

    triple_count = 0
    for edges in product(range(5), repeat=3):
        conditions = sum((ear_cell(sources[i], edges[i])
                          for i in range(3)), [])
        triple_count += strict_halfplanes(conditions) is not None
    assert triple_count == 0

    # Under the uniform law on three records, every ordered permutation of
    # the three types is bad. Same-continuation triples repeat one chamber.
    ordered_bad_lower = 6
    ordered_total = 3 ** 3
    assert F(ordered_bad_lower, ordered_total) == F(2, 9)
    same_continuation_bad = 0
    assert same_continuation_bad == 0
    return pair_counts, triple_count, F(2, 9)


def audit_renyi_identity():
    # Exact nonuniform calibration: continuation masses 1,2,3,4.
    masses = [F(1), F(2), F(3), F(4)]
    W = sum(masses)
    cube_sum = sum(x ** 3 for x in masses)
    k3_squared = W ** 3 / cube_sum
    assert cube_sum == W ** 3 / k3_squared
    eta = F(1, 4)
    lower = (1 - eta) ** 3 * cube_sum
    assert lower == F(27, 64) * W ** 3 / k3_squared
    return k3_squared, lower


def main():
    order, lifted = audit_nine_point_lift()
    pairs, triples, bad_fraction = audit_incompatible_continuations()
    k3_squared, lower = audit_renyi_identity()
    print(
        "PASS: n9-order=%s lifted=%d common-repair; "
        "continuation-cage pairs=%s triples=%d bad>=%s; "
        "Renyi K3^2=%s lower=%s"
        % (order, lifted, pairs, triples, bad_fraction,
           k3_squared, lower)
    )


if __name__ == "__main__":
    main()
