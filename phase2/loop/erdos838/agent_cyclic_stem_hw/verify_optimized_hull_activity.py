#!/usr/bin/env python3
"""Verifier for the optimized hull-activity / RNP reduction.

The hull identities and all finite tail inequalities are checked with exact
rational arithmetic.  Entropy inversions are numerical consequences of the
exact identity; they are reported only after the exact census has passed.
Large Pascal coefficients are kept as Python integers and logarithms are
evaluated from their leading bits, avoiding conversion overflow.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LATTICE = ROOT / "agent_planar_lattice_mean"
GRADED = ROOT / "agent_graded_supersat"
APA = ROOT / "agent_apa_rank"
for directory in (LATTICE, GRADED, APA):
    sys.path.insert(0, str(directory))

from graded_balanced import pascal_row  # noqa: E402
from graded_trace import pascal_cell  # noqa: E402
from planar_lattice_mean import closure_mask, is_convex, orient  # noqa: E402
from verify_half_weight_counterexample import EXPECTED_PROFILE as PROFILE_58  # noqa: E402


def log2_int(value: int) -> float:
    """Accurate finite log2 without overflowing through a float cast."""
    if value <= 0:
        raise ValueError(value)
    bits = value.bit_length()
    if bits <= 53:
        return math.log2(value)
    shift = bits - 53
    return shift + math.log2(value >> shift)


def ceil_log2_int(value: int) -> int:
    if value <= 0:
        raise ValueError(value)
    return (value - 1).bit_length()


def psi(rank: int, q: float) -> float:
    """(r+q) H_2(r/(r+q)), in a stable two-term form."""
    if rank < 0 or q < 0:
        raise ValueError((rank, q))
    if rank == 0 or q == 0:
        return 0.0
    return (
        rank * math.log1p(q / rank) / math.log(2.0)
        + q * math.log1p(rank / q) / math.log(2.0)
    )


def entropy_inverse(rank: int, log_count: float, n: int) -> float:
    """Smallest q in [0,n-r] with Psi(r,q) >= log_count."""
    if log_count <= 0:
        return 0.0
    upper = float(n - rank)
    if psi(rank, upper) + 1e-8 < log_count:
        raise AssertionError((rank, log_count, n, psi(rank, upper)))
    lower = 0.0
    for _ in range(160):
        middle = (lower + upper) / 2.0
        if psi(rank, middle) < log_count:
            lower = middle
        else:
            upper = middle
    return upper


def coarse_inverse(rank: int, log_count: float) -> float:
    """Consequence q >= r(2^(log M/r)/e-1) of Psi's elementary upper bound."""
    if rank == 0 or log_count <= 0:
        return 0.0
    return max(0.0, rank * (2.0 ** (log_count / rank) / math.e - 1.0))


def rank_row(rank: int, count: int, n: int, total: int) -> dict[str, object]:
    log_count = log2_int(count)
    required = entropy_inverse(rank, log_count, n)
    coarse = coarse_inverse(rank, log_count)
    ell = ceil_log2_int(n)
    demand = 2.0 ** (ell - rank)
    return {
        "rank": rank,
        "count": count,
        "log2_count": log_count,
        "density_log2": log_count - log2_int(total),
        "entropy_required_mean_q": required,
        "coarse_required_mean_q": coarse,
        "RNP_demand_2^(ell-r)": demand,
        "entropy_q_over_RNP_demand": required / demand,
        "coarse_q_over_RNP_demand": coarse / demand,
    }


def profile_audit(profile: list[int] | tuple[int, ...], n: int) -> dict[str, object]:
    values = list(profile)
    if not values or values[0] != 1:
        raise AssertionError("profiles must include the empty face")
    total = sum(values)
    ell = ceil_log2_int(n)
    ranks = [
        rank_row(rank, values[rank], n, total)
        for rank in range(1, min(ell, len(values)))
        if values[rank]
    ]
    modal_rank = max(range(len(values)), key=values.__getitem__)
    modal = rank_row(modal_rank, values[modal_rank], n, total) if modal_rank else None
    return {
        "n": n,
        "ell": ell,
        "profile": values,
        "V": total,
        "log2_V": log2_int(total),
        "modal_rank": modal_rank,
        "modal_rank_audit": modal,
        "ranks_below_ell": ranks,
    }


