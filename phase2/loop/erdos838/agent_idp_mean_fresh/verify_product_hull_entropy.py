#!/usr/bin/env python3
"""Exact audit of product-hull entropy and rooted-cluster identities."""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LATTICE = ROOT / "agent_planar_lattice_mean"
LEX = ROOT / "agent_lex_minimizer_search"
sys.path.insert(0, str(LATTICE))

from planar_lattice_mean import closure_mask, convex_hull, is_convex  # noqa: E402


PROFILE_58 = (1, 58, 1653, 30856, 220958, 428915, 284982, 76995, 15100, 2179, 210)


def points_4() -> tuple[tuple[int, int], ...]:
    return ((0, 0), (12, 0), (0, 12), (2, 3))


def points_9() -> tuple[tuple[int, int], ...]:
    record = json.loads((LEX / "exact_realizable_n9.json").read_text())
    return tuple(sorted(tuple(point) for point in record["coordinates_as_stored"]))


def masks_of_size(mask: int, size: int):
    labels = [i for i in range(mask.bit_length()) if (mask >> i) & 1]
    for chosen in combinations(labels, size):
        yield sum(1 << i for i in chosen)


def hull_and_closure(points, sample: int) -> tuple[int, int]:
    labels = [i for i in range(len(points)) if (sample >> i) & 1]
    hull = convex_hull(points, labels)
    hull_mask = sum(1 << i for i in hull)
    return hull_mask, closure_mask(points, hull)


def jointly_good(points, closed: int, exterior_subset: int) -> bool:
    labels = [
        i for i in range(len(points))
        if ((closed | exterior_subset) >> i) & 1
    ]
    hull = set(convex_hull(points, labels))
    return all(i in hull for i in range(len(points)) if (exterior_subset >> i) & 1)


def state_table(points):
    n = len(points)
    full = (1 << n) - 1
    rows = []
    for sample in range(1 << n):
        hull, closed = hull_and_closure(points, sample)
        exterior = full ^ closed
        bad_by_size = [0] * (n + 1)
        good_by_size = [0] * (n + 1)
        all_bad_masks = []
        sub = exterior
        while True:
            size = sub.bit_count()
            if jointly_good(points, closed, sub):
                good_by_size[size] += 1
            else:
                bad_by_size[size] += 1
                all_bad_masks.append(sub)
            if sub == 0:
                break
            sub = (sub - 1) & exterior

        # Every bad set contains a bad rooted cluster of size 2, 3, or 4.
        for bad in all_bad_masks:
            witness = False
            for size in range(2, min(4, bad.bit_count()) + 1):
                if any(not jointly_good(points, closed, part) for part in masks_of_size(bad, size)):
                    witness = True
                    break
            if not witness:
                raise AssertionError(("missing size-four witness", sample, closed, bad))

        o = exterior.bit_count()
        bad_total = sum(bad_by_size)
        rooted_cover = sum(bad_by_size[s] * (1 << (o - s)) for s in range(2, min(4, o) + 1))
        if bad_total > rooted_cover:
            raise AssertionError(("rooted cover", sample, bad_total, rooted_cover))
        rows.append(
            {
                "sample": sample,
                "sample_size": sample.bit_count(),
                "hull_size": hull.bit_count(),
                "closed": closed,
                "exterior_size": o,
                "good_by_size": good_by_size,
                "bad_by_size": bad_by_size,
                "bad_total": bad_total,
                "rooted_cover": rooted_cover,
            }
        )
    return rows


def weighted_moments(rows, n: int, p: Fraction):
    one_minus = 1 - p
    q = one_minus / p
    lhs = [Fraction() for _ in range(n + 1)]
    hull = [Fraction() for _ in range(n + 1)]
    bad = [Fraction() for _ in range(n + 1)]
    exp_o = Fraction()
    exp_h = Fraction()
    rooted_cover = Fraction()
    for row in rows:
        weight = p ** row["sample_size"] * one_minus ** (n - row["sample_size"])
        o = row["exterior_size"]
        h = row["hull_size"]
        exp_o += weight * (1 << o)
        exp_h += weight * (1 << h)
        rooted_cover += weight * row["rooted_cover"]
        for j in range(n + 1):
            lhs[j] += weight * math.comb(o, j)
            hull[j] += weight * math.comb(h, j)
            bad[j] += weight * row["bad_by_size"][j]
    for j in range(n + 1):
        if lhs[j] != q**j * hull[j] + bad[j]:
            raise AssertionError(("factorial toggle", p, j, lhs[j], hull[j], bad[j]))
    if p == Fraction(1, 2):
        if exp_o - exp_h != sum(bad):
            raise AssertionError("exponential toggle identity")
        if exp_o - exp_h > rooted_cover:
            raise AssertionError("averaged rooted cover")
        mean_o, mean_h = lhs[1], hull[1]
        var_o = 2 * lhs[2] + mean_o - mean_o * mean_o
        var_h = 2 * hull[2] + mean_h - mean_h * mean_h
        if bad[2] != (var_o - var_h) / 2:
            raise AssertionError("pair capture/variance identity")
    return {
        "p": str(p),
        "E_binom_O": [str(value) for value in lhs],
        "E_binom_H": [str(value) for value in hull],
        "bad_cluster_moments": [str(value) for value in bad],
        "E_2_to_O": str(exp_o),
        "E_2_to_H": str(exp_h),
        "weighted_rooted_cover": str(rooted_cover),
    }


