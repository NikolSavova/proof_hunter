#!/usr/bin/env python3
"""Exact verifier for the marked root--shield halfplane bank."""

from fractions import Fraction
from itertools import combinations


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


def all_subsets(items):
    items = list(items)
    for mask in range(1 << len(items)):
        yield [items[i] for i in range(len(items)) if (mask >> i) & 1]


def geometric_check():
    # Eleven points on y=x^2 are in strictly convex position.
    Q = [(Fraction(t), Fraction(t*t)) for t in range(-5, 6)]
    u, z, v = Q[0], Q[5], Q[-1]
    x = tuple((u[k] + v[k] + z[k]) / 3 for k in range(2))

    assert in_convex_position(Q)
    assert orient(u, v, z) != 0
    signs = [orient(u, v, x), orient(v, z, x), orient(z, u, x)]
    assert all(value < 0 for value in signs)

    # Full general position after x is inserted.
    ambient = Q + [x]
    for a, b, c in combinations(ambient, 3):
        assert orient(a, b, c) != 0

    sides = {1: [], -1: []}
    for point in Q:
        if point == z:
            continue
        value = orient(x, z, point)
        assert value != 0
        sides[1 if value > 0 else -1].append(point)

    assert sorted(map(len, sides.values())) == [5, 5]
    checked = 0
    for side in sides.values():
        for subset in all_subsets(side):
            assert in_convex_position([x, z] + subset)
            checked += 1
    return len(Q), checked


def decoder_check():
    # Abstract canonical incidences.  A cell is determined by (B,z,e), and
    # can emit several completions Y=B+{x}.  H is chosen inside B to force
    # substantial output collisions.
    base = tuple(range(6))
    roots = tuple(range(10, 14))
    b = 3
    q = 5

    occurrences = []
    seen_cell_data = {}
    completions = set()
    for Y_tuple in combinations(base, b + 1):
        Y = frozenset(Y_tuple)
        completions.add(Y)
        for x in Y:
            B = frozenset(Y - {x})
            H = tuple(sorted(B))
            for z in roots:
                for e_tuple in combinations(sorted(B), 2):
                    e = frozenset(e_tuple)
                    cell = (B, z, e)
                    seen_cell_data[cell] = cell
                    for S_tuple in all_subsets(H):
                        S = frozenset(S_tuple)
                        F = frozenset({x, z}) | S
                        occurrences.append((Y, F, x, z, e, cell, S))

    pair_fibres = {}
    profile_fibres = {}
    for record in occurrences:
        Y, F, x, z, e, cell, S = record
        assert x in Y & F
        assert z in F - Y
        assert cell == (Y - {x}, z, e)
        assert S == F - {x, z}
        pair_fibres.setdefault((Y, F), []).append(record)
        profile_fibres.setdefault((x, z, F), []).append(record)

    pair_cap = (q*q // 4) * (b*(b - 1) // 2)
    assert max(map(len, pair_fibres.values())) <= pair_cap

    edge_cap = b*(b - 1) // 2
    for fibre in profile_fibres.values():
        by_completion = {}
        for record in fibre:
            by_completion.setdefault(record[0], 0)
            by_completion[record[0]] += 1
        assert max(by_completion.values()) <= edge_cap

    # Direct global pair count with its exact decoder multiplicity.
    assert len(occurrences) <= pair_cap * len(pair_fibres)
    return len(occurrences), len(pair_fibres), max(map(len, pair_fibres.values()))


def main():
    q_size, geometric_subsets = geometric_check()
    occurrences, pairs, max_fibre = decoder_check()
    print(f"PASS: exact halfplane bank on a {q_size}-point convex polygon")
    print(f"PASS: all {geometric_subsets} subsets from the two marked sides")
    print(f"PASS: {occurrences} abstract marked occurrences, {pairs} output pairs")
    print(f"PASS: maximum pair fibre {max_fibre} obeys the exact decoder cap")


if __name__ == "__main__":
    main()