def exact_configuration_audit(
    name: str,
    points: tuple[tuple[object, object], ...],
    expected_profile: list[int] | tuple[int, ...],
) -> dict[str, object]:
    """Enumerate convex faces, their closures, and exact activity sums."""
    n = len(points)
    expected = list(expected_profile) + [0] * (n + 1 - len(expected_profile))
    expected[0] = 1
    maximum = max(rank for rank, count in enumerate(expected) if count)
    joint: dict[tuple[int, int], int] = {}
    profile = [0] * (n + 1)
    faces_by_rank: dict[int, list[tuple[tuple[int, ...], int, int, int]]] = {}
    for rank in range(maximum + 1):
        for face in itertools.combinations(range(n), rank):
            if not is_convex(points, face):
                continue
            q = n - closure_mask(points, face).bit_count()
            face_set = set(face)
            up_degree = sum(
                is_convex(points, face + (point,))
                for point in range(n)
                if point not in face_set
            )
            exterior_blocked = q - up_degree
            if exterior_blocked < 0:
                raise AssertionError((name, face, q, up_degree))
            profile[rank] += 1
            joint[(rank, q)] = joint.get((rank, q), 0) + 1
            faces_by_rank.setdefault(rank, []).append(
                (face, q, up_degree, exterior_blocked)
            )
    if profile != expected:
        raise AssertionError((name, profile, expected))

    identities = {}
    for activity in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
        value = sum(
            (
                count
                * activity**rank
                * (1 - activity) ** q
                for (rank, q), count in joint.items()
            ),
            Fraction(),
        )
        if value != 1:
            raise AssertionError((name, activity, value))
        identities[str(activity)] = str(value)

    total = sum(profile)
    for rank, face_rows in faces_by_rank.items():
        up_sum = sum(value[2] for value in face_rows)
        target = (rank + 1) * profile[rank + 1] if rank + 1 < len(profile) else 0
        if up_sum != target:
            raise AssertionError((name, rank, up_sum, target))
    rows = []
    exact_tail_checks = 0
    for rank, count in enumerate(profile):
        if not count or rank == 0:
            continue
        q_counts = {q: joint.get((rank, q), 0) for q in range(n - rank + 1)}
        q_sum = sum(q * multiplicity for q, multiplicity in q_counts.items())
        actual_mean = Fraction(q_sum, count)
        row = rank_row(rank, count, n, total)
        required = float(row["entropy_required_mean_q"])
        if float(actual_mean) + 1e-9 < required:
            raise AssertionError((name, rank, actual_mean, required))

        # The optimized tail statement is checked at every integral cutoff.
        cumulative = 0
        minimum_exact_margin = None
        for cutoff in range(n - rank + 1):
            cumulative += q_counts[cutoff]
            if not cumulative:
                continue
            if cutoff == 0:
                if cumulative > 1:
                    raise AssertionError((name, rank, cutoff, cumulative))
                margin = Fraction(1 - cumulative, 1)
            else:
                activity = Fraction(rank, rank + cutoff)
                lhs = cumulative * activity**rank * (1 - activity) ** cutoff
                if lhs > 1:
                    raise AssertionError((name, rank, cutoff, lhs))
                margin = 1 - lhs
            minimum_exact_margin = (
                margin
                if minimum_exact_margin is None or margin < minimum_exact_margin
                else minimum_exact_margin
            )
            exact_tail_checks += 1
        row.update(
            {
                "actual_mean_q_exact": str(actual_mean),
                "actual_mean_q_decimal": float(actual_mean),
                "actual_over_entropy_required": (
                    float(actual_mean) / required if required else None
                ),
                "q_distribution": {
                    str(q): multiplicity
                    for q, multiplicity in q_counts.items()
                    if multiplicity
                },
                "minimum_exact_tail_margin": str(minimum_exact_margin),
            }
        )
        face_rows = faces_by_rank[rank]
        exterior_sum = sum(value[3] for value in face_rows)
        near = [value for value in face_rows if value[2] <= 4 * (rank + 1)]
        near_exterior_sum = sum(value[3] for value in near)
        row.update(
            {
                "actual_mean_exterior_blocked_exact": str(
                    Fraction(exterior_sum, count)
                ),
                "near_maximal_count_u<=4(r+1)": len(near),
                "near_maximal_exterior_incidence_sum": near_exterior_sum,
                "near_maximal_exterior_incidence_over_V": near_exterior_sum / total,
            }
        )
        rows.append(row)

    return {
        "name": name,
        "n": n,
        "profile": profile,
        "V": total,
        "joint_rank_q": {
            f"{rank},{q}": count for (rank, q), count in sorted(joint.items())
        },
        "exact_hull_activity_identities": identities,
        "exact_tail_checks": exact_tail_checks,
        "rank_audits": rows,
    }


