#!/usr/bin/env python3
"""Exact checks for CANONICAL_SOURCE_ROLE_DELETION_PASCAL_DENSITY_BARRIER."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb
from pathlib import Path
import importlib.util
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GEOMETRY = ROOT / "agent_geometry" / "audit_geometry.py"


def load_geometry():
    spec = importlib.util.spec_from_file_location("canonical_pascal_geometry", GEOMETRY)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def all_nonempty_subsets(indices):
    for size in range(1, len(indices) + 1):
        yield from combinations(indices, size)


def hull_cycle(indices, points, g):
    ordered = sorted(indices, key=lambda index: (points[index].x, points[index].y))
    if len(ordered) <= 2:
        return tuple(ordered)

    def build(sequence):
        out = []
        for index in sequence:
            while (len(out) >= 2
                   and g.det(points[out[-2]], points[out[-1]], points[index]) <= 0):
                out.pop()
            out.append(index)
        return out

    lower = build(ordered)
    upper = build(reversed(ordered))
    cycle = lower[:-1] + upper[:-1]
    assert set(cycle) == set(indices) and len(cycle) == len(indices)
    return tuple(cycle)


def tangent_family(face, points, g):
    cycle = hull_cycle(face, points, g)
    triples = set()
    for i, first in enumerate(cycle):
        second = cycle[(i + 1) % len(cycle)]
        for third in cycle:
            if third not in (first, second):
                triples.add(tuple(sorted((first, second, third))))
    return tuple(sorted(triples))


def exact_geometry_audit(g):
    n, h = 6, 3
    points = g.cell(n, h)
    total_points = len(points)
    left_size = comb(n - 1, h - 1)
    left = tuple(range(left_size))
    right = tuple(range(left_size, total_points))
    orient = g.orient_table(points)

    left_faces = [face for face in all_nonempty_subsets(left)
                  if g.is_convex(face, orient)]
    right_faces = [face for face in all_nonempty_subsets(right)
                   if g.is_convex(face, orient)]
    sources = [face for face in left_faces if not g.is_cap(face, orient)]
    pockets = [face for face in right_faces if not g.is_cup(face, orient)]

    # Complete ambient face complex from the exact strong-glue classification.
    global_faces = [frozenset()]
    global_faces.extend(frozenset(face) for face in left_faces)
    global_faces.extend(frozenset(face) for face in right_faces)
    for left_face in left_faces:
        if not g.is_cap(left_face, orient):
            continue
        for right_face in right_faces:
            if g.is_cup(right_face, orient):
                global_faces.append(frozenset(left_face + right_face))
    assert len(global_faces) == len(set(global_faces))

    rank_sum = sum(len(face) for face in global_faces)
    mean_rank = Fraction(rank_sum, len(global_faces))
    max_rank = max(map(len, global_faces))
    threshold = Fraction(total_points - 2 * mean_rank,
                         (max_rank - 2) * mean_rank)

    degree = {}
    for triple in combinations(range(total_points), 3):
        degree[triple] = sum(
            not g.is_convex(tuple(sorted(triple + (point,))), orient)
            for point in range(total_points) if point not in triple
        )

    weights = {}
    root_for_source = {}
    assignment_checks = 0
    for face in sources:
        family = tangent_family(face, points, g)
        assigned = []
        heavy_count = 0
        for point in range(total_points):
            if point in face or g.is_convex(tuple(sorted(face + (point,))), orient):
                continue
            witnesses = [triple for triple in family
                         if not g.is_convex(tuple(sorted(triple + (point,))), orient)]
            assert witnesses
            witness = min(witnesses)
            assigned.append((point, witness))
            if degree[witness] >= threshold / 2:
                heavy_count += 1

        right_witnesses = {witness for point, witness in assigned if point in right}
        assert len(right_witnesses) == 1
        root = next(iter(right_witnesses))
        assert all(degree[root] >= len(right) for _ in [0])
        assert degree[root] >= threshold / 2
        assert all(witness == root for point, witness in assigned if point in right)
        root_for_source[face] = root
        weights[face] = Fraction(heavy_count, total_points)
        assert weights[face] >= Fraction(1, 2)
        assignment_checks += len(assigned)

    buckets = defaultdict(list)
    for face in sources:
        buckets[(root_for_source[face], len(face))].append(face)
    key = max(buckets, key=lambda candidate: sum(weights[face]
                                                  for face in buckets[candidate]))
    root, rank = key
    fibre = buckets[key]
    fibre_weight = sum((weights[face] for face in fibre), Fraction())
    assert len(root) == 3 and all(set(root) <= set(face) for face in fibre)

    # Exhaust unordered colourings and keep the maximum-weight injective fibre.
    nonroot = tuple(point for point in left if point not in root)
    role_count = rank - 3
    best = None
    best_weight = Fraction(-1)
    for colouring_word in product(range(role_count), repeat=len(nonroot)):
        colour = dict(zip(nonroot, colouring_word))
        retained = []
        for face in fibre:
            colours = [colour[point] for point in face if point not in root]
            if len(colours) == role_count and len(set(colours)) == role_count:
                retained.append(face)
        retained_weight = sum((weights[face] for face in retained), Fraction())
        if retained_weight > best_weight:
            best_weight = retained_weight
            best = (colour, retained)
    assert best is not None
    colour, retained = best
    injective_probability = Fraction(1, role_count**role_count)
    for value in range(2, role_count + 1):
        injective_probability *= value
    assert best_weight >= injective_probability * fibre_weight
    assert retained

    roles = [{point} for point in root]
    roles.extend({point for point in nonroot if colour[point] == role}
                 for role in range(role_count))
    assert set().union(*roles) == set(left)

    # Complete all-order role deletion transform on the full ambient complex.
    transform_checks = 0
    q = len(roles)
    for size in range(q + 1):
        masks = [frozenset(mask) for mask in combinations(range(q), size)]
        lhs = 0
        for mask in masks:
            deleted_points = set().union(*(roles[index] for index in mask)) if mask else set()
            lhs += sum(not (face & deleted_points) for face in global_faces)
        rhs = 0
        for face in global_faces:
            empty_roles = sum(not (face & role) for role in roles)
            rhs += comb(empty_roles, size)
        assert lhs == rhs
        transform_checks += len(masks)

    cyclic_checks = 0
    for length in range(1, q + 1):
        intervals = [
            frozenset((start + offset) % q for offset in range(length))
            for start in range(q)
        ]
        lhs = 0
        for interval in intervals:
            deleted_points = set().union(*(roles[index] for index in interval))
            lhs += sum(not (face & deleted_points) for face in global_faces)
        rhs = 0
        for face in global_faces:
            rhs += sum(all(not (face & roles[index]) for index in interval)
                       for interval in intervals)
        assert lhs == rhs
        cyclic_checks += len(intervals)

    # Every deletion child retains the complete right child.
    for mask in range(1 << q):
        deleted_points = set().union(
            *(roles[index] for index in range(q) if mask >> index & 1)
        ) if mask else set()
        deletion_faces = sum(not (face & deleted_points) for face in global_faces)
        assert deletion_faces >= len(right_faces) + 1

    # Every source-release record all-deletes, and the terminal load is literal.
    output_load = Counter()
    record_weight = Fraction()
    guard_checks = 0
    for face in retained:
        face_set = set(face)
        for pocket in pockets:
            for guard_size in range(len(face) + 1):
                for guard in combinations(face, guard_size):
                    remaining = tuple(sorted(face_set - set(guard)))
                    released = g.is_convex(remaining + pocket, orient)
                    assert released == (guard_size == len(face))
                    guard_checks += 1
            output_load[pocket] += weights[face]
            record_weight += weights[face]
    assert set(output_load.values()) == {best_weight}
    assert record_weight == best_weight * len(pockets)

    return {
        "faces": len(global_faces),
        "mean_rank": mean_rank,
        "max_rank": max_rank,
        "threshold": threshold,
        "assignment_checks": assignment_checks,
        "fibre": len(fibre),
        "rank": rank,
        "retained": len(retained),
        "retained_weight": best_weight,
        "transform_checks": transform_checks,
        "cyclic_checks": cyclic_checks,
        "guard_checks": guard_checks,
        "terminal_load": next(iter(output_load.values())),
    }


def path_product(m, index):
    out = 1
    for j in range(1, index + 1):
        out *= 1 + comb(m - index + j - 1, j)
    return out


def exact_dp_audit(g, nmax=120):
    caps, cups = g.dp_counts(nmax)
    faces = g.dp_convex_counts(nmax, caps, cups)
    checked = 0
    for n in range(6, nmax + 1, 2):
        h = n // 2
        m = n - 2
        index = m // 2
        a = caps[m][index - 1]
        b = caps[m][index]
        binomial = comb(m, index)
        cap = caps[n - 1][h - 1]
        child = faces[n - 1][h - 1]
        parent = faces[n][h]
        other_profile = cups[n - 1][h - 1]

        assert cap == b + (1 + binomial) * a
        assert child >= a * b
        latest_a = path_product(m, index - 1)
        latest_b = path_product(m, index)
        assert latest_a <= a <= comb(m, index - 1) * latest_a
        assert latest_b <= b <= comb(m, index) * latest_b
        assert latest_b <= (1 << m) * latest_a
        assert latest_a <= (1 << m) * latest_b
        assert a <= (1 << (2 * m)) * b
        assert b <= (1 << (2 * m)) * a
        assert cap * cap <= (1 << (4 * m + 4)) * child
        assert parent == 2 * child + cap * cap

        physical_n = comb(n, h)
        assert parent <= physical_n**7 * child
        assert 2 * (child - cap) >= child
        assert cap <= other_profile
        endpoint_products = (
            cap * cap,
            cap * other_profile,
            other_profile * cap,
            other_profile * other_profile,
        )
        assert endpoint_products[0] == min(endpoint_products)
        checked += 1
    return checked


def main():
    g = load_geometry()
    geometry = exact_geometry_audit(g)
    dp_checks = exact_dp_audit(g)
    print(
        "PASS: canonical-Pascal faces=%d fibre=%d retained=%d "
        "weight=%s terminal-load=%s transforms=%d cyclic=%d DP=%d"
        % (geometry["faces"], geometry["fibre"], geometry["retained"],
           geometry["retained_weight"], geometry["terminal_load"],
           geometry["transform_checks"], geometry["cyclic_checks"], dp_checks)
    )


if __name__ == "__main__":
    main()
