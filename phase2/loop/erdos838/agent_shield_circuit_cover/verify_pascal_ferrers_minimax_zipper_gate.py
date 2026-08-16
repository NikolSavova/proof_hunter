#!/usr/bin/env python3
"""Exact checks for PASCAL_FERRERS_MINIMAX_ZIPPER_GATE.md.

The script has three independent parts.

1.  It exhausts the Young lattice of all reverse-internal shuffles of
    A=T(4,3), B=T(8,2), and solves the exact bottleneck-path problem.
2.  It constructs the exact Pascal minimum-endpoint distribution and
    checks the reverse-lex zipper tail statistic through depth 24.
3.  It evaluates the five top-block boundary profiles of the opposite
    density Pascal pair at large finite depths.  These rows are evidence
    only; the report does not extrapolate them.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import combinations
from math import comb, log, log2


@lru_cache(None)
def endpoint_matrix(d: int, k: int, kind: str) -> tuple[tuple[int, ...], ...]:
    """Natural cap/cup chains, indexed by (minimum, maximum) label."""
    assert kind in ("cap", "cup")
    if k == 0 or k == d:
        return ((1,),)

    left = endpoint_matrix(d - 1, k - 1, kind)
    right = endpoint_matrix(d - 1, k, kind)
    ell, rr = len(left), len(right)
    out = [[0] * (ell + rr) for _ in range(ell + rr)]
    for i in range(ell):
        out[i][:ell] = left[i]
    for i in range(rr):
        out[ell + i][ell:] = right[i]

    if kind == "cap":
        # A cap is a cap of R, or a cap of L with zero/one label of R.
        minimum_degree = [sum(row) for row in left]
        for i, value in enumerate(minimum_degree):
            for j in range(ell, ell + rr):
                out[i][j] += value
    else:
        # A cup is a cup of L, or a cup of R with zero/one label of L.
        maximum_degree = [
            sum(right[i][j] for i in range(rr)) for j in range(rr)
        ]
        for i in range(ell):
            for j, value in enumerate(maximum_degree, ell):
                out[i][j] += value
    return tuple(map(tuple, out))


def shuffle_cost(
    positions: tuple[int, ...],
    cap_a: tuple[tuple[int, ...], ...],
    cup_b: tuple[tuple[int, ...], ...],
    cup_a_count: int,
    cap_b_count: int,
) -> tuple[int, int, int]:
    """Exact (CU,C,U) from the reverse-internal interval transform."""
    a, b = len(cap_a), len(cup_b)
    occupied = set(positions)
    word: list[tuple[str, int]] = []
    ia, ib = a - 1, b - 1
    for place in range(a + b):
        if place in occupied:
            word.append(("A", ia))
            ia -= 1
        else:
            word.append(("B", ib))
            ib -= 1
    pos_a = {label: place for place, (kind, label) in enumerate(word)
             if kind == "A"}
    pos_b = {label: place for place, (kind, label) in enumerate(word)
             if kind == "B"}

    left_a = [sum(pos_a[i] < pos_b[j] for i in range(a))
              for j in range(b)]
    left_b = [sum(pos_b[j] < pos_a[i] for j in range(b))
              for i in range(a)]

    cap = cup_a_count
    for i in range(b):
        for j in range(i, b):
            cap += (cup_b[i][j] * (1 + left_a[j])
                    * (1 + a - left_a[i]))
    cup = cap_b_count
    for i in range(a):
        for j in range(i, a):
            cup += (cap_a[i][j] * (1 + left_b[j])
                    * (1 + b - left_b[i]))
    return cap * cup, cap, cup


def exact_young_minimax() -> tuple[float, float, int]:
    cap_a = endpoint_matrix(4, 3, "cap")
    cup_a = endpoint_matrix(4, 3, "cup")
    cap_b = endpoint_matrix(8, 2, "cap")
    cup_b = endpoint_matrix(8, 2, "cup")
    a, b = len(cap_a), len(cup_b)
    assert (a, b) == (4, 28)
    ca = sum(map(sum, cap_a))
    ua = sum(map(sum, cup_a))
    cb = sum(map(sum, cap_b))
    ub = sum(map(sum, cup_b))
    assert (ca, ua, cb, ub) == (15, 10, 1218, 59487)

    start = tuple(range(b, b + a))
    finish = tuple(range(a))
    states = list(combinations(range(a + b), a))
    states.sort(key=sum, reverse=True)
    costs = {state: shuffle_cost(state, cap_a, cup_b, ua, cb)
             for state in states}

    infinity = 10 ** 100
    bottleneck: dict[tuple[int, ...], int] = {start: costs[start][0]}
    predecessor: dict[tuple[int, ...], tuple[int, ...]] = {}
    for state in states:
        if state == start:
            continue
        occupied = set(state)
        best, parent = infinity, None
        for x in state:
            if x + 1 >= a + b or x + 1 in occupied:
                continue
            candidate = list(state)
            candidate[candidate.index(x)] = x + 1
            previous = tuple(sorted(candidate))
            if previous not in bottleneck:
                continue
            value = max(bottleneck[previous], costs[state][0])
            if value < best:
                best, parent = value, previous
        assert parent is not None
        bottleneck[state] = best
        predecessor[state] = parent

    endpoint_product = 297_445 * 1_653
    assert endpoint_product == 491_676_585
    assert bottleneck[finish] == endpoint_product
    low = min(costs.values())
    assert low == (235_588_500, 83_100, 2_835)

    # Reconstruct one legal path and independently check its length and load.
    path = [finish]
    while path[-1] != start:
        path.append(predecessor[path[-1]])
    path.reverse()
    assert len(path) == a * b + 1 == 113
    for old, new in zip(path, path[1:]):
        delta = [x - y for x, y in zip(old, new)]
        assert sorted(delta) == [0, 0, 0, 1]
    assert max(costs[state][0] for state in path) == endpoint_product

    faces = 1_125_297
    low_exponent = log(low[0] / faces, a + b)
    bottleneck_exponent = log(endpoint_product / faces, a + b)
    assert abs(low_exponent - 1.541963896876714) < 1e-12
    assert abs(bottleneck_exponent - 1.754252003754168) < 1e-12
    return low_exponent, bottleneck_exponent, len(states)


@lru_cache(None)
def cap_count_and_minimum_degree(d: int, k: int) -> tuple[int, tuple[int, ...]]:
    """Cap count and exact distribution of its minimum endpoint."""
    if k == 0 or k == d:
        return 1, (1,)
    c_left, degree_left = cap_count_and_minimum_degree(d - 1, k - 1)
    c_right, degree_right = cap_count_and_minimum_degree(d - 1, k)
    right_size = comb(d - 1, k)
    count = c_right + (1 + right_size) * c_left
    degree = tuple((1 + right_size) * x for x in degree_left) + degree_right
    assert sum(degree) == count
    return count, degree


def lower_convex_hull(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Lower convex hull of points with increasing integer x-coordinate."""
    hull: list[tuple[int, int]] = []
    for point in points:
        while len(hull) >= 2:
            x1, y1 = hull[-2]
            x2, y2 = hull[-1]
            x3, y3 = point
            if ((y2 - y1) * (x3 - x2)
                    >= (y3 - y2) * (x2 - x1)):
                hull.pop()
            else:
                break
        hull.append(point)
    return hull