def n9_points() -> tuple[tuple[int, int], ...]:
    source = json.loads(
        (ROOT / "agent_lex_minimizer_search" / "exact_realizable_n9.json").read_text()
    )
    return tuple(tuple(point) for point in source["coordinates_as_stored"])


def n20_macro() -> tuple[tuple[tuple[int, int], ...], list[int]]:
    source = json.loads(
        (ROOT / "agent_growing_state_upper" / "LARGE_MACRO_CERTIFICATE.json").read_text()
    )["macros"]["20"]
    points = tuple(tuple(point) for point in source["points"])
    profile = list(source["convex_profile"])
    profile[0] = 1
    return points, profile


def asymptotic_square_audit() -> list[dict[str, object]]:
    rows = []
    for ell in (64, 128, 256):
        for numerator in (1, 2, 3, 4):
            rank = ell * numerator // 4
            left = Fraction(ell * ell, 4 * rank) - (ell - rank)
            right = Fraction((2 * rank - ell) ** 2, 4 * rank)
            if left != right or left < 0:
                raise AssertionError((ell, rank, left, right))
            rows.append(
                {
                    "ell": ell,
                    "rank": rank,
                    "rho": rank / ell,
                    "label_exponent_ell^2/(4r)": ell * ell / (4 * rank),
                    "RNP_demand_exponent_ell-r": ell - rank,
                    "exponent_margin_exact": str(left),
                }
            )
    return rows


def exterior_addability_regression() -> dict[str, object]:
    """A rooted-circuit regression: outside the hull does not mean addable."""
    points = ((-1, 0), (0, 1), (1, 0), (0, 3))
    face = (0, 1, 2)
    if not is_convex(points, face):
        raise AssertionError("base triangle must be convex")
    q = len(points) - closure_mask(points, face).bit_count()
    actual_up = sum(
        is_convex(points, face + (point,))
        for point in range(len(points))
        if point not in face
    )
    exterior_blocked = q - actual_up
    if (q, actual_up, exterior_blocked) != (1, 0, 1):
        raise AssertionError((q, actual_up, exterior_blocked))
    return {
        "points": points,
        "face": face,
        "outside_hull_q": q,
        "actual_addable_u": actual_up,
        "exterior_blocked_e": exterior_blocked,
        "status": "PASS",
        "warning": (
            "Counting points not interior to conv(A) computes q=u+e, not u; "
            "an exterior point can hide an old vertex."
        ),
    }


def inside_triangle(point, a, b, c) -> bool:
    signs = (orient(a, b, point), orient(b, c, point), orient(c, a, point))
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


def circuit_masks(points):
    """Root masks and full nonconvex-extension masks for every triple."""
    n = len(points)
    triples = list(itertools.combinations(range(n), 3))
    root_masks = {triple: 0 for triple in triples}
    bad_extension_masks = {triple: 0 for triple in triples}
    for quadruple in itertools.combinations(range(n), 4):
        root_data = None
        for root in quadruple:
            triple = tuple(label for label in quadruple if label != root)
            if inside_triangle(points[root], *(points[label] for label in triple)):
                root_data = (root, triple)
                break
        if root_data is None:
            continue
        root, triple = root_data
        root_masks[triple] |= 1 << root
        # T+p is nonconvex regardless of which member of the quadruple is
        # its unique interior root.  This is the mask needed for addability.
        for point in quadruple:
            other = tuple(label for label in quadruple if label != point)
            bad_extension_masks[other] |= 1 << point
    return root_masks, bad_extension_masks


