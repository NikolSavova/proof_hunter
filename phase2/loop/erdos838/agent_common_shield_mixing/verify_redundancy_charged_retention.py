#!/usr/bin/env python3
"""Audit for REDUNDANCY_CHARGED_SEMIALGEBRAIC_RETENTION.md."""

from __future__ import annotations

import json
import math
import random
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product


Point = tuple[int, int]


def parabola(t: int) -> Point:
    return (t, t * t)


def orientation(a: Point, b: Point, c: Point) -> int:
    det = (b[0] - a[0]) * (c[1] - a[1]) - (
        b[1] - a[1]
    ) * (c[0] - a[0])
    return (det > 0) - (det < 0)


def entropy(probabilities: list[float]) -> float:
    return -sum(p * math.log2(p) for p in probabilities if p > 0)


def marginal(
    law: dict[tuple[int, ...], Q], coordinates: tuple[int, ...]
) -> dict[tuple[int, ...], Q]:
    result: dict[tuple[int, ...], Q] = defaultdict(Q)
    for word, probability in law.items():
        result[tuple(word[i] for i in coordinates)] += probability
    return dict(result)


def entropy_of_law(law: dict[tuple[int, ...], Q]) -> float:
    return entropy([float(value) for value in law.values()])


def total_correlation(law: dict[tuple[int, ...], Q]) -> float:
    arity = len(next(iter(law)))
    return sum(
        entropy_of_law(marginal(law, (i,))) for i in range(arity)
    ) - entropy_of_law(law)


def conditional_law(
    law: dict[tuple[int, ...], Q],
    label_fn,
    chosen_label: tuple[int, ...],
) -> dict[tuple[int, ...], Q]:
    mass = sum(p for word, p in law.items() if label_fn(word) == chosen_label)
    return {
        word: p / mass
        for word, p in law.items()
        if label_fn(word) == chosen_label
    }


def entropy_telescope_audit() -> dict[str, object]:
    rng = random.Random(83820260815)
    minimum_slack = float("inf")
    trials = 80
    for _ in range(trials):
        weights = {
            word: Q(rng.randint(1, 30), 1)
            for word in product(range(4), repeat=3)
        }
        total = sum(weights.values(), Q())
        law = {word: weight / total for word, weight in weights.items()}

        # Coordinate-wise deterministic labels, as in a product partition.
        cuts = [rng.randint(1, 3) for _ in range(3)]

        def labels(word: tuple[int, ...]) -> tuple[int, ...]:
            return tuple(int(word[i] >= cuts[i]) for i in range(3))

        label_law: dict[tuple[int, ...], Q] = defaultdict(Q)
        for word, probability in law.items():
            label_law[labels(word)] += probability
        label_law = dict(label_law)

        expected_child_tc = 0.0
        for label, probability in label_law.items():
            child = conditional_law(law, labels, label)
            expected_child_tc += float(probability) * total_correlation(child)

        parent_tc = total_correlation(law)
        label_tc = total_correlation(label_law)
        slack = parent_tc - label_tc - expected_child_tc
        assert slack >= -2e-12
        minimum_slack = min(minimum_slack, slack)

    return {"trials": trials, "minimum_entropy_telescope_slack": minimum_slack}


def consecutive_tc_audit() -> dict[str, object]:
    rng = random.Random(150201730)
    minimum_slack = float("inf")
    trials = 80
    rank = 7
    words = tuple(product(range(2), repeat=rank))
    for _ in range(trials):
        raw = {word: Q(rng.randint(0, 12), 1) for word in words}
        raw = {word: value for word, value in raw.items() if value}
        total = sum(raw.values(), Q())
        law = {word: value / total for word, value in raw.items()}
        global_tc = total_correlation(law)
        local_sum = 0.0
        for start in range(rank - 2):
            local_sum += total_correlation(
                marginal(law, (start, start + 1, start + 2))
            )
        slack = 2 * global_tc - local_sum
        assert slack >= -2e-12
        minimum_slack = min(minimum_slack, slack)
    return {
        "rank": rank,
        "trials": trials,
        "minimum_two_global_minus_local_sum": minimum_slack,
    }


def tree_mass_audit() -> dict[str, object]:
    # An abstract finite recursion tree.  Every low node sends <=1/2 of its
    # mass to internal children; high nodes send <= all of it.  The report's
    # algebra predicts low internal mass <=2 and I<=2+H.
    rng = random.Random(404108)
    worst_low = 0.0
    worst_slack = float("inf")
    for _ in range(100):
        current = [(1.0, 0)]
        low_mass = 0.0
        high_mass = 0.0
        for depth in range(30):
            following = []
            for mass, _ in current:
                high = rng.random() < 0.32
                if high:
                    high_mass += mass
                    theta = rng.uniform(0.5, 0.92)
                else:
                    low_mass += mass
                    theta = rng.uniform(0.0, 0.5)
                child_mass = mass * theta
                split = rng.random()
                if child_mass > 1e-14:
                    following.append((child_mass * split, depth + 1))
                    following.append((child_mass * (1 - split), depth + 1))
            current = following
        internal = low_mass + high_mass
        slack = 2 + high_mass - internal
        assert low_mass <= 2 + 1e-10
        assert slack >= -1e-10
        worst_low = max(worst_low, low_mass)
        worst_slack = min(worst_slack, slack)
    return {
        "maximum_low_internal_mass": worst_low,
        "minimum_I_bound_slack": worst_slack,
    }


def cover_barrier_audit() -> dict[str, object]:
    rows = []
    for alphabet in (4, 8, 16, 32):
        family = [
            (parabola(3 * a), parabola(3 * b + 1), parabola(3 * c + 2))
            for a in range(alphabet)
            for b in range(a, alphabet)
            for c in range(b, alphabet)
        ]
        expected = math.comb(alphabet + 2, 3)
        assert len(family) == expected
        assert all(orientation(*triple) > 0 for triple in family)

        distinguished = [
            (parabola(3 * i), parabola(3 * i + 1), parabola(3 * alphabet - 1))
            for i in range(alphabet - 1)
        ]
        family_set = set(family)
        assert all(edge in family_set for edge in distinguished)
        pair_checks = 0
        for i in range(len(distinguished)):
            for j in range(i + 1, len(distinguished)):
                mixed = (
                    distinguished[j][0],
                    distinguished[i][1],
                    distinguished[i][2],
                )
                assert orientation(*mixed) < 0
                pair_checks += 1

        density = Q(expected, alphabet**3)
        assert density > Q(1, 6)
        assert density <= 1
        rows.append(
            {
                "alphabet": alphabet,
                "family": expected,
                "distinguished": len(distinguished),
                "pair_checks": pair_checks,
                "redundancy_bits": math.log2(1 / float(density)),
            }
        )
    return {"scales": rows}


def constant_audit() -> dict[str, float]:
    c0 = 0.5 * math.log2(Q(4, 3))
    direct = 0.5 * math.log2(0.5 / 0.25) + 0.5 * math.log2(0.5 / 0.75)
    assert abs(c0 - direct) < 1e-15
    assert c0 > 0.2
    return {"binary_kl_c0": c0}


def main() -> None:
    result = {
        "constant": constant_audit(),
        "entropy_telescope": entropy_telescope_audit(),
        "consecutive_total_correlation": consecutive_tc_audit(),
        "tree_mass": tree_mass_audit(),
        "cover_barrier": cover_barrier_audit(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: redundancy-charged retention audit verified")


if __name__ == "__main__":
    main()
