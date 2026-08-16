#!/usr/bin/env python3
"""Exact audit for the sparse-swap and exterior-code barrier."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path

from verify_onion_hall_obstruction import (
    is_convex_face,
    orient,
    strictly_inside_triangle,
)


Point = tuple[Fraction, Fraction]
HERE = Path(__file__).resolve().parent


def make_apex_cloud(count: int, chain: list[Point], centre: Point) -> list[Point]:
    """Choose exact rational apices preserving every rooted containment."""
    den = 10**8
    answer: list[Point] = []
    k = 1
    while len(answer) < count:
        t = Fraction(k, den)
        candidate = (centre[0] - t, centre[1] + t * t)
        prior = chain + answer
        rooted_ok = all(
            strictly_inside_triangle(chain[j], (candidate, chain[i], chain[l]))
            for i, j, l in combinations(range(len(chain)), 3)
        )
        if rooted_ok and all(orient(a, b, candidate) != 0 for a, b in combinations(prior, 2)):
            answer.append(candidate)
        k += 1
        if k > 100000:
            raise RuntimeError("failed to find enough exact exterior apices")
    return answer


def swap_neighbors(source: tuple[Point, ...], ambient: list[Point]) -> set[frozenset[Point]]:
    source_set = set(source)
    answer: set[frozenset[Point]] = set()
    for a in source:
        base = [x for x in source if x != a]
        for p in ambient:
            if p not in source_set and is_convex_face(base + [p]):
                answer.add(frozenset(base + [p]))
    return answer


def main() -> None:
    # Sharp coefficient-two certificate for one blocked point at r=4.
    sharp: list[Point] = [
        (Fraction(19), Fraction(-13)),
        (Fraction(-3), Fraction(20)),
        (Fraction(-7), Fraction(-6)),
        (Fraction(5), Fraction(-6)),
        (Fraction(19), Fraction(-20)),
    ]
    assert all(orient(a, b, c) != 0 for a, b, c in combinations(sharp, 3))
    sharp_A = [sharp[i] for i in (0, 1, 2, 4)]
    sharp_p = sharp[3]
    assert is_convex_face(sharp_A)
    assert not is_convex_face(sharp_A + [sharp_p])
    sharp_repairs = [
        i
        for i, a in enumerate(sharp_A)
        if is_convex_face([x for x in sharp_A if x != a] + [sharp_p])
    ]
    assert sharp_repairs == [1, 2]

    r = 4
    m = 5 * r
    last = m - 1
    chain: list[Point] = [
        (Fraction(i), Fraction(i * (last - i))) for i in range(m)
    ]
    apex_centre: Point = (Fraction(-1), Fraction(m * m))
    apices = make_apex_cloud(8, chain, apex_centre)
    ambient = chain + apices

    determinant_checks = 0
    for a, b, c in combinations(ambient, 3):
        determinant_checks += 1
        assert orient(a, b, c) != 0

    rooted_checks = 0
    for p in apices:
        for i, j, k in combinations(range(m), 3):
            rooted_checks += 1
            assert strictly_inside_triangle(chain[j], (p, chain[i], chain[k]))

    words = list(combinations(range(m), r))
    assert len(words) == math.comb(m, r)
    for word in words:
        source = tuple(chain[i] for i in word)
        assert is_convex_face(source)
        addable = [x for x in ambient if x not in source and is_convex_face(source + (x,))]
        assert set(addable) == set(chain) - set(source)
        assert len(addable) == 4 * r
        neighbors = swap_neighbors(source, ambient)
        assert len(neighbors) == 4 * r * r
        assert all(not (set(B) & set(apices)) for B in neighbors)

    # Greedy independent code in J(5r,r).
    code: list[frozenset[int]] = []
    for word in words:
        W = frozenset(word)
        if all(len(W & C) <= r - 2 for C in code):
            code.append(W)
    johnson_degree = r * (m - r)
    assert len(code) * (johnson_degree + 1) >= len(words)

    shadows: set[frozenset[int]] = set()
    for word in code:
        for a in word:
            shadow = word - {a}
            assert shadow not in shadows
            shadows.add(shadow)
    assert len(shadows) == r * len(code)

    result = {
        "r": r,
        "sharp_blocked_repairs_at_r4": len(sharp_repairs),
        "ambient_n": len(ambient),
        "chain_size": m,
        "exterior_apex_count": len(apices),
        "sources": len(words),
        "source_formula": f"binom({m},{r})",
        "u_each_source": 4 * r,
        "exterior_blocked_each_source": len(apices),
        "full_swap_degree_every_source": 4 * r * r,
        "induced_johnson_degree": johnson_degree,
        "greedy_independent_code_size": len(code),
        "disjoint_immediate_shadow_size": len(shadows),
        "rooted_triples_checked": rooted_checks,
        "general_position_triples_checked": determinant_checks,
        "verdict": (
            "swap-degree theorem and exterior planar constant-weight-code barrier verified; "
            "source-only swaps/shadows cannot supply n-dependent Hall gain"
        ),
    }
    (HERE / "swap_shadow_certificate.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
