#!/usr/bin/env python3
"""Exact checks for ENDPOINT_BASELINE_SCARCITY.md."""

from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "endpoint_baseline_scarcity_certificate.json"


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    return half(points)[:-1] + half(reversed(points))[:-1]


def convex(points, labels):
    labels = tuple(labels)
    return len(labels) <= 2 or len(hull([points[x] for x in labels])) == len(labels)


def powerset(items):
    items = tuple(items)
    for r in range(len(items) + 1):
        yield from itertools.combinations(items, r)


def construction():
    # Every high point lies on one strict concave parabola.  The four outer
    # blocks have three points each and are separated in x-order.
    t_x = (-2, -1, 0, 1, 2)
    cluster_x = {
        "L0": (Q(-41, 10), Q(-4), Q(-39, 10)),
        "L1": (Q(-31, 10), Q(-3), Q(-29, 10)),
        "R0": (Q(29, 10), Q(3), Q(31, 10)),
        "R1": (Q(39, 10), Q(4), Q(41, 10)),
    }
    points = {}
    T = []
    for x in t_x:
        label = f"t{x:+d}"
        points[label] = (Q(x), Q(-(x * x)))
        T.append(label)
    clusters = {}
    for name, xs in cluster_x.items():
        clusters[name] = []
        for a, x in enumerate(xs):
            label = f"{name}_{a}"
            points[label] = (x, -(x * x))
            clusters[name].append(label)
    Z = []
    for i, x in enumerate((Q(-3, 5), Q(-3, 10), Q(0), Q(3, 10), Q(3, 5))):
        label = f"z{i}"
        points[label] = (x, Q(-100) - x * x)
        Z.append(label)
    return points, tuple(T), {k: tuple(v) for k, v in clusters.items()}, tuple(Z)


def planar_regression_check():
    points, T, clusters, Z = construction()
    labels = tuple(points)
    for tri in itertools.combinations(labels, 3):
        assert orient(*(points[x] for x in tri)) != 0
    assert convex(points, T)
    assert convex(points, Z)

    cluster_order = ("L0", "L1", "R0", "R1")
    sources = []
    parents = defaultdict(list)
    for choice in itertools.product(*(clusters[c] for c in cluster_order)):
        U = tuple(sorted(T + choice, key=lambda x: points[x][0]))
        assert convex(points, U)
        assert len(U) == 9
        peeled = U[2:-2]
        assert set(peeled) == set(T)
        sources.append(U)
        parents[tuple(peeled)].append(U)
    assert len(sources) == 3**4 == 81
    assert len(parents) == 1

    e = (T[0], T[-1])
    interior = T[1:-1] + Z
    baseline_by_rank = defaultdict(list)
    for a in range(len(interior) + 1):
        for trace in itertools.combinations(interior, a):
            face = e + trace
            if convex(points, face):
                baseline_by_rank[len(face)].append(tuple(face))
    C = len(baseline_by_rank[5])
    upper = 1 + len(Z) * 3 + math.comb(len(Z), 2) * math.comb(3, 2)
    assert 1 <= C <= upper

    # Exact fixed-parent Boolean bank and its endpoint-retaining subbank.
    bank = set()
    guarded = set()
    Tset = set(T)
    for U in sources:
        petal = tuple(x for x in U if x not in Tset)
        for S in powerset(T):
            out = frozenset(petal + S)
            assert convex(points, out)
            bank.add(out)
            if set(e).issubset(S):
                guarded.add(out)
                ordered = sorted(out, key=lambda x: points[x][0])
                peeled = ordered[2:-2]
                assert (peeled[0], peeled[-1]) == e
    assert len(bank) == len(sources) * 2 ** len(T)
    assert len(guarded) == len(sources) * 2 ** (len(T) - 2)

    # Fixed common interval face, bad union, and fixed tangent mark.
    W = (Z[0], Z[2], Z[4])
    assert convex(points, W)
    assert not convex(points, e + W)
    p = T[2]
    tangent = tuple(T)
    for U in sources:
        Qcarrier = tuple(x for x in U if x != p)
        assert convex(points, Qcarrier)
        assert convex(points, U)
        ordered = sorted(U, key=lambda x: points[x][0])
        pos = ordered.index(p)
        assert tuple(ordered[pos - 2 : pos + 3]) == tangent

    # Same-rank likelihood identity at j=2, r=5.
    G = sum(Q(len(faces), 2**rank) for rank, faces in baseline_by_rank.items())
    j, r, N = 2, 5, len(sources)
    h = Q(N, 2 ** (r + 2 * j)) / G
    lhs = 4**j * h
    p_rank = Q(C, 2**r) / G
    rhs = p_rank * Q(N, C)
    assert lhs == rhs
    local_V = len(bank)
    expectation = sum(
        (Q(len(faces), 2**rank) / G) * Q(1, 2**rank)
        for rank, faces in baseline_by_rank.items()
    )
    assert lhs <= local_V * expectation
    assert local_V >= 2 ** (r + 2 * j) * h

    return {
        "points": len(points),
        "parent_rank": r,
        "depth": j,
        "source_rank": r + 2 * j,
        "outer_clusters": {k: len(v) for k, v in clusters.items()},
        "canonical_sources": len(sources),
        "distinct_parents": len(parents),
        "rank_five_endpoint_faces": C,
        "rank_five_endpoint_upper_bound": upper,
        "full_parent_boolean_bank": len(bank),
        "endpoint_retaining_bank": len(guarded),
        "common_W": list(W),
        "W_union_endpoint_convex": False,
        "fixed_mark": p,
        "fixed_tangent_five_tuple": list(tangent),
        "endpoint_half_weight_G": str(G),
        "likelihood_h": str(h),
        "same_rank_identity_value": str(lhs),
        "baseline_harmonic_rank_factor": str(expectation),
    }


