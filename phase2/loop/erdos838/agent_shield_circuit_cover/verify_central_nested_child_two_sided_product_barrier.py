#!/usr/bin/env python3
"""Exact checks for CENTRAL_NESTED_CHILD_TWO_SIDED_PRODUCT_BARRIER.md."""

from fractions import Fraction as F
from itertools import combinations, product


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lo = []
    for p in points:
        while len(lo) >= 2 and orient(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    up = []
    for p in reversed(points):
        while len(up) >= 2 and orient(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return lo[:-1] + up[:-1]


def is_convex(points):
    return len(hull(points)) == len(set(points))


def convex_masks(points):
    return {
        mask
        for mask in range(1 << len(points))
        if is_convex([points[i] for i in range(len(points)) if mask >> i & 1])
    }


def nested_child():
    # A non-Boolean arbitrary source order type.
    raw = [
        (F(-3), F(-5)),
        (F(-2), F(-1)),
        (F(-1), F(-14)),
        (F(1), F(5)),
        (F(2), F(10)),
        (F(4), F(-11)),
    ]
    assert all(orient(*triple) != 0 for triple in combinations(raw, 3))
    eps = F(1, 100)
    image = []
    tangent = []
    for f, g in raw:
        left = F(2) + eps * f + eps * eps * g
        right = F(2) + eps * f - eps * eps * g
        tangent.append((left, right))
        image.append(
            ((left - right) / (left + right), -F(2) / (left + right))
        )
    assert all(
        tangent[i][0] < tangent[i + 1][0]
        and tangent[i][1] < tangent[i + 1][1]
        for i in range(len(tangent) - 1)
    )
    assert convex_masks(raw) == convex_masks(image)
    return raw, image, convex_masks(image)


def role_cells():
    # Four macro roles on two short parabola arcs, two labels per role.
    centers = [F(-6, 5), F(-11, 10), F(11, 10), F(6, 5)]
    cells = []
    for cell_index, center in enumerate(centers):
        cell = []
        for value in range(2):
            x = center + F(value + 1, 100000) + F(cell_index * value, 10000000)
            cell.append((x, x * x - 1))
        cells.append(cell)
    return cells


def check_geometry():
    raw, child, child_faces = nested_child()
    cells = role_cells()
    all_points = [p for cell in cells for p in cell] + child
    assert len(all_points) == len(set(all_points))
    assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))

    words = list(product(*cells))
    assert len(words) == 2**4 == 16
    assert all(is_convex(word) for word in words)
    # Every partial transversal is ordinary.
    options = [[None] + cell for cell in cells]
    assert all(is_convex([p for p in state if p is not None]) for state in product(*options))

    left_labels = [p for cell in cells[:2] for p in cell]
    right_labels = [p for cell in cells[2:] for p in cell]
    for a in left_labels:
        for b in right_labels:
            for inner, outer in combinations(range(len(child)), 2):
                four = [a, b, child[inner], child[outer]]
                assert not is_convex(four)
                # Tangent coordinates increase with the index, so the
                # later point is geometrically inner.
                assert child[outer] not in hull(four)

    rank_vector = [
        sum(mask.bit_count() == rank for mask in child_faces)
        for rank in range(len(child) + 1)
    ]
    assert rank_vector == [1, 6, 15, 20, 11, 2, 0]
    H = len(child_faces)
    best_degree, first, second = max(
        (
            sum((mask >> i & 1) and (mask >> j & 1) for mask in child_faces),
            i,
            j,
        )
        for i, j in combinations(range(len(child)), 2)
    )
    assert (best_degree, first, second) == (13, 2, 5)
    assert best_degree * 15 >= H - len(child) - 1

    # Exhaust the complete one-label-per-role trace complex.
    category = {(False, False): 0, (True, False): 0, (False, True): 0, (True, True): 0}
    both_child_ranks = set()
    for state in product(*options):
        left = any(p is not None for p in state[:2])
        right = any(p is not None for p in state[2:])
        base = [p for p in state if p is not None]
        for mask in child_faces:
            trace = [child[i] for i in range(len(child)) if mask >> i & 1]
            if is_convex(base + trace):
                category[(left, right)] += 1
                if left and right:
                    both_child_ranks.add(mask.bit_count())
    assert category == {
        (False, False): 55,
        (True, False): 296,
        (False, True): 240,
        (True, True): 448,
    }
    assert both_child_ranks == {0, 1}
    actual = sum(category.values())
    D, k, s = 2, 2, len(child)
    P = (D + 1) ** k - 1
    upper = H * (1 + 2 * P) + (s + 1) * P * P
    assert actual == 1039 <= upper == 1383

    # Every full base plus every singleton child is an actual release face.
    assert all(is_convex(list(word) + [point]) for word in words for point in child)
    return H, best_degree, len(words), actual, upper


def check_loads(H, star):
    q, k, D, s = 4, 2, 2, 6
    M = D**q
    records = M * star
    circuit_states = D**2
    circuit_load = D ** (q - 2) * star
    assert records == circuit_states * circuit_load

    full_word_release_states = M * (s + 1)
    assert F(records, full_word_release_states) == F(star, s + 1)
    one_sided_states = star * (2 * (D + 1) ** k - 1)
    assert F(records, one_sided_states) == F(M, 2 * (D + 1) ** k - 1)

    # Asymptotic algebraic decoder checks.
    for k0 in range(2, 9):
        for D0 in (2, 3, 5, 11):
            M0 = D0 ** (2 * k0)
            side = 2 * (D0 + 1) ** k0 - 1
            assert F(M0, side) >= F(D0**k0, 2 * (1 + F(1, D0)) ** k0)
    return circuit_load


if __name__ == "__main__":
    H, star, words, actual, upper = check_geometry()
    circuit_load = check_loads(H, star)
    print(
        f"PASS: arbitrary child H={H} pair-star={star}, words={words}, "
        "all cross-rooted child pairs nested, "
        f"restricted faces={actual}<={upper}, circuit load={circuit_load}"
    )
