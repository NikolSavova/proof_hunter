#!/usr/bin/env python3
"""Checks for MACRO_RUN_PROFILE_SPECTRUM_WIDTH_GATE.md."""

import argparse
from fractions import Fraction
from itertools import product
from pathlib import Path
import re
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent


def abstract_width_gate():
    checked = 0
    menus = [
        [(4, 18), (7, 11), (15, 5)],
        [(10, 40), (20, 20), (40, 10)],
        [(9, 90), (27, 30), (81, 10)],
    ]
    for menu in menus:
        H = min(c * u for c, u in menu)
        cmin = min(c for c, _ in menu)
        cmax = max(c for c, _ in menu)
        for D in (5, 9):
            A = D + 1
            for q in range(2, 6):
                for word in product(menu, repeat=q):
                    first, last = word[0], word[-1]
                    actual = first[0] * last[1] * A ** (q - 2)
                    lower = Fraction(H * cmin * A ** (q - 2), cmax)
                    assert actual >= lower
                    checked += 1
    return checked


def exact_44_gate():
    # These are the full-spectrum values certified independently by
    # verify_pareto_two_level_recursive_menu.py.
    D, H = 44, 747670
    cmin, cmax, q = 15121, 102449, 3
    assert (D + 1) * cmin > 2 * q * cmax
    lower = Fraction(H * (D + 1) * cmin, cmax)
    assert lower > 2 * q * H
    return lower


def association_audit():
    # A≺B exact binary strong-glue recurrence. Product weights occur on
    # opposite marginals for the two associations; they cannot be combined.
    def glue(left, right):
        n, C, U, W = left
        m, D, V, Z = right
        return (n + m,
                D + (m + 1) * C,
                U + (n + 1) * V,
                W + Z + C * V)

    children = [(4, 13, 11, 14),
                (4, 11, 13, 14),
                (4, 12, 12, 15)]
    right = glue(children[0], glue(children[1], children[2]))
    left = glue(glue(children[0], children[1]), children[2])
    assert right == (12, 184, 376, 1124)
    assert left == (12, 392, 184, 1124)
    mixed = (left[1], right[2])
    assert mixed == (392, 376)
    assert mixed not in {(right[1], right[2]), (left[1], left[2])}
    return right, left


def sampled_dp(input_path):
    with tempfile.TemporaryDirectory(prefix="proof_hunter_ramp_") as tmp:
        binary = Path(tmp) / "macro_dp"
        subprocess.run(
            [
                "clang++",
                "-O3",
                "-std=c++17",
                str(HERE / "explore_macro_run_profile_dp.cpp"),
                "-o",
                str(binary),
            ],
            check=True,
        )
        result = subprocess.run(
            [str(binary), "6"],
            input=input_path.read_bytes(),
            check=True,
            stdout=subprocess.PIPE,
        )
    text = result.stdout.decode()
    assert "profile_frontier=102 C_range=(1118689,355504811)" in text
    expected = {
        1: 11389760938,
        2: 1275194558068,
        3: 204331272672794,
        4: 23657227423060068,
        5: 3131204364458925600,
        6: 422071623348857647279,
    }
    found = {int(q): int(w) for q, w in re.findall(r"q=(\d+).*? W=(\d+)", text)}
    assert found == expected, (found, text)
    return found


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path,
                        help="optional generated 512-direction W3 input")
    args = parser.parse_args()
    checked = abstract_width_gate()
    lower = exact_44_gate()
    right, left = association_audit()
    message = (
        f"PASS: spectrum-width inequality cases={checked}; "
        f"association audit right={right[1:]}, left={left[1:]}; "
        f"full-44 q3 cross lower={lower}"
    )
    if args.input:
        found = sampled_dp(args.input)
        message += f"; sampled q1..q6={found}"
    print(message)


if __name__ == "__main__":
    main()
