#!/usr/bin/env python3
"""Exact 44-point build from the globally optimal first reset menu.

The three witnesses were found by exhausting all reset states in
``verify_two_direction_four_point_wrapper.py``.  This script fixes the
rechart/gauge convention used by the root audit so that the resulting
44-point spectrum is reproducible.
"""

from fractions import Fraction as Q
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SHIELD = HERE.parent / "agent_shield_circuit_cover"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(SHIELD))

import verify_two_direction_four_point_wrapper as menu  # noqa: E402
from verify_recharted_all_loop_wrapper_gate import comb_arc  # noqa: E402
from verify_common_guard_all_direction import projection_orders  # noqa: E402
from explore_two_level_rechart import (  # noqa: E402
    best_three_fast,
    fast_chain_totals,
    orientation_cube,
    rechart,
)


SPEC = (((7, 0, 0), 43, (183, 1975), 1992),
        ((0, 1, 7), 11, (342, 414), 1986),
        ((7, 0, 0), 42, (1975, 183), 1992))


def main():
    blocks = [[(Q(0), Q(0))]]
    for word, chamber_index, expected_profile, expected_faces in SPEC:
        points, clusters = menu.configuration(word)
        signs = menu.all_signs(points)
        profiles = [menu.local_profile(cluster) for cluster in clusters]
        assert menu.wrapper_faces(profiles) == expected_faces

        # The 1e-30 perturbation is part of the convention: chamber indices
        # 42/43 refer to its fully split 182-order allowable sequence.
        points = menu.generic_perturb(points, signs)
        chambers = menu.projection_orders(points)
        order = chambers[chamber_index]
        assert menu.chain_counts(signs, order) == expected_profile
        blocks.append(rechart(points, order))
    blocks.append([(Q(0), Q(0))])

    parent = comb_arc(blocks)
    assert len(parent) == 44
    chambers = projection_orders(parent)
    signs = orientation_cube(parent)
    profiles = [fast_chain_totals(order, signs) for order in chambers]
    low = min(profiles, key=lambda row: row[0] * row[1])
    assert len(chambers) == 1884
    assert low == (18275, 49645)
    assert min(max(row) for row in profiles) == 39777

    level_three, chosen = best_three_fast(list(set(profiles)), 44, 747670)
    assert chosen == ((15121, 102449),
                      (44728, 21566),
                      (102449, 15121))
    assert level_three == 11358202734
    print("PASS: W2=747670; chambers=1884; min CU=%d; "
          "minmax=39777; W3=%d"
          % (low[0] * low[1], level_three))


if __name__ == "__main__":
    main()
