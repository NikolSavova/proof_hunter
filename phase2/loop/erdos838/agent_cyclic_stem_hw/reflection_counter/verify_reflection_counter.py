#!/usr/bin/env python3
"""Independent exact replay for the reflection-gadget counter search.

The verifier checks reducedness, once-per-positive-root support, unit
transvection products at activities 1 and 1/2, the full n=58 graded profile,
nested one-wire-lift counts, and the exact strand-doubling recurrence.  Use
``--full-catalog`` to rerun all 150 periodic cabling searches rather than only
their stored homogeneous and heterogeneous representatives.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from functools import cache
from pathlib import Path

import reflection_gadget_search as gadget


HERE = Path(__file__).resolve().parent


def add_shift(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * max(len(left), len(right) + 1)
    for degree, value in enumerate(left):
        out[degree] += value
    for degree, value in enumerate(right):
        out[degree + 1] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def convolution(left: tuple[int, ...], right: tuple[int, ...]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def polynomial_product(n: int, roots) -> list[list[tuple[int, ...]]]:
    matrix = [
        [(1,) if i == j else (0,) for j in range(n)] for i in range(n)
    ]
    for i, j in roots:
        matrix[j] = [
            add_shift(matrix[j][column], matrix[i][column])
            for column in range(n)
        ]
    return matrix


def graded_profile(n: int, word) -> tuple[int, ...]:
    """Compute the empty-inclusive path-pair f-vector from scratch."""
    roots = gadget.root_sequence(n, word)
    forward = polynomial_product(n, roots)
    backward = polynomial_product(n, reversed(roots))
    profile = [0]
    for i in range(n):
        for j in range(n):
            product = convolution(forward[i][j], backward[i][j])
            if len(profile) < len(product):
                profile.extend([0] * (len(product) - len(profile)))
            for degree, coefficient in enumerate(product):
                profile[degree] += coefficient
    # F(z)=1+nz+<A,B>-n.
    profile[0] += 1 - n
    if len(profile) < 2:
        profile.append(0)
    profile[1] += n
    while len(profile) > 1 and profile[-1] == 0:
        profile.pop()
    return tuple(profile)


def half_value(profile) -> Fraction:
    return sum(
        (Fraction(value, 2**degree) for degree, value in enumerate(profile)),
        Fraction(),
    )


def assert_evaluation(n: int, word, record) -> gadget.Evaluation:
    evaluation = gadget.evaluate_word(n, word)
    assert evaluation.f_half == Fraction(record["F_half"])
    assert evaluation.f_one == int(record["F_one"])
    assert evaluation.h == Fraction(record["H"])
    return evaluation


def verify_catalog(data) -> None:
    catalog = data["catalog_summary"]
    assert catalog["fixed_cabled_families"] == 150
    for family in catalog["homogeneous_representatives"]:
        macro_n = family["macro_n"]
        macro_word = tuple(family["macro_word"])
        word: gadget.Word = ()
        n = 1
        for row in family["rows"]:
            word = gadget.cable_word(
                n,
                word,
                macro_n,
                macro_word,
                phase="pre",
                sweep_bits=(0,) * len(macro_word),
            )
            n *= macro_n
            assert row["n"] == n
            assert_evaluation(n, word, row)

    for family in catalog["heterogeneous_symmetry_repeats"]:
        macro_n = family["macro_n"]
        macro_word = gadget.SMALL_RECORD_WORDS[macro_n]
        symmetries = tuple(family["inner_symmetries"])
        word = ()
        n = 1
        for expected_h in family["H_by_depth"]:
            word = gadget.cable_word(
                n,
                word,
                macro_n,
                macro_word,
                phase="pre",
                sweep_bits=(0,) * len(macro_word),
                inner_symmetries=symmetries,
            )
            n *= macro_n
            assert gadget.evaluate_word(n, word).h == Fraction(expected_h)


def lift_count(old_n: int, old_word) -> int:
    old_word = tuple(old_word)

    @cache
    def count(step: int, new_position: int) -> int:
        if step == len(old_word):
            return 1  # the remaining new-wire crossings are forced
        total = count(step, new_position - 1) if new_position else 0
        if new_position != old_word[step] + 1:
            total += count(step + 1, new_position)
        return total

    return count(0, old_n)


def verify_insertions(data) -> None:
    chain = data["nested_insertion_chain"]
    previous_roots = None
    previous_word = None
    previous_n = None
    for row in chain:
        n = row["n"]
        word = tuple(row["word_zero_based"])
        roots = gadget.root_sequence(n, word)
        assert_evaluation(n, word, row)
        if previous_roots is not None:
            restricted = tuple(root for root in roots if root[1] < n - 1)
            assert restricted == previous_roots
            assert row["extension_count"] == lift_count(previous_n, previous_word)
        previous_roots, previous_word, previous_n = roots, word, n


def strand_lift(profile, n: int) -> tuple[int, ...]:
    """Exact f-vector recurrence for replacing every wire by a two-wire cable."""
    out = [0] * (len(profile) + 2)
    out[0] = 1
    out[1] = 2 * n
    out[2] = n
    for degree, value in enumerate(profile[2:], 2):
        out[degree] += (2**degree) * value
        out[degree + 1] += (2**degree) * value
        out[degree + 2] += (2 ** (degree - 2)) * value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def verify_finite_and_strand(data) -> None:
    record = data["finite_braid_record"]
    n0 = record["n"]
    word = tuple(record["word_zero_based"])
    assert_evaluation(n0, word, record)
    profile = graded_profile(n0, word)
    assert profile == tuple(record["profile_including_empty"])
    assert sum(profile) == int(record["F_one"])
    assert half_value(profile) == Fraction(record["F_half"])
    assert profile[:4] == (1, n0, math.comb(n0, 2), math.comb(n0, 3))

    strand = data["strand_doubling"]
    n = n0
    current = profile
    for row in strand["rows"]:
        assert row["n"] == n and row["degree"] == len(current) - 1
        f_half = half_value(current)
        f_one = sum(current)
        h = Fraction(n) * f_half / f_one
        assert f_half == Fraction(row["F_half"])
        assert f_one == int(row["F_one"])
        assert h == Fraction(row["H"])
        r = math.floor(math.log2(n))
        p_r = Fraction((r + 1) * current[r + 1], (n - r) * current[r])
        assert p_r == Fraction(row["p_r"])
        assert (2**r) * p_r == Fraction(row["two_to_r_p_r"])
        current = strand_lift(current, n)
        n *= 2

    # Check the combinatorial recurrence against a literal 116-wire cable,
    # coefficient by coefficient, rather than trusting only its derivation.
    lifted_word = gadget.cable_word(
        2,
        (0,),
        n0,
        word,
        phase="pre",
        sweep_bits=(0,) * len(word),
    )
    assert graded_profile(2 * n0, lifted_word) == strand_lift(profile, n0)

    degree = len(profile) - 1
    expected_limit = Fraction(25 * n0 * n0, 2**degree)
    assert expected_limit == Fraction(strand["asymptotic_limit_N_times_H"])


def verify_full_catalog() -> None:
    result = gadget.scan_catalog(6)
    assert result["family_count"] == 150
    # Every tested stationary family has self-healed by its terminal stored
    # depth; this is an exact rational comparison, not a decimal threshold.
    assert all(Fraction(family["rows"][-1]["H"]) < 1 for family in result["families"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full-catalog", action="store_true")
    args = parser.parse_args()
    data = json.loads((HERE / "certificate.json").read_text())
    gadget.selftest()
    verify_catalog(data)
    verify_insertions(data)
    verify_finite_and_strand(data)
    if args.full_catalog:
        verify_full_catalog()
    print(
        "PASS: unit/complete roots, exact H/profile, nested lifts, "
        "and strand-doubling recurrence"
    )


if __name__ == "__main__":
    main()
