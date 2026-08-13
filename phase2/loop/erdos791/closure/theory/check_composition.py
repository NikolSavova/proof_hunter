#!/usr/bin/env python3
"""Finite checks for the elementary composition statements in STATUS_AND_THEORY.md.

This is not evidence for the open asymptotic claim.  It exhaustively checks the
product lemma for every small interval basis and checks the inverse block
identity for the resulting exact small range table.
"""

from itertools import combinations
import json
from pathlib import Path


def covers(a: tuple[int, ...], r: int) -> bool:
    sums = {x + y for x in a for y in a}
    return all(x in sums for x in range(r + 1))


def bases_through(r: int) -> list[tuple[int, ...]]:
    ans = []
    universe = range(r + 1)
    for k in range(1, r + 2):
        for a in combinations(universe, k):
            if covers(a, r):
                ans.append(a)
    return ans


def exact_small_R(kmax: int, rmax: int) -> list[int]:
    out = [-1] * (kmax + 1)
    for r in range(rmax + 1):
        for a in bases_through(r):
            for k in range(len(a), kmax + 1):
                out[k] = max(out[k], r)
    return out


def main() -> None:
    checked = 0
    for r in range(5):
        left = bases_through(r)
        for s in range(5):
            right = bases_through(s)
            for a in left:
                for c in right:
                    m = r + 1
                    d = tuple(sorted({x + m * y for x in a for y in c}))
                    target = (r + 1) * (s + 1) - 1
                    assert len(d) == len(a) * len(c)
                    assert covers(d, target)
                    assert (target + 1) * len(a) ** 2 * len(c) ** 2 == (
                        (r + 1) * (s + 1) * len(d) ** 2
                    )
                    checked += 1

    elementary_family_checks = 0
    for t in range(1, 21):
        a = tuple(range(t)) + tuple(j * t for j in range(1, t + 1))
        assert len(set(a)) == 2 * t
        assert covers(a, t * t + t - 1)
        elementary_family_checks += 1

    # The finite cutoff can truncate R(k), so only test the exact g/R inverse
    # statement for n up to the cutoff, where R is computed directly.
    rmax = 12
    kmax = 8
    rr = exact_small_R(kmax, rmax)
    inverse_checks = 0
    for n in range(rmax + 1):
        feasible = [k for k in range(1, kmax + 1) if rr[k] >= n]
        if not feasible:
            continue
        g = min(feasible)
        assert rr[g] >= n
        assert g == 1 or rr[g - 1] < n
        inverse_checks += 1

    output = {
        "status": "PASS",
        "product_basis_pairs_checked": checked,
        "elementary_scaled_family_checked_t_through": elementary_family_checks,
        "inverse_n_checked": inverse_checks,
        "small_R_truncated_at_12": rr,
        "scope": "finite sanity checks only; no asymptotic claim",
    }
    path = Path(__file__).with_name("CHECKS.json")
    path.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
