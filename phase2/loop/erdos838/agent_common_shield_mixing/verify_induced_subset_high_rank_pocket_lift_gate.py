#!/usr/bin/env python3
"""Exact checks for INDUCED_SUBSET_HIGH_RANK_POCKET_LIFT_GATE.md."""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

from agent_common_shield_mixing.verify_dense_hall_two_cloud_profile_barrier import (  # noqa: E402
    G0,
    X0,
    convex,
    hull,
    parabolic_cloud,
)


def shelf(n: int, rank: int) -> list[int]:
    return [comb(n, k) if k <= rank else 0 for k in range(n + 1)]


def restriction_average(profile: list[int], n: int, m: int) -> Fraction:
    answer = Fraction(0)
    for k, count in enumerate(profile[: m + 1]):
        answer += Fraction(count * comb(n - k, m - k), comb(n, m))
    return answer


def exact_shelf_restrictions():
    checked = 0
    for n in range(5, 19):
        for rank in range(0, min(7, n) + 1):
            profile = shelf(n, rank)
            for m in range(n + 1):
                actual = restriction_average(profile, n, m)
                expected = sum(comb(m, k) for k in range(min(rank, m) + 1))
                assert actual == expected
                checked += 1
    return checked


def greedy_rank_lp():
    # The exact minimizer of rank incidence under capacities and total mass
    # fills the levels from below.  Exhaust all small integral competitors.
    checked = 0
    n = 6
    capacities = [comb(n, k) for k in range(n + 1)]
    for total in range(1, 28):
        remaining = total
        greedy = []
        for capacity in capacities:
            take = min(capacity, remaining)
            greedy.append(take)
            remaining -= take
        assert remaining == 0
        optimum = sum(k * value for k, value in enumerate(greedy))

        # Dynamic program gives an independent exact optimum.
        dp = {0: 0}
        for k, capacity in enumerate(capacities):
            new = {}
            for mass, cost in dp.items():
                for take in range(min(capacity, total - mass) + 1):
                    key = mass + take
                    value = cost + k * take
                    new[key] = min(new.get(key, value), value)
            dp = new
        assert dp[total] == optimum
        checked += 1
    return checked


def quadratic_shelf_ledger():
    rows = []
    for level in (32, 48, 64, 96, 128):
        rank = level // 2
        n = 1 << level
        top_log = math.log2(sum(comb(n, k) for k in range(rank + 1)))
        assert top_log / level**2 < 0.51
        assert top_log / level**2 > 0.5 - 2 * math.log2(level) / level
        for numerator, denominator in ((1, 4), (1, 2), (3, 4), (7, 8)):
            alpha = numerator / denominator
            sublevel = int(alpha * level)
            m = 1 << sublevel
            restriction_log = math.log2(
                sum(comb(m, k) for k in range(rank + 1))
            )
            target = 0.5 * sublevel**2
            # The shelf has coefficient alpha/2, above alpha^2/2.
            assert restriction_log + 3 * level * math.log2(level) >= target
        rows.append((level, rank, top_log / level**2))
    return rows


def hereditary_high_rank_count():
    # Pure combinatorial double count: if every m-set has an r-witness,
    # then the number of distinct witnesses is at least this ratio.
    checked = 0
    for n in range(10, 31):
        for m in range(5, n + 1):
            for r in range(3, min(6, m) + 1):
                pairs_lower = comb(n, m)
                fibre = comb(n - r, m - r)
                ratio = Fraction(pairs_lower, fibre)
                assert ratio == Fraction(comb(n, r), comb(m, r))
                assert ratio >= Fraction(n, m) ** r
                checked += 1
    return checked


def planar_es_double_count():
    # ES(4)=5 on a nontrivial exact rational two-cloud configuration.
    points = parabolic_cloud(G0, 5, 1) + parabolic_cloud(X0, 5, -1)
    witnesses = 0
    for sample in itertools.combinations(points, 5):
        local = [quad for quad in itertools.combinations(sample, 4)
                 if convex(quad)]
        assert local
        witnesses += 1
    faces = [quad for quad in itertools.combinations(points, 4)
             if convex(quad)]
    assert witnesses == comb(10, 5)
    assert len(faces) >= Fraction(comb(10, 4), comb(5, 4))
    return witnesses, len(faces), Fraction(comb(10, 4), comb(5, 4))


def pocket_scale_ledger():
    rows = []
    for level in (64, 96, 128, 192, 256):
        # s=L^4 and an illustrative o(L) inverse-ES error sqrt(L).
        delta = 4 * math.log2(level)
        pocket_level = level - delta
        rank = pocket_level - math.sqrt(pocket_level)
        source_log = rank * delta
        pocket_log = 0.5 * pocket_level**2
        combined = source_log + pocket_log
        assert rank / level > 0.5
        assert combined / level**2 < 0.5
        rows.append((level, rank / level, combined / level**2))
    assert rows[-1][2] > rows[0][2]
    return rows


def adjacent_on_hull(points, a, b):
    boundary = hull(points)
    ia = boundary.index(a)
    ib = boundary.index(b)
    return (ia - ib) % len(boundary) in (1, len(boundary) - 1)


def fixed_edge_anti_alignment():
    source = parabolic_cloud(G0, 8, 1)
    pocket = parabolic_cloud(X0, 7, -1)
    fixed = source[:2]
    sources = [
        tuple(fixed + list(extra))
        for extra in itertools.combinations(source[2:], 2)
    ]
    pockets = list(itertools.combinations(pocket, 3))
    bad = 0
    for face in sources:
        assert convex(face)
        assert adjacent_on_hull(list(face), fixed[0], fixed[1])
        for inside in pockets:
            assert convex(inside)
            assert not convex(list(face) + list(inside))
            bad += 1
    assert len(sources) == comb(6, 2) == 15
    assert len(pockets) == comb(7, 3) == 35
    assert bad == 525
    return len(sources), len(pockets), bad


def fixed_edge_pigeonhole():
    # Each r-gon has r oriented boundary edges among n(n-1) possibilities.
    examples = []
    for n, rank, faces in ((100, 20, 10**8), (256, 30, 10**12)):
        lower = (rank * faces + n * (n - 1) - 1) // (n * (n - 1))
        assert lower >= faces // (n * n)
        examples.append((n, rank, faces, lower))
    return examples


def main():
    restrictions = exact_shelf_restrictions()
    greedy = greedy_rank_lp()
    shelf_rows = quadratic_shelf_ledger()
    hereditary = hereditary_high_rank_count()
    planar_es = planar_es_double_count()
    pocket = pocket_scale_ledger()
    anti = fixed_edge_anti_alignment()
    edges = fixed_edge_pigeonhole()
    print(
        "PASS: induced-subset/high-rank pocket gate; "
        f"restriction-identities={restrictions}; greedy-LPs={greedy}; "
        f"shelf={len(shelf_rows)}; hereditary={hereditary}; planar-ES={planar_es}; "
        f"pocket={len(pocket)}; anti-aligned={anti}; edges={edges}"
    )


if __name__ == "__main__":
    main()
