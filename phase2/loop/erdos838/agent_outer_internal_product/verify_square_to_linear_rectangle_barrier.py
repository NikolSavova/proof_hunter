#!/usr/bin/env python3
"""Exact checks for SQUARE_TO_LINEAR_RECTANGLE_BARRIER.md."""

from itertools import combinations
from math import comb


def parameters(r: int):
    p = 2 * r + 1
    a = 4**r
    t = p * a
    carriers = comb(t, 2)
    cells = carriers * t
    k = comb(2 * r, r)
    h = 2**r
    mass = cells * k
    groups = t // p
    return p, a, t, carriers, cells, k, h, mass, groups


def exact_scale_checks(r: int):
    p, a, t, carriers, cells, k, h, mass, groups = parameters(r)

    assert t % 4 == 0
    assert groups == a
    assert h <= k

    # Each unmarked source e union R has exactly r+1 root marks.
    assert p * k == (r + 1) * comb(p, r + 1)

    # The background complete four-partite four-graph has enough edges.
    background_capacity = (t // 4) ** 4
    assert mass <= background_capacity

    # Exact cube identities.  There are p roots in every block.
    cube_records = cells * a
    cube_union = carriers * groups * (2**p - 1)
    assert groups * p == t
    assert 2**p - 1 == 2 * a - 1
    assert carriers * groups * p * a == cube_records

    # Every cell is in the heavy branch at Delta=floor(r^(1/3)).
    delta = int(r ** (1 / 3))
    low_in_one_cube = sum(comb(2 * r, j) for j in range(delta))
    assert low_in_one_cube * 2 < a

    # Exact bank statistics.
    completions = carriers * t
    half_faces = t * t * h
    pair_records = cells * t * h
    assert pair_records == carriers * t * t * h
    assert pair_records == completions * t * h
    assert pair_records == half_faces * carriers
    assert mass == cells * k

    # The claimed upper bound for all non-background faces.
    nlabels = 4 * t
    low_faces = sum(comb(nlabels, i) for i in range(4))
    gadget_high_upper = groups * (2**p) * (1 + 2 * t + carriers)
    excess_ratio = (low_faces + gadget_high_upper) / mass

    return {
        "r": r,
        "p": p,
        "q": p + 2,
        "t": t,
        "cells": cells,
        "k": k,
        "h": h,
        "mass": mass,
        "background_capacity_ratio": mass / background_capacity,
        "cube_average_degree": cube_records / cube_union,
        "low_cube_fraction": low_in_one_cube / a,
        "gadget_excess_ratio": gadget_high_upper / mass,
        "low_face_ratio": low_faces / mass,
        "total_excess_ratio_upper": excess_ratio,
    }


def finite_pair_decoder_check():
    """Exhaust a small carrier x root x pocket x subset rectangle."""

    carrier_vertices = range(5)
    carrier_edges = list(combinations(carrier_vertices, 2))
    # A cyclic regular tournament on five roots: z points to the next two.
    roots = range(5)
    pockets = range(3)
    out_neighbours = {
        root: {(root + step) % len(roots) for step in (1, 2)}
        for root in roots
    }

    seen = {}
    completion_load = {}
    half_load = {}

    for edge in carrier_edges:
        for root in roots:
            for pocket in pockets:
                completion = frozenset(
                    [("a", edge[0]), ("a", edge[1]), ("x", pocket)]
                )
                completion_load[completion] = completion_load.get(completion, 0) + 1
                neighbours = sorted(out_neighbours[root])
                for mask in range(1 << len(neighbours)):
                    subset = {
                        ("z", neighbours[bit])
                        for bit in range(len(neighbours))
                        if mask & (1 << bit)
                    }
                    half = frozenset({("x", pocket), ("z", root)} | subset)
                    half_load[half] = half_load.get(half, 0) + 1
                    pair = (completion, half)
                    record = (edge, root, pocket, mask)
                    assert pair not in seen
                    seen[pair] = record

    carriers = len(carrier_edges)
    assert set(completion_load.values()) == {len(roots)}
    # completion_load was incremented once per root, before the subset loop.
    assert set(half_load.values()) == {carriers}
    half_bank_size = 1 << len(next(iter(out_neighbours.values())))
    assert len(seen) == carriers * len(roots) * len(pockets) * half_bank_size


def main():
    finite_pair_decoder_check()

    rows = [exact_scale_checks(r) for r in (11, 12, 16, 24, 40, 80)]
    excesses = [row["total_excess_ratio_upper"] for row in rows]
    assert all(x > y for x, y in zip(excesses, excesses[1:]))
    assert excesses[-1] < 0.2

    print("finite carrier-root pair decoder: exact multiplicity 1")
    for row in rows:
        print(
            "r={r:>2} q={q:>3} cap={background_capacity_ratio:.6f} "
            "cube_deg={cube_average_degree:.6f} low={low_cube_fraction:.6g} "
            "gad/M={gadget_excess_ratio:.6f} lowfaces/M={low_face_ratio:.3g} "
            "(V-M)/M<={total_excess_ratio_upper:.6f}".format(**row)
        )
    print("all square-to-linear rectangle checks passed")


if __name__ == "__main__":
    main()
