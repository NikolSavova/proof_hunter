#!/usr/bin/env python3
"""Exact audit of the common-circuit deletion cascade gate."""

from __future__ import annotations

import itertools
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "agent_lex_minimizer_search" / "exact_realizable_n9.json"


def determinant(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def is_convex(points: list[tuple[int, int]], mask: int) -> bool:
    labels = [i for i in range(len(points)) if (mask >> i) & 1]
    if len(labels) <= 3:
        return True
    labels.sort(key=lambda i: points[i])

    def half(sequence: list[int]) -> list[int]:
        answer: list[int] = []
        for i in sequence:
            while (
                len(answer) >= 2
                and determinant(points[answer[-2]], points[answer[-1]], points[i]) <= 0
            ):
                answer.pop()
            answer.append(i)
        return answer

    hull = half(labels)[:-1] + half(list(reversed(labels)))[:-1]
    return len(hull) == len(labels)


def mask(labels: list[int]) -> int:
    return sum(1 << i for i in labels)


def main() -> None:
    data = json.loads(DATA.read_text())
    points = [tuple(point) for point in data["coordinates_as_stored"]]
    n = len(points)
    assert n == 9
    assert all(
        determinant(points[i], points[j], points[k]) != 0
        for i, j, k in itertools.combinations(range(n), 3)
    )

    full = (1 << n) - 1
    faces = [is_convex(points, subset) for subset in range(1 << n)]
    face_vector = Counter(
        subset.bit_count() for subset in range(1, 1 << n) if faces[subset]
    )
    assert [face_vector[k] for k in range(1, 6)] == [9, 36, 84, 36, 3]
    assert sum(face_vector.values()) == 168

    bad_fours = [
        subset
        for subset in range(1 << n)
        if subset.bit_count() == 4 and not faces[subset]
    ]
    rectangle_count = 0
    no_common_deletion = 0
    minimum_release = (1, 1)
    witness_seen = False

    witness_x = mask([0, 1, 2, 3])
    witness_c = mask([1, 4, 5, 7])
    witness_rows = {mask([4, 5, 7]), mask([4, 5, 7, 8])}
    witness_columns = {
        mask([1]) | mask([label for j, label in enumerate([0, 2, 3]) if (code >> j) & 1])
        for code in range(8)
    }

    for x_ground in range(1, full):
        if x_ground.bit_count() != 4:
            continue
        y_ground = full ^ x_ground
        row_faces = [
            subset
            for subset in range(1, 1 << n)
            if not (subset & ~y_ground) and faces[subset]
        ]
        column_faces = [
            subset
            for subset in range(1, 1 << n)
            if not (subset & ~x_ground) and faces[subset]
        ]
        for circuit in bad_fours:
            cy = circuit & y_ground
            cx = circuit & x_ground
            if not cy or not cx:
                continue
            rows = [row for row in row_faces if row & cy == cy]
            columns = [column for column in column_faces if column & cx == cx]
            if not rows or not columns:
                continue
            rectangle_count += 1
            assert all(not faces[row | column] for row in rows for column in columns)

            releasing_deletions = []
            deletion = circuit
            while True:
                if all(
                    faces[(row | column) & ~deletion]
                    for row in rows
                    for column in columns
                ):
                    releasing_deletions.append(deletion)
                if deletion == 0:
                    break
                deletion = (deletion - 1) & circuit
            if not releasing_deletions:
                no_common_deletion += 1

            released = sum(
                faces[(row | column) & ~circuit]
                for row in rows
                for column in columns
            )
            total = len(rows) * len(columns)
            if released * minimum_release[1] < minimum_release[0] * total:
                minimum_release = (released, total)

            if x_ground == witness_x and circuit == witness_c:
                assert set(rows) == witness_rows
                assert set(columns) == witness_columns
                assert not releasing_deletions
                assert (released, total) == (15, 16)
                assert not faces[mask([0, 2, 3, 8])]
                witness_seen = True

    assert rectangle_count == 10_800
    assert no_common_deletion == 1_569
    assert minimum_release == (25, 28)
    assert witness_seen

    # The rank/cascade arithmetic used in (1).
    arithmetic_rows = 0
    for ambient_v in range(1, 20):
        for binom4 in range(1, 20):
            for q in range(0, 8):
                bound = 2 * ambient_v * (2 * binom4) ** q
                mass = bound + 1
                for _ in range(q):
                    assert mass > 2 * ambient_v
                    mass = (mass - ambient_v + binom4 - 1) // binom4
                assert mass > 2 * ambient_v
                arithmetic_rows += 1

    print(
        "PASS: exact common-circuit deletion barrier and cascade arithmetic; "
        f"faces=168, bad4={len(bad_fours)}, rectangles={rectangle_count}, "
        f"no_common_deletion={no_common_deletion}, "
        f"minimum_release={minimum_release[0]}/{minimum_release[1]}, "
        f"arithmetic={arithmetic_rows}"
    )


if __name__ == "__main__":
    main()
