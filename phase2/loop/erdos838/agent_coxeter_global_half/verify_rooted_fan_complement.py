#!/usr/bin/env python3
"""Exact verifier for ROOTED_FAN_COMPLEMENT_DICHOTOMY.md."""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from math import ceil, comb


Point = tuple[Q, Q]
Root = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> Q:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def normalize(points: tuple[Point, ...]) -> tuple[Point, ...]:
    if len(points) == 1:
        return ((Q(0), Q(0)),)
    xs = [point[0] for point in points]
    ys = [point[1] for point in points]
    dx = max(xs) - min(xs)
    dy = max(ys) - min(ys)
    return tuple(
        (
            (x - min(xs)) / dx if dx else Q(0),
            (y - min(ys)) / dy if dy else Q(0),
        )
        for x, y in points
    )


def slope_bound(points: tuple[Point, ...]) -> Q:
    return max(
        (
            abs((b[1] - a[1]) / (b[0] - a[0]))
            for a, b in combinations(points, 2)
        ),
        default=Q(0),
    )


def separated(left: tuple[Point, ...], right: tuple[Point, ...]) -> tuple[Point, ...]:
    a = normalize(left)
    b = normalize(right)
    height = ceil(3 * max(slope_bound(a), slope_bound(b)) + 5)
    out = tuple((x, y + height) for x, y in a) + tuple(
        (x + 2, y) for x, y in b
    )
    assert len({point[0] for point in out}) == len(out)
    return out


@lru_cache(None)
def cup_cap_set(r: int, s: int) -> tuple[Point, ...]:
    """Classical rational set with no r-cup and no s-cap."""
    assert r >= 2 and s >= 2
    if r == 2 or s == 2:
        return ((Q(0), Q(0)),)
    return separated(cup_cap_set(r, s - 1), cup_cap_set(r - 1, s))


def cup_cap_lengths(points: tuple[Point, ...]) -> tuple[int, int]:
    cup: dict[tuple[int, int], int] = {}
    cap: dict[tuple[int, int], int] = {}
    for j in range(1, len(points)):
        for k in range(j + 1, len(points)):
            cup[(j, k)] = cap[(j, k)] = 2
            for i in range(j):
                sign = orient(points[i], points[j], points[k])
                assert sign
                if sign > 0:
                    cup[(j, k)] = max(cup[(j, k)], cup.get((i, j), 2) + 1)
                else:
                    cap[(j, k)] = max(cap[(j, k)], cap.get((i, j), 2) + 1)
    return max(cup.values(), default=1), max(cap.values(), default=1)


def genericize(points: tuple[Point, ...]) -> tuple[Point, ...]:
    """Break parallelisms by an exact sign-preserving vertical perturbation."""
    coefficients = tuple(Q(2) ** index for index in range(len(points)))
    ratios = []
    for i, j, k in combinations(range(len(points)), 3):
        base = orient(points[i], points[j], points[k])
        change = orient(
            (points[i][0], coefficients[i]),
            (points[j][0], coefficients[j]),
            (points[k][0], coefficients[k]),
        )
        assert base
        if change:
            ratios.append(abs(base / change))
    epsilon = min(ratios, default=Q(2)) / 2
    base_signs = {
        triple: orient(*(points[index] for index in triple))
        for triple in combinations(range(len(points)), 3)
    }
    for _ in range(20):
        perturbed = tuple(
            (points[index][0], points[index][1] + epsilon * coefficients[index])
            for index in range(len(points))
        )
        assert all(
            orient(*(perturbed[index] for index in triple)) * sign > 0
            for triple, sign in base_signs.items()
        )
        slopes = [
            (perturbed[j][1] - perturbed[i][1])
            / (perturbed[j][0] - perturbed[i][0])
            for i, j in combinations(range(len(perturbed)), 2)
        ]
        if len(slopes) == len(set(slopes)):
            return perturbed
        epsilon /= 2
    raise AssertionError("failed to break all parallelisms")


def add_coherent_root(points: tuple[Point, ...], sign: int) -> tuple[Point, ...]:
    """Add a leftmost root whose star has the prescribed sign."""
    root_x = min(point[0] for point in points) - 1
    low = min(point[1] for point in points)
    high = max(point[1] for point in points)
    height = Q(1)
    for _ in range(100):
        # A root far above has positive star triples; far below has negative.
        root = (root_x, high + height) if sign > 0 else (root_x, low - height)
        out = (root,) + points
        if all(
            orient(root, points[i], points[j]) * sign > 0
            for i, j in combinations(range(len(points)), 2)
        ):
            slopes = [
                (out[j][1] - out[i][1]) / (out[j][0] - out[i][0])
                for i, j in combinations(range(len(out)), 2)
            ]
            if len(slopes) == len(set(slopes)):
                return out
        height *= 2
    raise AssertionError("failed to add a generic coherent root")


