#!/usr/bin/env python3
"""Exact checks for the Gordon cyclic-stem / random-hull bridge.

The combinatorial claims use integer or rational arithmetic.  The displayed
entropy and quadratic-potential drifts use ordinary logarithms only after all
profiles and deletion counts have been reconstructed exactly; their asserted
negative margins are much larger than floating-point error.
"""

from __future__ import annotations

import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LATTICE = ROOT / "agent_planar_lattice_mean"
MEAN = ROOT / "agent_mean_lattice"
APA = ROOT / "agent_apa_rank"
LEX = ROOT / "agent_lex_minimizer_search"
for directory in (LATTICE, MEAN, APA):
    sys.path.insert(0, str(directory))

from mean_lattice_attack import pascal_cells  # noqa: E402
from planar_lattice_mean import (  # noqa: E402
    closure_mask,
    convex_hull,
    is_convex,
    orient,
)
from verify_apa_counterexample import matrix_profile  # noqa: E402
from verify_half_weight_counterexample import (  # noqa: E402
    EXPECTED_PROFILE as PROFILE_58,
    points as points_58,
)


def points_9() -> tuple[tuple[int, int], ...]:
    record = json.loads((LEX / "exact_realizable_n9.json").read_text())
    return tuple(sorted(tuple(point) for point in record["coordinates_as_stored"]))


def halfplane_cells(points, x: int) -> set[frozenset[int]]:
    """All open-halfplane traces whose boundary passes through x.

    At a boundary event through x and y, the two adjacent cells are the
    strict positive orientation side, with y either absent or present.  The
    negative side supplies the other two directed cells.  This enumerates the
    circular sweep without numerical angles.
    """
    cells: set[frozenset[int]] = set()
    for y in range(len(points)):
        if y == x:
            continue
        positive = frozenset(
            z for z in range(len(points))
            if z not in (x, y) and orient(points[x], points[y], points[z]) > 0
        )
        negative = frozenset(
            z for z in range(len(points))
            if z not in (x, y) and orient(points[x], points[y], points[z]) < 0
        )
        cells.update((positive, positive | {y}, negative, negative | {y}))
    return cells


def cyclic_stems(points, x: int) -> list[frozenset[int]]:
    """Minimal halfplane feasible sets, ordered by Gordon adjacency."""
    cells = halfplane_cells(points, x)
    stems = [cell for cell in cells if not any(other < cell for other in cells)]
    universe = frozenset(range(len(points))) - {x}
    stem_set = set(stems)
    neighbours = {
        stem: {
            other for other in stems if other != stem
            and universe - (stem | other) in stem_set
        }
        for stem in stems
    }
    if any(len(values) != 2 for values in neighbours.values()):
        raise AssertionError((x, neighbours))
    first = min(stems, key=lambda value: (len(value), sorted(value)))
    order = [first]
    previous = None
    current = first
    while len(order) < len(stems):
        choices = neighbours[current] - ({previous} if previous is not None else set())
        if len(order) == 1:
            nxt = min(choices, key=lambda value: (len(value), sorted(value)))
        else:
            if len(choices) != 1:
                raise AssertionError("stem adjacency is not a cycle")
            nxt = next(iter(choices))
        if nxt in order:
            raise AssertionError("stem cycle closed too early")
        order.append(nxt)
        previous, current = current, nxt
    if order[0] not in neighbours[order[-1]]:
        raise AssertionError("stem cycle did not close")
    return order