def all_rank_entropy(points):
    n = len(points)
    faces = []
    for mask in range(1 << n):
        labels = [i for i in range(n) if (mask >> i) & 1]
        if not is_convex(points, labels):
            continue
        closed = closure_mask(points, labels)
        faces.append((len(labels), n - closed.bit_count()))
    v = len(faces)
    rank_sum = sum(h for h, _ in faces)
    exterior_sum = sum(o for _, o in faces)
    mu = Fraction(rank_sum, v)
    qbar = Fraction(exterior_sum, v)
    p_star = mu / (mu + qbar)

    # Exact hull-event normalization at three activities, plus p*.
    hull_sums = {}
    for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), p_star):
        total = sum((p**h * (1 - p) ** o for h, o in faces), Fraction())
        if total != 1:
            raise AssertionError(("hull activity", p, total))
        hull_sums[str(p)] = str(total)

    # The equality is analytic because it contains logarithms.  Every input
    # to it above has already been reconstructed exactly.
    cross_entropy = -float(mu) * math.log2(float(p_star)) - float(qbar) * math.log2(float(1 - p_star))
    divergence = sum(
        (1 / v) * math.log2((1 / v) / float(p_star**h * (1 - p_star) ** o))
        for h, o in faces
    )
    psi = cross_entropy
    if abs(math.log2(v) - (psi - divergence)) > 2e-12:
        raise AssertionError("optimized KL equality")
    inverse_bound = float(mu) * (2 ** (math.log2(v) / float(mu)) / math.e - 1)
    if float(qbar) + 1e-12 < inverse_bound:
        raise AssertionError("explicit exterior inverse")
    return {
        "V": v,
        "mu": str(mu),
        "mean_exterior": str(qbar),
        "p_star": str(p_star),
        "Psi": psi,
        "KL_uniform_to_product_hull": divergence,
        "log2_V": math.log2(v),
        "inverse_exterior_lower_bound": inverse_bound,
        "hull_activity_sums": hull_sums,
        "sum_two_to_minus_exterior": str(
            sum((Fraction(1, 2**o) for _, o in faces), Fraction())
        ),
    }


def sharp_four_point_state(points, rows):
    empty = rows[0]
    if empty["bad_by_size"][2] != 0 or empty["bad_by_size"][3] != 0:
        raise AssertionError("pair/triple sharpness failed")
    if empty["bad_by_size"][4] != 1:
        raise AssertionError("rooted quadruple missing")
    return {
        "closed_state": "empty",
        "bad_pairs": 0,
        "bad_triples": 0,
        "bad_quadruples": 1,
        "coordinates": [list(point) for point in points],
    }


def finite_idp_kill():
    n = 58
    z_one = sum(PROFILE_58)
    z_half = sum((Fraction(value, 2**rank) for rank, value in enumerate(PROFILE_58)), Fraction())
    h_value = Fraction(n) * z_half / z_one
    expected = Fraction(33994061, 16990512)
    if h_value != expected or h_value <= 2:
        raise AssertionError((h_value, expected))
    l_value = math.log(float(Fraction(n, 1) / h_value))
    target = math.log(n / 2)
    forced_deficit = math.log(float(h_value / 2))
    if not l_value < target or abs(target - l_value - forced_deficit) > 2e-15:
        raise AssertionError("finite IDP implication")
    return {
        "n": n,
        "H": str(h_value),
        "path_expectation_upper_bound_log_n_over_H": l_value,
        "target_log_n_over_2": target,
        "forced_deficit_before_path_KL": forced_deficit,
        "conclusion": "finite IDP is false",
    }


def audit(name: str, points):
    rows = state_table(points)
    entropy = all_rank_entropy(points)
    half = weighted_moments(rows, len(points), Fraction(1, 2))
    if Fraction(entropy["sum_two_to_minus_exterior"]) != Fraction(half["E_2_to_H"]):
        raise AssertionError("joint-toggle face-sum identity")
    return {
        "name": name,
        "n": len(points),
        "all_rank_entropy": entropy,
        "factorial_toggling": [
            half if p == Fraction(1, 2) else weighted_moments(rows, len(points), p)
            for p in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3))
        ],
        "max_rooted_cover_ratio": max(
            (row["rooted_cover"] / row["bad_total"] if row["bad_total"] else 1)
            for row in rows
        ),
        "states_checked": len(rows),
    }, rows


def main() -> None:
    four = points_4()
    result_4, rows_4 = audit("triangle_plus_interior", four)
    result_4["sharp_size_four_state"] = sharp_four_point_state(four, rows_4)
    result_9, _ = audit("exact_f9_minimizer", points_9())
    output = {
        "status": "PASS",
        "finite_idp_kill": finite_idp_kill(),
        "records": [result_4, result_9],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
