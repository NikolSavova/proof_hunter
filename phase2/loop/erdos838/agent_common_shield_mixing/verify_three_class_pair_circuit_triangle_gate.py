#!/usr/bin/env python3
"""Exact checks for THREE_CLASS_PAIR_CIRCUIT_TRIANGLE_GATE.md."""

from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
old = runpy.run_path(str(HERE / "verify_long_run_least_counterexample_reaudit.py"))
orient = old["orient"]
is_convex = old["is_convex"]
convex_masks = old["mod"]["convex_masks"]
hull = old["mod"]["hull"]


CYCLE6 = [
    (F(138), F(679)),
    (F(505), F(820)),
    (F(269), F(337)),
    (F(293), F(733)),
    (F(528), F(847)),
    (F(378), F(590)),
]


RESET12 = [
    (F(-11000), F(-11)),
    (F(-8988), F(22)),
    (F(-9971), F(1975)),
    (F(-10004), F(505)),
    (F(-1006), F(9987)),
    (F(999), F(10011)),
    (F(-30), F(12020)),
    (F(0), F(10497)),
    (F(9005), F(-24)),
    (F(10983), F(-19)),
    (F(9980), F(2008)),
    (F(9984), F(500)),
]


def interior_index(points, indices):
    H = set(hull([points[i] for i in indices]))
    inside = [i for i in indices if points[i] not in H]
    assert len(inside) == 1
    return inside[0]


