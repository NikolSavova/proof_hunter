#!/usr/bin/env python3
"""Exact tangent-reset substitution and strong-comb profile audit.

This verifier replaces every macro label of the scalable tangent reset by
an independently mirrored nonconvex four-point order type.  It checks the
physical bad-circuit matchings and, inside one class, exhaustively verifies
the heterogeneous first-cap/last-cup recurrence.  It also checks the sharp
max-plus ramp obstruction with exact Fraction arithmetic.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
RESET = runpy.run_path(str(HERE / "verify_scalable_partner_reset.py"))
orient = RESET["orient"]
hull = RESET["hull"]
is_convex = RESET["is_convex"]

MacroLabel = tuple[int, str, int]
PhysicalLabel = tuple[MacroLabel, int]
Point = tuple[Q, Q]


RAW_SEED = (
    (Q(0), Q(0)),
    (Q(1), Q(4)),
    (Q(2), Q(1)),
    (Q(4), Q(0)),
)


def seed(mirror: bool) -> tuple[Point, ...]:
    """A nonconvex order type in a chart with x and y both increasing."""
    sign = -1 if mirror else 1
    out = tuple((x, x + sign * y / 100) for x, y in RAW_SEED)
    assert all(out[i][0] < out[i + 1][0] and out[i][1] < out[i + 1][1]
               for i in range(len(out) - 1))
    assert len(hull(list(out))) == 3
    return out


def macro_order(t: int, m: int, cls: int,
                macro: dict[MacroLabel, Point]) -> list[MacroLabel]:
    labels = RESET["class_labels"](t, m, cls)
    return sorted(labels, key=lambda label: macro[label][0])


def desired_sign(labels: tuple[PhysicalLabel, PhysicalLabel, PhysicalLabel],
                 macro: dict[MacroLabel, Point],
                 seeds: dict[MacroLabel, tuple[Point, ...]]) -> int:
    ordered = sorted(labels, key=lambda label: (macro[label[0]][0],
                                                 seeds[label[0]][label[1]][0]))
    cells = [label[0] for label in ordered]
    if cells[0] == cells[2]:
        pts = [seeds[cell][label[1]] for cell, label in zip(cells, ordered)]
        return 1 if orient(*pts) > 0 else -1
    if cells[0] == cells[1]:
        return -1
    if cells[1] == cells[2]:
        return 1
    return 1 if orient(*(macro[cell] for cell in cells)) > 0 else -1


def substituted_points(t: int, m: int):
    macro, delta, _ = RESET["construct"](t, m)
    seeds: dict[MacroLabel, tuple[Point, ...]] = {}
    for cls in range(t):
        for rank, label in enumerate(macro_order(t, m, cls, macro)):
            # Alternation supplies genuinely heterogeneous C/U charts.
            seeds[label] = seed(rank % 2 == 1)

    physical_labels = [(label, k) for label in macro for k in range(4)]
    epsilon = Q(1, 2)
    for halvings in range(256):
        points = {
            (label, k): (
                macro[label][0] + epsilon * epsilon * seeds[label][k][0],
                macro[label][1] + epsilon * seeds[label][k][1],
            )
            for label in macro for k in range(4)
        }
        global_cells = sorted(macro, key=lambda label: macro[label][0])
        separated = all(
            max(points[(label, k)][0] for k in range(4))
            < min(points[(next_label, k)][0] for k in range(4))
            for label, next_label in zip(global_cells, global_cells[1:])
        )
        if separated and all(
            (lambda ordered:
                (1 if orient(*(points[label] for label in ordered)) > 0 else -1)
                == desired_sign((a, b, c), macro, seeds))(
                    sorted((a, b, c), key=lambda label: points[label][0]))
            for a, b, c in combinations(physical_labels, 3)
        ):
            return macro, points, seeds, delta, epsilon, halvings
        epsilon /= 2
    raise AssertionError("vertical substitution search did not terminate")


def interior_label(quad: tuple[PhysicalLabel, ...],
                   points: dict[PhysicalLabel, Point]) -> PhysicalLabel:
    boundary = set(hull([points[label] for label in quad]))
    inside = [label for label in quad if points[label] not in boundary]
    assert len(inside) == 1
    return inside[0]


def physical_circuit_audit(t: int, m: int,
                           points: dict[PhysicalLabel, Point]) -> dict[str, int]:
    degree: Counter[tuple[int, tuple[PhysicalLabel, PhysicalLabel]]] = Counter()
    load: Counter[PhysicalLabel] = Counter()
    edges = 0
    for i, j, a, macro_quad in RESET["selected_circuits"](t, m):
        for k in range(4):
            quad = tuple((label, k) for label in macro_quad)
            assert not is_convex([points[label] for label in quad])
            assert interior_label(quad, points) == ((j, "L", a), k)
            pi = (i, tuple(sorted(quad[:2])))
            pj = (j, tuple(sorted(quad[2:])))
            degree[pi] += 1
            degree[pj] += 1
            load.update(quad)
            edges += 1
    assert set(degree.values()) == {1}
    assert set(load.values()) == {t - 1}
    assert edges == comb(t, 2) * m * 4
    return {
        "physical_circuit_edges": edges,
        "physical_label_load": t - 1,
        "physical_pair_node_max_degree": 1,
        "physical_pair_node_triangles": 0,
    }


def is_cap(labels: tuple[PhysicalLabel, ...],
           points: dict[PhysicalLabel, Point]) -> bool:
    if len(labels) <= 2:
        return True
    ordered = sorted(labels, key=lambda label: points[label][0])
    return all(orient(points[a], points[b], points[c]) < 0
               for a, b, c in combinations(ordered, 3))


def is_cup(labels: tuple[PhysicalLabel, ...],
           points: dict[PhysicalLabel, Point]) -> bool:
    if len(labels) <= 2:
        return True
    ordered = sorted(labels, key=lambda label: points[label][0])
    return all(orient(points[a], points[b], points[c]) > 0
               for a, b, c in combinations(ordered, 3))


def subset_families(labels: list[PhysicalLabel],
                    points: dict[PhysicalLabel, Point]):
    caps: set[frozenset[PhysicalLabel]] = set()
    cups: set[frozenset[PhysicalLabel]] = set()
    faces: set[frozenset[PhysicalLabel]] = set()
    for size in range(1, len(labels) + 1):
        for subset_tuple in combinations(labels, size):
            subset = frozenset(subset_tuple)
            if is_cap(subset_tuple, points):
                caps.add(subset)
            if is_cup(subset_tuple, points):
                cups.add(subset)
            if is_convex([points[label] for label in subset_tuple]):
                faces.add(subset)
    return caps, cups, faces


def recurrence(children: list[tuple[int, int, int, int]]) -> tuple[int, int, int]:
    """Exact nonempty (C,U,W) recurrence for a convex strong comb."""
    cap = cup = face = 0
    q = len(children)
    for i, (n_i, c_i, _u_i, w_i) in enumerate(children):
        cap += c_i * (1 + sum(children[j][0] for j in range(i + 1, q)))
        face += w_i
    for j, (_n_j, _c_j, u_j, _w_j) in enumerate(children):
        prefix = 1
        for k in range(j):
            prefix *= 1 + children[k][0]
        cup += u_j * prefix
    for i in range(q):
        middle = 1
        for j in range(i + 1, q):
            if j > i + 1:
                middle *= 1 + children[j - 1][0]
            face += children[i][1] * children[j][2] * middle
    return cap, cup, face


def class_recurrence_audit(t: int, m: int,
                           points: dict[PhysicalLabel, Point]) -> dict[str, object]:
    cls = 0
    cells = RESET["class_labels"](t, m, cls)
    cells = sorted(cells, key=lambda label: points[(label, 0)][0])
    child_data = []
    child_families = {}
    for cell in cells:
        labels = [(cell, k) for k in range(4)]
        caps, cups, faces = subset_families(labels, points)
        child_data.append((4, len(caps), len(cups), len(faces)))
        child_families[cell] = (caps, cups, faces)
        assert len(faces) == 14

    labels = [(cell, k) for cell in cells for k in range(4)]
    caps, cups, faces = subset_families(labels, points)
    predicted = recurrence(child_data)
    assert predicted == (len(caps), len(cups), len(faces))

    # Fibrewise form: first trace cap, last trace cup, intermediate
    # occupied traces singleton; singleton active sets retain local faces.
    by_active: defaultdict[tuple[int, ...], set[tuple[int, ...]]] = defaultdict(set)
    cell_index = {cell: idx for idx, cell in enumerate(cells)}
    for face in faces:
        masks = [0] * len(cells)
        for cell, k in face:
            masks[cell_index[cell]] |= 1 << k
        active = tuple(i for i, mask in enumerate(masks) if mask)
        by_active[active].add(tuple(masks[i] for i in active))
    assert len(by_active) == (1 << len(cells)) - 1
    for active, family in by_active.items():
        if len(active) == 1:
            assert len(family) == child_data[active[0]][3]
        else:
            expected = (child_data[active[0]][1]
                        * child_data[active[-1]][2]
                        * 4 ** (len(active) - 2))
            assert len(family) == expected

    return {
        "cell_profiles_(n,C,U,W)": child_data,
        "class_direct_(C,U,W)": (len(caps), len(cups), len(faces)),
        "class_recurrence_(C,U,W)": predicted,
        "class_active_patterns": len(by_active),
    }


def max_plus_ramp_audit() -> dict[str, int]:
    """Check the sharp min envelope max(c,alpha) on an exact grid."""
    cases = 0
    for denominator in range(4, 21):
        for alpha_num in range(1, denominator + 1):
            for c_num in range(1, denominator + 1):
                alpha = Q(alpha_num, denominator)
                c = Q(c_num, denominator)
                target = max(alpha, c)
                # q+1 sample locations t in [0,alpha].
                xs = []
                for step in range(denominator + 1):
                    time = alpha * step / denominator
                    if c >= alpha:
                        x = time + (c - alpha) / 2
                    else:
                        x = min(time, c)
                    assert 0 <= x <= c
                    xs.append((time, x))
                envelope = max(c, alpha)
                for i in range(len(xs)):
                    ti, xi = xs[i]
                    for j in range(i + 1, len(xs)):
                        tj, xj = xs[j]
                        forward = c + (xi - ti) - (xj - tj)
                        envelope = max(envelope, forward)
                assert envelope == target
                cases += 1
    return {"exact_max_plus_ramp_cases": cases}


def finite_ramp_inequality_audit() -> dict[str, int]:
    """Verify the exact profile-gradient inequality implied by low parent W."""
    checks = 0
    # Formal positive integer profiles; recurrence is evaluated exactly.
    for d in range(3, 8):
        D = 2 ** d
        for q in range(3, min(8, d + 3)):
            height = q + 4
            children = []
            for i in range(q):
                a = 2 + min(i, height - 4)
                c_i = D ** a
                u_i = D ** (height - a)
                # Formal scalar profile saturating C_i U_i = W_i = D^h.
                # It is not asserted to be a realizable planar child.
                w_i = D ** height
                children.append((D, c_i, u_i, w_i))
            _cap, _cup, parent = recurrence(children)
            for i in range(q):
                for j in range(i + 1, q):
                    c_i, u_j = children[i][1], children[j][2]
                    assert c_i * u_j * (D + 1) ** (j - i - 1) <= parent
                    # Cleared logarithm-free form of
                    # a_j-a_i >= h+(j-i-1)r-p is exactly the same bank.
                    lhs = children[j][1] * parent
                    rhs = (children[i][1] * D ** height
                           * (D + 1) ** (j - i - 1))
                    assert lhs >= rhs
                    checks += 1
    return {"finite_profile_gradient_checks": checks}


def main() -> None:
    t, m = 3, 2
    macro, points, _seeds, delta, epsilon, halvings = substituted_points(t, m)
    assert len(points) == t * 2 * m * 4
    circuits = physical_circuit_audit(t, m, points)
    profile = class_recurrence_audit(t, m, points)

    nested, pocket_epsilon, pocket_halvings = RESET["nest_in_common_uv"](points)
    assert physical_circuit_audit(t, m, nested) == circuits

    print("PASS")
    print(f"  points/macro_delta/micro_epsilon: {len(points)}, {delta}, {epsilon}")
    print(f"  micro_halvings: {halvings}")
    print(f"  circuits: {circuits}")
    print(f"  profile: {profile}")
    print(f"  common_uv_epsilon/halvings: {pocket_epsilon}, {pocket_halvings}")
    print(f"  ramp: {max_plus_ramp_audit()}")
    print(f"  gradient: {finite_ramp_inequality_audit()}")


if __name__ == "__main__":
    main()
