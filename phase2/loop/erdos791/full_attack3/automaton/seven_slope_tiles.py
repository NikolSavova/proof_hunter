#!/usr/bin/env python3
"""Exact seven-slope K7 carry tiles modulo B=t^2."""

from __future__ import annotations

from math import gcd


SLOPES = (0, 10, 12, 15, 20, 30, 60)
PHASE_RADIUS = 120


def pair_parameters(a: int, b: int) -> dict[str, int | bool]:
    if not 0 <= a < b:
        raise ValueError((a, b))
    d = b - a
    divisible = (a * b) % d == 0
    if not divisible:
        return {"a": a, "b": b, "d": d, "divides_ab": False}
    u = a * a // d
    v = b * b // d
    h = a * b // d
    return {
        "a": a,
        "b": b,
        "d": d,
        "divides_ab": True,
        "u": u,
        "v": v,
        "h": h,
        "required_radius": max(v, u + v - b),
    }


def analytic_audit(t: int) -> list[dict[str, int | bool]]:
    rows = []
    for index, a in enumerate(SLOPES):
        for b in SLOPES[index + 1 :]:
            row = pair_parameters(a, b)
            if not row["divides_ab"]:
                rows.append(row)
                continue
            u, v, h = int(row["u"]), int(row["v"]), int(row["h"])
            p = (t - h, u)
            q = (-v, t - b + v)
            row.update(
                {
                    "p0": p[0],
                    "p1": p[1],
                    "q0": q[0],
                    "q1": q[1],
                    "kernel_p": (t + a) * p[0] + (t + b) * p[1],
                    "kernel_q": (t + a) * q[0] + (t + b) * q[1],
                    "determinant": p[0] * q[1] - p[1] * q[0],
                    "bounds_fit": -PHASE_RADIUS <= -v
                    and t - h <= t - 1 + PHASE_RADIUS
                    and t - b + u + v - 1 <= t - 1 + PHASE_RADIUS,
                }
            )
            rows.append(row)
    return rows


def tile(t: int, a: int) -> set[int]:
    """Canonical residues of the enlarged slope-(t+a) AP."""
    B = t * t
    return {
        (i * (t + a)) % B
        for i in range(-PHASE_RADIUS, t + PHASE_RADIUS)
    }


def admissible_scale(t: int) -> bool:
    return (
        t > max(int(pair_parameters(a, b).get("h", 0)) for i, a in enumerate(SLOPES) for b in SLOPES[i + 1 :])
        and t * t > t + 2 * PHASE_RADIUS
        and all(a == 0 or gcd(a, t) == 1 for a in SLOPES)
    )


def macro_coverage(placement: dict[int, set[int]], limit: int) -> set[int]:
    """Squares certified by one pair edge at two consecutive carry states."""
    covered: set[int] = set()
    for index, a in enumerate(SLOPES):
        for b in SLOPES[index + 1 :]:
            sums = {x + y for x in placement[a] for y in placement[b]}
            covered |= {q for q in sums if q - 1 in sums and 0 <= q < limit}
    return covered


def prefix_length(covered: set[int]) -> int:
    q = 0
    while q in covered:
        q += 1
    return q
