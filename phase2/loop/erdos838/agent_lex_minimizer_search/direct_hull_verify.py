#!/usr/bin/env python3
"""Direct, evaluator-independent hull census for the integer winners."""

from __future__ import annotations

import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def census(points):
    n = len(points)
    # First audit general position directly over all triples.
    determinants = [
        abs(orient(points[i], points[j], points[k]))
        for i, j, k in itertools.combinations(range(n), 3)
    ]
    if not determinants or min(determinants) == 0:
        raise AssertionError("not in general position")
    profile = [0] * (n + 1)
    for mask in range(1, 1 << n):
        selected = [points[i] for i in range(n) if (mask >> i) & 1]
        if len(selected) <= 2 or len(hull(selected)) == len(selected):
            profile[len(selected)] += 1
    return {
        "n": n,
        "minimum_absolute_orientation_determinant": min(determinants),
        "profile_nonempty": profile,
        "nonempty_count": sum(profile),
        "empty_inclusive_count": 1 + sum(profile),
        "first_moment_nonempty": sum(k * x for k, x in enumerate(profile)),
        "second_raw_moment_nonempty": sum(k * k * x for k, x in enumerate(profile)),
    }


def main():
    rows = {}
    for n, filename in [(8, "exact_realizable_n8_independent.json"), (9, "exact_realizable_n9.json")]:
        data = json.loads((HERE / filename).read_text())
        points = [tuple(p) for p in data["coordinates_as_stored"]]
        rows[str(n)] = {"coordinates": points, **census(points)}
    (HERE / "direct_hull_certificates.json").write_text(
        json.dumps(rows, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
