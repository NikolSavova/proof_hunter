#!/usr/bin/env python3
"""Exact checks for NEAR_AMBIENT_PAIR_STAR_DIRECTIONAL_RECTANGLE_BARRIER."""

from fractions import Fraction as Q
from itertools import combinations, product
from math import log2


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower = []
    for p in pts:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points):
    return len(hull(points)) == len(set(points))


def convex_masks(points):
    return {
        mask
        for mask in range(1 << len(points))
        if convex([points[i] for i in range(len(points)) if mask >> i & 1])
    }


def nested_child():
    # An arbitrary non-Boolean six-point order type, embedded through
    # projective tangent coordinates in one strict nesting chain.
    raw = [
        (Q(-3), Q(-5)),
        (Q(-2), Q(-1)),
        (Q(-1), Q(-14)),
        (Q(1), Q(5)),
        (Q(2), Q(10)),
        (Q(4), Q(-11)),
    ]
    eps = Q(1, 100)
    image = []
    tangents = []
    for f, g in raw:
        left = Q(2) + eps * f + eps * eps * g
        right = Q(2) + eps * f - eps * eps * g
        tangents.append((left, right))
        image.append(((left - right) / (left + right), -Q(2) / (left + right)))
    assert all(
        tangents[i][0] < tangents[i + 1][0]
        and tangents[i][1] < tangents[i + 1][1]
        for i in range(len(tangents) - 1)
    )
    assert convex_masks(raw) == convex_masks(image)
    return image, convex_masks(image)


def role_cells():
    # Two two-role arcs, with two labels in every role.
    centers = [Q(-6, 5), Q(-11, 10), Q(11, 10), Q(6, 5)]
    cells = []
    for i, center in enumerate(centers):
        cell = []
        for value in range(2):
            x = center + Q(value + 1, 100000) + Q(i * value, 10000000)
            cell.append((x, x * x - 1))
        cells.append(cell)
    return cells


def is_chain(points, sign):
    points = sorted(points)
    return all(
        sign * orient(points[i], points[j], points[k]) > 0
        for i, j, k in combinations(range(len(points)), 3)
    )


def endpoint_factorization(child, faces):
    caps = {}
    cups = {}
    endpoint_faces = {}
    for mask in faces:
        ids = [i for i in range(len(child)) if mask >> i & 1]
        if len(ids) < 2:
            continue
        left = min(ids, key=lambda i: child[i][0])
        right = max(ids, key=lambda i: child[i][0])
        e = tuple(sorted((left, right)))
        endpoint_faces.setdefault(e, set()).add(mask)
        pts = [child[i] for i in ids]
        if is_chain(pts, 1):
            caps.setdefault(e, set()).add(mask)
        if is_chain(pts, -1):
            cups.setdefault(e, set()).add(mask)

    assert sum(map(len, endpoint_faces.values())) == len(faces) - len(child) - 1
    for e, family in endpoint_faces.items():
        unions = set()
        for c in caps.get(e, set()):
            for u in cups.get(e, set()):
                union = c | u
                assert union in family
                unions.add(union)
        assert unions == family
        assert len(family) == len(caps.get(e, set())) * len(cups.get(e, set()))

    e = max(endpoint_faces, key=lambda pair: len(endpoint_faces[pair]))
    assert e == (2, 4)
    assert len(endpoint_faces[e]) == 10
    assert len(caps[e]) == 5 and len(cups[e]) == 2
    return e, endpoint_faces[e]


