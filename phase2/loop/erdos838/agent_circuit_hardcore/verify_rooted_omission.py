#!/usr/bin/env python3
"""Exact audit for the rooted marked-omission reduction.

This is a finite verifier, not a proof of (MO).  All geometric predicates and
all displayed ratios use integer/rational arithmetic.
"""

from __future__ import annotations

import itertools
import json
import random
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
TANGENT = ROOT / "agent_tangent_restart"
BIVARIATE = ROOT / "agent_bivariate_potential"
APA_RANK = ROOT / "agent_apa_rank"
TILTED = ROOT / "agent_tilted_switch"
for directory in (TANGENT, BIVARIATE, APA_RANK, TILTED):
    sys.path.insert(0, str(directory))

from tangent_restart_audit import pivot_parts, rooted_profile  # noqa: E402
from tilted_switch_audit import face_table, orient  # noqa: E402
from verify_apa_counterexample import rooted_paths  # noqa: E402
import verify_apa_counterexample as hard44  # noqa: E402
import verify_half_weight_counterexample as hard58  # noqa: E402


Q = Fraction
Point = tuple[int, int]


def value(profile: list[int] | tuple[int, ...], z: Q) -> Q:
    return sum((Q(count) * z**rank for rank, count in enumerate(profile)), Q())


def omission(profile: list[int] | tuple[int, ...], m: int) -> Q:
    return sum(
        (Q((m - rank) * count, 2**rank) for rank, count in enumerate(profile)),
        Q(),
    )


def mean_rank(profile: list[int] | tuple[int, ...], z: Q) -> Q:
    partition = value(profile, z)
    return sum(
        (Q(rank * count) * z**rank for rank, count in enumerate(profile)),
        Q(),
    ) / partition


def unrooted_profile(points: list[Point]) -> tuple[int, ...]:
    result = [0] * (len(points) + 1)
    for mask, is_face in enumerate(face_table(points)):
        if is_face:
            result[mask.bit_count()] += 1
    return tuple(result)


def random_instance(seed: int, m: int) -> tuple[Point, Point, list[Point]]:
    rng = random.Random(seed)
    u, v = (0, 0), (100_000, 0)
    while True:
        points = [
            (rng.randrange(-50_000, 150_001), rng.randrange(1, 200_001))
            for _ in range(m)
        ]
        all_points = [u, v] + points
        if len(set(all_points)) == len(all_points) and all(
            orient(all_points[i], all_points[j], all_points[k])
            for i, j, k in itertools.combinations(range(m + 2), 3)
        ):
            return u, v, points


def repair_capacity(points: list[Point], profile: list[int], u: Point, v: Point) -> dict[str, Q]:
    """Compute both sides of the exact good/repair capacity split."""
    m = len(points)
    faces = face_table(points)
    good_load = [Q() for _ in range(1 << m)]
    bad_mass = Q()
    total = Q()

    for mask in range(1 << m):
        chosen = [points[i] for i in range(m) if mask >> i & 1]
        # rooted_profile always has an empty term, so test the full chosen
        # set directly instead of using the profile's nonemptiness.
        rooted = len(face_table([u, v] + chosen)) and face_table([u, v] + chosen)[-1]
        if not rooted:
            continue
        rank = mask.bit_count()
        weight = Q(1, 2**rank)
        for q in range(m):
            if mask >> q & 1:
                continue
            target = mask | (1 << q)
            total += weight
            if faces[target]:
                good_load[target] += weight
            else:
                bad_mass += weight

    assert total == omission(profile, m)
    assert all(load <= 1 for load in good_load)
    good_mass = sum(good_load, Q())
    slack = sum((Q(1) - good_load[mask] for mask, is_face in enumerate(faces) if is_face), Q())
    assert good_mass + slack == sum(faces)
    assert total == good_mass + bad_mass
    return {
        "total": total,
        "good_mass": good_mass,
        "bad_repair_mass": bad_mass,
        "unused_face_capacity": slack,
    }


def random_audit(records_per_size: int = 8, maximum_m: int = 12) -> dict[str, object]:
    maximum_ratio = Q()
    maximum_record: dict[str, object] | None = None
    recurrence_checks = 0
    repair_checks = 0

    for m in range(2, maximum_m + 1):
        for offset in range(records_per_size):
            seed = 710_000 + 1_000 * m + offset
            u, v, points = random_instance(seed, m)
            profile = rooted_profile(u, v, points)
            v_one = Q(sum(face_table(points)))
            d_full = omission(profile, m)
            ratio = d_full / v_one
            assert ratio <= 1
            if ratio > maximum_ratio:
                maximum_ratio = ratio
                maximum_record = {
                    "m": m,
                    "seed": seed,
                    "rooted_profile": profile,
                    "V": int(v_one),
                    "D": str(d_full),
                }

            # Exact QuickHull marked-omission recurrence (6).
            x, left, right, discarded = pivot_parts(u, v, points)
            without = [point for point in points if point != x]
            p0 = rooted_profile(u, v, without)
            pa = rooted_profile(u, x, left)
            pb = rooted_profile(x, v, right)
            r0 = value(p0, Q(1, 2))
            ah = value(pa, Q(1, 2))
            bh = value(pb, Q(1, 2))
            predicted = (
                omission(p0, m - 1)
                + r0
                + Q(1, 2)
                * (
                    len(discarded) * ah * bh
                    + omission(pa, len(left)) * bh
                    + ah * omission(pb, len(right))
                )
            )
            assert d_full == predicted
            recurrence_checks += 1

            # The full repair split is exponential twice, so check it only
            # on the smaller records.
            if m <= 8:
                split = repair_capacity(points, profile, u, v)
                assert split["bad_repair_mass"] <= split["unused_face_capacity"]
                repair_checks += 1

    return {
        "status": "finite tests pass",
        "records": recurrence_checks,
        "repair_capacity_records": repair_checks,
        "maximum_MO_ratio": str(maximum_ratio),
        "maximum_record": maximum_record,
    }


