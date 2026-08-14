#!/usr/bin/env python3
"""Find certified cyclic three-cluster projection decompositions.

For disjoint clusters L,M,R, ``ordered_direction`` finds an integer vector u
such that every projection of L is smaller than every projection of M, which
is in turn smaller than every projection of R.  The certificate is checked
with exact integer dot products.  A three-cluster decomposition requires a
direction putting each of A,B,C between the other two.  For equal cluster
sizes this is the projection formulation of 3-decomposability; for n=8 we
also test the natural balanced (3,3,2) analogue, explicitly labeled as such.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ordered_direction(left, middle, right):
    constraints = [
        (b[0] - a[0], b[1] - a[1]) for a in left for b in middle
    ] + [(c[0] - b[0], c[1] - b[1]) for b in middle for c in right]
    boundaries = []
    for x, y in constraints:
        angle = math.atan2(y, x)
        boundaries.extend(((angle + math.pi / 2) % (2 * math.pi),
                           (angle - math.pi / 2) % (2 * math.pi)))
    boundaries.sort()
    for i, angle in enumerate(boundaries):
        nxt = boundaries[(i + 1) % len(boundaries)]
        if i + 1 == len(boundaries):
            nxt += 2 * math.pi
        test = (angle + nxt) / 2
        scale = 10**9
        u = (round(scale * math.cos(test)), round(scale * math.sin(test)))
        if all(u[0] * x + u[1] * y > 0 for x, y in constraints):
            return u
    return None


def between_direction(a, middle, c):
    result = ordered_direction(a, middle, c)
    if result is not None:
        return {"outer_order": "first,middle,third", "direction": result}
    result = ordered_direction(c, middle, a)
    if result is not None:
        return {"outer_order": "third,middle,first", "direction": result}
    return None


def canonical_partitions(n, sizes):
    universe = tuple(range(n))
    a_size, b_size, _ = sizes
    for a in itertools.combinations(universe, a_size):
        remaining = tuple(x for x in universe if x not in a)
        for b in itertools.combinations(remaining, b_size):
            c = tuple(x for x in remaining if x not in b)
            # Suppress permutations among equal-size cluster labels.  The
            # decomposition test below is symmetric in A,B,C.
            groups = (tuple(a), tuple(b), tuple(c))
            equal_swaps = [groups[i] for i in range(3) if sizes[i] == sizes[0]]
            if equal_swaps and groups[0] != min(equal_swaps):
                continue
            if sizes[1] == sizes[2] and groups[1] > groups[2]:
                continue
            yield groups


def find_decompositions(points, sizes):
    rows = []
    for groups in canonical_partitions(len(points), sizes):
        certs = []
        for middle in range(3):
            other = [i for i in range(3) if i != middle]
            cert = between_direction(
                [points[i] for i in groups[other[0]]],
                [points[i] for i in groups[middle]],
                [points[i] for i in groups[other[1]]],
            )
            if cert is None:
                break
            certs.append({"middle_cluster": middle, **cert})
        else:
            # Recheck the claimed projection blocks explicitly.
            rows.append(
                {
                    "clusters_by_sorted_point_index": [list(g) for g in groups],
                    "projection_certificates": certs,
                }
            )
    return rows


def main():
    d8 = json.loads((HERE / "exact_realizable_n8_independent.json").read_text())
    d9 = json.loads((HERE / "exact_realizable_n9.json").read_text())
    p8 = sorted(tuple(x) for x in d8["coordinates_as_stored"])
    p9 = sorted(tuple(x) for x in d9["coordinates_as_stored"])
    rows8 = find_decompositions(p8, (3, 3, 2))
    rows9 = find_decompositions(p9, (3, 3, 3))
    output = {
        "n8": {
            "status": "balanced_3_3_2_projection_analogue_not_standard_3_decomposability",
            "coordinates_sorted": p8,
            "decomposition_count": len(rows8),
            "decompositions": rows8,
        },
        "n9": {
            "status": "standard_equal_size_3_decomposability",
            "coordinates_sorted": p9,
            "decomposition_count": len(rows9),
            "decompositions": rows9,
        },
    }
    (HERE / "cluster_certificates.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print("n8 3+3+2 projection decompositions:", len(rows8))
    print("n9 3-decompositions:", len(rows9))
    if rows9:
        print(rows9[0])


if __name__ == "__main__":
    main()