def small_pascal_exterior_audit() -> dict[str, object]:
    """Exact EIC stress test on central Pascal cells through 35 points."""
    output = {}
    for parameter in (4, 5, 6, 7):
        points = tuple(sorted(pascal_cell(parameter, parameter // 2, Fraction(1, 97))))
        n = len(points)
        ell = ceil_log2_int(n)
        _, _, _, convex = pascal_row(parameter, parameter)[parameter // 2]
        profile = [1] + convex[1:]
        total = sum(profile)
        roots, bad_extensions = circuit_masks(points)
        full_mask = (1 << n) - 1
        rows = []
        for rank in range(ell):
            face_count = near_count = exterior_sum = 0
            for face in itertools.combinations(range(n), rank):
                mask = sum(1 << label for label in face)
                interior = 0
                bad = 0
                for triple in itertools.combinations(face, 3):
                    interior |= roots[triple]
                    bad |= bad_extensions[triple]
                if interior & mask:
                    continue
                face_count += 1
                q = n - rank - (interior & ~mask).bit_count()
                up_degree = (full_mask & ~mask & ~bad).bit_count()
                if up_degree <= 4 * (rank + 1):
                    near_count += 1
                    exterior_sum += q - up_degree
            if face_count != profile[rank]:
                raise AssertionError((parameter, rank, face_count, profile[rank]))
            rows.append(
                {
                    "rank": rank,
                    "face_count": face_count,
                    "near_maximal_count": near_count,
                    "near_maximal_exterior_incidence_sum": exterior_sum,
                    "exterior_incidence_over_V": exterior_sum / total,
                }
            )
        output[str(parameter)] = {"n": n, "V": total, "ranks_below_ell": rows}
    return output


def guarded_iterate_eic_profile_upper() -> dict[str, object]:
    """Rigorous EIC upper E_r/V <= n v_r/V on saved guarded profiles."""
    source = json.loads(
        (
            ROOT
            / "agent_generalized_deletion"
            / "rankwise_nearmax_certificate.json"
        ).read_text()
    )["guarded_vertical_profile_upper_bounds"]
    output = {}
    for family, rows in source.items():
        audited = []
        for row in rows:
            n = int(row["n"])
            ell = int(row["L"])
            candidates = [
                Fraction(n) * Fraction(value) * Fraction(1 << rank, 1 << ell)
                for rank, value in enumerate(row["profile_upper_terms"])
            ]
            maximum = max(candidates)
            audited.append(
                {
                    "depth": int(row["depth"]),
                    "n": n,
                    "maximizing_rank": candidates.index(maximum),
                    "EIC_profile_upper_exact": str(maximum),
                    "EIC_profile_upper_decimal": float(maximum),
                }
            )
        if not all(
            audited[index + 1]["EIC_profile_upper_decimal"]
            < audited[index]["EIC_profile_upper_decimal"]
            for index in range(1, len(audited) - 1)
        ):
            raise AssertionError((family, audited))
        output[family] = audited
    return output


def main() -> None:
    exact9_profile = json.loads(
        (ROOT / "agent_lex_minimizer_search" / "exact_realizable_n9.json").read_text()
    )["profile"]
    points20, profile20 = n20_macro()
    exact = {
        "n9_exact_minimizer": exact_configuration_audit(
            "n9_exact_minimizer", n9_points(), exact9_profile
        ),
        "n20_exact_macro": exact_configuration_audit(
            "n20_exact_macro", points20, profile20
        ),
    }

    half = json.loads((ROOT / "agent_half_weight" / "certificate.json").read_text())[
        "records"
    ]
    saved = {
        name: profile_audit(row["profile"], int(name))
        for name, row in half.items()
        if name in {"20", "24", "30"}
    }
    saved["58"] = profile_audit(PROFILE_58, 58)

    pascal = {}
    for parameter in (16, 32, 64):
        n, _, _, convex = pascal_row(parameter, parameter)[parameter // 2]
        profile = [1] + convex[1:]
        pascal[str(parameter)] = profile_audit(profile, n)

    certificate = {
        "mode": "optimized_hull_activity_and_rnp_label_gate",
        "exact_configuration_checks": exact,
        "saved_profile_stress_tests": saved,
        "central_pascal_stress_tests": pascal,
        "asymptotic_square_identity": asymptotic_square_audit(),
        "exterior_addability_regression": exterior_addability_regression(),
        "small_central_pascal_exact_exterior_incidence": small_pascal_exterior_audit(),
        "guarded_iterate_EIC_profile_upper_bounds": guarded_iterate_eic_profile_upper(),
        "status": "PASS",
    }
    output = HERE / "optimized_hull_certificate.json"
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print("PASS optimized hull activity")
    for row in exact.values():
        print(row["name"], "V=", row["V"], "tail_checks=", row["exact_tail_checks"])
    for name, row in saved.items():
        modal = row["modal_rank_audit"]
        print(
            "saved",
            name,
            "modal_r=",
            row["modal_rank"],
            "required_q=",
            f"{modal['entropy_required_mean_q']:.6f}",
            "demand=",
            f"{modal['RNP_demand_2^(ell-r)']:.6f}",
        )
    for name, row in pascal.items():
        below = row["ranks_below_ell"][-1]
        print(
            "pascal",
            name,
            "n=",
            row["n"],
            "last_r=",
            below["rank"],
            "q/demand=",
            f"{below['entropy_q_over_RNP_demand']:.6g}",
        )


if __name__ == "__main__":
    main()