def n9_cyclic_bridge() -> dict[str, object]:
    points = points_9()
    n = len(points)
    hull = frozenset(convex_hull(points, range(n)))
    if len(hull) != 3:
        raise AssertionError(hull)

    stem_rows = []
    er_half = Fraction(len(hull), 2)
    for x in range(n):
        if x in hull:
            continue
        stems = cyclic_stems(points, x)
        universe = frozenset(range(n)) - {x}
        k = len(stems)
        for index, stem in enumerate(stems):
            complement = universe - (stem | stems[(index + 1) % k])
            if complement not in stems:
                raise AssertionError("Gordon complement relation failed")

        union_by_cycle = (
            sum((Fraction(1, 2 ** len(stem)) for stem in stems), Fraction())
            - sum(
                (
                    Fraction(1, 2 ** len(stems[i] | stems[(i + 1) % k]))
                    for i in range(k)
                ),
                Fraction(),
            )
            + Fraction(1, 2 ** (n - 1))
        )
        union_by_complements = (
            sum((Fraction(1, 2 ** len(stem)) for stem in stems), Fraction())
            - sum(
                (Fraction(1, 2 ** (n - 1 - len(stem))) for stem in stems),
                Fraction(),
            )
            + Fraction(1, 2 ** (n - 1))
        )
        brute_count = 0
        labels = sorted(universe)
        for mask in range(1 << (n - 1)):
            chosen = {labels[i] for i in range(n - 1) if (mask >> i) & 1}
            brute_count += any(stem <= chosen for stem in stems)
        union_brute = Fraction(brute_count, 2 ** (n - 1))
        if union_by_cycle != union_by_complements or union_by_cycle != union_brute:
            raise AssertionError((x, union_by_cycle, union_by_complements, union_brute))
        er_half += union_brute / 2
        stem_rows.append(
            {
                "point": x,
                "cyclic_stems": [sorted(stem) for stem in stems],
                "stem_sizes": [len(stem) for stem in stems],
                "conditional_exposure_probability_given_x_absent": str(union_brute),
                "probability_outside_random_half_hull": str(union_brute / 2),
                "probability_point_matters": str(union_brute / 2),
            }
        )

    profile = [0] * (n + 1)
    weighted_omitted_numerator = 0
    weighted_exp_omitted_numerator = 0
    uniform_omitted_numerator = 0
    uniform_interior_numerator = 0
    faces: list[tuple[int, int]] = []
    for mask in range(1 << n):
        face = [i for i in range(n) if (mask >> i) & 1]
        if not is_convex(points, face):
            continue
        closed = closure_mask(points, face)
        h = len(face)
        interior = closed.bit_count() - h
        omitted = n - closed.bit_count()
        profile[h] += 1
        faces.append((mask, h))
        uniform_omitted_numerator += omitted
        uniform_interior_numerator += interior
        weighted_omitted_numerator += (1 << interior) * omitted
        weighted_exp_omitted_numerator += (1 << interior) * (1 << omitted)

    expected_profile = [1, 9, 36, 84, 36, 3, 0, 0, 0, 0]
    if profile != expected_profile:
        raise AssertionError(profile)
    v = sum(profile)
    first_moment = sum(rank * count for rank, count in enumerate(profile))
    z_half = sum(
        (Fraction(count, 2 ** rank) for rank, count in enumerate(profile)),
        Fraction(),
    )
    weighted_omitted = Fraction(weighted_omitted_numerator, 2 ** n)
    weighted_exp_omitted = Fraction(weighted_exp_omitted_numerator, 2 ** n)
    if er_half != weighted_omitted or weighted_exp_omitted != z_half:
        raise AssertionError((er_half, weighted_omitted, weighted_exp_omitted, z_half))

    return {
        "n": n,
        "hull": sorted(hull),
        "profile": profile,
        "V": v,
        "mu_uniform": str(Fraction(first_moment, v)),
        "mean_omitted_uniform": str(Fraction(uniform_omitted_numerator, v)),
        "mean_interior_uniform": str(Fraction(uniform_interior_numerator, v)),
        "mean_omitted_interior_weighted": str(weighted_omitted),
        "Gordon_er_half": str(er_half),
        "exp_omitted_interior_weighted": str(weighted_exp_omitted),
        "Z_half": str(z_half),
        "stems": stem_rows,
        "faces": faces,
    }


def block_qms_drift_n9(bridge: dict[str, object]) -> list[dict[str, object]]:
    """Direct block-deletion audit of the sharp quadratic potential."""
    n = int(bridge["n"])
    size = 1 << n
    values = [0] * size
    moments = [0] * size
    for mask, rank in bridge["faces"]:
        values[mask] = 1
        moments[mask] = rank
    for bit in range(n):
        for mask in range(size):
            if (mask >> bit) & 1:
                values[mask] += values[mask ^ (1 << bit)]
                moments[mask] += moments[mask ^ (1 << bit)]

    full_v = values[-1]
    full_mu = moments[-1] / full_v
    full_log = math.log2(full_v)
    rows = []
    for m in range(1, n):
        children = [mask for mask in range(size) if mask.bit_count() == m]
        normalizer = sum(values[mask] for mask in children)
        expected_log = sum(
            values[mask] * math.log2(values[mask]) for mask in children
        ) / normalizer
        expected_mu = sum(moments[mask] for mask in children) / normalizer
        expected_mu2 = sum(
            values[mask] * (moments[mask] / values[mask]) ** 2
            for mask in children
        ) / normalizer
        log_drift = full_log - expected_log
        quadratic_drift = 0.5 * (full_mu * full_mu - expected_mu2)
        margin = quadratic_drift - log_drift
        if not margin < -0.1:
            raise AssertionError((m, margin))
        rows.append(
            {
                "child_size": m,
                "normalizer_exact": normalizer,
                "mean_child_mu": expected_mu,
                "logV_drift": log_drift,
                "quadratic_potential_drift": quadratic_drift,
                "quadratic_minus_log_drift": margin,
                "mu_times_mean_drift": full_mu * (full_mu - expected_mu),
            }
        )
    return rows


