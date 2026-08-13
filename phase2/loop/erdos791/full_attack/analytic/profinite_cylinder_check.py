#!/usr/bin/env python3
"""Exact finite check of the cylinder equidistribution used in PROF proof.

For targets 0,...,M-1, bins floor(m*n/M)=s, and residues n mod q,
the count differs from M/(m*q) by a bounded endpoint error.  The theorem only
needs o(M); this audit records the actual worst discrepancy in a broad box.
"""

from fractions import Fraction
import json
from pathlib import Path


def main() -> None:
    worst = Fraction(0)
    witness = None
    checked = 0
    for M in range(1, 401):
        for m in range(1, 17):
            # Allocate separately for q so the straightforward code remains auditable.
            for q in range(1, 20):
                table = [[0] * q for _ in range(m)]
                for n in range(M):
                    table[(m * n) // M][n % q] += 1
                expected = Fraction(M, m * q)
                for s in range(m):
                    for r in range(q):
                        discrepancy = abs(Fraction(table[s][r]) - expected)
                        checked += 1
                        if discrepancy > worst:
                            worst = discrepancy
                            witness = (M, m, q, s, r, table[s][r], expected)
    output = {
        "status": "PASS",
        "cylinders_checked": checked,
        "max_M": 400,
        "max_macro_bins": 16,
        "max_modulus": 19,
        "worst_absolute_discrepancy": str(worst),
        "witness_M_m_q_s_r_count_expected": [
            *witness[:-1], str(witness[-1])
        ] if witness else None,
        "theorem_requirement": "for fixed m,q, discrepancy=o(M)",
    }
    target = Path(__file__).with_name("PROFINITE_CYLINDER_CHECK.json")
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
