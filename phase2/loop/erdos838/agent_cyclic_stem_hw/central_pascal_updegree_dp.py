#!/usr/bin/env python3
"""Exact ordinary up-degree DP for strong-glue Pascal cells.

The usual graded recurrence remembers only the size of a face.  Here a cap
state is ``(size, cap_up_degree, ordinary_up_degree)``, a cup state is the
reflected triple, and a convex-face state is ``(size, ordinary_up_degree)``.
The strong-glue classification makes these distributions close exactly.

The script is an adversarial test of the exterior-incidence conjecture used
in the Erdős 838 attack.  It never reconstructs coordinates.  Its recurrence
is nevertheless exact for every sufficiently strongly separated realization
of the Pascal cells.  Small cells are independently checked against the
coordinate/circuit enumerator in ``verify_optimized_hull_activity.py``.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GRADED = ROOT / "agent_graded_supersat"
sys.path.insert(0, str(GRADED))

from graded_balanced import pascal_row as graded_pascal_row  # noqa: E402


CapState = Counter[tuple[int, int, int]]
FaceState = Counter[tuple[int, int]]


@dataclass
class Cell:
    n: int
    caps: CapState
    cups: CapState
    faces: FaceState


def add(counter: Counter, key: tuple[int, ...], value: int, cutoff: int) -> None:
    if value and key[0] <= cutoff:
        counter[key] += value


def cap_degree_marginal(states: CapState) -> Counter[tuple[int, int]]:
    """Forget ordinary degree; cross faces use only cap/cup degree."""
    answer: Counter[tuple[int, int]] = Counter()
    for (rank, directional_degree, _), count in states.items():
        answer[rank, directional_degree] += count
    return answer


def ordinary_degree_marginal(states: CapState) -> Counter[tuple[int, int]]:
    """Forget directional degree; used to identify cap/cup-only faces."""
    answer: Counter[tuple[int, int]] = Counter()
    for (rank, _, ordinary_degree), count in states.items():
        answer[rank, ordinary_degree] += count
    return answer


def glue(left: Cell, right: Cell, cutoff: int) -> Cell:
    """Exact strong glue ``left \\prec right``, truncated by face size."""
    a, b = left.n, right.n
    caps: CapState = Counter()
    cups: CapState = Counter()

    # A cap of A, with zero or one point of B.
    for (rank, cap_degree, ordinary_degree), count in left.caps.items():
        add(caps, (rank, cap_degree + b, ordinary_degree + b), count, cutoff)
        add(
            caps,
            (rank + 1, cap_degree, cap_degree + b - 1),
            count * b,
            cutoff,
        )

    # Or a cap wholly in B.  It admits an A point as a cap only at rank one,
    # and as an ordinary convex extension exactly when it is also a cup,
    # which in general position means rank at most two.
    for (rank, cap_degree, ordinary_degree), count in right.caps.items():
        add(
            caps,
            (
                rank,
                cap_degree + (a if rank == 1 else 0),
                ordinary_degree + (a if rank <= 2 else 0),
            ),
            count,
            cutoff,
        )

    # Reflected cup formulas.
    for (rank, cup_degree, ordinary_degree), count in left.cups.items():
        add(
            cups,
            (
                rank,
                cup_degree + (b if rank == 1 else 0),
                ordinary_degree + (b if rank <= 2 else 0),
            ),
            count,
            cutoff,
        )
    for (rank, cup_degree, ordinary_degree), count in right.cups.items():
        add(cups, (rank, cup_degree + a, ordinary_degree + a), count, cutoff)
        add(
            cups,
            (rank + 1, cup_degree, cup_degree + a - 1),
            count * a,
            cutoff,
        )

    faces: FaceState = Counter()

    # Faces wholly in A.  Precisely the cap faces acquire all b points of B
    # as ordinary extensions.
    for key, count in left.faces.items():
        faces[key] += count
    for (rank, ordinary_degree), count in ordinary_degree_marginal(left.caps).items():
        faces[rank, ordinary_degree] -= count
        faces[rank, ordinary_degree + b] += count

    # Faces wholly in B, with the reflected cup correction.
    for key, count in right.faces.items():
        faces[key] += count
    for (rank, ordinary_degree), count in ordinary_degree_marginal(right.cups).items():
        faces[rank, ordinary_degree] -= count
        faces[rank, ordinary_degree + a] += count

    # A spanning face is a nonempty cap of A plus a nonempty cup of B.  Its
    # ordinary extension degree is the sum of the two directional degrees.
    # Collapsing the irrelevant ordinary-degree coordinate before this
    # multiplication is the key optimization over the naive exact DP.
    left_marginal = cap_degree_marginal(left.caps)
    right_marginal = cap_degree_marginal(right.cups)
    for (left_rank, left_degree), left_count in left_marginal.items():
        for (right_rank, right_degree), right_count in right_marginal.items():
            rank = left_rank + right_rank
            if rank <= cutoff:
                faces[rank, left_degree + right_degree] += left_count * right_count

    # No legitimate count can cancel to a negative number; delete exact
    # zeros created by replacing cap/cup marginals.
    faces += Counter()
    if any(count < 0 for count in faces.values()):
        raise AssertionError("negative face count")
    return Cell(a + b, caps, cups, faces)


def bounded(value: int, degree_cutoff: int) -> int:
    """Store all ordinary degrees above the cutoff in one overflow state."""
    return min(value, degree_cutoff + 1)


def glue_bounded(
    left: Cell, right: Cell, rank_cutoff: int, degree_cutoff: int
) -> Cell:
    """Exact DP for faces of ordinary degree at most ``degree_cutoff``.

    Directional cap/cup degrees never decrease, so states above the degree
    cutoff can be discarded.  Ordinary degree *can* be reset when a point is
    taken from the other block; hence cap/cup states retain one overflow
    value.  This is enough to recover every eventual low-degree face exactly.
    """
    a, b = left.n, right.n
    overflow = degree_cutoff + 1
    caps: CapState = Counter()
    cups: CapState = Counter()

    def add_directional(
        target: CapState,
        rank: int,
        directional: int,
        ordinary: int,
        count: int,
    ) -> None:
        if rank <= rank_cutoff and directional <= degree_cutoff and count:
            target[rank, directional, bounded(ordinary, degree_cutoff)] += count

    for (rank, cap_degree, ordinary_degree), count in left.caps.items():
        add_directional(
            caps,
            rank,
            cap_degree + b,
            ordinary_degree + b if ordinary_degree != overflow else overflow,
            count,
        )
        add_directional(
            caps, rank + 1, cap_degree, cap_degree + b - 1, count * b
        )
    for (rank, cap_degree, ordinary_degree), count in right.caps.items():
        add_directional(
            caps,
            rank,
            cap_degree + (a if rank == 1 else 0),
            (
                ordinary_degree + (a if rank <= 2 else 0)
                if ordinary_degree != overflow
                else overflow
            ),
            count,
        )

    for (rank, cup_degree, ordinary_degree), count in left.cups.items():
        add_directional(
            cups,
            rank,
            cup_degree + (b if rank == 1 else 0),
            (
                ordinary_degree + (b if rank <= 2 else 0)
                if ordinary_degree != overflow
                else overflow
            ),
            count,
        )
    for (rank, cup_degree, ordinary_degree), count in right.cups.items():
        add_directional(
            cups,
            rank,
            cup_degree + a,
            ordinary_degree + a if ordinary_degree != overflow else overflow,
            count,
        )
        add_directional(
            cups, rank + 1, cup_degree, cup_degree + a - 1, count * a
        )

    faces: FaceState = Counter()
    for (rank, ordinary_degree), count in left.faces.items():
        if rank <= rank_cutoff:
            faces[rank, ordinary_degree] += count
    for (rank, ordinary_degree), count in ordinary_degree_marginal(left.caps).items():
        if ordinary_degree <= degree_cutoff:
            faces[rank, ordinary_degree] -= count
            shifted = ordinary_degree + b
            if shifted <= degree_cutoff:
                faces[rank, shifted] += count

    for (rank, ordinary_degree), count in right.faces.items():
        if rank <= rank_cutoff:
            faces[rank, ordinary_degree] += count
    for (rank, ordinary_degree), count in ordinary_degree_marginal(right.cups).items():
        if ordinary_degree <= degree_cutoff:
            faces[rank, ordinary_degree] -= count
            shifted = ordinary_degree + a
            if shifted <= degree_cutoff:
                faces[rank, shifted] += count

    left_marginal = cap_degree_marginal(left.caps)
    right_marginal = cap_degree_marginal(right.cups)
    for (left_rank, left_degree), left_count in left_marginal.items():
        for (right_rank, right_degree), right_count in right_marginal.items():
            rank = left_rank + right_rank
            degree = left_degree + right_degree
            if rank <= rank_cutoff and degree <= degree_cutoff:
                faces[rank, degree] += left_count * right_count

    faces += Counter()
    if any(count < 0 for count in faces.values()):
        raise AssertionError("negative bounded face count")
    return Cell(a + b, caps, cups, faces)


def pascal_row_bounded(
    levels: int,
    rank_cutoff: int,
    degree_cutoff: int,
    verbose: bool = False,
) -> list[Cell]:
    singleton = Cell(
        1,
        Counter({(1, 0, 0): 1}),
        Counter({(1, 0, 0): 1}),
        Counter({(1, 0): 1}),
    )
    row = [singleton]
    started = time.monotonic()
    for level in range(1, levels + 1):
        new = [singleton]
        for index in range(1, level):
            new.append(
                glue_bounded(
                    row[index - 1], row[index], rank_cutoff, degree_cutoff
                )
            )
        new.append(singleton)
        row = new
        if verbose and level % 4 == 0:
            max_keys = max(
                len(cell.caps) + len(cell.cups) + len(cell.faces) for cell in row
            )
            print(
                f"bounded_level={level} max_state_keys={max_keys} "
                f"seconds={time.monotonic() - started:.3f}",
                flush=True,
            )
    return row


def pascal_row(levels: int, cutoff: int, verbose: bool = False) -> list[Cell]:
    singleton = Cell(
        1,
        Counter({(1, 0, 0): 1}),
        Counter({(1, 0, 0): 1}),
        Counter({(1, 0): 1}),
    )
    row = [singleton]
    started = time.monotonic()
    for level in range(1, levels + 1):
        new = [singleton]
        for index in range(1, level):
            new.append(glue(row[index - 1], row[index], cutoff))
        new.append(singleton)
        row = new
        if verbose and level % 2 == 0:
            max_keys = max(
                len(cell.caps) + len(cell.cups) + len(cell.faces) for cell in row
            )
            print(
                f"level={level} max_state_keys={max_keys} "
                f"seconds={time.monotonic() - started:.3f}",
                flush=True,
            )
    return row


def log2_int(value: int) -> float:
    if value <= 0:
        raise ValueError(value)
    shift = max(0, value.bit_length() - 53)
    return shift + math.log2(value >> shift)


def psi(rank: int, q: float) -> float:
    if q <= 0:
        return 0.0
    return (
        rank * math.log1p(q / rank) / math.log(2.0)
        + q * math.log1p(rank / q) / math.log(2.0)
    )


def entropy_inverse(rank: int, log_count: float, n: int) -> float:
    if log_count <= 0:
        return 0.0
    low, high = 0.0, float(n - rank)
    if psi(rank, high) + 1e-8 < log_count:
        raise AssertionError((rank, log_count, psi(rank, high)))
    for _ in range(160):
        middle = (low + high) / 2
        if psi(rank, middle) < log_count:
            low = middle
        else:
            high = middle
    return high


def audit_cell(parameter: int, cell: Cell) -> dict[str, object]:
    """Return exact low-extension census and entropy EIC lower bounds."""
    cutoff = max((rank for rank, _ in cell.faces), default=0)
    _, graded_caps, graded_cups, graded_faces = graded_pascal_row(
        parameter, cutoff
    )[parameter // 2]

    face_profile = [0] * (cutoff + 1)
    cap_profile = [0] * (cutoff + 1)
    cup_profile = [0] * (cutoff + 1)
    for (rank, _), count in cell.faces.items():
        face_profile[rank] += count
    for (rank, _, _), count in cell.caps.items():
        cap_profile[rank] += count
    for (rank, _, _), count in cell.cups.items():
        cup_profile[rank] += count
    if face_profile != graded_faces[: cutoff + 1]:
        raise AssertionError(("face profile", parameter))
    if cap_profile != graded_caps[: cutoff + 1]:
        raise AssertionError(("cap profile", parameter))
    if cup_profile != graded_cups[: cutoff + 1]:
        raise AssertionError(("cup profile", parameter))

    # The empty face is not carried by the nonempty recurrence.
    total_faces = 1 + sum(face_profile)
    ell = (cell.n - 1).bit_length()
    rows = []
    for rank in range(1, min(ell, cutoff + 1)):
        threshold = 4 * (rank + 1)
        near_count = sum(
            count
            for (state_rank, degree), count in cell.faces.items()
            if state_rank == rank and degree <= threshold
        )
        if not near_count:
            continue
        up_sum = sum(
            degree * count
            for (state_rank, degree), count in cell.faces.items()
            if state_rank == rank and degree <= threshold
        )
        required_mean_q = entropy_inverse(rank, log2_int(near_count), cell.n)
        # Hull activity applies to this precise near-maximal family.  Since
        # e=q-u and E[u] is known exactly, this is a rigorous lower bound on
        # its exterior-repair incidence sum.
        eic_lower = near_count * required_mean_q - up_sum
        eic_lower = max(0.0, eic_lower)
        rows.append(
            {
                "rank": rank,
                "face_count": face_profile[rank],
                "near_maximal_count": near_count,
                "near_density_log2": log2_int(near_count) - log2_int(total_faces),
                "mean_up_degree_on_near": up_sum / near_count,
                "entropy_required_mean_q": required_mean_q,
                "rigorous_EIC_over_V_lower": eic_lower / total_faces,
                "trivial_EIC_over_V_upper": cell.n * near_count / total_faces,
            }
        )
    return {
        "parameter": parameter,
        "n": cell.n,
        "ell": ell,
        "cutoff": cutoff,
        "V": total_faces,
        "log2_V": log2_int(total_faces),
        "rows_below_ell": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-parameter", type=int, default=16)
    parser.add_argument("--min-parameter", type=int, default=4)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    cutoff = args.max_parameter + 2
    row = pascal_row(args.max_parameter, cutoff, args.verbose)
    # A single terminal row contains only the requested last parameter.  Run
    # smaller requested parameters separately; this is cheap compared with
    # the largest cell and makes each certificate independently auditable.
    audits = []
    for parameter in range(args.min_parameter, args.max_parameter + 1):
        if parameter == args.max_parameter:
            parameter_row = row
        else:
            parameter_row = pascal_row(parameter, cutoff)
        audits.append(audit_cell(parameter, parameter_row[parameter // 2]))
    result = {
        "description": "exact up-degree DP for central strong-glue Pascal cells",
        "audits": audits,
    }
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n")
    print(rendered)


if __name__ == "__main__":
    main()
