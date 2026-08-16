#!/usr/bin/env python3
"""Exact audit for GLOBAL_RANK_THREE_ES4_REPLACEMENT_CODE.md."""

from fractions import Fraction
from itertools import combinations
from math import ceil, comb


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex4(points):
    """Four GP points are convex iff no point lies in the other triangle."""
    assert len(points) == 4
    signs = []
    for i in range(4):
        p = points[i]
        tri = [points[j] for j in range(4) if j != i]
        s = [orient(tri[k], tri[(k + 1) % 3], p) for k in range(3)]
        inside = all(x > 0 for x in s) or all(x < 0 for x in s)
        signs.append(inside)
    return not any(signs)


def v4(points):
    return sum(convex4([points[i] for i in I])
               for I in combinations(range(len(points)), 4))


def algebra():
    worst3 = Fraction(0)
    worstall = Fraction(0)
    rows = []
    for n in range(5, 501):
        lower = Fraction(comb(n, 4), 5)
        t3 = comb(n, 3) * ceil(Fraction(n, 8))
        tall = sum(comb(n, r) * ceil(Fraction(n, 2**r))
                   for r in range(1, 4))
        ratio3 = Fraction(t3, 1) / lower
        ratioall = Fraction(tall, 1) / lower
        assert ratio3 <= 10
        assert ratioall <= 80
        worst3 = max(worst3, ratio3)
        worstall = max(worstall, ratioall)
        if n in (5, 8, 9, 32, 70, 500):
            rows.append((n, t3, tall, ratio3, ratioall))
    return worst3, worstall, rows


def generalized():
    rows = []
    for r in range(3, 19):
        t = comb(2 * r - 2, r - 1) + 1
        assert t <= 4**r + 1
        # Pick n large enough that r <= log_2 n and audit the exact formula.
        n = 2 ** max(r, 6)
        histories = comb(n, r)
        demand_slots = histories * ceil(Fraction(n, 2**r))
        # Symbolic ES lower bank; retain as a rational capacity.
        bank_lower = Fraction(comb(n, r + 1), comb(t, r + 1))
        exact_ratio = Fraction(demand_slots, 1) / bank_lower
        formula = (Fraction(comb(t, r + 1) * (r + 1), n - r)
                   * ceil(Fraction(n, 2**r)))
        assert exact_ratio == formula
        coarse = 1 + Fraction(4 * (r + 1) * comb(4**r + 1, r + 1), 2**r)
        assert ceil(exact_ratio) <= coarse
        rows.append((r, t, exact_ratio.numerator.bit_length(),
                     exact_ratio.denominator.bit_length()))
    return rows


def geometry():
    configs = []
    # Strict cup.
    configs.append([(i, i * i) for i in range(5, 18)])
    # Alternating integral set.
    configs.append([(i, (1 if i % 2 else -1) * (i * i + 3 * i + 1))
                    for i in range(5, 19)])
    # Deterministic cubic perturbation.
    configs.append([(i, i**3 - 17 * i * i + 13 * i + (i % 3))
                    for i in range(5, 20)])

    out = []
    for pts in configs:
        # Audit general position.
        assert all(orient(pts[i], pts[j], pts[k]) != 0
                   for i, j, k in combinations(range(len(pts)), 3))
        count = v4(pts)
        assert 5 * count >= comb(len(pts), 4)
        out.append((len(pts), count, comb(len(pts), 4)))
    return out


def block_code(n=17):
    histories = list(combinations(range(n), 3))
    # A convex n-gon gives the largest convenient exact output bank.
    outputs = list(combinations(range(n), 4))
    q = ceil(Fraction(n, 8))
    copies = 10
    slots = [(c, F) for c in range(copies) for F in outputs]
    need = len(histories) * q
    assert need <= len(slots)

    load = {F: Fraction(0) for F in outputs}
    fibres = {F: set() for F in outputs}
    per = Fraction(n, 8 * q)
    for hidx, H in enumerate(histories):
        for c, F in slots[hidx * q:(hidx + 1) * q]:
            load[F] += per
            fibres[F].add((c, hidx))
    assert max(load.values()) <= copies
    assert max(len(v) for v in fibres.values()) <= copies
    return need, len(outputs), max(load.values()), max(map(len, fibres.values()))


def main():
    w3, wall, rows = algebra()
    gen = generalized()
    geom = geometry()
    block = block_code()
    print("PASS: global rank-three ES4 replacement code; "
          f"worst3={w3}; worst<=3={wall}; geometry={geom}; block={block}; "
          f"rows={rows}; generalized={gen}")


if __name__ == "__main__":
    main()
