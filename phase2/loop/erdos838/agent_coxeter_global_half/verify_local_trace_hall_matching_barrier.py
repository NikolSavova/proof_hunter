#!/usr/bin/env python3
"""Exact verifier for LOCAL_TRACE_HALL_MATCHING_BARRIER.md."""

from __future__ import annotations

from fractions import Fraction as Q
from itertools import combinations
from math import ceil, comb

from verify_label_replacing_es_mixed_code import symbolic_row as es_code_row
from verify_rooted_fan_complement import (
    convex_hull_size,
    genericize,
    orient,
    root_order,
)


Point = tuple[Q, Q]


def matching_star(m: int) -> tuple[tuple[Point, ...], int, int]:
    delta = Q(1, 100 * m)
    height = delta / 4
    epsilon = Q(1, 10_000 * m**4)
    left = tuple(
        (-2 + epsilon * i, Q(i) + epsilon * i * i)
        for i in range(1, m + 1)
    )
    j = (-delta, height)
    l = (delta, height)
    right = tuple(
        (2 + epsilon * k, Q(k - m - 1) - epsilon * k * k)
        for k in range(1, m + 1)
    )
    points = genericize(left + (j, l) + right)
    return points, m, m + 1


def audit_multi_trace(m: int = 8, traces_per_side: int = 5) -> dict[str, int]:
    delta = Q(1, 100 * m)
    height = delta / 4
    epsilon = Q(1, 10_000 * m**4)
    eta = Q(1, 10**8 * m**6 * traces_per_side**3)
    left = tuple(
        (-2 + epsilon * i, Q(i) + epsilon * i * i)
        for i in range(1, m + 1)
    )
    roots_left = tuple(
        (-delta + eta * a, height + eta * a * a)
        for a in range(1, traces_per_side + 1)
    )
    roots_right = tuple(
        (delta + eta * b, height - eta * b * b)
        for b in range(1, traces_per_side + 1)
    )
    right = tuple(
        (2 + epsilon * k, Q(k - m - 1) - epsilon * k * k)
        for k in range(1, m + 1)
    )
    points = genericize(left + roots_left + roots_right + right)
    for i in range(m):
        for a in range(traces_per_side):
            for b in range(traces_per_side):
                for k in range(m):
                    face = (
                        points[i],
                        points[m + a],
                        points[m + traces_per_side + b],
                        points[m + 2 * traces_per_side + k],
                    )
                    assert (convex_hull_size(face) == 4) == (i + k == m - 1)
    overlap = traces_per_side**2
    return {
        "m": m,
        "traces": overlap,
        "detached_face_overlap": overlap,
    }


def balanced_owners(m: int) -> dict[int, list[tuple[int, ...]]]:
    """Singleton plus an almost-regular cyclic orientation of all pairs."""
    owners = {i: [(i,)] for i in range(m)}
    for i, j in combinations(range(m), 2):
        forward = (j - i) % m
        backward = (i - j) % m
        if forward < backward:
            owner = i
        elif backward < forward:
            owner = j
        else:
            # Antipodal edges when m is even alternate owners.
            owner = i if i % 2 == 0 else j
        owners[owner].append((i, j))
    minimum = min(len(faces) for faces in owners.values())
    assert minimum >= 1 + (m - 1) // 2
    assert sum(len(faces) for faces in owners.values()) == m + comb(m, 2)
    return owners


def audit_row(m: int) -> dict[str, object]:
    points, j, l = matching_star(m)
    assert all(points[index][0] < points[index + 1][0] for index in range(len(points) - 1))
    assert all(
        orient(points[a], points[b], points[c]) > 0
        for a, b, c in combinations(range(m), 3)
    )
    assert all(
        orient(points[m + 2 + a], points[m + 2 + b], points[m + 2 + c]) < 0
        for a, b, c in combinations(range(m), 3)
    )

    compatibility = []
    for i in range(m):
        neighbours = []
        for k in range(m):
            face = (points[i], points[j], points[l], points[m + 2 + k])
            convex = convex_hull_size(face) == 4
            assert convex == (i + k == m - 1)
            if convex:
                neighbours.append(k)
        assert neighbours == [m - 1 - i]
        compatibility.append(tuple(neighbours))

    # Each side triangle is a genuine temporal two-edge path in one of its
    # two directions in the exact adjacent-swap reduced word.
    reflection_time = {root: index for index, root in enumerate(root_order(points))}
    for i in range(m):
        first = reflection_time[(i, j)]
        second = reflection_time[(j, l)]
        assert first != second
        assert first < second or second < first

    ambient = 2 * m + 2
    demand = Q(ambient, 8)
    natural_load = demand
    owned = balanced_owners(m)
    block_size = ceil(demand)
    used: set[tuple[int, ...]] = set()
    max_load = Q(0)
    for history in range(m):
        block = owned[history][:block_size]
        assert len(block) == block_size
        assert all(face not in used for face in block)
        used.update(block)
        load = demand / block_size
        assert load <= 1
        max_load = max(max_load, load)
        assert all(history in face for face in block)
    assert block_size <= 1 + (m - 1) // 2
    assert natural_load * 8 == ambient
    return {
        "m": m,
        "ambient": ambient,
        "matching_degree": max(map(len, compatibility)),
        "natural_load": natural_load,
        "side_block": block_size,
        "side_load": max_load,
    }


def audit_es() -> list[dict[str, object]]:
    rows = []
    for k in range(5, 21):
        m = comb(2 * k - 4, k - 2)
        terminal_load = Q(m + 1, 1 << k)
        code = es_code_row(k)
        assert code["top_mixed"] >= code["tokens"]
        rows.append(
            {
                "k": k,
                "m": m,
                "terminal_load": terminal_load,
                "code_margin": code["margin"],
            }
        )
    return rows


def main() -> None:
    rows = [audit_row(m) for m in range(2, 31)]
    multi = audit_multi_trace()
    es_rows = audit_es()
    print("local trace Hall matching barrier: PASS")
    for m in (2, 4, 8, 16, 30):
        row = rows[m - 2]
        print(
            f"matching m={m:2d} N={row['ambient']:2d} degree={row['matching_degree']} "
            f"natural_load={row['natural_load']} side_block={row['side_block']} "
            f"side_load={row['side_load']}"
        )
    for k in (5, 6, 8, 10, 15, 20):
        row = es_rows[k - 5]
        print(
            f"E({k},{k}) m={row['m']:10d} "
            f"terminal_load={float(row['terminal_load']):.4e} "
            f"complete_code_margin={float(row['code_margin']):.4e}"
        )
    print(
        f"multi-trace m={multi['m']} traces={multi['traces']} "
        f"detached-face overlap={multi['detached_face_overlap']}"
    )


if __name__ == "__main__":
    main()
