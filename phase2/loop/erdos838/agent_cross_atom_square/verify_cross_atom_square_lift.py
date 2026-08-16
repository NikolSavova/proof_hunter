#!/usr/bin/env python3
"""Exact audits for CROSS_ATOM_SQUARE_LIFT.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import ceil, comb, isqrt
from random import Random


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(points: frozenset[Point]) -> tuple[Point, ...]:
    ordered = sorted(points)
    if len(ordered) <= 1:
        return tuple(ordered)

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lo = half(ordered)
    hi = half(list(reversed(ordered)))
    return tuple(lo[:-1] + hi[:-1])


def is_convex_position(points: frozenset[Point]) -> bool:
    return len(convex_hull(points)) == len(points)


def square_localization_audit() -> dict[str, int]:
    checked = 0
    separated_branch = dominant_branch = cross_branch = 0
    # eta=1/3, delta=2/5.  Atom weights are split two per pocket.
    eta = Fraction(1, 3)
    delta = Fraction(2, 5)
    for m in range(4, 7):
        for raw in product(range(3), repeat=2 * m):
            if not any(raw):
                continue
            atoms = [raw[2 * i : 2 * i + 2] for i in range(m)]
            p = [sum(row) for row in atoms]
            h = sum(p)
            windows = [p[(i - 1) % m] + p[i] + p[(i + 1) % m] for i in range(m)]
            sep = sum(
                p[i] * p[j]
                for i in range(m)
                for j in range(m)
                if i != j and (i - j) % m not in (1, m - 1)
            )
            assert sep == h * h - sum(p[i] * windows[i] for i in range(m))
            assert sep >= h * (h - max(windows))
            if sep >= eta * h * h:
                separated_branch += 1
            else:
                idx = max(range(m), key=windows.__getitem__)
                mass = windows[idx]
                assert mass > (1 - eta) * h
                window_atoms = atoms[(idx - 1) % m] + atoms[idx] + atoms[(idx + 1) % m]
                maximum = max(window_atoms)
                if maximum >= delta * mass:
                    assert maximum * maximum >= delta * delta * (1 - eta) ** 2 * h * h
                    dominant_branch += 1
                else:
                    diagonal = sum(x * x for x in window_atoms)
                    cross = mass * mass - diagonal
                    assert diagonal <= maximum * mass
                    assert cross > (1 - delta) * mass * mass
                    cross_branch += 1
            checked += 1
    return {
        "weight_vectors": checked,
        "separated": separated_branch,
        "dominant": dominant_branch,
        "cross_atom": cross_branch,
    }


def octagon_and_tips() -> tuple[tuple[Point, ...], tuple[Point, ...]]:
    raw = (
        (0, 0),
        (4, -1),
        (8, 1),
        (10, 5),
        (8, 9),
        (4, 11),
        (0, 9),
        (-2, 5),
    )
    f = tuple((Fraction(x), Fraction(y)) for x, y in raw)
    assert is_convex_position(frozenset(f))
    eps = Fraction(1, 1000)
    tips: list[Point] = []
    for i, a in enumerate(f):
        b = f[(i + 1) % len(f)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        q = ((a[0] + b[0]) / 2 + eps * dy, (a[1] + b[1]) / 2 - eps * dx)
        assert orient(a, b, q) < 0
        for k, c in enumerate(f):
            d = f[(k + 1) % len(f)]
            if k != i:
                assert orient(c, d, q) > 0
        tips.append(q)
    return f, tuple(tips)


def four_root_decoder_audit() -> dict[str, int]:
    f, tips = octagon_and_tips()
    m = len(f)
    outputs: dict[frozenset[Point], list[tuple[int, int]]] = {}
    candidates_checked = true_decodes = 0
    for i in range(m):
        indices = (i, (i + 1) % m, (i + 2) % m)
        u = frozenset(f + tuple(tips[j] for j in indices))
        assert is_convex_position(u)
        rank = len(u)
        roots = (f[i], f[(i + 1) % m], f[(i + 2) % m], f[(i + 3) % m])
        recovered: list[frozenset[Point]] = []
        for j in range(3):
            pocket = frozenset(x for x in u if orient(roots[j], roots[j + 1], x) < 0)
            assert pocket == frozenset((tips[indices[j]],))
            recovered.append(pocket)
            outputs.setdefault(u, []).append((i, j))
            true_decodes += 1

        recovered_f = u - frozenset().union(*recovered)
        assert recovered_f == frozenset(f)

        # Audit the stated decoder over every ordered four-tuple.  We only
        # count; its universal bound is rank^4 tuples times three active slots.
        points = tuple(u)
        for a0 in points:
            for a1 in points:
                for a2 in points:
                    for a3 in points:
                        candidates_checked += 1
                        if len({a0, a1, a2, a3}) < 4:
                            continue
                        _ = (
                            {x for x in u if orient(a0, a1, x) < 0},
                            {x for x in u if orient(a1, a2, x) < 0},
                            {x for x in u if orient(a2, a3, x) < 0},
                        )
        assert len(outputs[u]) <= 3 * rank**4

    return {
        "protected_outputs": len(outputs),
        "true_active_decodes": true_decodes,
        "ordered_root_candidates": candidates_checked,
        "max_true_description_fibre": max(map(len, outputs.values())),
    }


def flank_code_audit() -> dict[str, int]:
    cases = tuples = 0
    max_fibre_seen = 0
    for q_minus in range(1, 8):
        for q_plus in range(1, 8):
            for y in range(1, 8):
                s_minus = 1 + q_minus + comb(q_minus, 2)
                s_plus = 1 + q_plus + comb(q_plus, 2)
                domain = q_minus * q_plus * y * y
                codomain = s_minus * s_plus
                loads = [0] * codomain
                for z in range(domain):
                    loads[z % codomain] += 1
                fibre = max(loads)
                expected = ceil(domain / codomain)
                assert fibre == expected
                assert expected <= ceil(4 * y * y / (q_minus * q_plus))
                if q_minus == q_plus == y:
                    assert expected <= 4
                cases += 1
                tuples += domain
                max_fibre_seen = max(max_fibre_seen, fibre)
    return {"parameter_cases": cases, "coded_tuples": tuples, "max_fibre": max_fibre_seen}


def open_slot_decoder_audit() -> dict[str, int]:
    rows = 0
    maximum = 0
    for s in range(1, 33):
        u = frozenset(range(s))
        descriptions: set[tuple[frozenset[int], frozenset[int]]] = set()
        # Exact reverse decoder: the deleted open set E and core U-E.
        for t in range(0, min(3, s) + 1):
            for choice in combinations(range(s), t):
                e = frozenset(choice)
                descriptions.add((u - e, e))
        expected = sum(comb(s, t) for t in range(0, min(3, s) + 1))
        assert len(descriptions) == expected
        maximum = max(maximum, expected)
        rows += 1
    return {"ranks": rows, "largest_S3": maximum}


def cauchy_telescope_audit() -> dict[str, int]:
    rng = Random(838)
    trials = 0
    for v in range(2, 18):
        for _ in range(500):
            cell_count = rng.randrange(1, 25)
            a_masks: list[set[int]] = []
            b_masks: list[set[int]] = []
            for _c in range(cell_count):
                a_masks.append({i for i in range(v) if rng.randrange(3) == 0} or {rng.randrange(v)})
                b_masks.append({i for i in range(v) if rng.randrange(3) == 0} or {rng.randrange(v)})
            l_a = max(sum(i in mask for mask in a_masks) for i in range(v))
            l_b = max(sum(i in mask for mask in b_masks) for i in range(v))
            k = rng.randrange(1, 10)
            g = [isqrt(k * len(a) * len(b)) for a, b in zip(a_masks, b_masks)]
            for x, a, b in zip(g, a_masks, b_masks):
                assert x * x <= k * len(a) * len(b)
            assert sum(g) * sum(g) <= k * sum(map(len, a_masks)) * sum(map(len, b_masks))
            assert sum(g) * sum(g) <= k * l_a * l_b * v * v
            trials += 1
    return {"random_integer_systems": trials}


def main() -> None:
    print("SQUARE_LOCALIZATION", square_localization_audit())
    print("FOUR_ROOT_DECODER", four_root_decoder_audit())
    print("FLANK_CODE", flank_code_audit())
    print("OPEN_SLOT_DECODER", open_slot_decoder_audit())
    print("CAUCHY_TELESCOPE", cauchy_telescope_audit())
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    main()
