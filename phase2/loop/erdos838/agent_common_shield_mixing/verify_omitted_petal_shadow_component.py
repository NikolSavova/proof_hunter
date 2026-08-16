#!/usr/bin/env python3
"""Exact checks for OMITTED_PETAL_SHADOW_COMPONENT.md."""

from collections import Counter, defaultdict, deque
from fractions import Fraction as F
from itertools import combinations, product
from math import comb

import verify_tangent_marked_shield_descent as tangent


def bad_four_circuits(base, support, points):
    ground = tuple(sorted(set(base) | set(support)))
    return [C for C in combinations(ground, 4)
            if not tangent.convex([points[i] for i in C])]


def relative_graph(base, containers, points):
    support = set().union(*containers.values()) if containers else set()
    graph = {i: set() for i in containers}
    witnesses = {}
    for C in bad_four_circuits(base, support, points):
        used = [i for i, X in containers.items() if set(C) & set(X)]
        for i, j in combinations(used, 2):
            graph[i].add(j)
            graph[j].add(i)
            witnesses.setdefault(tuple(sorted((i, j))), C)
    return graph, witnesses


def components(graph):
    ans = []
    unseen = set(graph)
    while unseen:
        root = next(iter(unseen))
        seen = {root}
        queue = deque([root])
        while queue:
            i = queue.popleft()
            for j in graph[i] - seen:
                seen.add(j)
                queue.append(j)
        ans.append(seen)
        unseen -= seen
    return ans


def relative_link_faces(base, support, points):
    support = tuple(sorted(support))
    return [E for r in range(len(support) + 1)
            for E in combinations(support, r)
            if tangent.convex([points[i] for i in tuple(base) + E])]


def check_relative_join_exhaustively():
    # A square plus a generic interior point: nontrivial links and circuits.
    points = [(F(-4), F(-4)), (F(4), F(-4)), (F(4), F(4)),
              (F(-4), F(4)), (F(0), F(1))]
    assert all(tangent.cross(*T) != 0 for T in combinations(points, 3))
    all_indices = set(range(len(points)))
    checked = 0
    for r in range(len(points) + 1):
        for base in combinations(range(len(points)), r):
            if not tangent.convex([points[i] for i in base]):
                continue
            Z = all_indices - set(base)
            containers = {i: {i} for i in Z}
            graph, _ = relative_graph(base, containers, points)
            comps = components(graph)
            global_count = len(relative_link_faces(base, Z, points))
            product_count = 1
            for comp in comps:
                support = set().union(*(containers[i] for i in comp))
                product_count *= len(relative_link_faces(base, support, points))
            assert global_count == product_count

            # Stronger setwise join audit.
            local_lists = []
            for comp in comps:
                support = set().union(*(containers[i] for i in comp))
                local_lists.append(relative_link_faces(base, support, points))
            joined = {
                tuple(sorted(set().union(*(set(E) for E in choices))))
                for choices in product(*local_lists)
            } if local_lists else {()}
            actual = set(relative_link_faces(base, Z, points))
            assert joined == actual
            checked += 1
    return checked


def check_weighted_shadow_identities():
    universe = range(8)
    petals = list(combinations(universe, 4))
    # A deliberately irregular weighted subfamily.
    family = [(D, F((7 * i) % 11 + 1, (i % 3) + 1))
              for i, D in enumerate(petals) if (sum(D) + i) % 4 != 0]
    checks = 0
    W = sum((w for _, w in family), F(0))
    for k in range(5):
        degree = defaultdict(F)
        for D, w in family:
            for I in combinations(D, k):
                degree[I] += w
        first = sum(degree.values(), F(0))
        second = sum((x * x for x in degree.values()), F(0))
        rhs = F(0)
        for D, w in family:
            for E, z in family:
                rhs += w * z * comb(len(set(D) & set(E)), k)
        assert first == comb(4, k) * W
        assert second == rhs
        Lambda = max(degree.values())
        assert first <= Lambda * len(degree)
        checks += 1
    return len(family), checks


