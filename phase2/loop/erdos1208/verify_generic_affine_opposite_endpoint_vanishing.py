#!/usr/bin/env python3
"""Exact Costas controls for generic affine orthogonal-tail vanishing."""

from __future__ import annotations

from analyze_affine_costas_energy import smallest_transform, welch
from search_rotated_support import is_distance_sidon
from verify_orthogonal_two_support_gate import difference_set
from verify_seven_incidence_opposite_endpoint_charge import charge_profile


EXPECTED = {
    (7, "raw"): (4_342, 2_340, 8, 11_170),
    (7, "stretched"): (24, 24, 1, 24),
    (11, "raw"): (607_206, 54_475, 105, 13_026_498),
    (11, "stretched"): (160, 160, 1, 160),
}


def main() -> None:
    for prime in (7, 11):
        raw = welch(prime)
        shear, stretch = smallest_transform(raw)
        separated = [(x + shear * y, stretch * y) for x, y in raw]
        assert not is_distance_sidon(raw)
        assert is_distance_sidon(separated)

        for label, points in (("raw", raw), ("stretched", separated)):
            profile = charge_profile(difference_set(points), adaptive=True)
            assert profile == EXPECTED[prime, label]
            pairs, _, _, second = profile
            print(
                prime,
                label,
                profile,
                "size-biased-load",
                second / pairs if pairs else 0.0,
            )

    print("generic affine opposite-endpoint controls: PASS")


if __name__ == "__main__":
    main()
