#!/usr/bin/env python3
"""Exact verifier for the root-shield square-to-linear energy gate."""

from fractions import Fraction
from itertools import combinations
from math import comb


def pair_energy(incidences):
    """Incidences are triples (Y, bank, k), with hashable face labels."""
    weights = {}
    loads = {}
    inverse = Fraction(0)
    total = 0
    face_universe = set()
    for Y, bank, k in incidences:
        bank = tuple(bank)
        B = len(bank)
        assert B > 0
        total += k
        inverse += Fraction(k*k, B)
        face_universe.add(Y)
        face_universe.update(bank)
        for F in bank:
            pair = (Y, F)
            weights[pair] = weights.get(pair, Fraction(0)) + Fraction(k, B)
            loads[pair] = loads.get(pair, 0) + 1

    energy = sum((value*value for value in weights.values()), Fraction(0))
    max_load = max(loads.values(), default=0)
    V = len(face_universe)
    assert total*total <= V*V*energy
    assert energy <= max_load*inverse
    return total, energy, inverse, max_load, V


def abstract_equality_check():
    V = 20
    k = 37
    faces = tuple(range(V))
    incidences = [(i, faces, k) for i in faces]
    total, energy, inverse, load, actual_V = pair_energy(incidences)
    assert actual_V == V
    assert load == 1
    assert total == V*k
    assert energy == k*k
    assert inverse == k*k
    assert total*total == V*V*energy


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def build(seq):
        out = []
        for point in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    lower = build(points)
    upper = build(reversed(points))
    return lower[:-1] + upper[:-1]


def in_convex_position(points):
    return len(convex_hull(points)) == len(set(points))


def circle_point(t):
    return ((1 - t*t) / (1 + t*t), 2*t / (1 + t*t))


def planar_instance(a=2):
    radii = [Fraction(1, i + 2) for i in range(a)]
    upper = [circle_point(t) for r in radii for t in (r, 1/r)]
    lower = [circle_point(t) for r in radii for t in (-r, -1/r)]
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    z = (Fraction(0), Fraction(1))
    Q = [u, v, z] + upper + lower
    assert len(Q) == 4*a + 3
    assert in_convex_position(Q)

    # Choose an exact rational height avoiding every chord through Q.
    x = None
    for denominator in range(2, 1000):
        candidate = (Fraction(0), Fraction(1, denominator))
        if all(orient(p, q, candidate) != 0 for p, q in combinations(Q, 2)):
            x = candidate
            break
    assert x is not None
    ambient = Q + [x]
    assert all(orient(p, q, r) != 0 for p, q, r in combinations(ambient, 3))

    triangle_signs = [orient(u, v, x), orient(v, z, x), orient(z, u, x)]
    assert all(value > 0 for value in triangle_signs)

    right_side = tuple(point for point in Q
                       if point != z and orient(x, z, point) > 0)
    left_side = tuple(point for point in Q
                      if point != z and orient(x, z, point) < 0)
    assert len(right_side) == len(left_side) == 2*a + 1
    halfplane_faces = tuple(frozenset({x, z}) | frozenset(S)
                            for size in range(len(right_side) + 1)
                            for S in combinations(right_side, size))
    assert len(halfplane_faces) == 2**(2*a + 1)
    assert all(in_convex_position(list(face)) for face in halfplane_faces)

    incidences = []
    complete_sources = 0
    r = (3*a) // 2
    k = comb(3*a, r)
    for chosen in combinations(lower, a):
        B_set = frozenset({u, v}) | frozenset(chosen)
        Y = B_set | {x}
        assert in_convex_position(list(Y))
        U = [point for point in Q if point != z and point not in B_set]
        assert len(U) == 3*a
        for guard in combinations(U, r):
            source = B_set | {z} | frozenset(guard)
            assert in_convex_position(list(source))
            complete_sources += 1
        incidences.append((Y, halfplane_faces, k))

    total, energy, inverse, load, _ = pair_energy(incidences)
    N = comb(2*a, a)
    bank_size = 2**(2*a + 1)
    assert len(incidences) == N
    assert complete_sources == N*k
    assert total == N*k
    assert load == 1
    assert energy == inverse == Fraction(N*k*k, bank_size)
    return len(Q), N, k, bank_size, energy


def asymptotic_formula_check():
    for a in range(1, 101):
        N = comb(2*a, a)
        k = comb(3*a, (3*a)//2)
        B = 2**(2*a + 1)
        energy = Fraction(N*k*k, B)
        lower = Fraction(2**(6*a - 1), (2*a + 1)*(3*a + 1)**2)
        assert energy >= lower
        marked = N*k
        assert marked >= Fraction(2**(5*a), (2*a + 1)*(3*a + 1))


def main():
    abstract_equality_check()
    asymptotic_formula_check()
    q, N, k, B, energy = planar_instance(2)
    print("PASS: exact pair-energy theorem and equality abstract model")
    print("PASS: complete-middle energy formulas for 1 <= a <= 100")
    print(f"PASS: rational planar instance q={q}, cells={N}, k={k}, bank={B}")
    print(f"PASS: planar normalized energy = {energy}")


if __name__ == "__main__":
    main()
