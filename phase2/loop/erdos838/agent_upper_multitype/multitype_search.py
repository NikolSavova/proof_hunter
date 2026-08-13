#!/usr/bin/env python3
"""Search finite-state vertical blow-ups for Erdős 838.

For a macro order type S on r x-ordered points, label macro-position i by a
child state ell[i].  All child states have the same size n.  The directional
vertical blow-up has the exact heterogeneous recurrences

 C' = sum_{B cap} C_{ell[min B]} n^(|B|-1),
 U' = sum_{B cup} U_{ell[max B]} n^(|B|-1),
 W' = sum_i W_{ell[i]}
      + sum_{B convex, |B|>=2}
          C_{ell[min B]} U_{ell[max B]} n^(|B|-2).

This script enumerates macro subsets exactly, then searches two-state label
rules using log-sum-exp arithmetic.  A candidate coefficient is estimated by
fitting log_2 W_d/(log_2 |Q_d|)^2 against 1/d and 1/d^2.
"""

from __future__ import annotations

import argparse
import itertools
import math
import random
from dataclasses import dataclass
from typing import Iterable, Sequence


Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    z = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (z > 0) - (z < 0)


def general_position(points: Sequence[Point]) -> bool:
    return all(
        orient(points[i], points[j], points[k]) != 0
        for i, j, k in itertools.combinations(range(len(points)), 3)
    )


def hull_size(points: Sequence[Point], indices: Sequence[int]) -> int:
    pts = sorted((points[i], i) for i in indices)
    if len(pts) <= 2:
        return len(pts)

    def half(seq: Iterable[tuple[Point, int]]) -> list[tuple[Point, int]]:
        out: list[tuple[Point, int]] = []
        for item in seq:
            while len(out) >= 2 and orient(out[-2][0], out[-1][0], item[0]) <= 0:
                out.pop()
            out.append(item)
        return out

    lower = half(pts)
    upper = half(reversed(pts))
    return len(lower[:-1] + upper[:-1])


@dataclass(frozen=True)
class Macro:
    points: tuple[Point, ...]
    caps: tuple[tuple[int, ...], ...]
    cups: tuple[tuple[int, ...], ...]
    convex: tuple[tuple[int, ...], ...]

    @property
    def r(self) -> int:
        return len(self.points)


def classify(points: Sequence[Point]) -> Macro:
    if not general_position(points):
        raise ValueError("points are not in general position")
    caps: list[tuple[int, ...]] = []
    cups: list[tuple[int, ...]] = []
    convex: list[tuple[int, ...]] = []
    r = len(points)
    for mask in range(1, 1 << r):
        ind = tuple(i for i in range(r) if mask >> i & 1)
        triples = list(itertools.combinations(ind, 3))
        if all(orient(points[i], points[j], points[k]) < 0 for i, j, k in triples):
            caps.append(ind)
        if all(orient(points[i], points[j], points[k]) > 0 for i, j, k in triples):
            cups.append(ind)
        if hull_size(points, ind) == len(ind):
            convex.append(ind)
    return Macro(tuple(points), tuple(caps), tuple(cups), tuple(convex))


def logadd(values: Iterable[float]) -> float:
    vals = list(values)
    m = max(vals)
    return m + math.log2(sum(2.0 ** (v - m) for v in vals))


def iterate(
    macros: Sequence[Macro], labels: Sequence[tuple[int, ...]], depth: int
) -> tuple[list[float], list[float], list[float], list[float]]:
    """Return histories of state-0 log C,U,W and normalized W coefficient."""
    states = len(macros)
    r = macros[0].r
    assert all(m.r == r for m in macros)
    assert all(len(x) == r for x in labels)
    c = [0.0] * states
    u = [0.0] * states
    w = [0.0] * states
    hc: list[float] = []
    hu: list[float] = []
    hw: list[float] = []
    ratios: list[float] = []
    lr = math.log2(r)
    for d in range(1, depth + 1):
        ln = (d - 1) * lr
        nc: list[float] = []
        nu: list[float] = []
        nw: list[float] = []
        for p, macro in enumerate(macros):
            ell = labels[p]
            nc.append(
                logadd(c[ell[b[0]]] + (len(b) - 1) * ln for b in macro.caps)
            )
            nu.append(
                logadd(u[ell[b[-1]]] + (len(b) - 1) * ln for b in macro.cups)
            )
            terms = [w[ell[i]] for i in range(r)]
            terms.extend(
                c[ell[b[0]]]
                + u[ell[b[-1]]]
                + (len(b) - 2) * ln
                for b in macro.convex
                if len(b) >= 2
            )
            nw.append(logadd(terms))
        c, u, w = nc, nu, nw
        hc.append(c[0])
        hu.append(u[0])
        hw.append(w[0])
        ratios.append(w[0] / ((d * lr) ** 2))
    return hc, hu, hw, ratios


def extrapolate(ratios: Sequence[float]) -> float:
    """Least-squares intercept in ratio_d = a + b/d + c/d^2."""
    # Tiny dependency-free normal-equation solve for the last half of data.
    start = len(ratios) // 2
    rows = [(1.0, 1.0 / d, 1.0 / (d * d)) for d in range(start + 1, len(ratios) + 1)]
    ys = ratios[start:]
    a = [[sum(x[i] * x[j] for x in rows) for j in range(3)] for i in range(3)]
    b = [sum(x[i] * y for x, y in zip(rows, ys)) for i in range(3)]
    for i in range(3):
        pivot = max(range(i, 3), key=lambda k: abs(a[k][i]))
        a[i], a[pivot] = a[pivot], a[i]
        b[i], b[pivot] = b[pivot], b[i]
        q = a[i][i]
        for j in range(i, 3):
            a[i][j] /= q
        b[i] /= q
        for k in range(3):
            if k == i:
                continue
            q = a[k][i]
            for j in range(i, 3):
                a[k][j] -= q * a[i][j]
            b[k] -= q * b[i]
    return b[0]


