#!/usr/bin/env python3
"""Exact checks for MINIMIZER_SINGLETON_ENDPOINT_SURPLUS_GATE.md."""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402


Point = tuple[Fraction, Fraction]


def is_convex(points: list[Point]) -> bool:
    if len(points) <= 3:
        return True
    pts = sorted(points)

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for point in seq:
            while (len(out) >= 2
                   and rt.determinant(out[-2], out[-1], point) <= 0):
                out.pop()
            out.append(point)
        return out

    return len(half(pts)[:-1] + half(list(reversed(pts)))[:-1]) == len(pts)


def is_chain(points: list[Point], sign: int) -> bool:
    points = sorted(points)
    return all(
        (rt.determinant(points[i], points[j], points[k]) > 0)
        == (sign > 0)
        for i, j, k in itertools.combinations(range(len(points)), 3)
    )


def families(points: list[Point]) -> tuple[list[int], list[int], list[int]]:
    faces: list[int] = []
    caps: list[int] = []
    cups: list[int] = []
    for mask in range(1, 1 << len(points)):
        subset = [points[i] for i in range(len(points)) if mask >> i & 1]
        if is_convex(subset):
            faces.append(mask)
        if is_chain(subset, -1):
            caps.append(mask)
        if is_chain(subset, +1):
            cups.append(mask)
    return faces, caps, cups


def subset_family(family: list[int], deleted: int) -> list[int]:
    return [mask for mask in family if not (mask >> deleted) & 1]


def audit_minimal_five_point_set() -> tuple[int, int, int, int]:
    points = [
        (Fraction(6), Fraction(15)),
        (Fraction(18), Fraction(22)),
        (Fraction(13), Fraction(4)),
        (Fraction(12), Fraction(17)),
        (Fraction(20), Fraction(29)),
    ]
    assert all(
        rt.determinant(points[i], points[j], points[k]) != 0
        for i, j, k in itertools.combinations(range(5), 3)
    )
    faces, caps, cups = families(points)
    assert (len(faces), len(caps), len(cups)) == (26, 17, 24)
    face_ranks = [sum(mask.bit_count() == rank for mask in faces)
                  for rank in range(1, 6)]
    assert face_ranks == [5, 10, 10, 1, 0]

    # V=26 is globally minimal: ranks <=3 already give 25, and ES(4)=5
    # forces at least one convex four-set.  Here we verify the witness count.
    assert sum(mask.bit_count() == 4 for mask in faces) == 1

    ell_sum = 0
    cap_delete_sum = 0
    cup_delete_sum = 0
    for x in range(5):
        q_faces = subset_family(faces, x)
        q_caps = subset_family(caps, x)
        q_cups = subset_family(cups, x)
        ell = len(faces) - len(q_faces)
        assert ell <= 1 + len(q_caps)
        assert ell <= 1 + len(q_cups)
        ell_sum += ell
        cap_delete_sum += len(q_caps)
        cup_delete_sum += len(q_cups)

        # Check the coefficientwise *mutation identity*, not a coefficientwise
        # minimality inequality.
        cap_mutation_profile: list[int] = []
        cup_mutation_profile: list[int] = []
        for rank in range(1, 6):
            cap_new = ((1 if rank == 1 else 0)
                       + sum(mask.bit_count() == rank - 1 for mask in q_caps))
            cup_new = ((1 if rank == 1 else 0)
                       + sum(mask.bit_count() == rank - 1 for mask in q_cups))
            q_rank = sum(mask.bit_count() == rank for mask in q_faces)
            cap_mutation_profile.append(q_rank + cap_new)
            cup_mutation_profile.append(q_rank + cup_new)
        assert sum(cap_mutation_profile) == len(q_faces) + 1 + len(q_caps)
        assert sum(cup_mutation_profile) == len(q_faces) + 1 + len(q_cups)

    mu_v = sum(mask.bit_count() for mask in faces)
    m_cap = sum(mask.bit_count() for mask in caps)
    m_cup = sum(mask.bit_count() for mask in cups)
    assert ell_sum == mu_v
    assert cap_delete_sum == 5 * len(caps) - m_cap
    assert cup_delete_sum == 5 * len(cups) - m_cup
    assert mu_v <= 5 + 5 * len(caps) - m_cap
    assert mu_v <= 5 + 5 * len(cups) - m_cup

    s_cap = 5 + 5 * len(caps) - m_cap - mu_v
    s_cup = 5 + 5 * len(cups) - m_cup - mu_v
    e_cap = 2 * m_cap - 5
    e_cup = 2 * m_cup - 5
    b_cap = 5 * len(caps) - e_cap
    b_cup = 5 * len(cups) - e_cup
    assert b_cap == 2 * mu_v + 2 * s_cap - 5 * len(caps) - 5
    assert b_cup == 2 * mu_v + 2 * s_cup - 5 * len(cups) - 5
    assert len(caps) >= Fraction(mu_v - 5, 5)
    assert len(cups) >= Fraction(mu_v - 5, 5)
    assert Fraction(len(caps) * len(cups), len(faces)) >= Fraction(
        (mu_v - 5) ** 2, 25 * len(faces)
    )
    return mu_v, s_cap, b_cap, b_cup


