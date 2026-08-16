#!/usr/bin/env python3
"""Exact finite audit for GLOBAL_MARKED_POCKET_RELEASE.md."""

import json
import sys
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
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
    return len(set(labels)) == len(labels) == len(
        hull_indices([points[i] for i in labels]))


def powerset(labels, max_size=None):
    labels = tuple(sorted(labels))
    stop = len(labels) if max_size is None else min(max_size, len(labels))
    for size in range(stop + 1):
        yield from combinations(labels, size)


def canonical_triples(face, points):
    if len(face) <= 2:
        return set()
    local_hull = hull_indices([points[i] for i in face])
    cyclic = [face[i] for i in local_hull]
    h = len(cyclic)
    triples = set()
    for i in range(h):
        for j in range(h):
            if j not in (i, (i + 1) % h):
                triples.add(tuple(sorted(
                    (cyclic[i], cyclic[(i + 1) % h], cyclic[j]))))
    return triples


def bad_circuit(q, points):
    return len(q) == 4 and not convex(q, points)


def interior_label(q, points):
    local_hull = set(hull_indices([points[i] for i in q]))
    assert len(local_hull) == 3
    return q[next(i for i in range(4) if i not in local_hull)]


def main():
    metadata = json.loads((ERDOS / "agent_lex_minimizer_search"
                           / "exact_realizable_n9.json").read_text())
    points = [tuple(p) for p in metadata["coordinates_as_stored"]]
    n = len(points)
    all_labels = tuple(range(n))
    faces = [face for face in powerset(all_labels) if convex(face, points)]
    v = len(faces)
    moment = sum(map(len, faces))
    rank = max(map(len, faces))
    assert (n, v, moment, rank) == (9, 169, 492, 5)

    degrees = {}
    role_classes = {}
    for triple in combinations(all_labels, 3):
        classes = defaultdict(list)
        for x in all_labels:
            if x in triple:
                continue
            q = tuple(sorted(triple + (x,)))
            if bad_circuit(q, points):
                inside = interior_label(q, points)
                # Roles 0,1,2 mean the corresponding sorted root label is
                # interior; role 3 means the neighbor x is interior.
                role = triple.index(inside) if inside in triple else 3
                classes[role].append(x)
        degrees[triple] = sum(map(len, classes.values()))
        if classes:
            best_role = min(classes, key=lambda r: (-len(classes[r]), r))
            role_classes[triple] = tuple(sorted(classes[best_role]))

    d_zero = F(n * v - 2 * moment, (rank - 2) * moment)
    threshold = d_zero / 2
    high = {t for t, degree in degrees.items() if degree >= threshold}
    assert len(high) == 84

    incidences = []
    for face in faces:
        for triple in canonical_triples(face, points) & high:
            pocket = role_classes[triple]
            assert pocket
            assert set(face).isdisjoint(pocket)
            assert len(pocket) * 4 >= degrees[triple]
            incidences.append((face, triple))
    assert len(incidences) == 258

    alpha = F(n * v - 2 * moment, 2 * (n - 3) * v)
    assert len(incidences) >= alpha * v

    release_totals = {}
    actual_multiplicities = {}
    tau_histograms = {}
    for g in (0, 1, 2):
        outputs = Counter()
        b_values = []
        tau_hist = Counter()
        for face, triple in incidences:
            pocket = role_classes[triple]
            pocket_faces = [f for f in powerset(pocket) if convex(f, points)]

            split_outer_traces = set()
            for q in combinations(tuple(sorted(set(face) | set(pocket))), 4):
                outer = tuple(sorted(set(q) & set(face)))
                inner = tuple(sorted(set(q) & set(pocket)))
                if outer and inner and bad_circuit(q, points):
                    split_outer_traces.add(outer)

            minimum_guard = None
            for guard in powerset(face):
                hits = all(set(guard) & set(edge)
                           for edge in split_outer_traces)
                releases_all = all(
                    convex((set(face) - set(guard)) | set(pocket_face), points)
                    for pocket_face in pocket_faces)
                assert hits == releases_all
                if hits and minimum_guard is None:
                    minimum_guard = len(guard)
            assert minimum_guard is not None
            tau_hist[minimum_guard] += 1

            count_here = 0
            for guard in powerset(face, g):
                for pocket_face in pocket_faces:
                    output = tuple(sorted(
                        (set(face) - set(guard)) | set(pocket_face)))
                    if not convex(output, points):
                        continue
                    count_here += 1
                    outputs[output] += 1

                    # Decoder (C,T,G) -> (F,A).
                    decoded_f = tuple(sorted(set(output) & set(pocket)))
                    decoded_a = tuple(sorted(
                        (set(output) - set(decoded_f)) | set(guard)))
                    assert decoded_f == pocket_face
                    assert decoded_a == face
            b_values.append(count_here)

        total = sum(b_values)
        multiplicity_bound = comb(n, 3) * sum(comb(n, i) for i in range(g + 1))
        assert total == sum(outputs.values())
        assert max(outputs.values()) <= multiplicity_bound
        assert total <= multiplicity_bound * v
        release_totals[g] = total
        actual_multiplicities[g] = max(outputs.values())
        tau_histograms[g] = tau_hist

    print("PASS: global marked-pocket release")
    print(f"  marked incidences: {len(incidences)}, alpha*V={float(alpha*v):.3f}")
    for g in (0, 1, 2):
        bound = comb(n, 3) * sum(comb(n, i) for i in range(g + 1))
        print(f"  g={g}: records={release_totals[g]}, "
              f"max multiplicity={actual_multiplicities[g]} <= {bound}")
    print(f"  exact guard histogram: {dict(tau_histograms[2])}")


if __name__ == "__main__":
    main()
