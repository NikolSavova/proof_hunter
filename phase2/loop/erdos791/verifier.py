#!/usr/bin/env python3
"""Independent verifier for Kohonen's finite placement certificates.

For nonnegative placement sets I, J, K, let IJ, IK and JK denote their
pair-sum sets.  The *tile-certified* square indices are exactly

    IJ union IK union {q : q-1 in JK and q in JK}.                 (1)

The word "exactly" refers to the finite tile rule being encoded.  Formula
(1) is a sufficient condition for the corresponding interval of the full
integer sumset A_t+A_t to be covered; it is not claimed to include accidental
coverage from same-type sums or partial overlaps of several tiles.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parent
DEFAULT_CERTIFICATE = ROOT / "kohonen_42_510.json"


def pair_sum_witnesses(left: Iterable[int], right: Iterable[int]) -> dict[int, tuple[int, int]]:
    """Return one deterministic witness for every pair sum."""
    out: dict[int, tuple[int, int]] = {}
    for a in sorted(left):
        for b in sorted(right):
            out.setdefault(a + b, (a, b))
    return out


def tile_coverage(I: Iterable[int], J: Iterable[int], K: Iterable[int]) -> set[int]:
    """The exact set certified by Kohonen's three useful tile implications."""
    ij = set(pair_sum_witnesses(I, J))
    ik = set(pair_sum_witnesses(I, K))
    jk = set(pair_sum_witnesses(J, K))
    return ij | ik | {q for q in jk if q - 1 in jk}


def prefix_length(covered: set[int]) -> int:
    """Length m of the initial run [0,m-1] in a finite coverage set."""
    q = 0
    while q in covered:
        q += 1
    return q


def normalized_certificate(raw: Mapping[str, object]) -> dict[str, object]:
    """Validate syntax and return a canonical certificate dictionary."""
    cert: dict[str, object] = {}
    for key in ("I", "J", "K"):
        value = raw.get(key)
        if not isinstance(value, list) or any(type(x) is not int for x in value):
            raise ValueError(f"{key} must be a JSON list of integers")
        if any(x < 0 for x in value):
            raise ValueError(f"{key} placements must be nonnegative")
        if len(value) != len(set(value)):
            raise ValueError(f"{key} contains duplicate placements")
        cert[key] = sorted(value)

    ell = raw.get("ell")
    m = raw.get("m")
    if type(ell) is not int or ell <= 0:
        raise ValueError("ell must be a positive integer")
    if type(m) is not int or m <= 0:
        raise ValueError("m must be a positive integer")
    actual_ell = sum(len(cert[key]) for key in ("I", "J", "K"))  # type: ignore[arg-type]
    if ell != actual_ell:
        raise ValueError(f"ell={ell}, but |I|+|J|+|K|={actual_ell}")
    cert["ell"] = ell
    cert["m"] = m
    return cert


def load_certificate(path: Path) -> dict[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)
    if not isinstance(raw, dict):
        raise ValueError("certificate root must be a JSON object")
    return normalized_certificate(raw)


def coverage_witnesses(cert: Mapping[str, object], m: int) -> list[dict[str, object]]:
    """Emit one checkable tile witness for every q in [0,m-1]."""
    I = cert["I"]
    J = cert["J"]
    K = cert["K"]
    assert isinstance(I, list) and isinstance(J, list) and isinstance(K, list)
    ij = pair_sum_witnesses(I, J)
    ik = pair_sum_witnesses(I, K)
    jk = pair_sum_witnesses(J, K)
    rows: list[dict[str, object]] = []
    for q in range(m):
        if q in ij:
            rows.append({"q": q, "kind": "I+J", "pair": list(ij[q])})
        elif q in ik:
            rows.append({"q": q, "kind": "I+K", "pair": list(ik[q])})
        elif q - 1 in jk and q in jk:
            rows.append(
                {
                    "q": q,
                    "kind": "consecutive-J+K",
                    "pair_q_minus_1": list(jk[q - 1]),
                    "pair_q": list(jk[q]),
                }
            )
        else:
            raise ValueError(f"square q={q} has no tile witness")
    return rows


def elementary_basis(cert: Mapping[str, object], t: int) -> set[int]:
    """Expand the generalized Mrose basis A_t literally."""
    if t < 2:
        raise ValueError("Kohonen's elementary segments require t >= 2")
    V = set(range(t + 1))
    H = set(range(0, t * t, t))
    S = set(range(0, t * t, t + 1))
    I = cert["I"]
    J = cert["J"]
    K = cert["K"]
    assert isinstance(I, list) and isinstance(J, list) and isinstance(K, list)
    scale = t * t
    return (
        {v + scale * i for v in V for i in I}
        | {h + scale * j for h in H for j in J}
        | {s + scale * k for s in S for k in K}
    )


def direct_sumset_check(cert: Mapping[str, object], t: int, m: int) -> tuple[int, int]:
    """Check [0,m*t^2-1] directly in A_t+A_t; return (|A_t|, range)."""
    A = elementary_basis(cert, t)
    sums = {a + b for a in A for b in A if a <= b}
    target_end = m * t * t - 1
    missing = next((x for x in range(target_end + 1) if x not in sums), None)
    if missing is not None:
        raise ValueError(f"direct expansion failed for t={t} at integer {missing}")
    actual_range = 0
    while actual_range + 1 in sums:
        actual_range += 1
    return len(A), actual_range


def canonical_digest(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def verify(path: Path, direct_t: Sequence[int]) -> dict[str, object]:
    cert = load_certificate(path)
    I = cert["I"]
    J = cert["J"]
    K = cert["K"]
    assert isinstance(I, list) and isinstance(J, list) and isinstance(K, list)
    covered = tile_coverage(I, J, K)
    actual_prefix = prefix_length(covered)
    claimed_m = cert["m"]
    assert isinstance(claimed_m, int)
    if actual_prefix < claimed_m:
        raise ValueError(f"claimed m={claimed_m}, but certified prefix is only {actual_prefix}")

    witnesses = coverage_witnesses(cert, claimed_m)
    result: dict[str, object] = {
        "status": "PASS",
        "certificate": str(path.resolve()),
        "ell": cert["ell"],
        "claimed_m": claimed_m,
        "exact_tile_prefix": actual_prefix,
        "ratio_m_over_ell_squared": str(Fraction(claimed_m, int(cert["ell"]) ** 2)),
        "certificate_sha256": canonical_digest(cert),
        "witnesses_sha256": canonical_digest(witnesses),
        "first_uncovered_square": actual_prefix,
    }
    direct_rows = []
    for t in direct_t:
        size, actual_range = direct_sumset_check(cert, t, claimed_m)
        direct_rows.append(
            {
                "t": t,
                "basis_size": size,
                "required_through": claimed_m * t * t - 1,
                "actual_sumset_prefix_through": actual_range,
            }
        )
    result["direct_expansion_checks"] = direct_rows
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument(
        "--direct-t",
        type=int,
        nargs="*",
        default=[2, 3, 5, 10],
        help="literal A_t+A_t cross-checks (default: 2 3 5 10; pass no values to skip)",
    )
    parser.add_argument("--emit-witnesses", type=Path)
    args = parser.parse_args()
    result = verify(args.certificate, args.direct_t)
    if args.emit_witnesses is not None:
        cert = load_certificate(args.certificate)
        rows = coverage_witnesses(cert, int(cert["m"]))
        args.emit_witnesses.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
        result["witness_file"] = str(args.emit_witnesses.resolve())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