def apex_local_barrier() -> dict[str, object]:
    chain_size = 12
    last = chain_size - 1
    chain = [(i, i * (last - i)) for i in range(chain_size)]
    apex = (-1, chain_size * chain_size)
    u, v = chain[0], chain[-1]
    points = [apex] + chain[1:-1]
    x, left, right, discarded = pivot_parts(u, v, points)
    assert x == apex and not left and not right and len(discarded) == 10
    r0 = value(rooted_profile(u, v, chain[1:-1]), Q(1, 2))
    delta_v = Q(sum(face_table(points)) - sum(face_table(chain[1:-1])))
    margin = delta_v - r0 - Q(len(discarded), 2)
    assert r0 == Q(59049, 1024)
    assert delta_v == 56
    assert margin == Q(-6825, 1024)
    return {
        "Delta_V": str(delta_v),
        "R_zero_half": str(r0),
        "discarded_points": len(discarded),
        "local_MO_induction_margin": str(margin),
        "pointwise_induction": False,
    }


def quarter_induction_barriers() -> dict[str, object]:
    """Exact failures of the two naive inductions for the quarter target."""
    # QuickHull pointwise failure on the apex/chain record.
    chain_size = 12
    last = chain_size - 1
    chain = [(i, i * (last - i)) for i in range(chain_size)]
    apex = (-1, chain_size * chain_size)
    u, v = chain[0], chain[-1]
    points = [apex] + chain[1:-1]
    m = len(points)
    r0_quarter = value(rooted_profile(u, v, chain[1:-1]), Q(1, 4))
    delta_v = Q(sum(face_table(points)) - sum(face_table(chain[1:-1])))
    quickhull_margin = 4 * delta_v - (2 * m - 1) * r0_quarter - Q(m * m, 4)
    assert quickhull_margin == Q(-1916525, 1048576)

    # Fixed-x stretchable counterexample to the deletion mean condition.
    ys = [110624, 1392103, 188780, 175318, 149905, 150245, 115772, 84074]
    pocket = list(enumerate(ys))
    u2, v2 = (-1, 0), (len(ys) + 1, 0)
    all_points = [u2, v2] + pocket
    assert all(
        orient(all_points[i], all_points[j], all_points[k])
        for i, j, k in itertools.combinations(range(len(all_points)), 3)
    )
    rooted = tuple(rooted_profile(u2, v2, pocket))
    convex = unrooted_profile(pocket)
    assert rooted == (1, 8, 21, 28, 14, 1)
    assert convex == (1, 8, 28, 56, 26, 1, 0, 0, 0)
    mu_r = mean_rank(rooted, Q(1, 4))
    mu_v = mean_rank(convex, Q(1))
    threshold = Q(2) - Q(1, 8) + Q(7, 8) ** 2 * mu_r
    mean_margin = mu_v - threshold
    assert mean_margin < 0

    return {
        "quickhull_pointwise_QI_margin": str(quickhull_margin),
        "mean_induction_counterexample": {
            "m": 8,
            "fixed_x_y_coordinates": ys,
            "rooted_profile": list(rooted),
            "unrooted_profile": list(convex),
            "mu_R_at_quarter": str(mu_r),
            "mu_V_at_one": str(mu_v),
            "mean_condition_margin": str(mean_margin),
        },
    }


def sentinel_profile(raw_points) -> tuple[int, ...]:
    """Rooted cap profile with far-below left/right sentinels."""
    points = tuple(sorted(raw_points))
    m = len(points)
    y_min = min(y for _, y in points)
    height = Q(10**40)
    u = (points[0][0] - 1, y_min - height)
    v = (points[-1][0] + 1, y_min - height)
    augmented = (u,) + points + (v,)
    paths = rooted_paths(augmented, 0, -1)[m + 1]
    profile = [0] * (m + 1)
    for edges, count in enumerate(paths):
        if edges:
            profile[edges - 1] = count
    assert profile[0] == 1 and profile[1] == m
    return tuple(profile)


def hard_record_audit() -> list[dict[str, object]]:
    records = []
    for label, points, convex_profile in (
        ("hard-44", hard44.points(), hard44.EXPECTED_PROFILE),
        ("hard-58", hard58.points(), hard58.EXPECTED_PROFILE),
    ):
        rooted = sentinel_profile(points)
        m = len(points)
        d_value = omission(rooted, m)
        v_one = Q(sum(convex_profile))
        assert d_value < v_one
        records.append(
            {
                "label": label,
                "m": m,
                "rooted_profile": list(rooted),
                "D": str(d_value),
                "V": int(v_one),
                "MO_ratio": str(d_value / v_one),
                "MO_ratio_decimal": float(d_value / v_one),
            }
        )
    return records


def main() -> None:
    result = {
        "random_marked_omission": random_audit(),
        "pointwise_quickhull_barrier": apex_local_barrier(),
        "quarter_target_induction_barriers": quarter_induction_barriers(),
        "hard_records": hard_record_audit(),
        "warning": "finite verification only; MO, RT, RPH, and EIC remain unproved",
    }
    output = HERE / "rooted_omission_certificate.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
