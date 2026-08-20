#!/usr/bin/env python3
"""Exact checks for AMBIENT_CENTROID_ENDPOINT_DIFFERENCE_HYPERGRAPH_GATE.md."""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import comb, gcd
from fractions import Fraction

Point = tuple[int, int]
Edge = tuple[int, int]


def add(*points: Point) -> Point:
    return (sum(p[0] for p in points), sum(p[1] for p in points))


def sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def norm2(v: Point) -> int:
    return v[0] * v[0] + v[1] * v[1]


def residue_parabola(p: int) -> list[Point]:
    return [(x, (x * x) % p) for x in range(p)]


def shear(points: list[Point], t: int) -> list[Point]:
    return [(x + t * y, y) for x, y in points]


def is_distance_sidon(points: list[Point]) -> bool:
    values = [norm2(sub(points[j], points[i])) for i, j in combinations(range(len(points)), 2)]
    return len(values) == len(set(values))


def is_vector_sidon_integer(points: list[Point]) -> bool:
    seen: dict[Point, Edge] = {}
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            d = sub(points[j], points[i])
            if d in seen and seen[d] != (i, j):
                return False
            seen[d] = (i, j)
    return True


def is_vector_sidon_mod(points: list[Point], p: int) -> bool:
    seen: dict[Point, Edge] = {}
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            d = ((points[j][0] - points[i][0]) % p, (points[j][1] - points[i][1]) % p)
            if d in seen and seen[d] != (i, j):
                return False
            seen[d] = (i, j)
    return True


def triple_loads(points: list[Point], modulus: int | None = None) -> Counter[Point]:
    loads: Counter[Point] = Counter()
    for triple in combinations(range(len(points)), 3):
        s = add(*(points[i] for i in triple))
        if modulus is not None:
            s = (s[0] % modulus, s[1] % modulus)
        loads[s] += 1
    return loads


def triple_cells(points: list[Point]) -> defaultdict[Point, list[tuple[int, int, int]]]:
    cells: defaultdict[Point, list[tuple[int, int, int]]] = defaultdict(list)
    for triple in combinations(range(len(points)), 3):
        cells[add(*(points[i] for i in triple))].append(triple)
    return cells


def centroid_matching_determinant_profile(points: list[Point]) -> Counter[int]:
    profile: Counter[int] = Counter()
    for triples in triple_cells(points).values():
        for source in triples:
            for target in triples:
                if source == target:
                    continue
                for permuted_target in permutations(target):
                    q1 = sub(points[permuted_target[0]], points[source[0]])
                    q2 = sub(points[permuted_target[1]], points[source[1]])
                    profile[abs(q1[0] * q2[1] - q1[1] * q2[0])] += 1
    return profile


def ordered_distinct_triangle_pairs(loads: Counter[Point]) -> int:
    return sum(v * (v - 1) for v in loads.values())


def directed_edges(points: list[Point]) -> tuple[list[Edge], dict[Point, Edge]]:
    edges: list[Edge] = []
    by_delta: dict[Point, Edge] = {}
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            e = (i, j)
            d = sub(points[j], points[i])
            assert d not in by_delta
            by_delta[d] = e
            edges.append(e)
    return edges, by_delta


def endpoint_hyperedges(points: list[Point]) -> set[frozenset[Edge]]:
    edges, by_delta = directed_edges(points)
    result: set[frozenset[Edge]] = set()
    # Two vertices force the third.  This also avoids a cubic scan in |E|.
    for index, e1 in enumerate(edges):
        d1 = sub(points[e1[1]], points[e1[0]])
        for e2 in edges[index + 1 :]:
            d2 = sub(points[e2[1]], points[e2[0]])
            e3 = by_delta.get((-d1[0] - d2[0], -d1[1] - d2[1]))
            if e3 is None or e3 == e1 or e3 == e2:
                continue
            endpoints = e1 + e2 + e3
            if len(set(endpoints)) != 6:
                continue
            result.add(frozenset((e1, e2, e3)))
    return result


