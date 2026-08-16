#!/usr/bin/env python3
"""Exact checks for PARENT_SEAM_JET_COMPLETION.md.

Only integer/rational orientation arithmetic is used.  No floating point
geometry or external package enters the certificate.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import combinations
from pathlib import Path


Point = tuple[Fraction | int, Fraction | int]


def cross(a: Point, b: Point, c: Point):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def general_position(points: list[Point]) -> bool:
    return len(set(points)) == len(points) and all(
        cross(a, b, c) != 0 for a, b, c in combinations(points, 3)
    )


def hull(points: list[Point]) -> list[Point]:
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts
    lower: list[Point] = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper: list[Point] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def convex(points: list[Point]) -> bool:
    if len(points) <= 2:
        return len(set(points)) == len(points)
    return general_position(points) and len(hull(points)) == len(points)


def all_nonempty_subsets(points: list[Point]):
    for mask in range(1, 1 << len(points)):
        yield tuple(points[i] for i in range(len(points)) if (mask >> i) & 1)


def ear_data(T: list[Point], X: tuple[Point, ...]):
    """Return oriented parent edge indices and inserted cyclic sequence."""
    ht = hull(T)
    hx = hull(T + list(X))
    sx = set(X)
    n = len(hx)
    starts = [
        i for i, p in enumerate(hx) if p in sx and hx[(i - 1) % n] not in sx
    ]
    assert len(starts) == 1, (T, X, hx)
    start = starts[0]
    seq: list[Point] = []
    i = start
    while hx[i] in sx:
        seq.append(hx[i])
        i = (i + 1) % n
    u = hx[(start - 1) % n]
    v = hx[i]
    iu, iv = ht.index(u), ht.index(v)
    assert iv == (iu + 1) % len(ht)
    return iu, iv, tuple(seq)


def seam_prediction(T: list[Point], L: tuple[Point, ...], R: tuple[Point, ...]):
    ht = hull(T)
    i, j, left = ear_data(T, L)
    k, ell, right = ear_data(T, R)

    if (i, j) == (k, ell):
        # On an empty x-side, the block next to the oriented initial endpoint
        # is determined by whether that endpoint is the left or right root.
        if ht[i][0] < ht[j][0]:
            first, second = left, right
            first_name = "L"
        else:
            first, second = right, left
            first_name = "R"
        prev = ht[i] if len(first) == 1 else first[-2]
        nxt = ht[j] if len(second) == 1 else second[1]
        jet = (prev, first[-1], second[0], nxt)
        good = cross(jet[0], jet[1], jet[2]) > 0 and cross(
            jet[1], jet[2], jet[3]
        ) > 0
        state = ("same", i, j, first_name, jet)
        return good, state

    if j == k:
        jet = (left[-1], ht[j], right[0])
        return cross(*jet) > 0, ("adjacent", i, j, ell, jet[0], jet[2])
    if ell == i:
        jet = (right[-1], ht[i], left[0])
        return cross(*jet) > 0, ("adjacent", k, ell, j, jet[0], jet[2])

    assert not ({i, j} & {k, ell})
    return True, ("disjoint", i, j, k, ell)


def check_rooted_multi_ears():
    a = (-1, 0)
    b = (1, 0)
    root = [a, b]
    left_pool = [(-6, -10), (-6, -9), (-5, -6), (-4, -12), (-3, -5)]
    right_pool = [(2, -9), (3, -10), (4, -7), (5, -13), (6, -4)]
    parent_tip = (Fraction(0), Fraction(1, 2))
    ambient = root + [parent_tip] + left_pool + right_pool
    assert general_position(ambient)

    left_faces = [
        X for X in all_nonempty_subsets(left_pool) if convex(root + list(X))
    ]
    right_faces = [
        Y for Y in all_nonempty_subsets(right_pool) if convex(root + list(Y))
    ]
    assert (len(left_faces), len(right_faces)) == (18, 22)

    counts = {"good": 0, "bad": 0}
    state_truth: dict[object, set[bool]] = {}
    indexed_pairs = []
    for li, L in enumerate(left_faces):
        for ri, R in enumerate(right_faces):
            predicted, state = seam_prediction(root, L, R)
            actual = convex(root + list(L) + list(R))
            assert predicted == actual
            counts["good" if actual else "bad"] += 1
            state_truth.setdefault(state, set()).add(actual)
            indexed_pairs.append((li, ri, L, R, state, actual))
    assert counts == {"good": 221, "bad": 175}
    assert all(len(values) == 1 for values in state_truth.values())

    # Select a sparse deterministic subgraph of the good pairs, then complete
    # every active jet cell and verify the exact rectangle bank.
    selected = [
        row for row in indexed_pairs if row[5] and (row[0] + 2 * row[1]) % 3 == 0
    ]
    cells: dict[object, tuple[set[int], set[int]]] = {}
    for li, ri, _L, _R, state, _actual in selected:
        left_ids, right_ids = cells.setdefault(state, (set(), set()))
        left_ids.add(li)
        right_ids.add(ri)

    completed_pairs: set[tuple[int, int]] = set()
    for state, (left_ids, right_ids) in cells.items():
        for li in left_ids:
            for ri in right_ids:
                L, R = left_faces[li], right_faces[ri]
                prediction, recovered_state = seam_prediction(root, L, R)
                assert recovered_state == state and prediction
                assert convex(root + list(L) + list(R))
                completed_pairs.add((li, ri))

    selected_pairs = {(row[0], row[1]) for row in selected}
    assert selected_pairs <= completed_pairs

    # Restore a nontrivial parent on the opposite side of the root and audit
    # all Boolean parent deletions in the completed bank.
    T = [a, b, parent_tip]
    boolean_outputs = set()
    for li, ri in completed_pairs:
        L, R = left_faces[li], right_faces[ri]
        assert convex(T + list(L) + list(R))
        for mask in range(1 << len(T)):
            U = tuple(T[i] for i in range(len(T)) if (mask >> i) & 1)
            output = frozenset(L + R + U)
            assert convex(list(output))
            boolean_outputs.add(output)
    assert len(boolean_outputs) == (1 << len(T)) * len(completed_pairs)

    return {
        "left_rooted_faces": len(left_faces),
        "right_rooted_faces": len(right_faces),
        "rooted_pairs": len(indexed_pairs),
        "good_rooted_pairs": counts["good"],
        "bad_rooted_pairs": counts["bad"],
        "jet_states": len(state_truth),
        "selected_pairs": len(selected_pairs),
        "active_selected_states": len(cells),
        "completed_pairs": len(completed_pairs),
        "boolean_outputs": len(boolean_outputs),
    }


def check_singleton_parent_grid():
    parents = [
        [(-3, 0), (3, 0), (0, 4)],
        [(-3, 0), (0, -3), (3, 0), (0, 4)],
        [(-3, 0), (3, 0), (2, 3), (0, 5), (-2, 4)],
    ]
    totals = {"same": 0, "adjacent_good": 0, "adjacent_bad": 0, "disjoint": 0}
    audited = 0
    endpoint_incidence = 0

    for T in parents:
        assert convex(T)
        ht = hull(T)
        a = min(ht, key=lambda p: p[0])
        b = max(ht, key=lambda p: p[0])
        xmin, xmax = a[0], b[0]
        left = [
            (x, y)
            for x in range(xmin - 5, xmin)
            for y in range(-9, 10)
            if convex(T + [(x, y)])
        ]
        right = [
            (x, y)
            for x in range(xmax + 1, xmax + 6)
            for y in range(-9, 10)
            if convex(T + [(x, y)])
        ]
        for L in left:
            i, j, _ = ear_data(T, (L,))
            assert a in (ht[i], ht[j])
            for R in right:
                if not general_position(T + [L, R]):
                    continue
                k, ell, _ = ear_data(T, (R,))
                assert b in (ht[k], ht[ell])
                endpoint_incidence += 2
                predicted, state = seam_prediction(T, (L,), (R,))
                actual = convex(T + [L, R])
                assert predicted == actual
                audited += 1
                if state[0] == "same":
                    totals["same"] += 1
                elif state[0] == "disjoint":
                    assert actual
                    totals["disjoint"] += 1
                elif actual:
                    totals["adjacent_good"] += 1
                else:
                    totals["adjacent_bad"] += 1

    assert audited == sum(totals.values())
    assert all(totals[key] > 0 for key in totals)

    # A parent with at least two internal vertices on each x-chain.  The
    # preserving insertion wedges are narrow, so use exact rational points.
    F = Fraction
    long_parent = [
        (F(-5), F(0)), (F(-4), F(-3)), (F(-1), F(-5)), (F(3), F(-4)),
        (F(5), F(0)), (F(4), F(3)), (F(1), F(5)), (F(-3), F(4)),
    ]
    L = (F(-6), F(25, 8))
    R = (F(6), F(-25, 8))
    assert convex(long_parent + [L]) and convex(long_parent + [R])
    p, state = seam_prediction(long_parent, (L,), (R,))
    assert state[0] == "disjoint" and p and convex(long_parent + [L, R])
    audited += 1
    totals["disjoint"] += 1

    return {
        "singleton_pairs": audited,
        "endpoint_incidence_checks": endpoint_incidence,
        **totals,
    }


def check_short_side_examples():
    # Empty lower parent side; the upper side has three internal vertices.
    T = [(-3, 0), (3, 0), (2, 3), (0, 4), (-2, 3)]
    L, R = (-6, -12), (4, 1)
    assert general_position(T + [L, R])
    assert convex(T + [L]) and convex(T + [R])
    assert not convex(T + [L, R])
    assert (3, 0) not in hull(T + [L, R])
    predicted, state = seam_prediction(T, (L,), (R,))
    assert state[0] == "adjacent" and not predicted

    # The unique lower parent vertex gives the exact Ferrers threshold.
    diamond = [(-2, 0), (0, -2), (2, 0), (0, 2)]
    ferrers_checks = 0
    for y in range(-5, 3):
        left = (-3, y)
        if not convex(diamond + [left]):
            continue
        for z in range(-5, 3):
            right = (3, z)
            if not convex(diamond + [right]) or not general_position(diamond + [left, right]):
                continue
            eL = ear_data(diamond, (left,))[:2]
            eR = ear_data(diamond, (right,))[:2]
            if eL == (0, 1) and eR == (1, 2):
                assert cross(left, (0, -2), right) == 3 * (y + z + 4)
                assert convex(diamond + [left, right]) == (y + z > -4)
                ferrers_checks += 1
    assert ferrers_checks > 5

    # Same root edge: the second seam turn is genuinely necessary.
    root = [(-1, 0), (1, 0)]
    left = ((-6, -9), (-6, -10))
    right = ((2, -9), (3, -10))
    assert general_position(root + list(left) + list(right))
    assert convex(root + list(left)) and convex(root + list(right))
    i, j, lseq = ear_data(root, left)
    k, ell, rseq = ear_data(root, right)
    assert (i, j) == (k, ell)
    first_turn = cross(lseq[-2], lseq[-1], rseq[0])
    second_turn = cross(lseq[-1], rseq[0], rseq[1])
    assert first_turn > 0 and second_turn < 0
    assert not convex(root + list(left) + list(right))
    assert (2, -9) not in hull(root + list(left) + list(right))

    return {
        "strict_endpoint_counterexample": True,
        "ferrers_threshold_checks": ferrers_checks,
        "same_edge_first_turn": first_turn,
        "same_edge_second_turn": second_turn,
    }


def check_separated_pair_square_loss():
    # Exact arithmetic from the four-cell conic audit in the outer report.
    m = (2, 3, 2, 3)
    H = (4, 8, 4, 8)
    p0 = 1
    for value in m:
        p0 *= value
    bank_sizes = tuple(H[g] * p0 // m[g] for g in range(len(m)))
    M = p0 // 2
    maximum = max(bank_sizes)
    assert (p0, M, bank_sizes, maximum) == (36, 18, (72, 96, 72, 96), 96)
    assert maximum > M and maximum < M * M
    # Hence B/M is a nontrivial multiplier, while sqrt(B)<M.  Avoiding
    # floating point, the latter is exactly B<M^2.
    return {
        "selected_records_M": M,
        "full_projection_product_P0": p0,
        "pair_bank_sizes": bank_sizes,
        "maximum_pair_bank": maximum,
        "B_over_M_numerator": maximum,
        "B_over_M_denominator": M,
        "pair_bank_below_M_squared": maximum < M * M,
    }


def main():
    rooted = check_rooted_multi_ears()
    singleton = check_singleton_parent_grid()
    examples = check_short_side_examples()
    square_loss = check_separated_pair_square_loss()
    certificate = {
        "artifact": "PARENT_SEAM_JET_COMPLETION",
        "arithmetic": "exact integers and fractions",
        "status": "PASS",
        "rooted_multi_ear_audit": rooted,
        "fixed_parent_singleton_audit": singleton,
        "sharp_examples": examples,
        "separated_pair_square_loss": square_loss,
    }
    output = Path(__file__).with_name("parent_seam_jet_completion_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
