#!/usr/bin/env python3
"""Exact regressions for SUCCESSIVE_RANK_DENSITY_GAIN_GATE_20260816.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
import importlib.util
import json
from math import comb
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def orient(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def hull_size(points, subset) -> int:
    ordered = sorted(subset, key=lambda index: points[index])

    def chain(indices):
        answer = []
        for index in indices:
            while (len(answer) >= 2
                   and orient(points[answer[-2]], points[answer[-1]],
                              points[index]) <= 0):
                answer.pop()
            answer.append(index)
        return answer

    return len(chain(ordered)[:-1] + chain(reversed(ordered))[:-1])


def face_profile(points) -> list[int]:
    size = len(points)
    profile = [0] * (size + 1)
    for rank in range(1, size + 1):
        if rank <= 2:
            profile[rank] = comb(size, rank)
        else:
            profile[rank] = sum(
                hull_size(points, subset) == rank
                for subset in combinations(range(size), rank)
            )
    return profile


def face_count(points, rank: int) -> int:
    if rank <= 2:
        return comb(len(points), rank)
    return sum(
        hull_size(points, subset) == rank
        for subset in combinations(range(len(points)), rank)
    )


def density_ratio(profile: list[int], size: int, rank: int) -> Fraction:
    """Return p_(rank+1)/p_rank exactly."""
    return Fraction(
        (rank + 1) * profile[rank + 1],
        (size - rank) * profile[rank],
    )


def audit_bridge() -> int:
    checks = 0
    for alpha_num in range(1, 10):
        alpha = Fraction(alpha_num, 10)
        for c_num in range(1, 20):
            c = Fraction(c_num, 10)
            eta = (1 - c / 2) * (1 - alpha * alpha)
            sigma = 2 - alpha * alpha - c * (1 - alpha * alpha) / 2
            assert sigma == 1 + eta
            assert eta > 0
            assert Fraction(1, 4) + eta / 4 > Fraction(1, 4)
            checks += 1
    return checks


def audit_finite_point_sets() -> tuple[Fraction, Fraction, int]:
    five = [
        (Fraction(6), Fraction(15)),
        (Fraction(18), Fraction(22)),
        (Fraction(13), Fraction(4)),
        (Fraction(12), Fraction(17)),
        (Fraction(20), Fraction(29)),
    ]
    profile_five = face_profile(five)
    assert profile_five[1:] == [5, 10, 10, 1, 0]
    assert density_ratio(profile_five, 5, 4) == 0

    stored = []
    for filename in (
        "exact_realizable_n8_independent.json",
        "exact_realizable_n9.json",
    ):
        data = json.loads(
            (HERE / "agent_lex_minimizer_search" / filename).read_text()
        )
        points = [tuple(map(Fraction, point))
                  for point in data["coordinates_as_stored"]]
        profile = face_profile(points)
        assert profile == data["profile"]
        stored.append((len(points), profile))

    minimum_ratio = None
    checks = 0
    for size, profile in stored:
        for rank in range(3, size):
            if size < 2**rank or profile[rank] == 0:
                continue
            ratio = density_ratio(profile, size, rank) * 2**rank
            assert ratio >= 1
            minimum_ratio = ratio if minimum_ratio is None else min(
                minimum_ratio, ratio
            )
            checks += 1
    assert minimum_ratio is not None
    return minimum_ratio, density_ratio(profile_five, 5, 4), checks


def double_chain(m: int):
    """A rational, general-position double chain on 2m points."""
    denominator = 4 * m * m
    upper = [
        (Fraction(2 * index),
         Fraction(2) + Fraction(index * index, denominator))
        for index in range(m)
    ]
    lower = [
        (Fraction(2 * index + 1),
         -Fraction(2) - Fraction(index * index, denominator))
        for index in range(m)
    ]
    return upper + lower


def audit_double_chain() -> tuple[int, Fraction, Fraction]:
    checks = 0
    first_ratio = None
    minimum_later_ratio = None
    for m in range(5, 13):
        points = double_chain(m)
        counts = {
            rank: face_count(points, rank)
            for rank in range(4, min(m, 8) + 1)
        }
        assert counts[4] == 2 * comb(m, 4) + comb(m, 2) ** 2
        assert counts[5] == 2 * comb(m, 5)
        for rank in range(6, min(m, 8) + 1):
            assert counts[rank] == 2 * comb(m, rank)
        checks += 1

        if m == 8:
            assert (counts[4], counts[5]) == (924, 112)
            first_ratio = Fraction(
                5 * counts[5], (2 * m - 4) * counts[4]
            )
            assert first_ratio == Fraction(5, 99)
            assert 16 * first_ratio == Fraction(80, 99) < 1
            assert first_ratio > Fraction(1, 64)  # c=3/2 still works.

        for rank in range(5, min(m, 8)):
            ratio = Fraction(
                (rank + 1) * counts[rank + 1],
                (2 * m - rank) * counts[rank],
            )
            assert ratio == Fraction(m - rank, 2 * m - rank)
            minimum_later_ratio = ratio if minimum_later_ratio is None else min(
                minimum_later_ratio, ratio
            )
            checks += 1

    assert first_ratio is not None and minimum_later_ratio is not None
    return checks, first_ratio, minimum_later_ratio


def audit_strong_trees() -> tuple[int, Fraction]:
    trees_module = load(
        "uniform_caterpillar_for_density",
        HERE / "verify_uniform_growing_rank_caterpillar.py",
    )
    checks = 0
    minimum_ratio = None
    for size in range(8, 12):
        for tree in trees_module.trees(size):
            profile = trees_module.ordinary_profiles(tree)[2]
            for rank in range(3, size):
                if size < 2**rank:
                    continue
                ratio = Fraction(
                    (rank + 1) * profile[rank + 1] * 2**rank,
                    (size - rank) * profile[rank],
                )
                assert ratio >= 1
                minimum_ratio = ratio if minimum_ratio is None else min(
                    minimum_ratio, ratio
                )
                checks += 1
    assert minimum_ratio is not None
    return checks, minimum_ratio


def audit_pascal() -> tuple[int, Fraction]:
    graded = load(
        "graded_balanced_for_density",
        HERE / "agent_graded_supersat" / "graded_balanced.py",
    )
    template = graded.pascal_row(4, 6)[2]
    checks = 0
    minimum_ratio = None
    for depth in range(1, 15):
        size, _, _, profile = graded.vertical_iterate(
            template, depth, 4 * depth + 3
        )
        for rank in range(3, min(len(profile) - 1, size)):
            if size < 2**rank or profile[rank] == 0:
                continue
            ratio = Fraction(
                (rank + 1) * profile[rank + 1] * 2**rank,
                (size - rank) * profile[rank],
            )
            assert ratio >= 1
            minimum_ratio = ratio if minimum_ratio is None else min(
                minimum_ratio, ratio
            )
            checks += 1
    assert minimum_ratio is not None
    return checks, minimum_ratio


def main() -> None:
    bridge_checks = audit_bridge()
    finite_minimum, threshold_kill, finite_checks = audit_finite_point_sets()
    double_checks, double_kill, double_later = audit_double_chain()
    tree_checks, tree_minimum = audit_strong_trees()
    pascal_checks, pascal_minimum = audit_pascal()
    print(
        "PASS: successive-rank density gain gate; "
        f"bridge_checks={bridge_checks}; finite_checks={finite_checks}; "
        f"double_chain_checks={double_checks}; "
        f"tree_checks={tree_checks}; pascal_checks={pascal_checks}; "
        f"threshold_kill={threshold_kill}; double_chain_kill={double_kill}; "
        f"double_chain_later_min={double_later}; "
        f"minimum_ratios=({finite_minimum},{tree_minimum},{pascal_minimum})"
    )


if __name__ == "__main__":
    main()
