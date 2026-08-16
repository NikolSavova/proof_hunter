#!/usr/bin/env python3
"""Exact checks for PARENT_UPPER_ENDPOINT_RESET_THRESHOLD.md."""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
sys.path.insert(0, str(ERDOS))

import reflection_trace as rt  # noqa: E402


Point = tuple[Fraction, Fraction]


def is_convex(points: list[Point]) -> bool:
    """Every supplied point is a vertex of the convex hull."""
    if len(points) <= 3:
        return True
    pts = sorted(points)

    def half(seq: list[Point]) -> list[Point]:
        out: list[Point] = []
        for p in seq:
            while len(out) >= 2 and rt.determinant(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    hull = half(pts)[:-1] + half(list(reversed(pts)))[:-1]
    return len(hull) == len(pts)


def is_chain(points: list[Point], sign: int) -> bool:
    pts = sorted(points)
    for i, j, k in itertools.combinations(range(len(pts)), 3):
        det = rt.determinant(pts[i], pts[j], pts[k])
        if (det > 0) != (sign > 0):
            return False
    return True


def masks_with(points: list[Point], predicate) -> list[int]:
    out = []
    for mask in range(1, 1 << len(points)):
        subset = [points[i] for i in range(len(points)) if mask >> i & 1]
        if predicate(subset):
            out.append(mask)
    return out


def endpoint_inequality_audit() -> int:
    checks = 0
    endpoint_values = range(1, 7)
    for a in range(1, 7):
        for b in range(1, 7):
            for ca in endpoint_values:
                for ua in endpoint_values:
                    for cb in endpoint_values:
                        for ub in endpoint_values:
                            wa_values = {1, max(1, ca * ua // 2), ca * ua}
                            wb_values = {1, max(1, cb * ub // 2), cb * ub}
                            for wa in wa_values:
                                for wb in wb_values:
                                    cp = cb + (b + 1) * ca
                                    up = ua + (a + 1) * ub
                                    lhs = cp * up
                                    base = (b + 1) * wa + (a + 1) * wb
                                    gap = lhs - base
                                    assert gap >= 0
                                    assert gap * gap >= 4 * (a + 1) * (b + 1) * wa * wb
                                    checks += 1
    return checks


def scalar_equality_audit() -> int:
    checks = 0
    for m in (2, 3, 7, 16, 31):
        baseline = m + math.comb(m, 2)
        for t in (baseline, baseline + 1, 3 * baseline):
            w = (m + 1) * t * t
            ca, ua = t, (m + 1) * t
            cb, ub = ua, ca
            assert ca * ua == w == cb * ub
            assert min(ca, ua, cb, ub) >= baseline
            wp = 2 * w + ca * ub
            cp = cb + (m + 1) * ca
            up = ua + (m + 1) * ub
            assert wp == (2 * m + 3) * t * t
            assert cp == up == 2 * (m + 1) * t
            assert cp * up == 4 * (m + 1) * w
            assert w - ca == w - ub
            checks += 1
    return checks


def phi(beta: float, penalty: float, length: float) -> float:
    return beta * length * length - penalty * length * math.log2(length)


def threshold_audit() -> int:
    checks = 0
    for beta in (0.25, 0.5, 0.6):
        for penalty in (0.0, 3.0, 17.0):
            for length in (8.0, 16.0, 31.0, 64.0, 127.0):
                reset = length + 1.0 + phi(beta, penalty, length - 1.0)
                delta = (
                    length * math.log2(length)
                    - (length - 1.0) * math.log2(length - 1.0)
                )
                claimed = (
                    (1.0 - 2.0 * beta) * length
                    + 1.0
                    + beta
                    + penalty * delta
                )
                assert abs((reset - phi(beta, penalty, length)) - claimed) < 1e-9
                assert delta + 1e-12 >= math.log2(length)
                if beta == 0.5:
                    assert claimed + 1e-12 >= 1.5 + penalty * math.log2(length)
                checks += 1
    return checks


def geometric_all_delete_audit() -> tuple[int, int, int, int]:
    eps = Fraction(1, 97)
    q = sorted(rt.pascal_cell(4, 2, eps))
    assert rt.evaluate(q)[:3] == (31, 31, 50)

    outer_eps = Fraction(1, 16384)
    p = sorted(rt.strong_glue(q, q, outer_eps))
    assert rt.evaluate(p)[:3] == (248, 248, 1061)

    faces = masks_with(q, is_convex)
    caps = set(masks_with(q, lambda s: is_chain(s, -1)))
    cups = set(masks_with(q, lambda s: is_chain(s, +1)))
    noncaps = [mask for mask in faces if mask not in caps]
    noncups = [mask for mask in faces if mask not in cups]
    assert (len(faces), len(caps), len(cups)) == (50, 31, 31)
    assert len(noncaps) == len(noncups) == 19

    all_delete_checks = 0
    for dmask in noncaps:
        d_indices = [i for i in range(6) if dmask >> i & 1]
        witness = None
        for triple in itertools.combinations(d_indices, 3):
            if rt.determinant(q[triple[0]], q[triple[1]], q[triple[2]]) > 0:
                witness = triple
                break
        assert witness is not None
        for z in range(6, 12):
            assert not is_convex([p[i] for i in witness] + [p[z]])

        for hmask in noncups:
            h_points = [p[6 + i] for i in range(6) if hmask >> i & 1]
            assert is_convex(h_points)
            sub = dmask
            while sub:
                union = [p[i] for i in range(6) if sub >> i & 1] + h_points
                assert not is_convex(union)
                all_delete_checks += 1
                sub = (sub - 1) & dmask

    return len(faces), len(noncaps), len(noncups), all_delete_checks


def graded_counts(points: list[Point], predicate) -> dict[int, int]:
    out: dict[int, int] = {}
    for mask in range(1, 1 << len(points)):
        subset = [points[i] for i in range(len(points)) if mask >> i & 1]
        if predicate(subset):
            out[len(subset)] = out.get(len(subset), 0) + 1
    return out


def eval_profile(profile: dict[int, int], activity: int, shift: int) -> int:
    return sum(
        count * activity ** (rank - shift)
        for rank, count in profile.items()
        if rank >= shift
    )


def planar_half_calibration() -> tuple[int, int, int, int, float]:
    q = sorted(rt.pascal_cell(4, 2, Fraction(1, 97)))
    caps_by_rank = graded_counts(q, lambda s: is_chain(s, -1))
    cups_by_rank = graded_counts(q, lambda s: is_chain(s, +1))
    faces_by_rank = graded_counts(q, is_convex)
    assert sum(caps_by_rank.values()) == sum(cups_by_rank.values()) == 31
    assert sum(faces_by_rank.values()) == 50

    n = c = u = w = 1
    for depth in range(1, 7):
        next_c = c * eval_profile(caps_by_rank, n, 1)
        next_u = u * eval_profile(cups_by_rank, n, 1)
        next_w = 6 * w + c * u * eval_profile(faces_by_rank, n, 2)
        n, c, u, w = 6 * n, next_c, next_u, next_w
        assert c == u
        if depth == 2:
            assert (n, c, u, w) == (36, 14136, 14136, 441399)

    # Independent exact rational evaluation of the 36-point iterate.
    outer_eps = Fraction(1, 16384)
    q36 = sorted(
        (
            macro_x + outer_eps * outer_eps * micro_x,
            macro_y + outer_eps * micro_y,
        )
        for macro_x, macro_y in q
        for micro_x, micro_y in q
    )
    assert rt.evaluate(q36)[:3] == (14136, 14136, 441399)

    # One more exact strong-glue wrapper; the recurrence is independently
    # checked by the reverse-product evaluator on all 72 rational points.
    wrap_eps = Fraction(1, 1 << 60)
    p72 = sorted(rt.strong_glue(q36, q36, wrap_eps))
    expected_w = 2 * 441399 + 14136 * 14136
    expected_c = 38 * 14136
    assert rt.evaluate(p72)[:3] == (expected_c, expected_c, expected_w)

    rhos = [
        (k - 2) / math.log2(math.comb(2 * k - 4, k - 2))
        for k in (4, 8, 16, 32, 64, 128, 256, 512)
    ]
    assert all(x > y > 0.5 for x, y in zip(rhos, rhos[1:]))
    return expected_w, expected_c, n, w, rhos[-1]


def main() -> None:
    endpoint_checks = endpoint_inequality_audit()
    scalar_checks = scalar_equality_audit()
    threshold_checks = threshold_audit()
    faces, noncaps, noncups, deletion_checks = geometric_all_delete_audit()
    wrapper_w, wrapper_c, last_n, last_w, rho = planar_half_calibration()
    print(
        "PASS: endpoint=%d scalar=%d threshold=%d; "
        "T(4,2) faces=%d noncap/noncup=%d/%d deletion-checks=%d; "
        "72pt=(W=%d,C=U=%d); depth6=(N=%d,W-bits=%d); rho512=%.9f"
        % (
            endpoint_checks,
            scalar_checks,
            threshold_checks,
            faces,
            noncaps,
            noncups,
            deletion_checks,
            wrapper_w,
            wrapper_c,
            last_n,
            last_w.bit_length(),
            rho,
        )
    )


if __name__ == "__main__":
    main()
