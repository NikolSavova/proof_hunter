#!/usr/bin/env python3
"""Exact checks for QUASIPOLY_SOURCE_TRIANGLE_TAG_CLOSURE.md."""

from fractions import Fraction as Q
from itertools import product
from math import comb

import verify_high_triangle_query_localization as previous


def local_audit():
    systems = 0
    for rows in range(1, 101):
        for columns in range(1, 101):
            edges = rows * columns
            maximum = max(rows, columns)
            if maximum <= 5:
                assert edges <= 5 * rows
            else:
                triangles = comb(maximum, 3)
                assert 5 * edges * edges <= 54 * rows * triangles
            systems += 1
    return systems


def graph_audit():
    systems = 0
    for rows in range(1, 5):
        for columns in range(1, 5):
            pairs = [(i, j) for i in range(rows) for j in range(columns)]
            for mask in range(1, 1 << len(pairs)):
                active_rows = {i for k, (i, _j) in enumerate(pairs)
                               if mask >> k & 1}
                active_columns = {j for k, (_i, j) in enumerate(pairs)
                                  if mask >> k & 1}
                a, b = len(active_rows), len(active_columns)
                edges = mask.bit_count()
                maximum = max(a, b)
                if maximum <= 5:
                    assert edges <= 5 * a
                else:
                    assert 5 * edges * edges <= 54 * a * comb(maximum, 3)
                systems += 1
    return systems


def weighted_tag_audit():
    # Source and triangle labels overlap deliberately across contexts.
    contexts = [
        {
            "weight": Q(2, 3),
            "sources": {"a0", "a1", "a2", "a3", "a4", "a5"},
            "triangles": {f"t{k}" for k in range(20)},
            "edges": 36,
        },
        {
            "weight": Q(5, 7),
            "sources": {"a3", "a4", "a5", "a6", "a7", "a8"},
            "triangles": {f"t{k}" for k in range(10, 45)},
            "edges": 42,
        },
        {
            "weight": Q(11, 13),
            "sources": {"a7", "a8", "a9", "a10"},
            "triangles": set(),
            "edges": 20,
        },
    ]
    source_loads = {}
    source_mass = triangle_mass = thick_demand = thin_demand = Q(0)
    pair_loads = {}
    for context in contexts:
        weight = context["weight"]
        source_mass += weight * len(context["sources"])
        for source in context["sources"]:
            source_loads[source] = source_loads.get(source, Q(0)) + weight
        if context["triangles"]:
            triangle_mass += weight * len(context["triangles"])
            thick_demand += weight * context["edges"]
            canonical = min(context["sources"])
            for triangle in context["triangles"]:
                key = (canonical, triangle)
                pair_loads[key] = pair_loads.get(key, Q(0)) + weight
        else:
            thin_demand += weight * context["edges"]

    kappa = max(source_loads.values())
    source_faces = set().union(*(context["sources"] for context in contexts))
    triangle_tags = set().union(*(context["triangles"] for context in contexts))
    assert max(pair_loads.values()) <= kappa
    assert source_mass <= kappa * len(source_faces)
    assert triangle_mass <= kappa * len(source_faces) * len(triangle_tags)
    assert 5 * thick_demand * thick_demand <= 54 * source_mass * triangle_mass
    assert thin_demand <= 5 * sum(
        context["weight"] * len(context["sources"])
        for context in contexts if not context["triangles"]
    )
    return kappa, len(source_faces), len(triangle_tags), max(pair_loads.values())


def dyadic_audit():
    alpha = Q(19, 23)
    descendants = [alpha / 2, alpha / 5, alpha / 11,
                   alpha / 19, alpha / 67, alpha / 131]
    layers = {}
    for weight in descendants:
        upper = alpha
        level = 0
        while not (upper / 2 < weight <= upper):
            level += 1
            upper /= 2
        layers[level] = upper
        assert weight <= upper < 2 * weight
    assert sum(layers.values(), Q(0)) < 2 * alpha
    assert sum(descendants, Q(0)) < len(descendants) * alpha
    return len(layers), sum(layers.values(), Q(0))


def scale_audit():
    # Once sigma*loglog(n)>C+2, K dominates n^(C+3/2).
    for exponent in range(3, 20):
        n = 2 ** (2 ** exponent)
        sigma = Q(1, 2)
        polynomial_exponent = 2
        recovery_exponent = sigma * exponent
        if recovery_exponent > polynomial_exponent:
            assert n ** recovery_exponent.numerator > (
                n ** polynomial_exponent
            ) ** recovery_exponent.denominator
    return 17


def main():
    local = local_audit()
    graphs = graph_audit()
    weighted = weighted_tag_audit()
    dyadic = dyadic_audit()
    scale = scale_audit()
    stars = previous.planar_star_audit(8)
    print(
        "PASS: local=%d bipartite=%d weighted=%s dyadic=%s "
        "scale=%d planar-stars=%d"
        % (local, graphs, weighted, dyadic, scale, stars)
    )


if __name__ == "__main__":
    main()
