#!/usr/bin/env python3
"""Exact/numerical checks for HEREDITARY_MULTIPLICITY_BARRIER.md.

The exact part verifies that every chain of hereditary double counts
telescopes to the direct binomial factor.  The floating-point part checks the
quadratic profile identities and the local-supersaturation formula on a grid.
It is a smoke test, not a premise of any proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb
from random import Random


def exact_chain_factor(chain: list[int], k: int) -> Fraction:
    out = Fraction(1)
    for large, small in zip(chain, chain[1:]):
        out *= Fraction(comb(large, k), comb(small, k))
    return out


def check_exact_telescoping() -> int:
    checked = 0
    for n in range(6, 31):
        for a in range(5, n + 1):
            for b in range(4, a + 1):
                for m in range(3, b + 1):
                    for k in range(1, m + 1):
                        chain = [n, a, b, m]
                        got = exact_chain_factor(chain, k)
                        want = Fraction(comb(n, k), comb(m, k))
                        assert got == want
                        checked += 1
    return checked


def check_profile_fixed_point() -> int:
    checked = 0
    for ai in range(1, 100):
        alpha = ai / 100
        for ti in range(1, 100):
            theta = ti / 100
            y = alpha * theta
            lifted = theta * (1 - theta) * alpha**2 + theta * alpha * (1 - alpha)
            direct = y * (1 - y)
            assert abs(lifted - direct) < 1e-12
            checked += 1
    return checked


def check_standard_supersaturation_profile() -> int:
    checked = 0
    for rhoi in range(101, 501):
        rho = rhoi / 100
        sigma = rho - 1
        for bi in range(1, int(100 / rho) + 1):
            beta = bi / 100
            local = beta - (rho - sigma) * beta**2
            direct = beta * (1 - beta)
            assert abs(local - direct) < 1e-12
            checked += 1
    return checked


def check_phi_formula() -> int:
    checked = 0
    for rhoi in range(101, 501, 3):
        rho = rhoi / 100
        for sigmai in range(0, 2 * rhoi + 1, 5):
            sigma = sigmai / 100
            if sigma <= rho / 2:
                formula = 1 / (4 * (rho - sigma))
            else:
                formula = sigma / rho**2
            # The concave quadratic has its maximum at the critical point or
            # at the right endpoint.  Evaluate those candidates directly.
            candidates = [1 / rho]
            if rho > sigma:
                critical = 1 / (2 * (rho - sigma))
                if critical <= 1 / rho:
                    candidates.append(critical)
            direct = max(beta - (rho - sigma) * beta**2 for beta in candidates)
            assert abs(formula - direct) < 1e-12
            checked += 1
    return checked


def orient(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def convex_hull(indices: list[int], points: list[tuple[int, int]]) -> tuple[int, ...]:
    ordered = sorted(indices, key=points.__getitem__)
    lower: list[int] = []
    for i in ordered:
        while len(lower) >= 2 and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in reversed(ordered):
        while len(upper) >= 2 and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return tuple(lower[:-1] + upper[:-1])


def random_general_position(n: int, seed: int) -> list[tuple[int, int]]:
    rng = Random(seed)
    while True:
        points = list({(rng.randrange(1000), rng.randrange(1000)) for _ in range(4 * n)})[:n]
        if len(points) != n:
            continue
        if all(orient(points[i], points[j], points[k]) != 0
               for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n)):
            return points


def check_hull_partition() -> int:
    checked = 0
    for seed in range(20):
        points = random_general_position(9, seed)
        n = len(points)
        convex_sets: list[tuple[tuple[int, ...], int]] = []
        hull_fibres: dict[frozenset[int], int] = {}
        for mask in range(1 << n):
            indices = [i for i in range(n) if mask >> i & 1]
            if len(indices) < 3:
                continue
            hull = convex_hull(indices, points)
            hull_key = frozenset(hull)
            hull_fibres[hull_key] = hull_fibres.get(hull_key, 0) + 1
            if len(hull) != len(indices):
                continue
            interior = 0
            for p in range(n):
                if p in hull_key:
                    continue
                if all(orient(points[hull[i]], points[hull[(i + 1) % len(hull)]], points[p]) > 0
                       for i in range(len(hull))):
                    interior += 1
            convex_sets.append((hull, interior))
            assert hull_fibres[hull_key] <= 2**interior
        rhs = 1 + n + comb(n, 2) + sum(2**interior for _, interior in convex_sets)
        assert rhs == 2**n
        for hull, interior in convex_sets:
            assert hull_fibres[frozenset(hull)] == 2**interior
        checked += 1
    return checked


def nested_triangles(depth: int) -> list[tuple[Fraction, Fraction]]:
    """Rational, rapidly shrinking, rotating triangles around the origin."""
    base = [(Fraction(-3), Fraction(-2)),
            (Fraction(3), Fraction(-2)),
            (Fraction(0), Fraction(4))]
    a, b = 1, 0  # (3+4i)^level
    points: list[tuple[Fraction, Fraction]] = []
    for level in range(depth):
        denominator = 10**level * 5**level
        points.extend(
            (Fraction(a * x - b * y, denominator),
             Fraction(b * x + a * y, denominator))
            for x, y in base
        )
        a, b = 3 * a - 4 * b, 4 * a + 3 * b
    return points


def onion_depth(indices: list[int], points: list[tuple[Fraction, Fraction]]) -> int:
    remaining = indices
    depth = 0
    while remaining:
        depth += 1
        if len(remaining) <= 2:
            return depth
        layer = frozenset(convex_hull(remaining, points))
        remaining = [i for i in remaining if i not in layer]
    return depth


def brute_convex_profile(points: list[tuple[Fraction, Fraction]]) -> tuple[int, ...]:
    n = len(points)
    profile = [0] * (n + 1)
    for mask in range(1, 1 << n):
        indices = [i for i in range(n) if mask >> i & 1]
        if len(indices) <= 2 or len(convex_hull(indices, points)) == len(indices):
            profile[len(indices)] += 1
    return tuple(profile[1:])


def brute_convex_count(points: list[tuple[Fraction, Fraction]]) -> int:
    return sum(brute_convex_profile(points))


def cap_cup_totals(points: list[tuple[Fraction, Fraction]]) -> tuple[int, int]:
    ordered = sorted(points)
    n = len(ordered)
    cap = [[0] * n for _ in range(n)]
    cup = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            cap[i][j] = cup[i][j] = 1
            for h in range(i):
                if orient(ordered[h], ordered[i], ordered[j]) < 0:
                    cap[i][j] += cap[h][i]
                else:
                    cup[i][j] += cup[h][i]
    return n + sum(map(sum, cap)), n + sum(map(sum, cup))


def check_nested_triangle_barriers() -> tuple[int, list[tuple[int, int, int, int, Fraction]]]:
    # Check the explicit rational coordinates through eight layers.
    points = nested_triangles(8)
    assert all(orient(points[i], points[j], points[k]) != 0
               for i in range(len(points))
               for j in range(i + 1, len(points))
               for k in range(j + 1, len(points)))
    for level in range(7):
        outer = points[3 * level:3 * level + 3]
        for p in points[3 * (level + 1):]:
            assert all(orient(outer[i], outer[(i + 1) % 3], p) > 0 for i in range(3))

    # A multiplicative outer-cage/inner-set recurrence already fails at six points.
    six = nested_triangles(2)
    assert brute_convex_count(six[:3]) == 7
    assert brute_convex_count(six[3:]) == 7
    assert brute_convex_count(six) == 47 < 7 * 7
    assert brute_convex_profile(six) == (6, 15, 20, 6, 0, 0)

    # Exhaust the onion-depth distribution for up to five nested triangles.
    reports: list[tuple[int, int, int, int, Fraction]] = []
    masks_checked = 0
    for depth in range(1, 6):
        sample = nested_triangles(depth)
        n = len(sample)
        total_depth = 0
        for mask in range(1 << n):
            indices = [i for i in range(n) if mask >> i & 1]
            depth_of_mask = onion_depth(indices, sample)
            fully_selected_triangles = sum(
                (mask >> (3 * level)) & 7 == 7 for level in range(depth)
            )
            assert depth_of_mask >= fully_selected_triangles
            total_depth += depth_of_mask
            masks_checked += 1
        expectation = Fraction(total_depth, 1 << n)
        assert expectation >= Fraction(depth, 8)
        caps, cups = cap_cup_totals(sample)
        reports.append((depth, caps, cups, brute_convex_count(sample), expectation))
    return masks_checked, reports


def main() -> None:
    exact = check_exact_telescoping()
    profile = check_profile_fixed_point()
    local = check_standard_supersaturation_profile()
    phi = check_phi_formula()
    hull = check_hull_partition()
    onion_masks, onion_reports = check_nested_triangle_barriers()
    print(f"exact nested chains checked: {exact}")
    print(f"profile grid points checked: {profile}")
    print(f"local supersaturation grid points checked: {local}")
    print(f"piecewise local-target formulas checked: {phi}")
    print(f"exact 9-point hull partitions checked: {hull}")
    print(f"nested-triangle onion subsets checked: {onion_masks}")
    for depth, caps, cups, convex, expectation in onion_reports:
        print(
            f"  triangle layers={depth} caps={caps} cups={cups} "
            f"nonempty convex subsets={convex} "
            f"expected onion depth={float(expectation):.6f}"
        )
    print("all multiplicity-barrier checks: PASS")


if __name__ == "__main__":
    main()
