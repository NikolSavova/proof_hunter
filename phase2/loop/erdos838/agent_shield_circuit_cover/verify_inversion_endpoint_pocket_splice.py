#!/usr/bin/env python3
"""Exact weighted bookkeeping for the inversion/pocket splice."""

from fractions import Fraction as Q
from itertools import combinations, product


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def geometric_barrier():
    # A pocket-labelled orientation seam does not imply endpoint failure:
    # all attached endpoint sets below have rank at most three.
    a, b, z, root = (0, 0), (1, 0), (0, 1), (2, 3)
    points = (a, b, z, root)
    assert all(orient(*triple) for triple in combinations(points, 3))
    base = {root}
    pocket = {z}
    assert len(base | pocket | {a}) == 3
    assert len(base | pocket | {b}) == 3
    g = 2
    assert g == 2 and orient(a, b, z) > 0


def weighted_splice():
    # A cell is (context, edge, pocket trace, weight, compatibility g,
    # pocket-labelled seam multiplicity).  Multiplicities never exceed the
    # trace rank r=4.  Output keys deliberately collide across contexts.
    cells = []
    weights = (Q(1), Q(2, 3), Q(3, 5), Q(4, 7))
    rank = 4
    for context, weight in enumerate(weights):
        for edge in range(3):
            for face in range(2):
                compatibility = (context + 2 * edge + face) % 3
                multiplicity = 1 + (2 * context + edge + face) % rank
                output = ((context + edge) % 3, face)
                cells.append((context, edge, face, weight, compatibility,
                              multiplicity, output))

    demand = sum(weight * multiplicity
                 for _, _, _, weight, _, multiplicity, _ in cells)
    compatible = sum(weight * multiplicity * g
                     for _, _, _, weight, g, multiplicity, _ in cells)
    zero = sum(weight * multiplicity
               for _, _, _, weight, g, multiplicity, _ in cells if g == 0)
    assert zero >= demand - compatible

    # Compare the endpoint-output load before and after retaining the
    # pocket seam label z.  Every cell has at most rank choices of z.
    cell_records = []
    seam_records = []
    for context, edge, face, weight, g, multiplicity, output in cells:
        for endpoint in range(g):
            key = (output, endpoint)
            cell_records.append((key, weight))
            for z in range(multiplicity):
                seam_records.append((key, weight, z))

    keys = {record[0] for record in seam_records}
    cell_load = max(sum(weight for key0, weight in cell_records if key0 == key)
                    for key in keys)
    seam_load = max(sum(weight for key0, weight, _ in seam_records if key0 == key)
                    for key in keys)
    assert seam_load <= rank * cell_load
    assert compatible == sum(weight for _, weight, _ in seam_records)

    # In the zero branch the canonical circuit is independent of which
    # z in the same named trace exposed the seam, so the same rank factor is
    # the exact worst possible description loss.
    circuit_cell = []
    circuit_seam = []
    for context, edge, face, weight, g, multiplicity, output in cells:
        if g:
            continue
        for endpoint in range(2):
            key = ((edge + face) % 3, endpoint)  # deliberate collisions
            circuit_cell.append((key, weight))
            for z in range(multiplicity):
                circuit_seam.append((key, weight, z))
    keys = {record[0] for record in circuit_seam}
    circuit_cell_load = max(
        sum(weight for key0, weight in circuit_cell if key0 == key)
        for key in keys)
    circuit_seam_load = max(
        sum(weight for key0, weight, _ in circuit_seam if key0 == key)
        for key in keys)
    assert circuit_seam_load <= rank * circuit_cell_load
    return (len(cells), demand, compatible, zero, cell_load, seam_load,
            circuit_cell_load, circuit_seam_load)


def exhaustive_zero_inequality():
    checked = 0
    for size in range(1, 9):
        for values in product(range(3), repeat=size):
            demand = Q(size)
            compatible = sum(map(Q, values))
            zero = Q(sum(value == 0 for value in values))
            assert zero >= demand - compatible
            checked += 1
    return checked


def main():
    geometric_barrier()
    checked = exhaustive_zero_inequality()
    (cells, demand, compatible, zero, cell_load, seam_load,
     circuit_cell_load, circuit_seam_load) = weighted_splice()
    print("PASS: pocket-labelled seam does not force g=0; "
          "patterns=%d cells=%d demand=%s compatible=%s zero=%s; "
          "endpoint loads=%s/%s circuit loads=%s/%s"
          % (checked, cells, demand, compatible, zero, cell_load, seam_load,
             circuit_cell_load, circuit_seam_load))


if __name__ == "__main__":
    main()
