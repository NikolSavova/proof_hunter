#!/usr/bin/env python3
"""Exact finite audit for the local-peak compensation target."""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PLATEAU = ROOT / "agent_global_braid_plateau"
sys.path.insert(0, str(PLATEAU))

import plateau_census as plateau  # noqa: E402


PROFILES = {
    20: (1, 20, 190, 1140, 2415, 866, 135, 8),
    24: (1, 24, 276, 2024, 5378, 2679, 413, 43, 3),
    30: (1, 30, 435, 4060, 13975, 10607, 3158, 481, 30),
    44: (1, 44, 946, 13244, 70450, 99093, 43597, 8726, 1075, 53),
    58: (
        1, 58, 1653, 30856, 220958, 428915,
        284982, 76995, 15100, 2179, 210,
    ),
}


def statistic(profile: tuple[int, ...]) -> tuple[Fraction, Fraction, Fraction]:
    n = profile[1]
    value = sum(profile)
    half = sum(
        (Fraction(count, 2**rank) for rank, count in enumerate(profile)),
        Fraction(),
    )
    moment = sum(rank * count for rank, count in enumerate(profile))
    half_moment = sum(
        (Fraction(rank * count, 2**rank) for rank, count in enumerate(profile)),
        Fraction(),
    )
    h_value = Fraction(n) * half / value
    delta = Fraction(moment, value) - half_moment / half
    compensation = h_value * max(Fraction(), 1 - delta)
    return h_value, delta, compensation


def main() -> None:
    expected = {
        2: Fraction(3, 4),
        3: Fraction(81, 128),
        4: Fraction(26, 45),
        5: Fraction(85, 162),
        6: Fraction(331, 600),
        7: Fraction(47_705, 85_264),
    }
    for n in range(2, 8):
        words, _, evaluations = plateau.enumerate_graph(n)
        maximum = Fraction()
        for word in words:
            graded = evaluations[word].graded
            assert graded is not None
            profile = (1,) + tuple(graded[1:])
            maximum = max(maximum, statistic(profile)[2])
        assert maximum == expected[n]
        print(f"n={n} classes={len(words)} max={maximum} ({float(maximum):.12f})")

    expected_decimals = {
        20: 0.7329302239521943,
        24: 0.7936311960943775,
        30: 0.7156253376633960,
        44: 0.7424190358093744,
        58: 0.6819525006141831,
    }
    for n, profile in PROFILES.items():
        h_value, delta, compensation = statistic(profile)
        assert abs(float(compensation) - expected_decimals[n]) < 1e-15
        assert compensation < 1
        print(
            f"record n={n} H={float(h_value):.12f} "
            f"delta={float(delta):.12f} comp={float(compensation):.12f}"
        )

    # The complete-three-skeleton truncation is an exact generic-downset
    # barrier: its compensation grows linearly.
    n = 100
    truncated = (1, n, n * (n - 1) // 2, n * (n - 1) * (n - 2) // 6)
    assert statistic(truncated)[2] > 12
    print("local compensation audit: PASS")


if __name__ == "__main__":
    main()
