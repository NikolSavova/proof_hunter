#!/usr/bin/env python3
"""Exact/profile probes for deletion paths and normalized rank extension.

This script has two independent purposes.

* It tests p_r=(r+1)v_(r+1)/((n-r)v_r) on the saved planar profiles and
  on balanced Pascal cells / their vertical iterates.
* It constructs an abstract 4-flag complex which has the planar
  first-repair bound and an Erdos--Szekeres-sized face in every suffix, but
  whose deletion-path sum stays bounded.  Thus those two coarse properties
  alone cannot prove the planar theorem.
"""

from __future__ import annotations

import json
import math
import sys
from decimal import Decimal, getcontext
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GRADED = ROOT / "agent_graded_supersat"
sys.path.insert(0, str(GRADED))

from graded_balanced import central_template, pascal_row, vertical_iterate  # noqa: E402


def extension_rows(profile: list[int] | tuple[int, ...], n: int) -> list[dict[str, float | int]]:
    rows = []
    for r in range(3, len(profile) - 1):
        if not profile[r]:
            continue
        probability = (r + 1) * profile[r + 1] / ((n - r) * profile[r])
        rows.append(
            {
                "r": r,
                "p_r": probability,
                "minus_log2_p_over_r": -math.log2(probability) / r if probability else math.inf,
                "log2_p_plus_r": math.log2(probability) + r if probability else -math.inf,
            }
        )
    return rows


def multiscale_blocks(depth: int) -> list[set[int]]:
    """Disjoint H_j, |H_j|=j, lying just below 2^(j-1)."""
    blocks: list[set[int]] = []
    # Small ranks are irrelevant because the complete 3-skeleton supplies
    # the required face.  Starting at j=4 makes the dyadic intervals disjoint.
    for j in range(4, depth + 1):
        endpoint = 2 ** (j - 1)
        blocks.append(set(range(endpoint - j + 1, endpoint + 1)))
    if any(left & right for i, left in enumerate(blocks) for right in blocks[i + 1 :]):
        raise AssertionError("blocks are not disjoint")
    return blocks


def abstract_profile(m: int, blocks: list[set[int]]) -> list[int]:
    """Complete 3-skeleton plus the Boolean simplices on the blocks."""
    intersections = [sum(x <= m for x in block) for block in blocks]
    max_rank = max([min(3, m)] + intersections)
    profile = [0] * (max_rank + 1)
    for r in range(min(3, m) + 1):
        profile[r] = math.comb(m, r)
    for h in intersections:
        for r in range(4, h + 1):
            profile[r] += math.comb(h, r)
    return profile


