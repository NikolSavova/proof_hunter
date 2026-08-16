#!/usr/bin/env python3
"""Exact audit of the proposed low-addable-face budget.

For L=ceil(log_2 n), this computes

    N(P)=sum_{r<L} (L-r) #{convex r-faces A : u(A)<=4(r+1)}.

The implementation uses the rooted-circuit characterization.  For every
triple T it stores a bit mask of points p for which T+p is a nonconvex
quadruple.  OR-ing these masks over the triples of A simultaneously tests
whether A is convex and computes all blocked additions.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RANK = ROOT / "agent_apa_rank"
GRADED = ROOT / "agent_graded_supersat"
LOW = ROOT / "agent_low_v_structure"
sys.path[:0] = [str(RANK), str(GRADED), str(LOW)]

import verify_apa_counterexample as apa  # noqa: E402
import verify_half_weight_counterexample as hw  # noqa: E402
from graded_trace import pascal_cell  # noqa: E402
import guarded_template_verify as guard  # noqa: E402


def inside_triangle(point, a, b, c) -> bool:
    values = (
        apa.orient(a, b, point),
        apa.orient(b, c, point),
        apa.orient(c, a, point),
    )
    return all(value > 0 for value in values) or all(value < 0 for value in values)


def circuit_table(points) -> dict[tuple[int, int, int], int]:
    n = len(points)
    table = {triple: 0 for triple in itertools.combinations(range(n), 3)}
    for quadruple in itertools.combinations(range(n), 4):
        roots = []
        for root in quadruple:
            triple = tuple(label for label in quadruple if label != root)
            if inside_triangle(
                points[root], *(points[label] for label in triple)
            ):
                roots.append((root, triple))
        if roots:
            assert len(roots) == 1
            root, triple = roots[0]
            table[triple] |= 1 << root
    return table


def audit(points, expected_profile: tuple[int, ...] | None = None) -> dict[str, object]:
    points = tuple(points)
    n = len(points)
    level = math.ceil(math.log2(n))
    table = circuit_table(points)
    full_mask = (1 << n) - 1
    face_counts = []
    low_counts = []
    weighted = 0
    for rank in range(level):
        faces = low = 0
        for labels in itertools.combinations(range(n), rank):
            face_mask = sum(1 << label for label in labels)
            blocked = 0
            for triple in itertools.combinations(labels, 3):
                blocked |= table[triple]
            if blocked & face_mask:
                continue
            faces += 1
            up_degree = (full_mask & ~face_mask & ~blocked).bit_count()
            if up_degree <= 4 * (rank + 1):
                low += 1
                weighted += level - rank
        face_counts.append(faces)
        low_counts.append(low)
    profile = expected_profile or apa.matrix_profile(points)
    assert tuple(face_counts) == tuple(profile[:level])
    value = sum(profile)
    return {
        "n": n,
        "L": level,
        "V": value,
        "rank_counts_below_L": face_counts,
        "low_addable_counts_below_L": low_counts,
        "N": weighted,
        "N_over_V": weighted / value,
    }


def guarded_template(parameter: int):
    m, index = 2 * parameter - 4, parameter - 2
    cell = tuple(sorted(pascal_cell(m, index, Q(1, 97))))
    paths = guard.pascal_paths(m, index)
    assert len(cell) == len(paths)
    for exponent in range(2, 20):
        epsilon = Q(1, 10**exponent)
        points = tuple(
            (Q(guard.GUARD[0][0]) + epsilon * epsilon * x,
             Q(guard.GUARD[0][1]) + epsilon * y)
            for x, y in cell
        ) + tuple((Q(x), Q(y)) for x, y in guard.GUARD[1:])
        if all(
            (apa.orient(points[i], points[j], points[k]) > 0)
            - (apa.orient(points[i], points[j], points[k]) < 0)
            == guard.guarded_sign(paths, i, j, k)
            for i, j, k in itertools.combinations(range(len(points)), 3)
        ):
            return points
    raise AssertionError("failed to realize guarded template")


def vertical_compose(points, epsilon: Q):
    return tuple(
        sorted(
            (
                macro_x + epsilon * epsilon * (block + 1) * micro_x,
                macro_y + epsilon * (block + 1) * micro_y,
            )
            for block, (macro_x, macro_y) in enumerate(points)
            for micro_x, micro_y in points
        )
    )


def main() -> None:
    records = {}
    coordinate_record = json.loads((HERE / "planar_acp_record.json").read_text())
    points_24 = tuple(
        (Q(x), Q(y)) for x, y in enumerate(coordinate_record["y_coordinates"])
    )
    records["ACP_coordinate_n24"] = audit(points_24)
    records["APA_counterexample_n44"] = audit(
        apa.points(), apa.EXPECTED_PROFILE
    )
    records["half_weight_counterexample_n58"] = audit(
        hw.points(), hw.EXPECTED_PROFILE
    )
    for m in range(4, 8):
        points = tuple(sorted(pascal_cell(m, m // 2, Q(1, 97))))
        records[f"central_Pascal_m{m}"] = audit(points)
    cell = tuple(sorted(pascal_cell(4, 2, Q(1, 97))))
    epsilon = Q(1, 16384)
    vertical_square = tuple(
        sorted(
            (
                macro_x + epsilon * epsilon * micro_x,
                macro_y + epsilon * micro_y,
            )
            for macro_x, macro_y in cell
            for micro_x, micro_y in cell
        )
    )
    records["vertical_T42_depth2"] = audit(vertical_square)
    guarded = {}
    for parameter in range(3, 6):
        guarded[parameter] = guarded_template(parameter)
        records[f"guarded_template_k{parameter}"] = audit(guarded[parameter])
    guarded_square = vertical_compose(guarded[3], Q(1, 10**8))
    records["guarded_template_k3_depth2"] = audit(guarded_square)

    output = {
        "description": "exact low-addable-face budget audit",
        "definition": "sum_(r<L) (L-r) # {rank-r convex A : u(A)<=4(r+1)}",
        "records": records,
    }
    (HERE / "low_addable_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print("low-addable audit: PASS")
    for name, row in records.items():
        print(
            name,
            f"n={row['n']}",
            f"N/V={row['N_over_V']:.12f}",
            f"low={row['low_addable_counts_below_L']}",
        )


if __name__ == "__main__":
    main()
