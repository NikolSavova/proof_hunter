#!/usr/bin/env python3
"""Exact checks for PLANAR_CROSS_CLASS_PRODUCT_AND_CAGE_ELIMINATION.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import log2
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
old = runpy.run_path(str(HERE / "verify_long_run_least_counterexample_reaudit.py"))
orient = old["orient"]
is_convex = old["is_convex"]
nested_child = old["nested_child"]
role_cells = old["new_role_cells"]


def local_complex(size, bad_quads):
    bad = {frozenset(Q) for Q in bad_quads}
    return {
        frozenset(i for i in range(size) if mask >> i & 1)
        for mask in range(1 << size)
        if not any(Q <= {i for i in range(size) if mask >> i & 1}
                   for Q in bad)
    }


def check_cross_class_product_identity():
    sizes = [5, 6, 4]
    offsets = [0, 5, 11]
    local_bad = [
        [(0, 1, 2, 3), (1, 2, 3, 4)],
        [(0, 1, 2, 3), (2, 3, 4, 5)],
        [(0, 1, 2, 3)],
    ]
    locals_ = [local_complex(s, bad) for s, bad in zip(sizes, local_bad)]
    lifted_bad = set()
    for off, bad in zip(offsets, local_bad):
        lifted_bad.update(frozenset(off + x for x in Q) for Q in bad)
    n = sum(sizes)
    global_faces = {
        frozenset(i for i in range(n) if mask >> i & 1)
        for mask in range(1 << n)
        if not any(Q <= {i for i in range(n) if mask >> i & 1}
                   for Q in lifted_bad)
    }
    unions = {
        frozenset().union(*(
            frozenset(off + x for x in face)
            for off, face in zip(offsets, choice)
        ))
        for choice in product(*locals_)
    }
    assert global_faces == unions
    assert len(global_faces) == len(unions)
    count_product = 1
    for family in locals_:
        count_product *= len(family)
    assert len(global_faces) == count_product
    return [len(family) for family in locals_], count_product


def phi(L, C):
    return L * L / 2 - C * L * log2(L)


def check_fixed_gap_product_scale():
    rows = []
    C = 3
    for L in (2**10, 2**12, 2**14, 2**16):
        L2 = log2(L)
        L3 = log2(L2)
        logg = L - L2 - L3
        local = logg * logg / 4 - logg / 2
        target = phi(L, C)
        assert 2 * local > target
        t = int(L / 6)
        assert t * local > 10 * target
        rows.append((L, round((2 * local - target) / (L * L2), 6),
                     round(t * local / target, 6)))
    return rows


def matching_number(vertices, edges):
    edges = list(map(frozenset, edges))
    best = 0

    def rec(index, used, count):
        nonlocal best
        if index == len(edges):
            best = max(best, count)
            return
        rec(index + 1, used, count)
        if not (edges[index] & used):
            rec(index + 1, used | edges[index], count + 1)

    rec(0, frozenset(), 0)
    return best


def cover_number(vertices, edges):
    edges = list(map(frozenset, edges))
    for size in range(len(vertices) + 1):
        for cover in combinations(vertices, size):
            cover = set(cover)
            if all(cover & edge for edge in edges):
                return size
    raise AssertionError


def check_cover_matching():
    vertices = tuple(range(9))
    systems = [
        [(0, 1, 2, 3), (3, 4, 5, 6), (0, 6, 7, 8)],
        list(combinations(range(6), 4)),
        [(0, 1, 2, 3), (4, 5, 6, 7)],
    ]
    rows = []
    for edges in systems:
        tau = cover_number(vertices, edges)
        nu = matching_number(vertices, edges)
        assert tau <= 4 * nu
        rows.append((tau, nu, len(edges)))
    return rows


def endpoint(points, u, v, x, y, z):
    left = is_convex([u, x, y, z])
    right = is_convex([v, x, y, z])
    assert left != right
    return 0 if left else 1


def check_five_point_elimination():
    u, v, z = (F(0), F(0)), (F(1), F(0)), (F(0), F(1))
    checked = 0
    for den in range(4, 9):
        for ai in range(1, den):
            for bi in range(1, den - ai):
                y = (F(ai, den), F(bi, den))
                assert not is_convex([u, v, y, z])
                for si in range(-2 * den, 3 * den):
                    for ti in range(-2 * den, 0):
                        x = (F(si, den), F(ti, den))
                        if not all(orient(*triple) != 0 for triple in
                                   combinations([u, v, z, y, x], 3)):
                            continue
                        if (is_convex([u, v, x, y])
                                and is_convex([u, v, x, z])):
                            endpoint(None, u, v, x, y, z)
                            checked += 1
    assert checked > 1000
    return checked


def check_two_outside_amplification():
    u, v, z = (F(0), F(0)), (F(1), F(0)), (F(0), F(1))
    checked = 0
    outside = [(F(s, 4), F(t, 4))
               for s in range(-6, 11) for t in range(-8, 0)]
    for y in ((F(1, 5), F(1, 5)), (F(2, 7), F(1, 7))):
        admissible = [
            x for x in outside
            if is_convex([u, v, x, y]) and is_convex([u, v, x, z])
        ]
        for x, xp in combinations(admissible, 2):
            if not all(orient(*triple) != 0 for triple in
                       combinations([u, v, z, y, x, xp], 3)):
                continue
            if not is_convex([u, v, x, xp]):
                continue
            ex = endpoint(None, u, v, x, y, z)
            ep = endpoint(None, u, v, xp, y, z)
            if ex == ep:
                assert is_convex([x, xp, y, z])
                checked += 1
    assert checked > 1000
    return checked


def check_exact_role_bank():
    _raw, child, _faces = nested_child()
    cells = role_cells()
    u, v = (F(-1), F(0)), (F(1), F(0))
    all_faces = set()
    pair_rows = []
    for yi, zi in combinations(range(len(child)), 2):
        y, z = child[yi], child[zi]
        colors = []
        for cell in cells:
            row = []
            for x in cell:
                row.append(endpoint(None, u, v, x, y, z))
            colors.append(row)
        counts = [
            [sum(color == side for color in row) for row in colors]
            for side in (0, 1)
        ]
        products = [
            _product(1 + value for value in count)
            for count in counts
        ]
        Q = _product(1 + len(cell) for cell in cells)
        assert products[0] * products[1] >= Q

        for side, anchor in ((0, u), (1, v)):
            options = [
                [None] + [
                    x for x, color in zip(cell, row) if color == side
                ]
                for cell, row in zip(cells, colors)
            ]
            produced = 0
            for choice in product(*options):
                trace = tuple(x for x in choice if x is not None)
                face = [anchor, y, z] + list(trace)
                assert is_convex(face)
                key = frozenset(face)
                assert key not in all_faces
                all_faces.add(key)
                produced += 1
            assert produced == products[side]
        pair_rows.append(tuple(products))

    assert set(pair_rows) == {(9, 9)}
    assert len(all_faces) == 15 * 18 == 270
    return len(pair_rows), len(all_faces), pair_rows[0]


def _product(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def check_opposite_side_is_needed():
    u, v = (F(0), F(0)), (F(1), F(0))
    z = (F(-1248, 1000), F(-3772, 1000))
    y = (F(-473, 1000), F(-1845, 1000))
    x = (F(2525, 1000), F(-2834, 1000))
    xp = (F(4874, 1000), F(-3046, 1000))
    points = [u, v, z, y, x, xp]
    assert all(orient(*triple) != 0 for triple in combinations(points, 3))
    assert not is_convex([u, v, y, z])
    assert all(is_convex([u, v, a, b])
               for a in (x, xp) for b in (y, z))
    assert is_convex([u, v, x, xp])
    assert endpoint(None, u, v, x, y, z) == 1
    assert endpoint(None, u, v, xp, y, z) == 1
    assert not is_convex([x, xp, y, z])
    return True


if __name__ == "__main__":
    identity = check_cross_class_product_identity()
    scales = check_fixed_gap_product_scale()
    covers = check_cover_matching()
    five = check_five_point_elimination()
    six = check_two_outside_amplification()
    bank = check_exact_role_bank()
    stress = check_opposite_side_is_needed()
    print("PASS")
    print(f"  cross-class local/product counts: {identity}")
    print(f"  fixed-gap scale rows: {scales}")
    print(f"  cover/matching rows: {covers}")
    print(f"  five/six point checks: {five}/{six}")
    print(f"  exact role bank pairs/faces/profile: {bank}")
    print(f"  opposite-side stress: {stress}")
