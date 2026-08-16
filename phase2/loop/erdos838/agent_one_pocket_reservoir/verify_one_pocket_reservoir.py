#!/usr/bin/env python3
"""Exact checks for ONE_POCKET_RESERVOIR.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb, floor, isqrt


Point = tuple[Fraction, Fraction]


def orient(a: Point, b: Point, c: Point) -> Fraction:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull_indices(points: list[Point]) -> tuple[int, ...]:
    """Monotone-chain hull; inputs in the geometric checks are general position."""
    order = sorted(range(len(points)), key=lambda i: points[i])

    def half(seq: list[int]) -> list[int]:
        out: list[int] = []
        for i in seq:
            while len(out) >= 2 and orient(points[out[-2]], points[out[-1]], points[i]) <= 0:
                out.pop()
            out.append(i)
        return out

    lo = half(order)
    hi = half(list(reversed(order)))
    return tuple(lo[:-1] + hi[:-1])


def convex(points: list[Point]) -> bool:
    return len(points) <= 2 or len(hull_indices(points)) == len(points)


def incidence_exhaustion() -> int:
    """Exhaust tiny abstract banks and check the two double counts."""
    checked = 0
    # A source chooses B distinct outputs from a four-face universe.
    universe = range(4)
    for s in range(1, 5):
        for bank_size in (1, 2, 3):
            banks = list(combinations(universe, bank_size))
            for assignment in product(banks, repeat=s):
                deg = [sum(j in bank for bank in assignment) for j in universe]
                lam = max(deg)
                assert bank_size * s == sum(deg)
                assert bank_size * s <= lam * len(universe)

                for d in range(1, 5):
                    assert d * s * bank_size <= d * lam * len(universe)
                    for eps_den in (2, 3):
                        # Use the exact rational threshold B / D^(1/eps_den)
                        # only when D is a perfect eps_den-th power.
                        base = round(d ** (1 / eps_den))
                        if base**eps_den == d:
                            threshold = Fraction(bank_size, base)
                            light_sources = [
                                a for a, bank in enumerate(assignment)
                                if all(Fraction(deg[j]) <= threshold for j in bank)
                            ]
                            assert bank_size * len(light_sources) <= threshold * len(universe)
                            high = [j for j in universe if Fraction(deg[j]) > threshold]
                            high_mass = sum(deg[j] for j in high)
                            assert high_mass >= bank_size * s - threshold * len(universe)
                            assert len(high) * s >= high_mass
                checked += 1
    return checked


def hybrid_exhaustion() -> int:
    """Check (13) after squaring, avoiding floating arithmetic."""
    checked = 0
    universe = range(4)
    banks1 = list(combinations(universe, 2))
    banks2 = list(combinations(universe, 3))
    for s in range(1, 5):
        for a1 in product(banks1, repeat=s):
            deg1 = [sum(j in bank for bank in a1) for j in universe]
            l1 = max(deg1)
            for a2 in product(banks2, repeat=s):
                deg2 = [sum(j in bank for bank in a2) for j in universe]
                l2 = max(deg2)
                # (D*S)^2 <= D^2 L1 L2 V^2/(Q B); cancel D^2.
                assert s * s * 2 * 3 <= l1 * l2 * len(universe) ** 2
                checked += 1
    return checked


def asymptotic_integer_audit() -> list[tuple[int, int, int]]:
    """Audit safe exponents behind (15)--(17) using an exact 0.24 surrogate."""
    rows: list[tuple[int, int, int]] = []
    for log_d in (64, 96, 128):
        d = 1 << log_d
        k = log_d // 8
        low_rank = sum(comb(d, i) for i in range(k))
        established_surrogate = 1 << floor(Fraction(6, 25) * log_d * log_d)
        bank = 1 << floor(Fraction(1, 5) * log_d * log_d)
        assert established_surrogate - low_rank >= bank
        assert (1 << k) ** 8 == d
        rows.append((log_d, k, bank.bit_length() - 1))
    return rows


def nested_chain_audit(d: int = 5) -> dict[str, int]:
    """Exact rational low-addable saturation of the shield-overlap branch."""
    q = 2 * d
    big = 4 * q
    u: Point = (Fraction(-big), Fraction(0))
    v: Point = (Fraction(big), Fraction(0))
    z: Point = (Fraction(0), Fraction(-big))
    tips: list[Point] = [(Fraction(i), Fraction(2**i)) for i in range(1, q + 1)]
    all_points = [u, v, z] + tips

    # General position.
    for a, b, c in combinations(all_points, 3):
        assert orient(a, b, c) != 0

    base = [u, v, z]
    assert convex(base)
    for i in range(d):
        source = base + [tips[i]]
        assert convex(source)
        for j in range(q):
            if i == j:
                continue
            trial = source + [tips[j]]
            # Earlier tips are interior; later tips hide the current tip.
            assert not convex(trial)
        for j in range(d, q):
            target = base + [tips[j]]
            assert convex(target)
            # In source+[new tip], index 3 is the old tip and index 4 the new.
            assert set(hull_indices(source + [tips[j]])) == {0, 1, 2, 4}

    blockers = tips[d:]
    # Points on the strictly convex exponential graph are in convex position.
    assert convex(blockers)
    for size in range(len(blockers) + 1):
        for face in combinations(blockers, size):
            assert convex(list(face))
    return {
        "sources": d,
        "selected_degree": d,
        "common_blocker_faces": 1 << d,
        "overlap_of_each_blocker_face": d,
    }


def main() -> None:
    incidence = incidence_exhaustion()
    hybrid = hybrid_exhaustion()
    asymptotic = asymptotic_integer_audit()
    nested = nested_chain_audit()
    print("one-pocket reservoir verification: PASS")
    print("incidence systems:", incidence)
    print("hybrid systems:", hybrid)
    print("asymptotic rows (logD,k,logB):", asymptotic)
    print("nested saturation:", nested)


if __name__ == "__main__":
    main()
