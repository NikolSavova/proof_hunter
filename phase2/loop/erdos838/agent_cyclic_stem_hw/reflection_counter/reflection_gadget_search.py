#!/usr/bin/env python3
"""Exact search for repeatable gadgets in unit type-A reflection orders.

The objects are reduced words for the longest permutation.  Every positive
root therefore appears exactly once, with unit transvection weight.  Besides
checking arbitrary supplied words, this script constructs block-cabled words:
copies of an inner sorting network are placed before or after a macro sorting
network, and every macro crossing is expanded to a row- or column-sweep of the
rectangular crossing grid.

All reported partition functions are evaluated with Python integers and
Fractions.  Floating point is used only to print logarithms of exact values.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Iterator, Sequence


Word = tuple[int, ...]
Root = tuple[int, int]


def bubble_word(n: int) -> Word:
    return tuple(i for top in range(1, n) for i in range(top - 1, -1, -1))


def root_sequence(n: int, word: Sequence[int]) -> tuple[Root, ...]:
    """Validate a reduced word for w0 and return its once-per-root order."""
    wires = list(range(n))
    roots: list[Root] = []
    for step, generator in enumerate(word):
        if not 0 <= generator < n - 1:
            raise ValueError(f"invalid generator {generator} at step {step}")
        a, b = wires[generator : generator + 2]
        if a > b:
            raise ValueError(f"nonreduced crossing at step {step}: {(a, b)}")
        roots.append((a, b))
        wires[generator], wires[generator + 1] = b, a
    expected = n * (n - 1) // 2
    if len(word) != expected or wires != list(reversed(range(n))):
        raise ValueError("word is not a reduced decomposition of w0")
    if len(set(roots)) != expected:
        raise AssertionError("a positive root was repeated")
    return tuple(roots)


def matrix_at(n: int, roots: Iterable[Root], z: Fraction) -> list[list[Fraction]]:
    matrix = [[Fraction(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        row_i = matrix[i]
        row_j = matrix[j]
        matrix[j] = [a + z * b for a, b in zip(row_j, row_i)]
    return matrix


def partition_at(n: int, roots: Sequence[Root], z: Fraction) -> Fraction:
    forward = matrix_at(n, roots, z)
    backward = matrix_at(n, reversed(roots), z)
    raw_trace = sum(
        forward[i][j] * backward[i][j] for i in range(n) for j in range(n)
    )
    return 1 + n * z + raw_trace - n


def partition_at_half_dyadic(n: int, roots: Sequence[Root]) -> Fraction:
    """Evaluate F(1/2) with one common power-of-two denominator.

    Every path entering row ``i`` has at most ``i`` edges.  Scaling every
    entry by ``2**n`` therefore makes ``row_i / 2`` integral whenever it is
    used to update a later row.  This is exactly equivalent to Fraction
    arithmetic and is much faster in the substitution scans.
    """
    scale = 1 << n

    def product(order: Iterable[Root]) -> list[list[int]]:
        matrix = [[scale * int(i == j) for j in range(n)] for i in range(n)]
        for i, j in order:
            row_i = matrix[i]
            if any(value & 1 for value in row_i):
                raise AssertionError("insufficient dyadic scale")
            row_j = matrix[j]
            matrix[j] = [a + (b >> 1) for a, b in zip(row_j, row_i)]
        return matrix

    forward = product(roots)
    backward = product(reversed(roots))
    denominator = scale * scale
    numerator = sum(
        forward[i][j] * backward[i][j] for i in range(n) for j in range(n)
    )
    numerator += (2 - n) * denominator // 2
    return Fraction(numerator, denominator)


@dataclass(frozen=True)
class Evaluation:
    n: int
    f_half: Fraction
    f_one: int

    @property
    def h(self) -> Fraction:
        return self.n * self.f_half / self.f_one

    @property
    def exponent(self) -> float:
        """log_n H; a positive limit would refute H=n^{o(1)}."""
        return math.log2(float(self.h)) / math.log2(self.n)

    def record(self) -> dict[str, object]:
        return {
            "n": self.n,
            "F_half": str(self.f_half),
            "F_one": str(self.f_one),
            "H": str(self.h),
            "H_decimal": float(self.h),
            "log_n_H": self.exponent,
        }


def evaluate_word(n: int, word: Sequence[int]) -> Evaluation:
    roots = root_sequence(n, word)
    f_half = partition_at_half_dyadic(n, roots)
    f_one = partition_at(n, roots, Fraction(1))
    if f_one.denominator != 1:
        raise AssertionError("F(1) is not integral")
    return Evaluation(n, f_half, f_one.numerator)


def transform_word(word: Sequence[int], n: int, symmetry: str) -> Word:
    """The four elementary reduced-word symmetries of w0."""
    if symmetry not in {"id", "reverse", "mirror", "reverse_mirror"}:
        raise ValueError(symmetry)
    out = tuple(word)
    if "reverse" in symmetry:
        out = tuple(reversed(out))
    if "mirror" in symmetry:
        out = tuple(n - 2 - generator for generator in out)
    root_sequence(n, out)
    return out


def block_swap_word(block_size: int, offset: int, sweep: str) -> Word:
    """Swap two adjacent equal blocks, preserving order inside each block."""
    if sweep == "row":
        # Move right-block wires left, one at a time.
        return tuple(
            offset + position
            for right_index in range(block_size)
            for position in range(block_size + right_index - 1, right_index - 1, -1)
        )
    if sweep == "column":
        # Move left-block wires right, one at a time.
        return tuple(
            offset + position
            for left_index in range(block_size - 1, -1, -1)
            for position in range(left_index, left_index + block_size)
        )
    raise ValueError(sweep)


def cable_word(
    inner_n: int,
    inner_word: Sequence[int],
    macro_n: int,
    macro_word: Sequence[int],
    *,
    phase: str,
    sweep_bits: Sequence[int] = (),
    inner_symmetries: Sequence[str] = (),
) -> Word:
    """Inflate each macro wire to an ``inner_n``-wire sorting network.

    ``phase`` places all commuting internal networks before or after all
    expanded macro crossings.  A bit selects row (0) or column (1) sweep for
    each macro crossing.  Internal copies may independently use a word
    symmetry; this is useful for finite-state gadget searches.
    """
    root_sequence(inner_n, inner_word)
    root_sequence(macro_n, macro_word)
    if phase not in {"pre", "post"}:
        raise ValueError(phase)
    if not sweep_bits:
        sweep_bits = (0,) * len(macro_word)
    if len(sweep_bits) != len(macro_word):
        raise ValueError("one sweep bit is required per macro crossing")
    if not inner_symmetries:
        inner_symmetries = ("id",) * macro_n
    if len(inner_symmetries) != macro_n:
        raise ValueError("one internal symmetry is required per macro block")

    internals: list[int] = []
    for block_position, symmetry in enumerate(inner_symmetries):
        local = transform_word(inner_word, inner_n, symmetry)
        internals.extend(block_position * inner_n + generator for generator in local)

    crossings: list[int] = []
    for generator, bit in zip(macro_word, sweep_bits):
        crossings.extend(
            block_swap_word(inner_n, generator * inner_n, "column" if bit else "row")
        )

    result = tuple(internals + crossings if phase == "pre" else crossings + internals)
    root_sequence(inner_n * macro_n, result)
    return result


def insert_extensions(old_n: int, old_word: Sequence[int]) -> Iterator[Word]:
    """Enumerate lifts to ``w0`` on one extra, initially rightmost, wire.

    Deleting the new wire from every returned sorting network recovers
    ``old_word`` exactly.  At a state, either the next old crossing is made
    (unless the new wire separates its two participants), or the new largest
    wire crosses its current left neighbor.  This is a complete enumeration
    of such one-wire lifts.
    """
    root_sequence(old_n, old_word)
    prefix: list[int] = []

    def visit(old_step: int, new_position: int) -> Iterator[Word]:
        if old_step == len(old_word) and new_position == 0:
            candidate = tuple(prefix)
            root_sequence(old_n + 1, candidate)
            yield candidate
            return

        if new_position > 0:
            prefix.append(new_position - 1)
            yield from visit(old_step, new_position - 1)
            prefix.pop()

        if old_step < len(old_word):
            generator = old_word[old_step]
            # The new wire lies between the adjacent old positions exactly at
            # this gap, and then the old crossing is temporarily unavailable.
            if new_position != generator + 1:
                full_generator = generator + int(new_position <= generator)
                prefix.append(full_generator)
                yield from visit(old_step + 1, new_position)
                prefix.pop()

    yield from visit(0, old_n)


def greedy_insertion_chain(start_n: int, stop_n: int) -> dict[str, object]:
    if start_n not in SMALL_RECORD_WORDS or stop_n < start_n:
        raise ValueError("start from one of the stored sizes 2..7")
    n = start_n
    word = SMALL_RECORD_WORDS[n]
    rows: list[dict[str, object]] = [
        {"extension_count": 1, "word_zero_based": list(word), **evaluate_word(n, word).record()}
    ]
    while n < stop_n:
        best_word: Word | None = None
        best_eval: Evaluation | None = None
        count = 0
        for candidate in insert_extensions(n, word):
            count += 1
            evaluation = evaluate_word(n + 1, candidate)
            if best_eval is None or evaluation.h > best_eval.h:
                best_word, best_eval = candidate, evaluation
        if best_word is None or best_eval is None:
            raise AssertionError("one-wire lift enumeration was empty")
        n += 1
        word = best_word
        rows.append(
            {
                "extension_count": count,
                "word_zero_based": list(word),
                "root_sequence_zero_based": [list(root) for root in root_sequence(n, word)],
                **best_eval.record(),
            }
        )
    return {
        "model": "greedy maximum-H nested one-wire lifts",
        "start_n": start_n,
        "stop_n": stop_n,
        "rows": rows,
    }


SMALL_RECORD_WORDS: dict[int, Word] = {
    2: (0,),
    3: (0, 1, 0),
    4: (0, 1, 2, 1, 0, 1),
    5: (0, 1, 2, 1, 3, 2, 1, 0, 1, 2),
    6: (0, 1, 2, 3, 2, 4, 3, 2, 1, 0, 2, 1, 2, 3, 2),
    7: (0, 1, 2, 3, 2, 4, 3, 5, 4, 3, 2, 1, 0, 2, 3, 2, 1, 2, 3, 4, 3),
}


def iterate_fixed_gadget(
    macro_n: int,
    macro_word: Word,
    depth: int,
    phase_pattern: str,
    sweep_pattern: str,
) -> list[dict[str, object]]:
    if not phase_pattern or set(phase_pattern) - {"0", "1"}:
        raise ValueError("phase pattern must be a nonempty 0/1 string")
    if not sweep_pattern or set(sweep_pattern) - {"0", "1"}:
        raise ValueError("sweep pattern must be a nonempty 0/1 string")
    word: Word = ()
    n = 1
    rows: list[dict[str, object]] = []
    for level in range(1, depth + 1):
        phase = "pre" if phase_pattern[(level - 1) % len(phase_pattern)] == "0" else "post"
        bits = tuple(
            int(sweep_pattern[k % len(sweep_pattern)]) for k in range(len(macro_word))
        )
        word = cable_word(n, word, macro_n, macro_word, phase=phase, sweep_bits=bits)
        n *= macro_n
        evaluation = evaluate_word(n, word)
        row = {"level": level, "phase": phase, **evaluation.record()}
        rows.append(row)
    return rows


def scan_catalog(max_depth: int) -> dict[str, object]:
    families: list[dict[str, object]] = []
    # These periodic choices cover homogeneous, alternating, and short cyclic
    # schedules without presenting heuristic output as an exhaustive theorem.
    phase_patterns = ("0", "1", "01", "001", "011")
    sweep_patterns = ("0", "1", "01", "001", "011")
    for macro_n, macro_word in SMALL_RECORD_WORDS.items():
        # Keep exact big-integer matrix arithmetic moderate: n <= 128.
        depth = min(max_depth, max(1, int(math.log(128, macro_n))))
        for phase_pattern in phase_patterns:
            for sweep_pattern in sweep_patterns:
                rows = iterate_fixed_gadget(
                    macro_n, macro_word, depth, phase_pattern, sweep_pattern
                )
                families.append(
                    {
                        "macro_n": macro_n,
                        "macro_word": list(macro_word),
                        "phase_pattern": phase_pattern,
                        "sweep_pattern": sweep_pattern,
                        "rows": rows,
                    }
                )
    families.sort(key=lambda family: family["rows"][-1]["H_decimal"], reverse=True)
    return {
        "model": "unit complete once-per-positive-root type-A reflection orders",
        "family_count": len(families),
        "families": families,
    }


def selftest() -> None:
    expected = {
        3: Fraction(81, 64),
        4: Fraction(4, 3),
        5: Fraction(65, 48),
        6: Fraction(167, 120),
        7: Fraction(1645, 1168),
    }
    for n, target in expected.items():
        got = evaluate_word(n, SMALL_RECORD_WORDS[n]).h
        if got != target:
            raise AssertionError(f"small record n={n}: got {got}, expected {target}")

    for size in range(1, 7):
        for sweep in ("row", "column"):
            word = block_swap_word(size, 0, sweep)
            # It sorts the binary parabolic quotient; after internal reversals
            # cable_word is responsible for the full w0 check.
            if len(word) != size * size:
                raise AssertionError("wrong rectangular gadget length")

    # A mixed-schedule cable is independently subjected to the full reduced
    # word/once-per-root validator.
    mixed = cable_word(
        5,
        SMALL_RECORD_WORDS[5],
        3,
        SMALL_RECORD_WORDS[3],
        phase="post",
        sweep_bits=(0, 1, 0),
        inner_symmetries=("id", "reverse", "mirror"),
    )
    root_sequence(15, mixed)
    print("selftest: exact small H records and mixed cable validation PASS")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--scan", type=Path)
    parser.add_argument("--max-depth", type=int, default=6)
    parser.add_argument("--insert-chain", type=Path)
    parser.add_argument("--insert-start", type=int, default=7)
    parser.add_argument("--insert-stop", type=int, default=8)
    args = parser.parse_args()
    if args.selftest:
        selftest()
    if args.scan is not None:
        result = scan_catalog(args.max_depth)
        args.scan.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        for family in result["families"][:12]:
            last = family["rows"][-1]
            print(
                f"r={family['macro_n']} phase={family['phase_pattern']} "
                f"sweep={family['sweep_pattern']} n={last['n']} "
                f"H={last['H_decimal']:.12g} log_n(H)={last['log_n_H']:.6g}"
            )
    if args.insert_chain is not None:
        result = greedy_insertion_chain(args.insert_start, args.insert_stop)
        args.insert_chain.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        for row in result["rows"]:
            print(
                f"insert n={row['n']} candidates={row['extension_count']} "
                f"H={row['H_decimal']:.12g} log_n(H)={row['log_n_H']:.6g}"
            )
    if not args.selftest and args.scan is None and args.insert_chain is None:
        parser.error("choose --selftest, --scan PATH, and/or --insert-chain PATH")


if __name__ == "__main__":
    main()
