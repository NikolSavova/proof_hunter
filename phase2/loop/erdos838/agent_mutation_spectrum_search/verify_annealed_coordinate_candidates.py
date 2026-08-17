#!/usr/bin/env python3
"""Exact audit of the saved coordinate-annealing candidates.

The annealing which found the coordinates was heuristic.  Everything checked
below is deterministic and exact: general position, ordinary/cap/cup counts,
the complete two-block spectrum through n=18, the complete three-block
spectrum through n=12, and all three-block moves involving at most four
labels thereafter.
"""

from __future__ import annotations

import importlib.util
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))
sys.path.insert(0, str(HERE))

import reflection_trace as rt  # noqa: E402
from verify_greedy_ifs_mutation_spectrum import (  # noqa: E402
    horizontal_glue,
    normalize,
    sparse_three_minimum,
)

CONTROL_PATH = HERE / "verify_mutation_spectrum_controls.py"
SPEC = importlib.util.spec_from_file_location("annealed_controls", CONTROL_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load mutation-spectrum controls")
controls = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(controls)


Y_COORDINATES = {
    10: (
        736769, -125284, -16754918, -3321502, -7377938,
        -6206528, -3052739, -3640513, -2970863, -2506569,
    ),
    12: (
        6467145, 6173108, 5840490, 7992019, 8517023, 5033492,
        10758894, 16710080, 1928295, 368948, -1029265, -2416701,
    ),
    14: (
        -1402863, -1358871, -688131, 225365, -3680365, -1936358,
        -854768, -8306706, 827189, -13719192, 2184148, -34782460,
        21822765, 25855774,
    ),
    16: (
        -259619, -65166, 17462, 44217, 387011, 1422277, 653029,
        2932287, 3979495, -1255834, -3778606, -6067143, -7633051,
        6594402, -10650148, 9829648,
    ),
    18: (
        -56989111, 8029727, 6518235, -28592764, 5243870, 2103006,
        1917149, -2477683, -8080130, -8121297, -9622417, -647405,
        -1929583, 735992, 1714743, 1088562, 2391646, 3161682,
    ),
    20: (
        8392834, 7550502, -13790050, 6030771, 4612422, -9608074,
        -7226018, 3047872, 2607592, -5358542, -4814394, -4741160,
        296069, 1793012, -4513448, -5520703, -6539372, 312185,
        -8306210, 938392,
    ),
}

EXPECTED_PROFILES = {
    10: (125, 157, 249),
    12: (306, 203, 500),
    14: (434, 497, 963),
    16: (951, 645, 1743),
    18: (1087, 1435, 2965),
    20: (1469, 1636, 4895),
}


def points(size: int):
    return [
        (Fraction(index), Fraction(y))
        for index, y in enumerate(Y_COORDINATES[size])
    ]


def main() -> None:
    profiles = {size: rt.evaluate(points(size))[:3] for size in Y_COORDINATES}
    assert profiles == EXPECTED_PROFILES

    two_block = {}
    for size in (10, 12, 14, 16, 18):
        row = controls.spectrum(f"annealed_{size}", points(size))
        two_block[size] = (
            row["minimum_slack"],
            row["proper_minimum_slack"],
            row["deep_minimum_slack"],
            row["decreasing_count"],
        )
    assert two_block == {
        10: (0, 0, 25, 0),
        12: (0, 0, 43, 0),
        14: (0, 19, 101, 0),
        16: (0, 45, 164, 0),
        18: (0, 48, 188, 0),
    }

    full_three = {}
    for size in (10, 12):
        row = controls.q_block_spectrum(points(size), 3)
        full_three[size] = (
            row["minimum_slack"],
            row["all_blocks_nonempty_minimum_slack"],
            row["decreasing_count"],
        )
    assert full_three == {10: (0, 15, 0), 12: (0, 38, 0)}

    sparse = {}
    for size in (14, 16, 18, 20):
        best, masks, assignments, cache_size = sparse_three_minimum(
            points(size), 4
        )
        sparse[size] = (best, masks, assignments, cache_size)
    for size in (14, 16, 18):
        assert sparse[size][0] == EXPECTED_PROFILES[size][2]
        assert sparse[size][1] is None
    assert sparse[20][0] == 4885
    masks = sparse[20][1]
    assert masks is not None
    assert tuple(mask.bit_count() for mask in masks) == (0, 19, 1)

    original = points(20)
    middle = [
        original[index] for index in range(20) if masks[1] >> index & 1
    ]
    right = [
        original[index] for index in range(20) if masks[2] >> index & 1
    ]
    mutated = horizontal_glue(normalize(middle, reflect=True), normalize(right))
    assert rt.evaluate(mutated)[:3] == (1441, 2191, 4885)
    post = sparse_three_minimum(mutated, 4)
    assert post[0] == 4885 and post[1] is None

    print(
        "PASS: exact annealed candidates; profiles=%s; q2=%s; q3=%s; "
        "sparse=(%d,%d,%d,%d); repaired20=(1441,2191,4885); post=%d"
        % (
            profiles,
            two_block,
            full_three,
            sparse[14][0], sparse[16][0], sparse[18][0], sparse[20][0],
            post[0],
        )
    )


if __name__ == "__main__":
    main()
