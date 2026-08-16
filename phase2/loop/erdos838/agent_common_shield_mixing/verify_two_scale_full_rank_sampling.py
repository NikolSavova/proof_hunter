#!/usr/bin/env python3
"""Exact audit for TWO_SCALE_FULL_RANK_SAMPLING_BARRIER.md.

The geometry check uses a rational, general-position planar order type.  All
remaining checks use integers or Fraction, so no numerical optimizer is being
trusted for the coefficient threshold.
"""

from __future__ import annotations

import importlib.util
import json
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUTER = HERE.parent / "agent_outer_internal_product"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    assert specification is not None and specification.loader is not None
    module = importlib.util.module_from_spec(specification)
    specification.loader.exec_module(module)
    return module


TWO = load_module(
    "two_reference_for_rank_sampling",
    OUTER / "verify_two_reference_hall_demand.py",
)


def planar_hypergeometric_audit() -> dict[str, object]:
    """Enumerate every restriction and check the lift rank by rank."""
    points = TWO.POINTS
    n = len(points)
    faces = TWO.enumerate_faces(points)
    face_set = set(faces)
    assert len(faces) == 449
    profile = Counter(map(len, faces))

    reports = {}
    for t in range(n + 1):
        restriction_count = comb(n, t)
        rank_totals = Counter()
        for target in combinations(range(n), t):
            target_set = set(target)
            # Convex position is intrinsic to the chosen points, so these are
            # exactly the faces of the induced configuration P[target].
            induced = [face for face in faces if set(face) <= target_set]
            assert all(face in face_set for face in induced)
            rank_totals.update(map(len, induced))

        recovered_total = Q()
        for k, v_k in profile.items():
            if k > t:
                assert rank_totals[k] == 0
                continue
            a_k = Q(rank_totals[k], restriction_count)
            containment = Q(comb(t, k), comb(n, k))
            containment_alt = Q(comb(n - k, t - k), comb(n, t))
            assert containment == containment_alt
            assert a_k == v_k * containment
            recovered_total += a_k / containment
            # Exact finite version of the coarse lift used in the theorem.
            if t > 0:
                assert Q(comb(n, k), comb(t, k)) >= Q(n, t) ** k
        assert recovered_total == sum(v for k, v in profile.items() if k <= t)
        assert recovered_total <= sum(profile.values())
        reports[t] = sum(rank_totals.values())

    return {
        "points": n,
        "faces": len(faces),
        "profile": dict(sorted(profile.items())),
        "restriction_incidence_totals": reports,
    }


def profile_fixed_point_audit() -> dict[str, object]:
    """Check the full-profile identity and its exact 1/4 ceiling."""
    checked = 0
    best = Q()
    best_pair = None
    for denominator_a in range(2, 41):
        for numerator_a in range(1, denominator_a + 1):
            alpha = Q(numerator_a, denominator_a)
            for denominator_theta in range(2, 41):
                for numerator_theta in range(1, denominator_theta):
                    theta = Q(numerator_theta, denominator_theta)
                    y = alpha * theta
                    lifted = (
                        alpha * alpha * theta * (1 - theta)
                        + alpha * (1 - alpha) * theta
                    )
                    assert lifted == y * (1 - y)
                    assert lifted <= Q(1, 4)
                    if lifted > best:
                        best = lifted
                        best_pair = (alpha, theta)
                    checked += 1

    # The rational grid contains alpha=theta=1/sqrt(2) only approximately,
    # but it contains many exact pairs with alpha*theta=1/2, e.g. (1,1/2).
    assert best == Q(1, 4)
    return {
        "rational_pairs": checked,
        "maximum": str(best),
        "one_maximizer": tuple(map(str, best_pair)),
    }


