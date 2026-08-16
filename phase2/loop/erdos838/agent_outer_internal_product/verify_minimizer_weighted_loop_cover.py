#!/usr/bin/env python3
"""Exact audit for MINIMIZER_WEIGHTED_LOOP_COVER_GATE.md."""

import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations, product
from math import comb
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent


def cross(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_indices(points):
    order = sorted(range(len(points)), key=lambda i: points[i])
    if len(order) <= 1:
        return order
    lower = []
    for i in order:
        while (len(lower) >= 2
               and cross(points[lower[-2]], points[lower[-1]], points[i]) <= 0):
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(order):
        while (len(upper) >= 2
               and cross(points[upper[-2]], points[upper[-1]], points[i]) <= 0):
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def convex(labels, points):
    labels = tuple(labels)
    return (len(labels) == len(set(labels))
            and len(labels) == len(hull_indices([points[i] for i in labels])))


def powerset(items):
    items = tuple(items)
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def canonical_triples(face, points):
    if len(face) <= 2:
        return set()
    cyclic = [face[i] for i in hull_indices([points[j] for j in face])]
    triples = set()
    h = len(cyclic)
    for i in range(h):
        for j in range(h):
            if j not in (i, (i + 1) % h):
                triples.add(tuple(sorted(
                    (cyclic[i], cyclic[(i + 1) % h], cyclic[j]))))
    assert len(triples) <= h * (h - 2)
    return triples


def audit_rank_safe_marking():
    metadata = json.loads((ERDOS / "agent_lex_minimizer_search"
                           / "exact_realizable_n9.json").read_text())
    points = [tuple(p) for p in metadata["coordinates_as_stored"]]
    n = len(points)
    labels = tuple(range(n))
    assert all(cross(*[points[i] for i in q]) != 0
               for q in combinations(labels, 3))

    faces = [a for a in powerset(labels) if convex(a, points)]
    v = len(faces)
    moment = sum(map(len, faces))
    rank = max(map(len, faces))
    assert (v, moment, rank) == (169, 492, 5)

    degree = {}
    for triple in combinations(labels, 3):
        degree[triple] = sum(
            not convex(triple + (p,), points)
            for p in labels if p not in triple)

    d_zero = F(n * v - 2 * moment, (rank - 2) * moment)
    threshold = d_zero / 2
    assigned = defaultdict(list)
    bad_total = 0
    for face in faces:
        triples = sorted(canonical_triples(face, points))
        for p in labels:
            if p in face or convex(face + (p,), points):
                continue
            witnesses = [t for t in triples if not convex(t + (p,), points)]
            assert witnesses
            assigned[(face, witnesses[0])].append(p)
            bad_total += 1

    assert bad_total == n * v - 2 * moment == 537
    light = sum(len(ps) for (face, triple), ps in assigned.items()
                if degree[triple] < threshold)
    heavy = bad_total - light
    light_bound = F(v * (n * v - 2 * moment), 2 * v)
    assert light <= light_bound
    assert heavy >= bad_total / 2

    omega = defaultdict(F)
    for key, ps in assigned.items():
        if degree[key[1]] >= threshold:
            omega[key] = F(len(ps), n)
    total_weight = sum(omega.values(), F(0))
    beta_v = F(n * v - 2 * moment, 2 * n)
    assert total_weight >= beta_v
    per_face = Counter()
    for (face, _), weight in omega.items():
        per_face[face] += weight
    assert all(weight <= 1 for weight in per_face.values())

    mu = F(moment, v)
    for k in (1, 2, 4, 8):
        high_weight = sum(
            weight for (face, _), weight in omega.items()
            if len(face) > k * mu)
        high_faces = sum(len(face) > k * mu for face in faces)
        assert high_weight <= high_faces
        assert high_faces <= F(v, k)
        retained = total_weight - high_weight
        assert retained >= total_weight - F(v, k)

    return {
        "faces": v,
        "bad": bad_total,
        "heavy": heavy,
        "weight": total_weight,
        "lower": beta_v,
    }


def audit_rooted_loop_chart():
    # Exact instance of (28)--(32): five local cap points and three
    # two-label upper roles.
    m = 5
    delta = F(1, 100 * m * m)
    local = [(F(2) - delta * t * t, -F(1, 5) + delta * t)
             for t in range(1, m + 1)]
    a, b, c0 = (F(0), F(-1)), (F(4), F(-1)), (F(0), F(4))
    epsilon = F(1, 700)
    upper = [(epsilon * u, F(4) - epsilon * epsilon * u * u)
             for u in (6, 4, 2, -2, -4, -6)]
    points = [a, b, c0] + local + upper
    labels = tuple(range(len(points)))
    root = (0, 1, 2)
    edge = (0, 1)
    pocket = tuple(range(3, 8))
    roles = ((8, 9), (10, 11), (12, 13))

    assert all(cross(*[points[i] for i in q]) != 0
               for q in combinations(labels, 3))
    assert convex(root, points)
    assert convex((0, 1, 2) + tuple(range(8, 14)), points)
    assert {p for p in labels if p not in root
            and not convex(root + (p,), points)} == set(pocket)

    sources = []
    for choice in product(*roles):
        source = root + choice
        assert convex(source, points)
        assert root in canonical_triples(source, points)
        triples = sorted(canonical_triples(source, points))
        for p in pocket:
            witnesses = [t for t in triples
                         if not convex(t + (p,), points)]
            assert witnesses and witnesses[0] == root
        sources.append(source)
    assert len(sources) == 2 ** 3

    for i, j, k in combinations(pocket, 3):
        for role in roles:
            for y in role:
                assert not convex((i, j, k, y), points)

    all_outputs = Counter()
    sigmas = []
    local_faces = [f for f in powerset(pocket) if f]
    for local_face in local_faces:
        core = tuple(sorted(edge + local_face))
        assert convex(core, points)

        looped = set()
        ordinary_edges = set()
        for r, role in enumerate(roles):
            for y in role:
                for q in combinations(tuple(sorted(set(core) | {y})), 4):
                    if not convex(q, points) and y in q:
                        looped.add(r)
        for r, s in combinations(range(len(roles)), 2):
            for y, z in product(roles[r], roles[s]):
                for q in combinations(tuple(sorted(set(core) | {y, z})), 4):
                    if not convex(q, points) and y in q and z in q:
                        ordinary_edges.add((r, s))

        def is_cover(guard):
            guard = set(guard)
            return (looped <= guard
                    and all(r in guard or s in guard
                            for r, s in ordinary_edges))

        valid_guards = []
        for guard in powerset(range(len(roles))):
            releases = True
            remaining = [roles[r] for r in range(len(roles))
                         if r not in guard]
            for choice in product(*remaining) if remaining else [()]:
                if not convex(tuple(sorted(set(core) | set(choice))), points):
                    releases = False
                    break
            assert releases == is_cover(guard)
            if releases:
                valid_guards.append(guard)

        min_size = min(map(len, valid_guards))
        cover = min(g for g in valid_guards if len(g) == min_size)
        sigma = len(cover)  # Every role has size two.
        sigmas.append(sigma)
        if len(local_face) >= 3:
            assert looped == {0, 1, 2}
            assert sigma == 3

        remaining = [r for r in range(3) if r not in cover]
        expected = 2 ** len(remaining)
        before = sum(all_outputs.values())
        choices = product(*(roles[r] for r in remaining)) if remaining else [()]
        for choice in choices:
            output = tuple(sorted(set(core) | set(choice)))
            assert convex(output, points)
            all_outputs[output] += 1
        assert sum(all_outputs.values()) - before == expected

    # The local intersection and role occupancy mask make the union load one.
    assert max(all_outputs.values()) == 1
    p_ext = 8
    exact_formula = sum(F(p_ext, 2 ** sigma) for sigma in sigmas)
    assert exact_formula == sum(all_outputs.values())

    # Exact finite Jensen: (mean 2^-sigma)^H >= 2^-sum sigma.
    h = len(sigmas)
    mean_exp = sum(F(1, 2 ** sigma) for sigma in sigmas) / h
    assert mean_exp ** h >= F(1, 2 ** sum(sigmas))

    return {
        "points": len(points),
        "sources": len(sources),
        "local_faces": h,
        "records": sum(all_outputs.values()),
        "sigma_hist": dict(Counter(sigmas)),
    }


def main():
    marked = audit_rank_safe_marking()
    chart = audit_rooted_loop_chart()
    print("PASS: minimizer weighted loop-cover gate")
    print("  rank-safe n=9:", marked)
    print("  rooted all-loop chart:", chart)


if __name__ == "__main__":
    main()
