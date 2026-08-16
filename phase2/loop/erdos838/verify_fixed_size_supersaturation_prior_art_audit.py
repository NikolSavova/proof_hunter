#!/usr/bin/env python3
"""Exact checks for FIXED_SIZE_SUPERSATURATION_PRIOR_ART_AUDIT_20260816.md."""

from __future__ import annotations

from fractions import Fraction
from math import comb


Point = tuple[int, int]


def poly_add(target: list[int], source: list[int], scale: int = 1) -> None:
    if len(target) < len(source):
        target.extend([0] * (len(source) - len(target)))
    for index, value in enumerate(source):
        target[index] += scale * value


def shifted_binomial(power: int, shift: int, scale: int) -> list[int]:
    out = [0] * (shift + power + 1)
    for index in range(power + 1):
        out[shift + index] = scale * comb(power, index)
    return out


def fake_cutoff_ledger(size: int, cutoff: int) -> dict[tuple[int, int], int]:
    assert 3 <= cutoff <= size
    ledger: dict[tuple[int, int], int] = {
        (rank, 0): comb(size, rank) for rank in range(3, cutoff)
    }
    for interior in range(size - cutoff + 1):
        ledger[(cutoff, interior)] = comb(size - interior - 1, cutoff - 1)
    return ledger


def verify_fake_ledger(limit: int = 72) -> int:
    rows = 0
    for size in range(3, limit + 1):
        rhs = [comb(size, degree) if degree >= 3 else 0
               for degree in range(size + 1)]
        for cutoff in range(3, size + 1):
            lhs = [0] * (size + 1)
            ledger = fake_cutoff_ledger(size, cutoff)
            for (rank, interior), count in ledger.items():
                assert count >= 0
                poly_add(lhs, shifted_binomial(interior, rank, count))

            assert lhs == rhs
            for rank in range(3, cutoff + 1):
                assert sum(
                    count for (seen_rank, _), count in ledger.items()
                    if seen_rank == rank
                ) == comb(size, rank)
            assert all(rank <= cutoff for rank, _ in ledger)
            rows += size + len(ledger)
    return rows


def orient(a: Point, b: Point, c: Point) -> int:
    value = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    assert value != 0
    return 1 if value > 0 else -1


def convex_hull(points: list[Point]) -> list[Point]:
    ordered = sorted(points)

    def cross(a: Point, b: Point, c: Point) -> int:
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    lower: list[Point] = []
    for point in ordered:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper: list[Point] = []
    for point in reversed(ordered):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def inside_strict(point: Point, polygon: list[Point]) -> bool:
    signs = [orient(polygon[i], polygon[(i + 1) % len(polygon)], point) for i in range(len(polygon))]
    return all(sign == signs[0] for sign in signs)


def geometric_ledger(points: list[Point]) -> dict[tuple[int, int], int]:
    size = len(points)
    ledger: dict[tuple[int, int], int] = {}
    for mask in range(1 << size):
        chosen = [points[i] for i in range(size) if mask & (1 << i)]
        if len(chosen) < 3:
            continue
        hull = convex_hull(chosen)
        if len(hull) != len(chosen):
            continue
        chosen_set = set(chosen)
        interior = sum(
            inside_strict(point, hull)
            for point in points
            if point not in chosen_set
        )
        key = (len(chosen), interior)
        ledger[key] = ledger.get(key, 0) + 1
    return ledger


def verify_geometric_identity() -> int:
    examples: list[list[Point]] = [
        [(0, 0), (8, 1), (11, 9), (5, 15), (-2, 8)],
        [(0, 0), (12, 1), (11, 12), (-1, 11), (4, 4), (7, 6)],
        [(0, 0), (15, 1), (18, 11), (10, 19), (-2, 14), (3, 5), (9, 7)],
        [(0, 0), (20, 1), (23, 13), (14, 24), (2, 22), (-4, 10), (5, 4), (11, 9)],
    ]
    rows = 0
    for points in examples:
        for a in range(len(points)):
            for b in range(a + 1, len(points)):
                for c in range(b + 1, len(points)):
                    orient(points[a], points[b], points[c])
                    rows += 1
        ledger = geometric_ledger(points)
        lhs = [0] * (len(points) + 1)
        for (rank, interior), count in ledger.items():
            poly_add(lhs, shifted_binomial(interior, rank, count))
        rhs = [comb(len(points), degree) if degree >= 3 else 0 for degree in range(len(points) + 1)]
        assert lhs == rhs
        assert sum(count for (rank, _), count in ledger.items() if rank == 3) == comb(len(points), 3)
        rows += (1 << len(points)) + len(ledger)
    return rows


def verify_exponent_ledgers() -> int:
    rows = 0
    # If c_k = 2^{-a k}, one transversal box has exponent (2-a)k^2.
    for k in range(4, 401):
        for numerator in range(0, 17):
            a = Fraction(numerator, 8)
            exponent = (Fraction(2) - a) * k * k
            assert exponent > (1 + Fraction(1, 20)) * k * k if a < Fraction(19, 20) else True
            if a >= 1:
                assert exponent <= k * k
            rows += 1

    # The ES double count has main exponent 2k^2-kr, maximized at r=k.
    for k in range(4, 201):
        best = None
        for rank in range(k, 2 * k + 1):
            exponent = 2 * k * k - k * rank
            if best is None or exponent > best:
                best = exponent
            rows += 1
        assert best == k * k

    # Exact finite double counts approach the same coefficient-one boundary.
    for k in range(5, 31):
        ambient = 4**k
        threshold = 2**k
        numerator = comb(ambient, k)
        denominator = comb(threshold, k)
        assert numerator >= denominator
        # Integer comparison: the ratio is below N^k/t^k times a harmless
        # exp(O(k log k)) factor, so no hidden fixed quadratic gain appears.
        assert numerator * threshold**k <= denominator * ambient**k * (4 * k) ** k
        rows += 1
    return rows


def main() -> None:
    fake = verify_fake_ledger()
    geometry = verify_geometric_identity()
    exponents = verify_exponent_ledgers()
    print(
        "PASS: fixed-size prior-art audit; "
        f"fake_weighted_rows={fake}, geometric_rows={geometry}, exponent_rows={exponents}"
    )


if __name__ == "__main__":
    main()