def endpoint_rewards(macro: Macro) -> tuple[list[int], list[int]]:
    """Largest cap-minus-one by first point and cup-minus-one by last."""
    cap = [0] * macro.r
    cup = [0] * macro.r
    for b in macro.caps:
        cap[b[0]] = max(cap[b[0]], len(b) - 1)
    for b in macro.cups:
        cup[b[-1]] = max(cup[b[-1]], len(b) - 1)
    return cap, cup


def reachable(adj: Sequence[Sequence[bool]], start: int) -> set[int]:
    seen = {start}
    todo = [start]
    while todo:
        p = todo.pop()
        for q, yes in enumerate(adj[p]):
            if yes and q not in seen:
                seen.add(q)
                todo.append(q)
    return seen


def two_state_cycle_means(weights: Sequence[Sequence[float]], adj: Sequence[Sequence[bool]]) -> list[float]:
    """Maximum reachable cycle mean from each vertex of a two-state graph."""
    assert len(weights) == 2
    cycles: list[tuple[set[int], float]] = []
    for p in range(2):
        if adj[p][p]:
            cycles.append(({p}, weights[p][p]))
    if adj[0][1] and adj[1][0]:
        cycles.append(({0, 1}, (weights[0][1] + weights[1][0]) / 2.0))
    out = []
    for start in range(2):
        reach = reachable(adj, start)
        out.append(max(mean for vertices, mean in cycles if vertices & reach))
    return out


def tropical_coefficient(macros: Sequence[Macro], labels: Sequence[tuple[int, ...]], initial: int = 0) -> float:
    """Exact quadratic coefficient of a two-state equal-branching system."""
    assert len(macros) == len(labels) == 2
    r = macros[0].r
    neg = -10**9
    wc = [[neg] * 2 for _ in range(2)]
    wu = [[neg] * 2 for _ in range(2)]
    adj = [[False] * 2 for _ in range(2)]
    for p in range(2):
        cr, ur = endpoint_rewards(macros[p])
        for i, q in enumerate(labels[p]):
            adj[p][q] = True
            wc[p][q] = max(wc[p][q], cr[i])
            wu[p][q] = max(wu[p][q], ur[i])
    muc = two_state_cycle_means(wc, adj)
    muu = two_state_cycle_means(wu, adj)
    parents = reachable(adj, initial)
    coupling = max(
        muc[labels[p][i]] + muu[labels[p][j]]
        for p in parents
        for i in range(r)
        for j in range(i + 1, r)
    )
    return coupling / (2.0 * math.log2(r))


def point_sets(r: int, samples: int, seed: int) -> Iterable[tuple[Point, ...]]:
    """Yield diverse exact x-ordered point sets, deduplicated by chirotope."""
    rng = random.Random(seed)
    seen: set[tuple[int, ...]] = set()
    attempts = 0
    while len(seen) < samples and attempts < 100 * samples:
        attempts += 1
        ys = rng.sample(range(-20 * r, 20 * r + 1), r)
        pts = tuple((i, ys[i]) for i in range(r))
        if not general_position(pts):
            continue
        chi = tuple(orient(pts[i], pts[j], pts[k]) for i, j, k in itertools.combinations(range(r), 3))
        if chi in seen:
            continue
        seen.add(chi)
        yield pts


def bits(mask: int, r: int) -> tuple[int, ...]:
    return tuple((mask >> i) & 1 for i in range(r))


def search(r: int, samples: int, depth: int, seed: int, top: int, mirror: bool) -> None:
    winners: list[tuple[float, tuple[Point, ...], int, int, float]] = []
    for si, pts in enumerate(point_sets(r, samples, seed)):
        macro = classify(pts)
        macro_b = classify(tuple((x, -y) for x, y in pts)) if mirror else macro
        # Allow completely independent child-state labelings.  The useful
        # two-state experiment takes the second macro to be the vertical
        # reflection of the first, thereby exchanging cap and cup profiles.
        for ma in range(1 << r):
            la = bits(ma, r)
            for mb in range(1 << r):
                lb = bits(mb, r)
                _, _, _, ratios = iterate((macro, macro_b), (la, lb), depth)
                est = extrapolate(ratios)
                item = (est, pts, ma, mb, ratios[-1])
                if len(winners) < top:
                    winners.append(item)
                    winners.sort(key=lambda z: z[0])
                elif est < winners[-1][0]:
                    winners[-1] = item
                    winners.sort(key=lambda z: z[0])
        print(f"sample={si + 1} best={winners[0]}")
    print("\nFINAL")
    for row in winners:
        print(row)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=6)
    parser.add_argument("--samples", type=int, default=20)
    parser.add_argument("--depth", type=int, default=50)
    parser.add_argument("--seed", type=int, default=838)
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--mirror", action="store_true")
    args = parser.parse_args()
    search(args.r, args.samples, args.depth, args.seed, args.top, args.mirror)


if __name__ == "__main__":
    main()
