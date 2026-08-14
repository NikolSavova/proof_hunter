#!/usr/bin/env python3
"""Exact graded recurrences for the balanced Pascal-template construction.

This file is deliberately independent of ``agent_upper_multitype``.  It
computes the cap, cup, and convex-subset polynomials for a Pascal cell and
for its iterated almost-vertical blow-up.  It also has a scalar first-moment
mode, which reaches depths for which the full coefficient arrays are too
large.

All polynomials use the vertex-count grading: coefficient j counts j-point
objects.  Python integers make every reported finite calculation exact.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass


Poly = list[int]
Cell = tuple[int, Poly, Poly, Poly]


def add(left: Poly, right: Poly, cutoff: int) -> Poly:
    return [
        (left[i] if i < len(left) else 0)
        + (right[i] if i < len(right) else 0)
        for i in range(cutoff + 1)
    ]


def mul(left: Poly, right: Poly, cutoff: int) -> Poly:
    result = [0] * (cutoff + 1)
    for i, a in enumerate(left[: cutoff + 1]):
        if not a:
            continue
        for j, b in enumerate(right[: cutoff + 1 - i]):
            if b:
                result[i + j] += a * b
    return result


def optional_point(poly: Poly, population: int, cutoff: int) -> Poly:
    """Return poly(z)*(1+population*z), truncated at cutoff."""
    result = (poly + [0] * (cutoff + 1))[: cutoff + 1]
    for degree in range(1, cutoff + 1):
        result[degree] += population * (
            poly[degree - 1] if degree - 1 < len(poly) else 0
        )
    return result


def pascal_row(m: int, cutoff: int) -> list[Cell]:
    singleton = (
        1,
        [0, 1] + [0] * (cutoff - 1),
        [0, 1] + [0] * (cutoff - 1),
        [0, 1] + [0] * (cutoff - 1),
    )
    old = [singleton]
    for level in range(1, m + 1):
        new = [singleton]
        for i in range(1, level):
            na, ca, ua, va = old[i - 1]
            nb, cb, ub, vb = old[i]
            # Strong glue A prec B: a cap is in B, or a cap in A with
            # zero/one B point.  Cups are the reflected formula.
            caps = add(optional_point(ca, nb, cutoff), cb, cutoff)
            cups = add(ua, optional_point(ub, na, cutoff), cutoff)
            convex = add(add(va, vb, cutoff), mul(ca, ub, cutoff), cutoff)
            new.append((na + nb, caps, cups, convex))
        new.append(singleton)
        old = new
    return old


def vertical_iterate(template: Cell, depth: int, cutoff: int) -> Cell:
    r, template_caps, template_cups, template_convex = template
    n = 1
    caps = [0, 1] + [0] * (cutoff - 1)
    cups = caps[:]
    convex = caps[:]
    for _ in range(depth):
        new_caps = [0] * (cutoff + 1)
        new_cups = [0] * (cutoff + 1)
        new_convex = [r * value for value in convex]
        for a in range(1, cutoff + 1):
            if caps[a]:
                for j in range(1, min(cutoff - a + 2, len(template_caps))):
                    if template_caps[j]:
                        new_caps[a + j - 1] += (
                            caps[a] * template_caps[j] * n ** (j - 1)
                        )
            if cups[a]:
                for j in range(1, min(cutoff - a + 2, len(template_cups))):
                    if template_cups[j]:
                        new_cups[a + j - 1] += (
                            cups[a] * template_cups[j] * n ** (j - 1)
                        )
        for a in range(1, cutoff + 1):
            if not caps[a]:
                continue
            for b in range(1, cutoff + 1 - a):
                if not cups[b]:
                    continue
                max_j = min(cutoff - a - b + 3, len(template_convex))
                for j in range(2, max_j):
                    if template_convex[j]:
                        new_convex[a + b + j - 2] += (
                            caps[a]
                            * cups[b]
                            * template_convex[j]
                            * n ** (j - 2)
                        )
        n *= r
        caps, cups, convex = new_caps, new_cups, new_convex
    return n, caps, cups, convex


def weighted_sum(profile: Poly, base: int, shift: int) -> tuple[int, int]:
    """Return sum a_j base^(j-shift) and its exponent first moment."""
    value = 0
    exponent_moment = 0
    for j in range(shift, len(profile)):
        if profile[j]:
            term = profile[j] * base ** (j - shift)
            value += term
            exponent_moment += (j - shift) * term
    return value, exponent_moment


@dataclass(frozen=True)
class MomentState:
    n: int
    caps: int
    cups: int
    convex: int
    cap_moment: int
    cup_moment: int
    convex_moment: int

    @property
    def convex_mean(self) -> float:
        return self.convex_moment / self.convex


def vertical_moments(template: Cell, depth: int) -> MomentState:
    r, sc, su, sv = template
    state = MomentState(1, 1, 1, 1, 1, 1, 1)
    for _ in range(depth):
        ac, ac_moment = weighted_sum(sc, state.n, 1)
        au, au_moment = weighted_sum(su, state.n, 1)
        dv, dv_moment = weighted_sum(sv, state.n, 2)
        new_caps = state.caps * ac
        new_cups = state.cups * au
        cross = state.caps * state.cups * dv
        within = r * state.convex
        new_convex = within + cross
        new_cap_moment = state.cap_moment * ac + state.caps * ac_moment
        new_cup_moment = state.cup_moment * au + state.cups * au_moment
        new_convex_moment = (
            r * state.convex_moment
            + (state.cap_moment * state.cups + state.caps * state.cup_moment) * dv
            + state.caps * state.cups * dv_moment
        )
        state = MomentState(
            state.n * r,
            new_caps,
            new_cups,
            new_convex,
            new_cap_moment,
            new_cup_moment,
            new_convex_moment,
        )
    return state


def central_template(h: int, cutoff: int | None = None) -> Cell:
    """Return S_h=T_(2h-4,h-2), whose largest cap/cup has h-1 points."""
    if h < 3:
        raise ValueError("h must be at least 3")
    m = 2 * h - 4
    if cutoff is None:
        cutoff = 2 * h - 2
    return pascal_row(m, cutoff)[h - 2]


def diagonal_experiment(h: int, depth: int) -> dict[str, float | int]:
    # The exact diagonal size nearest (log_2 n)/2.
    r = math.comb(2 * h - 4, h - 2)
    target = round(depth * math.log2(r) / 2)
    template = central_template(h, target)
    n, _, _, convex = vertical_iterate(template, depth, target)
    value = convex[target]
    if not value:
        raise AssertionError("diagonal coefficient vanished")
    return {
        "h": h,
        "depth": depth,
        "r": r,
        "n_log2": math.log2(n),
        "target_k": target,
        "target_offset": target - math.log2(n) / 2,
        "v_k_log2": math.log2(value),
        "sigma": math.log2(value) / (target * target),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--h", type=int, nargs="+", default=[6, 8, 10, 12, 16, 20])
    parser.add_argument("--depth", type=int, nargs="+", default=[1, 2, 3, 4, 6, 8])
    parser.add_argument("--moments-only", action="store_true")
    args = parser.parse_args()
    for h in args.h:
        full_template = central_template(h)
        for depth in args.depth:
            moment = vertical_moments(full_template, depth)
            print(
                f"moment h={h:3d} d={depth:3d} log2n={math.log2(moment.n):10.4f} "
                f"mu={moment.convex_mean:10.5f} "
                f"mu-log2n={moment.convex_mean-math.log2(moment.n):+.6f}",
                flush=True,
            )
            if not args.moments_only:
                item = diagonal_experiment(h, depth)
                print(
                    f"  diagonal k={item['target_k']:4d} "
                    f"log2v={item['v_k_log2']:12.5f} sigma={item['sigma']:.9f}",
                    flush=True,
                )


if __name__ == "__main__":
    main()
