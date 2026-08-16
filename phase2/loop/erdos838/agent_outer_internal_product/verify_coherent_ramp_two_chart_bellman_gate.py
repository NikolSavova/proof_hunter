#!/usr/bin/env python3
"""Verifier for COHERENT_RAMP_TWO_CHART_BELLMAN_GATE."""

from fractions import Fraction as Q
from itertools import combinations
from math import log, prod


Point = tuple[Q, Q]


def det(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def is_cap(points, trace):
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(det(word[i], word[j], word[k]) < 0
               for i, j, k in combinations(range(len(word)), 3))


def is_cup(points, trace):
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(det(word[i], word[j], word[k]) > 0
               for i, j, k in combinations(range(len(word)), 3))


def is_cap_by_turns(points, trace):
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(det(word[i], word[i + 1], word[i + 2]) < 0
               for i in range(len(word) - 2))


def is_cup_by_turns(points, trace):
    word = sorted((points[i] for i in trace), key=lambda p: p[0])
    return all(det(word[i], word[i + 1], word[i + 2]) > 0
               for i in range(len(word) - 2))


def hull(points, trace):
    word = sorted((points[i], i) for i in trace)
    if len(word) <= 1:
        return [i for _, i in word]
    lower = []
    for point, index in word:
        while (len(lower) >= 2
               and det(lower[-2][0], lower[-1][0], point) <= 0):
            lower.pop()
        lower.append((point, index))
    upper = []
    for point, index in reversed(word):
        while (len(upper) >= 2
               and det(upper[-2][0], upper[-1][0], point) <= 0):
            upper.pop()
        upper.append((point, index))
    return [index for _, index in lower[:-1] + upper[:-1]]


def is_face(points, trace):
    return len(hull(points, trace)) == len(trace)


def profile(points):
    cap = cup = face = 0
    for mask in range(1, 1 << len(points)):
        trace = tuple(i for i in range(len(points)) if mask >> i & 1)
        cap += is_cap(points, trace)
        cup += is_cup(points, trace)
        face += is_face(points, trace)
    return cap, cup, face


def make_positive_slopes(points):
    points = sorted(points)
    if len(points) < 2:
        return points
    slopes = [(b[1] - a[1]) / (b[0] - a[0])
              for a, b in combinations(points, 2)]
    shift = max(Q(0), Q(1) - min(slopes))
    return [(x, y + shift * x) for x, y in points]


def normalize(points):
    points = make_positive_slopes(points)
    if len(points) == 1:
        return [(Q(0), Q(0))]
    xmin, xmax = points[0][0], points[-1][0]
    ymin, ymax = points[0][1], points[-1][1]
    return [((x - xmin) / (xmax - xmin),
             (y - ymin) / (ymax - ymin)) for x, y in points]


def binary_strong_glue(left, right):
    """Exact rational realization of the binary association A prec B."""
    left, right = normalize(left), normalize(right)
    slopes = []
    for block in (left, right):
        slopes.extend((b[1] - a[1]) / (b[0] - a[0])
                      for a, b in combinations(block, 2))
    epsilon = (min(Q(1, 4), min(slopes) / (8 + 2 * min(slopes)))
               if slopes else Q(1, 4))
    out = ([(epsilon * x, y) for x, y in left]
           + [(1 + epsilon * x, 2 + y) for x, y in right])
    cut = len(left)
    for i, j in combinations(range(cut), 2):
        for k in range(cut, len(out)):
            assert det(out[i], out[j], out[k]) < 0
    for i in range(cut):
        for j, k in combinations(range(cut, len(out)), 2):
            assert det(out[i], out[j], out[k]) > 0
    return out


def linear_glue(blocks, epsilon=Q(1, 10**6)):
    points = []
    roles = []
    # A common positive shear makes every internal chord much steeper than
    # a macro seam while preserving all local orientations.
    shear = Q(20)
    for role, block in enumerate(blocks):
        for x, y in block:
            points.append((Q(role) + epsilon * epsilon * x,
                           Q(role * role) + epsilon * (y + shear * x)))
            roles.append(role)
    assert [x for x, _ in points] == sorted(x for x, _ in points)
    for i, j, k in combinations(range(len(points)), 3):
        value = det(points[i], points[j], points[k])
        assert value
        word = roles[i], roles[j], roles[k]
        if word[0] < word[1] < word[2]:
            assert value > 0
        elif word[0] == word[1] < word[2]:
            assert value < 0
        elif word[0] < word[1] == word[2]:
            assert value > 0
        else:
            assert word[0] == word[1] == word[2]
    return points


def exact_linear_profiles():
    raw = [
        [(0, -4), (1, -3), (2, -3), (7, -2)],
        [(0, -4), (1, -3), (2, -4), (7, 4)],
        [(0, -4), (1, -4), (2, -3), (7, -3)],
    ]
    blocks = [[(Q(x), Q(y)) for x, y in block] for block in raw]
    local = [profile(block) for block in blocks]
    parent = linear_glue(blocks)
    for mask in range(1, 1 << len(parent)):
        trace = tuple(i for i in range(len(parent)) if mask >> i & 1)
        assert is_cap(parent, trace) == is_cap_by_turns(parent, trace)
        assert is_cup(parent, trace) == is_cup_by_turns(parent, trace)
    actual = profile(parent)
    sizes = [len(block) for block in blocks]
    expected_c = sum(row[0] for row in local)
    expected_u = sum(row[1] for row in local)
    expected_h = sum(row[2] for row in local)
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            expected_c += local[i][0] * sizes[j]
            term = local[i][0] * local[j][1]
            for middle in range(i + 1, j):
                term *= 1 + sizes[middle]
            expected_h += term
    expected_u = sum(
        local[j][1]
        * prod(1 + sizes[i] for i in range(j))
        for j in range(len(blocks))
    )
    assert actual == (expected_c, expected_u, expected_h)

    right = binary_strong_glue(
        blocks[0], binary_strong_glue(blocks[1], blocks[2])
    )
    left = binary_strong_glue(
        binary_strong_glue(blocks[0], blocks[1]), blocks[2]
    )
    right_actual = profile(right)
    left_actual = profile(left)
    D = 4
    A = D + 1
    right_expected = (
        sum(local[i][0] * (1 + (2 - i) * D) for i in range(3)),
        sum(local[i][1] * A**i for i in range(3)),
        expected_h,
    )
    left_expected = (
        sum(local[i][0] * A ** (2 - i) for i in range(3)),
        sum(local[i][1] * (1 + i * D) for i in range(3)),
        expected_h,
    )
    assert actual == right_actual == right_expected == (184, 376, 1124)
    assert left_actual == left_expected == (392, 184, 1124)
    assert (392, 376, 1124) not in (right_actual, left_actual)
    return right_actual, left_actual


def formal_ramp_checks():
    checked = 0
    for q in (2, 3, 4, 6, 8, 12):
        for D in (q * q, 2 * q * q, 4 * q * q):
            h = 4 * q
            for a in (0, q, 2 * q):
                caps = [D ** (a + i) for i in range(q)]
                cups = [D ** (h - a - i) for i in range(q)]
                H = D**h
                assert all(caps[i] * cups[i] == H for i in range(q))

                C = sum(caps[i] * (1 + (q - 1 - i) * D)
                        for i in range(q))
                U = sum(cups[i] * (1 + D) ** i for i in range(q))
                W = q * H
                for i, j in combinations(range(q), 2):
                    W += caps[i] * cups[j] * (1 + D) ** (j - i - 1)

                S = sum(Q(1, D**j) + Q(j * D, D**j)
                        for j in range(q))
                T = sum(Q((1 + D) ** j, D**j) for j in range(q))
                assert C == D ** (a + q - 1) * S
                assert U == D ** (h - a) * T
                assert C * U == D ** (h + q - 1) * S * T
                assert 2 <= S < 4
                assert q <= T < 2 * q
                assert q * H <= W <= 2 * q * H

                surplus = log(C * U / W, D)
                lower = q - 1
                upper = q - 1 + log(8, D)
                assert lower <= surplus <= upper

                C_left = sum(caps[i] * (1 + D) ** (q - 1 - i)
                             for i in range(q))
                U_left = sum(cups[i] * (1 + i * D) for i in range(q))
                assert C_left == D ** (a + q - 1) * T
                assert U_left == D ** (h - a) * S
                assert C_left * U_left == C * U
                checked += 1
    return checked


def sampled_404_calibration():
    W3 = 11358202734
    low = (2562123, 33305052)
    left = (1118689, 355504811)
    middle = (3842402, 27715665)
    right = (355504811, 1118689)
    W4 = 204331272672794

    assert low[0] * low[1] == 85331639745396
    surplus = log(Q(low[0] * low[1], W3), 134)
    assert abs(surplus - 1.8221013266320347) < 1e-14
    left_imbalance = log(Q(left[0], left[1]), 134)
    right_imbalance = log(Q(right[0], right[1]), 134)
    assert abs(left_imbalance + 1.1763106907418235) < 1e-14
    assert abs(right_imbalance - 1.1763106907418233) < 1e-14
    witness_surpluses = [log(Q(c * u, W3), 134)
                         for c, u in (left, middle, right)]
    targets = (2.136352302607002, 1.8673355868070163,
               2.136352302607002)
    assert all(abs(a - b) < 1e-14
               for a, b in zip(witness_surpluses, targets))
    coefficient = log(W4, 2) / log(404, 2) ** 2
    assert abs(coefficient - 0.6341378038955277) < 1e-15
    return surplus, right_imbalance - left_imbalance, coefficient


if __name__ == "__main__":
    parent_profiles = exact_linear_profiles()
    ramps = formal_ramp_checks()
    sampled = sampled_404_calibration()
    print(
        "PASS: exact right/left (C,U,H)=%s; ramps=%d; "
        "sampled reset surplus=%.12f width=%.12f W4 coefficient=%.12f"
        % (parent_profiles, ramps, sampled[0], sampled[1], sampled[2])
    )