def check_product_formula():
    checks = 0
    for t in range(1, 8):
        for L in range(2, 6):
            M = L ** t
            for k in range(t + 1):
                outputs = comb(t, k) * L ** k
                degree = L ** (t - k)
                incidences = outputs * degree
                square = outputs * degree * degree
                assert incidences == M * comb(t, k)
                assert square * L ** k == M * M * comb(t, k)
                checks += 1
    return checks


def check_rational_barrier():
    blocks, repairs, points = tangent.configuration()
    bit_words = list(product(range(2), repeat=8))
    fixed_words = [bits for bits in bit_words
                   if bits[7] == bits[0] == bits[1] == bits[2] == 0]
    completions = [tangent.completion_indices(bits) for bits in fixed_words]
    base = frozenset((14, 0, 2, 4))
    petals = [frozenset(set(Q) - set(base)) for Q in completions]
    assert len(petals) == len(set(petals)) == 16
    assert all(len(D) == 4 for D in petals)
    assert all(tangent.convex([points[i] for i in set(base) | set(D)])
               for D in petals)

    # The actual marked repair occurrence and shield remain fixed.
    mark = 16
    shield = frozenset((16, 18, 19))
    assert tangent.convex([points[i] for i in shield])
    for D in petals:
        star = tuple(sorted(set(base) | set(D) | {mark}))
        assert tangent.convex([points[i] for i in star])
        assert not tangent.convex([points[i] for i in set(star) | set(shield)])

    levels = []
    M = len(petals)
    for k in range(5):
        degree = Counter()
        for D in petals:
            for I in combinations(sorted(D), k):
                degree[frozenset(I)] += 1
        incidences = sum(degree.values())
        square = sum(d * d for d in degree.values())
        expected_outputs = comb(4, k) * 2 ** k
        expected_degree = 2 ** (4 - k)
        assert incidences == M * comb(4, k)
        assert len(degree) == expected_outputs
        assert set(degree.values()) == {expected_degree}
        assert square == M * M * comb(4, k) // 2 ** k
        levels.append((k, incidences, len(degree), expected_degree, square))
    assert levels[2] == (2, 96, 24, 4, 384)

    # Relative graph on all four variable containers is complete, even
    # though the paying construction is a four-coordinate product.
    containers = {i: {2 * i, 2 * i + 1} for i in range(3, 7)}
    graph, witnesses = relative_graph(base, containers, points)
    assert all(graph[i] == set(containers) - {i} for i in containers)
    assert len(witnesses) == comb(4, 2)

    # A literal central heavy child: fix the outer values in blocks 3,4;
    # blocks 5,6 remain as a connected rank-two product of four petals.
    fixed_I = frozenset((6, 8))
    child = [D - fixed_I for D in petals if fixed_I <= D]
    assert len(child) == 4 and len(set(child)) == 4
    child_base = base | fixed_I
    assert all(len(E) == 2 for E in child)
    assert all(tangent.convex([points[i] for i in child_base | E]) for E in child)
    assert all(not tangent.convex([points[i] for i in child_base | E | G])
               for E, G in combinations(child, 2))
    child_containers = {i: {2 * i, 2 * i + 1} for i in (5, 6)}
    child_graph, child_witnesses = relative_graph(child_base, child_containers, points)
    assert child_graph[5] == {6} and child_graph[6] == {5}
    assert (5, 6) in child_witnesses

    # Every bad circuit between two child carriers crosses both petal
    # differences; audit existence exhaustively.
    cross_checks = 0
    for E, G in combinations(child, 2):
        union = child_base | E | G
        circuits = bad_four_circuits(child_base, E | G, points)
        crossing = [C for C in circuits
                    if set(C) & (E - G) and set(C) & (G - E)]
        assert crossing
        assert not tangent.convex([points[i] for i in union])
        cross_checks += 1
    return levels, len(witnesses), len(child), cross_checks


def main():
    joins = check_relative_join_exhaustively()
    weighted = check_weighted_shadow_identities()
    formula = check_product_formula()
    barrier = check_rational_barrier()
    print(
        "omitted petal shadow/component: PASS; "
        f"relative_join_bases={joins}; weighted={weighted}; "
        f"product_formulas={formula}; barrier={barrier}"
    )


if __name__ == "__main__":
    main()