def check_six_point_cycle():
    assert all(orient(*triple) != 0 for triple in combinations(CYCLE6, 3))
    class_pairs = [(0, 1), (2, 3), (4, 5)]
    interiors = []
    pair_quads = []
    for i, j in combinations(range(3), 2):
        quad = class_pairs[i] + class_pairs[j]
        pair_quads.append(frozenset(quad))
        assert not is_convex([CYCLE6[k] for k in quad])
        interiors.append(interior_index(CYCLE6, quad) // 2)
    assert interiors == [1, 0, 2]

    convex_quads = [
        frozenset(Q) for Q in combinations(range(6), 4)
        if is_convex([CYCLE6[k] for k in Q])
    ]
    assert len(convex_quads) == 3
    assert not set(convex_quads) & set(pair_quads)
    assert all(len({k // 2 for k in Q}) == 3 for Q in convex_quads)

    # ES(4)=5 double count: every five-set contains a convex four-set,
    # and each convex four-set occurs in exactly two five-sets.
    incidence = 0
    for five in combinations(range(6), 5):
        count = sum(Q <= set(five) for Q in convex_quads)
        assert count >= 1
        incidence += count
    assert incidence == 2 * len(convex_quads) == 6
    return interiors, [tuple(sorted(Q)) for Q in convex_quads]


def check_seam_decoder():
    # Two disjoint copies of the exact six-point cycle.  Pair-node edges
    # are matchings, so a doubled pair in an output seam recovers both
    # incident circuit edges and hence the source triangle.
    outputs = {}
    for copy in range(2):
        offset = 6 * copy
        points = [(x + F(20000 * copy), y) for x, y in CYCLE6]
        quads = [
            Q for Q in combinations(range(6), 4)
            if is_convex([points[k] for k in Q])
        ]
        assert len(quads) == 3
        for Q in quads:
            global_Q = frozenset(offset + k for k in Q)
            doubled = [
                cls for cls in range(3)
                if sum((offset + 2 * cls + bit) in global_Q
                       for bit in (0, 1)) == 2
            ]
            assert len(doubled) == 1
            key = global_Q
            assert key not in outputs
            outputs[key] = copy
    assert len(outputs) == 6
    return len(outputs)


def check_planar_pair_reset():
    assert all(orient(*triple) != 0 for triple in combinations(RESET12, 3))
    classes = {
        0: ((0, 1), (10, 11)),
        1: ((2, 3), (4, 5)),
        2: ((6, 7), (8, 9)),
    }
    circuit_edges = [
        ((0, (0, 1)), (1, (2, 3))),
        ((1, (4, 5)), (2, (6, 7))),
        ((2, (8, 9)), (0, (10, 11))),
    ]
    for left, right in circuit_edges:
        quad = left[1] + right[1]
        assert not is_convex([RESET12[k] for k in quad])

    # Each class is already a rich Boolean four-set in this regression.
    for pair_nodes in classes.values():
        labels = pair_nodes[0] + pair_nodes[1]
        assert is_convex([RESET12[k] for k in labels])
        assert len(convex_masks([RESET12[k] for k in labels])) == 16

    # Pair nodes have degree one and the auxiliary graph is three disjoint
    # edges, hence contains no triangle despite a class-level directed cycle.
    adjacency = {}
    for left, right in circuit_edges:
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)
    assert set(map(len, adjacency.values())) == {1}
    triangles = 0
    vertices = list(adjacency)
    for a, b, c in combinations(vertices, 3):
        triangles += (b in adjacency[a] and c in adjacency[a]
                      and c in adjacency[b])
    assert triangles == 0
    return len(circuit_edges), triangles


def round_robin_factors(g):
    assert g % 2 == 0
    fixed = g - 1
    modulus = g - 1
    factors = []
    for r in range(modulus):
        pairs = [(fixed, r)]
        for k in range(1, g // 2):
            pairs.append(tuple(sorted(((r + k) % modulus,
                                       (r - k) % modulus))))
        factors.append(tuple(sorted(pairs)))
    return factors


def check_scalable_pair_reset():
    t, g = 8, 12
    factors = round_robin_factors(g)
    all_pairs = [pair for factor in factors for pair in factor]
    assert len(all_pairs) == len(set(all_pairs)) == g * (g - 1) // 2
    assert all(len({x for pair in factor for x in pair}) == g
               for factor in factors)

    # Give the t-1 neighbours of every class distinct one-factors.
    pair_owner = {}
    graph_edges = []
    for i, j in combinations(range(t), 2):
        neighbours_i = [x for x in range(t) if x != i]
        neighbours_j = [x for x in range(t) if x != j]
        fi = factors[neighbours_i.index(j)]
        fj = factors[neighbours_j.index(i)]
        for pi, pj in zip(fi, fj):
            vi, vj = (i, pi), (j, pj)
            assert vi not in pair_owner
            assert vj not in pair_owner
            pair_owner[vi] = j
            pair_owner[vj] = i
            graph_edges.append((vi, vj))

    adjacency = {}
    label_occurrences = {(i, x): 0 for i in range(t) for x in range(g)}
    for vi, vj in graph_edges:
        adjacency.setdefault(vi, set()).add(vj)
        adjacency.setdefault(vj, set()).add(vi)
        for cls, pair in (vi, vj):
            for x in pair:
                label_occurrences[cls, x] += 1
    assert set(map(len, adjacency.values())) == {1}
    assert set(label_occurrences.values()) == {t - 1}
    assert len(graph_edges) == (t * (t - 1) // 2) * (g // 2)
    return len(graph_edges), t - 1


def projectively_nest(points):
    scale = F(20000)
    eps = F(1, 10**8)
    image = []
    tangents = []
    ordered = sorted(points)
    for raw_x, raw_y in ordered:
        f, h = raw_x / scale, raw_y / scale
        left = F(2) + eps * f + eps * eps * h
        right = F(2) + eps * f - eps * eps * h
        tangents.append((left, right))
        image.append(((left - right) / (left + right),
                      -F(2) / (left + right)))
    assert all(tangents[i][0] < tangents[i + 1][0]
               and tangents[i][1] < tangents[i + 1][1]
               for i in range(len(tangents) - 1))
    return ordered, image


def check_common_uv_embedding():
    raw, child = projectively_nest(RESET12)
    assert convex_masks(raw) == convex_masks(child)
    u, v, x = (F(-1), F(0)), (F(1), F(0)), (F(1, 7), F(1))
    assert all(not is_convex([u, v, y, z])
               for y, z in combinations(child, 2))
    assert all(is_convex([u, v, x, y]) for y in child)
    all_points = [u, v, x] + child
    assert all(orient(*triple) != 0 for triple in combinations(all_points, 3))
    return len(child)


if __name__ == "__main__":
    cycle = check_six_point_cycle()
    decoded = check_seam_decoder()
    reset = check_planar_pair_reset()
    scalable = check_scalable_pair_reset()
    nested = check_common_uv_embedding()
    print("PASS")
    print(f"  six-point cycle interiors/seams: {cycle}")
    print(f"  decoded seams from two triangles: {decoded}")
    print(f"  planar reset edges/triangles: {reset}")
    print(f"  factorized reset edges/label load: {scalable}")
    print(f"  common-uv nested child size: {nested}")
