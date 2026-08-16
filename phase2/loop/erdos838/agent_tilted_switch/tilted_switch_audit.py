#!/usr/bin/env python3
"""Exact checks for the first-failure tilted switching attack on Erdos 838.

The script uses integer orientations only.  It verifies the repair-degree
bound on exhaustive finite records, the boundary-switch identity, and the
stable-postponement obstruction on the exact n=8 and n=9 minimizers.
"""

from __future__ import annotations

import itertools
import json
import math
import random
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def orient(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def forbidden_circuits(points: list[tuple[int, int]]) -> list[int]:
    """Return the non-convex four-subsets, as bit masks."""
    answer: list[int] = []
    for four in itertools.combinations(range(len(points)), 4):
        signs = []
        for triple in itertools.combinations(four, 3):
            value = orient(points[triple[0]], points[triple[1]], points[triple[2]])
            assert value != 0
            signs.append(1 if value > 0 else -1)
        # Direct hull test: a four-set is nonconvex iff one point lies in the
        # triangle of the other three.  The four omitted-point orientations
        # have the alternating signs appropriate to the affine dependence.
        nonconvex = False
        for root in four:
            tri = [x for x in four if x != root]
            tri_sign = orient(points[tri[0]], points[tri[1]], points[tri[2]])
            side = [orient(points[tri[i]], points[tri[(i + 1) % 3]], points[root])
                    for i in range(3)]
            if all(x * tri_sign > 0 for x in side):
                nonconvex = True
                break
        if nonconvex:
            answer.append(sum(1 << x for x in four))
    return answer


def face_table(points: list[tuple[int, int]]) -> bytearray:
    """All convex-position subsets, via an exact upward circuit zeta pass."""
    n = len(points)
    bad = bytearray(1 << n)
    for circuit in forbidden_circuits(points):
        bad[circuit] = 1
    # Mark every superset of a forbidden rooted four-circuit.
    for bit in range(n):
        step = 1 << bit
        for base in range(0, 1 << n, step << 1):
            left = base
            right = base + step
            for offset in range(step):
                if bad[left + offset]:
                    bad[right + offset] = 1
    return bytearray(1 - value for value in bad)


def profile(faces: bytearray, n: int) -> list[int]:
    out = [0] * (n + 1)
    for mask, good in enumerate(faces):
        if good:
            out[mask.bit_count()] += 1
    return out


def repair_degree(mask: int, faces: bytearray) -> int:
    return sum(faces[mask ^ (1 << q)] for q in range(mask.bit_length()) if mask >> q & 1)


def boundary_statistics(faces: bytearray, n: int) -> dict[str, object]:
    """Compute B_r=sum_A b(A), T_r=sum_A b(A)u(A), and repair maxima."""
    boundary = [0] * (n + 1)
    mixed = [0] * (n + 1)
    maximal_faces = [0] * (n + 1)
    max_repair = [0] * (n + 1)
    repair_hist: dict[int, Counter[int]] = defaultdict(Counter)

    full = (1 << n) - 1
    for mask, good in enumerate(faces):
        if not good:
            d = repair_degree(mask, faces)
            if d:
                size = mask.bit_count()
                max_repair[size] = max(max_repair[size], d)
                repair_hist[size][d] += 1
            continue
        r = mask.bit_count()
        outside = full ^ mask
        u = 0
        remaining = outside
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            u += faces[mask | bit]
        b = n - r - u
        boundary[r] += b
        mixed[r] += b * u
        if u == 0:
            maximal_faces[r] += 1

    for r in range(3, n - 1):
        assert (r - 1) * boundary[r + 1] <= mixed[r]
        assert mixed[r] <= (r + 1) * boundary[r + 1]
    assert max(max_repair[5:], default=0) <= 3
    assert max(max_repair[4:5], default=0) <= 4
    return {
        "boundary_B_r": boundary,
        "mixed_sum_b_times_u": mixed,
        "maximal_face_counts": maximal_faces,
        "maximum_repair_degree_by_size": max_repair,
        "repair_degree_histograms": {
            str(size): dict(sorted(hist.items())) for size, hist in sorted(repair_hist.items())
        },
        "switch_inequality": "(r-1) B_(r+1) <= sum_{|A|=r} b(A)u(A) <= (r+1) B_(r+1)",
    }


def stopping_rank(permutation: tuple[int, ...], faces: bytearray) -> int:
    mask = 0
    for r, point in enumerate(permutation):
        mask |= 1 << point
        if not faces[mask]:
            return r
    return len(permutation)


def stable_postpone(permutation: tuple[int, ...], faces: bytearray) -> tuple[int, ...]:
    """Keep the initial convex prefix, then stably accept or postpone the tail."""
    r = stopping_rank(permutation, faces)
    if r == len(permutation):
        return permutation
    prefix = list(permutation[:r])
    mask = sum(1 << q for q in prefix)
    accepted: list[int] = []
    rejected: list[int] = []
    for q in permutation[r:]:
        if faces[mask | (1 << q)]:
            accepted.append(q)
            mask |= 1 << q
        else:
            rejected.append(q)
    image = tuple(prefix + accepted + rejected)
    assert stopping_rank(image, faces) == r + len(accepted)
    return image


def postponement_census(points: list[tuple[int, int]], faces: bytearray) -> dict[str, object]:
    """Exhaust all permutations (used only at n<=9) and count map fibres."""
    n = len(points)
    fibres: Counter[tuple[int, ...]] = Counter()
    gains = Counter()
    immobile = Counter()
    for permutation in itertools.permutations(range(n)):
        r = stopping_rank(permutation, faces)
        image = stable_postpone(permutation, faces)
        rp = stopping_rank(image, faces)
        fibres[image] += 1
        gains[rp - r] += 1
        if rp == r < n:
            immobile[r] += 1
    maximum = max(fibres.values())
    witness = next(list(image) for image, value in fibres.items() if value == maximum)
    return {
        "permutations": __import__("math").factorial(n),
        "gain_histogram": dict(sorted(gains.items())),
        "immobile_stopped_permutations_by_rank": dict(sorted(immobile.items())),
        "maximum_stable_postponement_fibre": maximum,
        "maximum_fibre_image": witness,
    }


def nested_triangle_points(h: int, d: int) -> tuple[list[tuple[int, int]], list[int], list[int], list[int]]:
    """A convex h-gon H and d general-position points inside a triangle A in H."""
    scale = 1_000_003
    outer = [(scale * i, scale * i * i) for i in range(h)]
    a_indices = [0, h // 2, h - 1]
    triangle = [outer[i] for i in a_indices]
    points = list(outer)
    rng = random.Random(838_20260813 + 1000 * h + d)
    while len(points) < h + d:
        alpha = rng.randrange(1, scale - 2)
        beta = rng.randrange(1, scale - alpha - 1)
        gamma = scale - alpha - beta
        candidate = (
            (alpha * triangle[0][0] + beta * triangle[1][0] + gamma * triangle[2][0]) // scale,
            (alpha * triangle[0][1] + beta * triangle[1][1] + gamma * triangle[2][1]) // scale,
        )
        if candidate in points:
            continue
        if all(orient(points[i], points[j], candidate) != 0
               for i in range(len(points)) for j in range(i + 1, len(points))):
            points.append(candidate)
    outer_set = set(range(h))
    a_set = set(a_indices)
    return points, a_indices, sorted(outer_set - a_set), list(range(h, h + d))


def binomial_sum(n: int, r: int) -> int:
    return sum(math.comb(n, k) for k in range(r + 1))


def postponement_counterfamily() -> dict[str, object]:
    """Verify a finite geometric member and the exact all-n congestion formula."""
    h, d = 5, 4
    points, a_order, g_order, d_order = nested_triangle_points(h, d)
    faces = face_table(points)
    image = tuple(a_order + g_order + d_order)
    assert stopping_rank(image, faces) == h
    source_count = 0
    tilted_load = 0
    gain_histogram: Counter[int] = Counter()
    # All shuffles preserve the orders internal to G and D.
    for g_positions in itertools.combinations(range(len(g_order) + len(d_order)), len(g_order)):
        g_positions = set(g_positions)
        gi = di = 0
        tail = []
        for position in range(len(g_order) + len(d_order)):
            if position in g_positions:
                tail.append(g_order[gi])
                gi += 1
            else:
                tail.append(d_order[di])
                di += 1
        source = tuple(a_order + tail)
        assert stable_postpone(source, faces) == image
        rank = stopping_rank(source, faces)
        source_count += 1
        tilted_load += binomial_sum(h + d, rank)
        gain_histogram[h - rank] += 1
    assert source_count == math.comb(h + d - 3, h - 3)

    asymptotic_rows = []
    for n in (100, 1000, 5000):
        hh = int(math.log2(n))
        gg = hh - 3
        dd = n - hh
        load = sum(
            math.comb(gg - k + dd - 1, gg - k) * binomial_sum(n, 3 + k)
            for k in range(gg + 1)
        )
        target = binomial_sum(n, hh)
        ratio = Fraction(load, target)
        # The ratio is asymptotic to 2^h, hence polynomial (Theta(n)) for
        # h=floor(log_2 n), not subpolynomial.
        asymptotic_rows.append({
            "n": n,
            "h": hh,
            "tilted_load": str(load),
            "target_tilt": str(target),
            "load_over_target_exact": str(ratio),
            "load_over_target_decimal": float(ratio),
            "ratio_over_2_to_h": float(ratio / (1 << hh)),
        })
    return {
        "finite_geometric_member": {
            "n": h + d,
            "h_outer": h,
            "d_inner": d,
            "coordinates": [list(point) for point in points],
            "outer_triangle_A": a_order,
            "remaining_outer_G": g_order,
            "inner_D": d_order,
            "shuffle_sources_in_one_fibre": source_count,
            "tilted_load": tilted_load,
            "target_tilt": binomial_sum(h + d, h),
            "tilted_congestion": str(Fraction(tilted_load, binomial_sum(h + d, h))),
            "gain_histogram": dict(sorted(gain_histogram.items())),
        },
        "formula": (
            "L(n,h)=sum_{k=0}^{h-3} C(n-k-4,h-k-3) S_{k+3}(1); "
            "L(n,h)/S_h(1)=(1-o(1))(2^h-1-h-C(h,2)) when h=o(n)"
        ),
        "asymptotic_exact_rows": asymptotic_rows,
    }


def main() -> None:
    records = json.loads((ROOT / "agent_lex_minimizer_search" / "direct_hull_certificates.json").read_text())
    certificate: dict[str, object] = {
        "claim_boundary": (
            "Finite enumeration verifies the universal repair lemma and switch identity on the "
            "exact minimizers; it is not evidence for the still-open maximal-face restart bound."
        ),
        "records": {},
        "stable_postponement_counterfamily": postponement_counterfamily(),
    }
    for n in (8, 9):
        points = [tuple(point) for point in records[str(n)]["coordinates"]]
        faces = face_table(points)
        got_profile = profile(faces, n)
        expected = [1] + records[str(n)]["profile_nonempty"][1:]
        assert got_profile == expected
        row = {
            "n": n,
            "coordinates": [list(point) for point in points],
            "profile": got_profile,
            "boundary": boundary_statistics(faces, n),
            "postponement": postponement_census(points, faces),
        }
        certificate["records"][str(n)] = row

    search_records = json.loads(
        (ROOT / "agent_dual_number_amortization" / "half_weight_search_records.json").read_text()
    )
    ys20 = search_records["exact_records"]["20"]["y_at_x_0_through_19"]
    points20 = list(enumerate(ys20))
    faces20 = face_table(points20)
    profile20 = profile(faces20, 20)
    assert profile20 == [1, 20, 190, 1140, 2415, 866, 135, 8] + [0] * 13
    certificate["records"]["20"] = {
        "n": 20,
        "coordinate_format": "(i,y_i), with y_i stored below",
        "y_at_x_0_through_19": ys20,
        "profile": profile20,
        "boundary": boundary_statistics(faces20, 20),
        "postponement": "not enumerated (20! permutations)",
    }

    path = HERE / "certificate.json"
    path.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
    print(json.dumps(certificate, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