def root_order(points: tuple[Point, ...]) -> tuple[Root, ...]:
    decorated = sorted(
        (
            (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]),
            i,
            j,
        )
        for i, j in combinations(range(len(points)), 2)
    )
    assert len({item[0] for item in decorated}) == len(decorated)
    roots = tuple((i, j) for _, i, j in decorated)
    wires = list(range(len(points)))
    for i, j in roots:
        left = wires.index(i)
        right = wires.index(j)
        assert abs(left - right) == 1
        generator = min(left, right)
        assert wires[generator] < wires[generator + 1]
        wires[generator], wires[generator + 1] = (
            wires[generator + 1],
            wires[generator],
        )
    assert wires == list(reversed(range(len(points))))
    return roots


def convex_hull_size(points: tuple[Point, ...]) -> int:
    ordered = sorted(points)

    def half(sequence) -> list[Point]:
        out: list[Point] = []
        for point in sequence:
            while len(out) >= 2 and orient(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out

    lower = half(ordered)
    upper = half(reversed(ordered))
    return len(lower[:-1] + upper[:-1])


def audit_es_row(k: int) -> dict[str, int]:
    base = cup_cap_set(k, k)
    assert len(base) == comb(2 * k - 4, k - 2)
    cup_length, cap_length = cup_cap_lengths(base)
    assert (cup_length, cap_length) == (k - 1, k - 1)

    points = genericize(base)
    assert cup_cap_lengths(points) == (cup_length, cap_length)
    triples = tuple(combinations(range(len(points)), 3))
    positive = sum(orient(*(points[index] for index in triple)) > 0 for triple in triples)
    negative = len(triples) - positive
    sign = 1 if positive >= negative else -1
    promoted = max(positive, negative)
    assert promoted * 2 >= len(triples)

    rooted = add_coherent_root(points, sign)
    roots = root_order(rooted)
    positions = {root: index for index, root in enumerate(roots)}
    assert all(
        orient(rooted[0], rooted[i], rooted[j]) * sign > 0
        for i, j in combinations(range(1, len(rooted)), 2)
    )

    temporal_promoted = 0
    convex_promoted = 0
    for a, b, c in combinations(range(1, len(rooted)), 3):
        same_sign = orient(rooted[a], rooted[b], rooted[c]) * sign > 0
        times = (positions[(0, a)], positions[(a, b)], positions[(b, c)])
        temporal = times[0] < times[1] < times[2] if sign > 0 else times[0] > times[1] > times[2]
        assert temporal == same_sign
        if temporal:
            temporal_promoted += 1
            convex_promoted += convex_hull_size(
                (rooted[0], rooted[a], rooted[b], rooted[c])
            ) == 4
    assert temporal_promoted == promoted
    assert convex_promoted == promoted

    opposite_length = cap_length if sign > 0 else cup_length
    m = len(points)
    for length in range(1, m // 2 + 1):
        if opposite_length < length:
            assert Q(promoted) > Q(m**3, 8 * length**2)

    convex_rank_bound = 2 * k - 4
    assert (1 << convex_rank_bound) <= (2 * k - 3) * m
    return {
        "k": k,
        "m": m,
        "promoted": promoted,
        "cup_rank": cup_length,
        "cap_rank": cap_length,
        "convex_rank_bound": convex_rank_bound,
        "max_rooted_cell_bank": 1 << (convex_rank_bound - 1),
        "max_complement_bank": 1 << convex_rank_bound,
    }


def audit_zero_triple_family(m: int = 24) -> dict[str, int]:
    # A strict cap W and a root far above it give a coherent positive star
    # and no positive complementary triple.
    base = tuple((Q(i), -Q(i * i)) for i in range(1, m + 1))
    points = genericize(base)
    assert cup_cap_lengths(points) == (2, m)
    rooted = add_coherent_root(points, 1)
    roots = root_order(rooted)
    positions = {root: index for index, root in enumerate(roots)}
    promoted = 0
    for a, b, c in combinations(range(1, m + 1), 3):
        times = (positions[(0, a)], positions[(a, b)], positions[(b, c)])
        promoted += times[0] < times[1] < times[2]
    assert promoted == 0
    return {"m": m, "promoted": promoted, "external_bank": 1 << m}


def main() -> None:
    zero = audit_zero_triple_family()
    rows = [audit_es_row(k) for k in (4, 5, 6)]
    print("rooted-fan complementary dichotomy: PASS")
    print(
        f"zero-triple fan m={zero['m']} promoted={zero['promoted']} "
        f"external_bank={zero['external_bank']}"
    )
    for row in rows:
        print(
            f"E({row['k']},{row['k']}) m={row['m']:2d} "
            f"promoted={row['promoted']:5d} cup/cap="
            f"({row['cup_rank']},{row['cap_rank']}) "
            f"banks(root,complement)="
            f"({row['max_rooted_cell_bank']},{row['max_complement_bank']})"
        )


if __name__ == "__main__":
    main()
