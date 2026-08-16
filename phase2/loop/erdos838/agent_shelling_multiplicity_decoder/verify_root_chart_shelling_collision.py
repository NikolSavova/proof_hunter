#!/usr/bin/env python3
"""Exact checks for ROOT_CHART_KRAFT_AND_SHELLING_COLLISION.md."""

from __future__ import annotations

from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


hull = load_module(
    "shelling_collision_hull",
    ROOT / "agent_hull_root_envelope_dynamic" / "verify_hull_root_envelope.py",
)
reflection = load_module(
    "shelling_collision_reflection",
    ROOT / "reflection_trace.py",
)


def fast_chart_profile(points, order):
    """Exact O(n^3) cap/cup totals and hinged ranks in one chart."""
    size = len(order)
    if size == 1:
        return {
            "C": 1, "U": 1, "alpha": (0,), "beta": (0,),
            "kraft": Q(1), "minimum": 0, "maximum": 0,
        }

    caps = [[0] * size for _ in range(size)]
    cups = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            caps[i][j] = cups[i][j] = 1
            for before in range(i):
                sign = hull.orient(
                    points[order[before]], points[order[i]], points[order[j]]
                )
                if sign < 0:
                    caps[i][j] += caps[before][i]
                else:
                    cups[i][j] += cups[before][i]

    alpha = [0] * size
    start = {}
    for i in range(size - 2, -1, -1):
        for j in range(size - 1, i, -1):
            best = 2
            for after in range(j + 1, size):
                if hull.orient(
                    points[order[i]], points[order[j]], points[order[after]]
                ) < 0:
                    best = max(best, 1 + start[j, after])
            start[i, j] = best
            alpha[i] = max(alpha[i], best - 1)

    beta = [0] * size
    end = {}
    for j in range(size):
        for i in range(j):
            best = 2
            for before in range(i):
                if hull.orient(
                    points[order[before]], points[order[i]], points[order[j]]
                ) > 0:
                    best = max(best, 1 + end[before, i])
            end[i, j] = best
            beta[j] = max(beta[j], best - 1)

    lengths = [a + b for a, b in zip(alpha, beta)]
    return {
        "C": size + sum(map(sum, caps)),
        "U": size + sum(map(sum, cups)),
        "alpha": tuple(alpha),
        "beta": tuple(beta),
        "kraft": sum(Q(1, 2 ** value) for value in lengths),
        "minimum": min(lengths),
        "maximum": max(lengths),
    }


def ordinary_face_masks(points):
    answer = []
    for mask in range(1, 1 << len(points)):
        ids = [i for i in range(len(points)) if mask >> i & 1]
        selected = [points[i] for i in ids]
        if len(ids) <= 2 or len(hull.hull_ids(selected)) == len(ids):
            answer.append(mask)
    return answer