def one_step_drift(profile, child_profiles) -> dict[str, float | int]:
    v = sum(profile)
    moment = sum(rank * count for rank, count in enumerate(profile))
    mu = moment / v
    child_v = [sum(row) for row in child_profiles]
    child_mu = [
        sum(rank * count for rank, count in enumerate(row)) / value
        for row, value in zip(child_profiles, child_v)
    ]
    normalizer = sum(child_v)
    probabilities = [value / normalizer for value in child_v]
    entropy = -sum(q * math.log2(q) for q in probabilities)
    log_drift = math.log2(v) + entropy - math.log2(normalizer)
    expected_mu = sum(q * value for q, value in zip(probabilities, child_mu))
    expected_mu2 = sum(q * value * value for q, value in zip(probabilities, child_mu))
    mu_linear = mu * (mu - expected_mu)
    quadratic = 0.5 * (mu * mu - expected_mu2)
    return {
        "V": v,
        "mu": mu,
        "mu_minus_log2_n": mu - math.log2(len(child_profiles)),
        "variance": (
            sum(rank * rank * count for rank, count in enumerate(profile)) / v
            - mu * mu
        ),
        "deletion_entropy_defect": math.log2(len(child_profiles)) - entropy,
        "logV_drift": log_drift,
        "mu_times_mean_drift": mu_linear,
        "log_drift_over_mu_times_mean_drift": log_drift / mu_linear,
        "quadratic_potential_drift": quadratic,
        "quadratic_minus_log_drift": quadratic - log_drift,
    }


def n58_audit() -> dict[str, object]:
    points = points_58()
    children = [
        matrix_profile(points[:label] + points[label + 1 :])
        for label in range(len(points))
    ]
    row = one_step_drift(PROFILE_58, children)
    qms_ratio = math.log2(sum(PROFILE_58)) / (0.5 * row["mu"] ** 2)
    if not row["mu"] < 0.9 * math.log2(58):
        raise AssertionError("n=58 record is not in the displayed finite low-mean regime")
    if not qms_ratio > 1.48:
        raise AssertionError(qms_ratio)
    if not row["quadratic_minus_log_drift"] < -0.03:
        raise AssertionError(row)
    return {
        "profile": list(PROFILE_58),
        **row,
        "mu_over_log2_n": row["mu"] / math.log2(58),
        "QMS_ratio": qms_ratio,
        "warning": "This record is not known to minimize V at n=58.",
    }


def pascal_audit() -> list[dict[str, object]]:
    rows = pascal_cells(128, {32, 64, 128})
    out = []
    for row in rows:
        if not row["mu_minus_log2_n"] > 2:
            raise AssertionError("central Pascal cell is not in the high-mean branch")
        if not row["qms_ratio"] > 1:
            raise AssertionError("central Pascal QMS counterexample was not reproduced")
        out.append(
            {
                "family": row["family"],
                "n": row["n"],
                "mu": row["mu"],
                "mu_minus_log2_n": row["mu_minus_log2_n"],
                "QMS_ratio": row["qms_ratio"],
            }
        )
    return out


def main() -> None:
    bridge = n9_cyclic_bridge()
    block_rows = block_qms_drift_n9(bridge)
    points = points_9()
    child_profiles_9 = []
    for label in range(9):
        child = points[:label] + points[label + 1 :]
        profile = [0] * 9
        for mask in range(1 << 8):
            face = [i for i in range(8) if (mask >> i) & 1]
            if is_convex(child, face):
                profile[len(face)] += 1
        child_profiles_9.append(tuple(profile))
    one_step_9 = one_step_drift(tuple(bridge["profile"]), child_profiles_9)
    if not one_step_9["quadratic_minus_log_drift"] < -0.2:
        raise AssertionError(one_step_9)

    # The face masks are an internal work array, not part of the certificate.
    bridge.pop("faces")
    certificate = {
        "schema": "cyclic stems, random half-hulls, and QMS drift barriers",
        "n9_exact_minimizer": {
            **bridge,
            "one_step_deletion": one_step_9,
            "all_direct_block_deletions": block_rows,
            "minimizer_status": (
                "f(9)=169, conditional on the documented completeness of the "
                "Aichholzer-Aurenhammer-Krasser realizable order-type database"
            ),
        },
        "n58_low_mean_nonminimizer": n58_audit(),
        "central_pascal_high_mean_QMS_counterfamily": pascal_audit(),
    }
    output = HERE / "certificate.json"
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
