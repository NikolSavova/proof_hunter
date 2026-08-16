#!/usr/bin/env python3
"""Exact checks for THREE_CLOUD_COMMON_EDGE_DOMINANCE_TRICHOTOMY."""

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys

COMMON = Path(__file__).resolve().parents[1] / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))

from verify_planar_singleton_terminal_two_cell_universal_cage import (  # noqa: E402
    convex,
    general_position,
    make_configuration,
    signs,
    tangent,
)


def comparable(p, q):
    lp, rp = tangent(p)
    lq, rq = tangent(q)
    return (lp < lq and rp < rq) or (lq < lp and rq < rp)


def local_criterion_check():
    F = Fraction
    u, v, w = (F(-1), F(0)), (F(1), F(0)), (F(0), F(-3))
    base = [u, v, w]
    points = [
        (F(13, 50), F(133, 100)),
        (F(-1, 50), F(63, 50)),
        (F(-3, 100), F(51, 50)),
        (F(29, 100), F(41, 25)),
        (F(-1, 20), F(47, 50)),
        (F(-37, 100), F(111, 100)),
    ]
    assert general_position(base + points)
    assert all(convex(base + [p]) for p in points)
    comparable_count = 0
    incomparable_count = 0
    outputs = set()
    for i, j in combinations(range(len(points)), 2):
        comp = comparable(points[i], points[j])
        good = convex(base + [points[i], points[j]])
        assert good == (not comp)
        comparable_count += int(comp)
        incomparable_count += int(not comp)
        if good:
            # Labels i,j and the fixed carrier are physically recovered.
            out = (i, j)
            assert out not in outputs
            outputs.add(out)
    assert comparable_count and incomparable_count
    assert len(outputs) == incomparable_count
    return comparable_count, incomparable_count


def universal_three_cloud_check():
    original, child, u, v, carrier, eps = make_configuration()
    assert signs(original) == signs(child)
    clouds = [[i for i in range(len(child)) if i % 3 == residue]
              for residue in range(3)]

    # The entire transformed child is one strict dominance chain, hence
    # every pair from different named clouds is comparable.
    for a, b in combinations(range(3), 2):
        for i in clouds[a]:
            for j in clouds[b]:
                assert comparable(child[i], child[j])

    carrier_faces = []
    for mask in range(1 << len(carrier)):
        base = [u, v] + [carrier[i] for i in range(len(carrier))
                         if mask >> i & 1]
        assert convex(base)
        carrier_faces.append(base)
        for a, b in combinations(range(3), 2):
            for i in clouds[a]:
                assert convex(base + [child[i]])
                for j in clouds[b]:
                    assert not convex(base + [child[i], child[j]])

    return eps, len(carrier_faces), sum(
        len(clouds[a]) * len(clouds[b]) for a, b in combinations(range(3), 2)
    )


if __name__ == "__main__":
    comp, incomp = local_criterion_check()
    eps, carriers, cross_pairs = universal_three_cloud_check()
    print(
        "PASS: tangent criterion comparable=%d incomparable=%d; "
        "universal cage eps=%s carriers=%d cross-pairs/carrier=%d"
        % (comp, incomp, eps, carriers, cross_pairs)
    )
