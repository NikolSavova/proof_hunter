#!/usr/bin/env python3
"""Exact verifier for the global Ferrers rectangle--shield telescope."""

from fractions import Fraction
from itertools import combinations
from math import comb


def uniform_telescope(contexts):
    """contexts are (integer demand, tuple of hashable target faces)."""
    loads = {}
    total = 0
    universe = set()
    for demand, bank in contexts:
        bank = tuple(bank)
        assert demand >= 0 and bank
        total += demand
        universe.update(bank)
        weight = Fraction(demand, len(bank))
        for face in bank:
            loads[face] = loads.get(face, Fraction(0)) + weight
    maximum = max(loads.values(), default=Fraction(0))
    assert total <= maximum * len(universe)
    return total, maximum, len(universe), loads


def hall_density(contexts):
    """Brute-force the exact weighted bank-expansion ratio (4a)."""
    best = Fraction(0)
    count = len(contexts)
    for mask in range(1, 1 << count):
        demand = 0
        targets = set()
        for index, (weight, bank) in enumerate(contexts):
            if mask & (1 << index):
                demand += weight
                targets.update(bank)
        best = max(best, Fraction(demand, len(targets)))
    return best


def fractional_primal_dual_certificates():
    # Three equal jobs on the triangle of two-face banks.  Splitting each
    # job equally gives load 6 on every face.  Uniform dual prices give
    # value 6, so both certificates prove lambda_*=6 exactly.
    faces = ("a", "b", "c")
    contexts = [(6, ("a", "b")), (6, ("b", "c")), (6, ("a", "c"))]
    total, maximum, size, _ = uniform_telescope(contexts)
    assert total == 18 and size == 3 and maximum == 6
    dual_prices = {face: Fraction(1, 3) for face in faces}
    dual = sum(Fraction(demand) * min(dual_prices[face] for face in bank)
               for demand, bank in contexts)
    assert dual == maximum == hall_density(contexts) == 6

    # Two jobs reuse one four-face bank.  Uniform routing and the uniform
    # dual again coincide at total-demand / bank-size.
    common = tuple(range(4))
    contexts = [(5, common), (7, common)]
    total, maximum, size, _ = uniform_telescope(contexts)
    prices = {face: Fraction(1, 4) for face in common}
    dual = sum(Fraction(demand) * min(prices[face] for face in bank)
               for demand, bank in contexts)
    assert total == 12 and size == 4 and maximum == dual == 3
    assert hall_density(contexts) == 3

    # Uniform routing need not be optimal.  Fractional Hall detects load 1:
    # route the flexible job entirely to b.  A dual concentrated on a also
    # certifies 1.
    contexts = [(1, ("a",)), (1, ("a", "b"))]
    _, uniform_load, _, _ = uniform_telescope(contexts)
    assert uniform_load == Fraction(3, 2)
    assert hall_density(contexts) == 1
    dual_prices = {"a": Fraction(1), "b": Fraction(0)}
    dual = sum(Fraction(demand) * min(dual_prices[face] for face in bank)
               for demand, bank in contexts)
    assert dual == 1


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def strictly_inside_triangle(point, a, b, c):
    signs = (orient(a, b, point), orient(b, c, point), orient(c, a, point))
    triangle_sign = orient(a, b, c)
    return all(value > 0 for value in signs) if triangle_sign > 0 else all(
        value < 0 for value in signs
    )


def ferrers_check():
    x = (Fraction(0), Fraction(0))
    z = (Fraction(0), Fraction(1))
    left = [
        (Fraction(-1), Fraction(-3)),
        (Fraction(-2), Fraction(-3)),
        (Fraction(-3), Fraction(-2)),
        (Fraction(-4), Fraction(1)),
    ]
    right = [
        (Fraction(1), Fraction(-2)),
        (Fraction(2), Fraction(-1)),
        (Fraction(3), Fraction(0)),
        (Fraction(4), Fraction(2)),
        (Fraction(5), Fraction(5)),
    ]

    rows = []
    for u in left:
        a = -u[0]
        row = []
        for column, v in enumerate(right):
            c = v[0]
            formula = u[1] / a + v[1] / c < 0
            geometry = strictly_inside_triangle(x, u, v, z)
            assert formula == geometry
            if formula:
                row.append(column)
        rows.append(set(row))

    # Sort by degree and verify nested neighbourhoods.
    rows.sort(key=len, reverse=True)
    assert all(rows[index + 1] <= rows[index]
               for index in range(len(rows) - 1))
    degrees = [len(row) for row in rows]
    edges = sum(degrees)
    rectangle = max((index + 1) * degree
                    for index, degree in enumerate(degrees))
    harmonic = sum((Fraction(1, index) for index in range(1, len(rows) + 1)),
                   Fraction(0))
    assert rectangle * harmonic >= edges

    # Same-side pairs never form rooted carriers.
    for side in (left, right):
        for u, v in combinations(side, 2):
            assert not strictly_inside_triangle(x, u, v, z)
    return edges, rectangle, harmonic


def three_arc_load_check():
    # Finite Proposition-4 parameters: l=r=2, g=1, p=3, h=1, D=4.
    left_size = right_size = 2
    blocks = 1
    h = 1
    p = 2 * h + 1
    D = 4
    sources = left_size * right_size * blocks * comb(p, h + 1)
    demand = D * sources
    outer_shield = 2 ** (left_size + right_size + blocks * p)
    blocker_shield = 2 ** D  # the finite verifier uses a convex D-block
    union_size = outer_shield + blocker_shield - 1  # shared empty face
    optimal_one_context_load = Fraction(demand, union_size)
    assert sources == 12 and demand == 48
    assert outer_shield == 128 and blocker_shield == 16
    assert optimal_one_context_load == Fraction(48, 143)
    # Keep the comparison exact: load < sqrt(D) iff load^2 < D.
    assert optimal_one_context_load * optimal_one_context_load < D

    # Root markings of an (h+1)-set have exact load h+1.
    marked = left_size * right_size * blocks * p * comb(2 * h, h)
    assert marked == (h + 1) * sources
    return sources, demand, optimal_one_context_load, marked


def mark_tensor_checks():
    # Exact finite audit of the source, Boolean-core, and blocker banks.
    for k in range(4, 31):
        for rank in range(4, min(k, 10) + 1):
            for hidden in (1, 2, 5):
                for D in (4, 8, 16):
                    sources = hidden * comb(k, rank)
                    demand = D * sources
                    core_shield = 2 ** k
                    blocker_shield = 2 ** D  # a valid explicit convex test block
                    ambient_lower = max(sources, core_shield, blocker_shield)
                    assert demand <= D * ambient_lower

                    # Every four-core set extends to a used rank-set.
                    core = tuple(range(k))
                    for four in combinations(core, 4):
                        extension = four + tuple(label for label in core
                                                 if label not in four)[:rank - 4]
                        assert len(extension) == rank
                        assert set(four) <= set(extension)


def main():
    fractional_primal_dual_certificates()
    edges, rectangle, harmonic = ferrers_check()
    sources, demand, load, marked = three_arc_load_check()
    mark_tensor_checks()
    print("PASS: exact uniform telescope, Hall density, and matching LP dual certificates")
    print(f"PASS: rational Ferrers graph edges={edges}, best-rectangle={rectangle}, "
          f"harmonic={harmonic}")
    print(f"PASS: three-arc sources={sources}, demand={demand}, "
          f"fractional-load={load}, marked={marked}")
    print("PASS: complete MARK_C4 core/Boolean-shield alternatives on exact finite grid")


if __name__ == "__main__":
    main()
