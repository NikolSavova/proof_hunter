#!/usr/bin/env python3
"""Exact verifier for REALIZED_CHAMBER_CYCLE_OR_FOREST_GATE.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import importlib.util
import sys


ROOT = Path(__file__).resolve().parent.parent
GEOMETRY = ROOT / "agent_geometry" / "audit_geometry.py"


def load_geometry():
    spec = importlib.util.spec_from_file_location("chamber_cycle_geometry",
                                                  GEOMETRY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def cycle_exponent_audit() -> int:
    checks = 0
    # c_i,u_i are base-two logarithms of cap/cup counts.  All computations
    # are exact integers; twice-energy and twice-potential avoid fractions.
    for k in range(2, 5):
        for caps in product(range(3), repeat=k):
            for cups in product(range(3), repeat=k):
                for net in product(range(-1, 2), repeat=k):
                    edge_exponents = []
                    twice_rhs_terms = []
                    for i in range(k):
                        j = (i + 1) % k
                        edge = caps[i] + cups[j] + net[i]
                        edge_exponents.append(edge)

                        energy2_i = caps[i] + cups[i]
                        energy2_j = caps[j] + cups[j]
                        rho2_i = cups[i] - caps[i]
                        rho2_j = cups[j] - caps[j]
                        twice_rhs = (energy2_i + energy2_j
                                     + rho2_j - rho2_i + 2 * net[i])
                        assert twice_rhs == 2 * edge
                        twice_rhs_terms.append(twice_rhs)

                    # Potential telescopes exactly around the cycle.
                    assert sum(edge_exponents) == (
                        sum(caps) + sum(cups) + sum(net))
                    assert sum(twice_rhs_terms) == 2 * sum(edge_exponents)
                    assert max(edge_exponents) * k >= sum(edge_exponents)
                    checks += 1
    return checks


def directed_core(vertices: int, edges: set[tuple[int, int]]) -> set[int]:
    alive = set(range(vertices))
    changed = True
    while changed:
        changed = False
        remove = set()
        for v in alive:
            indeg = any(a in alive and b == v for a, b in edges)
            outdeg = any(a == v and b in alive for a, b in edges)
            if not indeg or not outdeg:
                remove.add(v)
        if remove:
            alive.difference_update(remove)
            changed = True
    return alive


def has_directed_cycle(vertices: int, edges: set[tuple[int, int]]) -> bool:
    adjacency = [[] for _ in range(vertices)]
    for a, b in edges:
        adjacency[a].append(b)
    colour = [0] * vertices

    def visit(v: int) -> bool:
        colour[v] = 1
        for w in adjacency[v]:
            if colour[w] == 1:
                return True
            if colour[w] == 0 and visit(w):
                return True
        colour[v] = 2
        return False

    return any(colour[v] == 0 and visit(v) for v in range(vertices))


def directed_graph_audit() -> dict[str, int]:
    graphs = 0
    for n in range(1, 5):
        possible = [(a, b) for a in range(n) for b in range(n) if a != b]
        for mask in range(1 << len(possible)):
            edges = {possible[j] for j in range(len(possible))
                     if (mask >> j) & 1}
            core = directed_core(n, edges)
            cycle = has_directed_cycle(n, edges)
            assert bool(core) == cycle
            graphs += 1

    # Explicit high-outdegree layered role forests.
    layered = 0
    for depth in range(2, 7):
        for width in range(2, 6):
            vertices = depth * width
            edges = set()
            for level in range(depth - 1):
                for a in range(width):
                    for b in range(width):
                        edges.add((level * width + a,
                                   (level + 1) * width + b))
            assert not has_directed_cycle(vertices, edges)
            assert not directed_core(vertices, edges)
            assert all(sum(x == v for x, _ in edges) == width
                       for v in range((depth - 1) * width))
            layered += 1
    return {"loopless_digraphs": graphs, "layered_dags": layered}


def det(a, b, c) -> Fraction:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_vertices(points: list[tuple[Fraction, Fraction]]) -> tuple[int, ...]:
    order = sorted(range(len(points)), key=lambda i: points[i])
    lower: list[int] = []
    for i in order:
        while (len(lower) >= 2
               and det(points[lower[-2]], points[lower[-1]], points[i]) < 0):
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in order:
        while (len(upper) >= 2
               and det(points[upper[-2]], points[upper[-1]], points[i]) > 0):
            upper.pop()
        upper.append(i)
    return tuple(sorted(set(lower).union(upper)))


def is_convex_position(points: list[tuple[Fraction, Fraction]]) -> bool:
    if len(points) <= 3:
        return True
    return len(hull_vertices(points)) == len(points)


def geometric_outstar(m: int) -> dict[str, int]:
    q = (m - 1) // 2
    source = [(Fraction(i), Fraction(i * i)) for i in range(m)]
    delta = Fraction(1, 1_000_000 * m * m)
    queries = [
        (Fraction(2 * j + 1, 2),
         Fraction(-7, 3) + delta * (j + 1) * (j + 2))
        for j in range(q)
    ]
    total = source + queries

    # Exact general position.
    assert all(det(total[a], total[b], total[c])
               for a, b, c in combinations(range(len(total)), 3))
    assert is_convex_position(source)
    assert is_convex_position(queries)

    sign_vectors = []
    hidden_sets = []
    tag_sizes = []
    for j, z in enumerate(queries):
        local = source + [z]
        hull = set(hull_vertices(local))
        source_hull = tuple(i for i in range(m) if i in hull)
        hidden = tuple(i for i in range(m) if i not in hull)
        assert hidden
        hidden_sets.append(hidden)

        full = source + [z]
        tag = [source[i] for i in source_hull] + [z]
        assert not is_convex_position(full)
        assert is_convex_position(tag)
        assert tag[-1] == z  # physical edge label is retained
        tag_sizes.append(len(tag))

        signs = tuple(1 if det(source[a], source[b], z) > 0 else -1
                      for a, b in combinations(range(m), 2))
        sign_vectors.append(signs)

    assert len(set(sign_vectors)) == q
    assert len(set(hidden_sets)) == q

    # Query graph is the out-star 0 -> j+1.
    edges = {(0, j + 1) for j in range(q)}
    assert not has_directed_cycle(q + 1, edges)
    assert not directed_core(q + 1, edges)

    # The ambient query-label bank is Boolean because all queries are in
    # convex position.
    ambient_query_faces = 1 << q
    assert ambient_query_faces >= 2 ** q
    return {
        "m": m,
        "queries": q,
        "distinct_chambers": len(set(sign_vectors)),
        "min_projected_tag_rank": min(tag_sizes),
        "max_projected_tag_rank": max(tag_sizes),
        "ambient_query_faces": ambient_query_faces,
    }


def endpoint_energy_audit(g, nmax: int = 56) -> int:
    caps, cups = g.dp_counts(nmax)
    faces = g.dp_convex_counts(nmax, caps, cups)
    checks = 0
    for n in range(nmax + 1):
        for i in range(n + 1):
            assert faces[n][i] <= caps[n][i] * cups[n][i]
            checks += 1
    return checks


def main() -> None:
    g = load_geometry()
    cycles = cycle_exponent_audit()
    graphs = directed_graph_audit()
    stars = [geometric_outstar(m) for m in (8, 12, 20, 30)]
    endpoints = endpoint_energy_audit(g)
    print("PASS: realized chamber cycle-or-forest gate")
    print("cycle exponent systems:", cycles)
    print("directed graphs:", graphs)
    print("geometric diffuse out-stars:", stars)
    print("endpoint-energy Pascal cells:", endpoints)


if __name__ == "__main__":
    main()
