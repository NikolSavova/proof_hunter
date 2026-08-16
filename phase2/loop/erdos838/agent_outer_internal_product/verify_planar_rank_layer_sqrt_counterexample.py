#!/usr/bin/env python3
"""Exact audit for PLANAR_RANK_LAYER_SQRT_ANTICONCENTRATION_COUNTEREXAMPLE."""

from fractions import Fraction
from pathlib import Path
from math import comb
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "agent_graded_supersat"))
from graded_balanced import pascal_row, vertical_iterate  # noqa: E402


def main():
    template = pascal_row(4, 6)[2]
    size, caps, cups, faces = template
    assert size == 6
    assert caps[:5] == [0, 6, 15, 10, 0]
    assert cups[:5] == caps[:5]
    assert faces[:6] == [0, 6, 15, 20, 9, 0]

    previous_top_cap = 1
    previous_top_face = None
    for depth in range(1, 15):
        cutoff = 4 * depth + 2
        n, cap_profile, cup_profile, face_profile = vertical_iterate(
            template, depth, cutoff
        )
        assert n == 6**depth
        assert cap_profile == cup_profile
        top_cap_rank = 2 * depth + 1
        top_face_rank = 4 * depth
        assert not any(cap_profile[top_cap_rank + 1 :])
        assert not any(face_profile[top_face_rank + 1 :])
        top_cap = cap_profile[top_cap_rank]
        top_face = face_profile[top_face_rank]
        block_size = 6 ** (depth - 1)
        assert top_cap == 10 * block_size**2 * previous_top_cap
        assert top_face == 9 * block_size**2 * previous_top_cap**2
        if depth >= 2:
            previous_block = 6 ** (depth - 2)
            assert Fraction(previous_top_face, previous_top_cap**2) == Fraction(
                9, 100 * previous_block**2
            )
        total_faces = sum(face_profile)
        assert total_faces < 40 * top_face
        assert total_faces + 1 < 40 * top_face
        middle_bank = sum(
            comb(top_face_rank, rank)
            for rank in range(
                (top_face_rank + 2) // 3,
                2 * top_face_rank // 3 + 1,
            )
        )
        average_middle_load = Fraction(
            top_face * middle_bank, total_faces + 1
        )
        assert average_middle_load > Fraction(middle_bank, 40)
        previous_top_cap = top_cap
        previous_top_face = top_face

    # Exact constants in (9)--(13).
    tail_sum = Fraction(3, 10) + Fraction(3, 175)
    assert tail_sum == Fraction(111, 350)
    cap_ratio_bound = Fraction(31, 10) / (1 - tail_sum)
    assert cap_ratio_bound == Fraction(1085, 239) < 5
    cross_bound = 25 * (
        1 + Fraction(20, 54) + Fraction(5, 108)
    )
    assert cross_bound == Fraction(425, 12)
    assert Fraction(1, 15) + cross_bound < 40

    print(
        "PASS: T(4,2) vertical depths=14; top rank=56; "
        "V/top<40; cap-ratio bound=%s" % cap_ratio_bound
    )


if __name__ == "__main__":
    main()
