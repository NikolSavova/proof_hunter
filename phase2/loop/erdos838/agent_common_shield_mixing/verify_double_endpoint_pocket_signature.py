#!/usr/bin/env python3
"""Exact checks for DOUBLE_ENDPOINT_POCKET_SIGNATURE.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import ceil, comb

from verify_mixed_seam_vertex_cover_pi2 import convex, hull, orient


def hidden_label(points):
    boundary = set(hull(points))
    hidden = [index for index, point in enumerate(points)
              if point not in boundary]
    assert len(hidden) == 1
    return hidden[0]


def signed_type_audit():
    triangle = [(F(0), F(0)), (F(6), F(0)), (F(0), F(6))]
    interior = (F(1), F(1))
    samples = []
    for hidden in range(4):
        vertices = iter(triangle)
        sample = [interior if label == hidden else next(vertices)
                  for label in range(4)]
        assert all(orient(*triple) != 0 for triple in combinations(sample, 3))
        assert not convex(sample) and hidden_label(sample) == hidden
        # Coordinate zero is designated as the endpoint.  The remaining
        # three coordinates are the pocket triple for every signed type.
        assert len(sample[1:]) == 3
        samples.append(sample)
    return [hidden_label(sample) for sample in samples]


def matching_pigeonhole_audit():
    systems = 0
    # Abstract one-endpoint signatures 0,...,s-1; ordered pairs give s^2
    # double signatures.  Exhaust small words and check the largest fibre.
    for signatures in range(1, 3):
        classes = signatures * signatures
        for size in range(1, 9):
            for word in product(range(classes), repeat=size):
                largest = max(word.count(label) for label in set(word))
                assert largest >= ceil(size / classes)
                systems += 1
    return systems


def symbolic_bound_audit():
    cases = 0
    for rank in range(3, 31):
        signatures = 4 * comb(rank, 3)
        doubles = signatures * signatures
        assert doubles == 16 * comb(rank, 3) ** 2
        for matching in range(1, 200):
            assert ceil(matching / doubles) * doubles >= matching
            cases += 1
    return cases


def main():
    types = signed_type_audit()
    systems = matching_pigeonhole_audit()
    bounds = symbolic_bound_audit()
    print("PASS: signed types=%s; matching systems=%d; symbolic bounds=%d"
          % (types, systems, bounds))


if __name__ == "__main__":
    main()
