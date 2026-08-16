#!/usr/bin/env python3
"""Exact verifier for the reset chronology theorem and colorful blow-up.

Only exact integer/Fraction arithmetic is used.  The construction shrinks a
copy of the exact twelve-point colorful barrier around every point of a
ten-point Erdos--Szekeres macro obstruction.  It checks general position,
all class-pair matchings, global pair-node degree one, label load one, the
hereditary colorful obstruction, the macro rank bound, and the injective
canonical 2+1+1 release bank.  It also audits the opposite, high-reuse
tangent model.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
COLORFUL = runpy.run_path(str(
    ROOT / "agent_shield_circuit_cover"
    / "verify_colorful_pair_endpoint_transversal_barrier.py"
))
TANGENT = runpy.run_path(str(HERE / "verify_scalable_partner_reset.py"))

BASE_POINTS = tuple(COLORFUL["POINTS"])
BASE_PAIRS = tuple(COLORFUL["PAIRS"])
BASE_CLASSES = tuple(COLORFUL["CLASSES"])
BASE_CIRCUITS = tuple(COLORFUL["CIRCUITS"])

Point = tuple[Q, Q]
Label = tuple[int, int]

# A ten-point subset of the exact barrier with no convex six-set.  It is
# used only as the finite Ramsey macro regression.
MACRO_10 = tuple(BASE_POINTS[z] for z in (0, 1, 2, 3, 5, 6, 7, 8, 9, 10))


def orient(a: Point, b: Point, c: Point) -> int:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(labels, points):
    ordered = sorted((points[z], z) for z in labels)
    if len(ordered) <= 1:
        return tuple(z for _p, z in ordered)

    def half(seq):
        out = []
        for item in seq:
            while (len(out) >= 2
                   and orient(out[-2][0], out[-1][0], item[0]) <= 0):
                out.pop()
            out.append(item)
        return out

    return tuple(z for _p, z in
                 half(ordered)[:-1] + half(list(reversed(ordered)))[:-1])


def convex(labels, points) -> bool:
    return len(labels) <= 3 or len(hull(labels, points)) == len(labels)


def max_convex_rank(points) -> int:
    labels = list(points)
    return max(size for size in range(1, len(labels) + 1)
               if any(convex(subset, points)
                      for subset in combinations(labels, size)))


def infinitesimal_copies(gadget_count: int):
    """Shrink exact colorful gadgets around the ten ES-extremal centers."""
    assert gadget_count == len(MACRO_10)
    centers = {gadget: (Q(x), Q(y))
               for gadget, (x, y) in enumerate(MACRO_10)}
    assert max_convex_rank(centers) == 5

    epsilon = Q(1, 2)
    labels = [(gadget, local)
              for gadget in range(gadget_count) for local in range(12)]
    # Distinct rational shears prevent a same-cell secant from being
    # identically aligned with another macro center during the epsilon limit.
    local_offsets = {}
    for gadget in range(gadget_count):
        shear = Q(gadget + 1, 101)
        for local, (x, y) in enumerate(BASE_POINTS):
            local_offsets[gadget, local] = (Q(x) + shear * y, Q(y))
    for halvings in range(256):
        points = {
            (gadget, local): (
                centers[gadget][0] + epsilon * local_offsets[gadget, local][0],
                centers[gadget][1] + epsilon * local_offsets[gadget, local][1],
            )
            for gadget in range(gadget_count) for local in range(12)
        }
        if not all(orient(points[a], points[b], points[c]) != 0
                   for a, b, c in combinations(labels, 3)):
            epsilon /= 2
            continue
        # Every transversal through distinct gadget cells has the macro
        # chirotope.  Hence a bad macro four-set remains bad fibrewise.
        stable = True
        for a, b, c in combinations(labels, 3):
            ga, gb, gc = a[0], b[0], c[0]
            if len({ga, gb, gc}) < 3:
                continue
            macro_sign = orient(centers[ga], centers[gb], centers[gc])
            micro_sign = orient(points[a], points[b], points[c])
            if macro_sign * micro_sign <= 0:
                stable = False
                break
        if stable:
            return points, centers, epsilon, halvings
        epsilon /= 2
    raise AssertionError("infinitesimal-copy search did not terminate")


def colorful_blowup(t: int, r: int):
    """One twelve-point obstruction for every class triple and copy."""
    assert t >= 3 and r >= 1
    members: defaultdict[int, list[Label]] = defaultdict(list)
    matchings: defaultdict[tuple[int, int], list[tuple[Label, ...]]] = (
        defaultdict(list)
    )
    gadgets = []

    for triple in combinations(range(t), 3):
        for copy in range(r):
            gadget = len(gadgets)
            local_to_global = {z: (gadget, z) for z in range(12)}
            for local_colour, global_class in enumerate(triple):
                members[global_class].extend(
                    local_to_global[z] for z in BASE_CLASSES[local_colour]
                )

            # Local circuit order is 01, 12, 20.
            circuit_pairs = ((triple[0], triple[1]),
                             (triple[1], triple[2]),
                             (triple[2], triple[0]))
            local_edges = []
            for class_pair, circuit in zip(circuit_pairs, BASE_CIRCUITS):
                key = tuple(sorted(class_pair))
                quad = tuple(local_to_global[z] for z in circuit)
                matchings[key].append(quad)
                local_edges.append(quad)
            gadgets.append((triple, copy, local_to_global, local_edges))
    points, centers, epsilon, halvings = infinitesimal_copies(len(gadgets))
    return points, members, matchings, gadgets, centers, epsilon, halvings


def pair_in_class(quad, cls, membership):
    pair = tuple(sorted(z for z in quad if z in membership[cls]))
    assert len(pair) == 2
    return pair


def canonical_release(quad, y, points):
    assert not convex(quad, points)
    for z in sorted(quad):
        face = tuple(x for x in quad if x != z) + (y,)
        if convex(face, points):
            return frozenset(face)
    raise AssertionError("ES(4)=5 release missing")


def blowup_audit(t: int = 5, r: int = 1) -> dict[str, int]:
    (points, members, matchings, gadgets, centers,
     epsilon, halvings) = colorful_blowup(t, r)
    m = r * (t - 2)
    g = 2 * m * (t - 1)
    membership = {cls: set(labels) for cls, labels in members.items()}

    assert len(points) == 12 * r * comb(t, 3)
    assert all(len(members[cls]) == g for cls in range(t))
    assert all(orient(points[a], points[b], points[c]) != 0
               for a, b, c in combinations(points, 3))
    assert all(len(matchings[i, j]) == m
               for i, j in combinations(range(t), 2))

    label_load = Counter()
    pair_degree = Counter()
    edges = []
    for i, j in combinations(range(t), 2):
        seen = set()
        for quad in matchings[i, j]:
            assert not convex(quad, points)
            assert not (seen & set(quad))
            seen.update(quad)
            pi = pair_in_class(quad, i, membership)
            pj = pair_in_class(quad, j, membership)
            pair_degree[(i, pi)] += 1
            pair_degree[(j, pj)] += 1
            label_load.update(quad)
            edges.append((i, j, quad))
    assert set(label_load.values()) == {1}
    assert set(pair_degree.values()) == {1}
    assert len(edges) == m * comb(t, 2)

    # Every local colorful endpoint word is bad.  A global endpoint word
    # contains one such six-label word for every gadget, so heredity kills it.
    local_colorful_checks = 0
    for _triple, _copy, local_to_global, _local_edges in gadgets:
        assert all(convex(tuple(local_to_global[z] for z in local_class),
                          points)
                   for local_class in BASE_CLASSES)
        pairs = [tuple(local_to_global[z] for z in pair) for pair in BASE_PAIRS]
        for bits in product((0, 1), repeat=6):
            trace = tuple(pairs[q][bits[q]] for q in range(6))
            assert not convex(trace, points)
            local_colorful_checks += 1

    # Degree-one pair nodes turn the five-point release into a global
    # injection, not merely a load-three per-class-triple bank.
    outputs = {}
    records = 0
    for i, j, quad in edges:
        for k in range(t):
            if k in (i, j):
                continue
            for y in members[k]:
                face = canonical_release(quad, y, points)
                assert face not in outputs
                outputs[face] = (i, j, quad, k, y)
                records += 1
    expected = m * comb(t, 2) * (t - 2) * g
    assert records == len(outputs) == expected

    # A global ordinary partial endpoint trace activates a convex subset of
    # macro gadgets and uses at most five endpoints in each active gadget.
    macro_rank = max_convex_rank(centers)
    local_endpoint_rank = 5
    endpoint_nodes = 6 * len(gadgets)
    global_endpoint_rank_bound = macro_rank * local_endpoint_rank
    assert global_endpoint_rank_bound < endpoint_nodes // 2

    # The source-size/load inequality is sharp here.
    incidence_per_class = 2 * m * (t - 1)
    assert g == incidence_per_class
    return {
        "t": t,
        "matching_size_m": m,
        "class_size_g": g,
        "points": len(points),
        "circuit_edges": len(edges),
        "label_load": 1,
        "pair_node_degree": 1,
        "pair_node_triangles": 0,
        "local_colorful_failures": local_colorful_checks,
        "global_colorful_transversals": 0,
        "macro_convex_rank": macro_rank,
        "global_partial_endpoint_rank_bound": global_endpoint_rank_bound,
        "physical_pair_nodes": endpoint_nodes,
        "injective_2+1+1_releases": records,
        "micro_epsilon": epsilon,
        "micro_halvings": halvings,
    }


def tangent_audit(t: int = 5, m: int = 4) -> dict[str, int]:
    points, _delta, _halvings = TANGENT["construct"](t, m)
    circuits = TANGENT["circuit_audit"](t, m, points)
    releases = TANGENT["es5_audit"](t, m, points)
    all_lower = ([(i, "L", a) for i in range(t - 1) for a in range(m)]
                 + TANGENT["class_labels"](t, m, t - 1))
    ordered = sorted(all_lower, key=lambda z: points[z][0])
    assert all(TANGENT["orient"](points[a], points[b], points[c]) > 0
               for a, b, c in combinations(ordered, 3))
    expected_releases = m * comb(t, 2) * (t - 2) * (2 * m)
    assert releases["es5_records"] == expected_releases
    assert releases["es5_max_decoder_load"] == 1

    # Full-support matchings force the maximum possible label itinerary.
    g = 2 * m
    load_sum = g * (t - 1)
    turns = g * comb(t - 1, 2)
    assert load_sum == 2 * m * (t - 1)
    return {
        "t": t,
        "matching_size_m": m,
        "class_size_g": g,
        "label_load": circuits["label_load"],
        "partner_turns_per_class": turns,
        "all_lower_plus_top_roles": len(all_lower),
        "injective_2+1+1_releases": releases["es5_distinct_faces"],
    }


def base_twelve_point_audit() -> dict[str, int]:
    points = {(0, i): p for i, p in enumerate(BASE_POINTS)}
    colorful = one_gap = 0
    partial_rank_vector = []
    for rank in range(7):
        good = 0
        for roles in combinations(range(6), rank):
            for bits in product((0, 1), repeat=rank):
                trace = tuple((0, BASE_PAIRS[roles[q]][bits[q]])
                              for q in range(rank))
                good += convex(trace, points)
        partial_rank_vector.append(good)
    assert partial_rank_vector == [1, 12, 60, 160, 114, 16, 0]
    for bits in product((0, 1), repeat=6):
        trace = tuple((0, BASE_PAIRS[q][bits[q]]) for q in range(6))
        colorful += convex(trace, points)
    assert colorful == 0
    gap_counts = []
    for omitted in range(6):
        retained = [p for q, p in enumerate(BASE_PAIRS) if q != omitted]
        good = 0
        for bits in product((0, 1), repeat=5):
            trace = tuple((0, retained[q][bits[q]]) for q in range(5))
            good += convex(trace, points)
        gap_counts.append(good)
        one_gap += good
    assert gap_counts == [0, 0, 8, 8, 0, 0]
    face_count = sum(
        convex(tuple((0, z) for z in range(12) if mask >> z & 1), points)
        for mask in range(1, 1 << 12)
    )
    assert face_count == 709
    return {"colorful_6_faces": colorful,
            "one_gap_counts": tuple(gap_counts),
            "one_gap_total": one_gap,
            "partial_endpoint_rank_vector": tuple(partial_rank_vector),
            "partial_endpoint_words": sum(partial_rank_vector),
            "ordinary_faces": face_count}


def main() -> None:
    base = base_twelve_point_audit()
    blowup = blowup_audit()
    tangent = tangent_audit()
    print("PASS")
    print(f"  12-point barrier: {base}")
    print(f"  colorful blow-up: {blowup}")
    print(f"  tangent high-reuse audit: {tangent}")


if __name__ == "__main__":
    main()
