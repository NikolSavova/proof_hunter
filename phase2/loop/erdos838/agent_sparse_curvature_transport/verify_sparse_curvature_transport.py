#!/usr/bin/env python3
"""Exact checks for SPARSE_CURVATURE_TRANSPORT_AND_NATIVE_COLLISION.md."""

from __future__ import annotations

from collections import deque
from fractions import Fraction as Q
from functools import lru_cache
from math import factorial
from pathlib import Path
import importlib.util
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
F = (0, 1, 3, 7, 14, 26, 44, 72, 113, 168)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


hull = load_module(
    "sparse_transport_hull",
    ROOT / "agent_hull_root_envelope_dynamic" / "verify_hull_root_envelope.py",
)
reflection = load_module(
    "sparse_transport_reflection",
    ROOT / "reflection_trace.py",
)


def fraction_text(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


def ordinary_faces(points):
    answer = []
    for mask in range(1, 1 << len(points)):
        if mask.bit_count() <= 2 or len(hull.hull_ids(points, mask)) == mask.bit_count():
            answer.append(mask)
    return answer


class Dinic:
    def __init__(self, size):
        self.graph = [[] for _ in range(size)]

    def add(self, source, target, capacity):
        self.graph[source].append([target, capacity, len(self.graph[target])])
        self.graph[target].append([source, 0, len(self.graph[source]) - 1])

    def flow(self, source, sink):
        total = 0
        while True:
            level = [-1] * len(self.graph)
            level[source] = 0
            queue = deque([source])
            while queue:
                vertex = queue.popleft()
                for target, capacity, _ in self.graph[vertex]:
                    if capacity and level[target] < 0:
                        level[target] = level[vertex] + 1
                        queue.append(target)
            if level[sink] < 0:
                return total
            cursor = [0] * len(self.graph)

            def augment(vertex, amount):
                if vertex == sink:
                    return amount
                while cursor[vertex] < len(self.graph[vertex]):
                    edge = self.graph[vertex][cursor[vertex]]
                    target, capacity, reverse = edge
                    if capacity and level[target] == level[vertex] + 1:
                        pushed = augment(target, min(amount, capacity))
                        if pushed:
                            edge[1] -= pushed
                            self.graph[target][reverse][1] += pushed
                            return pushed
                    cursor[vertex] += 1
                return 0

            while True:
                pushed = augment(source, 10 ** 30)
                if not pushed:
                    break
                total += pushed


def native_minimax(faces, rows):
    """Minimum face load for the forced number of native top-cap tokens.

    A row is (root, shelling_mass, forced_native, available_face_masks).
    Shellings below one root are interchangeable at the top transition.  The
    root-to-face capacity enforces that a face occurs at most once per shelling.
    """
    total_mass = sum(weight * forced for _, weight, forced, _ in rows)
    if total_mass == 0:
        return 0
    face_index = {face: index for index, face in enumerate(faces)}

    def feasible(load):
        source = 0
        first_root = 1
        first_face = first_root + len(rows)
        sink = first_face + len(faces)
        network = Dinic(sink + 1)
        for index, (_, weight, forced, options) in enumerate(rows):
            root_node = first_root + index
            network.add(source, root_node, weight * forced)
            for face in options:
                network.add(root_node, first_face + face_index[face], weight)
        for index in range(len(faces)):
            network.add(first_face + index, sink, load)
        return network.flow(source, sink) == total_mass

    lower = (total_mass + len(faces) - 1) // len(faces)
    upper = total_mass
    while lower < upper:
        middle = (lower + upper) // 2
        if feasible(middle):
            upper = middle
        else:
            lower = middle + 1
    return lower


def audit_configuration(points, expected=None):
    size = len(points)
    assert size < len(F)
    full = (1 << size) - 1
    totals = hull.all_mask_face_totals(points)
    faces = ordinary_faces(points)
    face_set = set(faces)

    # Exact excess-potential transport on every deletion transition, not only
    # those reached by one chosen shelling.
    transition_count = 0
    for mask in range(1, 1 << size):
        rank = mask.bit_count()
        assert totals[mask] >= F[rank]
        if rank == 1:
            continue
        parent_excess = totals[mask] - F[rank]
        seam = F[rank] - F[rank - 1] - 1
        for root in hull.hull_ids(points, mask):
            child = mask ^ (1 << root)
            cap_cost = totals[mask] - totals[child] - 1
            child_excess = totals[child] - F[rank - 1]
            assert child_excess + cap_cost == seam + parent_excess
            transition_count += 1

    @lru_cache(None)
    def shellings(mask):
        if mask & (mask - 1) == 0:
            return 1
        return sum(
            shellings(mask ^ (1 << root))
            for root in hull.hull_ids(points, mask)
        )

    total_shellings = shellings(full)
    excess = totals[full] - F[size]
    seam = F[size] - F[size - 1] - 1
    roots = hull.hull_ids(points, full)
    root_rows = []
    flow_rows = []
    hull_face = sum(1 << root for root in roots)
    assert hull_face in face_set

    for root in roots:
        child = full ^ (1 << root)
        weight = shellings(child)
        child_v = totals[child]
        cap_cost = totals[full] - child_v - 1
        child_excess = child_v - F[size - 1]
        forced_native = max(0, seam - child_excess)
        assert forced_native == max(0, cap_cost - excess)
        options = [
            face for face in faces
            if face.bit_count() >= 2 and face >> root & 1
        ]
        assert len(options) == cap_cost
        assert hull_face in options
        flow_rows.append((root, weight, forced_native, options))
        lower = Q(weight * forced_native, total_shellings * cap_cost)
        root_rows.append({
            "root": root,
            "shelling_weight": weight,
            "child_V": child_v,
            "C": cap_cost,
            "D": child_excess,
            "forced_native": forced_native,
            "single_root_average_lower": fraction_text(lower),
        })

    assert sum(row[1] for row in flow_rows) == total_shellings
    native_mass = sum(weight * forced for _, weight, forced, _ in flow_rows)
    optimum = native_minimax(faces, flow_rows)
    core = F[size] - size
    assert core == sum(F[k + 1] - F[k] - 1 for k in range(1, size))
    assert core + excess == totals[full] - size

    result = {
        "n": size,
        "V": totals[full],
        "f_n": F[size],
        "excess": excess,
        "K_top": seam,
        "hull_size": len(roots),
        "shellings": total_shellings,
        "potential_transitions": transition_count,
        "full_ledger_per_shelling": totals[full] - size,
        "universal_core_per_shelling": core,
        "top_layer_per_shelling": seam,
        "top_density_in_full_ledger": fraction_text(Q(seam, totals[full] - size)),
        "forced_native_mass": native_mass,
        "native_menu_optimum": optimum,
        "native_menu_optimum_over_W": fraction_text(Q(optimum, total_shellings)),
        "full_native_hull_face_load": total_shellings,
        "root_rows": root_rows,
    }
    if expected is not None:
        assert result == expected
    return result


def convex_family_rows(expected=None):
    rows = []
    for size in (4, 5, 6, 8, 12, 20, 32):
        points = [(index, index * index) for index in range(size)]
        assert len(hull.hull_ids(points)) == size
        value = 2 ** size - 1
        cap_cost = 2 ** (size - 1) - 1
        shelling_count = factorial(size)
        # Relative to the convex family itself: every child is again convex,
        # E=0 and K=C.  The full set is a top-cap output for every root.
        rows.append({
            "n": size,
            "V": value,
            "W": shelling_count,
            "C_equals_K": cap_cost,
            "top_density": fraction_text(Q(cap_cost, value - size)),
            "forced_common_face_load_over_W": "1",
        })
    if expected is not None:
        assert rows == expected
    return rows


def build_certificate():
    n9 = [
        (62614, 7322), (2922, 4014), (10209, 14386),
        (20660, 24299), (33336, 29017), (30137, 33324),
        (15334, 45211), (14934, 55621), (10934, 61521),
    ]
    pascal6 = sorted(reflection.pascal_cell(4, 2, Q(1, 97)))
    convex8 = [(index, index * index) for index in range(8)]
    pascal3 = sorted(reflection.pascal_cell(3, 1, Q(1, 97)))
    epsilon = Q(1, 16384)
    vertical9 = sorted(
        (x + epsilon * epsilon * u, y + epsilon * v)
        for x, y in pascal3 for u, v in pascal3
    )
    return {
        "n9_points": [list(point) for point in n9],
        "n9_minimizer": audit_configuration(n9),
        "pascal_T_4_2": audit_configuration(pascal6),
        "convex_8_global_baseline": audit_configuration(convex8),
        "vertical_T_3_1_square": audit_configuration(vertical9),
        "convex_family_rows": convex_family_rows(),
    }


def main():
    expected = json.loads(
        (HERE / "sparse_curvature_transport_certificate.json").read_text()
    )
    actual = build_certificate()
    assert actual == expected
    print(
        "PASS: exact excess-potential curvature transport and forced-native "
        "minimax congestion; "
        f"n9={actual['n9_minimizer']['native_menu_optimum']}/"
        f"{actual['n9_minimizer']['shellings']}; "
        f"pascal6={actual['pascal_T_4_2']['native_menu_optimum']}/"
        f"{actual['pascal_T_4_2']['shellings']}; "
        f"vertical9={actual['vertical_T_3_1_square']['native_menu_optimum']}/"
        f"{actual['vertical_T_3_1_square']['shellings']}"
    )


if __name__ == "__main__":
    main()
