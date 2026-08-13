#!/usr/bin/env python3
"""Exact size-graded C/U/V recurrence for Pascal strong-glue cells."""

from __future__ import annotations

import argparse
import math


def add(a: list[int], b: list[int], k: int) -> list[int]:
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(k + 1)]


def mul(a: list[int], b: list[int], k: int) -> list[int]:
    out = [0] * (k + 1)
    for i, x in enumerate(a[: k + 1]):
        if not x:
            continue
        for j, y in enumerate(b[: k + 1 - i]):
            if y:
                out[i + j] += x * y
    return out


def scale_shift(a: list[int], scale: int, k: int) -> list[int]:
    out = a[:]
    out.extend([0] * (k + 1 - len(out)))
    for i in range(k, 0, -1):
        out[i] += scale * (a[i - 1] if i - 1 < len(a) else 0)
    return out[: k + 1]


def row(m: int, k: int):
    # tuple is size, cap polynomial, cup polynomial, convex polynomial.
    singleton = (1, [0, 1] + [0] * (k - 1), [0, 1] + [0] * (k - 1), [0, 1] + [0] * (k - 1))
    old = [singleton]
    for level in range(1, m + 1):
        new = [singleton]
        for i in range(1, level):
            na, ca, ua, wa = old[i - 1]
            nb, cb, ub, wb = old[i]
            c = add(scale_shift(ca, nb, k), cb, k)
            u = add(ua, scale_shift(ub, na, k), k)
            w = add(add(wa, wb, k), mul(ca, ub, k), k)
            new.append((na + nb, c, u, w))
        new.append(singleton)
        old = new
    return old


def vertical_iterate(template, depth: int, k: int):
    r, sc, su, sv = template
    n = 1
    c = [0, 1] + [0] * (k - 1)
    u = c[:]
    w = c[:]
    for _ in range(depth):
        nc = [0] * (k + 1)
        nu = [0] * (k + 1)
        nw = [r * x for x in w]
        for a in range(1, k + 1):
            if c[a]:
                for j in range(1, min(k - a + 2, len(sc))):
                    if sc[j]:
                        nc[a + j - 1] += c[a] * sc[j] * n ** (j - 1)
            if u[a]:
                for j in range(1, min(k - a + 2, len(su))):
                    if su[j]:
                        nu[a + j - 1] += u[a] * su[j] * n ** (j - 1)
        for a in range(1, k + 1):
            if not c[a]:
                continue
            for b in range(1, k + 1 - a):
                if not u[b]:
                    continue
                for j in range(2, min(k - a - b + 3, len(sv))):
                    if sv[j]:
                        nw[a + b + j - 2] += c[a] * u[b] * sv[j] * n ** (j - 2)
        n *= r
        c, u, w = nc, nu, nw
    return n, c, u, w


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, nargs="+", default=[10, 20, 30, 40, 50, 60])
    args = parser.parse_args()
    for k in args.k:
        m = 2 * k
        size, _, _, w = row(m, k)[k]
        value = w[k]
        print(
            f"k={k} m={m} n={size} log2n={math.log2(size):.8f} "
            f"log2vk={math.log2(value):.8f} coefficient={math.log2(value)/(k*k):.8f}"
        )
        if k <= 40:
            trials = []
            for depth in range(2, min(10, k) + 1):
                tm2 = max(2, round(2 * k / depth))
                template = row(tm2, k)[tm2 // 2]
                nn, _, _, ww = vertical_iterate(template, depth, k)
                if ww[k]:
                    trials.append((math.log2(ww[k]) / (k * k), depth, tm2, math.log2(nn)))
            print(f"  multidepth_best={min(trials)}")
        # A depth-two vertical composition of a central Pascal template just
        # below the k-gon threshold; this has about 2^(2k) points.
        tm = k - 1
        ti = tm // 2
        r, c, u, v = row(tm, k)[ti]
        composed = r * v[k]
        for j in range(2, k + 1):
            if not v[j]:
                continue
            endpoint = sum(c[a] * u[k - j + 2 - a] for a in range(1, k - j + 2))
            composed += v[j] * endpoint * r ** (j - 2)
        print(
            f"  vertical2 template_m={tm} r={r} N={r*r} "
            f"log2N={2*math.log2(r):.8f} log2vk={math.log2(composed):.8f} "
            f"coefficient={math.log2(composed)/(k*k):.8f}"
        )


if __name__ == "__main__":
    main()
