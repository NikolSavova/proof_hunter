#!/usr/bin/env python3
"""Exact probe for a hereditary/link strengthening of HW2.

For every convexly independent face T in a planar point configuration P,
test the closure-corrected candidate

    (n-|cl(T)|) * Z_link(T)(1/2)
        <= 2^(|T|+1) * Z_link(T)(1).

The empty face is HW2, while a hull triangle containing all other points no
longer gives an immediate false positive.  Exact integer arithmetic is used
after multiplying the half-weight sum by 2^(n-|T|).
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def is_general_position(points):
    n = len(points)
    return all(
        orient(points[i], points[j], points[k]) != 0
        for i in range(n)
        for j in range(i + 1, n)
        for k in range(j + 1, n)
    )


def is_convex_face(points, mask):
    ids = [i for i in range(len(points)) if mask >> i & 1]
    if len(ids) <= 3:
        return True
    ids.sort(key=lambda i: points[i])
    lower = []
    for i in ids:
        while len(lower) >= 2 and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(ids):
        while len(upper) >= 2 and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return len(lower[:-1] + upper[:-1]) == len(ids)


def closure_size(points, mask):
    ids = [i for i in range(len(points)) if mask >> i & 1]
    if len(ids) <= 2:
        return len(ids)
    ids.sort(key=lambda i: points[i])
    lower = []
    for i in ids:
        while len(lower) >= 2 and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(ids):
        while len(upper) >= 2 and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    polygon = lower[:-1] + upper[:-1]
    return sum(
        all(
            orient(points[polygon[j]], points[polygon[(j + 1) % len(polygon)]], p) >= 0
            for j in range(len(polygon))
        )
        for p in points
    )


def superset_zeta(values, n):
    out = values[:]
    for bit in range(n):
        step = 1 << bit
        for mask in range(1 << n):
            if not mask & step:
                out[mask] += out[mask | step]
    return out


def audit(points, label):
    assert is_general_position(points), label
    n = len(points)
    faces = [is_convex_face(points, mask) for mask in range(1 << n)]
    counts = superset_zeta([int(x) for x in faces], n)

    # weighted_scaled[T] = 2^(n-|T|) Z_link(T)(1/2)
    weighted_scaled = superset_zeta(
        [int(faces[mask]) * (1 << (n - mask.bit_count())) for mask in range(1 << n)],
        n,
    )

    worst = None
    for t, is_face in enumerate(faces):
        if not is_face:
            continue
        k = t.bit_count()
        # (n-|cl(T)|) Z <= 2^(k+1) V.  Clear denominator 2^(n-k).
        live = n - closure_size(points, t)
        lhs = live * weighted_scaled[t]
        rhs = (1 << (n + 1)) * counts[t]
        ratio = lhs / rhs
        record = (ratio, k, t, lhs, rhs, counts[t], live)
        if worst is None or record > worst:
            worst = record
        if lhs > rhs:
            return False, record, sum(faces)
    return True, worst, sum(faces)


def random_points(n, rng):
    while True:
        points = [(rng.randrange(10_000), rng.randrange(10_000)) for _ in range(n)]
        if len(set(points)) == n and is_general_position(points):
            return points


def saved_examples():
    direct = json.loads(
        (ROOT / "agent_lex_minimizer_search" / "direct_hull_certificates.json").read_text()
    )
    for key, item in direct.items():
        yield [tuple(p) for p in item["coordinates"]], f"direct-{key}"

    for name in ("exact_realizable_n8_independent.json", "exact_realizable_n9.json"):
        item = json.loads((ROOT / "agent_lex_minimizer_search" / name).read_text())
        yield [tuple(p) for p in item["coordinates_as_stored"]], name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--random", type=int, default=100)
    parser.add_argument("--max-n", type=int, default=12)
    parser.add_argument("--seed", type=int, default=838)
    args = parser.parse_args()
    rng = random.Random(args.seed)

    cases = list(saved_examples())
    for index in range(args.random):
        n = rng.randrange(4, args.max_n + 1)
        cases.append((random_points(n, rng), f"random-{index}-n{n}"))

    global_worst = None
    for points, label in cases:
        ok, record, face_count = audit(points, label)
        if global_worst is None or record[0] > global_worst[0]:
            global_worst = record + (label, face_count)
        if not ok:
            ratio, k, mask, lhs, rhs, count, live = record
            print(f"FAIL {label}: n={len(points)} k={k} mask={mask:#x}")
            print(
                f"ratio={ratio:.12g}, lhs={lhs}, rhs={rhs}, "
                f"link_faces={count}, live={live}"
            )
            print("points=", points)
            raise SystemExit(1)

    ratio, k, mask, lhs, rhs, count, live, label, face_count = global_worst
    print(f"PASS {len(cases)} configurations")
    print(
        f"worst={ratio:.12g} at {label}, k={k}, mask={mask:#x}, "
        f"link_faces={count}, live={live}, parent_faces={face_count}"
    )


if __name__ == "__main__":
    main()