def convex_tail_statistic(tails: list[int], count: int) -> tuple[int, float]:
    """Max x times the lower-convex envelope of tails/count."""
    hull = lower_convex_hull(list(enumerate(tails)))
    best_num, best_den, best_x = -1, 1, -1
    for (x1, y1), (x2, y2) in zip(hull, hull[1:]):
        dx, dy = x2 - x1, y2 - y1
        candidates = {x1, x2}
        if dy < 0:
            critical = (dy * x1 - y1 * dx) / (2 * dy)
            for x in range(int(critical) - 1, int(critical) + 3):
                if x1 <= x <= x2:
                    candidates.add(x)
        for x in candidates:
            interpolated_num = y1 * dx + dy * (x - x1)
            numerator, denominator = x * interpolated_num, dx * count
            if numerator * best_den > best_num * denominator:
                best_num, best_den, best_x = numerator, denominator, x
    return best_x, log2(best_num / best_den)


def convex_floor_statistic(tails: list[int], count: int,
                           multiplier: int) -> tuple[int, float]:
    """Min (1+x)(1+multiplier*lower-convex-tail(x))."""
    hull = lower_convex_hull(list(enumerate(tails)))
    best_value, best_x = float("inf"), -1
    for (x1, y1), (x2, y2) in zip(hull, hull[1:]):
        dx, dy = x2 - x1, y2 - y1
        candidates = {x1, x2}
        slope = dy / dx
        intercept = y1 - slope * x1
        if slope:
            # Derivative of (1+x)(1+M(intercept+slope*x)/count).
            critical = -(count / multiplier + intercept + slope) / (2 * slope)
            for x in range(int(critical) - 1, int(critical) + 3):
                if x1 <= x <= x2:
                    candidates.add(x)
        for x in candidates:
            y = y1 + dy * (x - x1) / dx
            value = (1 + x) * (1 + multiplier * y / count)
            if value < best_value:
                best_value, best_x = value, x
    return best_x, best_value


