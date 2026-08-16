#!/usr/bin/env python3
"""Exact verifier for PROJECTED_SOURCE_CROSS_BRANCH_STORAGE_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, log2
from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parent.parent
GEOMETRY = ROOT / "agent_geometry" / "audit_geometry.py"


def load_geometry():
    spec = importlib.util.spec_from_file_location("cross_branch_geometry",
                                                  GEOMETRY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def subsets(indices: tuple[int, ...]):
    for r in range(1, len(indices) + 1):
        yield from combinations(indices, r)


def hull_profiles(d: tuple[int, ...], orient):
    lower: list[int] = []
    for k in d:
        while (len(lower) >= 2
               and orient[lower[-2]][lower[-1]][k] < 0):
            lower.pop()
        lower.append(k)
    upper: list[int] = []
    for k in d:
        while (len(upper) >= 2
               and orient[upper[-2]][upper[-1]][k] > 0):
            upper.pop()
        upper.append(k)
    return tuple(upper), tuple(lower)


def geometry_and_load_audit(g) -> dict[str, object]:
    points = g.cell(6, 3)
    left_size = comb(5, 2)
    left = tuple(range(left_size))
    right = tuple(range(left_size, len(points)))
    orient = g.orient_table(points)

    left_faces = [d for d in subsets(left) if g.is_convex(d, orient)]
    right_faces = [u for u in subsets(right) if g.is_convex(u, orient)]
    sources = [d for d in left_faces if not g.is_cap(d, orient)]
    pockets = [u for u in right_faces if not g.is_cup(u, orient)]
    pocket_rank_counts = Counter(map(len, pockets))
    pocket_rank = max(pocket_rank_counts, key=pocket_rank_counts.get)
    pocket_layer = sorted(u for u in pockets if len(u) == pocket_rank)

    assert len(sources) == 274
    assert len(pocket_layer) == 140 and pocket_rank == 4

    roots: dict[tuple[int, ...], tuple[int, ...]] = {}
    cap_of: dict[tuple[int, ...], tuple[int, ...]] = {}
    cup_of: dict[tuple[int, ...], tuple[int, ...]] = {}
    cap_fibres: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)

    for d in sources:
        bad_triples = [t for t in combinations(d, 3)
                       if not g.is_cap(t, orient)]
        assert bad_triples
        roots[d] = min(bad_triples)
        a, b = hull_profiles(d, orient)
        assert g.is_cap(a, orient)
        assert g.is_cup(b, orient)
        assert set(a).union(b) == set(d)
        cap_of[d], cup_of[d] = a, b
        cap_fibres[a].append(d)

    # Fixed-cap fibres give distinct cup profiles and recover their sources.
    for a, fibre in cap_fibres.items():
        cups = [cup_of[d] for d in fibre]
        assert len(cups) == len(set(cups))
        assert all(tuple(sorted(set(a).union(b))) == d
                   for d, b in zip(fibre, cups))

    # Full tags are bad; projected cap tags are good and expose the same
    # top-seam direction for every right label.
    full_bad_checks = projected_good_checks = 0
    ambient_projected_tags: set[tuple[int, ...]] = set()
    for d in sources:
        a = cap_of[d]
        for z in right:
            assert not g.is_convex(d + (z,), orient)
            assert not g.is_convex(roots[d] + (z,), orient)
            w = tuple(sorted(a + (z,)))
            assert g.is_convex(w, orient)
            ambient_projected_tags.add(w)
            full_bad_checks += 1
            projected_good_checks += 1

    # Every prefix sibling node: exact lambda_A m_z output loads.
    nodes: dict[tuple[int, ...], list[tuple[int, ...]]] = defaultdict(list)
    for u in pocket_layer:
        for j in range(pocket_rank):
            nodes[u[:j]].append(u)

    cross_level_outputs: set[tuple[int, ...]] = set()
    node_checks = record_load_checks = 0
    max_observed_load = 0
    for prefix, family in nodes.items():
        depth = len(prefix)
        sibling_classes: dict[int, list[tuple[int, ...]]] = defaultdict(list)
        for u in family:
            sibling_classes[u[depth]].append(u)

        lambda_a = Counter(cap_of.values())
        m_z = {z: len(us) for z, us in sibling_classes.items()}
        actual_loads: Counter[tuple[int, ...]] = Counter()
        output_key: dict[tuple[int, ...],
                         tuple[tuple[int, ...], int]] = {}

        for d in sources:
            a = cap_of[d]
            for u in family:
                z = u[depth]
                w = tuple(sorted(a + (z,)))
                actual_loads[w] += 1
                output_key[w] = (a, z)
                cross_level_outputs.add(w)
                record_load_checks += 1

        assert len(actual_loads) == len(lambda_a) * len(m_z)
        for w, load in actual_loads.items():
            a, z = output_key[w]
            assert load == lambda_a[a] * m_z[z]
            max_observed_load = max(max_observed_load, load)

        total_records = len(sources) * len(family)
        assert len(actual_loads) * max(actual_loads.values()) >= total_records
        node_checks += 1

    # Cross-level reuse is contained in the single ambient cap x singleton
    # bank; repeated levels cannot multiply it.
    assert cross_level_outputs.issubset(ambient_projected_tags)
    all_left_caps = [a for a in left_faces if g.is_cap(a, orient)]
    assert len(ambient_projected_tags) <= len(all_left_caps) * len(right)

    fibre_sizes = Counter(map(len, cap_fibres.values()))
    return {
        "sources": len(sources),
        "distinct_source_caps": len(cap_fibres),
        "largest_cap_fibre": max(map(len, cap_fibres.values())),
        "cap_fibre_histogram": dict(sorted(fibre_sizes.items())),
        "pocket_layer": len(pocket_layer),
        "prefix_nodes": len(nodes),
        "node_checks": node_checks,
        "record_load_checks": record_load_checks,
        "max_observed_tag_load": max_observed_load,
        "full_bad_checks": full_bad_checks,
        "projected_good_checks": projected_good_checks,
        "ambient_projected_tags": len(ambient_projected_tags),
        "cross_level_projected_tags": len(cross_level_outputs),
    }


def pascal_square_root_audit(g, nmax: int = 96) -> dict[str, object]:
    caps, cups = g.dp_counts(nmax)
    faces = g.dp_convex_counts(nmax, caps, cups)
    endpoint_checks = 0
    for n in range(nmax + 1):
        for i in range(n + 1):
            assert faces[n][i] <= caps[n][i] * cups[n][i]
            endpoint_checks += 1

    central_checks = 0
    last: dict[str, float | int] = {}
    for n in range(6, nmax + 1, 2):
        h = n // 2
        parent = faces[n][h]
        child = faces[n - 1][h - 1]
        cy = caps[n - 1][h - 1]
        uy = cups[n - 1][h - 1]
        right_size = comb(n - 1, h)
        tag_bank = cy * right_size

        assert child <= cy * uy
        assert tag_bank <= parent
        assert tag_bank * uy >= child * right_size
        assert parent == (faces[n - 1][h - 1] + faces[n - 1][h]
                          + caps[n - 1][h - 1] * cups[n - 1][h])
        central_checks += 1
        last = {
            "n": n,
            "tag_coefficient_over_n2": log2(tag_bank) / (n * n),
            "opposite_cup_coefficient_over_n2": log2(uy) / (n * n),
            "child_coefficient_over_n2": log2(child) / (n * n),
            "parent_coefficient_over_n2": log2(parent) / (n * n),
        }

    return {
        "endpoint_cells": endpoint_checks,
        "central_splits": central_checks,
        "nmax": nmax,
        "last": last,
    }


def exhaustive_load_tables() -> dict[str, int]:
    product_tables = 0
    for a in range(1, 4):
        for q in range(1, 4):
            for lambdas in product(range(1, 5), repeat=a):
                for ms in product(range(1, 5), repeat=q):
                    loads = [x * y for x in lambdas for y in ms]
                    total = sum(lambdas) * sum(ms)
                    assert len(loads) == a * q
                    assert sum(loads) == total
                    assert len(loads) * max(loads) >= total
                    product_tables += 1

    arbitrary_tables = 0
    # Arbitrary nonproduct weights on all matrices of dimensions at most 2.
    for a in range(1, 3):
        for q in range(1, 3):
            for entries in product(range(3), repeat=a * q):
                total = sum(entries)
                if not total:
                    continue
                assert a * q * max(entries) >= total
                arbitrary_tables += 1
    return {
        "product_weight_tables": product_tables,
        "arbitrary_weight_tables": arbitrary_tables,
    }


def main() -> None:
    g = load_geometry()
    geometry = geometry_and_load_audit(g)
    pascal = pascal_square_root_audit(g)
    tables = exhaustive_load_tables()
    print("PASS: projected-source cross-branch storage gate")
    print("geometry/load:", geometry)
    print("Pascal calibration:", pascal)
    print("load tables:", tables)


if __name__ == "__main__":
    main()
