#!/usr/bin/env python3
"""Exact counterexamples to naive lattice expansion after ACP Theorem 23.

All geometry uses integer determinants.  The script audits three different
statements which must not be conflated:

* fixed directed chord, opposite half-planes: rectangle completion works;
* closure comparability alone: the lattice product inequality can fail;
* a full Theorem-23 support rectangle in one nested tangent cell: product
  entropy need not give product-many core-preserving hulls or faces.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
from typing import Iterable

Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def in_triangle_strict(p: Point, a: Point, b: Point, c: Point) -> bool:
    signs = (orient(a, b, p), orient(b, c, p), orient(c, a, p))
    return all(value > 0 for value in signs) or all(value < 0 for value in signs)


class PlanarClosure:
    """Convex-hull closure on a general-position integer point set."""

    def __init__(self, points: Iterable[Point]):
        self.points = tuple(points)
        self.n = len(self.points)
        assert len(set(self.points)) == self.n
        assert len({p[0] for p in self.points}) == self.n, "x coordinates not fixed-distinct"
        for i, j, k in combinations(range(self.n), 3):
            assert orient(self.points[i], self.points[j], self.points[k]) != 0
        self.containers: list[tuple[int, ...]] = []
        for p in range(self.n):
            masks = []
            for i, j, k in combinations((q for q in range(self.n) if q != p), 3):
                if in_triangle_strict(
                    self.points[p], self.points[i], self.points[j], self.points[k]
                ):
                    masks.append((1 << i) | (1 << j) | (1 << k))
            self.containers.append(tuple(masks))

    def closure(self, mask: int) -> int:
        result = mask
        for p, triangles in enumerate(self.containers):
            if mask >> p & 1:
                continue
            if any(triangle & mask == triangle for triangle in triangles):
                result |= 1 << p
        return result

    def is_closed(self, mask: int) -> bool:
        return self.closure(mask) == mask

    def is_face(self, mask: int) -> bool:
        """Every selected point is a vertex of the selected convex hull."""
        return all(
            not any(triangle & mask == triangle for triangle in self.containers[p])
            for p in range(self.n)
            if mask >> p & 1
        )

    def closed_flags(self) -> list[int]:
        return [int(self.is_closed(mask)) for mask in range(1 << self.n)]


def subset_superset_counts(flags: list[int], n: int) -> tuple[list[int], list[int]]:
    down = flags.copy()
    up = flags.copy()
    for bit_index in range(n):
        bit = 1 << bit_index
        for mask in range(1 << n):
            if mask & bit:
                down[mask] += down[mask ^ bit]
            else:
                up[mask] += up[mask | bit]
    return down, up


def lattice_audit(points: tuple[Point, ...], chosen_mask: int | None = None) -> dict:
    geometry = PlanarClosure(points)
    flags = geometry.closed_flags()
    closed_count = sum(flags)
    face_count = sum(geometry.is_face(mask) for mask in range(1 << geometry.n))
    down, up = subset_superset_counts(flags, geometry.n)
    candidates = [mask for mask, flag in enumerate(flags) if flag]
    if chosen_mask is None:
        chosen_mask = min(candidates, key=lambda mask: Fraction(closed_count, down[mask] * up[mask]))
    assert flags[chosen_mask]
    product_count = down[chosen_mask] * up[chosen_mask]
    return {
        "points": [list(point) for point in points],
        "K_mask": chosen_mask,
        "closed_hulls": closed_count,
        "ordinary_convex_faces": face_count,
        "down_K": down[chosen_mask],
        "up_K": up[chosen_mask],
        "rectangle_pairs": product_count,
        "hulls_per_pair": str(Fraction(closed_count, product_count)),
        "violates_constant_one": product_count > closed_count,
    }


def minimal_planar_counterexample() -> dict:
    # Point 2 is strictly inside the triangle on 0,1,3.  The closure lattice
    # is the Boolean 4-cube with exactly that one nonclosed subset removed.
    points = ((0, 0), (1, 4), (2, 1), (4, 0))
    audit = lattice_audit(points, 1 << 2)
    assert audit["closed_hulls"] == 15
    assert audit["ordinary_convex_faces"] == 15
    assert audit["down_K"] == 2 and audit["up_K"] == 8
    assert audit["rectangle_pairs"] == 16
    return audit


def chirotope(points: tuple[Point, ...]) -> tuple[int, ...]:
    return tuple(
        1 if orient(points[i], points[j], points[k]) > 0 else -1
        for i, j, k in combinations(range(len(points)), 3)
    )


def fixed_x_permutation_census(max_n: int = 7) -> list[dict]:
    """Enumerate realized chirotopes among points (i, permutation[i])."""
    rows = []
    for n in range(3, max_n + 1):
        representatives: dict[tuple[int, ...], tuple[Point, ...]] = {}
        gp_permutations = 0
        for y_order in permutations(range(n)):
            points = tuple((i, y_order[i]) for i in range(n))
            if any(orient(points[i], points[j], points[k]) == 0 for i, j, k in combinations(range(n), 3)):
                continue
            gp_permutations += 1
            representatives.setdefault(chirotope(points), points)

        violations = 0
        worst: dict | None = None
        worst_ratio = Fraction(1)
        for points in representatives.values():
            audit = lattice_audit(points)
            ratio = Fraction(audit["closed_hulls"], audit["rectangle_pairs"])
            if audit["violates_constant_one"]:
                violations += 1
            if worst is None or ratio < worst_ratio:
                worst_ratio = ratio
                worst = audit
        assert worst is not None
        rows.append(
            {
                "n": n,
                "general_position_permutations": gp_permutations,
                "distinct_labeled_chirotopes": len(representatives),
                "violating_chirotopes": violations,
                "worst_hulls_per_pair": str(worst_ratio),
                "worst_points": worst["points"],
                "worst_K_mask": worst["K_mask"],
                "worst_counts_C_down_up": [
                    worst["closed_hulls"],
                    worst["down_K"],
                    worst["up_K"],
                ],
            }
        )
    return rows


# Raw integer rings.  The exact affine shear (x,y)->(100000*x+y,y)
# makes every x-coordinate distinct without changing any orientation sign.
RAW_RINGS: dict[int, tuple[Point, ...]] = {
    3: (
        (10004, 6), (4982, 8656), (-4988, 8671), (-9995, -1), (-4990, -8658),
        (5017, -8667), (101, 16), (-64, 76), (-37, -92),
    ),
    4: (
        (10004, 6), (7053, 7067), (12, 10011), (-7066, 7070), (-9990, 2),
        (-7054, -7078), (12, -10012), (7069, -7083), (97, 19), (-17, 101),
        (-97, -18), (17, -101),
    ),
    5: (
        (10004, 6), (8072, 5874), (3102, 9522), (-3085, 9510), (-8079, 5880),
        (-9983, -7), (-8078, -5890), (-3092, -9523), (3076, -9492),
        (8086, -5864), (101, 16), (14, 97), (-92, 44), (-69, -70), (45, -89),
    ),
    6: (
        (10004, 6), (8642, 4996), (5012, 8671), (5, 9999), (-4990, 8662),
        (-8643, 4993), (-9988, -12), (-8662, -5012), (-5014, -8641),
        (-4, -9986), (5018, -8671), (8659, -5014), (97, 17), (36, 96),
        (-66, 77), (-98, -17), (-33, -95), (66, -76),
    ),
}

EXPECTED_RING_CLOSED = {3: 230, 4: 871, 5: 2990, 6: 9841}


def nested_ring_audits() -> list[dict]:
    rows = []
    for inner_count, raw_points in RAW_RINGS.items():
        outer_count = 2 * inner_count
        points = tuple((100000 * x + y, y) for x, y in raw_points)
        inner_mask = ((1 << inner_count) - 1) << outer_count
        outer_mask = (1 << outer_count) - 1
        geometry = PlanarClosure(points)
        assert geometry.is_face(inner_mask) and geometry.is_closed(inner_mask)
        assert geometry.is_face(outer_mask)
        assert geometry.closure(outer_mask) == (1 << len(points)) - 1
        audit = lattice_audit(points, inner_mask)
        assert audit["closed_hulls"] == EXPECTED_RING_CLOSED[inner_count]
        assert audit["down_K"] == 1 << inner_count
        assert audit["up_K"] == 1 << outer_count
        assert audit["rectangle_pairs"] == 1 << (3 * inner_count)
        audit.update({"inner_points": inner_count, "outer_points": outer_count})
        rows.append(audit)
    return rows


def nested_chain_points(q: int) -> tuple[Point, ...]:
    scale = 100 * q * q
    return ((0, 0), (scale, 0)) + tuple(
        (scale // 2 + j * j, -scale * (1 << (j + 1))) for j in range(q)
    )


def near_product_nested_chain(a: int) -> dict:
    """Theorem-23 equality with no localized product of hulls/faces.

    There are a shallow hidden singletons and a^3 deep repaired triangles.
    Hence |I|=a, |T|=a^3, |G|=a^4.  With kappa=1 and tau=3, both
    marginal entropy densities equal rho=log_2(a) exactly.
    """
    hidden_count = a
    target_count = a**3
    q = hidden_count + target_count
    points = nested_chain_points(q)
    geometry = PlanarClosure(points)
    root_mask = 0b11

    # The exact nested-ear relation: for i<j, z_i is strictly inside
    # triangle u,v,z_j, while z_j is exterior to u,v,z_i.
    for i in range(q):
        source = root_mask | (1 << (i + 2))
        assert geometry.is_face(source)
        expected_closure = root_mask | (((1 << (i + 1)) - 1) << 2)
        assert geometry.closure(source) == expected_closure
    for i in range(hidden_count):
        for j in range(hidden_count, q):
            union = root_mask | (1 << (i + 2)) | (1 << (j + 2))
            repaired = root_mask | (1 << (j + 2))
            assert not geometry.is_face(union)
            assert geometry.is_face(repaired)
            assert geometry.closure(repaired) >> (i + 2) & 1

    edges = hidden_count * target_count
    assert edges == a**4
    assert hidden_count**4 == edges
    assert target_count**4 == edges**3
    localized_count = q + 1
    assert edges > localized_count
    return {
        "a": a,
        "point_count": len(points),
        "points": [list(point) for point in points],
        "fixed_core_indices": [0, 1],
        "hidden_z_indices": list(range(2, 2 + hidden_count)),
        "target_z_indices": list(range(2 + hidden_count, 2 + q)),
        "hidden_support": hidden_count,
        "target_support": target_count,
        "record_edges": edges,
        "tau": 3,
        "kappa": 1,
        "entropy_density_equality_integer_checks": {
            "hidden_support^4_equals_edges": hidden_count**4,
            "target_support^4_equals_edges^3": target_count**4,
        },
        "mutual_information_bits": 0,
        "independent_support_probability": "1",
        "weighted_C4_probability": "1",
        "core_preserving_closed_hulls": localized_count,
        "core_preserving_convex_faces": localized_count,
        "records_per_localized_object": str(Fraction(edges, localized_count)),
    }


def fixed_chord_positive_control() -> dict:
    # All lower choices and all upper rooted triangles lie in opposite open
    # half-planes of the directed chord uv.  Every cross-union is a distinct
    # convex quadrilateral, exactly as fixed-frame completion predicts.
    points = (
        (0, 0), (100, 0),
        (17, -31), (39, -47), (61, -43), (83, -29),
        (13, 23), (32, 41), (57, 37), (78, 31), (91, 19),
    )
    geometry = PlanarClosure(points)
    lower = range(2, 6)
    upper = range(6, 11)
    faces = set()
    for i in lower:
        for j in upper:
            mask = 0b11 | (1 << i) | (1 << j)
            assert geometry.is_face(mask)
            faces.add(mask)
    assert len(faces) == len(lower) * len(upper) == 20
    return {
        "points": [list(point) for point in points],
        "lower_choices": len(lower),
        "upper_choices": len(upper),
        "distinct_cross_union_faces": len(faces),
    }


def abstract_meet_distributive_countermodels(max_power: int = 12) -> list[dict]:
    # One rooted 4-element circuit has 15 closed sets: every subset is closed
    # except {a,b,c}, whose closure also contains p.  K={p} has down=2,
    # up=8.  Direct products remain convex geometries / meet-distributive
    # lattices, and tensor all four counts.
    rows = []
    for power in range(1, max_power + 1):
        closed = 15**power
        down = 2**power
        up = 8**power
        pairs = down * up
        assert pairs == 16**power > closed
        rows.append(
            {
                "power": power,
                "closed_hulls": closed,
                "down_K": down,
                "up_K": up,
                "rectangle_pairs": pairs,
                "hulls_per_pair": str(Fraction(closed, pairs)),
            }
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quick", action="store_true", help="skip fixed-x permutation census")
    args = parser.parse_args()

    result = {
        "conjectures_tested": {
            "LR_constant_one": "For every planar closure lattice C(P) and K in C(P), |down K||up K| <= |C(P)|.",
            "localized_Theorem23_product": "A full support rectangle satisfying Theorem 23 with epsilon=0 forces at least |G| distinct core-preserving intermediate hulls or convex faces.",
            "fixed_chord_control": "Opposite-side families sharing one directed chord have all distinct convex cross-unions.",
        },
        "minimal_planar_counterexample": minimal_planar_counterexample(),
        "nested_ring_planar_counterexamples": nested_ring_audits(),
        "near_product_nested_chain": [near_product_nested_chain(a) for a in (2, 3)],
        "fixed_chord_positive_control": fixed_chord_positive_control(),
        "abstract_meet_distributive_products": abstract_meet_distributive_countermodels(),
    }
    if not args.quick:
        result["fixed_x_permutation_census"] = fixed_x_permutation_census()

    output = Path(__file__).with_name("certificate.json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print("lattice rectangle counter-audit: PASS")
    print(f"minimal planar lattice count: {result['minimal_planar_counterexample']['closed_hulls']} < 16")
    for row in result["nested_ring_planar_counterexamples"]:
        print(
            "nested ring k={inner_points}: C={closed_hulls}, rectangle={rectangle_pairs}, ratio={hulls_per_pair}".format(
                **row
            )
        )
    for row in result["near_product_nested_chain"]:
        print(
            f"near-product a={row['a']}: edges={row['record_edges']}, localized={row['core_preserving_closed_hulls']}"
        )
    if not args.quick:
        for row in result["fixed_x_permutation_census"]:
            print(
                f"fixed-x n={row['n']}: order types={row['distinct_labeled_chirotopes']}, "
                f"violations={row['violating_chirotopes']}, worst={row['worst_hulls_per_pair']}"
            )


if __name__ == "__main__":
    main()
