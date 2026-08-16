#!/usr/bin/env python3
"""Exact checks for POST_COLLISION_REMAPPING_MINIMAX.md."""

from __future__ import annotations

from collections import deque
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations
from math import factorial
from pathlib import Path
import importlib.util
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


hull = load_module(
    "post_collision_hull",
    ROOT / "agent_hull_root_envelope_dynamic" / "verify_hull_root_envelope.py",
)
reflection = load_module(
    "post_collision_reflection",
    ROOT / "reflection_trace.py",
)


def ordinary_faces(points):
    faces = []
    for mask in range(1, 1 << len(points)):
        ids = [i for i in range(len(points)) if mask >> i & 1]
        selected = [points[i] for i in ids]
        if len(ids) <= 2 or len(hull.hull_ids(selected)) == len(ids):
            faces.append(mask)
    return faces


def extreme_shellings(points):
    full = (1 << len(points)) - 1

    @lru_cache(None)
    def recurse(mask):
        if mask & (mask - 1) == 0:
            return ((mask.bit_length() - 1,),)
        return tuple(
            (root,) + tail
            for root in hull.hull_ids(points, mask)
            for tail in recurse(mask ^ (1 << root))
        )

    return recurse(full)


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


def minimum_menu_load(faces, menus):
    """Exact integral minimax assignment of aggregated menus to faces."""
    output = {face: i for i, face in enumerate(faces)}
    menu_count = len(menus)
    output_count = len(faces)
    total_mass = sum(menus.values())

    def feasible(load):
        source = 0
        first_menu = 1
        first_output = first_menu + menu_count
        sink = first_output + output_count
        network = Dinic(sink + 1)
        for index, (options, mass) in enumerate(menus.items()):
            menu_vertex = first_menu + index
            network.add(source, menu_vertex, mass)
            for face in options:
                network.add(menu_vertex, first_output + output[face], mass)
        for index in range(output_count):
            network.add(first_output + index, sink, load)
        return network.flow(source, sink) == total_mass

    lower = (total_mass + output_count - 1) // output_count
    upper = total_mass
    while lower < upper:
        middle = (lower + upper) // 2
        if feasible(middle):
            upper = middle
        else:
            lower = middle + 1
    return lower


def mutation_audit(points, expected):
    """One-next-transition add/replace/toggle menu, exhausted exactly."""
    size = len(points)
    faces = ordinary_faces(points)
    face_set = set(faces)
    nontrivial = [face for face in faces if face.bit_count() >= 2]
    shellings = extreme_shellings(points)
    menus = {}
    counts = {name: {} for name in ("canonical", "add", "replace", "toggle")}
    successes = {name: 0 for name in ("add", "replace", "toggle")}

    for shelling in shellings:
        position = [0] * size
        for index, label in enumerate(shelling):
            position[label] = index
        for face in nontrivial:
            root = min(
                (label for label in range(size) if face >> label & 1),
                key=position.__getitem__,
            )
            next_label = shelling[position[root] + 1]
            candidates = {
                "canonical": face,
                "add": face | (1 << next_label),
                "replace": (face & ~(1 << root)) | (1 << next_label),
                "toggle": face ^ (1 << next_label),
            }
            for name in ("add", "replace", "toggle"):
                if candidates[name] not in face_set:
                    candidates[name] = face
                successes[name] += candidates[name] != face
            options = tuple(sorted(set(candidates.values())))
            menus[options] = menus.get(options, 0) + 1
            for name, output in candidates.items():
                counts[name][output] = counts[name].get(output, 0) + 1

    shelling_count = len(shellings)
    domain = shelling_count * len(nontrivial)
    all_face_lower = (domain + len(faces) - 1) // len(faces)
    result = {
        "n": size,
        "V": len(faces),
        "nontrivial_faces": len(nontrivial),
        "shellings": shelling_count,
        "domain": domain,
        "all_face_lower": all_face_lower,
        "nontrivial_output_lower": shelling_count,
        "menu_types": len(menus),
        "menu_optimum": minimum_menu_load(faces, menus),
        "successes": successes,
        "map_maximum_load": {
            name: max(profile.values()) for name, profile in counts.items()
        },
        "map_image_size": {
            name: len(profile) for name, profile in counts.items()
        },
    }
    assert result == expected
    assert result["menu_optimum"] >= result["all_face_lower"]
    assert result["menu_optimum"] <= shelling_count
    return result


