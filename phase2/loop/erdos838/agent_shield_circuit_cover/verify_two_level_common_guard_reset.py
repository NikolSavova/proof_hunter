#!/usr/bin/env python3
"""Exact two-level common-guard ramp/reset audit (44 points)."""

from __future__ import annotations

import importlib.util
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "four_point_audit", HERE / "verify_two_direction_four_point_wrapper.py")
assert SPEC and SPEC.loader
v = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(v)


def chamber_seeds(points):
    """One normalized (f,g) seed for every oriented projection chamber."""
    critical = sorted({-(points[j][0] - points[i][0])
                       / (points[j][1] - points[i][1])
                       for i, j in combinations(range(len(points)), 2)
                       if points[j][1] != points[i][1]})
    probes = [critical[0] - 1]
    probes.extend((a + b) / 2 for a, b in zip(critical, critical[1:]))
    probes.append(critical[-1] + 1)
    seeds = []
    seen = set()
    for slope in probes:
        order = tuple(sorted(range(len(points)),
                             key=lambda i: points[i][0] + slope * points[i][1]))
        for sign, candidate in ((1, order), (-1, order[::-1])):
            if candidate in seen:
                continue
            seen.add(candidate)
            chart = [(sign * (x + slope * y), sign * (-slope * x + y))
                     for x, y in points]
            chart = [chart[i] for i in candidate]
            f0, f1 = min(x for x, _ in chart), max(x for x, _ in chart)
            g0, g1 = min(y for _, y in chart), max(y for _, y in chart)
            seeds.append([((x - f0) / (f1 - f0), (y - g0) / (g1 - g0))
                          for x, y in chart])
    assert len(seeds) == 182
    return seeds


def cluster(seed, parameter):
    epsilon = Q(1, 10 ** 6)
    return [v.pocket(Q(1) / parameter + epsilon * f + epsilon * epsilon * g,
                     parameter + epsilon * f - epsilon * epsilon * g)
            for f, g in seed]


def profile(points):
    signs = v.all_signs(points)
    order = tuple(sorted(range(len(points)), key=lambda i: points[i][0]))
    return v.chain_counts(signs, order)


def second_level_faces(rows):
    sizes = [1, 14, 14, 14, 1]
    caps = [1] + [row[0] for row in rows] + [1]
    cups = [1] + [row[1] for row in rows] + [1]
    faces = [1, 1561, 1561, 1561, 1]
    total = sum(faces)
    for i in range(5):
        for j in range(i + 1, 5):
            term = caps[i] * cups[j]
            for h in range(i + 1, j):
                term *= 1 + sizes[h]
            total += term
    return total


def main():
    # A first-level W-minimizing rooted word.
    base, _ = v.configuration((0, 1, 0))
    base_signs = v.all_signs(base)
    base = v.generic_perturb(base, base_signs)
    seeds = chamber_seeds(base)

    parameters = (Q(4), Q(1), Q(1, 4))
    attainable = []
    for parameter in parameters:
        menu = {}
        for seed in seeds:
            copy = cluster(seed, parameter)
            menu.setdefault(profile(copy), seed)
        attainable.append(menu)
    assert tuple(map(len, attainable)) == (166, 34, 166)

    best = None
    for rows in product(*(menu.keys() for menu in attainable)):
        faces = second_level_faces(rows)
        if best is None or faces < best[0]:
            best = (faces, rows)
    assert best == (868563, ((199, 1371), (422, 392), (1371, 199)))

    children = [cluster(menu[row], parameter)
                for menu, row, parameter
                in zip(attainable, best[1], parameters)]
    assert tuple(profile(child) for child in children) == best[1]
    parent = [(Q(-1), Q(0))] + sum(children, []) + [(Q(1), Q(0))]
    signs = v.all_signs(parent)

    # Split all pair directions without changing the 44-point chirotope.
    eta = Q(1, 10 ** 100)
    perturbed = [(x + eta * 2 ** i, y + eta * 3 ** i)
                 for i, (x, y) in enumerate(parent)]
    assert v.all_signs(perturbed) == signs
    slopes = {(perturbed[j][1] - perturbed[i][1])
              / (perturbed[j][0] - perturbed[i][0])
              for i, j in combinations(range(44), 2)}
    assert len(slopes) == 946

    orders = v.projection_orders(perturbed)
    assert len(orders) == 1892
    natural = tuple(sorted(range(44), key=lambda i: perturbed[i][0]))
    assembly = v.chain_counts(signs, natural)
    resets = [v.chain_counts(signs, order) for order in orders
              if order not in (natural, natural[::-1])]
    minimum_product = min(resets, key=lambda row: row[0] * row[1])
    minimum_maximum = min(resets, key=lambda row: max(row))

    assert assembly == (425706, 21427)
    assert minimum_product == (111422, 25911)
    assert minimum_product[0] * minimum_product[1] == 2887055442
    assert minimum_maximum == (59393, 57086)

    print("PASS: base n=14 W=1561, attainable menus=(166,34,166), "
          "second W=868563, parent n=44, chambers=1892, "
          "assembly=(425706,21427), "
          "min reset CU=2887055442 at (111422,25911), "
          "min reset max=59393 at (59393,57086)")


if __name__ == "__main__":
    main()
