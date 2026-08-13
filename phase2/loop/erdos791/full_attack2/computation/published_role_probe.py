#!/usr/bin/env python3
"""Exact phased-role costs for published small extremal/restricted bases.

The bases are transcribed from Tables 1--3 of J. Kohonen, JIS 17
(2014), Article 14.6.8.  In that paper a basis of "length k" has k+1
elements because a_0=0 is included.  Rows marked global below are the two
known extremal nonrestricted length-10 bases; other rows are extremal within
the restricted class and are used only as a structural diagnostic.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from phased_role_model import ROLES, solve


def six_step(prefix: tuple[int, ...], last: int, suffix: tuple[int, ...]) -> tuple[int, ...]:
    middle = tuple(range(prefix[-1] + 6, last + 1, 6))
    return prefix + middle + suffix


ROWS = [
    (32, (0, 1, 2, 5, 8, 11, 14, 15, 16), "restricted"),
    (40, (0, 1, 3, 4, 9, 11, 16, 17, 19, 20), "restricted"),
    (46, (0, 1, 2, 3, 7, 11, 15, 19, 21, 22, 24), "global"),
    (46, (0, 1, 2, 5, 7, 11, 15, 19, 21, 22, 24), "global"),
    (54, (0, 1, 3, 4, 9, 11, 16, 18, 23, 24, 26, 27), "restricted"),
    (54, (0, 1, 3, 5, 6, 13, 14, 21, 22, 24, 26, 27), "restricted"),
    (64, (0, 1, 3, 4, 9, 11, 16, 21, 23, 28, 29, 31, 32), "restricted"),
    (72, (0, 1, 3, 4, 9, 11, 16, 20, 25, 27, 32, 33, 35, 36), "restricted"),
    (80, six_step((0, 1, 3, 4, 5, 8), 32, (35, 36, 37, 39, 40)), "restricted"),
    (92, six_step((0, 1, 3, 4, 5, 8), 38, (41, 42, 43, 45, 46)), "restricted"),
    (104, six_step((0, 1, 3, 4, 5, 8), 44, (47, 48, 49, 51, 52)), "restricted"),
    (116, six_step((0, 1, 3, 4, 5, 8), 50, (53, 54, 55, 57, 58)), "restricted"),
    (128, six_step((0, 1, 3, 4, 5, 8), 56, (59, 60, 61, 63, 64)), "restricted"),
    (140, six_step((0, 1, 3, 4, 5, 8), 62, (65, 66, 67, 69, 70)), "restricted"),
    (152, six_step((0, 1, 3, 4, 5, 8), 68, (71, 72, 73, 75, 76)), "restricted"),
    (
        536,
        (
            0, 1, 3, 4, 7, 8, 9, 16, 17, 21, 24, 35, 46,
            57, 68, 79, 90, 101, 112, 123, 134, 145, 156, 167,
            178, 189, 200, 211, 222, 233, 244, 247, 251, 252,
            259, 260, 261, 264, 265, 267, 268,
        ),
        "restricted",
    ),
]


def is_basis(A: tuple[int, ...], n: int) -> bool:
    sums = {x + y for x in A for y in A}
    return set(range(n + 1)) <= sums


def unique_diagonals(A: tuple[int, ...], n: int) -> list[int]:
    answer = []
    for x in A:
        if 2 * x > n:
            continue
        reps = [(a, b) for i, a in enumerate(A) for b in A[i:] if a + b == 2 * x]
        if reps == [(x, x)]:
            answer.append(x)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=60)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    results = []
    for index, (n, A, classification) in enumerate(ROWS):
        if not is_basis(A, n):
            raise RuntimeError((n, A))
        diagonal = unique_diagonals(A, n)
        ordinary = solve(A, n, args.seconds, 8, 791_900 + index, allowed_roles=ROLES)
        triangle = solve(
            A, n, args.seconds, 8, 792_900 + index, allowed_roles=ROLES, triangle=True
        )
        results.append(
            {
                "range": n,
                "basis": A,
                "basis_size": len(A),
                "classification": classification,
                "unique_diagonals": diagonal,
                "ordinary_role_cost": ordinary.get("role_cost"),
                "ordinary_status": ordinary["status"],
                "triangle_role_cost": triangle.get("role_cost"),
                "triangle_status": triangle["status"],
            }
        )
        print(n, len(A), ordinary["status"], ordinary.get("role_cost"), flush=True)
    payload = {
        "status": "PASS" if all(row["ordinary_status"] == "OPTIMAL" and row["triangle_status"] == "OPTIMAL" for row in results) else "INCOMPLETE",
        "source": "https://cs.uwaterloo.ca/journals/JIS/VOL17/Kohonen2/kohonen5.html",
        "scope": "published finite diagnostic; restricted rows are not claimed globally extremal",
        "rows": results,
    }
    parser_output = json.dumps(payload, indent=2) + "\n"
    args.output.write_text(parser_output)
    print(parser_output, end="")


if __name__ == "__main__":
    main()
