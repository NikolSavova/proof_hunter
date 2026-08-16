#!/usr/bin/env python3
"""Exact checks for HULL_ROOT_ENVELOPE_AND_CHART_RESET_GATE.md.

The verifier is deliberately independent of the minimizer search code.  It
enumerates ordinary faces, radial-root cap/cup families, extreme shellings,
and hinged endpoint ranks directly from exact integer determinants.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import cmp_to_key, lru_cache
from itertools import combinations, product
from math import comb
from pathlib import Path
import json


HERE = Path(__file__).resolve().parent


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_ids(points, mask=None):
    if mask is None:
        ids = list(range(len(points)))
    else:
        ids = [i for i in range(len(points)) if mask >> i & 1]
    ids.sort(key=lambda i: points[i])
    if len(ids) <= 2:
        return ids
    lower = []
    for i in ids:
        while (len(lower) >= 2
               and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0):
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(ids):
        while (len(upper) >= 2
               and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0):
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def face_profile(points):
    profile = [0] * (len(points) + 1)
    for rank in range(1, len(points) + 1):
        for subset in combinations(range(len(points)), rank):
            if rank <= 2:
                profile[rank] += 1
                continue
            selected = [points[i] for i in subset]
            if len(hull_ids(selected)) == rank:
                profile[rank] += 1
    return profile


def all_mask_face_totals(points):
    """Return V(P|mask) for every mask by a Boolean zeta transform."""
    size = len(points)
    is_face = [0] * (1 << size)
    for mask in range(1, 1 << size):
        ids = [i for i in range(size) if mask >> i & 1]
        if len(ids) <= 2:
            is_face[mask] = 1
        else:
            selected = [points[i] for i in ids]
            is_face[mask] = int(len(hull_ids(selected)) == len(ids))
    totals = is_face[:]
    for bit in range(size):
        for mask in range(1 << size):
            if mask >> bit & 1:
                totals[mask] += totals[mask ^ (1 << bit)]
    return totals


def radial_order(points, mask, root):
    """Clockwise order about an extreme root, normalized to root sign -1."""
    ids = [i for i in range(len(points))
           if mask >> i & 1 and i != root]

    def compare(i, j):
        value = orient(points[root], points[i], points[j])
        assert value
        return -1 if value > 0 else 1

    order = tuple(reversed(sorted(ids, key=cmp_to_key(compare))))
    assert all(
        orient(points[order[i]], points[order[j]], points[root]) < 0
        for i in range(len(order)) for j in range(i + 1, len(order))
    )
    return order


def chart_profile(points, order):
    """Direct cap/cup totals and hinged ranks in one ordered chart."""
    position = {label: i for i, label in enumerate(order)}
    cap_total = cup_total = 0
    alpha = {label: 0 for label in order}
    beta = {label: 0 for label in order}
    for submask in range(1, 1 << len(order)):
        labels = [order[i] for i in range(len(order)) if submask >> i & 1]
        signs = [
            orient(points[i], points[j], points[k])
            for i, j, k in combinations(labels, 3)
        ]
        is_cap = all(value < 0 for value in signs)
        is_cup = all(value > 0 for value in signs)
        if is_cap:
            cap_total += 1
            first = min(labels, key=position.get)
            alpha[first] = max(alpha[first], len(labels) - 1)
        if is_cup:
            cup_total += 1
            last = max(labels, key=position.get)
            beta[last] = max(beta[last], len(labels) - 1)
    lengths = {i: alpha[i] + beta[i] for i in order}
    kraft = sum(Fraction(1, 2 ** lengths[i]) for i in order)
    cap_paths = sum(2 ** alpha[i] for i in order)
    cup_paths = sum(2 ** beta[i] for i in order)
    return {
        "C": cap_total,
        "U": cup_total,
        "alpha": alpha,
        "beta": beta,
        "lengths": lengths,
        "kraft": kraft,
        "cap_paths": cap_paths,
        "cup_paths": cup_paths,
    }


def audit_n9(points, expected):
    size = len(points)
    full = (1 << size) - 1
    totals = all_mask_face_totals(points)
    assert totals[full] == expected["V"]
    reachable = set()
    transitions = []
    chart_cache = {}

    def visit(mask):
        if mask in reachable:
            return
        reachable.add(mask)
        if mask & (mask - 1) == 0:
            return
        for root in hull_ids(points, mask):
            child = mask ^ (1 << root)
            order = radial_order(points, mask, root)
            profile = chart_profile(points, order)
            chart_cache[mask, root] = (order, profile)
            cost = totals[mask] - totals[child] - 1
            assert profile["C"] == cost
            assert profile["C"] >= profile["cap_paths"]
            assert profile["U"] >= profile["cup_paths"]
            assert profile["kraft"] <= 1
            child_size = child.bit_count()
            assert (profile["cap_paths"] * profile["cup_paths"]
                    * profile["kraft"] >= child_size ** 3)
            assert (profile["C"] * profile["U"] * profile["kraft"]
                    >= child_size ** 3)
            transitions.append((mask, root, child, cost))
            visit(child)

    visit(full)

    @lru_cache(None)
    def shelling_count(mask):
        if mask & (mask - 1) == 0:
            return 1
        return sum(shelling_count(mask ^ (1 << root))
                   for root in hull_ids(points, mask))

    @lru_cache(None)
    def cost_sequences(mask):
        if mask & (mask - 1) == 0:
            return {()}
        rows = set()
        for root in hull_ids(points, mask):
            child = mask ^ (1 << root)
            cost = totals[mask] - totals[child] - 1
            rows.update((cost,) + tail for tail in cost_sequences(child))
        return rows

    sequences = cost_sequences(full)
    assert len(reachable) == expected["reachable_masks"]
    assert len(transitions) == expected["root_transitions"]
    assert shelling_count(full) == expected["shellings"]
    assert len(sequences) == expected["distinct_cost_sequences"]
    assert {sum(row) for row in sequences} == {expected["cost_sum"]}

    costs_by_size = defaultdict(set)
    for _, _, child, cost in transitions:
        costs_by_size[child.bit_count()].add(cost)
    normalized_costs = {
        str(k): sorted(values) for k, values in sorted(costs_by_size.items())
    }
    assert normalized_costs == expected["costs_by_child_size"]

    top_rows = {}
    for root in hull_ids(points, full):
        child = full ^ (1 << root)
        order, profile = chart_cache[full, root]
        top_rows[str(root)] = {
            "order": list(order),
            "child_V": totals[child],
            "C": profile["C"],
            "U": profile["U"],
            "lengths": sorted(profile["lengths"].values()),
            "kraft": [profile["kraft"].numerator,
                      profile["kraft"].denominator],
        }
    assert top_rows == expected["top_root_rows"]

    # A physical point swaps its hinged responsibility between two equally
    # cheap top root charts.  This is the finite chart-reset certificate.
    profile_left = chart_cache[full, 1][1]
    profile_right = chart_cache[full, 8][1]
    assert (profile_left["alpha"][2], profile_left["beta"][2]) == (3, 1)
    assert (profile_right["alpha"][2], profile_right["beta"][2]) == (1, 3)

    return {
        "reachable": len(reachable),
        "transitions": len(transitions),
        "shellings": shelling_count(full),
        "sequences": len(sequences),
        "top_rows": top_rows,
    }


def audit_sharp_hinged_n8(points, expected):
    profile = chart_profile(points, tuple(range(8)))
    faces = face_profile(points)
    assert faces == expected["face_profile"]
    assert profile["C"] == profile["U"] == expected["C"]
    assert tuple(profile["alpha"][i] for i in range(8)) == tuple(expected["alpha"])
    assert tuple(profile["beta"][i] for i in range(8)) == tuple(expected["beta"])
    assert set(profile["lengths"].values()) == {3}
    assert profile["kraft"] == 1
    assert profile["C"] * profile["U"] * profile["kraft"] >= 8 ** 3

    # Independently reconstruct the actual mixed threshold words by sweeping
    # the 28 distinct slopes.  Equality in Kraft then forces all eight words.
    slope_classes = defaultdict(list)
    for i, j in combinations(range(8), 2):
        slope_classes[Fraction(
            points[j][1] - points[i][1], points[j][0] - points[i][0]
        )].append((i, j))
    # Every tie is between disjoint edges, so any tie order is the limit of a
    # chirotope-preserving generic perturbation and the DP updates commute.
    assert all(
        len(set(edge for pair in roots for edge in pair)) == 2 * len(roots)
        for roots in slope_classes.values()
    )
    roots = [edge for slope in sorted(slope_classes)
             for edge in sorted(slope_classes[slope])]
    alpha = [0] * 8
    beta = [0] * 8
    cup_last = [[] for _ in range(8)]
    cap_first = [[] for _ in range(8)]
    for time, (i, j) in enumerate(roots):
        old_ai, old_aj = alpha[i], alpha[j]
        old_bi, old_bj = beta[i], beta[j]
        while len(cup_last[j]) < old_bi + 1:
            cup_last[j].append(time)
        while len(cap_first[i]) < old_aj + 1:
            cap_first[i].append(time)
        alpha[i] = max(old_ai, old_aj + 1)
        beta[j] = max(old_bj, old_bi + 1)
    words = []
    for i in range(8):
        tagged = [(time, 0) for time in cup_last[i]]
        tagged += [(time, 1) for time in cap_first[i]]
        words.append(tuple(bit for _, bit in sorted(tagged)))
    assert tuple(alpha) == tuple(expected["alpha"])
    assert tuple(beta) == tuple(expected["beta"])
    assert set(words) == set(product((0, 1), repeat=3))
    return sum(faces), profile["C"], profile["U"]


def binary_scalar_profile(n):
    """First n fixed-length binary words and their exact moment banks."""
    rank = (n - 1).bit_length()
    alpha = [i.bit_count() for i in range(n)]
    beta = [rank - value for value in alpha]
    kraft = sum(Fraction(1, 2 ** (a + b)) for a, b in zip(alpha, beta))
    return sum(2 ** a for a in alpha), sum(2 ** b for b in beta), kraft


def audit_scalar_barrier(limit):
    """An all-n polynomial scalar model of recurrence plus hinged Kraft."""
    last_bad = None
    for n in range(1, limit + 1):
        cap_paths, cup_paths, kraft = binary_scalar_profile(n)
        ell = n * (n + 1) // 2
        if cap_paths > ell or cup_paths > ell:
            last_bad = n
        if n >= 20:
            assert cap_paths <= ell and cup_paths <= ell
            assert kraft <= 1
            assert cap_paths * cup_paths * kraft >= n ** 3
            assert ell * ell * kraft >= n ** 3
            value = n + comb(n + 1, 3)
            next_value = n + 1 + comb(n + 2, 3)
            assert next_value == value + 1 + ell
            assert ell <= value
    assert last_bad == 19

    # Proof-oriented boundary checks.  Within a fixed bit length, each new
    # contribution is at most n, while ell(n+1)-ell(n)=n+1.  At a power-of-two
    # reset the only nontrivial bank is 2*3^(r-1)+2^(r-1), checked at r=6;
    # thereafter the RHS grows by a factor exceeding the LHS factor.
    for rank in range(6, 32):
        n = 2 ** (rank - 1) + 1
        boundary_cup = 2 * 3 ** (rank - 1) + 2 ** (rank - 1)
        boundary_floor = n * (n + 1) // 2
        assert boundary_cup <= boundary_floor
        if rank > 6:
            previous = 2 * 3 ** (rank - 2) + 2 ** (rank - 2)
            previous_n = 2 ** (rank - 2) + 1
            previous_floor = previous_n * (previous_n + 1) // 2
            assert boundary_cup <= 3 * previous
            assert boundary_floor >= 3 * previous_floor
    return last_bad, limit


def cap_cup_in_x_order(points):
    order = tuple(sorted(range(len(points)), key=lambda i: points[i][0]))
    assert len({points[i][0] for i in order}) == len(points)
    return chart_profile(points, order)


def audit_affine_reset_chain(expected_rows):
    """Build a stretchable chain with a freshly chosen chart at each step."""
    points = [(0, 0)]
    value = 1
    rows = []
    for new_size in range(2, len(expected_rows) + 2):
        slope = (-1 if new_size % 2 == 0 else 1) * (new_size - 1)
        # det [[1,t],[-t,1]]=1+t^2>0, so this preserves the order type.
        transformed = [(x + slope * y, -slope * x + y) for x, y in points]
        assert len({x for x, _ in transformed}) == len(transformed)
        transformed.sort()
        profile = cap_cup_in_x_order(transformed)
        root_x = max(x for x, _ in transformed) + 1
        wall = 1
        while any(
            orient(a, b, (root_x, -wall)) >= 0
            for a, b in combinations(transformed, 2)
        ):
            wall *= 2
        root = (root_x, -wall)
        assert all(orient(a, b, root) < 0
                   for a, b in combinations(transformed, 2))
        points = transformed + [root]
        value += 1 + profile["C"]
        assert sum(face_profile(points)) == value
        bit_length = max(
            max(abs(x).bit_length(), abs(y).bit_length()) for x, y in points
        )
        row = [new_size, slope, profile["C"], profile["U"], value, bit_length]
        rows.append(row)
    assert rows == expected_rows
    assert len({row[1] for row in rows}) == len(rows)
    return rows


def main():
    certificate = json.loads((HERE / "hull_root_envelope_certificate.json").read_text())

    exact_f = {int(k): v for k, v in certificate["exact_f"].items()}
    weighted = [exact_f[n + 1] - exact_f[n] - 1 for n in range(1, 9)]
    assert weighted == certificate["weighted_root_increments"]

    n9 = audit_n9(
        [tuple(row) for row in certificate["n9"]["points"]],
        certificate["n9"],
    )
    top = next(iter(n9["top_rows"].values()))
    assert top["child_V"] - exact_f[8] + top["C"] == weighted[7] == 54
    assert exact_f[9] == exact_f[8] + 1 + weighted[7]
    hinged = audit_sharp_hinged_n8(
        [tuple(row) for row in certificate["hinged_n8"]["points"]],
        certificate["hinged_n8"],
    )
    scalar = audit_scalar_barrier(certificate["scalar_audit_limit"])
    reset = audit_affine_reset_chain(certificate["affine_reset_rows"])

    print(
        "PASS: exact hull-root envelope/flag identities; "
        f"weighted increments={weighted}; n9={n9['shellings']} shellings, "
        f"{n9['sequences']} cost sequences, {n9['transitions']} root charts; "
        f"sharp hinged n8 (V,C,U)={hinged}; scalar last bad n={scalar[0]}; "
        f"stretchable fresh-chart chain through n={reset[-1][0]}"
    )


if __name__ == "__main__":
    main()