def check_linearity_and_links(points: list[Point], hyperedges: set[frozenset[Edge]]) -> None:
    pair_codegree: Counter[frozenset[Edge]] = Counter()
    links: defaultdict[Edge, list[tuple[frozenset[int], frozenset[int]]]] = defaultdict(list)
    for h in hyperedges:
        edge_list = list(h)
        for pair in combinations(edge_list, 2):
            pair_codegree[frozenset(pair)] += 1
        for e in edge_list:
            others = [f for f in edge_list if f != e]
            sources = frozenset((others[0][0], others[1][0]))
            targets = frozenset((others[0][1], others[1][1]))
            links[e].append((sources, targets))
    assert max(pair_codegree.values(), default=0) <= 1
    for entries in links.values():
        source_loads = Counter(source for source, _ in entries)
        target_loads = Counter(target for _, target in entries)
        assert max(source_loads.values(), default=0) <= 2
        assert max(target_loads.values(), default=0) <= 2
        assert len(entries) <= 2 * comb(len(points) - 2, 2)


def ordered_zero_sum_profile(points: list[Point]) -> tuple[int, int]:
    edges, by_delta = directed_edges(points)
    total = 0
    clean = 0
    for e1 in edges:
        d1 = sub(points[e1[1]], points[e1[0]])
        for e2 in edges:
            d2 = sub(points[e2[1]], points[e2[0]])
            e3 = by_delta.get((-d1[0] - d2[0], -d1[1] - d2[1]))
            if e3 is None:
                continue
            total += 1
            if len(set(e1 + e2 + e3)) == 6:
                clean += 1
    return total, clean


def coordinate_height(points: list[Point]) -> int:
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return max(max(xs) - min(xs), max(ys) - min(ys))


