#!/usr/bin/env python3
"""Exact audits for the two-ended/cyclic-window attack on Erdos 838.

The finite part uses exact rational coordinates from the product-blocker
construction.  The scalable part is integer arithmetic except for reported
base-two logarithms.  No numerical orientation predicate is used.
"""

from __future__ import annotations

import importlib.util
import json
import math
from itertools import combinations, product
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS838 = HERE.parent
PRODUCT_VERIFIER = ERDOS838 / "agent_entropy_spread" / "verify_product_blocker.py"


def load_product_module():
    spec = importlib.util.spec_from_file_location("product_blocker", PRODUCT_VERIFIER)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def hull_order(points, indices, orient):
    """Counterclockwise monotone-chain hull, with exact predicates."""
    ordered = sorted(indices, key=lambda i: (points[i][0], points[i][1]))
    if len(ordered) <= 2:
        return ordered
    lower = []
    for i in ordered:
        while len(lower) >= 2 and orient(points[lower[-2]], points[lower[-1]], points[i]) <= 0:
            lower.pop()
        lower.append(i)
    upper = []
    for i in reversed(ordered):
        while len(upper) >= 2 and orient(points[upper[-2]], points[upper[-1]], points[i]) <= 0:
            upper.pop()
        upper.append(i)
    return lower[:-1] + upper[:-1]


def violated_edges(points, polygon, p, orient):
    """Support edges of a CCW convex polygon violated by p."""
    return frozenset(
        i
        for i in range(len(polygon))
        if orient(points[polygon[i]], points[polygon[(i + 1) % len(polygon)]], points[p]) < 0
    )


def cap_cup_subsets(points, block, orient):
    caps = []
    cups = []
    for size in range(1, len(block) + 1):
        for subset in combinations(block, size):
            signs = [orient(points[i], points[j], points[k]) for i, j, k in combinations(subset, 3)]
            if all(sign < 0 for sign in signs):
                caps.append(subset)
            if all(sign > 0 for sign in signs):
                cups.append(subset)
    return caps, cups