def fraction_text(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


def audit_shelling_decoder(points, expected):
    """Audit every reachable state and the uniform shelling flow."""
    size = len(points)
    full = (1 << size) - 1
    totals = hull.all_mask_face_totals(points)
    reachable = set()
    transitions = []
    charts = {}

    def visit(mask):
        if mask in reachable:
            return
        reachable.add(mask)
        if mask & (mask - 1) == 0:
            return
        for root in hull.hull_ids(points, mask):
            child = mask ^ (1 << root)
            order = hull.radial_order(points, mask, root)
            profile = fast_chart_profile(points, order)
            direct = hull.chart_profile(points, order)
            assert (profile["C"], profile["U"], profile["kraft"]) == (
                direct["C"], direct["U"], direct["kraft"]
            )
            assert profile["alpha"] == tuple(direct["alpha"][i] for i in order)
            assert profile["beta"] == tuple(direct["beta"][i] for i in order)
            assert profile["C"] == totals[mask] - totals[child] - 1
            correction = int(mask.bit_count() <= 3)
            charts[mask, root] = (order, profile, profile["maximum"] + correction)
            transitions.append((mask, root, child))
            visit(child)

    visit(full)

    @lru_cache(None)
    def suffix_paths(mask):
        if mask & (mask - 1) == 0:
            return 1
        return sum(
            suffix_paths(mask ^ (1 << root))
            for root in hull.hull_ids(points, mask)
        )

    prefix_paths = {full: 1}
    for rank in range(size, 1, -1):
        for mask in (row for row in reachable if row.bit_count() == rank):
            for root in hull.hull_ids(points, mask):
                child = mask ^ (1 << root)
                prefix_paths[child] = prefix_paths.get(child, 0) + prefix_paths[mask]

    shellings = suffix_paths(full)
    assert sum(prefix_paths[mask] for mask in reachable if mask.bit_count() == 1) == shellings

    faces = ordinary_face_masks(points)
    loads = {face: 0 for face in faces if face.bit_count() >= 2}
    weighted_caps = weighted_hinged = weighted_code = 0
    raw_rows = []
    minimum_rows = []
    maximum_rows = []

    for mask in reachable:
        if mask & (mask - 1) == 0:
            continue
        roots = hull.hull_ids(points, mask)
        profiles = [charts[mask, root][1] for root in roots]
        raw_rows.append(sum(profile["kraft"] for profile in profiles))
        minimum_rows.append(sum(Q(1, 2 ** profile["minimum"])
                                for profile in profiles))
        maximum_rows.append(sum(Q(1, 2 ** charts[mask, root][2])
                                for root in roots))
        assert maximum_rows[-1] <= 1

    for mask, root, child in transitions:
        order, profile, code_length = charts[mask, root]
        flow = prefix_paths[mask] * suffix_paths(child)
        weighted_caps += flow * profile["C"]
        weighted_hinged += flow * profile["maximum"]
        weighted_code += flow * code_length
        position = {label: index for index, label in enumerate(order)}
        for face in loads:
            if face & ~mask or not (face >> root & 1):
                continue
            support = [i for i in range(size)
                       if i != root and face >> i & 1]
            support.sort(key=position.get)
            assert all(
                hull.orient(points[i], points[j], points[k]) < 0
                for i, j, k in combinations(support, 3)
            )
            loads[face] += flow

    assert set(loads.values()) == {shellings}
    assert weighted_caps == shellings * (totals[full] - size)

    @lru_cache(None)
    def path_kraft(mask):
        if mask & (mask - 1) == 0:
            return Q(1)
        return sum(
            Q(1, 2 ** charts[mask, root][2])
            * path_kraft(mask ^ (1 << root))
            for root in hull.hull_ids(points, mask)
        )

    result = {
        "n": size,
        "V": totals[full],
        "reachable": len(reachable),
        "transitions": len(transitions),
        "shellings": shellings,
        "tagged_nontrivial_faces": weighted_caps,
        "nontrivial_faces": totals[full] - size,
        "face_fibre": next(iter(set(loads.values()))),
        "nontrivial_states": len(raw_rows),
        "raw_violations": sum(value > 1 for value in raw_rows),
        "minimum_violations": sum(value > 1 for value in minimum_rows),
        "maximum_violations": sum(value > 1 for value in maximum_rows),
        "maximum_raw_mass": fraction_text(max(raw_rows)),
        "top_raw_mass": fraction_text(sum(
            charts[full, root][1]["kraft"]
            for root in hull.hull_ids(points, full)
        )),
        "top_maximum_mass": fraction_text(sum(
            Q(1, 2 ** charts[full, root][2])
            for root in hull.hull_ids(points, full)
        )),
        "path_kraft": fraction_text(path_kraft(full)),
        "weighted_hinged_length": weighted_hinged,
        "weighted_corrected_length": weighted_code,
    }
    assert result == expected
    return result


def audit_convex_polygons():
    rows = []
    for size in range(4, 13):
        points = [(i, i * i) for i in range(size)]
        full = (1 << size) - 1
        roots = hull.hull_ids(points, full)
        assert len(roots) == size
        profiles = [
            fast_chart_profile(points, hull.radial_order(points, full, root))
            for root in roots
        ]
        assert all(profile["kraft"] == 1 for profile in profiles)
        assert all(profile["maximum"] == size - 2 for profile in profiles)
        assert all(
            sorted(a + b for a, b in zip(profile["alpha"], profile["beta"]))
            == list(range(1, size - 2)) + [size - 2, size - 2]
            for profile in profiles
        )
        raw = sum(profile["kraft"] for profile in profiles)
        maximum = sum(Q(1, 2 ** profile["maximum"])
                      for profile in profiles)
        assert raw == size
        assert maximum == Q(size, 2 ** (size - 2)) <= 1
        rows.append([size, fraction_text(raw), fraction_text(maximum)])
    return rows


def audit_vertical_pascal_36(expected):
    base = sorted(reflection.pascal_cell(4, 2, Q(1, 97)))
    epsilon = Q(1, 16384)
    points = sorted(
        (x + epsilon * epsilon * u, y + epsilon * v)
        for x, y in base for u, v in base
    )
    assert reflection.evaluate(points)[:3] == (14136, 14136, 441399)
    full = (1 << len(points)) - 1
    rows = []
    for root in hull.hull_ids(points, full):
        profile = fast_chart_profile(
            points, hull.radial_order(points, full, root)
        )
        rows.append([
            root, profile["C"], profile["U"],
            fraction_text(profile["kraft"]),
            profile["minimum"], profile["maximum"],
        ])
    result = {
        "n": 36,
        "hull": [row[0] for row in rows],
        "root_rows": rows,
        "raw_mass": fraction_text(sum(Q(row[3]) for row in rows)),
        "minimum_mass": fraction_text(sum(Q(1, 2 ** row[4]) for row in rows)),
        "maximum_mass": fraction_text(sum(Q(1, 2 ** row[5]) for row in rows)),
    }
    assert result == expected
    return result


def main():
    certificate = json.loads((HERE / "root_chart_shelling_collision_certificate.json").read_text())
    n9_points = [tuple(row) for row in certificate["n9_points"]]

    pascal6 = sorted(reflection.pascal_cell(4, 2, Q(1, 97)))
    pascal3 = sorted(reflection.pascal_cell(3, 1, Q(1, 97)))
    epsilon = Q(1, 16384)
    vertical9 = sorted(
        (x + epsilon * epsilon * u, y + epsilon * v)
        for x, y in pascal3 for u, v in pascal3
    )

    audits = {
        "n9_minimizer": audit_shelling_decoder(
            n9_points, certificate["n9_minimizer"]
        ),
        "pascal_T_4_2": audit_shelling_decoder(
            pascal6, certificate["pascal_T_4_2"]
        ),
        "vertical_T_3_1_square": audit_shelling_decoder(
            vertical9, certificate["vertical_T_3_1_square"]
        ),
    }
    assert sum(Q(1, 53 * (113 + 54 - 53)) for _ in range(3)) == Q(1, 2014)
    assert 54 * (113 + 54) >= 3
    assert Q(54) > Q(113 * 3, 8)  # K_8,1 versus f(8) log_2(8)/8.
    convex = audit_convex_polygons()
    assert convex == certificate["convex_polygon_rows"]
    vertical36 = audit_vertical_pascal_36(certificate["vertical_T_4_2_square"])

    print(
        "PASS: root maximum-hinged row Kraft, raw radial-chart union failure, "
        "and exact shelling-to-face fibre identity; "
        f"n9_shellings={audits['n9_minimizer']['shellings']}; "
        f"pascal6_shellings={audits['pascal_T_4_2']['shellings']}; "
        f"vertical9_shellings={audits['vertical_T_3_1_square']['shellings']}; "
        f"vertical36_raw/max={vertical36['raw_mass']}/{vertical36['maximum_mass']}"
    )


if __name__ == "__main__":
    main()
