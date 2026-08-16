#!/usr/bin/env python3
"""Exact audits for the forward/tangent Bellman follow-up on Erdos 838.

The script has several independent parts.

* It checks the exact two-root tangent compatibility criterion and a small
  rational example in which both root turns fail and no subset of the two
  roots repairs the union.
* It checks the dyadic-LCA partition of a one-dimensional tangent failure
  relation.  This is the combinatorial reason that a failed endpoint can be
  localized to one of only O(log n) separation levels.
* It checks a scalable *abstract* max-plus countercycle.  The countercycle
  satisfies all scalar inequalities currently available for a pocket
  (two-point endpoint floors, C U >= W, and the quarter-exponent local
  lower bound), but misses capped Hall by a linear exponent.  It is not
  asserted to be the profile of a realizable planar order type.

All geometric and countercycle checks use integer arithmetic.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    """Strict monotone-chain hull of integer points."""
    points = sorted(set(points))
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and orient(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orient(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def is_convex(points):
    return len(hull(points)) == len(set(points))


def non_chord_neighbor(cycle, root, other_root):
    i = cycle.index(root)
    left = cycle[(i - 1) % len(cycle)]
    right = cycle[(i + 1) % len(cycle)]
    assert (left == other_root) ^ (right == other_root)
    return right if left == other_root else left


def tangent_geometry_audit():
    u = (0, 0)
    v = (1, 0)

    # First the four-point regression from the ACP report: the u turn is
    # good and the v turn is bad.
    upper_one = [(100, 1)]
    lower_one = [(-100, -2)]

    # A cleaner integer example found in this lane.  Both rooted polygons
    # are convex and have uv as an edge, but both cross-root turns fail.
    # Moreover A union B remains nonconvex after adding any subset of {u,v}.
    upper = [(-7, 5)]
    lower = [(-4, -2), (5, -3), (7, -3), (-3, -1)]

    def record(a_chain, b_chain):
        upper_hull = hull([u, v, *a_chain])
        lower_hull = hull([u, v, *b_chain])
        assert len(upper_hull) == len(a_chain) + 2
        assert len(lower_hull) == len(b_chain) + 2
        au = non_chord_neighbor(upper_hull, u, v)
        av = non_chord_neighbor(upper_hull, v, u)
        bu = non_chord_neighbor(lower_hull, u, v)
        bv = non_chord_neighbor(lower_hull, v, u)
        turn_u = orient(au, u, bu)
        turn_v = orient(bv, v, av)
        compatible = turn_u > 0 and turn_v > 0
        actual = is_convex([u, v, *a_chain, *b_chain])
        assert compatible == actual
        root_subset_hull_sizes = {}
        for mask in range(4):
            roots = ([u] if mask & 1 else []) + ([v] if mask & 2 else [])
            candidate = [*roots, *a_chain, *b_chain]
            root_subset_hull_sizes[str(mask)] = len(hull(candidate))
        return {
            "upper": a_chain,
            "lower": b_chain,
            "turn_u": turn_u,
            "turn_v": turn_v,
            "compatible_by_turns": compatible,
            "convex_by_hull": actual,
            "root_subset_hull_sizes": root_subset_hull_sizes,
            "root_subset_point_counts": {
                str(mask): len(a_chain) + len(b_chain) + (mask & 1 != 0) + (mask & 2 != 0)
                for mask in range(4)
            },
        }

    one_bad = record(upper_one, lower_one)
    both_bad = record(upper, lower)
    assert one_bad["turn_u"] > 0 and one_bad["turn_v"] < 0
    assert both_bad["turn_u"] < 0 and both_bad["turn_v"] < 0
    assert all(
        both_bad["root_subset_hull_sizes"][str(mask)]
        < both_bad["root_subset_point_counts"][str(mask)]
        for mask in range(4)
    )
    return {"one_bad_endpoint": one_bad, "both_bad_endpoints": both_bad}


def dyadic_key(a, b, height):
    """LCA rectangle of two distinct ranks a<b in [0,2^height)."""
    assert 0 <= a < b < 1 << height
    differing_bit = (a ^ b).bit_length() - 1
    depth = height - 1 - differing_bit
    prefix = a >> (differing_bit + 1)
    # At their LCA, a is in the left child and b is in the right child.
    assert ((a >> differing_bit) & 1) == 0
    assert ((b >> differing_bit) & 1) == 1
    return depth, prefix


def dyadic_failure_audit():
    # Repeated ranks represent many rooted histories sharing one tangent
    # neighbor.  The weights make the check genuinely weighted.
    height = 5
    left_weight = [((7 * i + 3) % 11) + 1 for i in range(1 << height)]
    right_weight = [((5 * i + 1) % 13) + 1 for i in range(1 << height)]
    buckets = {}
    total = 0
    for a, wa in enumerate(left_weight):
        for b, wb in enumerate(right_weight):
            if a >= b:
                continue
            weight = wa * wb
            key = dyadic_key(a, b, height)
            buckets[key] = buckets.get(key, 0) + weight
            total += weight
    assert sum(buckets.values()) == total

    level_mass = [0] * height
    for (depth, _prefix), weight in buckets.items():
        level_mass[depth] += weight
    assert max(level_mass) * height >= total

    # At one fixed depth, distinct LCA nodes have disjoint rank intervals.
    for depth in range(height):
        nodes = sorted(prefix for d, prefix in buckets if d == depth)
        assert len(nodes) == len(set(nodes))

    return {
        "rank_count": 1 << height,
        "tree_height": height,
        "failure_relation_weight": total,
        "level_masses": level_mass,
        "largest_level": max(range(height), key=level_mass.__getitem__),
        "largest_level_fraction": max(level_mass) / total,
    }


def all_cup_cap_rows():
    rows = []
    for m in (8, 16, 32, 64):
        d = m + math.comb(m, 2)
        e = (1 << m) - 1
        bad_order = 2 * e + d * d
        reverse_order = 2 * e + e * e
        rows.append(
            {
                "m": m,
                "D": d,
                "E": e,
                "cup_then_cap_W": bad_order,
                "cap_then_cup_W": reverse_order,
                "orientation_gap_bits": math.log2(reverse_order) - math.log2(bad_order),
                "bad_order_W_over_local_W": bad_order / e,
            }
        )
        assert bad_order == 2 * e + d * d
        assert reverse_order == 2 * e + e * e
    return rows


def abstract_countercycle(s, base=16):
    """Build the exact scalar countercycle described in the report.

    The symbols x,c,u,w are logarithmic exponents.  Nothing in this
    function asserts that blocks with these four parameters are realizable.
    """
    m = base * (1 << s)
    assert m % 4 == 0
    t = m // 4
    h = m * m // 4
    left_x = [base << q for q in range(s)]
    plateau_count = t - 2
    assert plateau_count >= 2

    x = []
    c = []
    u = []
    w = []
    kind = []

    # Increasing cap-light tail.
    for value in left_x:
        local = value * value // 4
        x.append(value)
        c.append(2 * value)
        u.append(local - 2 * value)
        w.append(local)
        kind.append("left_tail")

    # A maximally anti-aligned plateau.  Its cap exponent increases just
    # fast enough to cancel every intervening singleton-choice exponent.
    for j in range(1, plateau_count + 1):
        cap = (2 if j == 1 else j) * m
        x.append(m)
        c.append(cap)
        u.append(h - cap)
        w.append(h)
        kind.append("plateau")

    # Decreasing cup-light mirror tail.
    for value in reversed(left_x):
        local = value * value // 4
        x.append(value)
        c.append(local - 2 * value)
        u.append(2 * value)
        w.append(local)
        kind.append("right_tail")

    b = len(x)
    source_entropy = sum(x)
    assert source_entropy == h - 2 * base
    assert b == t - 2 + 2 * s

    # These are precisely the scalar inequalities available to the proposed
    # F+W Bellman: endpoint pairs, C U >= W, and local quarter supply.
    for xi, ci, ui, wi in zip(x, c, u, w):
        assert ci >= 2 * xi
        assert ui >= 2 * xi
        assert wi >= ci and wi >= ui
        assert ci + ui >= wi
        assert wi >= xi * xi // 4

    prefix = [0]
    for value in x:
        prefix.append(prefix[-1] + value)
    forward_max = -1
    forward_argmax = None
    for i, j in combinations(range(b), 2):
        middle = prefix[j] - prefix[i + 1]
        term = c[i] + u[j] + middle
        if term > forward_max:
            forward_max = term
            forward_argmax = (i, j)
    local_max = max(w)
    bellman_capacity = max(local_max, forward_max)
    assert forward_max == h
    assert local_max == h

    # log |S| + log n - rank, with log n replaced by the smaller main term
    # m.  The true ambient log is m+Theta(log b), so this is a conservative
    # capped-Hall target.
    capped_target_main = source_entropy + m - b
    deficit = capped_target_main - bellman_capacity
    expected_deficit = m - b - 2 * base
    assert deficit == expected_deficit
    assert deficit > 0

    return {
        "s": s,
        "base": base,
        "max_block_log_size_M": m,
        "block_count_b": b,
        "plateau_count": plateau_count,
        "source_entropy": source_entropy,
        "local_quarter_capacity": local_max,
        "max_forward_capacity": forward_max,
        "forward_argmax": forward_argmax,
        "capped_target_using_log_n_ge_M": capped_target_main,
        "linear_exponent_deficit": deficit,
        "deficit_over_M": deficit / m,
        "state_kinds": {
            label: kind.count(label) for label in sorted(set(kind))
        },
    }


def fixed_child_batch_rows():
    """Numerical scale audit for Proposition 8 in the report."""
    rows = []
    c = 0.24
    for r in (64, 128, 256, 512, 1024):
        depth = math.ceil(math.sqrt(r))
        log_source_bound = (depth + 1) * r
        loss_exponent = math.sqrt(log_source_bound / c) + 2
        rows.append(
            {
                "rank_r": r,
                "batch_depth": depth,
                "log2_fixed_child_prefix_count_upper": log_source_bound,
                "chosen_ES_constant_c": c,
                "log2_congestion_upper": loss_exponent,
                "congestion_exponent_over_r": loss_exponent / r,
            }
        )
    assert rows[-1]["congestion_exponent_over_r"] < rows[0]["congestion_exponent_over_r"]
    return rows


def prefix_cube_collapse_rows():
    """Exact set-system regression for invisible discarded coordinates."""
    rows = []
    for depth, alphabet in ((4, 16), (8, 64), (16, 256)):
        paths = alphabet**depth
        visible_subsets = (alphabet + 1) ** depth
        rank_drop_allowance = 1 << depth
        rows.append(
            {
                "depth": depth,
                "alphabet": alphabet,
                "projection_fibre": paths,
                "rank_drop_allowance": rank_drop_allowance,
                "fibre_over_allowance": paths / rank_drop_allowance,
                "union_of_path_boolean_cubes": visible_subsets,
                "boolean_union_over_paths": visible_subsets / paths,
            }
        )
        assert paths > rank_drop_allowance
        assert visible_subsets < rank_drop_allowance * paths
    return rows


def weighted_exposure_amgm_audit():
    """Exhaust Lemma 9 on a nontrivial rational grid.

    Thresholds are deliberately heterogeneous.  Since the proof only uses
    the pointwise floor 2^{-t} >= 2^{-s}, exhaustive tests of every threshold
    assignment would add no logical coverage and would be prohibitively
    large; the boundary cases t=s and t=0 are included explicitly below.
    """
    values = tuple(Fraction(i, 4) for i in range(5))
    tested = 0
    tight = 0
    worst_slack = None
    for q in range(1, 7):
        for s in range(5):
            cap = 1 << s
            threshold_patterns = (
                lambda i, j, s=s: s,
                lambda i, j: 0,
                lambda i, j, s=s: (3 * i + 5 * j) % (s + 1),
            )
            for alpha in product(values, repeat=q):
                z = sum(alpha, Fraction(0))
                for threshold in threshold_patterns:
                    pair_credit = sum(
                        alpha[i] * alpha[j] / (1 << threshold(i, j))
                        for i, j in combinations(range(q), 2)
                    )
                    slack = Fraction(cap) + pair_credit - z
                    assert slack >= 0
                    tested += 1
                    tight += slack == 0
                    if worst_slack is None or slack < worst_slack:
                        worst_slack = slack
    return {
        "rational_grid_denominator": 4,
        "max_coordinate_count": 6,
        "max_depth": 4,
        "threshold_patterns_per_vector": 3,
        "instances_checked": tested,
        "tight_instances": tight,
        "minimum_slack": str(worst_slack),
    }


def _threshold_pair_mass(edges, left_size, right_size, depth):
    """Return the full and disjoint left-pair masses in (46)--(49)."""
    left_neighbors = [set() for _ in range(left_size)]
    for a, b in edges:
        left_neighbors[a].add(b)
    full = Fraction(0)
    disjoint = Fraction(0)
    for a, aa in combinations(range(left_size), 2):
        t = (a + 2 * aa) % (depth + 1)
        weight = Fraction(1, 1 << t)
        full += len(left_neighbors[a]) * len(left_neighbors[aa]) * weight
        distinct_right_pairs = sum(
            b != bb
            for b in left_neighbors[a]
            for bb in left_neighbors[aa]
        )
        disjoint += distinct_right_pairs * weight
    return full, disjoint


def ordered_array_threshold_audit():
    """Exhaust (46) and the graph-corrected inequality (49) on 3x3 graphs."""
    left_size = right_size = 3
    all_edges = [(a, b) for a in range(left_size) for b in range(right_size)]
    checked = 0
    min_slack_46 = None
    min_slack_49 = None
    for mask in range(1, 1 << len(all_edges)):
        edges = [edge for bit, edge in enumerate(all_edges) if mask >> bit & 1]
        m = len(edges)
        left_degree = [sum(a == aa for aa, _ in edges) for a in range(left_size)]
        right_degree = [sum(b == bb for _, bb in edges) for b in range(right_size)]

        # Equation (49) chooses the side of larger maximum degree.  Transpose
        # the array when the right marginal is larger.
        if max(left_degree) >= max(right_degree):
            oriented_edges = edges
        else:
            oriented_edges = [(b, a) for a, b in edges]
        delta = max(sum(a == aa for aa, _ in oriented_edges) for a in range(left_size))

        for depth in range(4):
            full, disjoint = _threshold_pair_mass(
                oriented_edges, left_size, right_size, depth
            )
            rhs_46 = (1 << depth) * delta + full / delta
            rhs_49 = 2 * (1 << depth) * delta + 2 * disjoint / delta
            slack_46 = rhs_46 - m
            slack_49 = rhs_49 - m
            assert slack_46 >= 0
            assert slack_49 >= 0
            min_slack_46 = slack_46 if min_slack_46 is None else min(min_slack_46, slack_46)
            min_slack_49 = slack_49 if min_slack_49 is None else min(min_slack_49, slack_49)
            checked += 1
    return {
        "bipartite_array_shape": [left_size, right_size],
        "nonempty_support_graphs": (1 << len(all_edges)) - 1,
        "depths": [0, 1, 2, 3],
        "instances_checked": checked,
        "minimum_slack_equation_46": str(min_slack_46),
        "minimum_slack_equation_49": str(min_slack_49),
    }


def high_row_decoder_rows():
    """Check the conditional high-row algebra and its point-word vacuity."""
    rows = []
    for rank in (64, 128, 256, 512):
        batch = math.ceil(math.sqrt(rank))
        # A representative critical regime log_2 n=2r, d=2^r.
        n = 1 << (2 * rank)
        d = 1 << rank
        b_order = n + 1
        recovery = 2 * batch * batch * (batch + 1) * n ** (3 * batch)
        cutoff = 4 * d * b_order * recovery
        max_distinct_batch_words = n**batch
        assert cutoff > max_distinct_batch_words
        child_count = cutoff
        assert child_count >= 2 * b_order

        # The split theorem is rational.  Its weaker quadratic form is the
        # exact expression used to prove (54).
        split_lower = Fraction(child_count, 2) * (
            Fraction(child_count, b_order) - 1
        )
        quadratic_lower = Fraction(child_count * child_count, 4 * b_order)
        assert split_lower >= quadratic_lower
        recovered = quadratic_lower / recovery
        demand = d * child_count
        assert recovered >= demand

        log_cutoff = math.log2(cutoff)
        rows.append(
            {
                "rank_r": rank,
                "batch_length": batch,
                "log2_n": 2 * rank,
                "log2_high_row_cutoff": log_cutoff,
                "log2_max_distinct_batch_words": math.log2(max_distinct_batch_words),
                "cutoff_over_max_words_log2": log_cutoff
                - math.log2(max_distinct_batch_words),
                "cutoff_log_over_r_squared": log_cutoff / (rank * rank),
                "cutoff_log_over_r": log_cutoff / rank,
                "recovered_over_selected_demand": float(recovered / demand),
            }
        )
    assert rows[-1]["cutoff_log_over_r_squared"] < rows[0]["cutoff_log_over_r_squared"]
    assert rows[-1]["cutoff_log_over_r"] > rows[0]["cutoff_log_over_r"]
    return rows


def weighted_prefix_projection_rows():
    """Scalable countercycle to naive global Boolean + weighted-pair summing."""
    rows = []
    for rank in (16, 32, 64, 128, 256):
        depth = math.ceil(math.sqrt(rank))
        alphabet = 1 << rank
        histories = alphabet**depth
        selected_mass = histories * alphabet
        boolean_union = (alphabet + 1) ** depth
        delayed_pair_credit = Fraction(math.comb(alphabet, 2), 1 << depth)
        proposed_capacity = boolean_union + delayed_pair_credit
        assert selected_mass > proposed_capacity
        log_ratio = (
            math.log2(selected_mass * proposed_capacity.denominator)
            - math.log2(proposed_capacity.numerator)
        )
        rows.append(
            {
                "rank_r": rank,
                "depth_s": depth,
                "log2_alphabet_M": rank,
                "log2_history_count": depth * rank,
                "log2_selected_mass": (depth + 1) * rank,
                "log2_selected_over_projected_capacity": log_ratio,
                "gap_over_log2_M": log_ratio / rank,
            }
        )
    assert rows[-1]["gap_over_log2_M"] > 0.99
    return rows


def main():
    result = {
        "schema": "erdos838-forward-tangent-bellman-v1",
        "tangent_geometry": tangent_geometry_audit(),
        "dyadic_failure_partition": dyadic_failure_audit(),
        "realizable_all_cup_cap_stress": all_cup_cap_rows(),
        "abstract_capped_countercycles": [abstract_countercycle(s) for s in range(3, 8)],
        "fixed_child_sqrt_rank_batch": fixed_child_batch_rows(),
        "prefix_cube_collapse": prefix_cube_collapse_rows(),
        "weighted_exposure_amgm": weighted_exposure_amgm_audit(),
        "ordered_array_threshold": ordered_array_threshold_audit(),
        "high_row_decoder": high_row_decoder_rows(),
        "weighted_prefix_projection_countercycle": weighted_prefix_projection_rows(),
        "claim_scope": (
            "The tangent and all-cup/all-cap checks are realizable.  The scalable "
            "capped countercycle is only a scalar-inequality obstruction, not a "
            "realizable planar construction."
        ),
    }
    out = HERE / "forward_bellman_certificate.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
