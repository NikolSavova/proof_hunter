#!/usr/bin/env python3
"""Checks for ADAPTIVE_AREA_CELL_CARTESIAN_REUSE_GATE.md."""

from itertools import permutations


def abstract_profile(n):
    k = 10 * n
    q_count = n
    fibre_size = 2 * n
    fibre_mass = 4 * k * k
    selected_per_q = n
    quota = (k * k * fibre_size + fibre_mass - 1) // fibre_mass
    tail_per_q = max(0, selected_per_q - quota)
    target_area_cells = k
    tail_occurrences = q_count * tail_per_q
    adaptive_lift = tail_occurrences * target_area_cells
    return {
        "k": k,
        "q_count": q_count,
        "fibre_size": fibre_size,
        "fibre_mass": fibre_mass,
        "source_codegree": q_count,
        "selected_per_q": selected_per_q,
        "quota": quota,
        "tail_per_q": tail_per_q,
        "target_area_cells": target_area_cells,
        "max_area_cell": 1,
        "tail_occurrences": tail_occurrences,
        "adaptive_lift": adaptive_lift,
    }


def check_abstract_model():
    for n in range(4, 101):
        p = abstract_profile(n)
        assert p["source_codegree"] < p["k"]
        assert p["quota"] == (n + 1) // 2
        assert p["tail_per_q"] == n // 2
        assert p["max_area_cell"] == 1
        assert p["adaptive_lift"] == p["k"] * n * (n // 2)
        pair_minimum = n * (n - 1) // 2 * p["target_area_cells"]
        assert p["tail_per_q"] * p["target_area_cells"] <= pair_minimum // p["quota"]
        paired_functional_num = p["q_count"] * pair_minimum
        paired_functional_den = p["fibre_size"]
        assert paired_functional_num * p["fibre_mass"] >= (
            p["adaptive_lift"] * p["k"] * p["k"] * paired_functional_den
        )
        # The excess is linear in k along either parity subsequence.
        assert p["adaptive_lift"] * 1_000 >= p["fibre_mass"] * p["k"]
    print("factor-k abstract adaptive profiles: PASS")


def symbolic_point(name):
    return {name: 1}


def add(*forms):
    out = {}
    for form in forms:
        for variable, coefficient in form.items():
            out[variable] = out.get(variable, 0) + coefficient
    return {variable: coefficient for variable, coefficient in out.items()
            if coefficient}


def subtract(first, second):
    return add(first, {variable: -coefficient
                       for variable, coefficient in second.items()})


def check_symbolic_cartesian_collision():
    for q_count in range(4, 9):
        C = symbolic_point("C")
        Cp = symbolic_point("Cp")
        q = [symbolic_point(f"q{j}") for j in range(q_count)]
        Y = [subtract(qj, C) for qj in q]
        Yp = [subtract(qj, Cp) for qj in q]
        for j, ell in permutations(range(q_count), 2):
            assert add(Y[j], Yp[ell]) == add(Yp[j], Y[ell])
    print("symbolic two-role pair-sum collisions: PASS")


def has_good_index_pair(q_count, cross_equalities):
    """Cross equalities are pairs (j,l) asserting Y_j=Y'_l."""
    equal = set(cross_equalities)
    for j, ell in permutations(range(q_count), 2):
        if (j, ell) not in equal and (ell, j) not in equal:
            return True
    return False


def check_cross_coincidence_patterns():
    # Cross equality is a partial matching, hence represented by a partial
    # permutation between the two indexed families.
    for q_count in range(4, 9):
        indices = range(q_count)
        # Full permutations are the worst case; deleting equalities can only
        # make it easier to find a good pair.
        checked = 0
        for image in permutations(indices):
            equalities = {(j, image[j]) for j in indices}
            # Same-index equality is excluded by target-role disjointness.
            if any(image[j] == j for j in indices):
                continue
            assert has_good_index_pair(q_count, equalities)
            checked += 1
        assert checked
    print("cross-family coincidence exhaustion Q=4..8: PASS")


def main():
    check_abstract_model()
    check_symbolic_cartesian_collision()
    check_cross_coincidence_patterns()
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
