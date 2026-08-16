#!/usr/bin/env python3
"""Exact planar f-vector shape audit for the Erdős 838 attack.

This verifier does four things:

* certifies an integral 14-point counterexample to ordinary log-concavity;
* certifies the six-point parabola/chord counterexample to ULC;
* recursively finds and audits saved exact convex-subset profiles; and
* checks the surviving two-step and block-growth diagnostics.

Every geometric predicate is integral.  Convex profiles are computed both
by direct hull enumeration and by upward-closing the nonconvex quadruples.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUTPUT = HERE / "fvector_shape_certificate.json"
GENERATED_PROFILE_CERTIFICATES = {
    OUTPUT.resolve(),
    (HERE / "block_window_certificate.json").resolve(),
}

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


Point = tuple[int, int]


LC_KILL_Y = (
    -4015,
    2780,
    8170,
    5429,
    -4867,
    -2452,
    -5229,
    -5102,
    7389,
    -596,
    -8841,
    -8375,
    -8464,
    -8566,
)
LC_KILL_PROFILE = (1, 14, 91, 364, 668, 606, 253, 15, 2, 0, 0, 0, 0, 0, 0)
ULC_KILL_PROFILE = (1, 6, 15, 20, 5, 1, 0)


def orient(a: Point, b: Point, c: Point) -> int:
    determinant = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )
    return (determinant > 0) - (determinant < 0)


def general_position(points: Sequence[Point]) -> bool:
    return all(
        orient(points[i], points[j], points[k])
        for i, j, k in itertools.combinations(range(len(points)), 3)
    )


def convex_hull(points: Sequence[Point], indices: Iterable[int]) -> list[int]:
    selected = sorted(indices, key=lambda index: (points[index], index))
    if len(selected) <= 1:
        return selected

    def half(items: Iterable[int]) -> list[int]:
        answer: list[int] = []
        for item in items:
            while (
                len(answer) >= 2
                and orient(points[answer[-2]], points[answer[-1]], points[item]) <= 0
            ):
                answer.pop()
            answer.append(item)
        return answer

    lower = half(selected)
    upper = half(reversed(selected))
    return lower[:-1] + upper[:-1]


def is_convex(points: Sequence[Point], indices: Sequence[int]) -> bool:
    return len(indices) <= 2 or len(convex_hull(points, indices)) == len(indices)


def direct_profile(points: Sequence[Point]) -> tuple[int, ...]:
    profile = [0] * (len(points) + 1)
    for rank in range(len(points) + 1):
        profile[rank] = sum(
            is_convex(points, face)
            for face in itertools.combinations(range(len(points)), rank)
        )
    return tuple(profile)


def circuit_profile(points: Sequence[Point]) -> tuple[int, ...]:
    """Profile from the upward closure of nonconvex quadruples."""
    n = len(points)
    nonconvex = bytearray(1 << n)
    for quadruple in itertools.combinations(range(n), 4):
        if not is_convex(points, quadruple):
            nonconvex[sum(1 << point for point in quadruple)] = 1
    for point in range(n):
        bit = 1 << point
        for mask in range(1 << n):
            if mask & bit and nonconvex[mask ^ bit]:
                nonconvex[mask] = 1
    profile = [0] * (n + 1)
    for mask, bad in enumerate(nonconvex):
        if not bad:
            profile[mask.bit_count()] += 1
    return tuple(profile)


def last_nonzero(profile: Sequence[int]) -> int:
    return max(rank for rank, count in enumerate(profile) if count)


def lc_failures(profile: Sequence[int]) -> list[dict[str, object]]:
    failures = []
    for rank in range(1, last_nonzero(profile)):
        lhs = profile[rank] ** 2
        rhs = profile[rank - 1] * profile[rank + 1]
        if lhs < rhs:
            failures.append(
                {"rank": rank, "lhs": lhs, "rhs": rhs, "ratio": str(Fraction(lhs, rhs))}
            )
    return failures


def ulc_failures(profile: Sequence[int]) -> list[dict[str, object]]:
    n = profile[1]
    failures = []
    for rank in range(1, last_nonzero(profile)):
        lhs = (
            profile[rank] ** 2
            * math.comb(n, rank - 1)
            * math.comb(n, rank + 1)
        )
        rhs = (
            profile[rank - 1]
            * profile[rank + 1]
            * math.comb(n, rank) ** 2
        )
        if lhs < rhs:
            failures.append(
                {"rank": rank, "lhs": lhs, "rhs": rhs, "ratio": str(Fraction(lhs, rhs))}
            )
    return failures


def step_failures(profile: Sequence[int], step: int) -> list[dict[str, object]]:
    failures = []
    maximum = last_nonzero(profile)
    for rank in range(step, maximum - step + 1):
        lhs = profile[rank] ** 2
        rhs = profile[rank - step] * profile[rank + step]
        if lhs < rhs:
            failures.append(
                {"rank": rank, "lhs": lhs, "rhs": rhs, "ratio": str(Fraction(lhs, rhs))}
            )
    return failures


def block_growth(profile: Sequence[int], block: int) -> bool:
    """Check v_(k+b) >= 2 v_k through k+b <= ell-b."""
    n = profile[1]
    ell = (n - 1).bit_length()
    return all(
        rank + block < len(profile)
        and profile[rank + block] >= 2 * profile[rank]
        for rank in range(max(0, ell - 2 * block + 1))
    )


def minimal_block(profile: Sequence[int]) -> int | None:
    ell = (profile[1] - 1).bit_length()
    return next((block for block in range(1, ell + 1) if block_growth(profile, block)), None)


def saved_profiles() -> dict[tuple[int, ...], list[str]]:
    """Find integer arrays which certify their own n through ranks 0--3."""
    profiles: dict[tuple[int, ...], list[str]] = {}
    for path in ROOT.rglob("*.json"):
        if path.resolve() in GENERATED_PROFILE_CERTIFICATES:
            continue
        # Parallel block-search output is audited by verify_block_window.py.
        # Some search snapshots are deliberately truncated before ell, so
        # they are not members of this fixed full-profile corpus.
        if HERE / "block_search" in path.parents:
            continue
        try:
            document = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError):
            continue

        def visit(value: object, key_path: tuple[str, ...] = ()) -> None:
            if isinstance(value, dict):
                for key, child in value.items():
                    visit(child, key_path + (str(key),))
            elif isinstance(value, list):
                if (
                    len(value) >= 4
                    and all(isinstance(item, int) and not isinstance(item, bool) for item in value)
                ):
                    n = value[1]
                    if (
                        value[0] == 1
                        and n >= 3
                        and value[2] == math.comb(n, 2)
                        and value[3] == math.comb(n, 3)
                    ):
                        profile = tuple(value)
                        profiles.setdefault(profile, []).append(
                            f"{path.relative_to(ROOT)}:{'.'.join(key_path)}"
                        )
                for child in value:
                    if isinstance(child, (dict, list)):
                        visit(child, key_path)

        visit(document)
    return profiles


def guarded_block_audit() -> list[dict[str, object]]:
    source = json.loads(
        (ROOT / "agent_generalized_deletion" / "rankwise_nearmax_certificate.json").read_text()
    )["guarded_vertical_profile_upper_bounds"]
    rows = []
    for family, records in source.items():
        for record in records:
            ell = int(record["L"])
            terms = [Fraction(value) for value in record["profile_upper_terms"]]
            # term_k = 2^(ell-k) v_k / V, so v_(k+b)>=2v_k iff
            # 2^b term_(k+b)>=2 term_k.
            good = []
            for block in range(1, ell + 1):
                if all(
                    terms[rank + block] * (1 << block) >= 2 * terms[rank]
                    for rank in range(max(0, ell - 2 * block + 1))
                ):
                    good.append(block)
            rows.append(
                {
                    "family": family,
                    "depth": record["depth"],
                    "n": record["n"],
                    "ell": ell,
                    "minimal_block": min(good),
                }
            )
    return rows


def log_concavity_insufficiency_model(log_n: int = 64) -> dict[str, object]:
    """Exact rational LC sequence with known-scale mass but mean ~L/4."""
    n = 1 << log_n
    mode = log_n // 4
    support = log_n
    profile: list[Fraction] = [Fraction(math.comb(n, rank)) for rank in range(mode + 1)]
    peak = profile[-1]
    profile.extend(peak / (1 << shift) for shift in range(1, support - mode + 1))
    for rank in range(1, support):
        if profile[rank] ** 2 < profile[rank - 1] * profile[rank + 1]:
            raise AssertionError(("LC model", rank))
    for rank in range(2, support - 1):
        if profile[rank] ** 2 < profile[rank - 2] * profile[rank + 2]:
            raise AssertionError(("two-step LC model", rank))
    total = sum(profile)
    mean = sum(rank * count for rank, count in enumerate(profile)) / total
    return {
        "log2_n": log_n,
        "mode": mode,
        "support_maximum": support,
        "log2_peak_lower_bound": log_n * mode - math.lgamma(mode + 1) / math.log(2),
        "quarter_scale_target": log_n * log_n / 4,
        "mean_exact": str(mean),
        "mean_decimal": float(mean),
        "ordinary_LC": True,
        "two_step_LC": True,
        "interpretation": "shape plus the known quarter-scale V bound does not force mean near log n",
    }


def main() -> None:
    lc_points = tuple((index, value) for index, value in enumerate(LC_KILL_Y))
    ulc_points = tuple((index, index * index) for index in range(5)) + ((5, 0),)
    if not general_position(lc_points) or not general_position(ulc_points):
        raise AssertionError("counterexample is not in general position")
    if direct_profile(lc_points) != LC_KILL_PROFILE:
        raise AssertionError("direct LC-kill profile mismatch")
    if circuit_profile(lc_points) != LC_KILL_PROFILE:
        raise AssertionError("circuit LC-kill profile mismatch")
    if direct_profile(ulc_points) != ULC_KILL_PROFILE:
        raise AssertionError("direct ULC-kill profile mismatch")
    if circuit_profile(ulc_points) != ULC_KILL_PROFILE:
        raise AssertionError("circuit ULC-kill profile mismatch")

    lc_kill_failures = lc_failures(LC_KILL_PROFILE)
    ulc_kill_failures = ulc_failures(ULC_KILL_PROFILE)
    if lc_kill_failures != [{"rank": 7, "lhs": 225, "rhs": 506, "ratio": "225/506"}]:
        raise AssertionError(lc_kill_failures)
    if not ulc_kill_failures:
        raise AssertionError("ULC kill did not fail")

    profiles = saved_profiles()
    saved_rows = []
    for profile, sources in profiles.items():
        saved_rows.append(
            {
                "n": profile[1],
                "profile": list(profile),
                "sources": sources,
                "LC_failures": lc_failures(profile),
                "ULC_failures": ulc_failures(profile),
                "two_step_LC_failures": step_failures(profile, 2),
                "minimal_doubling_block": minimal_block(profile),
            }
        )

    certificate = {
        "description": "exact planar convex-face f-vector shape audit",
        "ordinary_log_concavity_counterexample": {
            "points": [list(point) for point in lc_points],
            "profile": list(LC_KILL_PROFILE),
            "failures": lc_kill_failures,
            "two_step_failures": step_failures(LC_KILL_PROFILE, 2),
            "minimal_doubling_block": minimal_block(LC_KILL_PROFILE),
        },
        "ultra_log_concavity_counterexample": {
            "points": [list(point) for point in ulc_points],
            "profile": list(ULC_KILL_PROFILE),
            "ordinary_LC_failures": lc_failures(ULC_KILL_PROFILE),
            "ULC_failures": ulc_kill_failures,
        },
        "saved_profile_count_with_duplicates_removed": len(saved_rows),
        "saved_profiles_with_LC_failure": sum(bool(row["LC_failures"]) for row in saved_rows),
        "saved_profiles_with_ULC_failure": sum(bool(row["ULC_failures"]) for row in saved_rows),
        "saved_profiles_with_two_step_LC_failure": sum(
            bool(row["two_step_LC_failures"]) for row in saved_rows
        ),
        "saved_profile_audits": saved_rows,
        "guarded_directional_block_audit": guarded_block_audit(),
        "log_concavity_insufficiency_model": log_concavity_insufficiency_model(),
    }
    OUTPUT.write_text(json.dumps(certificate, indent=2) + "\n")
    print(
        json.dumps(
            {
                "saved_profiles": len(saved_rows),
                "saved_LC_failures": certificate["saved_profiles_with_LC_failure"],
                "saved_ULC_failures": certificate["saved_profiles_with_ULC_failure"],
                "saved_two_step_failures": certificate[
                    "saved_profiles_with_two_step_LC_failure"
                ],
                "LC_kill": lc_kill_failures,
                "ULC_kill": ulc_kill_failures,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
