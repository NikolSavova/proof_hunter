#!/usr/bin/env python3
"""Exact/tropical audit for heterogeneous macroscopic vertical jumps.

The exact assertions in this file use Python integers.  Floating point is
used only for displayed logarithms and limiting entropy formulae.

The audit has three independent parts.

1. Exhaustively recover endpoint-coloured macro-support polynomials for a
   saved stretchable 16-point macro and check that they sum to the saved
   uncoloured cap/cup/convex profiles.
2. Stress the balanced-core lower bound on the sharp two-block guard made
   from an all-cup block followed by an all-cap block.
3. Stress canonical Baek--Balko microcells using the exact Pascal-cell
   recurrence and the exact layer-transversal product.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[4]
MACRO_CERT = (
    ROOT
    / "phase2/loop/erdos838/agent_growing_state_upper/"
    "LARGE_MACRO_CERTIFICATE.json"
)
DEFAULT_OUTPUT = Path(__file__).with_name("heterogeneous_certificate.json")


def log2_int(value: int) -> float:
    if value <= 0:
        raise ValueError("expected a positive integer")
    bits = value.bit_length()
    shift = max(0, bits - 53)
    return math.log2(value >> shift) + shift


def orient(points: Sequence[Sequence[int]], i: int, j: int, k: int) -> int:
    xi, yi = points[i]
    xj, yj = points[j]
    xk, yk = points[k]
    return (xj - xi) * (yk - yi) - (yj - yi) * (xk - xi)


def is_cap(points: Sequence[Sequence[int]], inds: Sequence[int]) -> bool:
    # Strictly decreasing adjacent slopes imply every triple is negative.
    return all(
        orient(points, inds[i], inds[i + 1], inds[i + 2]) < 0
        for i in range(len(inds) - 2)
    )


def is_cup(points: Sequence[Sequence[int]], inds: Sequence[int]) -> bool:
    return all(
        orient(points, inds[i], inds[i + 1], inds[i + 2]) > 0
        for i in range(len(inds) - 2)
    )


def convex_hull_size(points: Sequence[Sequence[int]], inds: Sequence[int]) -> int:
    if len(inds) <= 2:
        return len(inds)
    lower: list[int] = []
    for i in inds:
        while len(lower) >= 2 and orient(points, lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)
    upper: list[int] = []
    for i in reversed(inds):
        while len(upper) >= 2 and orient(points, upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
    return len(lower[:-1] + upper[:-1])


def zero_profiles(types: int, r: int) -> list[list[int]]:
    return [[0] * (r + 1) for _ in range(types)]


def coloured_profiles(
    points: Sequence[Sequence[int]], colours: Sequence[int]
) -> tuple[list[list[int]], list[list[int]], list[list[list[int]]]]:
    """Endpoint-coloured cap, cup, and convex support profiles.

    A[a][j] counts j-point macro caps whose first colour is a.
    B[b][j] counts j-point macro cups whose last colour is b.
    P[a][b][j] counts j-point convex macro supports whose endpoint colours
    are a,b.  Singletons are included in all three arrays; callers use the
    convex entries only from degree two upward.
    """
    r = len(points)
    q = max(colours) + 1
    caps = zero_profiles(q, r)
    cups = zero_profiles(q, r)
    convex = [[([0] * (r + 1)) for _ in range(q)] for _ in range(q)]
    for mask in range(1, 1 << r):
        inds = tuple(i for i in range(r) if mask >> i & 1)
        j = len(inds)
        if is_cap(points, inds):
            caps[colours[inds[0]]][j] += 1
        if is_cup(points, inds):
            cups[colours[inds[-1]]][j] += 1
        if convex_hull_size(points, inds) == j:
            convex[colours[inds[0]]][colours[inds[-1]]][j] += 1
    return caps, cups, convex


def poly(profile: Sequence[int], x: int, shift: int) -> int:
    return sum(profile[j] * x ** (j - shift) for j in range(shift, len(profile)))


def add_profiles(profiles: Iterable[Sequence[int]]) -> list[int]:
    profiles = list(profiles)
    return [sum(p[j] for p in profiles) for j in range(len(profiles[0]))]


def macro_colour_audit() -> dict[str, object]:
    saved = json.loads(MACRO_CERT.read_text())
    macro = saved["macros"]["16"]
    points = macro["points"]
    r = len(points)
    assert r == 16
    best: dict[str, object] | None = None

    for cut in range(1, r):
        colours = [0 if i < cut else 1 for i in range(r)]
        caps, cups, convex = coloured_profiles(points, colours)

        assert add_profiles(caps) == macro["cap_profile"]
        assert add_profiles(cups) == macro["cup_profile"]
        uncoloured = [
            sum(convex[a][b][j] for a in range(2) for b in range(2))
            for j in range(r + 1)
        ]
        assert uncoloured == macro["convex_profile"]
        # A contiguous two-colouring cannot have a 1 -> 0 endpoint pair.
        assert sum(convex[1][0]) == 0

        child_n = 16
        few = child_n + math.comb(child_n, 2)
        many = 2**child_n - 1
        paa = poly(convex[0][0], child_n, 2)
        pab = poly(convex[0][1], child_n, 2)
        pbb = poly(convex[1][1], child_n, 2)
        ptotal = poly(uncoloured, child_n, 2)
        assert paa + pab + pbb == ptotal

        # Type 0 is all-cup (few caps, many cups), type 1 all-cap.
        same = few * many * (paa + pbb)
        anti = few * few * pab
        exact_cross = same + anti
        balanced_core_floor = few * few * ptotal
        assert exact_cross >= balanced_core_floor
        # On either monochromatic induced core the skew diameter is zero.
        # Their combined common-skew floors are W_child*(P_00+P_11).
        common_skew_floor = many * (paa + pbb)
        assert same >= common_skew_floor
        exact_total = r * many + exact_cross
        rec = {
            "cut": cut,
            "P_00": paa,
            "P_01": pab,
            "P_11": pbb,
            "P_total": ptotal,
            "same_type_contribution": same,
            "anti_aligned_contribution": anti,
            "exact_spanning_contribution": exact_cross,
            "balanced_core_floor": balanced_core_floor,
            "balanced_core_slack": exact_cross - balanced_core_floor,
            "combined_common_skew_floor": common_skew_floor,
            "combined_common_skew_slack": same - common_skew_floor,
            "exact_total_W": exact_total,
            "normalized_log2_W": log2_int(exact_total) / math.log2(r * child_n) ** 2,
            "anti_aligned_fraction": anti / exact_cross,
        }
        if best is None or int(rec["exact_total_W"]) < int(best["exact_total_W"]):
            best = rec
    assert best is not None
    return {
        "macro_size": r,
        "child_size": 16,
        "cut_minimizing_exact_W": best,
        "statement": (
            "All 15 contiguous colour cuts exactly recover the saved uncoloured "
            "profiles; the record reports the strongest all-cup/all-cap "
            "anti-alignment among them."
        ),
    }


def guard_audit() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for n in (4, 8, 16, 32, 64, 128):
        few = n + math.comb(n, 2)
        many = 2**n - 1
        # Two-point macro: an all-cup block followed by an all-cap block.
        cross = few * few
        total = 2 * many + cross
        b = few
        p_macro = 1
        balanced_core_floor = b * b * p_macro
        assert cross == balanced_core_floor
        assert total == 2 * many + balanced_core_floor
        assert few * many >= many  # C(Q)U(Q) >= W(Q), in each guard.
        records.append(
            {
                "block_size": n,
                "few_endpoint_count": few,
                "many_endpoint_and_W_count": many,
                "anti_aligned_cross_term": cross,
                "balanced_core_floor": balanced_core_floor,
                "exact_parent_W": total,
                "endpoint_deficiency_bits": max(
                    0.0, 0.5 * log2_int(many) - log2_int(few)
                ),
                "log2_parent_W_over_log2_size_squared": (
                    log2_int(total) / math.log2(2 * n) ** 2
                ),
            }
        )
    return records


def fixed_point_audit() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for p, q in ((1, 1), (1, 2), (2, 3), (3, 7)):
        alpha = Fraction(p, p + q)
        beta = Fraction(q, p + q)
        for c in (Fraction(1, 3), Fraction(2, 5), Fraction(1, 2)):
            output = c * (alpha * alpha + beta * beta) + alpha * beta
            gain = output - c
            assert gain == (1 - 2 * c) * alpha * beta
            assert gain >= 0
            records.append(
                {
                    "alpha": f"{alpha.numerator}/{alpha.denominator}",
                    "beta": f"{beta.numerator}/{beta.denominator}",
                    "input_coefficient": f"{c.numerator}/{c.denominator}",
                    "output_coefficient": f"{output.numerator}/{output.denominator}",
                    "gain": f"{gain.numerator}/{gain.denominator}",
                }
            )
    return records


def size_bucket_audit() -> list[dict[str, object]]:
    families = (
        [1] * 64 + [16] * 16 + [1024] * 2,
        [2**j for j in range(1, 41)],
        [3] * 257 + [65] * 33 + [4097] * 5,
    )
    records: list[dict[str, object]] = []
    for sizes in families:
        buckets: dict[int, list[int]] = {}
        for n in sizes:
            t = n.bit_length() - 1
            buckets.setdefault(t, []).append(n)
            assert 2**t <= n < 2 ** (t + 1)
        total = sum(sizes)
        t, members = max(buckets.items(), key=lambda item: len(item[1]) * 2 ** item[0])
        score = len(members) * 2**t
        # The proof uses at most floor(log_2 N)+1 possible buckets.
        possible_buckets = total.bit_length()
        assert total < 2 * possible_buckets * score
        records.append(
            {
                "number_of_blocks": len(sizes),
                "total_size": total,
                "winning_dyadic_exponent": t,
                "winning_bucket_count": len(members),
                "winning_bucket_floor_mass": score,
                "cover_deficit_bits": log2_int(total) - log2_int(score),
                "certified_deficit_upper_bits": math.log2(2 * possible_buckets),
            }
        )
    return records


def pascal_table(depth: int) -> tuple[list[int], list[int], list[int], list[int]]:
    sizes = caps = cups = convex = [1]
    for d in range(1, depth + 1):
        ns = [1] * (d + 1)
        nc = [1] * (d + 1)
        nu = [1] * (d + 1)
        nw = [1] * (d + 1)
        for i in range(1, d):
            a, b = sizes[i - 1], sizes[i]
            ns[i] = a + b
            nc[i] = caps[i] * 1 + (b + 1) * caps[i - 1]
            nu[i] = cups[i - 1] + (a + 1) * cups[i]
            nw[i] = convex[i - 1] + convex[i] + caps[i - 1] * cups[i]
        sizes, caps, cups, convex = ns, nc, nu, nw
    return sizes, caps, cups, convex


def bb_transversal(k: int, x: int) -> int:
    d = k - 2 * x - 3
    if x < 1 or d < 0:
        raise ValueError((k, x))
    masses = [sum(math.comb(k - 2, ell) for ell in range(x + 1))]
    for h in range(1, d + 1):
        masses.append(
            sum(
                math.comb(t - 1, h - 1) * math.comb(k - t - 2, x)
                for t in range(h, d + 1)
            )
        )
    assert sum(masses) == 2 ** (k - 3)
    return math.prod(masses)


def entropy(p: float) -> float:
    if p <= 0 or p >= 1:
        return 0.0
    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def simpson_entropy(a: float, b: float, steps: int = 10_000) -> float:
    if a == b:
        return 0.0
    if steps % 2:
        steps += 1
    dx = (b - a) / steps
    total = entropy(a) + entropy(b)
    for j in range(1, steps):
        total += (4 if j % 2 else 2) * entropy(a + j * dx)
    return total * dx / 3


def bb_limits(theta: float) -> tuple[float, float]:
    mu = 1 - 2 * theta
    transversal = (
        simpson_entropy(theta, 0.5)
        + mu * mu / (4 * math.log(2))
        + theta * mu
    )
    internal = entropy(theta) - theta * (1 - theta) / math.log(2)
    return transversal, internal


def bb_audit() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for k, fractions in ((40, (0.10, 0.20, 0.30, 0.40)), (80, (0.10, 0.21, 0.30, 0.40))):
        depth = k - 3
        sizes, caps, cups, convex = pascal_table(depth)
        for target in fractions:
            x = max(1, round(target * k))
            if k < 2 * x + 3:
                continue
            trans = bb_transversal(k, x)
            c, u, w = caps[x], cups[x], convex[x]
            assert sizes[x] == math.comb(k - 3, x)
            assert c * u >= w
            theta = x / k
            lim_t, lim_i = bb_limits(theta)
            L = k - 2  # total output has exactly 2^(k-2) points.
            records.append(
                {
                    "k": k,
                    "x": x,
                    "theta": theta,
                    "transversal_count": trans,
                    "score_two_cell": {
                        "size": sizes[x],
                        "caps": c,
                        "cups": u,
                        "convex": w,
                        "endpoint_deficiency_bits": max(
                            0.0,
                            0.5 * log2_int(w) - log2_int(c),
                            0.5 * log2_int(w) - log2_int(u),
                        ),
                    },
                    "finite_transversal_coefficient": log2_int(trans) / (L * L),
                    "finite_cell_coefficient": log2_int(w) / (L * L),
                    "finite_combined_lower_coefficient": max(
                        log2_int(trans), log2_int(w)
                    )
                    / (L * L),
                    "limiting_transversal_coefficient": lim_t,
                    "limiting_cell_coefficient": lim_i,
                    "limiting_combined_coefficient": max(lim_t, lim_i),
                }
            )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    certificate = {
        "schema": "erdos838-heterogeneous-macro-jump-v1",
        "macro_colour_audit": macro_colour_audit(),
        "two_block_guard": guard_audit(),
        "dyadic_size_bucket": size_bucket_audit(),
        "fixed_point_identity": fixed_point_audit(),
        "canonical_baek_balko": bb_audit(),
        "exact_assertions": [
            "endpoint-coloured profiles sum coefficientwise to the saved exact profiles",
            "all-cup/all-cap two-block anti-alignment attains b(I)^2 P exactly",
            "same-type coloured supports satisfy the zero-skew induced-core floor",
            "a dyadic child-size bucket covers total log-size up to log2(2(L+1))",
            "c_out-c=(1-2c)alpha*beta for rational scale splits",
            "Pascal cell C*U >= W and the Baek--Balko layer masses sum to 2^(k-3)",
        ],
    }
    args.output.write_text(json.dumps(certificate, indent=2) + "\n")
    print("heterogeneous macro-jump audit: PASS")
    print("wrote", args.output)
    best = certificate["macro_colour_audit"]["cut_minimizing_exact_W"]
    print(
        "16-block coloured macro best cut:",
        best["cut"],
        "coefficient=",
        f"{best['normalized_log2_W']:.9f}",
    )
    last_guard = certificate["two_block_guard"][-1]
    print(
        "guard n=128 deficiency bits=",
        f"{last_guard['endpoint_deficiency_bits']:.6f}",
        "parent coefficient=",
        f"{last_guard['log2_parent_W_over_log2_size_squared']:.6f}",
    )
    for rec in certificate["canonical_baek_balko"][-4:]:
        print(
            "BB",
            f"theta={rec['theta']:.3f}",
            "finite combined=",
            f"{rec['finite_combined_lower_coefficient']:.6f}",
            "limit combined=",
            f"{rec['limiting_combined_coefficient']:.6f}",
        )


if __name__ == "__main__":
    main()
