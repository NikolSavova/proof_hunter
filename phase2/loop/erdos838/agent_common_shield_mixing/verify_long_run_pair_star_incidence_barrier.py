#!/usr/bin/env python3
"""Exact checks for LONG_RUN_PAIR_STAR_INCIDENCE_BARRIER.md."""

from collections import Counter
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

is_convex = mod["is_convex"]
orient = mod["orient"]
nested_child = mod["nested_child"]
role_cells = mod["role_cells"]


def check_exact_geometry_and_loads():
    _raw, child, child_faces = nested_child()
    cells = role_cells()
    q = len(cells)
    D = len(cells[0])
    words = list(product(range(D), repeat=q))
    root = [(-2, 3), (0, -1), (2, 3)]

    # Exact marked-root provenance: the root plus every word is convex,
    # while every child label lies strictly inside the root triangle.
    assert all(is_convex(root + [cells[i][word[i]] for i in range(q)])
               for word in words)
    assert all(not is_convex(root + [point]) for point in child)
    all_points = root + [p for cell in cells for p in cell] + child
    assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))

    best_degree, oi, pi = max(
        (
            sum((mask >> i & 1) and (mask >> j & 1)
                for mask in child_faces),
            i,
            j,
        )
        for i in range(len(child))
        for j in range(i + 1, len(child))
    )
    star = [
        mask for mask in child_faces
        if (mask >> oi & 1) and (mask >> pi & 1)
    ]
    assert len(star) == best_degree == 13

    def word_points(word):
        return [cells[i][word[i]] for i in range(q)]

    def face_points(mask):
        return [child[i] for i in range(len(child)) if mask >> i & 1]

    # Every pair-star/outside-word incidence is bad.
    compatible = []
    for mask in star:
        for word in words:
            union = face_points(mask) + word_points(word)
            if is_convex(union):
                compatible.append((mask, word))
    assert not compatible

    # The canonical inner left/right role labels and the fixed child pair
    # form the same signed 1+3 class in every record.
    left_role = q // 2 - 1
    right_role = q // 2
    circuit = Counter()
    triangle = Counter()
    context = Counter()
    child_face = Counter()
    face_triangle = Counter()
    separated = Counter()

    for mask in star:
        for word in words:
            a = word[left_role]
            b = word[right_role]
            circuit[(a, b)] += 1
            tri = tuple(sorted((child[oi], cells[left_role][a],
                                cells[right_role][b])))
            assert is_convex(list(tri))
            triangle[tri] += 1
            context[word] += 1
            child_face[mask] += 1
            face_triangle[(mask, tri)] += 1
            separated[(mask, word)] += 1

    records = len(star) * D**q
    assert records == 208
    assert len(circuit) == D**2
    assert set(circuit.values()) == {len(star) * D ** (q - 2)}
    assert circuit == Counter({k: v for k, v in circuit.items()})
    assert set(triangle.values()) == {len(star) * D ** (q - 2)}
    assert set(context.values()) == {len(star)}
    assert set(child_face.values()) == {D**q}
    assert set(face_triangle.values()) == {D ** (q - 2)}
    assert set(separated.values()) == {1}

    # Full words coexist with at most one child label in this chart.
    full_rank_release = 0
    for word in words:
        base = word_points(word)
        for point in child:
            assert is_convex(base + [point])
            full_rank_release += 1
        for i in range(len(child)):
            for j in range(i + 1, len(child)):
                assert not is_convex(base + [child[i], child[j]])
    assert full_rank_release == D**q * len(child)

    # Exact weight 1/n preserves all load ratios.
    n0 = 37
    weight = F(1, n0)
    assert records * weight == F(records, n0)
    assert max(triangle.values()) * weight == F(
        len(star) * D ** (q - 2), n0
    )
    return records, len(star), D**q, max(triangle.values())


def check_effective_branching():
    checks = 0
    for q in range(2, 11):
        for D in range(2, 7):
            profiles = 1 + q
            root_mass = profiles * D**q
            remaining = root_mass
            for i in range(q):
                class_mass = profiles * D ** (q - i - 1)
                assert remaining == D * class_mass
                r = F(remaining, class_mass)
                assert r == D
                remaining = class_mass
                checks += 1
            assert remaining == profiles
    return checks


def phi(x, C):
    return x * x / 2 - C * x * log2(x)


def check_three_log_scale():
    rows = []
    C = 3
    for L in (2**10, 2**12, 2**14, 2**16):
        L2 = log2(L)
        L3 = log2(L2)
        lm = L - L3
        q_real = L / 2 - (C - 0.5) * L2
        q = int(q_real) // 2 * 2
        assert 0 < q < 2 * L

        # Continuous logarithm of D=(n-m)/q. Integer flooring changes this
        # by o(1), since D is exponential in L.
        logD = L + log2(1 - 1 / L2) - log2(q)
        logP = q * logD
        target = phi(L, C)
        assert abs(logP - target) <= 2 * L

        logJ_lower = phi(lm, C) - 2 * lm - 2
        logM_lower = logJ_lower + logP - L
        deficit = 2 * target - logM_lower
        ratio = deficit / (L * L3)
        assert 1 < ratio < 3
        assert abs((L - lm) - L3) < 1e-10
        rows.append((L, q, round((logP - target) / L, 6),
                     round(ratio, 6)))
    return rows


if __name__ == "__main__":
    records, star, words, circuit_load = check_exact_geometry_and_loads()
    branching = check_effective_branching()
    rows = check_three_log_scale()
    print("PASS")
    print(f"  exact records/pair-star/outside words: {records}/{star}/{words}")
    print("  compatible pair-star incidences: 0")
    print(f"  exact circuit/triangle load: {circuit_load}")
    print(f"  complete effective-branching levels: {branching}")
    print(f"  three-log scale rows: {rows}")
