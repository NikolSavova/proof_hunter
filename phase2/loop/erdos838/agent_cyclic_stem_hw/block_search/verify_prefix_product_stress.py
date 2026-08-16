#!/usr/bin/env python3
"""Exact stress tests for the prefix-product tail condition PT_(b,s).

Families:

* the parabolic arbitrarily deep nested-prefix pocket;
* exact rational common-apex product grids;
* the 17/65/129 dyadic-boundary examples;
* homogeneous vertical iteration of the 17-point example; and
* the exact pair tower above the 129-point resonance.

Every profile coefficient and every integer slack is exact.  Logarithms are
used only to report the finer real-valued slack.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
STEM = HERE.parent
ERDOS838 = STEM.parent
sys.path[:0] = [
    str(HERE),
    str(STEM),
    str(ERDOS838 / "agent_graded_supersat"),
    str(ERDOS838 / "agent_apa_rank"),
]

import verify_block_resonance as resonance  # noqa: E402
import verify_block_window as window  # noqa: E402
from amplification_probe import cap_cup_profiles  # noqa: E402
from graded_balanced import vertical_iterate  # noqa: E402
from verify_apa_counterexample import matrix_profile  # noqa: E402


OUTPUT = HERE / "prefix_product_stress_certificate.json"


def prefixes(profile: list[int] | tuple[int, ...]) -> list[int]:
    return list(itertools.accumulate(profile))


def comparison_holds(numerator: int, denominator: int, exponent: int) -> bool:
    """Return numerator/denominator >= 2^exponent exactly."""
    if exponent >= 0:
        return numerator >= (1 << exponent) * denominator
    return (1 << (-exponent)) * numerator >= denominator


def pt_slack(profile: list[int] | tuple[int, ...], block: int) -> dict[str, object]:
    """Smallest integer and real slack in PT_(block,s)."""
    n = profile[1]
    ell = (n - 1).bit_length()
    cumulative = prefixes(profile)
    numerator_rank = ell - block
    if numerator_rank < 0:
        return {
            "block": block,
            "integer_slack": 0,
            "real_slack": 0.0,
            "worst_q": 0,
            "tests": [],
        }
    numerator = cumulative[numerator_rank]
    tests = []
    real_slack = 0.0
    worst_q = 0
    for q in range(0, ell // block + 2):
        denominator_rank = ell - (q + 1) * block
        if denominator_rank < 0:
            break
        denominator = cumulative[denominator_rank]
        deficit = q - (math.log2(numerator) - math.log2(denominator))
        tests.append(
            {
                "q": q,
                "numerator_rank": numerator_rank,
                "denominator_rank": denominator_rank,
                "numerator": numerator,
                "denominator": denominator,
                "real_deficit": deficit,
            }
        )
        if deficit > real_slack:
            real_slack, worst_q = deficit, q
    integer_slack = 0
    while any(
        not comparison_holds(
            row["numerator"], row["denominator"], row["q"] - integer_slack
        )
        for row in tests
    ):
        integer_slack += 1
    return {
        "block": block,
        "integer_slack": integer_slack,
        "real_slack": max(0.0, real_slack),
        "worst_q": worst_q,
        "tests": tests,
    }


def profile_record(name: str, profile: list[int] | tuple[int, ...], metadata=None):
    n = profile[1]
    ell = (n - 1).bit_length()
    # PT only uses F_(ell-b), so b>=1 requires coefficients through ell-1.
    if len(profile) < ell:
        raise AssertionError((name, "profile does not reach ell", len(profile), ell))
    blocks = [pt_slack(profile, block) for block in range(1, ell + 1)]
    best = min(blocks, key=lambda row: ((row["integer_slack"] + 3) * row["block"], row["block"]))
    positive = [row for row in blocks if row["integer_slack"]]
    return {
        "name": name,
        "n": n,
        "ell": ell,
        "profile_through_ell": list(profile[: ell + 1]),
        "metadata": metadata or {},
        "block_slacks": [
            {
                "block": row["block"],
                "integer_slack": row["integer_slack"],
                "real_slack": row["real_slack"],
                "worst_q": row["worst_q"],
            }
            for row in blocks
        ],
        "maximum_integer_slack": max(row["integer_slack"] for row in blocks),
        "best_PT_cost_(s+3)b": (best["integer_slack"] + 3) * best["block"],
        "best_block": best["block"],
        "positive_slack_blocks": [row["block"] for row in positive],
    }


def nested_prefix_points(depth: int) -> tuple[tuple[int, int], ...]:
    scale = 2 * depth + 4
    u = (0, 0)
    c = (scale, 0)
    prefix = tuple((j, j * (j - scale)) for j in range(1, depth + 1))
    inner = (scale // 2, 1)
    outer = (scale // 2, scale * scale)
    return (u, c, *prefix, inner, outer)


def nested_prefix_rows() -> list[dict[str, object]]:
    rows = []
    for depth in (1, 2, 4, 8, 16, 32, 64, 128, 256):
        points = nested_prefix_points(depth)
        ell = (len(points) - 1).bit_length()
        profile = resonance.truncated_profile(points, ell)
        rows.append(profile_record(f"nested_prefix_d{depth}", profile, {"depth": depth}))
    return rows


def load_product_module():
    path = ERDOS838 / "agent_entropy_spread" / "verify_product_blocker.py"
    spec = importlib.util.spec_from_file_location("pt_product_blocker", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def integralize(points: list[tuple[Fraction, Fraction]]) -> tuple[tuple[int, int], ...]:
    scale = max(coordinate.denominator for point in points for coordinate in point)
    if any(scale % coordinate.denominator for point in points for coordinate in point):
        raise AssertionError("product-grid denominators are not nested powers")
    return tuple((int(x * scale), int(y * scale)) for x, y in points)


def poly_multiply(left: list[int], right: list[int], cutoff: int) -> list[int]:
    result = [0] * (cutoff + 1)
    for i, a in enumerate(left[: cutoff + 1]):
        if not a:
            continue
        for j, b in enumerate(right[: cutoff + 1 - i]):
            if b:
                result[i + j] += a * b
    return result


def weighted_path_matrix(
    block_sizes: list[int], roots, cutoff: int
) -> list[list[list[int]]]:
    """Increasing-x paths, weighted at every arrival vertex.

    A path from i to j receives z per edge and the product of the block
    populations of every vertex other than i.  Removing the final factor
    m_j z leaves exactly the populations of its internal macro vertices.
    """
    blocks = len(block_sizes)
    matrix = [[[0] * (cutoff + 2) for _ in range(blocks)] for _ in range(blocks)]
    for label in range(blocks):
        matrix[label][label][0] = 1
    for i, j in roots:
        weight = block_sizes[j]
        for column in range(blocks):
            source = matrix[i][column]
            target = matrix[j][column]
            for degree in range(1, cutoff + 2):
                target[degree] += weight * source[degree - 1]
    return matrix


def product_grid_symbolic_profile(rank: int, cell_size: int, cutoff: int) -> list[int]:
    """Exact nonuniform vertical-composition profile for a product grid."""
    last = rank - 1
    shear = 2 * rank
    macro = [(-1, rank * rank - shear)] + [
        (i, i * (last - i) + shear * i) for i in range(rank)
    ]
    # x-order is cloud, left singleton, r-2 internal M-cells, right singleton.
    block_sizes = [cell_size, 1] + [cell_size] * (rank - 2) + [1]
    if len(macro) != len(block_sizes):
        raise AssertionError("bad product macro")
    roots = resonance.slope_roots(tuple(macro))
    cups = weighted_path_matrix(block_sizes, roots, cutoff)
    caps = weighted_path_matrix(block_sizes, reversed(roots), cutoff)

    micro_caps = []
    micro_cups = []
    micro_convex = []
    for population in block_sizes:
        cap = [0] * (cutoff + 1)
        cup = [0] * (cutoff + 1)
        cap[1] = cup[1] = population
        if cutoff >= 2:
            cap[2] = cup[2] = math.comb(population, 2)
        for degree in range(3, min(population, cutoff) + 1):
            cup[degree] = math.comb(population, degree)
        micro_caps.append(cap)
        micro_cups.append(cup)
        micro_convex.append(
            [0]
            + [math.comb(population, degree) for degree in range(1, min(population, cutoff) + 1)]
            + [0] * max(0, cutoff - population)
        )

    profile = [0] * (cutoff + 1)
    profile[0] = 1
    for polynomial in micro_convex:
        for degree, value in enumerate(polynomial[: cutoff + 1]):
            profile[degree] += value
    blocks = len(block_sizes)
    for left in range(blocks):
        for right in range(left + 1, blocks):
            # Strip z*m_right from each endpoint path.  Degree e becomes
            # e-1, and the remaining coefficient is the internal population
            # product.
            upper = [
                cups[right][left][edges] // block_sizes[right]
                for edges in range(1, cutoff + 2)
            ]
            lower = [
                caps[right][left][edges] // block_sizes[right]
                for edges in range(1, cutoff + 2)
            ]
            if any(
                cups[right][left][edges] % block_sizes[right]
                or caps[right][left][edges] % block_sizes[right]
                for edges in range(1, cutoff + 2)
            ):
                raise AssertionError("nonintegral endpoint stripping")
            # In the almost-vertical convention, the left endpoint carries
            # the negative cap microchain and the right endpoint the positive
            # cup microchain.
            contribution = poly_multiply(micro_caps[left], micro_cups[right], cutoff)
            contribution = poly_multiply(contribution, upper, cutoff)
            contribution = poly_multiply(contribution, lower, cutoff)
            for degree, value in enumerate(contribution):
                profile[degree] += value
    return profile


def thin_product_points(rank: int, cell_size: int) -> tuple[tuple[int, int], ...]:
    """A canonical sufficiently thin rational realization of the grid."""
    last = rank - 1
    shear = 2 * rank
    macro = [
        (Fraction(i), Fraction(i * (last - i) + shear * i))
        for i in range(rank)
    ]
    apex = (Fraction(-1), Fraction(rank * rank - shear))
    exponent = 12 + 2 * (rank + cell_size).bit_length()
    epsilon = Fraction(1, 2**exponent)
    delta = Fraction(1, 2 ** (2 * exponent))
    points = []
    for block, (x, y) in enumerate(macro):
        population = 1 if block in (0, last) else cell_size
        for micro in range(population):
            points.append(
                (x + epsilon * epsilon * micro, y + epsilon * micro * micro)
            )
    for micro in range(cell_size):
        points.append(
            (
                apex[0] + delta * delta * micro,
                apex[1] + delta * micro * micro,
            )
        )
    return integralize(points)


def product_grid_rows() -> list[dict[str, object]]:
    parameters = (
        (4, 2), (4, 4), (4, 8), (4, 16),
        (6, 2), (6, 4), (6, 8), (6, 16),
        (8, 2), (8, 4), (8, 8), (8, 12),
        (12, 2), (12, 4), (12, 8),
        (16, 2), (16, 4), (24, 3), (32, 2), (48, 2), (64, 2),
    )
    rows = []
    for rank, cell_size in parameters:
        points = thin_product_points(rank, cell_size)
        ell = (len(points) - 1).bit_length()
        profile = resonance.truncated_profile(points, ell)
        symbolic = product_grid_symbolic_profile(rank, cell_size, ell)
        if tuple(symbolic) != tuple(profile):
            raise AssertionError(
                ("product symbolic mismatch", rank, cell_size, symbolic, profile)
            )
        rows.append(
            profile_record(
                f"product_grid_r{rank}_m{cell_size}",
                profile,
                {
                    "rank_parameter": rank,
                    "cell_size": cell_size,
                    "realization": "canonical dyadic thin product",
                },
            )
        )
    return rows


def scalable_product_grid_rows() -> list[dict[str, object]]:
    rows = []
    for rank in (8, 12, 16, 24, 32, 48, 64):
        cell_size = 1 << rank
        n = (rank - 1) * cell_size + 2
        ell = (n - 1).bit_length()
        profile = product_grid_symbolic_profile(rank, cell_size, ell)
        if profile[1] != n:
            raise AssertionError((rank, profile[1], n))
        rows.append(
            profile_record(
                f"scalable_product_grid_r{rank}_M2pow{rank}",
                profile,
                {"rank_parameter": rank, "cell_size": str(cell_size)},
            )
        )
    return rows


def dyadic_rows() -> list[dict[str, object]]:
    rows = [profile_record("dyadic_kill_n17", window.BLOCK_KILL_PROFILE)]
    source = json.loads((HERE / "block_resonance_certificate.json").read_text())
    rows.extend(profile_record(row["name"], row["profile"]) for row in source["cases"])
    rows.extend(
        profile_record(
            f"pair_tower_depth{row['pair_depth']}",
            row["profile_through_ell"],
            {"pair_depth": row["pair_depth"]},
        )
        for row in source["homogeneous_pair_tower_from_n129"]
    )
    return rows


def vertical_kill_rows(maximum_depth: int = 12) -> list[dict[str, object]]:
    points = tuple((index, value) for index, value in enumerate(window.BLOCK_KILL_Y))
    profile = list(matrix_profile(points))
    caps, cups = cap_cup_profiles(points)
    template = (len(points), list(caps), list(cups), [0] + profile[1:])
    rows = []
    for depth in range(1, maximum_depth + 1):
        ell = math.ceil(depth * math.log2(len(points)))
        _n, _caps, _cups, convex = vertical_iterate(template, depth, ell)
        rows.append(
            profile_record(
                f"vertical_n17_depth{depth}",
                [1] + convex[1 : ell + 1],
                {"depth": depth},
            )
        )
    return rows


def family_summary(rows: list[dict[str, object]]) -> dict[str, object]:
    record = max(rows, key=lambda row: (row["maximum_integer_slack"], row["ell"]))
    normalized = max(
        rows,
        key=lambda row: row["maximum_integer_slack"] / max(1.0, math.log2(row["ell"])),
    )
    return {
        "cases": len(rows),
        "maximum_integer_slack": record["maximum_integer_slack"],
        "maximum_slack_witness": record["name"],
        "maximum_s_over_log2_ell": normalized["maximum_integer_slack"]
        / max(1.0, math.log2(normalized["ell"])),
        "normalized_witness": normalized["name"],
        "maximum_best_PT_cost": max(row["best_PT_cost_(s+3)b"] for row in rows),
    }


def main() -> None:
    families = {
        "nested_prefix": nested_prefix_rows(),
        "product_grid": product_grid_rows(),
        "scalable_product_grid": scalable_product_grid_rows(),
        "dyadic_resonance_and_pair_tower": dyadic_rows(),
        "vertical_iteration_n17": vertical_kill_rows(),
    }
    output = {
        "description": "exact PT_(b,s) slack stress on nested/product/dyadic families",
        "definition": (
            "minimal s>=0 with F_(ell-b)/F_(ell-(q+1)b)>=2^(q-s) for every q"
        ),
        "families": families,
        "summaries": {name: family_summary(rows) for name, rows in families.items()},
    }
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print("prefix-product stress: PASS")
    for name, summary in output["summaries"].items():
        print(name, summary)


if __name__ == "__main__":
    main()
