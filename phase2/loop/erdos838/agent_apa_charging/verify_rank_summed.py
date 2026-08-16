#!/usr/bin/env python3
"""Exact audit of the KL and rank-summed first-switch consequences."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SWITCH = ROOT / "agent_tilted_switch"
sys.path.insert(0, str(SWITCH))

import tilted_switch_audit as switch  # noqa: E402

from verify_local_compensation import PROFILES  # noqa: E402


def rank_data(profile: tuple[int, ...], t: Fraction):
    z = sum((Fraction(v) * t**r for r, v in enumerate(profile)), Fraction())
    mu = sum((Fraction(r * v) * t**r for r, v in enumerate(profile)), Fraction()) / z
    return z, mu


def audit_kl(profile: tuple[int, ...]) -> dict[str, str]:
    n = profile[1]
    v, mu1 = rank_data(profile, Fraction(1))
    w, muh = rank_data(profile, Fraction(1, 2))
    delta = mu1 - muh
    h = Fraction(n) * w / v

    # Avoid transcendental arithmetic: the identities imply
    # 2^(mu1-m) = 2^mu1 * w/v.  The final scalar inequality is analytic,
    # while all signs and the compensation itself remain exact here.
    compensation = h * max(Fraction(), 1 - delta)
    assert delta >= 0
    return {
        "n": str(n),
        "H": str(h),
        "mu_1": str(mu1),
        "mu_half": str(muh),
        "delta": str(delta),
        "local_compensation": str(compensation),
    }


def face_statistics(points: list[tuple[int, int]], lam: int = 4):
    faces = switch.face_table(points)
    n = len(points)
    full = (1 << n) - 1
    moment_rows = {}
    raw = []
    for t in (Fraction(1), Fraction(1, 2)):
        z = Fraction()
        er = er2 = eu = eu2 = eb = ebu = ebr = Fraction()
        boundary = Fraction()
        boundary_low = Fraction()
        for mask, good in enumerate(faces):
            if not good:
                continue
            r = mask.bit_count()
            remaining = full ^ mask
            u = 0
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                u += faces[mask | bit]
            b = n - r - u
            weight = t**r
            z += weight
            er += weight * r
            er2 += weight * r * r
            eu += weight * u
            eu2 += weight * u * u
            eb += weight * b
            ebu += weight * b * u
            ebr += weight * b * r
            boundary += weight * b
            if u <= lam * (r + 1):
                boundary_low += weight * b
        assert t * eu == er
        beta3 = Fraction()
        for mask, good in enumerate(faces):
            if not good or mask.bit_count() != 3:
                continue
            remaining = full ^ mask
            u = 0
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                u += faces[mask | bit]
            beta3 += t**3 * (n - 3 - u)
        assert (ebr - 2 * eb - beta3) / t <= ebu <= (ebr - 3 * beta3) / t
        mu = er / z
        beta3 /= z
        lhs = er2 / z - (1 - t) * mu + 3 * t * beta3
        middle = t * t * eu2 / z
        rhs = er2 / z - (1 - t) * mu + 2 * t * eb / z + t * beta3
        assert lhs <= middle <= rhs
        factor = lam * t / (lam * t - 1)
        assert boundary <= factor * boundary_low
        moment_rows[str(t)] = {
            "Z": str(z),
            "boundary": str(boundary),
            "low_extension_boundary": str(boundary_low),
            "localization_factor": str(factor),
            "rank_second_moment": str(er2 / z),
            "rank_three_boundary_expectation": str(beta3),
            "scaled_up_second_moment": str(middle),
            "moment_upper_bound": str(rhs),
        }
        raw.append((t, boundary, boundary_low))
    ell = (n - 1).bit_length()
    near_maximal_deficit = 0
    value = 0
    total_rank = 0
    for mask, good in enumerate(faces):
        if not good:
            continue
        value += 1
        r = mask.bit_count()
        total_rank += r
        remaining = full ^ mask
        u = 0
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            u += faces[mask | bit]
        if r < ell and u <= lam * (r + 1):
            near_maximal_deficit += ell - r
    npm_constant = Fraction(near_maximal_deficit, value)
    assert Fraction(total_rank, value) >= ell - 2 * npm_constant - Fraction(1, 2)

    # Exact alpha=1/2 check of the maximal-face restriction identity.
    maximal_sum = 0
    for restriction in range(1 << n):
        sub = restriction
        while True:
            if faces[sub]:
                outside = restriction ^ sub
                maximal = True
                remaining = outside
                while remaining:
                    bit = remaining & -remaining
                    remaining ^= bit
                    if faces[sub | bit]:
                        maximal = False
                        break
                maximal_sum += maximal
            if sub == 0:
                break
            sub = (sub - 1) & restriction
    maximal_expectation_direct = Fraction(maximal_sum, 2**n)
    maximal_expectation_formula = Fraction()
    for mask, good in enumerate(faces):
        if not good:
            continue
        r = mask.bit_count()
        remaining = full ^ mask
        u = 0
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            u += faces[mask | bit]
        maximal_expectation_formula += Fraction(1, 2 ** (r + u))
    assert maximal_expectation_direct == maximal_expectation_formula
    return {
        "activities": moment_rows,
        "ell": ell,
        "near_maximal_deficit": near_maximal_deficit,
        "number_of_faces": value,
        "NPM_constant_exact": str(npm_constant),
        "expected_maximal_faces_in_half_restriction": str(maximal_expectation_direct),
    }


def main() -> None:
    records = json.loads(
        (ROOT / "agent_lex_minimizer_search" / "direct_hull_certificates.json").read_text()
    )
    small = {}
    for n in (8, 9):
        points = [tuple(point) for point in records[str(n)]["coordinates"]]
        small[str(n)] = face_statistics(points)

    output = {
        "kl_profiles": {str(n): audit_kl(profile) for n, profile in PROFILES.items()},
        "exact_planar_face_tables": small,
        "claims": {
            "kl": "D2(q1||qh)=mu1-m; D2(qh||q1)=m-muh; sum=delta",
            "localization": (
                "sum t^r B_r <= Lambda*t/(Lambda*t-1) "
                "sum_{u<=Lambda(r+1)} t^r b(A)"
            ),
            "moment": (
                "E R^2-(1-t)mu+3t beta3 <= E(tu)^2 <= "
                "E R^2-(1-t)mu+2t E b+t beta3"
            ),
            "near_maximal_mean": (
                "sum_{r<ell}(ell-r) #{A:u(A)<=4(r+1)} <= C V "
                "implies mu1>=log2(n)-2C-1/2"
            ),
        },
    }
    (HERE / "rank_summed_certificate.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n"
    )
    print("rank-summed first-switch and KL audit: PASS")


if __name__ == "__main__":
    main()
