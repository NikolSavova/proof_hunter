#!/usr/bin/env python3
"""Generate, solve, and DRAT-check every capacity-tight split in a range."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import time
from math import floor
from pathlib import Path


HERE = Path(__file__).resolve().parent


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def target(ell: int) -> int:
    return floor(85 * ell * ell / 294) + 1


def canonical_splits(ell: int) -> list[tuple[int, int, int]]:
    return [
        (i, j, ell - i - j)
        for i in range(1, ell - 1)
        for j in range(1, ell - i)
        if j >= ell - i - j
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", type=Path, required=True)
    parser.add_argument("--checker", type=Path, required=True)
    parser.add_argument("--work", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--ell-min", type=int, default=18)
    parser.add_argument("--ell-max", type=int, default=24)
    parser.add_argument("--seconds", type=int, default=60)
    args = parser.parse_args()
    args.work.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, object]] = []
    census: list[dict[str, object]] = []
    for ell in range(args.ell_min, args.ell_max + 1):
        m = target(ell)
        splits = canonical_splits(ell)
        infeasible = [s for s in splits if s[0] * (s[1] + s[2]) + s[1] * s[2] - 1 < m]
        feasible = [s for s in splits if s not in infeasible]
        tight = [s for s in feasible if s[0] * (s[1] + s[2]) + s[1] * s[2] - 1 == m]
        census.append(
            {
                "ell": ell,
                "target_m": m,
                "canonical_positive_splits": len(splits),
                "capacity_infeasible": len(infeasible),
                "capacity_feasible": len(feasible),
                "capacity_tight_splits": [list(s) for s in tight],
            }
        )
        for counts in tight:
            stem = f"ell{ell}_m{m}_{counts[0]}{counts[1]}{counts[2]}"
            cnf = args.work / f"{stem}.cnf"
            metadata = args.work / f"{stem}.json"
            proof = args.work / f"{stem}.drat"
            model = args.work / f"{stem}.sol"
            generate = subprocess.run(
                [
                    sys.executable,
                    str(HERE / "exact_cnf.py"),
                    "--ell",
                    str(ell),
                    "--m",
                    str(m),
                    "--counts",
                    *map(str, counts),
                    "--output",
                    str(cnf),
                    "--metadata",
                    str(metadata),
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            del generate
            started = time.monotonic()
            solved = subprocess.run(
                [
                    str(args.solver),
                    "-q",
                    "--unsat",
                    "--no-binary",
                    "-t",
                    str(args.seconds),
                    str(cnf),
                    str(proof),
                ],
                capture_output=True,
                text=True,
            )
            solve_seconds = time.monotonic() - started
            model.write_text(solved.stdout)
            status = "UNSAT" if solved.returncode == 20 else "SAT" if solved.returncode == 10 else "UNKNOWN"
            row: dict[str, object] = {
                "ell": ell,
                "m": m,
                "counts": list(counts),
                "status": status,
                "solver_exit": solved.returncode,
                "solve_seconds": round(solve_seconds, 6),
                "cnf_sha256": sha256(cnf),
                "cnf_bytes": cnf.stat().st_size,
                "proof_checked": False,
            }
            if status == "UNSAT":
                checked = subprocess.run(
                    [str(args.checker), str(cnf), str(proof)],
                    capture_output=True,
                    text=True,
                )
                verified = checked.returncode == 0 and "s VERIFIED" in checked.stdout
                row.update(
                    {
                        "proof_checked": verified,
                        "checker_exit": checked.returncode,
                        "proof_sha256": sha256(proof),
                        "proof_bytes": proof.stat().st_size,
                        "checker_summary": [
                            line.strip()
                            for line in checked.stdout.splitlines()
                            if "lemmas in core" in line or line.startswith("s ")
                        ],
                    }
                )
            rows.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)

    result = {
        "scope": "all canonical positive J/K-unordered type splits",
        "target_formula": "floor(85*ell^2/294)+1",
        "census": census,
        "capacity_bound": "m <= i*(j+k)+j*k-1",
        "capacity_tight_exact_runs": rows,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")


if __name__ == "__main__":
    main()
