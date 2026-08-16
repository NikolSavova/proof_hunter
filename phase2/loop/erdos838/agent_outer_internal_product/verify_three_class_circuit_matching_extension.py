#!/usr/bin/env python3
"""Verifier for THREE_CLASS_CIRCUIT_MATCHING_EXTENSION_AND_ANTI_ALIGNMENT."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from random import Random


def det(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull(points, trace):
    word = sorted((points[i], i) for i in trace)
    if len(word) <= 1:
        return [i for _, i in word]
    lower = []
    for point, index in word:
        while (len(lower) >= 2
               and det(lower[-2][0], lower[-1][0], point) <= 0):
            lower.pop()
        lower.append((point, index))
    upper = []
    for point, index in reversed(word):
        while (len(upper) >= 2
               and det(upper[-2][0], upper[-1][0], point) <= 0):
            upper.pop()
        upper.append((point, index))
    return [index for _, index in lower[:-1] + upper[:-1]]


def convex(points, trace):
    return len(hull(points, trace)) == len(trace)


def inside_triangle(point, triangle):
    signs = [det(triangle[i], triangle[(i + 1) % 3], point)
             for i in range(3)]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def build_planar_anti_alignment(m):
    """Three disjoint pair sectors; each selected circuit is 2+2."""
    rng = Random(838_000 + m)
    pair_data = (("A", "B"), ("B", "C"), ("C", "A"))
    templates = ((-4, -3), (4, -3), (0, 5), (0, 0))
    for attempt in range(100):
        points = []
        classes = {name: [] for name in "ABC"}
        matchings = {pair: [] for pair in pair_data}
        for pair_index, pair in enumerate(pair_data):
            base_x = (-12000, 12000, 0)[pair_index]
            base_y = (0, 0, 14000)[pair_index]
            for index in range(m):
                center_x = base_x + 120 * index
                center_y = base_y + 47 * index * index + 19 * index
                ids = []
                for local, (dx, dy) in enumerate(templates):
                    jitter_x = Q(rng.randrange(-100, 101), 100000)
                    jitter_y = Q(rng.randrange(-100, 101), 100000)
                    ids.append(len(points))
                    points.append((Q(center_x + dx) + jitter_x,
                                   Q(center_y + dy) + jitter_y))
                # The fourth template point is the designated interior one.
                if not inside_triangle(points[ids[3]],
                                       [points[i] for i in ids[:3]]):
                    break
                first, second = pair
                classes[first].extend((ids[3], ids[0]))
                classes[second].extend((ids[1], ids[2]))
                matchings[pair].append(frozenset(ids))
            else:
                continue
            break
        if any(det(points[i], points[j], points[k]) == 0
               for i, j, k in combinations(range(len(points)), 3)):
            continue
        if not all(not convex(points, edge)
                   for matching in matchings.values() for edge in matching):
            continue
        assert all(len(classes[name]) == 4 * m for name in "ABC")
        return points, classes, matchings
    raise AssertionError("failed to find generic rational perturbation")


def canonical_extension(points, circuit, external):
    assert len(circuit) == 4 and external not in circuit
    candidates = []
    for omitted in sorted(circuit):
        face = frozenset((set(circuit) - {omitted}) | {external})
        if convex(points, face):
            candidates.append((omitted, face))
    # This is the five-point Erdos--Szekeres lemma, checked exactly here.
    assert candidates
    return candidates[0]


def face_count(points, support):
    count = 0
    labels = list(support)
    for mask in range(1, 1 << len(labels)):
        trace = [labels[i] for i in range(len(labels)) if mask >> i & 1]
        count += convex(points, trace)
    return count


def planar_bank_audit(m=3):
    points, classes, matchings = build_planar_anti_alignment(m)
    # Incident pair matchings use disjoint physical supports in each class.
    for name in "ABC":
        incident = []
        for pair, matching in matchings.items():
            if name in pair:
                incident.append(set().union(*matching) & set(classes[name]))
        assert len(incident) == 2 and incident[0].isdisjoint(incident[1])

    representations = defaultdict(list)
    thirds = {("A", "B"): "C", ("B", "C"): "A", ("C", "A"): "B"}
    total_records = 0
    per_pair_outputs = {}
    for pair, matching in matchings.items():
        outputs = set()
        third = thirds[pair]
        for edge in matching:
            for external in classes[third]:
                omitted, face = canonical_extension(points, edge, external)
                outputs.add(face)
                representations[face].append((pair, edge, external, omitted))
                total_records += 1
        assert len(outputs) == len(matching) * len(classes[third])
        per_pair_outputs[pair] = len(outputs)
    max_load = max(map(len, representations.values()))
    assert max_load <= 3
    assert len(representations) * max_load >= total_records

    # Actual induced class banks, not formal placeholders.
    class_faces = {name: face_count(points, support)
                   for name, support in classes.items()}
    g = 4 * m
    baseline = g + comb(g, 2) + comb(g, 3)
    assert all(value >= baseline for value in class_faces.values())
    if m == 3:
        assert class_faces == {"A": 1161, "B": 1161, "C": 1161}

    # Duplicating each geometric record h times multiplies precisely the
    # external history load and creates no new physical output.
    history = 7
    duplicated_load = max_load * history
    assert len(representations) >= total_records * history / duplicated_load
    return {
        "points": len(points),
        "g": g,
        "matching": m,
        "records": total_records,
        "outputs": len(representations),
        "load": max_load,
        "class_faces": class_faces,
    }


def full_overlap_abstract_cycle(m=7):
    """Perfect support overlap in every class but no circuit triangle."""
    assert m > 1
    a = {(i, bit): ("A", i, bit) for i in range(m) for bit in range(2)}
    b = {(i, bit): ("B", i, bit) for i in range(m) for bit in range(2)}
    c = {(i, bit): ("C", i, bit) for i in range(m) for bit in range(2)}
    ab = [frozenset([a[((i - 1) % m, bit)] for bit in range(2)]
                    + [b[(i, bit)] for bit in range(2)]) for i in range(m)]
    bc = [frozenset([b[(i, bit)] for bit in range(2)]
                    + [c[(i, bit)] for bit in range(2)]) for i in range(m)]
    ca = [frozenset([c[(i, bit)] for bit in range(2)]
                    + [a[(i, bit)] for bit in range(2)]) for i in range(m)]
    assert all(len(set().union(*family)) == 4 * m for family in (ab, bc, ca))
    assert set().union(*ab) & set(a.values()) == set(a.values())
    assert set().union(*ca) & set(a.values()) == set(a.values())
    assert set().union(*ab) & set(b.values()) == set(b.values())
    assert set().union(*bc) & set(b.values()) == set(b.values())
    assert set().union(*bc) & set(c.values()) == set(c.values())
    assert set().union(*ca) & set(c.values()) == set(c.values())
    triangles = 0
    for edge_ab in ab:
        for edge_bc in bc:
            if edge_ab.isdisjoint(edge_bc):
                continue
            for edge_ca in ca:
                if not edge_bc.isdisjoint(edge_ca) and not edge_ca.isdisjoint(edge_ab):
                    triangles += 1
    assert triangles == 0
    return len(ab) + len(bc) + len(ca)


def colorful_six_reset_kill():
    points = [(Q(x), Q(y)) for x, y in [
        (-11000, -11), (-7797, 629),
        (-9971, 1975), (-10004, 505),
        (-1006, 9987), (999, 10011),
        (-30, 12020), (-254, 13159),
        (9005, -24), (15883, -1249),
        (9980, 2008), (9984, 500),
    ]]
    assert all(det(points[i], points[j], points[k])
               for i, j, k in combinations(range(12), 3))
    circuits = ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11))
    classes = ((0, 1, 10, 11), (2, 3, 4, 5), (6, 7, 8, 9))
    assert all(not convex(points, edge) for edge in circuits)
    assert all(convex(points, cls) for cls in classes)
    assert [face_count(points, cls) for cls in classes] == [15, 15, 15]

    # These are the two physical partner pairs in each of the three classes.
    pair_nodes = ((0, 1), (10, 11), (2, 3),
                  (4, 5), (6, 7), (8, 9))
    convex_colorful = []
    for bits in product((0, 1), repeat=6):
        trace = tuple(pair_nodes[i][bits[i]] for i in range(6))
        if convex(points, trace):
            convex_colorful.append((bits, trace))
    assert convex_colorful == []
    return 1 << len(pair_nodes)


def pair_node_triangle_payment():
    points = [(Q(x), Q(y)) for x, y in [
        (138, 679), (505, 820),
        (269, 337), (293, 733),
        (528, 847), (378, 590),
    ]]
    assert all(det(points[i], points[j], points[k])
               for i, j, k in combinations(range(6), 3))
    nodes = ((0, 1), (2, 3), (4, 5))
    pair_unions = [nodes[i] + nodes[j]
                   for i, j in combinations(range(3), 2)]
    assert all(not convex(points, trace) for trace in pair_unions)
    seams = [trace for trace in combinations(range(6), 4)
             if convex(points, trace)]
    assert len(seams) == 3
    assert all(len({label // 2 for label in trace}) == 3 for trace in seams)
    # Six five-subsets each see a seam; each seam is counted exactly twice.
    incidence = sum(
        sum(set(seam) <= set(five) for seam in seams)
        for five in combinations(range(6), 5)
    )
    assert incidence == 2 * len(seams) == 6
    return len(seams)


if __name__ == "__main__":
    audit = planar_bank_audit()
    abstract_edges = full_overlap_abstract_cycle()
    colorful = colorful_six_reset_kill()
    triangle_seams = pair_node_triangle_payment()
    print(
        "PASS: planar anti-alignment=%s; full-overlap triangle-free edges=%d; "
        "colorful six killed=%d; pair-triangle seams=%d"
        % (audit, abstract_edges, colorful, triangle_seams)
    )
