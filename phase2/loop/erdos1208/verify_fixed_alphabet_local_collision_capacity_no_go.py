#!/usr/bin/env python3
"""Verifier for the fixed-alphabet local-collision capacity barrier."""

from __future__ import annotations

from collections import defaultdict, deque
from itertools import product


G = tuple[int, int]
Poly = tuple[G, ...]
Word = tuple[G, ...]


ZERO: G = (0, 0)
ONE: G = (1, 0)
I: G = (0, 1)
UNITS: tuple[G, ...] = ((1, 0), (-1, 0), (0, 1), (0, -1))


def gadd(a: G, b: G) -> G:
    return a[0] + b[0], a[1] + b[1]


def gsub(a: G, b: G) -> G:
    return a[0] - b[0], a[1] - b[1]


def gmul(a: G, b: G) -> G:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def gconj(a: G) -> G:
    return a[0], -a[1]


def trim(a: list[G] | tuple[G, ...]) -> Poly:
    out = list(a)
    while len(out) > 1 and out[-1] == ZERO:
        out.pop()
    return tuple(out) if out else (ZERO,)


def padd(a: Poly, b: Poly) -> Poly:
    out = [ZERO] * max(len(a), len(b))
    for j in range(len(out)):
        out[j] = gadd(a[j] if j < len(a) else ZERO, b[j] if j < len(b) else ZERO)
    return trim(out)