def zipper_tail_audit() -> list[tuple[int, int, float, int, float]]:
    expected = {
        8: (3, -0.04898737711220609),
        12: (10, 0.9427898199385184),
        16: (15, 2.096675495852173),
        20: (56, 3.401486362988956),
        24: (210, 4.745167723410088),
    }
    convex_expected = {
        8: (3, -0.04898737711220609),
        12: (7, 0.7969801753341951),
        16: (15, 1.8902952798683748),
        20: (49, 3.067780112526734),
        24: (176, 4.2993808325147365),
    }
    rows = []
    for d, (expected_cut, expected_log) in expected.items():
        count, degree = cap_count_and_minimum_degree(d, 3 * d // 4)
        tails = [0] * (len(degree) + 1)
        tail = 0
        best_numerator, best_cut = -1, None
        for cut in range(len(degree) - 1, -1, -1):
            tail += degree[cut]
            tails[cut] = tail
            numerator = cut * tail
            if numerator > best_numerator:
                best_numerator, best_cut = numerator, cut
        value = log2(best_numerator / count)
        assert best_cut == expected_cut
        assert abs(value - expected_log) < 1e-12
        convex_cut, convex_value = convex_tail_statistic(tails, count)
        want_cut, want_value = convex_expected[d]
        assert convex_cut == want_cut
        assert abs(convex_value - want_value) < 1e-12

        # Companion A=T(s,3s/4) contributes its right-role size as the
        # multiplier in the other middle rectangle.  At every audited
        # depth the exact convex-envelope floor is the completed endpoint.
        s = 4 * ((11 * d // 20) // 4)
        right_role = comb(s - 1, 3 * s // 4) if s else 1
        floor_cut, floor_value = convex_floor_statistic(
            tails, count, right_role)
        assert floor_cut == 0
        assert abs(floor_value - (1 + right_role)) < 1e-9
        rows.append((d, best_cut, value, convex_cut, convex_value))

    # The first label is the all-left Pascal path.  Its exact atom is D/C.
    for d in (8, 12, 16, 20, 24):
        count, degree = cap_count_and_minimum_degree(d, 3 * d // 4)
        dominant = 1
        k = 3 * d // 4
        for h in range(k):
            dominant *= 1 + comb(d - 1 - h, k - h)
        assert degree[0] == dominant
        assert max(degree) == dominant
        assert dominant <= count
    return rows


@lru_cache(None)
def pascal_cap(d: int, k: int) -> int:
    if k == 0 or k == d:
        return 1
    return (pascal_cap(d - 1, k)
            + (1 + comb(d - 1, k)) * pascal_cap(d - 1, k - 1))


def pascal_cup(d: int, k: int) -> int:
    return pascal_cap(d, d - k)


def block_gamma(d: int, k: int, kind: str,
                p_left: int, p_right: int,
                q_left: int, q_right: int) -> int:
    left_size = comb(d - 1, k - 1)
    right_size = comb(d - 1, k)
    if kind == "cap":
        left = pascal_cap(d - 1, k - 1)
        right = pascal_cap(d - 1, k)
        return (p_left * q_left * left + p_right * q_right * right
                + right_size * p_right * q_left * left)
    left = pascal_cup(d - 1, k - 1)
    right = pascal_cup(d - 1, k)
    return (p_left * q_left * left + p_right * q_right * right
            + left_size * p_right * q_left * right)


def macro_boundary_rows(t: int = 320) -> list[float]:
    s = 4 * ((11 * t // 20) // 4)
    ka, kb = 3 * s // 4, t // 4
    a, b = comb(s, ka), comb(t, kb)
    la, ra = comb(s - 1, ka - 1), comb(s - 1, ka)
    lb, rb = comb(t - 1, kb - 1), comb(t - 1, kb)
    stages = [
        ("BR", "BL", "AR", "AL"),
        ("BR", "AR", "BL", "AL"),
        ("AR", "BR", "BL", "AL"),
        ("AR", "BR", "AL", "BL"),
        ("AR", "AL", "BR", "BL"),
    ]
    ca, ua = pascal_cap(s, ka), pascal_cup(s, ka)
    cb, ub = pascal_cap(t, kb), pascal_cup(t, kb)
    out = []
    for stage in stages:
        place = {name: i for i, name in enumerate(stage)}
        l_bl = (ra if place["AR"] < place["BL"] else 0) + (
            la if place["AL"] < place["BL"] else 0)
        l_br = (ra if place["AR"] < place["BR"] else 0) + (
            la if place["AL"] < place["BR"] else 0)
        cap = ua + block_gamma(
            t, kb, "cup", 1 + l_bl, 1 + l_br,
            1 + a - l_bl, 1 + a - l_br)

        l_al = (rb if place["BR"] < place["AL"] else 0) + (
            lb if place["BL"] < place["AL"] else 0)
        l_ar = (rb if place["BR"] < place["AR"] else 0) + (
            lb if place["BL"] < place["AR"] else 0)
        cup = cb + block_gamma(
            s, ka, "cap", 1 + l_al, 1 + l_ar,
            1 + b - l_al, 1 + b - l_ar)
        out.append(log((cap * cup) / (ca * ub), a + b))
    expected = [
        1.5441390981876193,
        1.8858948898644496,
        1.542513592152695,
        1.990541437634818,
        1.5441390981876193,
    ]
    for got, want in zip(out, expected):
        assert abs(got - want) < 1e-12
    return out


def nested_half_boundary_rows() -> list[tuple[int, float]]:
    """Exact raw-tail lower point at the local-density-one-half node."""
    expected = {
        80: 0.30478506681478434,
        160: 0.330603918075777,
        320: 0.3444311942238661,
        640: 0.3518955904127721,
    }
    rows = []
    for d, want in expected.items():
        k, depth = 3 * d // 4, d // 2
        local_d, local_k = d - depth, k - depth
        assert 2 * local_k == local_d
        cut = comb(local_d - 1, local_k - 1)
        suffix = pascal_cap(local_d - 1, local_k)
        for h in range(depth - 1, -1, -1):
            node_d, node_k = d - h, k - h
            right_size = comb(node_d - 1, node_k)
            suffix = (pascal_cap(node_d - 1, node_k)
                      + (1 + right_size) * suffix)
        rate = log2(cut * suffix / pascal_cap(d, k)) / d
        assert abs(rate - want) < 1e-12
        rows.append((d, rate))
    return rows


def main() -> None:
    low, bottleneck, states = exact_young_minimax()
    tails = zipper_tail_audit()
    half = nested_half_boundary_rows()
    macro = macro_boundary_rows()
    h = -(0.25 * log2(0.25) + 0.75 * log2(0.75))
    combined = 1 + 11 / 20 + (11 / 20) / (4 * log(2) * h)
    assert abs(combined - 1.7945161063038442) < 1e-12
    assert combined > log2(3)
    print(
        "PASS: Pascal Ferrers minimax/zipper gate; "
        f"states={states}, pointwise/minimax exponents={low:.12f}/"
        f"{bottleneck:.12f}; convex-tail d24={tails[-1][4]:.12f}; "
        f"half-node d640 rate={half[-1][1]:.12f}; "
        f"two-rectangle exponent={combined:.12f}; "
        "macro d320=" + ",".join(f"{x:.9f}" for x in macro)
    )


if __name__ == "__main__":
    main()