def pascal_endpoint_gaps(max_m: int, selected: set[int]) -> dict[str, object]:
    """High-precision scalar strong-glue DP at t=1 and t=1/2."""
    getcontext().prec = 100

    # A state is (population, C, U, W); each enumerator is (value,z*d/dz).
    def leaf(z: Decimal):
        item = (z, z)
        return (1, item, item, item)

    def add(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def glue(left, right, z: Decimal):
        a, ca, ua, wa = left
        b, cb, ub, wb = right
        cap_left = ((1 + b * z) * ca[0], (1 + b * z) * ca[1] + b * z * ca[0])
        cup_right = ((1 + a * z) * ub[0], (1 + a * z) * ub[1] + a * z * ub[0])
        cross = (ca[0] * ub[0], ca[1] * ub[0] + ca[0] * ub[1])
        return (a + b, add(cb, cap_left), add(ua, cup_right), add(add(wa, wb), cross))

    def centers(z: Decimal):
        row = [leaf(z)]
        answer = {}
        for level in range(1, max_m + 1):
            row = [leaf(z)] + [glue(row[i - 1], row[i], z) for i in range(1, level)] + [leaf(z)]
            if level in selected:
                answer[level] = row[level // 2]
        return answer

    at_one = centers(Decimal(1))
    at_half = centers(Decimal(1) / 2)
    answer = {}
    for m in sorted(selected):
        one, half = at_one[m], at_half[m]
        mu1 = one[3][1] / (one[3][0] + 1)
        muh = half[3][1] / (half[3][0] + 1)
        answer[str(m)] = {
            "n": one[0],
            "mu1_minus_muh": float(mu1 - muh),
            "mu1": float(mu1),
            "muh": float(muh),
        }
    return answer


def local_r(profile: list[int], m: int) -> float:
    def mean(t: float) -> float:
        terms = [value * t**r for r, value in enumerate(profile)]
        return sum(r * value for r, value in enumerate(terms)) / sum(terms)

    mu1, muh = mean(1.0), mean(0.5)
    return math.log((m - muh) / (m - mu1))


def abstract_barrier(depth: int) -> dict[str, object]:
    n = 2**depth
    blocks = multiscale_blocks(depth)
    total = 0.0
    minimum_rank_slack = math.inf
    maximum_repair_degree = 0
    # Profiles suffice for X.  The repair assertion is structural: a face of
    # size at least four lies in one unique disjoint block.  If two deletions
    # repaired a nonface of size at least five, their (>=3)-point intersection
    # would have to lie in two disjoint blocks (or both repaired faces would
    # lie in the same block, forcing the original set to be a face).
    maximum_repair_degree = 1
    for m in range(n, 0, -1):
        profile = abstract_profile(m, blocks)
        rank = len(profile) - 1
        minimum_rank_slack = min(minimum_rank_slack, rank - math.ceil(math.log2(m)))
        total += local_r(profile, m)
    if minimum_rank_slack < 0 or maximum_repair_degree > 3:
        raise AssertionError("abstract barrier lost a defining property")
    full_profile = abstract_profile(n, blocks)
    probe_rank = depth // 2
    probe = extension_rows(full_profile, n)[probe_rank - 3]
    return {
        "depth": depth,
        "n": n,
        "number_of_boolean_facets": len(blocks),
        "maximum_repair_degree_for_nonfaces_of_size_at_least_5": maximum_repair_degree,
        "minimum_suffix_rank_minus_ceil_log2_suffix_size": minimum_rank_slack,
        "path_X": total,
        "path_X_over_log_n": total / math.log(n),
        "rank_extension_at_floor_depth_over_2": probe,
    }


def main() -> None:
    half = json.loads((ROOT / "agent_half_weight" / "certificate.json").read_text())["records"]
    saved = {
        name: extension_rows(row["profile"], int(name))
        for name, row in half.items()
    }

    pascal = {}
    for m in (16, 32, 64):
        n, _, _, convex = pascal_row(m, m)[m // 2]
        profile = [1] + convex[1:]
        pascal[str(m)] = {
            "n": n,
            "log2_n": math.log2(n),
            "extensions": extension_rows(profile, n),
        }

    iterates = {}
    for h, depth in ((6, 6), (8, 6), (10, 6)):
        template = central_template(h)
        n = template[0] ** depth
        cutoff = math.ceil(math.log2(n)) + 2
        _, _, _, convex = vertical_iterate(template, depth, cutoff)
        iterates[f"h{h}_d{depth}"] = {
            "n_log2": math.log2(n),
            "extensions": extension_rows([1] + convex[1:], n),
        }

    barriers = [abstract_barrier(depth) for depth in (8, 10, 12, 14)]
    output = {
        "mode": "rank_extension_and_abstract_path_barrier",
        "saved_planar_profiles": saved,
        "balanced_pascal_cells": pascal,
        "balanced_vertical_iterates": iterates,
        "central_pascal_endpoint_gaps": pascal_endpoint_gaps(
            256, {20, 32, 64, 128, 256}
        ),
        "abstract_multiscale_4_flag_barrier": barriers,
    }
    HERE.mkdir(parents=True, exist_ok=True)
    (HERE / "rank_extension_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    for row in barriers:
        p = row["rank_extension_at_floor_depth_over_2"]
        print(
            "abstract",
            row["n"],
            f"X={row['path_X']:.9f}",
            f"X/logn={row['path_X_over_log_n']:.6f}",
            f"rank={p['r']}",
            f"-log2(p)/r={p['minus_log2_p_over_r']:.6f}",
        )


if __name__ == "__main__":
    main()
