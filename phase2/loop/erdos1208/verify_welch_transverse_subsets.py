#!/usr/bin/env python3
"""Exact certificates for WELCH_TRANSVERSE_SUBSET_AUDIT.md."""

from __future__ import annotations

from analyze_affine_costas_energy import is_distance_sidon, welch
from verify_transverse_local_gate import differences, local_overlap
from search_welch_transverse_subsets import local_solutions


CASES = {
    127: {
        "d": (-4, 9),
        "full": 6887,
        "indices": [
            10, 13, 19, 22, 23, 29, 46, 47, 48, 53, 55, 57, 60,
            62, 67, 68, 71, 72, 78, 80, 81, 86, 97, 100, 114,
        ],
        "maximum": 43,
    },
    251: {
        "d": (-3, -5),
        "full": 27474,
        "indices": [
            3, 4, 6, 9, 12, 23, 33, 38, 41, 46, 57, 59, 67, 73,
            77, 99, 100, 118, 123, 145, 151, 155, 159, 160, 161,
            165, 169, 173, 181, 185, 193, 196, 208, 213, 214, 216,
            224, 228, 232, 249,
        ],
        "maximum": 68,
    },
    509: {
        "d": (-1, 2),
        "full": 114191,
        "indices": [
            68, 87, 117, 129, 135, 151, 166, 174, 195, 200, 209,
            242, 247, 248, 249, 255, 256, 269, 280, 286, 298, 299,
            303, 305, 328, 336, 369, 379, 395, 398, 401, 402, 404,
            413, 416, 419, 432, 438, 439, 442, 448, 451, 452, 453,
            455, 461, 468, 473, 478, 482, 497, 499, 500, 502, 506,
        ],
        "maximum": 94,
    },
}


def main() -> None:
    for prime, data in CASES.items():
        full = welch(prime)
        assert len(differences(full)) == len(full) * (len(full) - 1) + 1
        _, full_solutions = local_solutions(full, data["d"])
        assert len(full_solutions) == data["full"]

        subset = [full[index] for index in data["indices"]]
        assert is_distance_sidon(subset)
        difference_set = differences(subset)
        maximum, maximizing_d = max(
            (local_overlap(d, difference_set), d) for d in difference_set
        )
        assert maximum == data["maximum"]
        assert local_overlap(data["d"], difference_set) == maximum
        print(
            prime,
            len(full),
            data["full"],
            len(subset),
            maximum,
            maximizing_d,
        )
    print("PASS")


if __name__ == "__main__":
    main()