def primitive_unoriented(v: Point) -> Point:
    g = gcd(abs(v[0]), abs(v[1]))
    w = (v[0] // g, v[1] // g)
    if w[0] < 0 or (w[0] == 0 and w[1] < 0):
        w = (-w[0], -w[1])
    return w


def direction_occupancies(points: list[Point]) -> Counter[Point]:
    occupancies: Counter[Point] = Counter()
    for i, j in combinations(range(len(points)), 2):
        occupancies[primitive_unoriented(sub(points[j], points[i]))] += 1
    return occupancies


def collinear_hyperedge_count(points: list[Point], hyperedges: set[frozenset[Edge]]) -> int:
    count = 0
    for hyperedge in hyperedges:
        e1, e2, _ = tuple(hyperedge)
        q1 = sub(points[e1[1]], points[e1[0]])
        q2 = sub(points[e2[1]], points[e2[0]])
        if q1[0] * q2[1] == q1[1] * q2[0]:
            count += 1
    return count


def check_collinear_budget(points: list[Point], hyperedges: set[frozenset[Edge]]) -> tuple[int, int]:
    occupancies = direction_occupancies(points)
    collinear = collinear_hyperedge_count(points, hyperedges)
    square_energy = sum(value * value for value in occupancies.values())
    assert 3 * collinear <= 2 * square_energy

    M = coordinate_height(points)
    harmonic = sum((Fraction(1, q) for q in range(1, M + 1)), Fraction())
    assert Fraction(square_energy) <= 4 * M * M * harmonic
    return collinear, square_energy


def hyperedge_abs_determinant(points: list[Point], hyperedge: frozenset[Edge]) -> int:
    e1, e2, e3 = tuple(hyperedge)
    q1 = sub(points[e1[1]], points[e1[0]])
    q2 = sub(points[e2[1]], points[e2[0]])
    q3 = sub(points[e3[1]], points[e3[0]])
    determinants = {
        abs(q1[0] * q2[1] - q1[1] * q2[0]),
        abs(q2[0] * q3[1] - q2[1] * q3[0]),
        abs(q3[0] * q1[1] - q3[1] * q1[0]),
    }
    assert len(determinants) == 1
    return determinants.pop()


def check_low_determinant_budget(
    points: list[Point],
    hyperedges: set[frozenset[Edge]],
    cutoff: int,
) -> tuple[int, int]:
    M = coordinate_height(points)
    low_count = sum(
        0 < hyperedge_abs_determinant(points, hyperedge) <= cutoff
        for hyperedge in hyperedges
    )

    # Exact integer version of the lattice-coset envelope before the
    # reciprocal-norm relaxation in the note.
    ordered_pair_envelope = 0
    reciprocal_sup = Fraction()
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            q = sub(points[j], points[i])
            content = gcd(abs(q[0]), abs(q[1]))
            primitive = (q[0] // content, q[1] // content)
            primitive_sup = max(abs(primitive[0]), abs(primitive[1]))
            determinant_count = 2 * (cutoff // content)
            ordered_pair_envelope += determinant_count * (
                1 + (2 * M) // primitive_sup
            )
            reciprocal_sup += Fraction(1, max(abs(q[0]), abs(q[1])))

    assert 6 * low_count <= ordered_pair_envelope
    assert reciprocal_sup <= 4 * len(points)
    coarse = 2 * cutoff * len(points) * (len(points) - 1)
    coarse += 4 * cutoff * M * reciprocal_sup
    assert ordered_pair_envelope <= coarse
    return low_count, ordered_pair_envelope


def main() -> None:
    expected = {
        7: (4, 14, 4, 21),
        11: (24, 110, 6, 62),
        13: (66, 312, 6, 80),
        17: (232, 1_088, 11, 189),
        19: (538, 1_938, 10, 183),
        23: (1_442, 4_554, 13, 249),
        29: (3_316, 12_992, 14, 409),
        43: (21_142, 72_842, 28, 1_175),
    }

    for p, (integer_pairs, modular_pairs, first_t, height) in expected.items():
        base = residue_parabola(p)
        assert is_vector_sidon_integer(base)
        assert is_vector_sidon_mod(base, p)
        actual_integer = ordered_distinct_triangle_pairs(triple_loads(base))
        actual_modular = ordered_distinct_triangle_pairs(triple_loads(base, p))
        assert (actual_integer, actual_modular) == (integer_pairs, modular_pairs)
        assert all(not is_distance_sidon(shear(base, t)) for t in range(first_t))
        transformed = shear(base, first_t)
        assert is_distance_sidon(transformed)
        assert coordinate_height(transformed) == height
        # An invertible linear map preserves exact integer triple sums.
        assert ordered_distinct_triangle_pairs(triple_loads(transformed)) == integer_pairs

    # The smallest nontrivial genuine certificate is cheap enough for a
    # direct hypergraph construction and all factor checks.
    points = shear(residue_parabola(7), 4)
    loads = triple_loads(points)
    pair_count = ordered_distinct_triangle_pairs(loads)
    hyperedges = endpoint_hyperedges(points)
    assert pair_count == 4
    assert len(hyperedges) == 6 * pair_count == 24
    check_linearity_and_links(points, hyperedges)
    collinear, direction_energy = check_collinear_budget(points, hyperedges)
    low_profiles = {
        cutoff: check_low_determinant_budget(points, hyperedges, cutoff)
        for cutoff in (1, 3, 10, 21)
    }

    total, clean = ordered_zero_sum_profile(points)
    assert clean == 6 * len(hyperedges) == 144
    assert clean == 36 * pair_count
    assert total - clean <= 30 * len(points) ** 3

    # A genuine one-dimensional Golomb ruler puts the full hypergraph in
    # the collinear branch and is paid for by the same directional budget.
    ruler = [(x, 0) for x in (0, 1, 4, 10, 12, 17)]
    assert is_distance_sidon(ruler)
    ruler_hyperedges = endpoint_hyperedges(ruler)
    ruler_collinear, ruler_direction_energy = check_collinear_budget(ruler, ruler_hyperedges)
    assert ruler_collinear == len(ruler_hyperedges)
    assert ruler_direction_energy == comb(len(ruler), 2) ** 2
    assert check_low_determinant_budget(ruler, ruler_hyperedges, 17)[0] == 0

    # The Cauchy lower bound in the finite-field model is exact as an
    # inequality (although weak for small p).
    p = 43
    modular_loads = triple_loads(residue_parabola(p), p)
    R = comb(p, 3)
    lhs = ordered_distinct_triangle_pairs(modular_loads)
    assert lhs * p * p >= R * R - R * p * p

    parabola_43 = shear(residue_parabola(43), 28)
    determinant_profile = centroid_matching_determinant_profile(parabola_43)
    assert sum(determinant_profile.values()) == 126_852
    assert len(determinant_profile) == 1_060
    assert determinant_profile[0] == 390
    assert max(determinant_profile.values()) == 774
    assert sum(load for d, load in determinant_profile.items() if 0 < d <= 10) == 5_278

    print("ambient centroid endpoint difference hypergraph gate: PASS")
    print("p=7 exact: pair_count=4, |H|=24, ordered_clean=144")
    print(f"p=7 collinear branch: |H_col|={collinear}, sum_e2={direction_energy}")
    print("p=7 low-determinant profiles:", low_profiles)
    print(
        "Golomb ruler branch:",
        f"|H|={len(ruler_hyperedges)}, sum_e2={ruler_direction_energy}",
    )
    print("p=43 lift: pair_count=21142, |H|=126852, t=28, m=1175")
    print("p=43 determinant profile: zero=390, low<=10=5278, support=1060, max=774")


if __name__ == "__main__":
    main()