def exact_product_cell_audit(r=8, m=3):
    """Verify full two-ended multiplication and the global-fibre barrier."""
    product_module = load_product_module()
    points, blocks, cloud, epsilon, delta = product_module.build(r, m)
    orient = product_module.orient
    hull = product_module.hull
    b = r - 2

    # Full two-ended faces: arbitrary cap in the first internal block,
    # arbitrary cup in the last, and one point in every middle block.
    caps, _ = cap_cup_subsets(points, blocks[1], orient)
    _, cups = cap_cup_subsets(points, blocks[-2], orient)
    two_ended = set()
    for cap, cup in product(caps, cups):
        for middle in product(*blocks[2:-2]):
            target = tuple((*cap, *middle, *cup))
            assert hull(points, target) == set(target)
            two_ended.add(frozenset(target))
    expected_full = len(caps) * len(cups) * m ** (b - 2)
    assert len(two_ended) == expected_full

    # All ordered block intervals, and the exact two-scalar forward scan
    # P_j=C_j+m_j P_(j-1), F_j=F_(j-1)+P_(j-1)U_j.
    all_interval_faces = set()
    cap_counts = []
    cup_counts = []
    for block in blocks[1:-1]:
        block_caps, block_cups = cap_cup_subsets(points, block, orient)
        cap_counts.append(len(block_caps))
        cup_counts.append(len(block_cups))
    for i in range(b):
        block_caps, _ = cap_cup_subsets(points, blocks[i + 1], orient)
        for j in range(i + 1, b):
            _, block_cups = cap_cup_subsets(points, blocks[j + 1], orient)
            middle_blocks = blocks[i + 2 : j + 1]
            for cap, cup in product(block_caps, block_cups):
                for middle in product(*middle_blocks):
                    target = tuple((*cap, *middle, *cup))
                    assert hull(points, target) == set(target)
                    all_interval_faces.add(frozenset(target))
    transported = cap_counts[0]
    forward = 0
    for j in range(1, b):
        forward += transported * cup_counts[j]
        transported = cap_counts[j] + m * transported
    assert len(all_interval_faces) == forward

    # The rank-r pair-pair slice is the count isolated in the product report.
    pair_pair = {
        frozenset((*left, *middle, *right))
        for left in combinations(blocks[1], 2)
        for right in combinations(blocks[-2], 2)
        for middle in product(*blocks[2:-2])
    }
    expected_pair_pair = math.comb(m, 2) ** 2 * m ** (r - 4)
    assert len(pair_pair) == expected_pair_pair
    assert pair_pair <= two_ended

    # A two-ended interval target cannot in general retain even a common
    # suffix coordinate.  Once a later block is occupied, the two-point cup
    # at the old right endpoint becomes an intermediate two-point block and
    # one of its points is hidden.
    left_pair = tuple(blocks[1][:2])
    right_pair = tuple(blocks[2][:2])
    common_suffix = blocks[3][0]
    interval_target = (*left_pair, *right_pair)
    retained_suffix_target = (*interval_target, common_suffix)
    assert hull(points, interval_target) == set(interval_target)
    retained_suffix_hull = hull(points, retained_suffix_target)
    assert retained_suffix_hull != set(retained_suffix_target)

    # Exact simultaneous-repair theorem on a regression family.  Fix the
    # top micro-point in every other internal block.  Sources use any of the
    # other m-1 points in those blocks.  Their violated edge windows are
    # pairwise disjoint, so every chosen blocker is extreme simultaneously.
    repaired_blocks = tuple(range(1, b + 1, 2))
    free_blocks = tuple(i for i in range(1, b + 1) if i not in repaired_blocks)
    fixed_free_choice = {i: blocks[i][0] for i in free_blocks}
    common_target = None
    fibre = 0
    window_records = []
    for repaired_choices in product(*(blocks[i][:-1] for i in repaired_blocks)):
        choice_by_block = dict(fixed_free_choice)
        choice_by_block.update(dict(zip(repaired_blocks, repaired_choices)))
        source = [blocks[0][0]] + [choice_by_block[i] for i in range(1, b + 1)] + [blocks[-1][0]]
        polygon = hull_order(points, source, orient)
        assert set(polygon) == set(source)
        blockers = [blocks[i][-1] for i in repaired_blocks]
        windows = [violated_edges(points, polygon, p, orient) for p in blockers]
        assert all(windows)
        assert all(windows[i].isdisjoint(windows[j]) for i, j in combinations(range(len(windows)), 2))
        simultaneous = hull(points, source + blockers)
        assert set(blockers) <= simultaneous
        expected_target = (set(source) - set(repaired_choices)) | set(blockers)
        assert simultaneous == expected_target
        if common_target is None:
            common_target = frozenset(simultaneous)
            window_records = [sorted(window) for window in windows]
        else:
            assert frozenset(simultaneous) == common_target
        fibre += 1
    expected_fibre = (m - 1) ** len(repaired_blocks)
    assert fibre == expected_fibre

    # Check every sub-batch too: disjoint windows make all selected labels
    # survive as vertices, hence the blocker subsets give distinct targets
    # for each fixed source.
    source = [blocks[0][0]] + [blocks[i][0] for i in range(1, b + 1)] + [blocks[-1][0]]
    blockers = [blocks[i][-1] for i in repaired_blocks]
    batch_targets = set()
    for mask in range(1 << len(blockers)):
        chosen = [blockers[j] for j in range(len(blockers)) if mask >> j & 1]
        target = frozenset(hull(points, source + chosen))
        assert set(chosen) <= target
        batch_targets.add(target)
    assert len(batch_targets) == 2 ** len(blockers)

    return {
        "r": r,
        "M": m,
        "n": len(points),
        "epsilon": str(epsilon),
        "cloud_delta": str(delta),
        "internal_blocks": b,
        "micro_cap_count": len(caps),
        "micro_cup_count": len(cups),
        "full_two_ended_faces": len(two_ended),
        "full_two_ended_formula": f"{len(caps)}*{len(cups)}*{m}^{b-2}",
        "all_interval_forward_faces": len(all_interval_faces),
        "forward_scan_final_transport": transported,
        "rank_r_pair_pair_faces": len(pair_pair),
        "rank_r_pair_pair_formula": f"binom({m},2)^2*{m}^{r-4}",
        "suffix_retention_regression": {
            "interval_target": list(interval_target),
            "common_suffix_point": common_suffix,
            "extended_point_count": len(retained_suffix_target),
            "extended_hull": sorted(retained_suffix_hull),
            "hidden_points": sorted(set(retained_suffix_target) - retained_suffix_hull),
        },
        "simultaneous_repair_blocks": list(repaired_blocks),
        "disjoint_violated_edge_windows": window_records,
        "fixed_source_boolean_targets": len(batch_targets),
        "one_target_inverse_fibre": fibre,
        "one_target_inverse_fibre_formula": f"({m}-1)^{len(repaired_blocks)}",
    }


