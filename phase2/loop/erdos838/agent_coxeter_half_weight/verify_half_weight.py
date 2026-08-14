#!/usr/bin/env python3
"""Exact verifier for the saved unrestricted half-weight braid records."""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "agent_reflection_gate"))
import reflection_order_gate as gate  # noqa: E402


def product(n: int, roots, value: Fraction, derivative: bool = False):
    rows = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    ders = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i, j in roots:
        old_row = rows[j]
        old_der = ders[j]
        rows[j] = [x + value * y for x, y in zip(old_row, rows[i])]
        ders[j] = [x + y + value * z for x, y, z in zip(old_der, rows[i], ders[i])]
    return (rows, ders) if derivative else rows


def exact_record(path: Path) -> dict[str, object]:
    raw = json.loads(path.read_text())
    n = int(raw["n"])
    word = tuple(map(int, raw["word_zero_based"]))
    roots = gate.root_sequence(n, word)
    if gate.word_from_roots(n, roots) != word:
        raise AssertionError("word/root round trip failed")

    q_values = {}
    data = {}
    for key, z in (("one", Fraction(1)), ("half", Fraction(1, 2))):
        cups, dcups = product(n, roots, z, derivative=True)
        caps, dcaps = product(n, tuple(reversed(roots)), z, derivative=True)
        q = sum(
            (cups[i][j] * caps[i][j] for i in range(n) for j in range(n)),
            Fraction(0),
        )
        qprime = sum(
            (
                dcups[i][j] * caps[i][j] + cups[i][j] * dcaps[i][j]
                for i in range(n)
                for j in range(n)
            ),
            Fraction(0),
        )
        f = 1 + n * z + q - n
        fprime = n + qprime
        mu = z * fprime / f
        q_values[key] = q
        data[key] = {
            "F": [f.numerator, f.denominator],
            "Q": [q.numerator, q.denominator],
            "mu": [mu.numerator, mu.denominator],
        }

    f1 = Fraction(*data["one"]["F"])
    fh = Fraction(*data["half"]["F"])
    h = n * fh / f1
    if abs(float(h) - float(raw["H_full"])) > 1e-12:
        raise AssertionError("saved floating objective disagrees with exact replay")
    scope = "all_type_A; stretchability_not_claimed"
    coordinate_source = None
    if path.name.startswith("planar_seed_n"):
        saved_path = HERE.parent / "agent_dual_number_amortization" / "half_weight_search_records.json"
        saved = json.loads(saved_path.read_text())
        record = saved["exact_records"][str(n)]
        ys = tuple(map(int, record[f"y_at_x_0_through_{n-1}"]))
        slopes = sorted(
            (Fraction(ys[j] - ys[i], j - i), i, j)
            for i in range(n)
            for j in range(i + 1, n)
        )
        for first, second in zip(slopes, slopes[1:]):
            if first[0] == second[0] and len({first[1], first[2], second[1], second[2]}) < 4:
                raise AssertionError("coordinate record has a collinear triple")
        coordinate_word = gate.word_from_roots(n, tuple((i, j) for _, i, j in slopes))
        if coordinate_word != word:
            raise AssertionError("saved word does not match the exact coordinate slope order")
        scope = "fixed_x_integer_planar_certificate"
        coordinate_source = str(saved_path.relative_to(HERE.parent.parent.parent.parent))

    return {
        "n": n,
        "source": path.name,
        "root_sequence_valid": True,
        "reflection_order_scope": scope,
        "coordinate_source": coordinate_source,
        "specializations": data,
        "H": [h.numerator, h.denominator],
        "H_decimal": float(h),
        "half_mean_minus_log2_n_plus_1": float(Fraction(*data["half"]["mu"]))
        - (__import__("math").log2(n) - 1),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    paths = args.paths or [HERE / f"seeded_n{n}.json" for n in (20, 24, 30)]
    result = {
        "normalization": "F(z)=1+n*z+<A(z),B(z)>-n",
        "records": [exact_record(path) for path in paths],
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
