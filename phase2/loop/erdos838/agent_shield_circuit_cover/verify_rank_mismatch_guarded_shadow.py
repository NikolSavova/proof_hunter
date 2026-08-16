#!/usr/bin/env python3
"""Exact checks for RANK_MISMATCH_GUARDED_SHADOW.md."""

from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict, deque
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "rank_mismatch_guarded_shadow_certificate.json"


def subsets(items, rank=None):
    items = tuple(items)
    ranks = range(len(items) + 1) if rank is None else (rank,)
    for r in ranks:
        yield from itertools.combinations(items, r)


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def point_in_triangle_strict(p, a, b, c):
    vals = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return (all(v > 0 for v in vals) or all(v < 0 for v in vals))


def is_convex_subset(points, labels):
    labels = tuple(labels)
    if len(labels) <= 3:
        return True
    for hidden in labels:
        others = [x for x in labels if x != hidden]
        for tri in itertools.combinations(others, 3):
            if point_in_triangle_strict(points[hidden], *(points[t] for t in tri)):
                return False
    return True


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def flow(self, s, t):
        ans = 0
        while True:
            level = [-1] * len(self.g)
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, cap, _ in self.g[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                return ans
            it = [0] * len(self.g)

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while it[u] < len(self.g[u]):
                    edge = self.g[u][it[u]]
                    v, cap, rev = edge
                    if cap and level[v] == level[u] + 1:
                        got = dfs(v, min(pushed, cap))
                        if got:
                            edge[1] -= got
                            self.g[v][rev][1] += got
                            return got
                    it[u] += 1
                return 0

            while True:
                got = dfs(s, 10**18)
                if not got:
                    break
                ans += got


def max_clone_flow(carriers, shadows, beta, capacity):
    left = list(carriers)
    right = sorted(set().union(*(shadows[u] for u in left)))
    ri = {v: i for i, v in enumerate(right)}
    source = 0
    loff = 1
    roff = loff + len(left)
    sink = roff + len(right)
    dinic = Dinic(sink + 1)
    for i, u in enumerate(left):
        dinic.add(source, loff + i, beta)
        for v in shadows[u]:
            dinic.add(loff + i, roff + ri[v], beta)
    for i in range(len(right)):
        dinic.add(roff + i, sink, capacity)
    return dinic.flow(source, sink), beta * len(left), len(right)


def endpoint_partition_check():
    m = 7
    labels = tuple(range(m))
    points = {i: (i, i * i) for i in labels}
    assert all(is_convex_subset(points, s) for s in subsets(labels))
    bins = defaultdict(set)
    nontrivial = []
    for r in range(2, m + 1):
        for face in subsets(labels, r):
            bins[(min(face), max(face))].add(face)
            nontrivial.append(face)
    flat = [face for bank in bins.values() for face in bank]
    assert len(flat) == len(set(flat)) == len(nontrivial) == 2**m - m - 1
    for (i, j), bank in bins.items():
        assert len(bank) == 2 ** (j - i - 1)

    rho = Fraction(3, 2)
    J = 3
    low = high = 0
    high_bank = set()
    for e, bank in bins.items():
        c = len(bank)
        counts = (c, 2 * c, c // 2)
        for n in counts:
            if n <= rho * c:
                low += n
            else:
                high += n
                high_bank.update(bank)
    total_bank = sum(map(len, bins.values()))
    assert low <= rho * J * total_bank
    assert high > rho * len(high_bank)
    return {
        "m": m,
        "nontrivial_faces": len(nontrivial),
        "endpoint_bins": len(bins),
        "rho": str(rho),
        "J": J,
        "low_histories": low,
        "low_bound": str(rho * J * total_bank),
        "high_histories": high,
        "high_bank_union": len(high_bank),
    }


def guarded_shadow_check():
    m, s, k, g = 10, 6, 4, 2
    e = (0, m - 1)
    middle = tuple(range(1, m - 1))
    carriers = [tuple(sorted(e + q)) for q in subsets(middle, s - g)]
    shadows = {}
    degrees = defaultdict(int)
    for u in carriers:
        free = tuple(x for x in u if x not in e)
        out = {tuple(sorted(e + q)) for q in subsets(free, k - g)}
        shadows[u] = out
        for t in out:
            degrees[t] += 1
    R = math.comb(s - g, k - g)
    beta = 2 ** (s - k)
    delta = max(degrees.values())
    expected_delta = math.comb(m - k, s - k)
    assert all(len(v) == R for v in shadows.values())
    assert delta == expected_delta
    assert len(degrees) == math.comb(m - g, k - g)
    assert len(carriers) * R == len(degrees) * delta
    K = math.ceil(beta * delta / R)
    flow, demand, outputs = max_clone_flow(carriers, shadows, beta, K)
    assert flow == demand
    flow_bad, _, _ = max_clone_flow(carriers, shadows, beta, K - 1)
    assert flow_bad < demand

    # Fix one heavy prefix and enumerate its endpoint-retaining Boolean bank.
    T = (0, 1, 2, 9)
    remaining = tuple(x for x in range(m) if x not in T)
    petals = list(subsets(remaining, s - k))
    bank = set()
    for d in petals:
        for a in subsets((1, 2)):
            face = tuple(sorted(e + a + d))
            bank.add(face)
    assert len(bank) == len(petals) * 2 ** (k - g)

    # Complete convex family: all pairs are compatible.  Check the exact
    # outside-union representation multiplicity and Theorem 4's bank bound.
    rep = defaultdict(int)
    for d1, d2 in itertools.combinations(petals, 2):
        rep[frozenset(d1) | frozenset(d2)] += 1
    max_rep = max(rep.values())
    assert max_rep <= 3 ** (2 * (s - k))
    mixed = {
        tuple(sorted(e + a + tuple(outside)))
        for outside in rep
        for a in subsets((1, 2))
    }
    eplus = math.comb(len(petals), 2)
    assert len(mixed) * 3 ** (2 * (s - k)) >= 2 ** (k - g) * eplus
    return {
        "m": m,
        "s": s,
        "k": k,
        "guard_rank": g,
        "carriers": len(carriers),
        "shadow_outputs": outputs,
        "left_degree_R": R,
        "beta": beta,
        "max_shadow_degree": delta,
        "sharp_clone_congestion": K,
        "flow_at_K": flow,
        "flow_at_K_minus_1": flow_bad,
        "fixed_prefix_petals": len(petals),
        "fixed_prefix_boolean_bank": len(bank),
        "compatible_pairs": eplus,
        "mixed_bank": len(mixed),
        "max_pair_union_multiplicity": max_rep,
    }


def bad_circuit_check():
    points = {
        "l": (Fraction(-20), Fraction(0)),
        "r": (Fraction(20), Fraction(0)),
        "d": (Fraction(0), Fraction(-20)),
        "x": (Fraction(1), Fraction(10)),
        "y": (Fraction(-1), Fraction(30)),
    }
    T = ("l", "r", "d")
    U = T + ("x",)
    V = T + ("y",)
    union = T + ("x", "y")
    assert is_convex_subset(points, U)
    assert is_convex_subset(points, V)
    assert not is_convex_subset(points, union)
    circuit = ("l", "r", "x", "y")
    assert point_in_triangle_strict(
        points["x"], points["l"], points["r"], points["y"]
    )
    assert "x" in set(U) - set(V)
    assert "y" in set(V) - set(U)
    # Exact general position audit.
    for triple in itertools.combinations(points, 3):
        assert orient(*(points[z] for z in triple)) != 0
    return {
        "points": {k: [str(x), str(y)] for k, (x, y) in points.items()},
        "carrier_U_convex": True,
        "carrier_V_convex": True,
        "union_convex": False,
        "hidden_point": "x",
        "circuit": list(circuit),
        "cross_petals": ["x", "y"],
    }


def mismatch_poor_table():
    rows = []
    k, g = 4, 2
    for b in range(1, 9):
        s = k + b
        R = math.comb(s - g, k - g)
        beta = 2**b
        rows.append({
            "b": b,
            "s": s,
            "R": R,
            "beta": beta,
            "beta_over_R": str(Fraction(beta, R)),
            "guarded_boolean_multiplier": 2 ** (k - g),
        })
    assert rows[-1]["beta"] > rows[-1]["R"]
    return rows


def main():
    cert = {
        "endpoint_partition": endpoint_partition_check(),
        "guarded_shadow": guarded_shadow_check(),
        "cross_petal_bad_circuit": bad_circuit_check(),
        "mismatch_poor_table": mismatch_poor_table(),
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print("PASS verify_rank_mismatch_guarded_shadow")
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
