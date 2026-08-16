#!/usr/bin/env python3
"""Exact checks for LONG_RUN_LEAST_COUNTEREXAMPLE_REAUDIT.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import log2
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
SHIELD = HERE.parent / "agent_shield_circuit_cover"
mod = runpy.run_path(
    str(SHIELD / "verify_central_nested_child_two_sided_product_barrier.py")
)

orient = mod["orient"]
is_convex = mod["is_convex"]
nested_child = mod["nested_child"]
old_role_cells = mod["role_cells"]


def pair_star(child_faces, m):
    degree, first, second = max(
        (
            sum((mask >> i & 1) and (mask >> j & 1)
                for mask in child_faces),
            i,
            j,
        )
        for i in range(m)
        for j in range(i + 1, m)
    )
    return first, second, [
        mask for mask in child_faces
        if (mask >> first & 1) and (mask >> second & 1)
    ], degree


def mask_points(mask, points):
    return [point for i, point in enumerate(points) if mask >> i & 1]


def check_old_one_sided_escape():
    _raw, child, child_faces = nested_child()
    cells = old_role_cells()
    oi, pi, star, degree = pair_star(child_faces, len(child))
    assert degree == len(star) == 13

    rows = []
    for role_indices in (range(0, 2), range(2, 4)):
        contexts = []
        for choice in product(*([[None] + cells[i] for i in role_indices])):
            points = [point for point in choice if point is not None]
            if points:
                contexts.append(points)
        compatible = sum(
            is_convex(mask_points(mask, child) + context)
            for mask in star
            for context in contexts
        )
        total = len(star) * len(contexts)
        degrees = {
            sum(is_convex(mask_points(mask, child) + context)
                for mask in star)
            for context in contexts
        }
        rows.append((compatible, total, degrees))

    assert rows == [(32, 104, {4}), (24, 104, {3})]

    words = list(product(*cells))
    assert all(
        is_convex(list(word) + [point])
        for word in words
        for point in child
    )
    return rows, len(words) * len(child)


def new_role_cells():
    centers = [F(-4, 5), F(-2, 5), F(2, 5), F(4, 5)]
    cells = []
    for cell_index, center in enumerate(centers):
        cell = []
        for value in range(2):
            x = center + F(value + 1, 100000) + F(cell_index * value, 10000000)
            cell.append((x, F(1) - x * x))
        cells.append(cell)
    return cells


def check_planar_persistent_carrier():
    _raw, child, child_faces = nested_child()
    cells = new_role_cells()
    u, v, w = (F(-1), F(0)), (F(1), F(0)), (F(0), F(-2))
    all_points = [u, v, w] + child + [p for cell in cells for p in cell]
    assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))

    options = [[None] + cell for cell in cells]
    states = [tuple(p for p in choice if p is not None)
              for choice in product(*options)]
    words = list(product(*cells))

    assert all(is_convex([u, v, w] + list(word)) for word in words)
    assert all(not is_convex([u, v, w, point]) for point in child)
    assert all(is_convex([u, v] + list(state)) for state in states)
    assert all(
        is_convex([u, v] + list(state) + [point])
        for state in states
        for point in child
    )
    assert all(
        not is_convex([u, v] + list(state) + [child[i], child[j]])
        for state in states
        for i, j in combinations(range(len(child)), 2)
    )

    oi, pi, star, degree = pair_star(child_faces, len(child))
    assert degree == len(star) == 13
    incidence = sum(
        is_convex([u, v] + list(state) + mask_points(mask, child))
        for state in states
        for mask in star
    )
    assert incidence == 0

    trace_count = len(child_faces) + (len(child) + 1) * len(states)
    assert len(child_faces) == 55
    assert len(states) == 3**4 == 81
    assert trace_count == 622
    return len(words), len(states), len(star), trace_count


def build_small_four_complex():
    n = 17
    u, v, w = 0, 1, 2
    groups = [set(range(3, 7)), set(range(7, 11))]
    child = set().union(*groups)
    roles = [set((11, 12)), set((13, 14)), set((15, 16))]
    outside = set().union(*roles)

    bad = set()
    for quad in combinations(range(n), 4):
        Q = set(quad)
        child_count = len(Q & child)
        outside_count = len(Q & outside)
        repeated_role = any(len(Q & role) >= 2 for role in roles)
        if repeated_role:
            bad.add(frozenset(Q))
        if any(len(Q & group) == 4 for group in groups):
            bad.add(frozenset(Q))
        if child_count >= 2 and outside_count >= 1:
            bad.add(frozenset(Q))
        if {u, v, w} <= Q and child_count == 1:
            bad.add(frozenset(Q))
        if {u, v} <= Q and child_count == 2:
            bad.add(frozenset(Q))

    def face(vertices):
        V = set(vertices)
        return not any(quad <= V for quad in bad)

    faces = [
        set(i for i in range(n) if mask >> i & 1)
        for mask in range(1 << n)
        if face(i for i in range(n) if mask >> i & 1)
    ]
    assert all(face(S - {x}) for S in faces for x in S)
    assert all(face(S) for S in combinations(range(n), 3))

    words = [set(word) for word in product(*[sorted(role) for role in roles])]
    assert all(face({u, v, w} | word) for word in words)
    assert all(face({u, v} | word | {y}) for word in words for y in child)
    assert all(not face({u, v, w, y}) for y in child)

    child_faces = [S for S in faces if S <= child]
    star = [S for S in child_faces if {3, 4} <= S]
    # At most three labels per group: (g-1) A^(t-1)=3*15.
    assert len(child_faces) == 15**2
    assert len(star) == 45
    incidence = sum(face({u, v} | word | S) for word in words for S in star)
    assert incidence == 0

    # Every prefix class has exact branching ratio two.
    for depth in range(len(roles)):
        prefixes = list(product(*[sorted(role) for role in roles[:depth]]))
        for prefix in prefixes:
            children = [prefix + (x,) for x in sorted(roles[depth])]
            assert len(children) == 2

    Q = 3 ** len(roles)
    crude_bound = 12 * n**3 + 8 * Q + 7 * len(child) * Q
    crude_bound += 6 * len(child_faces)
    assert len(faces) <= crude_bound
    return len(bad), len(faces), max(map(len, faces)), Q, incidence, crude_bound


def phi(L, C):
    return L * L / 2 - C * L * log2(L)


def check_asymptotic_global_bound():
    rows = []
    C = 3
    B0 = 20
    for L in (2**10, 2**12, 2**14, 2**16):
        L2 = log2(L)
        L3 = log2(L2)
        lm = L - L3
        target = phi(L, C)

        q_real = L / 2 - (C - 0.5) * L2 - B0
        q = int(q_real) // 2 * 2
        assert q > 0
        logD = L + log2(1 - 1 / L2) - log2(q)
        logQ = q * (logD + log2(1 + 2 ** (-logD)))
        assert logQ <= target - (B0 - 2) * L

        child_threshold = target - (L3 + B0 + 2) * L
        best = None
        # t groups, each of size g=m/t; each group contributes all subsets
        # of rank at most three.  Work in logarithms, since m is enormous.
        for t in range(1, int(L)):
            logg = lm - log2(t)
            correction = log2(1 + 5 * 2 ** (-2 * logg)
                              + 6 * 2 ** (-3 * logg))
            logA = 3 * logg - log2(6) + correction
            logH = t * logA
            if logH <= child_threshold:
                best = (t, logg, logA, logH)
            else:
                break
        assert best is not None
        t, logg, logA, logH = best
        assert 3 * t + 3 < 2 * L
        assert child_threshold - logH < logA + 1
        terms = [
            3 * L + 10,
            logQ + 3,
            lm + logQ + 3,
            logH + 3,
        ]
        assert max(terms) < target

        log_full_words = q * logD
        logJ = logg + (t - 1) * logA
        log_records = logJ + log_full_words - L
        deficit_ratio = (2 * target - log_records) / (L * L3)
        assert 1 < deficit_ratio < 20
        rows.append((L, q, t, round((logQ - target) / L, 5),
                     round(deficit_ratio, 5)))
    return rows


if __name__ == "__main__":
    old_rows, old_singletons = check_old_one_sided_escape()
    planar = check_planar_persistent_carrier()
    abstract = build_small_four_complex()
    asymptotic = check_asymptotic_global_bound()
    print("PASS")
    print(f"  old one-sided incidences: {old_rows}")
    print(f"  old full-word singleton bank: {old_singletons}")
    print(f"  persistent-carrier data: {planar}")
    print(f"  abstract bad/faces/Q/E/bound: {abstract}")
    print(f"  asymptotic rows: {asymptotic}")