def scalable_capped_rows():
    """Audit the two-regime capped-Hall arithmetic for M=2^r.

    In the cloud regime, ``quarter_margin`` is the margin obtained from the
    main term (log T)^2/4 of the established universal lower bound.  It is
    quadratic in r, so its subtraction of the known o((log T)^2) error is
    asymptotically harmless.
    """
    rows = []
    for r in (16, 24, 32, 48, 64):
        m = 1 << r
        source_count = m ** (r - 2)
        pair_faces = math.comb(m, 2) ** 2 * m ** (r - 4)
        direct_threshold = m**3 // 64
        for label, t_cloud in (
            ("small", m),
            ("direct_edge", direct_threshold),
            ("cloud_edge", direct_threshold + 1),
            ("large", m**4),
        ):
            n = (r - 2) * m + 2 + t_cloud
            ell = (n - 1).bit_length()
            demand = 1 << (ell - r)
            direct_ratio_num = pair_faces
            direct_ratio_den = demand * source_count
            direct_pays = direct_ratio_num >= direct_ratio_den
            t_log = math.log2(t_cloud)
            demand_log_upper = (r - 2) * r + math.log2(demand)
            quarter_margin = t_log * t_log / 4 - demand_log_upper
            if t_cloud <= direct_threshold:
                assert direct_pays
            else:
                # A uniform quadratic margin swallows the known lower-order
                # Erdos--Szekeres error in the cloud lower bound.
                assert quarter_margin > r * r / 2
            rows.append(
                {
                    "r": r,
                    "regime": label,
                    "log2_M": r,
                    "log2_T": t_log,
                    "ell": ell,
                    "g": ell - r,
                    "log2_D": ell - r,
                    "direct_pair_pool_pays": direct_pays,
                    "log2_direct_pool_over_capped_demand": (
                        math.log2(direct_ratio_num) - math.log2(direct_ratio_den)
                    ),
                    "cloud_quarter_main_term_margin": quarter_margin,
                }
            )
    return rows


def main():
    finite = exact_product_cell_audit()
    rows = scalable_capped_rows()
    result = {
        "schema": "erdos838-two-ended-capped-hall-v1",
        "finite_exact_geometry": finite,
        "scalable_capped_hall": rows,
        "verdict": (
            "Disjoint tangent windows admit exact simultaneous replacement, but their "
            "target fibres can be exponential.  The complete product obstruction is "
            "nevertheless discharged at capped Hall scale: two-ended faces handle "
            "T<=M^3/64 and the blocker cloud lower bound handles T>M^3/64."
        ),
    }
    path = HERE / "certificate.json"
    path.write_text(json.dumps(result, indent=2) + "\n")
    print("two-ended capped Hall audit: PASS")
    print("wrote", path)
    print(
        "finite",
        f"n={finite['n']}",
        f"two-ended={finite['full_two_ended_faces']}",
        f"fibre={finite['one_target_inverse_fibre']}",
    )
    for row in rows:
        if row["regime"] in ("direct_edge", "cloud_edge"):
            print(
                "scale",
                f"r={row['r']}",
                row["regime"],
                f"direct-log-margin={row['log2_direct_pool_over_capped_demand']:.3f}",
                f"cloud-quarter-margin={row['cloud_quarter_main_term_margin']:.3f}",
            )


if __name__ == "__main__":
    main()