def global_incidence_check():
    # A pure exact finite model of Theorem 2's decoder.  Every record is
    # (j,e,r,T,Q), with Q having j ordered symbols on each side.  We choose
    # the endpoint-retaining bank and audit its representation load.
    records = []
    ranks = (3, 4, 5)
    depths = (1, 2)
    endpoints = ("e0", "e1")
    for j in depths:
        for e in endpoints:
            for r in ranks:
                T = tuple([f"{e}_L"] + [f"{e}_t{r}_{a}" for a in range(r - 2)] + [f"{e}_R"])
                degree = 1 + j + r
                for qid in range(degree):
                    left = tuple(f"{e}_j{j}_r{r}_q{qid}_l{a}" for a in range(j))
                    right = tuple(f"{e}_j{j}_r{r}_q{qid}_u{a}" for a in range(j))
                    records.append((j, e, r, T, left + right))
    outputs = defaultdict(int)
    incidence = Q(0)
    for j, e, r, T, petal in records:
        internal = T[1:-1]
        for chosen in powerset(internal):
            out = (j, e, frozenset(petal + (T[0], T[-1]) + chosen))
            outputs[out] += 1
            incidence += 1
    # The state key explicitly records decoded (j,e); only r can collide.
    max_load = max(outputs.values())
    J, R = len(depths), len(ranks)
    assert max_load <= R
    assert incidence <= R * len(outputs)
    assert incidence <= J * R * len(outputs)
    return {
        "depths_J": J,
        "ranks_R": R,
        "records": len(records),
        "bank_incidences": int(incidence),
        "distinct_decoded_outputs": len(outputs),
        "maximum_output_load": max_load,
        "theorem_global_load_bound": J * R,
    }


def coefficient_check():
    # Balanced full-product gate: a=kappa=1/4, c0=1/8.
    a = Q(1, 4)
    kappa = Q(1, 4)
    c0 = Q(1, 8)
    conclusion = a + c0 * (a / kappa) ** 2
    assert conclusion == Q(3, 8)
    rows = []
    for d in (16, 32, 64):
        q = d // 4
        log_M = q * d
        conservative_gain = Q(1, 8) * d * d - 3 * d
        rows.append({
            "log_cluster_size": d,
            "clusters": q,
            "log_M": log_M,
            "asymptotic_one_gap_gain_before_lower_order_cleanup": str(conservative_gain),
        })
    return {
        "history_coefficient_a": str(a),
        "cluster_count_coefficient_kappa": str(kappa),
        "local_reservoir_coefficient_c0": str(c0),
        "conditional_face_coefficient": str(conclusion),
        "finite_scale_rows": rows,
    }


def main():
    cert = {
        "planar_scarcity_regression": planar_regression_check(),
        "global_decoder_model": global_incidence_check(),
        "coefficient_gate": coefficient_check(),
    }
    CERT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print("PASS verify_endpoint_baseline_scarcity")
    print(json.dumps(cert, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