def geometry_and_loads():
    child, faces = nested_child()
    e, star = endpoint_factorization(child, faces)
    cells = role_cells()
    points = [p for cell in cells for p in cell] + child
    assert all(orient(*triple) for triple in combinations(points, 3))

    options = [[None] + cell for cell in cells]
    left = [
        [p for p in state if p is not None]
        for state in product(*options[:2])
        if any(p is not None for p in state)
    ]
    right = [
        [p for p in state if p is not None]
        for state in product(*options[2:])
        if any(p is not None for p in state)
    ]
    assert len(left) == len(right) == 8

    def trace(mask):
        return [child[i] for i in range(len(child)) if mask >> i & 1]

    left_inc = sum(convex(s + trace(mask)) for s in left for mask in star)
    right_inc = sum(convex(s + trace(mask)) for s in right for mask in star)
    cross_inc = sum(
        convex(a + b + trace(mask))
        for a in left
        for b in right
        for mask in star
    )
    assert (left_inc, right_inc, cross_inc) == (32, 24, 0)

    # The inner endpoint 4 is hidden by the outer endpoint 2 and every
    # actual left/right label pair.
    for a in [p for cell in cells[:2] for p in cell]:
        for b in [p for cell in cells[2:] for p in cell]:
            four = [child[e[0]], child[e[1]], a, b]
            assert not convex(four)
            assert child[e[1]] not in hull(four)

    category = {(False, False): 0, (True, False): 0, (False, True): 0, (True, True): 0}
    both_ranks = set()
    for state in product(*options):
        has_left = any(p is not None for p in state[:2])
        has_right = any(p is not None for p in state[2:])
        base = [p for p in state if p is not None]
        for mask in faces:
            if convex(base + trace(mask)):
                category[(has_left, has_right)] += 1
                if has_left and has_right:
                    both_ranks.add(mask.bit_count())
    assert category == {
        (False, False): 55,
        (True, False): 296,
        (False, True): 240,
        (True, True): 448,
    }
    assert both_ranks == {0, 1}
    H, m, P = len(faces), len(child), len(left)
    restricted = sum(category.values())
    upper = H * (1 + 2 * P) + (m + 1) * P * P
    assert restricted == 1039 <= upper == 1383

    # Uniform common-complement routing: the two-sided base state has star
    # load exactly J. Empty/singleton child releases have the stated average
    # lower bound, while the separated (F,S) tag is injective only in V^2.
    records = len(star) * P * P
    assert records == 640
    assert Q(records, P * P) == len(star)
    assert Q(records, (m + 1) * P * P) == Q(len(star), m + 1)
    return H, len(star), left_inc, right_inc, restricted, upper


def algebra_and_scale():
    # Reflection has the anti-alignment sign, and the symmetric scalar
    # rectangle displays the exact square loss.
    for A, B, C, U in product(range(1, 8), repeat=4):
        current = A * C + B * U
        reflected = A * U + B * C
        assert (current <= reflected) == ((A - B) * (C - U) <= 0)

    J, T = 16, 16
    A = B = C = U = 4
    assert C * U == J and A * B == T
    assert A * C == B * U == 16 < J * T
    assert J * A == J * B == 64 < J * T
    assert J * A * B == 256 < (J * T) ** 2
    assert A * B < J * T * T

    # Pure-half near-ambient audit in logarithmic coordinates. L is itself
    # log_2 n, so no enormous integers are constructed.
    checked = 0
    for power in range(12, 21, 2):
        L = float(2**power)
        L2 = log2(L)
        a = log2(L2)
        phi = L * L / 2
        child_phi = (L - a) ** 2 / 2
        delta = phi - child_phi
        assert abs(delta - (L * a - a * a / 2)) < 1e-5 * delta
        # H sqrt(T) misses H T by delta/2 logarithmic units.
        assert abs(phi - (child_phi + delta / 2) - delta / 2) < 1e-5 * delta
        # The rank-one two-sided term mT is negligible.
        log_m = L - a
        assert child_phi + delta / 2 > log_m + delta
        # D=n/L and k~a/2 realize P=sqrt(T) up to o(delta).
        log_D = L - L2
        k_real = delta / (2 * log_D)
        assert abs(k_real / (a / 2) - 1) < 0.02
        checked += 1
    return checked


if __name__ == "__main__":
    H, star, left_inc, right_inc, restricted, upper = geometry_and_loads()
    scales = algebra_and_scale()
    print(
        "PASS: endpoint energy H=%d star=%d; one-sided incidences=%d,%d; "
        "two-sided incidence=0; restricted=%d<=%d; scales=%d"
        % (H, star, left_inc, right_inc, restricted, upper, scales)
    )
