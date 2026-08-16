#!/usr/bin/env python3
"""Exact audit of minimal rooted defects and their rank expansion."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
LATTICE = ROOT / "agent_planar_lattice_mean"
LEX = ROOT / "agent_lex_minimizer_search"
sys.path.insert(0, str(LATTICE))

from planar_lattice_mean import (  # noqa: E402
    closure_mask,
    convex_hull,
    is_convex,
    orient,
)


def points_4() -> tuple[tuple[int, int], ...]:
    return ((0, 0), (12, 0), (0, 12), (2, 3))


def points_9() -> tuple[tuple[int, int], ...]:
    record = json.loads((LEX / "exact_realizable_n9.json").read_text())
    return tuple(sorted(tuple(point) for point in record["coordinates_as_stored"]))


def nested_fan(q: int) -> tuple[tuple[int, int], ...]:
    width = 4 * q
    return ((-width, 0), (width, 0)) + tuple((i, 1 << i) for i in range(1, q + 1))


def labels(mask: int, n: int) -> list[int]:
    return [i for i in range(n) if (mask >> i) & 1]


def jointly_good(points, closed: int, exterior_subset: int) -> bool:
    chosen = labels(closed | exterior_subset, len(points))
    hull = set(convex_hull(points, chosen))
    return all(
        i in hull
        for i in range(len(points))
        if (exterior_subset >> i) & 1
    )


def local_bad_table(points, face: int):
    n = len(points)
    full = (1 << n) - 1
    closed = closure_mask(points, labels(face, n))
    exterior_global = full ^ closed
    exterior_labels = labels(exterior_global, n)
    q = len(exterior_labels)

    bad = [0] * (1 << q)
    for local in range(1 << q):
        global_mask = sum(
            1 << exterior_labels[j]
            for j in range(q)
            if (local >> j) & 1
        )
        bad[local] = int(not jointly_good(points, closed, global_mask))

    minimal = []
    for mask in range(1 << q):
        if not bad[mask]:
            continue
        if all(not bad[mask ^ (1 << j)] for j in range(q) if (mask >> j) & 1):
            minimal.append(mask)

    # Boolean Möbius transform of the bad indicator.
    beta = bad[:]
    for j in range(q):
        for mask in range(1 << q):
            if (mask >> j) & 1:
                beta[mask] -= beta[mask ^ (1 << j)]

    # Inversion and support-on-unions checks.
    for mask in range(1 << q):
        recovered = 0
        sub = mask
        while True:
            recovered += beta[sub]
            if sub == 0:
                break
            sub = (sub - 1) & mask
        if recovered != bad[mask]:
            raise AssertionError(("Mobius inversion", face, mask))
        if beta[mask]:
            union = 0
            for root in minimal:
                if root & ~mask == 0:
                    union |= root
            if union != mask:
                raise AssertionError(("Mobius support", face, mask, beta[mask]))

    bad_probability = Fraction(sum(bad), 1 << q)
    mobius_probability = sum(
        (Fraction(beta[mask], 1 << mask.bit_count()) for mask in range(1 << q)),
        Fraction(),
    )
    if bad_probability != mobius_probability:
        raise AssertionError(("local rank identity", face))

    cover_probability = sum(
        (Fraction(1, 1 << root.bit_count()) for root in minimal),
        Fraction(),
    )
    if bad_probability > cover_probability:
        raise AssertionError(("minimal-root cover", face))

    return {
        "closed": closed,
        "q": q,
        "bad": bad,
        "minimal": minimal,
        "beta": beta,
        "bad_probability": bad_probability,
        "cover_probability": cover_probability,
    }


def verify_general_position(points) -> None:
    for i, j, k in combinations(range(len(points)), 3):
        if orient(points[i], points[j], points[k]) == 0:
            raise AssertionError(("collinear", i, j, k, points[i], points[j], points[k]))


def exhaustive_configuration(points, name: str):
    verify_general_position(points)
    n = len(points)
    faces = [
        mask
        for mask in range(1 << n)
        if is_convex(points, labels(mask, n))
    ]
    z_half = sum((Fraction(1, 1 << mask.bit_count()) for mask in faces), Fraction())
    hull_term = Fraction()
    defect_direct = Fraction()
    defect_mobius = Fraction()
    positive_cover = Fraction()
    four_roots = 0

    for face in faces:
        table = local_bad_table(points, face)
        closed = table["closed"]
        q = table["q"]
        hull_term += Fraction(1, 1 << q)
        defect_direct += Fraction(1, 1 << face.bit_count()) * table["bad_probability"]
        defect_mobius += sum(
            (
                Fraction(coefficient, 1 << (face.bit_count() + mask.bit_count()))
                for mask, coefficient in enumerate(table["beta"])
            ),
            Fraction(),
        )
        positive_cover += sum(
            (
                Fraction(1, 1 << (face.bit_count() + root.bit_count()))
                for root in table["minimal"]
            ),
            Fraction(),
        )

        for root in table["minimal"]:
            size = root.bit_count()
            if closed:
                if not (2 <= size <= 3):
                    raise AssertionError(("nonempty minimal root", name, face, root, size))
            else:
                if size != 4:
                    raise AssertionError(("empty-state minimal root", name, root, size))
                four_roots += 1

    if z_half - hull_term != defect_direct:
        raise AssertionError(("factorial defect grouping", name, z_half, hull_term, defect_direct))
    if defect_direct != defect_mobius:
        raise AssertionError(("global Mobius rank identity", name))
    if defect_direct > positive_cover:
        raise AssertionError(("global positive cover", name))

    # At the empty state, the good exterior sets are exactly all convex faces.
    empty = local_bad_table(points, 0)
    if Fraction(sum(empty["bad"]), 1 << n) != 1 - Fraction(len(faces), 1 << n):
        raise AssertionError(("empty state is original face problem", name))

    return {
        "name": name,
        "n": n,
        "V": len(faces),
        "Z_half": str(z_half),
        "hull_term": str(hull_term),
        "defect": str(defect_direct),
        "positive_minimal_root_cover": str(positive_cover),
        "empty_state_four_roots": four_roots,
    }


def verify_nested_fans():
    rows = []
    for q in range(2, 13):
        points = nested_fan(q)
        verify_general_position(points)
        base = 0b11
        table = local_bad_table(points, base)
        if table["closed"] != base or table["q"] != q:
            raise AssertionError(("fan base closure", q, table["closed"]))

        expected_roots = {(1 << i) | (1 << j) for i, j in combinations(range(q), 2)}
        if set(table["minimal"]) != expected_roots:
            raise AssertionError(("fan minimal roots", q))

        for mask, value in enumerate(table["bad"]):
            if value != int(mask.bit_count() >= 2):
                raise AssertionError(("fan bad ideal", q, mask, value))
        for mask, coefficient in enumerate(table["beta"]):
            size = mask.bit_count()
            expected = 0 if size < 2 else (-1) ** size * (size - 1)
            if coefficient != expected:
                raise AssertionError(("fan Mobius", q, mask, coefficient, expected))

        local_defect = Fraction(1, 4) * table["bad_probability"]
        expected_defect = Fraction(1, 4) * (1 - Fraction(q + 1, 1 << q))
        if local_defect != expected_defect:
            raise AssertionError(("fan defect formula", q))
        local_cover = Fraction(1, 4) * table["cover_probability"]
        if local_cover != Fraction(q * (q - 1), 32):
            raise AssertionError(("fan cover formula", q))

        absolute_mass = Fraction(1, 4) * sum(
            (
                Fraction(abs(coefficient), 1 << mask.bit_count())
                for mask, coefficient in enumerate(table["beta"])
            ),
            Fraction(),
        )
        formula = Fraction(1, 4) * (
            1 + Fraction(q - 3, 3) * Fraction(3**q, 2**q)
        )
        if absolute_mass != formula:
            raise AssertionError(("fan absolute mass", q, absolute_mass, formula))

        rows.append(
            {
                "q": q,
                "local_defect": str(local_defect),
                "local_positive_cover": str(local_cover),
                "Mobius_absolute_mass": str(absolute_mass),
            }
        )
    return rows


def main() -> None:
    result = {
        "configurations": [
            exhaustive_configuration(points_4(), "four_point_circuit"),
            exhaustive_configuration(points_9(), "exact_nine_point_minimizer"),
        ],
        "nested_fans": verify_nested_fans(),
        "status": "PASS",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
