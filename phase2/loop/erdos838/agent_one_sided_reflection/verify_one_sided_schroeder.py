#!/usr/bin/env python3
"""Exact audit for ONE_SIDED_SCHROEDER_TREE.md.

The script uses only integer/Fraction arithmetic.  It enumerates every
separable permutation through seven gaps (eight points), constructs its
one-sided chirotope and a recursive rational realization, and checks the
classification, cup-cap product, and face counts.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations
import json
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent


def pattern(values: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    order = {v: i + 1 for i, v in enumerate(sorted(values))}
    return tuple(order[v] for v in values)


def avoids_forbidden(perm: tuple[int, ...]) -> bool:
    for ii in combinations(range(len(perm)), 4):
        pat = pattern([perm[i] for i in ii])
        if pat in ((2, 4, 1, 3), (3, 1, 4, 2)):
            return False
    return True


def standardize(values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted(values).index(x) for x in values)


def decompose(perm: tuple[int, ...]):
    """Return a binary direct/skew decomposition, or None."""
    if len(perm) == 1:
        return ("leaf",)
    for cut in range(1, len(perm)):
        left, right = perm[:cut], perm[cut:]
        if max(left) < min(right):
            dl, dr = decompose(standardize(left)), decompose(standardize(right))
            if dl is not None and dr is not None:
                return ("+", dl, dr)
        if min(left) > max(right):
            dl, dr = decompose(standardize(left)), decompose(standardize(right))
            if dl is not None and dr is not None:
                return ("-", dl, dr)
    return None


def slopes_from_tree(tree) -> list[Fraction]:
    if tree[0] == "leaf":
        return [Fraction(0)]
    sign, lt, rt = tree
    left = slopes_from_tree(lt)
    right = slopes_from_tree(rt)
    m = len(left) + len(right)
    eta = Fraction(1, 4 * m)

    def compress(values: list[Fraction], lo: Fraction) -> list[Fraction]:
        low, high = min(values), max(values)
        if low == high:
            return [lo + eta / 2 for _ in values]
        return [lo + eta * (x - low) / (high - low) for x in values]

    if sign == "+":
        return compress(left, Fraction(0)) + compress(right, Fraction(1))
    return compress(left, Fraction(1)) + compress(right, Fraction(0))


def points_from_tree(tree) -> list[tuple[Fraction, Fraction]]:
    slopes = slopes_from_tree(tree)
    points = [(Fraction(0), Fraction(0))]
    for e in slopes:
        x, y = points[-1]
        points.append((x + 1, y + e))
    return points


def orient_points(points, i: int, j: int, k: int) -> int:
    xi, yi = points[i]
    xj, yj = points[j]
    xk, yk = points[k]
    det = (xj - xi) * (yk - yi) - (yj - yi) * (xk - xi)
    return (det > 0) - (det < 0)


def sign_from_perm(perm: tuple[int, ...], i: int, k: int) -> int:
    return 1 if perm[i] < perm[k - 1] else -1


def audit_closure(perm: tuple[int, ...]) -> None:
    n = len(perm) + 1
    for a, b, c, d in combinations(range(n), 4):
        sac = sign_from_perm(perm, a, c)
        sbd = sign_from_perm(perm, b, d)
        sad = sign_from_perm(perm, a, d)
        assert sac != sbd or sad == sac


def exhaustive_closure_assignments(n: int) -> set[tuple[int, ...]]:
    """Enumerate every abstract interval-sign assignment via gap tournaments.

    This is independent of permutation generation: all 2^(m choose 2)
    tournaments on the m=n-1 naturally ordered gaps are tested against the
    four-point closure law.
    """
    m = n - 1
    pairs = list(combinations(range(m), 2))
    accepted: set[tuple[int, ...]] = set()
    for bits in range(1 << len(pairs)):
        compare: dict[tuple[int, int], int] = {}
        for bit, pair in enumerate(pairs):
            compare[pair] = 1 if bits >> bit & 1 else -1

        def s(i: int, k: int) -> int:
            return compare[(i, k - 1)]

        closed = True
        for a, b, c, d in combinations(range(n), 4):
            if s(a, c) == s(b, d) and s(a, d) != s(a, c):
                closed = False
                break
        if not closed:
            continue

        # Rank of a gap in the alleged total order: number of predecessors.
        rank = [0] * m
        for p, q in pairs:
            if compare[(p, q)] == 1:
                rank[q] += 1
            else:
                rank[p] += 1
        assert sorted(rank) == list(range(m)), (n, bits, rank)
        perm = tuple(rank)
        assert avoids_forbidden(perm)
        accepted.add(perm)
    return accepted


def audit_realization(perm: tuple[int, ...], tree) -> list[tuple[Fraction, Fraction]]:
    points = points_from_tree(tree)
    assert len(points) == len(perm) + 1
    adjacent = []
    for i in range(len(perm)):
        adjacent.append(points[i + 1][1] - points[i][1])
    assert pattern(adjacent) == tuple(x + 1 for x in perm)
    for i, j, k in combinations(range(len(points)), 3):
        got = orient_points(points, i, j, k)
        want = sign_from_perm(perm, i, k)
        assert got == want, (perm, tree, (i, j, k), got, want, points)
    return points


def is_cup(mask: int, perm: tuple[int, ...], wanted: int) -> bool:
    selected = [i for i in range(len(perm) + 1) if mask >> i & 1]
    for i, j, k in combinations(selected, 3):
        if sign_from_perm(perm, i, k) != wanted:
            return False
    return True


def convex_hull_size(mask: int, perm: tuple[int, ...]) -> int:
    selected = [i for i in range(len(perm) + 1) if mask >> i & 1]
    if len(selected) <= 2:
        return len(selected)

    def orient(i: int, j: int, k: int) -> int:
        return sign_from_perm(perm, i, k)

    lower: list[int] = []
    for x in selected:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], x) <= 0:
            lower.pop()
        lower.append(x)
    upper_inc: list[int] = []
    for x in selected:
        while len(upper_inc) >= 2 and orient(upper_inc[-2], upper_inc[-1], x) >= 0:
            upper_inc.pop()
        upper_inc.append(x)
    return len(set(lower + upper_inc))


def statistics(perm: tuple[int, ...]) -> dict[str, int]:
    n = len(perm) + 1
    cups = caps = faces = 0
    p = q = 0
    for mask in range(1 << n):
        size = mask.bit_count()
        cup = is_cup(mask, perm, 1)
        cap = is_cup(mask, perm, -1)
        cups += cup
        caps += cap
        if cup:
            p = max(p, size)
        if cap:
            q = max(q, size)
        convex = convex_hull_size(mask, perm) == size
        faces += convex
        assert convex == (cup or cap), (perm, mask, cup, cap)
    assert faces == cups + caps - (1 + n + comb(n, 2))
    assert (p - 1) * (q - 1) >= n - 1
    return {"cups": cups, "caps": caps, "faces": faces, "p": p, "q": q}


def main() -> None:
    expected_counts = {3: 2, 4: 6, 5: 22, 6: 90, 7: 394, 8: 1806}
    expected_min_faces = {3: 8, 4: 15, 5: 27, 6: 45, 7: 73, 8: 114}
    records = []

    # Independent brute-force audit that closure itself forces exactly the
    # separable permutations.  Stopping at n=7 keeps the verifier quick; the
    # permutation-side enumeration below continues through n=8.
    for n in range(3, 8):
        by_closure = exhaustive_closure_assignments(n)
        by_avoidance = {
            p for p in permutations(range(n - 1)) if avoids_forbidden(p)
        }
        assert by_closure == by_avoidance

    for n in range(3, 9):
        members = []
        min_faces = 1 << n
        min_product_slack = 10**9
        witnesses = []
        for perm in permutations(range(n - 1)):
            avoiding = avoids_forbidden(perm)
            tree = decompose(perm)
            assert avoiding == (tree is not None), perm
            if not avoiding:
                continue
            audit_closure(perm)
            audit_realization(perm, tree)
            stats = statistics(perm)
            members.append(perm)
            slack = (stats["p"] - 1) * (stats["q"] - 1) - (n - 1)
            min_product_slack = min(min_product_slack, slack)
            if stats["faces"] < min_faces:
                min_faces = stats["faces"]
                witnesses = [perm]
            elif stats["faces"] == min_faces:
                witnesses.append(perm)

        assert len(members) == expected_counts[n]
        assert min_faces == expected_min_faces[n]
        assert min_product_slack == 0
        row = {
            "n": n,
            "one_sided_systems": len(members),
            "minimum_convex_subsets": min_faces,
            "minimum_product_slack": min_product_slack,
            "first_minimizer": list(witnesses[0]),
            "number_of_minimizers": len(witnesses),
        }
        records.append(row)
        print(
            f"n={n}: systems={len(members)}, min V={min_faces}, "
            f"min product slack={min_product_slack}"
        )

    # Algebra in the sparse-defect corollary: if
    # E <= n^2/(8 log^4 n), then n+32E <= n+4n^2/log^4 n,
    # so the Caro--Wei core has asymptotic size at least log^4(n)/4.
    for exponent in (16, 24, 32, 48, 64):
        n = 1 << exponent
        core_lower = Fraction(n * n, n + Fraction(4 * n * n, exponent**4))
        assert core_lower / exponent**4 < Fraction(1, 4)
        assert core_lower / exponent**4 > Fraction(1, 4) - Fraction(exponent**4, 16 * n)

    certificate = {
        "description": "exact one-sided/Schroeder classification and cup-cap product audit",
        "arithmetic": "integer and fractions.Fraction only",
        "records": records,
        "assertions": [
            "all abstract closure assignments through n=7 exhaust exactly the avoiding permutations",
            "avoidance of 2413/3142 iff recursive direct/skew decomposition",
            "four-point closure for every classified sign system",
            "exact rational realization with sign(i,j,k)=compare(pi_i,pi_(k-1))",
            "every convex subset is a cup or cap",
            "(maximum cup - 1)(maximum cap - 1) >= n - 1",
            "Caro-Wei plus E-product constants checked algebraically",
        ],
    }
    out = HERE / "one_sided_schroeder_certificate.json"
    out.write_text(json.dumps(certificate, indent=2) + "\n")
    print(f"PASS: wrote {out}")


if __name__ == "__main__":
    main()
