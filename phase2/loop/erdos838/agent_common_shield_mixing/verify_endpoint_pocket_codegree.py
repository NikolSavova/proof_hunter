#!/usr/bin/env python3
"""Exact checks for ENDPOINT_POCKET_CODEGREE_DICHOTOMY.md."""

from fractions import Fraction as F
from itertools import combinations, product

from verify_mixed_seam_vertex_cover_pi2 import convex, hull, orient


def inside_triangle(point, triangle):
    signs = [orient(triangle[i], triangle[(i + 1) % 3], point)
             for i in range(3)]
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def cage_audit():
    left, right, top = (-3, 0), (3, 0), (0, 5)
    a, b, pocket = (-2, -1), (2, -1), (0, -4)
    points = [left, right, top, a, b, pocket]
    assert all(orient(*triple) != 0 for triple in combinations(points, 3))

    base = [left, right, top]
    context = base + [pocket]
    assert convex(base + [a]) and convex(base + [b])
    assert convex(base + [a, b]) and convex(context)
    assert convex([left, a, b, right])
    assert inside_triangle(a, [left, pocket, right])
    assert inside_triangle(b, [left, pocket, right])
    assert not convex(context + [a]) and not convex(context + [b])
    assert convex([pocket, a]) and convex([pocket, b])

    circuits = []
    for endpoint in (a, b):
        witness = [left, pocket, right, endpoint]
        boundary = set(hull(witness))
        hidden = [point for point in witness if point not in boundary]
        assert hidden == [endpoint]
        assert endpoint in witness and pocket in witness
        circuits.append(tuple(witness))
    return len(points), circuits


def low_codegree_audit():
    patterns = 0
    strict_examples = 0
    for size in range(1, 9):
        for values in product(range(3), repeat=size):
            total = F(size)
            compatible = sum(map(F, values))
            zero = sum(value == 0 for value in values)
            assert F(zero) >= total - compatible
            if F(zero) > total - compatible:
                strict_examples += 1
            patterns += 1
    assert strict_examples > 0
    return patterns, strict_examples


def weighted_decoder_audit():
    # Records are (context, edge, face, endpoint, output, context weight).
    weights = [F(1), F(2, 3), F(1, 4), F(3, 5)]
    records = []
    detached_records = []
    g_sum = F(0)
    for context, weight in enumerate(weights):
        for edge in range(3):
            for face in range(2):
                g = (context + edge + face) % 3
                h = min(2, g + ((context + 2 * edge + face) % 2))
                assert g <= h
                g_sum += weight * g
                for endpoint in range(g):
                    # Deliberate reuse across contexts and edges.
                    output = ((edge + context) % 3, face, endpoint)
                    records.append((context, edge, face, endpoint,
                                    output, weight))
                for endpoint in range(h):
                    # The detached output deliberately forgets context/base.
                    output = (edge % 2, face, endpoint)
                    detached_records.append((context, edge, face, endpoint,
                                             output, weight))

    assert g_sum == sum(record[-1] for record in records)
    outputs = {record[4] for record in records}
    loads = {output: sum(record[-1] for record in records
                         if record[4] == output)
             for output in outputs}
    decoder_load = max(loads.values())
    assert g_sum <= decoder_load * len(outputs)

    h_sum = sum(record[-1] for record in detached_records)
    detached_outputs = {record[4] for record in detached_records}
    detached_loads = {
        output: sum(record[-1] for record in detached_records
                    if record[4] == output)
        for output in detached_outputs
    }
    detached_load = max(detached_loads.values())
    assert h_sum <= detached_load * len(detached_outputs)

    demand = sum(weights) * 3 * 2
    zero_mass = F(0)
    for context, weight in enumerate(weights):
        for edge in range(3):
            for face in range(2):
                g = (context + edge + face) % 3
                if g == 0:
                    zero_mass += weight
    assert zero_mass >= demand - g_sum
    return (g_sum, len(outputs), decoder_load, h_sum,
            len(detached_outputs), detached_load, demand, zero_mass)


def main():
    point_count, circuits = cage_audit()
    patterns, strict = low_codegree_audit()
    (g_sum, outputs, load, h_sum, detached_outputs, detached_load,
     demand, zero) = weighted_decoder_audit()
    print("PASS: cage points=%d circuits=%d; g-patterns=%d strict=%d; "
          "weighted g=%s outputs=%d load=%s; h=%s detached=%d load=%s; "
          "demand=%s zero=%s"
          % (point_count, len(circuits), patterns, strict, g_sum, outputs,
             load, h_sum, detached_outputs, detached_load, demand, zero))


if __name__ == "__main__":
    main()
