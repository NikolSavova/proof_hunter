#!/usr/bin/env python3
"""Exact homogeneous-blow-up test for the 58-point H>2 template.

The directional composition recurrence is evaluated only at ``t=1`` and
``t=1/2``.  This avoids constructing the enormous full rank profile while
remaining exact (Python integers and ``Fraction`` throughout).
"""

from __future__ import annotations

import json
from fractions import Fraction

from verify_apa_counterexample import rooted_paths
from verify_half_weight_counterexample import EXPECTED_PROFILE, points


def cap_cup_profiles(raw_points):
    """Return exact x-monotone cap and cup profiles, graded by vertices."""
    pts = tuple(sorted(raw_points))
    n = len(pts)
    profiles = []
    for sign in (+1, -1):
        profile = [0] * (n + 1)
        profile[1] = n
        for left in range(n - 1):
            paths = rooted_paths(pts, left, sign)
            for right in range(left + 1, n):
                for edges, count in enumerate(paths[right]):
                    if count:
                        profile[edges + 1] += count
        profiles.append(tuple(profile))
    return tuple(profiles)


def scaled_eval(profile, nt, shift, start):
    """Return sum(profile[j] * nt**(j-shift), j >= start)."""
    return sum(
        (Fraction(profile[j]) * nt ** (j - shift)
         for j in range(start, len(profile)) if profile[j]),
        Fraction(),
    )


def iterate_at(template, cap_profile, cup_profile, t, max_depth):
    """Evaluate the exact directional-composition recurrence at one t."""
    r = len(points())
    n = 1
    caps = t
    cups = t
    convex_nonempty = t
    values = []
    for depth in range(1, max_depth + 1):
        nt = n * t
        cap_factor = scaled_eval(cap_profile, nt, 1, 1)
        cup_factor = scaled_eval(cup_profile, nt, 1, 1)
        cross_factor = scaled_eval(template, nt, 2, 2)
        convex_nonempty = r * convex_nonempty + caps * cups * cross_factor
        caps *= cap_factor
        cups *= cup_factor
        n *= r
        values.append((n, 1 + convex_nonempty))
    return values


def main():
    template = EXPECTED_PROFILE
    cap_profile, cup_profile = cap_cup_profiles(points())
    assert sum(cap_profile[1:3]) == 58 + 1653
    assert sum(cup_profile[1:3]) == 58 + 1653

    unit = iterate_at(template, cap_profile, cup_profile, Fraction(1), 10)
    half = iterate_at(template, cap_profile, cup_profile, Fraction(1, 2), 10)
    rows = []
    for depth, ((n, z_one), (_, z_half)) in enumerate(zip(unit, half), 1):
        h_value = n * z_half / z_one
        rows.append(
            {
                "depth": depth,
                "n": n,
                "H": str(h_value),
                "H_decimal": float(h_value),
            }
        )

    assert rows[0]["H"] == "33994061/16990512"
    print(
        json.dumps(
            {
                "template_size": 58,
                "cap_profile": list(cap_profile),
                "cup_profile": list(cup_profile),
                "iterations": rows,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
