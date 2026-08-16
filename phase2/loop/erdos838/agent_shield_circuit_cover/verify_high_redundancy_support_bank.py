#!/usr/bin/env python3
"""Exact checks for HIGH_REDUNDANCY_SUPPORT_BANK.md."""

from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import prod
from pathlib import Path


HERE = Path(__file__).resolve().parent


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def support_data(words):
    rank = len(words[0])
    assert words and all(len(word) == rank for word in words)
    supports = [set(word[i] for word in words) for i in range(rank)]
    box = prod(map(len, supports))
    mass = len(set(words))
    assert mass == len(words) and box % mass == 0
    return supports, box, mass, box // mass


def support_arithmetic_audit():
    # Exact exponent version of M=P_0 2^{-R}.  Integer ratios are used in
    # the test cases, so no floating-point logarithms enter.
    examples = [
        [(0, 0, 0), (1, 1, 1)],
        [(a, b, (a + b) % 3) for a in range(3) for b in range(3)],
        [(a, a, b, b) for a in range(4) for b in range(2)],
    ]
    records = []
    for words in examples:
        supports, box, mass, redundancy_factor = support_data(words)
        assert mass * redundancy_factor == box
        records.append(
            {
                "support_sizes": [len(x) for x in supports],
                "box": box,
                "mass": mass,
                "two_to_R": redundancy_factor,
            }
        )

    # Integer AM--GM form: r^r product |X_i| <= (sum |X_i|)^r.
    for sizes in product(range(1, 7), repeat=4):
        assert 4**4 * prod(sizes) <= sum(sizes) ** 4

    # Coefficient rank-tax table, scaled by 64 to keep everything exact.
    # gain = max(0, eta + 1/4 - kappa).
    rows = []
    for kappa64, eta64 in ((8, 5), (16, 5), (24, 12), (32, 8)):
        gain64 = max(0, eta64 + 16 - kappa64)
        rows.append((kappa64, eta64, gain64))
    assert rows == [(8, 5, 13), (16, 5, 5), (24, 12, 4), (32, 8, 0)]
    return {"support_examples": records, "rank_tax_rows_over_64": rows}


def diagonal_parabola_audit(d=2, alphabet=3):
    rank = 3 * d
    coordinate_sets = []
    for coordinate in range(rank):
        # Disjoint, globally ordered parameter intervals.
        coordinate_sets.append(
            tuple((100 * coordinate + label, (100 * coordinate + label) ** 2)
                  for label in range(alphabet))
        )

    words = []
    for labels in product(range(alphabet), repeat=d):
        word = []
        for block, label in enumerate(labels):
            word.extend(coordinate_sets[3 * block + offset][label] for offset in range(3))
        words.append(tuple(word))

    # Every consecutive triple is positive, and indeed every increasing
    # triple from the whole support is positive on y=x^2.
    all_points = sum(coordinate_sets, ())
    ordered = sorted(all_points)
    assert all(cross(ordered[i], ordered[j], ordered[k]) > 0
               for i in range(len(ordered))
               for j in range(i + 1, len(ordered))
               for k in range(j + 1, len(ordered)))
    assert all(cross(word[i], word[i + 1], word[i + 2]) > 0
               for word in words for i in range(rank - 2))

    supports = [set(word[i] for word in words) for i in range(rank)]
    box = prod(map(len, supports))
    mass = len(words)
    assert mass == alphabet**d
    assert box == alphabet ** (3 * d) == mass**3
    assert box // mass == mass**2
    ambient_faces = 1 << len(all_points)
    assert ambient_faces >= box
    return {
        "rank": rank,
        "points": len(all_points),
        "mass": mass,
        "box": box,
        "two_to_R": box // mass,
        "ambient_faces": ambient_faces,
    }


def reed_solomon_audit(prime=5, length=4, dimension=2):
    assert length < prime and 1 <= dimension <= length
    evaluation_points = tuple(range(length))
    code = set()
    for coefficients in product(range(prime), repeat=dimension):
        word = tuple(
            sum(coefficients[j] * pow(x, j, prime) for j in range(dimension)) % prime
            for x in evaluation_points
        )
        code.add(word)
    assert len(code) == prime**dimension
    supports = [set(word[i] for word in code) for i in range(length)]
    assert all(len(support) == prime for support in supports)
    box = prime**length
    mass = len(code)
    assert box // mass == prime ** (length - dimension)

    # A separated parabola macro-realization makes every transversal an
    # ordinary positive word.  We check all p^q of them exactly.
    clusters = [
        tuple((100 * i + a, (100 * i + a) ** 2) for a in range(prime))
        for i in range(length)
    ]
    for labels in product(range(prime), repeat=length):
        word = [clusters[i][labels[i]] for i in range(length)]
        assert all(cross(word[j], word[j + 1], word[j + 2]) > 0
                   for j in range(length - 2))
    assert box == mass * prime ** (length - dimension)
    return {
        "parameters": [prime, length, dimension],
        "mass": mass,
        "box": box,
        "two_to_R": box // mass,
        "all_transversals_positive": True,
    }


def alternating_ferrers_audit():
    verifier_path = HERE / "verify_alternating_ferrers_planar_wrapper.py"
    spec = spec_from_file_location("alternating_ferrers_verifier", verifier_path)
    module = module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    base, cells = module.rational_instance()
    selected = tuple((label,) * 4 for label in range(1, 5))
    for word in selected:
        assert all(module.compatible(i, word[i], word[(i + 1) % 4]) for i in range(4))
        assert module.convex(list(base) + [cells[i][word[i] - 1] for i in range(4)])
    supports, box, mass, redundancy_factor = support_data(selected)
    assert [len(support) for support in supports] == [4, 4, 4, 4]
    assert (mass, box, redundancy_factor) == (4, 256, 64)

    exact = module.geometry_audit()
    assert exact["valid_singleton_words"] == 70
    assert exact["total_faces"] == 9722 > box
    assert exact["one_gap_layers"] == [216, 196, 216, 196]
    assert exact["opposite_complete_rectangles"] == [
        {"cells": [0, 2], "rows": 13, "columns": 13},
        {"cells": [1, 3], "rows": 13, "columns": 13},
    ]
    return {
        "selected_constant_words": mass,
        "support_box": box,
        "two_to_R": redundancy_factor,
        "valid_singleton_words": exact["valid_singleton_words"],
        "total_faces": exact["total_faces"],
        "one_gap_layers": exact["one_gap_layers"],
        "opposite_rectangles": exact["opposite_complete_rectangles"],
    }


def main():
    results = {
        "support_arithmetic": support_arithmetic_audit(),
        "diagonal_parabola": diagonal_parabola_audit(),
        "reed_solomon": reed_solomon_audit(),
        "alternating_ferrers": alternating_ferrers_audit(),
    }
    print("HIGH_REDUNDANCY_SUPPORT_BANK verifier: PASS")
    for name, result in results.items():
        print(f"{name}: {result}")


if __name__ == "__main__":
    main()
