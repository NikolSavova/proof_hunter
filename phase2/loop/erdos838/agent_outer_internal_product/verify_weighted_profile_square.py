#!/usr/bin/env python3
"""Exact audit for WEIGHTED_PROFILE_SQUARE_GATE.md."""

import sys
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_prevalence_common_cage as cage  # noqa: E402


def build_instance():
    p, r, m = 5, 2, 4
    points = []
    u = tuple(range(len(points), len(points) + p))
    points.extend(cage.circle(F(35 + 5 * i, 1000)) for i in range(p))
    v = tuple(range(len(points), len(points) + p))
    points.extend(cage.circle(F(1690 + 10 * i, 1000)) for i in range(p))
    w = tuple(range(len(points), len(points) + p))
    points.extend(cage.circle(F(-1770 + 10 * i, 1000)) for i in range(p))
    optional = tuple(range(len(points), len(points) + r))
    points.extend(cage.circle(F(-1710 + 10 * i, 1000)) for i in range(r))
    inner = tuple(range(len(points), len(points) + m))
    shift = (F(1, 1000), F(-1, 2000))
    inner_parameters = (F(1, 7), F(3, 5), F(5, 3), F(-4))
    points.extend(cage.circle(t, F(1, 100), shift) for t in inner_parameters)
    core = tuple(sorted(u + v + w))
    root = tuple(sorted((u[-1], v[0], w[2])))
    sources = [tuple(sorted(core + chosen)) for chosen in cage.powerset(optional)]
    return points, root, inner, sources, u, v, w


def main():
    points, root, inner, sources, u, v, w = build_instance()
    n = len(points)
    assert all(cage.cross(points[i], points[j], points[k]) != 0
               for i, j, k in combinations(range(n), 3))

    # U and V complete every source.  W completes only the source without
    # optional W-arc labels.
    base_source = min(sources, key=len)
    profile_data = (
        (u, next(iter(set(root) & set(u))), sources),
        (v, next(iter(set(root) & set(v))), sources),
        (w, next(iter(set(root) & set(w))), (base_source,)),
    )

    carrier_outputs = Counter()
    completion_outputs = Counter()
    local_sizes = []
    total_weight = 0
    for guard, z, profile_sources in profile_data:
        assert set(guard) & set(root) == {z}
        edge = set(root) - {z}
        carrier_count = 0
        completion_count = 0
        for source in profile_sources:
            assert set(guard) <= set(source)
            base = set(source) - set(guard)
            assert edge <= base

            for d in cage.powerset(tuple(x for x in guard if x != z)):
                restored = set(d) | {z}
                output = tuple(sorted(base | restored))
                assert cage.convex(output, points)
                assert set(root) <= set(output)
                decoded_d = set(output) & set(guard)
                decoded_source = (set(output) - decoded_d) | set(guard)
                assert decoded_d == restored
                assert decoded_source == set(source)
                carrier_outputs[output] += 1
                carrier_count += 1

                # Restoring z retains the whole root and kills every mixed
                # carrier/completion product.
                for x in inner:
                    mixed = tuple(sorted(set(output) | {x}))
                    assert not cage.convex(mixed, points)

            for x in inner:
                output = tuple(sorted(base | {x}))
                assert cage.convex(output, points)
                assert edge <= set(output)
                decoded_x = set(output) & set(inner)
                decoded_source = (set(output) - decoded_x) | set(guard)
                assert decoded_x == {x}
                assert decoded_source == set(source)
                completion_outputs[output] += 1
                completion_count += 1

        weight = len(profile_sources)
        assert carrier_count == weight * 2 ** (len(guard) - 1)
        assert completion_count == weight * len(inner)
        local_sizes.append((carrier_count, completion_count))
        total_weight += weight

    assert total_weight == 9
    assert local_sizes == [(64, 16), (64, 16), (16, 4)]
    assert sum(carrier_outputs.values()) == 144
    assert sum(completion_outputs.values()) == 36

    # Each profile has sqrt(2^(p-1)*m)=8 times its source weight.
    cauchy_left = total_weight * 8
    assert cauchy_left == 72
    assert cauchy_left ** 2 == 144 * 36

    print("PASS: weighted profile square gate")
    print(f"  profile source weight W={total_weight}")
    print(f"  carrier records={sum(carrier_outputs.values())}, "
          f"max overlap={max(carrier_outputs.values())}")
    print(f"  completion records={sum(completion_outputs.values())}, "
          f"max overlap={max(completion_outputs.values())}")
    print("  Cauchy audit: 72^2 = 144*36")
    print("  every pointwise carrier/completion product is nonconvex")


if __name__ == "__main__":
    main()
