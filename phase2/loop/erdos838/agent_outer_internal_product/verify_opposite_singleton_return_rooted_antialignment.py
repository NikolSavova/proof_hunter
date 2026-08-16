#!/usr/bin/env python3
"""Exact audit for OPPOSITE_SINGLETON_RETURN_AND_ROOTED_PROFILE_ANTI_ALIGNMENT_GATE."""

from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from verify_source_reuse_balanced_one_ended_profile import (  # noqa: E402
    configuration,
    convex as cage_convex,
)

sys.path.insert(0, str(ROOT / "agent_shield_circuit_cover"))
from verify_strong_separation_endpoint_profile_counterexample import (  # noqa: E402
    construction,
    convex as rooted_convex,
    hull,
)


def profile(block, roots, convexity, include_empty=True):
    count = 0
    start = 0 if include_empty else 1
    for mask in range(start, 1 << len(block)):
        trace = tuple(block[i] for i in range(len(block)) if mask >> i & 1)
        count += int(convexity(trace + tuple(roots)))
    return count


def main():
    # Opposite singleton profiles of the balanced Boolean source.
    _, source, left, right = configuration()
    q = len(source)
    p_left = profile(source, (left[0],), cage_convex)
    p_right = profile(source, (right[0],), cage_convex)
    assert (p_left, p_right) == (82, 82)
    assert p_left * p_right >= 2**q
    far_left = set(hull(tuple(source) + (left[0],))) & set(source)
    far_right = set(hull(tuple(source) + (right[0],))) & set(source)
    assert len(far_left) == len(far_right) == 5
    assert far_left | far_right == set(source)
    for far, endpoint in ((far_left, left[0]), (far_right, right[0])):
        far = tuple(far)
        for mask in range(1 << len(far)):
            trace = tuple(far[i] for i in range(len(far)) if mask >> i & 1)
            assert cage_convex(trace + (endpoint,))

    # Rooted two-direction profiles: the common root destroys the product.
    m = 14
    block, a, b, c = construction(m)
    assert profile(block, (), rooted_convex) == 2**m
    cap = profile(block, (a, c), rooted_convex)
    cup = profile(block, (b, c), rooted_convex)
    assert (cap, cup) == (86, 106)
    assert cap * cup == 9116 < 2**m

    cap_nonempty = profile(block, (a, c), rooted_convex, False)
    cup_nonempty = profile(block, (b, c), rooted_convex, False)
    assert (cap_nonempty, cup_nonempty) == (85, 105)
    assert cap_nonempty * cup_nonempty < 2**m - 1

    # Exact algebra of the conditional return bank.
    s_left, s_right = 3, 5
    k_left, k_right = 7, 11
    bank_left = k_left * 2**s_left
    bank_right = k_right * 2**s_right
    assert max(bank_left, bank_right) ** 2 >= (
        k_left * k_right * 2 ** (s_left + s_right)
    )

    print(
        "PASS: opposite singleton profiles=(%d,%d), rooted profiles=(%d,%d), "
        "rooted product=%d<%d"
        % (p_left, p_right, cap, cup, cap * cup, 2**m)
    )


if __name__ == "__main__":
    main()