def pmul(a: Poly, b: Poly) -> Poly:
    out = [ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = gadd(out[i + j], gmul(x, y))
    return trim(out)


def pconj(a: Poly) -> Poly:
    return trim([gconj(x) for x in a])


def pscale(unit: G, a: Poly) -> Poly:
    return trim([gmul(unit, x) for x in a])


def pshift(a: Poly, amount: int) -> Poly:
    return trim([ZERO] * amount + list(a))


def norm(a: Poly) -> Poly:
    return pmul(a, pconj(a))


def append_block(low: Poly, high: Poly, shift: int) -> Poly:
    return padd(low, pshift(high, shift))


def word_difference(x: Word, y: Word) -> Poly:
    return trim([gsub(a, b) for a, b in zip(x, y)])


def color(x: Word, y: Word) -> Poly:
    return norm(word_difference(x, y))


def additive_energy(p: tuple[G, ...]) -> int:
    counts: dict[G, int] = defaultdict(int)
    for a in p:
        for b in p:
            counts[gsub(a, b)] += 1
    return sum(v * v for v in counts.values())


def maximum_rainbow(points: list[Word]) -> tuple[int, list[int]]:
    n = len(points)
    colors: list[list[Poly | None]] = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(i):
            colors[i][j] = colors[j][i] = color(points[i], points[j])

    best: list[int] = []

    def rec(candidates: list[int], chosen: list[int], used: frozenset[Poly]) -> None:
        nonlocal best
        if len(chosen) + len(candidates) <= len(best):
            return
        if len(chosen) > len(best):
            best = chosen[:]
        while candidates:
            if len(chosen) + len(candidates) <= len(best):
                return
            v = candidates.pop()
            new_colors = [colors[v][u] for u in chosen]
            assert all(c is not None for c in new_colors)
            actual = [c for c in new_colors if c is not None]
            if len(set(actual)) != len(actual) or any(c in used for c in actual):
                continue
            next_candidates: list[int] = []
            forbidden = used.union(actual)
            for w in candidates:
                vw = colors[v][w]
                assert vw is not None
                if vw in forbidden:
                    continue
                # When w is added later, its edges to the old chosen set and
                # to v must already have distinct colors.
                old = [colors[w][u] for u in chosen]
                if vw in old:
                    continue
                next_candidates.append(w)
            rec(next_candidates, chosen + [v], frozenset(forbidden))

    rec(list(range(n)), [], frozenset())
    return len(best), best


def max_ap_length(p: tuple[G, ...]) -> int:
    ps = set(p)
    best = 1
    for x in p:
        for y in p:
            if x == y:
                continue
            d = gsub(y, x)
            length = 1
            z = x
            while gadd(z, d) in ps:
                z = gadd(z, d)
                length += 1
            best = max(best, length)
    return best


def translation_component_bound(p: tuple[G, ...], r: int) -> int:
    words = list(product(p, repeat=r))
    index = {w: j for j, w in enumerate(words)}
    differences = {
        tuple(gsub(x[j], y[j]) for j in range(r))
        for x in words
        for y in words
        if x != y
    }
    largest = 1
    for d in differences:
        # Canonicalize +/- d so every undirected translation edge is used once.
        neg = tuple((-z[0], -z[1]) for z in d)
        if neg < d:
            continue
        adjacency: list[list[int]] = [[] for _ in words]
        for ix, x in enumerate(words):
            y = tuple(gadd(x[j], d[j]) for j in range(r))
            iy = index.get(y)
            if iy is not None:
                adjacency[ix].append(iy)
                adjacency[iy].append(ix)
        assert all(len(row) <= 2 for row in adjacency)
        seen: set[int] = set()
        for start in range(len(words)):
            if start in seen or not adjacency[start]:
                continue
            queue = deque([start])
            seen.add(start)
            size = 0
            edge_twice = 0
            while queue:
                v = queue.popleft()
                size += 1
                edge_twice += len(adjacency[v])
                for w in adjacency[v]:
                    if w not in seen:
                        seen.add(w)
                        queue.append(w)
            # Torsion-free translation graphs have no cycles.
            assert edge_twice // 2 == size - 1
            largest = max(largest, size)
    return largest


def main() -> None:
    # A genuine non-isometric Gaussian factor reallocation.
    a: Poly = (ONE, I)  # 1 + i z
    b: Poly = (ONE, (1, 1))  # 1 + (1+i) z
    u = pmul(a, b)
    v = pmul(a, pconj(b))
    assert norm(u) == norm(v)
    assert all(v != pscale(e, u) for e in UNITS)
    assert all(v != pscale(e, pconj(u)) for e in UNITS)

    # Common-suffix composition fails, with H=1 or H=i already witnessing it.
    shift = max(len(u), len(v)) + 1
    suffixes: tuple[Poly, ...] = ((ONE,), (I,))
    common_suffix_equalities = [
        norm(append_block(u, h, shift)) == norm(append_block(v, h, shift))
        for h in suffixes
    ]
    assert not all(common_suffix_equalities)

    # A global unit or conjugation must be applied to the suffix too; those
    # genuine planar isometries do compose.
    for e in UNITS:
        h: Poly = ((2, -1), (1, 1))
        assert norm(append_block(u, h, shift)) == norm(
            append_block(pscale(e, u), pscale(e, h), shift)
        )
        assert norm(append_block(u, h, shift)) == norm(
            append_block(pscale(e, pconj(u)), pscale(e, pconj(h)), shift)
        )

    square: tuple[G, ...] = ((0, 0), (1, 0), (0, 1), (1, 1))
    cross: tuple[G, ...] = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))
    assert additive_energy(square) == 36
    assert 36**2 > 4**5  # E(square) > |square|^(5/2), without floats.

    # Exact small Shannon-capacity stress: local rainbow numbers do not
    # multiply under consecutive-scale composition.
    square1 = list(product(square, repeat=1))
    square2 = list(product(square, repeat=2))
    m1, witness1 = maximum_rainbow(square1)
    m2, witness2 = maximum_rainbow(square2)
    assert m1 == 2
    assert m2 == 5 > m1 * m1

    # Exact translation graphs are uniformly short even though a fixed
    # displacement can occur in exponentially many separate components.
    for p in (square, cross):
        ell = max_ap_length(p)
        for r in (1, 2, 3):
            observed = translation_component_bound(p, r)
            assert observed <= ell

    print("non-isometric equal-norm pair:", u, v)
    print("common suffix H=1,i equalities:", common_suffix_equalities)
    print("square E^2 / |P|^5:", 36**2, 4**5)
    print("square rainbow maxima r=1,2:", m1, m2)
    print("square r=2 witness:", [square2[j] for j in witness2])
    print("translation AP bounds square/cross:", max_ap_length(square), max_ap_length(cross))
    print("fixed-alphabet local-collision capacity barrier: PASS")


if __name__ == "__main__":
    main()
