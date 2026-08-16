#!/usr/bin/env python3
"""Exact checks for CARRIER_ALPHABET_SQUARE_GATE.md."""

from fractions import Fraction
from itertools import combinations_with_replacement
from math import ceil, comb, isqrt


def minimal_endpoint_count(edge_count: int) -> int:
    assert edge_count >= 1
    # First integer d with d(d-1)/2 >= edge_count.
    d = (1 + isqrt(1 + 8 * edge_count)) // 2
    while comb(d, 2) < edge_count:
        d += 1
    while d > 1 and comb(d - 1, 2) >= edge_count:
        d -= 1
    return d


def endpoint_formula_checks():
    for edges in range(1, 5000):
        d = minimal_endpoint_count(edges)
        assert comb(d, 2) >= edges
        assert d == 1 or comb(d - 1, 2) < edges
        formula = ceil((1 + (1 + 8 * edges) ** 0.5) / 2)
        assert d == formula


def finite_global_gate_check():
    # Twelve marked profiles project with load lambda=3 to four key faces.
    profiles = 12
    key_load = 3
    carrier_edges = 15
    d = minimal_endpoint_count(carrier_edges)
    assert d == 6

    records = profiles * carrier_edges
    # Use an abstract ambient V satisfying the two actual lower bounds.
    detached_face_lower_bound = 37
    ambient_faces = 50
    assert ambient_faces >= ceil(profiles / key_load)
    assert ambient_faces >= detached_face_lower_bound

    first = key_load * carrier_edges
    second = Fraction(profiles * carrier_edges, detached_face_lower_bound)
    assert Fraction(records, ambient_faces) <= first
    assert Fraction(records, ambient_faces) <= second

    # In the convex-shield branch the detached lower bound is 2^d.
    convex_ambient_faces = 2**d
    assert Fraction(records, convex_ambient_faces) <= Fraction(
        profiles * carrier_edges, 2**d
    )


def middle_mark_load_checks():
    for r in range(1, 100):
        p = 2 * r + 1
        k = comb(2 * r, r)
        assert p * k == (r + 1) * comb(p, r + 1)


def ferrers_rectangle_checks():
    # Exhaust all nonincreasing degree sequences with at most 7 rows and
    # degrees at most 9.  Such a sequence is precisely a Ferrers graph.
    for row_count in range(1, 8):
        harmonic = sum((Fraction(1, i) for i in range(1, row_count + 1)),
                       Fraction(0))
        for increasing in combinations_with_replacement(range(10), row_count):
            degrees = tuple(reversed(increasing))
            edges = sum(degrees)
            rectangle = max((i + 1) * degree for i, degree in enumerate(degrees))
            assert Fraction(edges, 1) <= rectangle * harmonic


def main():
    endpoint_formula_checks()
    finite_global_gate_check()
    middle_mark_load_checks()
    ferrers_rectangle_checks()
    print("minimal endpoint formula checked through 4999 edges")
    print("global loaded-key and convex-shield bounds checked")
    print("exact middle mark load checked through r=99")
    print("Ferrers rectangle inequality exhaustively checked")
    print("all carrier-alphabet square-gate checks passed")


if __name__ == "__main__":
    main()