def tail_threshold_audit() -> dict[str, object]:
    """Verify the c=1/4 threshold, optimizer, and square gain exactly."""
    c = Q(1, 4)
    tested = []
    for lambda_ in [Q(i, 40) for i in range(1, 41)]:
        def recurrence(alpha: Q) -> Q:
            return c * alpha * alpha + lambda_ * alpha * (1 - alpha)

        if lambda_ <= Q(1, 2):
            # A concave stationary point, if present, lies at or beyond 1;
            # otherwise the quadratic is convex.  In both cases the endpoint
            # maximum is c.  A fine exact grid supplies an independent audit.
            predicted = c
            alpha_star = Q(1)
        else:
            alpha_star = lambda_ / (2 * (lambda_ - c))
            assert 0 < alpha_star < 1
            predicted = lambda_ * lambda_ / (4 * (lambda_ - c))
            gain = (lambda_ - Q(1, 2)) ** 2 / (4 * (lambda_ - c))
            assert predicted - c == gain > 0

        grid_max = max(recurrence(Q(i, 400)) for i in range(1, 401))
        assert grid_max <= predicted
        assert recurrence(alpha_star) == predicted
        assert (predicted > c) == (lambda_ > Q(1, 2))
        tested.append((str(lambda_), str(alpha_star), str(predicted)))

    return {"tested_lambdas": len(tested), "boundary": "1/2", "examples": tested[::10]}


def greedy_rank_allocation_audit() -> dict[str, object]:
    """Dynamic-programming audit of the exact low-rank filling lemma."""
    t, n = 7, 19
    capacities = [comb(t, k) for k in range(t + 1)]
    prices = [Q(comb(n, k), comb(t, k)) for k in range(t + 1)]
    assert prices == sorted(prices)

    # dp[h] is the minimum price for h selected subsets after the ranks seen.
    dp: list[Q | None] = [Q(0)] + [None] * ((1 << t) - 1)
    for capacity, price in zip(capacities, prices):
        next_dp: list[Q | None] = [None] * (1 << t)
        for old_mass, old_cost in enumerate(dp):
            if old_cost is None:
                continue
            for take in range(min(capacity, (1 << t) - 1 - old_mass) + 1):
                candidate = old_cost + take * price
                slot = old_mass + take
                if next_dp[slot] is None or candidate < next_dp[slot]:
                    next_dp[slot] = candidate
        dp = next_dp

    for mass in range(1 << t):
        remaining = mass
        greedy = Q()
        for capacity, price in zip(capacities, prices):
            take = min(remaining, capacity)
            greedy += take * price
            remaining -= take
        assert remaining == 0
        assert dp[mass] == greedy

    return {
        "t": t,
        "ambient_n": n,
        "masses_checked": 1 << t,
        "prices": list(map(str, prices)),
    }


def truncation_audit() -> dict[str, object]:
    """Check exact full-profile recovery, telescoping, and concentration."""
    n, middle, t, r = 64, 32, 16, 4
    ambient = sum(comb(n, k) for k in range(r + 1))

    lifted = sum(
        Q(comb(t, k)) * Q(comb(n, k), comb(t, k))
        for k in range(r + 1)
    )
    assert lifted == ambient

    for k in range(r + 1):
        direct = Q(comb(n, k), comb(t, k))
        two_step = Q(comb(n, k), comb(middle, k)) * Q(
            comb(middle, k), comb(t, k)
        )
        assert direct == two_step

    concentration = []
    previous_deficit = None
    for t0, r0 in [(16, 2), (64, 3), (256, 4), (1024, 5)]:
        masses = [comb(t0, k) for k in range(r0 + 1)]
        total = sum(masses)
        mean = Q(sum(k * masses[k] for k in range(r0 + 1)), total)
        variance = sum(
            Q(masses[k], total) * (Q(k) - mean) ** 2
            for k in range(r0 + 1)
        )
        deficit = Q(r0) - mean
        assert 0 < deficit < 1
        assert 0 < variance < 1
        if previous_deficit is not None:
            assert deficit < previous_deficit
        previous_deficit = deficit
        concentration.append(
            {
                "t": t0,
                "r": r0,
                "deficit": str(deficit),
                "variance": str(variance),
            }
        )

    return {
        "parameters": (n, middle, t, r),
        "ambient_faces": ambient,
        "lifted_faces": int(lifted),
        "concentration": concentration,
    }


def main() -> None:
    result = {
        "planar_hypergeometric": planar_hypergeometric_audit(),
        "profile_fixed_point": profile_fixed_point_audit(),
        "tail_threshold": tail_threshold_audit(),
        "greedy_rank_allocation": greedy_rank_allocation_audit(),
        "complete_truncation": truncation_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: exact two-scale full-rank recurrence and 1/4 barrier verified")


if __name__ == "__main__":
    main()