def audit_pascal_singleton_failure() -> tuple[int, list[int], list[int]]:
    child = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    points = sorted(rt.strong_glue(child, child, Fraction(1, 16384)))
    faces, caps, cups = families(points)
    assert (len(caps), len(cups), len(faces)) == (248, 248, 1061)

    ell_values: list[int] = []
    best_mutations: list[int] = []
    for x in range(12):
        q_faces = subset_family(faces, x)
        q_caps = subset_family(caps, x)
        q_cups = subset_family(cups, x)
        ell = len(faces) - len(q_faces)
        best = len(q_faces) + 1 + min(len(q_caps), len(q_cups))
        ell_values.append(ell)
        best_mutations.append(best)
        assert best < len(faces)
        assert ell > 1 + min(len(q_caps), len(q_cups))

    assert ell_values == [394] * 3 + [332] * 6 + [394] * 3
    assert min(best_mutations) == 832
    assert max(best_mutations) == 908
    return len(faces), ell_values, best_mutations


def audit_two_anchor_avoidance(points: list[Point]) -> tuple[int, int, int]:
    _, caps, cups = families(points)
    n, c, u = len(points), len(caps), len(cups)
    cap_set, cup_set = set(caps), set(cups)
    r = max(max(mask.bit_count() for mask in caps),
            max(mask.bit_count() for mask in cups))
    b_cap = [sum((mask | (1 << y)) not in cap_set for mask in caps)
             for y in range(n)]
    b_cup = [sum((mask | (1 << z)) not in cup_set for mask in cups)
             for z in range(n)]

    cap_delete: list[list[int]] = []
    cup_delete: list[list[int]] = []
    for y in range(n):
        cap_row: list[int] = []
        cup_row: list[int] = []
        for z in range(n):
            deleted = (1 << y) | (1 << z)
            cap_row.append(sum(mask & deleted == 0 for mask in caps))
            cup_row.append(sum(mask & deleted == 0 for mask in cups))
        cap_delete.append(cap_row)
        cup_delete.append(cup_row)

    cap_deficit = sum(c - cap_delete[y][z]
                      for y in range(n) for z in range(n))
    cup_deficit = sum(u - cup_delete[y][z]
                      for y in range(n) for z in range(n))
    assert cap_deficit <= 2 * n * r * c
    assert cup_deficit <= 2 * n * r * u

    weighted_cap_deficit = sum(
        b_cap[y] * b_cup[z] * (c - cap_delete[y][z])
        for y in range(n) for z in range(n)
    )
    weighted_cup_deficit = sum(
        b_cap[y] * b_cup[z] * (u - cup_delete[y][z])
        for y in range(n) for z in range(n)
    )
    assert weighted_cap_deficit <= c * u * cap_deficit
    assert weighted_cup_deficit <= c * u * cup_deficit

    good_weight = sum(
        b_cap[y] * b_cup[z]
        for y in range(n) for z in range(n)
        if 2 * cap_delete[y][z] >= c and 2 * cup_delete[y][z] >= u
    )
    total_weight = sum(b_cap) * sum(b_cup)
    assert good_weight >= total_weight - 8 * n * r * c * u
    low = max(n - 2 * r, 0)
    assert total_weight >= low * low * c * u
    assert good_weight >= (low * low - 8 * n * r) * c * u
    return r, total_weight, good_weight


def audit_scalar_sharpness() -> tuple[int, int, int, int, Fraction]:
    r, q, scale = 5, 20, 101
    assert scale % r == 1
    n = r * q - 1
    c = scale * n
    m_cap = r * c
    ell = 1 + scale * (n - r)
    assert ell % r == 0
    v = n * ell // r
    mu = r
    c_delete = c - m_cap // n
    assert c_delete == scale * (n - r)
    assert ell == 1 + c_delete
    assert mu * v == n + n * c - m_cap

    good_extensions = 2 * m_cap - n
    bad_extensions = n * c - good_extensions
    assert bad_extensions == 2 * mu * v - n * c - n
    assert bad_extensions * 10 > 8 * n * c
    all_pair_load = Fraction(c * c, v)
    assert all_pair_load > 500
    return n, c, v, bad_extensions, all_pair_load


def main() -> None:
    mu_v, s_cap, b_cap, b_cup = audit_minimal_five_point_set()
    pascal_v, ell_values, best_mutations = audit_pascal_singleton_failure()
    p5 = [(Fraction(x), Fraction(y)) for x, y in
          [(6, 15), (18, 22), (13, 4), (12, 17), (20, 29)]]
    avoid_r, avoid_total, avoid_good = audit_two_anchor_avoidance(p5)
    n, c, v, bad, load = audit_scalar_sharpness()
    print(
        "PASS: minimal P5 muV=%d cap-slack=%d bad=(%d,%d); "
        "Pascal V=%d ell=%s singleton-mutations=[%d,%d]; "
        "avoidance R=%d weighted=%d/%d; "
        "scalar n=%d C=%d V=%d bad=%d pair-load=%s"
        % (
            mu_v, s_cap, b_cap, b_cup,
            pascal_v, sorted(set(ell_values)), min(best_mutations),
            max(best_mutations), avoid_r, avoid_good, avoid_total,
            n, c, v, bad, load,
        )
    )


if __name__ == "__main__":
    main()