def convex_menu_audit(expected):
    rows = []
    for size in range(4, 9):
        faces = list(range(1, 1 << size))
        face_set = set(faces)
        nontrivial = [face for face in faces if face.bit_count() >= 2]
        menus = {}
        for shelling in permutations(range(size)):
            position = [0] * size
            for index, label in enumerate(shelling):
                position[label] = index
            for face in nontrivial:
                root = min(
                    (label for label in range(size) if face >> label & 1),
                    key=position.__getitem__,
                )
                next_label = shelling[position[root] + 1]
                options = {
                    face,
                    face | (1 << next_label),
                    (face & ~(1 << root)) | (1 << next_label),
                    face ^ (1 << next_label),
                }
                options.discard(0)
                assert options <= face_set
                key = tuple(sorted(options))
                menus[key] = menus.get(key, 0) + 1
        shellings = factorial(size)
        domain = shellings * len(nontrivial)
        lower = (domain + len(faces) - 1) // len(faces)
        optimum = minimum_menu_load(faces, menus)
        row = [
            size, len(faces), len(nontrivial), shellings, domain,
            len(menus), lower, optimum,
        ]
        rows.append(row)
    assert rows == expected
    return rows


def counting_barrier_audit():
    """The all-face lower bound tends to the full shelling weight."""
    rows = []
    for size in (8, 16, 32, 64, 128):
        # Every generic planar set has all subsets of ranks one, two, and
        # three as ordinary faces. This is enough to make n/V=O(n^-2).
        baseline = size + size * (size - 1) // 2
        baseline += size * (size - 1) * (size - 2) // 6
        retained_fraction = Q(baseline - size, baseline)
        assert 1 - retained_fraction <= Q(7, size * size)
        rows.append([size, str(retained_fraction)])
    return rows


def main():
    certificate = json.loads((HERE / "post_collision_remapping_certificate.json").read_text())
    n9 = [tuple(row) for row in certificate["n9_points"]]
    pascal = sorted(reflection.pascal_cell(4, 2, Q(1, 97)))

    n9_result = mutation_audit(n9, certificate["n9_minimizer"])
    pascal_result = mutation_audit(pascal, certificate["pascal_T_4_2"])
    convex = convex_menu_audit(certificate["convex_rows"])
    barrier = counting_barrier_audit()
    assert barrier == certificate["counting_barrier_rows"]

    # The previously audited vertical Pascal square has W=64560, V=273.
    vertical = certificate["vertical_T_3_1_square"]
    assert vertical["domain"] == vertical["shellings"] * (
        vertical["V"] - vertical["n"]
    )
    assert vertical["all_face_lower"] == (
        vertical["domain"] + vertical["V"] - 1
    ) // vertical["V"]
    vertical36 = certificate["vertical_T_4_2_square"]
    assert Q(vertical36["V"] - vertical36["n"], vertical36["V"]) == Q(
        vertical36["unavoidable_weight_fraction"]
    ) == Q(147121, 147133)

    print(
        "PASS: arbitrary-remapping minimax fibre barrier and exact "
        "one-next-label menu optima; "
        f"n9={n9_result['menu_optimum']}/{n9_result['shellings']}; "
        f"pascal6={pascal_result['menu_optimum']}/{pascal_result['shellings']}; "
        f"convex_n8={convex[-1][-1]}/{convex[-1][3]}; "
        f"vertical9_lower={vertical['all_face_lower']}/{vertical['shellings']}"
    )


if __name__ == "__main__":
    main()
