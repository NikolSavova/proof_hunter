#!/usr/bin/env python3
"""Exact checks for the hereditary rank-k tag/Cauchy gate."""

from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
COMMON = ROOT / "agent_common_shield_mixing"
sys.path.insert(0, str(COMMON))
import verify_dense_hall_two_cloud_profile_barrier as dense  # noqa: E402


def abstract_tag_cauchy():
    # Deliberately overlapping sources and tags.
    contexts = [
        (Q(1, 2), {"a0", "a1", "a2"}, {"t0", "t1", "t2", "t3"}, 6),
        (Q(2, 3), {"a1", "a2", "a3"}, {"t2", "t3", "t4", "t5"}, 6),
        (Q(3, 5), {"a3", "a4"}, {"t0", "t5"}, 2),
    ]
    source_load = {}
    pair_load = {}
    source_mass = tag_mass = demand = Q(0)
    gamma = Q(3)
    for weight, sources, tags, edges in contexts:
        source_mass += weight * len(sources)
        tag_mass += weight * len(tags)
        demand += weight * edges
        canonical = min(sources)
        for source in sources:
            source_load[source] = source_load.get(source, Q(0)) + weight
        for tag in tags:
            key = (canonical, tag)
            pair_load[key] = pair_load.get(key, Q(0)) + weight
        assert edges * edges <= gamma * len(sources) * len(tags)

    kappa = max(source_load.values())
    source_universe = set().union(*(part[1] for part in contexts))
    tag_universe = set().union(*(part[2] for part in contexts))
    assert max(pair_load.values()) <= kappa
    assert source_mass <= kappa * len(source_universe)
    assert tag_mass <= kappa * len(source_universe) * len(tag_universe)
    assert demand * demand <= gamma * source_mass * tag_mass
    assert demand * demand <= (
        gamma * kappa * kappa
        * len(source_universe) * len(source_universe)
        * len(tag_universe)
    )
    return kappa, len(source_universe), len(tag_universe), demand


def support_and_shadow_thresholds():
    # The universal support-triangle gate for a balanced complete rectangle
    # is possible only when the physical support is comparable with the
    # face alphabet.
    for alphabet in range(6, 101):
        edges = alphabet * alphabet
        least_support = next(
            support for support in range(3, 1000)
            if 5 * edges * edges <= 54 * alphabet * comb(support, 3)
        )
        assert least_support <= 2 * alphabet

    # A rank-r face has at most 2^r hereditary subface tags.  For a
    # balanced m-by-m rectangle, even the union of all per-face downsets
    # cannot meet i >= m^3/Gamma when m^2 > Gamma*2^r.
    barriers = 0
    for rank in range(3, 15):
        for alphabet in (2**rank, 2 ** (rank + 2), 3**rank):
            maximum_shadow = alphabet * (1 << rank)
            required = alphabet**3
            if alphabet * alphabet > (1 << rank):
                assert maximum_shadow < required
                barriers += 1
    return barriers


def anti_aligned_face_rectangle():
    size, rank = 7, 3
    guards = dense.parabolic_cloud(dense.G0, size, 1)
    pockets = dense.parabolic_cloud(dense.X0, size, -1)
    rows = list(combinations(guards, rank))
    columns = list(combinations(pockets, rank))
    assert all(dense.convex(face) for face in rows + columns)

    bad = 0
    for row in rows:
        for column in columns:
            assert not dense.convex(row + column)
            bad += 1
    alphabet = comb(size, rank)
    assert len(rows) == len(columns) == alphabet == 35
    assert bad == alphabet * alphabet == 1225

    # The complete rank-at-most-r downshadow of all rank-r faces on one
    # seven-point cloud is exactly all subsets through rank r.
    downshadow = {
        frozenset(part)
        for face in columns
        for subrank in range(rank + 1)
        for part in combinations(face, subrank)
    }
    expected_shadow = sum(comb(size, subrank)
                          for subrank in range(rank + 1))
    assert len(downshadow) == expected_shadow == 64

    edges = alphabet * alphabet
    required_tags = Q(edges * edges, alphabet)
    assert required_tags == alphabet**3 == 42875
    assert len(downshadow) < required_tags
    assert 5 * edges * edges > 54 * alphabet * len(downshadow)

    # First-point projection is highly reused.
    mark_load = max(
        sum(1 for face in rows if min(face) == point)
        for point in guards
    )
    assert mark_load == comb(size - 1, rank - 1)
    return alphabet, bad, len(downshadow), required_tags, mark_load


def free_rank_scale():
    # If K=n^(sigma loglog n), tags of rank
    # k <= (2 sigma-epsilon)loglog n cost o(K) after square root.
    sigma = Q(1, 3)
    epsilon = Q(1, 12)
    checks = 0
    for loglog_n in range(20, 101):
        tag_rank = int((2 * sigma - epsilon) * loglog_n)
        tag_exponent = Q(tag_rank, 2)
        recovery_exponent = sigma * loglog_n
        assert tag_exponent < recovery_exponent
        checks += 1
    return checks


def main():
    abstract = abstract_tag_cauchy()
    thresholds = support_and_shadow_thresholds()
    rectangle = anti_aligned_face_rectangle()
    scale = free_rank_scale()
    print(
        "PASS: abstract=%s thresholds=%d; rectangle alphabet=%d bad=%d "
        "shadow=%d required=%s mark_load=%d; scale=%d"
        % (abstract, thresholds, *rectangle, scale)
    )


if __name__ == "__main__":
    main()
