#!/usr/bin/env python3
"""Exact audit of OUTER_INTERNAL_MIXED_BANK.md."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt
from pathlib import Path


HERE = Path(__file__).resolve().parent
ERDOS = HERE.parent
CHAIN = ERDOS / "agent_cyclic_stem_hw"
MIXED = ERDOS / "agent_recursive_pocket_induction"
APA = ERDOS / "agent_apa_rank"
for directory in (CHAIN, MIXED, APA):
    sys.path.insert(0, str(directory))

from verify_apa_counterexample import matrix_profile, orient  # noqa: E402
from verify_insertion_chain_universality import transform  # noqa: E402
from verify_long_chain_mixed_barrier import hard_points, hull  # noqa: E402


Point = tuple[Fraction, Fraction]


def parabola_point(t: Fraction) -> Point:
    return (t, t * t - 1)


def choose_lower_parameters(chain: list[Point], count: int) -> list[Fraction]:
    """Choose rational lower-parabola labels avoiding every existing line."""
    u = (Fraction(-1), Fraction(0))
    v = (Fraction(1), Fraction(0))
    fixed = [u, v] + list(chain)
    chosen: list[Fraction] = []
    for denominator in (101, 103, 107, 109, 113, 127, 131, 137):
        for numerator in range(-denominator + 1, denominator):
            if numerator == 0:
                continue
            t = Fraction(numerator, denominator)
            if t in chosen:
                continue
            candidate = parabola_point(t)
            if all(
                orient(candidate, first, second) != 0
                for first, second in combinations(fixed, 2)
            ):
                chosen.append(t)
                fixed.append(candidate)
                if len(chosen) == count:
                    return chosen
    raise AssertionError("failed to find generic lower-parabola labels")


def theorem_one_integer_stress() -> dict[str, int]:
    """Audit the exact floor inequalities behind Theorem 1."""
    cases = 0
    for degree in range(2, 65):
        for contexts in (1, 2, 3, 7, 19):
            a_sum = 0
            q_sum = 0
            mixed = 0
            remainder = 0
            b_numerator = degree**3
            # q/b = 2q/D^3.  Use a deterministic mix of poor and rich cells.
            q_values = [
                (index * index * degree + 3 * index + 1) % (degree**3 + 7)
                for index in range(contexts)
            ]
            for q in q_values:
                a = 2 * degree
                paid = min(degree**2, isqrt(a * q))
                a_sum += a
                q_sum += q
                mixed += paid
                remainder += degree**2 - paid

                # Check D^2-floor(sqrt(2Dq)) <= D^2 delta+1 without floats.
                # If q>=D^3/2, delta=0 and the cell is paid completely.
                if 2 * q >= b_numerator:
                    assert paid == degree**2
                else:
                    # The report's inequality is equivalent to
                    # paid+1 >= D^2 sqrt(2q/D^3).  Square exact integers.
                    assert (paid + 1) ** 2 * degree**3 >= degree**4 * 2 * q

            overlap = 3
            source_multiplicity = 5
            volume = max(
                (contexts * degree + source_multiplicity - 1)
                // source_multiplicity,
                q_sum,
                (a_sum + overlap - 1) // overlap,
            )
            assert a_sum <= overlap * volume
            assert q_sum <= volume
            # Exact Cauchy, without evaluating sqrt(Lambda).
            assert mixed * mixed <= a_sum * q_sum
            assert mixed * mixed <= overlap * volume * volume
            assert remainder == contexts * degree**2 - mixed
            assert contexts <= Fraction(source_multiplicity * volume, degree)
            cases += 1
    return {"integer_parameter_cases": cases}


def dense_cross_union_audit() -> dict[str, int]:
    """All points on one parabola: every outer--internal union is convex."""
    parameters = [Fraction(index) for index in range(13)]
    points = [parabola_point(value) for value in parameters]
    assert all(orient(a, b, c) != 0 for a, b, c in combinations(points, 3))
    assert set(hull(points)) == set(points)

    outer_count = 7
    internal_count = 6
    carriers = list(combinations(range(outer_count), 3))
    internal_faces = [
        tuple(face)
        for rank in range(internal_count + 1)
        for face in combinations(range(outer_count, 13), rank)
    ]
    mixed = set()
    for carrier in carriers:
        for internal in internal_faces:
            union = tuple(carrier) + tuple(internal)
            union_points = [points[index] for index in union]
            assert set(hull(union_points)) == set(union_points)
            codeword = (frozenset(carrier), frozenset(internal))
            assert codeword not in mixed
            mixed.add(codeword)

    degree = 4
    threshold = degree**3 // 2
    q = len(internal_faces)
    assert q == 64 and q >= threshold
    assert len(mixed) == len(carriers) * q
    assert 2 * degree * q >= degree**4
    return {
        "dense_outer_labels": outer_count,
        "dense_internal_labels": internal_count,
        "dense_contexts": len(carriers),
        "dense_internal_reservoir": q,
        "dense_mixed_faces": len(mixed),
        "dense_D": degree,
        "dense_D_cubed_over_two": threshold,
    }


def sparse_chain_audit() -> dict[str, int | str]:
    """Exact finite audit of the scalable sparse cross-union construction."""
    original = hard_points()
    _, _, chain, tangent_coordinates = transform(original)
    assert len(chain) == 20
    u: Point = (Fraction(-1), Fraction(0))
    v: Point = (Fraction(1), Fraction(0))

    lower_parameters = choose_lower_parameters(chain, 9)
    lower = [parabola_point(t) for t in lower_parameters]
    w = lower[0]
    cloud = lower[1:]
    lower_hull = [u, v] + lower
    ambient = lower_hull + chain

    assert all(orient(a, b, c) != 0 for a, b, c in combinations(ambient, 3))
    assert set(hull(lower_hull)) == set(lower_hull)

    context_extra = 3
    carriers = [
        [u, v, w] + [cloud[index] for index in labels]
        for labels in combinations(range(len(cloud)), context_extra)
    ]
    assert len(carriers) == comb(8, 3) == 56
    for carrier in carriers:
        assert len(carrier) == 6
        assert set(hull(carrier)) == set(carrier)
        for tip in chain:
            candidate = carrier + [tip]
            assert set(hull(candidate)) == set(candidate)

    strict_pairs = 0
    bad_circuits = 0
    for i, earlier in enumerate(chain):
        left_i, right_i = tangent_coordinates[i]
        for j in range(i + 1, len(chain)):
            later = chain[j]
            left_j, right_j = tangent_coordinates[j]
            height_i = earlier[1]
            barycentric = (
                height_i * (right_i - right_j) / 2,
                height_i * (left_i - left_j) / 2,
                height_i * (left_j + right_j) / 2,
            )
            assert all(value > 0 for value in barycentric)
            assert sum(barycentric) == 1
            quadruple = [u, v, earlier, later]
            assert len(hull(quadruple)) == 3
            assert earlier not in set(hull(quadruple))
            strict_pairs += 1
            bad_circuits += 1

    profile = matrix_profile(tuple(chain))
    internal_faces = sum(profile)
    compatible_faces = 1 + len(chain)
    incompatible_faces = internal_faces - compatible_faces
    weighted_two_two_shadow = sum(
        count * comb(rank, 2) for rank, count in enumerate(profile)
    )
    assert internal_faces == 4775
    assert compatible_faces == 21
    assert incompatible_faces == 4754
    assert weighted_two_two_shadow >= incompatible_faces
    assert strict_pairs == comb(len(chain), 2)

    # Every carrier has exactly the same compatible internal faces.  Testing
    # all internal faces is unnecessary: every face of rank >=2 contains one
    # of the bad pairs just audited, while empty/singletons were checked.
    for carrier in carriers:
        for first, second in combinations(chain, 2):
            assert len(hull(carrier + [first, second])) == len(carrier) + 1

    finite_degree = 10
    threshold = finite_degree**3 // 2
    assert internal_faces >= threshold
    assert compatible_faces < threshold

    # Symbolic rank/cap/context/shield scaling from Section 3.
    symbolic_rows = []
    for rank in (8, 16, 32, 64):
        degree = 1 << rank
        contexts = comb(degree, rank - 4)
        ambient_n = 1 << (2 * rank)
        assert ambient_n // (1 << rank) == degree
        records = contexts * degree**2
        # Compare with 2^(D+3) by bit length; never materialize that
        # double-exponential integer.
        assert records.bit_length() <= degree + 3
        symbolic_rows.append(
            {
                "rank": rank,
                "D": degree,
                "ambient_n": ambient_n,
                "outer_context_log2_floor": contexts.bit_length() - 1,
                "selected_record_bit_length": records.bit_length(),
                "outer_shield_log2": degree + 3,
            }
        )

    return {
        "finite_chain_labels": len(chain),
        "finite_lower_cloud_labels": len(cloud),
        "finite_outer_contexts": len(carriers),
        "finite_bad_2_plus_2_circuits": bad_circuits,
        "finite_internal_reservoir_H": internal_faces,
        "finite_compatible_q": compatible_faces,
        "finite_incompatible_faces": incompatible_faces,
        "finite_weighted_circuit_shadow_Xi": weighted_two_two_shadow,
        "finite_D": finite_degree,
        "finite_D_cubed_over_two": threshold,
        "symbolic_rows": symbolic_rows,
        "is_counterexample_to_unconditional_cross_union_density": "yes",
        "is_counterexample_to_fixed_power_EIC_prime": "no; outer shield bank pays",
    }


def main() -> None:
    result = {
        "theorem_one": theorem_one_integer_stress(),
        "dense_cross_union": dense_cross_union_audit(),
        "sparse_four_circuit": sparse_chain_audit(),
        "status": "PASS",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    print("PASS: global outer--internal mixed bank and four-circuit defect")


if __name__ == "__main__":
    main()
