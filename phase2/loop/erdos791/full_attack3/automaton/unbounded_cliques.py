#!/usr/bin/env python3
"""General K_r slope family with fixed endpoint-phase overhead."""

from __future__ import annotations

from math import gcd, lcm


def slope_family(r: int) -> tuple[int, ...]:
    if r < 2:
        raise ValueError(r)
    M = lcm(*range(1, r))
    return tuple(i * M for i in range(r))


def pair_parameters(a: int, b: int) -> dict[str, int]:
    if not 0 <= a < b or (a * b) % (b - a):
        raise ValueError((a, b))
    d = b - a
    u, v, h = a * a // d, b * b // d, a * b // d
    return {
        "a": a,
        "b": b,
        "d": d,
        "u": u,
        "v": v,
        "h": h,
        "required_radius": max(v, u + v - b),
    }


def phase_radius(r: int) -> int:
    D = slope_family(r)
    return max(pair_parameters(a, b)["required_radius"] for i, a in enumerate(D) for b in D[i + 1 :])


def tile(t: int, a: int, C: int) -> set[int]:
    B = t * t
    return {(i * (t + a)) % B for i in range(-C, t + C)}


def admissible_scale(t: int, r: int) -> bool:
    D = slope_family(r)
    C = phase_radius(r)
    maximum_h = max(
        pair_parameters(a, b)["h"]
        for index, a in enumerate(D)
        for b in D[index + 1 :]
    )
    return t > maximum_h and t * t > t + 2 * C and all(a == 0 or gcd(a, t) == 1 for a in D)


def analytic_audit(t: int, r: int) -> list[dict[str, int | bool]]:
    D, C = slope_family(r), phase_radius(r)
    rows = []
    for index, a in enumerate(D):
        for b in D[index + 1 :]:
            row: dict[str, int | bool] = pair_parameters(a, b)
            u, v, h = int(row["u"]), int(row["v"]), int(row["h"])
            p, q = (t - h, u), (-v, t - b + v)
            row.update(
                {
                    "kernel_p": (t + a) * p[0] + (t + b) * p[1],
                    "kernel_q": (t + a) * q[0] + (t + b) * q[1],
                    "determinant": p[0] * q[1] - p[1] * q[0],
                    "bounds_fit": -C <= -v
                    and t - h <= t - 1 + C
                    and t - b + u + v - 1 <= t - 1 + C,
                }
            )
            rows.append(row)
    return rows
