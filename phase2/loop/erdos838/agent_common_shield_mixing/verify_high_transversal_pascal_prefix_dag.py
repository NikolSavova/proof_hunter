#!/usr/bin/env python3
"""Exact verifier for HIGH_TRANSVERSAL_PASCAL_PREFIX_DAG_BARRIER.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import ceil, comb, log2
from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parent.parent
GEOMETRY = ROOT / "agent_geometry" / "audit_geometry.py"


def load_geometry():
    spec = importlib.util.spec_from_file_location("prefix_dag_geometry",
                                                  GEOMETRY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def subsets(indices: tuple[int, ...]):
    for r in range(1, len(indices) + 1):
        yield from combinations(indices, r)


def rational_geometry_and_trie_audit(g) -> dict[str, object]:
    # Exact top split T(6,3)=T(5,2) prec T(5,3).
    n, i = 6, 3
    points = g.cell(n, i)
    left_size = comb(n - 1, i - 1)
    left = tuple(range(left_size))
    right = tuple(range(left_size, len(points)))
    orient = g.orient_table(points)

    left_faces = [a for a in subsets(left) if g.is_convex(a, orient)]
    right_faces = [a for a in subsets(right) if g.is_convex(a, orient)]
    sources = [a for a in left_faces if not g.is_cap(a, orient)]
    pockets = [a for a in right_faces if not g.is_cup(a, orient)]

    source_buckets: dict[tuple[tuple[int, ...], int],
                         list[tuple[int, ...]]] = defaultdict(list)
    for d in sources:
        bad = [t for t in combinations(d, 3)
               if not g.is_cap(t, orient)]
        assert bad
        source_buckets[(min(bad), len(d))].append(d)
    source_key = max(source_buckets, key=lambda k: len(source_buckets[k]))
    root, source_rank = source_key
    source_fibre = source_buckets[source_key]

    pocket_counts = Counter(map(len, pockets))
    pocket_rank = max(pocket_counts, key=pocket_counts.get)
    pocket_layer = sorted(u for u in pockets if len(u) == pocket_rank)

    assert len(source_fibre) == 6 and source_rank == 5
    assert len(pocket_layer) == 140 and pocket_rank == 4

    # Every root-plus-right-label circuit is bad; retaining a branch label
    # with any source is impossible.
    circuit_checks = 0
    for d in source_fibre:
        assert set(root).issubset(d)
        for z in right:
            assert not g.is_convex(root + (z,), orient)
            assert not g.is_convex(d + (z,), orient)
            circuit_checks += 2

    # Build every node of the increasing-prefix trie.
    nodes: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for u in pocket_layer:
        for j in range(pocket_rank + 1):
            nodes[u[:j]].append(u)

    node_checks = 0
    edge_checks = 0
    for prefix, family in nodes.items():
        j = len(prefix)
        assert all(u[:j] == prefix for u in family)
        if j == pocket_rank:
            assert len(family) == 1
            continue

        classes: dict[int, list[tuple[int, ...]]] = defaultdict(list)
        for u in family:
            z = u[j]
            if prefix:
                assert z > prefix[-1]
            classes[z].append(u)
            # The literal singleton trace is a bad root circuit.
            assert not g.is_convex(root + (z,), orient)
            for d in source_fibre:
                remaining = u[j:]
                assert remaining
                assert not g.is_convex(d + remaining, orient)
            edge_checks += 1

        largest = max(map(len, classes.values()))
        dispersion = Fraction(len(family), largest)
        assert len(classes) >= dispersion

        # Within a fixed child branch, deleting z is injective because the
        # prefix and z are globally fixed.
        for z, child in classes.items():
            reduced = [u[j + 1:] for u in child]
            assert len(reduced) == len(set(reduced))
            assert nodes[prefix + (z,)] == child
        node_checks += 1

    # Follow the canonical largest-child branch and verify exact telescoping.
    family = pocket_layer
    prefix: tuple[int, ...] = ()
    dispersions: list[Fraction] = []
    supports: list[int] = []
    sizes = [len(family)]
    for j in range(pocket_rank):
        classes = defaultdict(list)
        for u in family:
            classes[u[j]].append(u)
        z, child = min(classes.items(), key=lambda item: (-len(item[1]),
                                                          item[0]))
        h = Fraction(len(family), len(child))
        assert len(classes) >= h
        dispersions.append(h)
        supports.append(len(classes))
        prefix += (z,)
        family = child
        sizes.append(len(family))

    assert len(family) == 1 and family[0] == prefix
    product_h = Fraction(1)
    for h in dispersions:
        product_h *= h
    assert product_h == len(pocket_layer)

    # Across all leaves, full deletion collapses U to empty.  For every fixed
    # D, all pocket-layer records therefore have the same terminal output D.
    terminal_collision_load = len(pocket_layer)
    assert len({tuple(d) for _u in pocket_layer
                for d in source_fibre}) == len(source_fibre)

    return {
        "source_fibre": len(source_fibre),
        "source_rank": source_rank,
        "pocket_layer": len(pocket_layer),
        "pocket_rank": pocket_rank,
        "records": len(source_fibre) * len(pocket_layer),
        "trie_nodes": len(nodes),
        "node_checks": node_checks,
        "edge_checks": edge_checks,
        "circuit_checks": circuit_checks,
        "max_path_sizes": sizes,
        "max_path_dispersions": [str(h) for h in dispersions],
        "max_path_supports": supports,
        "terminal_collision_load": terminal_collision_load,
    }


def add(a: list[int], b: list[int]) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return out


def shift_scale(a: list[int], scale: int) -> list[int]:
    return [0] + [scale * x for x in a]


def convolution(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                out[i + j] += x * y
    return out


def rank_refined_pascal_dp(g, nmax: int = 56) -> dict[str, object]:
    # Polynomials are indexed by face rank and count nonempty objects.
    caps: list[list[list[int]]] = []
    cups: list[list[list[int]]] = []
    faces: list[list[list[int]]] = []

    for n in range(nmax + 1):
        cap_row: list[list[int]] = []
        cup_row: list[list[int]] = []
        face_row: list[list[int]] = []
        for i in range(n + 1):
            if n == 0 or i == 0 or i == n:
                c = [0, 1]
                u = [0, 1]
                f = [0, 1]
            else:
                left_size = comb(n - 1, i - 1)
                right_size = comb(n - 1, i)
                c_left, c_right = caps[n - 1][i - 1], caps[n - 1][i]
                u_left, u_right = cups[n - 1][i - 1], cups[n - 1][i]
                f_left, f_right = faces[n - 1][i - 1], faces[n - 1][i]

                # A spanning cap has a nonempty cap in the left child and
                # zero or one arbitrary point in the right child.
                c = add(c_right, add(c_left,
                                     shift_scale(c_left, right_size)))
                # Reflected statement for cups.
                u = add(u_left, add(u_right,
                                    shift_scale(u_right, left_size)))
                # A spanning face is cap(left) union cup(right).
                f = add(add(f_left, f_right), convolution(c_left, u_right))
            cap_row.append(c)
            cup_row.append(u)
            face_row.append(f)
        caps.append(cap_row)
        cups.append(cup_row)
        faces.append(face_row)

    scalar_caps, scalar_cups = g.dp_counts(nmax)
    scalar_faces = g.dp_convex_counts(nmax, scalar_caps, scalar_cups)
    cell_checks = 0
    for n in range(nmax + 1):
        for i in range(n + 1):
            assert sum(caps[n][i]) == scalar_caps[n][i]
            assert sum(cups[n][i]) == scalar_cups[n][i]
            assert sum(faces[n][i]) == scalar_faces[n][i]
            cell_checks += 1

    central_checks = 0
    last_stats: dict[str, object] = {}
    for n in range(8, nmax + 1, 2):
        h = n // 2
        parent = scalar_faces[n][h]
        child_size = comb(n - 1, h - 1)

        source_by_rank = [
            (faces[n - 1][h - 1][r] if r < len(faces[n - 1][h - 1]) else 0)
            - (caps[n - 1][h - 1][r] if r < len(caps[n - 1][h - 1]) else 0)
            for r in range(n + 1)
        ]
        pocket_by_rank = [
            (faces[n - 1][h][r] if r < len(faces[n - 1][h]) else 0)
            - (cups[n - 1][h][r] if r < len(cups[n - 1][h]) else 0)
            for r in range(n + 1)
        ]
        assert all(x >= 0 for x in source_by_rank + pocket_by_rank)
        source_total = sum(source_by_rank)
        pocket_total = sum(pocket_by_rank)
        assert source_total == pocket_total > 0

        r = max(range(len(source_by_rank)), key=source_by_rank.__getitem__)
        s = max(range(len(pocket_by_rank)), key=pocket_by_rank.__getitem__)
        source_layer = source_by_rank[r]
        pocket_layer = pocket_by_rank[s]
        assert n * source_layer >= source_total
        assert n * pocket_layer >= pocket_total
        assert source_layer <= child_size ** r
        assert pocket_layer <= child_size ** s

        # Pigeonhole the canonical noncap triple inside the selected rank.
        triple_count = comb(child_size, 3)
        source_fibre_lower = source_layer // triple_count
        if source_fibre_lower:
            record_lower = source_fibre_lower * pocket_layer
            exponent = ceil(14 * n * log2(n + 2))
            assert parent * parent <= record_lower * (1 << exponent)

        # Each fixed-rank layer is itself live within the stated O(n log n)
        # envelope.
        exponent = ceil(7 * n * log2(n + 2))
        assert parent <= source_layer * (1 << exponent)
        assert parent <= pocket_layer * (1 << exponent)

        last_stats = {
            "n": n,
            "source_rank": r,
            "pocket_rank": s,
            "source_layer_bits": source_layer.bit_length(),
            "pocket_layer_bits": pocket_layer.bit_length(),
            "parent_bits": parent.bit_length(),
        }
        central_checks += 1

    return {
        "rank_refined_cells": cell_checks,
        "central_splits": central_checks,
        "nmax": nmax,
        "last": last_stats,
    }


def abstract_uniform_prefix_audit() -> int:
    families_checked = 0
    # Exhaust every nonempty uniform family on at most five labels.
    for n in range(1, 6):
        ground = tuple(range(n))
        for rank in range(1, n + 1):
            layer = list(combinations(ground, rank))
            for mask in range(1, 1 << len(layer)):
                family = [layer[j] for j in range(len(layer))
                          if (mask >> j) & 1]
                original_size = len(family)
                product_h = Fraction(1)
                for depth in range(rank):
                    classes: dict[int, list[tuple[int, ...]]] = defaultdict(list)
                    for u in family:
                        classes[u[depth]].append(u)
                    largest = max(map(len, classes.values()))
                    h = Fraction(len(family), largest)
                    assert len(classes) >= h
                    z, family = min(classes.items(),
                                    key=lambda item: (-len(item[1]), item[0]))
                    assert all(u[depth] == z for u in family)
                    product_h *= h
                assert len(family) == 1
                assert product_h == original_size
                families_checked += 1
    return families_checked


def main() -> None:
    g = load_geometry()
    geometry = rational_geometry_and_trie_audit(g)
    dp = rank_refined_pascal_dp(g)
    abstract = abstract_uniform_prefix_audit()
    print("PASS: high-transversal Pascal prefix-DAG barrier")
    print("geometry/trie:", geometry)
    print("rank-refined DP:", dp)
    print("abstract uniform families:", abstract)


if __name__ == "__main__":
    main()
