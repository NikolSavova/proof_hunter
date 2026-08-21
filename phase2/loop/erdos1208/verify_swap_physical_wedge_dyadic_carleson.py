#!/usr/bin/env python3
"""Verify the physical-wedge dyadic decomposition."""

from __future__ import annotations

from collections import defaultdict
from contextlib import redirect_stdout
from io import StringIO
from math import comb
from random import Random

Wedge = tuple[int, int, int, int, int]


def wedges(k: int) -> list[Wedge]:
    return [
        (endpoint, first_other, second_other, first_role, second_role)
        for endpoint in range(k)
        for first_other in range(k)
        if first_other != endpoint
        for second_other in range(k)
        if second_other != endpoint
        for first_role in (0, 1)
        for second_role in (2, 3)
    ]


def mass(load: int) -> int:
    return 3 * comb(load, 3)


def audit_counts() -> None:
    for k in range(2, 12):
        all_wedges = wedges(k)
        assert len(all_wedges) == 4 * k * (k - 1) ** 2
        same_edge = [row for row in all_wedges if row[1] == row[2]]
        one_endpoint = [row for row in all_wedges if row[1] != row[2]]
        assert len(same_edge) == 4 * k * (k - 1)
        assert len(one_endpoint) == 4 * k * (k - 1) * (k - 2)


def audit_decomposition() -> None:
    rng = Random(1208)
    for k in range(3, 11):
        universe = wedges(k)
        for _ in range(100):
            cells: dict[Wedge, list[int]] = defaultdict(list)
            for wedge in rng.sample(universe, rng.randrange(len(universe) + 1)):
                cells[wedge] = [rng.randrange(1, 13) for _ in range(rng.randrange(7))]

            wedge_mass = {
                wedge: sum(mass(load) for load in loads)
                for wedge, loads in cells.items()
            }
            centre_mass = sum(wedge_mass.values())
            physical_second = sum(
                comb(load, 2) for loads in cells.values() for load in loads
            )
            assert centre_mass == sum(
                (load - 2) * comb(load, 2)
                for loads in cells.values()
                for load in loads
            )

            for threshold in (0, 1, 5, 20, 100):
                for rich_load in (3, 4, 7, 13):
                    heavy = sum(
                        mass(load)
                        for wedge, loads in cells.items()
                        if wedge_mass[wedge] > threshold
                        for load in loads
                        if load >= rich_load
                    )
                    upper = (
                        4 * threshold * k * (k - 1) ** 2
                        + (rich_load - 3) * physical_second
                        + heavy
                    )
                    assert centre_mass <= upper

                    same_low = sum(
                        wedge_mass[wedge]
                        for wedge in cells
                        if wedge[1] == wedge[2]
                        and wedge_mass[wedge] <= threshold
                    )
                    one_low = sum(
                        wedge_mass[wedge]
                        for wedge in cells
                        if wedge[1] != wedge[2]
                        and wedge_mass[wedge] <= threshold
                    )
                    assert same_low <= 4 * threshold * k * (k - 1)
                    assert one_low <= 4 * threshold * k * (k - 1) * (k - 2)


def audit_stored_stress() -> None:
    rows = {
        23: (204, 68, 3, 24, 180),
        29: (4857, 945, 48, 774, 4083),
        31: (5058, 418, 123, 1992, 3066),
    }
    for prime, (total, support, maximum, same_edge, one_endpoint) in rows.items():
        k = prime - 1
        assert total == same_edge + one_endpoint
        assert support <= 4 * k * (k - 1) ** 2
        assert maximum <= total
    assert (93 + 30, 87 + 21) == (123, 108)
    assert mass(6) == 60


def audit_genuine_zero_controls() -> None:
    from analyze_swap_optimal_nested_cores import difference_set, profile
    from search_rotated_support import mian_chowla
    from verify_closed_fibre_q_height_layered_barrier import (
        lifted_residue_parabola,
    )

    families = (
        ([(mark, 0) for mark in mian_chowla(14)], "Golomb-14"),
        (lifted_residue_parabola(17), "lifted-parabola-17"),
    )
    for points, name in families:
        _, summary, _ = profile(difference_set(points), points)
        repeated = dict(
            summary["matching_projected_mixed_repeated_pair_cells"]
        )["same_centre_cross_difference_energy"]
        assert repeated[1] == 0, name
        assert repeated[6][0] == 0, name

    # Importing the certificate performs its own full exact audit and prints
    # a profile.  Silence that independent output here, then test the new
    # same-centre statistic on the certified point set.
    with redirect_stdout(StringIO()):
        from verify_high_codegree_transverse_equal_area_rank_flat_barrier import (
            POINTS as rank_flat_points,
        )

    _, summary, _ = profile(
        difference_set(rank_flat_points), rank_flat_points
    )
    repeated = dict(
        summary["matching_projected_mixed_repeated_pair_cells"]
    )["same_centre_cross_difference_energy"]
    assert repeated[1] == 0
    assert repeated[6][0] == 0


def main() -> None:
    audit_counts()
    audit_decomposition()
    audit_stored_stress()
    audit_genuine_zero_controls()
    print("SWAP PHYSICAL-WEDGE DYADIC CARLESON GATE: PASS")


if __name__ == "__main__":
    main()
