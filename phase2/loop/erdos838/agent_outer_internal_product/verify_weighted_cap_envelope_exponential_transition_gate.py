#!/usr/bin/env python3
"""Exact checks for WEIGHTED_CAP_ENVELOPE_EXPONENTIAL_TRANSITION_GATE.md."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import importlib.util
import json
import sys


ROOT = Path(__file__).resolve().parent.parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def envelope_algebra_audit() -> int:
    """Finite exact regression of concavity slopes and comparison with f,p."""
    checked = 0
    penalties = (Fraction(1, 7), Fraction(1, 2), Fraction(1),
                 Fraction(3, 2), Fraction(4), Fraction(13))
    for shift in range(1, 151):
        profiles = []
        for index in range(9):
            # Deliberately nonconvex-looking menus: the theorem needs only a
            # finite collection of integer profile pairs.
            w = 20 + ((17 * index * index + 11 * shift * index + shift) % 83)
            c = 3 + ((19 * index + 7 * shift + index * index) % 31)
            profiles.append((w, c))
        f = min(w for w, _ in profiles)
        p = min(c for w, c in profiles if w == f)

        selected = []
        for t in penalties:
            optimum = min(Fraction(w) + t * c for w, c in profiles)
            optimizers = [(w, c) for w, c in profiles
                          if Fraction(w) + t * c == optimum]
            # Every optimizer, not just a favorable tie choice, obeys (4).
            for w, c in optimizers:
                assert c <= p
                assert Fraction(w - f) <= t * (p - c)
                checked += 1
            selected.append(max(c for _, c in optimizers))
        assert all(c2 <= c1 for c1, c2 in zip(selected, selected[1:]))

        # Pairwise proof of slope monotonicity, including all ties.
        for i, t1 in enumerate(penalties):
            for t2 in penalties[i + 1:]:
                opt1 = min(Fraction(w) + t1 * c for w, c in profiles)
                opt2 = min(Fraction(w) + t2 * c for w, c in profiles)
                for w1, c1 in profiles:
                    if Fraction(w1) + t1 * c1 != opt1:
                        continue
                    for w2, c2 in profiles:
                        if Fraction(w2) + t2 * c2 == opt2:
                            assert c2 <= c1
                            checked += 1
    return checked


def all_nonempty(labels: tuple[int, ...]):
    for rank in range(1, len(labels) + 1):
        yield from combinations(labels, rank)


def one_flip_audit(g, maximum_size: int = 16) -> dict[str, int]:
    subset_checks = 0
    triple_checks = 0
    for size in range(4, maximum_size + 1):
        cup_points = tuple(g.Point(Fraction(i), Fraction(2 * i * i))
                           for i in range(size))
        points = (g.Point(Fraction(0), Fraction(0)),
                  g.Point(Fraction(1), Fraction(5))) + tuple(
                      g.Point(Fraction(i), Fraction(2 * i * i))
                      for i in range(2, size)
                  )
        cup_orient = g.orient_table(cup_points)
        orient = g.orient_table(points)
        flipped = []
        for triple in combinations(range(size), 3):
            i, j, k = triple
            if cup_orient[i][j][k] != orient[i][j][k]:
                flipped.append(triple)
            triple_checks += 1
        assert flipped == [(0, 1, 2)]

        caps = 0
        faces = 0
        bad = 0
        maximum_cap_rank = 0
        labels = tuple(range(size))
        for subset in all_nonempty(labels):
            expected_bad = ({0, 1, 2}.issubset(subset)
                            and any(label >= 3 for label in subset))
            got_face = g.is_convex(subset, orient)
            assert got_face == (not expected_bad), (size, subset)
            if got_face:
                faces += 1
            else:
                bad += 1
            if g.is_cap(subset, orient):
                caps += 1
                maximum_cap_rank = max(maximum_cap_rank, len(subset))
            subset_checks += 1

        ell = size + comb(size, 2)
        assert caps == ell + 1
        assert maximum_cap_rank == 3
        assert bad == (1 << (size - 3)) - 1
        assert faces == 7 * (1 << (size - 3))

        cup_caps = sum(g.is_cap(subset, cup_orient)
                       for subset in all_nonempty(labels))
        cup_faces = sum(g.is_convex(subset, cup_orient)
                        for subset in all_nonempty(labels))
        assert cup_caps == ell
        assert cup_faces == (1 << size) - 1

        saving = cup_faces - faces
        assert saving == (1 << (size - 3)) - 1

    return {
        "sizes": maximum_size - 3,
        "subset_checks": subset_checks,
        "triple_checks": triple_checks,
    }


def four_point_envelope_audit(wrapper) -> dict[str, object]:
    profiles = []
    for seed in wrapper.SEEDS:
        cap, cup, faces = wrapper.local_profile(seed)
        profiles.append((faces, cap, cup))
    assert sorted(set(profiles)) == [
        (14, 11, 13), (14, 13, 11), (15, 10, 15),
        (15, 12, 12), (15, 15, 10),
    ]

    for t in (Fraction(1, 10), Fraction(1, 2), Fraction(1),
              Fraction(2), Fraction(11)):
        got = min(Fraction(w) + t * c for w, c, _ in profiles)
        want = min(Fraction(14) + 11 * t, Fraction(15) + 10 * t)
        assert got == want

    ell = 10
    critical = max(Fraction(15 - w, c - ell)
                   for w, c, _ in profiles if c > ell)
    assert critical == 1
    return {"rooted_types": len(profiles), "profiles": sorted(set(profiles)),
            "critical": str(critical)}


def cap_cover_audit(g, raw_points) -> tuple[int, int, int]:
    points = tuple(sorted(raw_points, key=lambda point: point.x))
    orient = g.orient_table(points)
    size = len(points)
    cap_triples = [triple for triple in combinations(range(size), 3)
                   if g.is_cap(triple, orient)]
    checked = 0
    for rank in range(3, size + 1):
        has_cup = any(g.is_cup(subset, orient)
                      for subset in combinations(range(size), rank))
        if has_cup:
            continue
        lhs = len(cap_triples) * comb(size - 3, rank - 3)
        rhs = comb(size, rank)
        assert lhs >= rhs
        assert len(cap_triples) * comb(rank, 3) >= comb(size, 3)
        checked += 1
    return size, len(cap_triples), checked


def geometric_cover_audits(g) -> list[tuple[int, int, int]]:
    configurations = []
    configurations.append(tuple(g.Point(Fraction(i), Fraction(2 * i * i))
                                if i != 1 else
                                g.Point(Fraction(1), Fraction(5))
                                for i in range(11)))
    configurations.append(g.cell(6, 3))

    data = json.loads((ROOT / "agent_lex_minimizer_search" /
                       "direct_hull_certificates.json").read_text())
    for key in ("8", "9"):
        configurations.append(tuple(
            g.Point(Fraction(x), Fraction(y))
            for x, y in data[key]["coordinates"]
        ))
    rows = [cap_cover_audit(g, points) for points in configurations]
    assert sum(row[2] for row in rows) > 0
    return rows


def minimizer_projection_audit(wrapper) -> dict[str, object]:
    data = json.loads((ROOT / "agent_lex_minimizer_search" /
                       "direct_hull_certificates.json").read_text())
    rows = {}
    expected = {"8": (113, 56, 56), "9": (168, 82, 82)}
    for key in ("8", "9"):
        points = [tuple(map(Fraction, point))
                  for point in data[key]["coordinates"]]
        signs = wrapper.all_signs(points)
        perturbed = wrapper.generic_perturb(points, signs)
        orders = wrapper.projection_orders(perturbed)
        profiles = [wrapper.chain_counts(signs, order) for order in orders]
        face_count = data[key]["nonempty_count"]
        want_w, want_c, want_u = expected[key]
        assert face_count == want_w
        assert min(c for c, _ in profiles) == want_c
        assert min(u for _, u in profiles) == want_u
        assert len(orders) == int(key) * (int(key) - 1)
        rows[key] = (face_count, len(orders), want_c, want_u)
    return rows


def live_scale_audit() -> list[tuple[int, int, int, int]]:
    rows = []
    for length in (32, 48, 64, 96, 128):
        exponent = 49 * length * length // 100
        target = 1 << exponent
        child_size = 1 << (length - 1)
        rank = exponent + 1  # ceil(log_2(target+1))
        assert 3 <= rank <= child_size

        numerator = comb(child_size, 3)
        denominator = comb(rank, 3)
        gamma = (numerator + denominator - 1) // denominator
        ell = child_size + comb(child_size, 2)
        cover_product = (ell + gamma) ** 2

        # The one-flip lower witness gives T_a >= 2^(a-3)-1.
        assert child_size - 3 > exponent
        # The polynomial cap-triple bank remains below the fixed-gap target.
        assert cover_product < target
        rows.append((length, exponent, cover_product.bit_length() - 1,
                     child_size - 3))
    return rows


def main() -> None:
    g = load_module("weighted_cap_geometry",
                    ROOT / "agent_geometry" / "audit_geometry.py")
    wrapper = load_module(
        "weighted_cap_wrapper",
        ROOT / "agent_shield_circuit_cover" /
        "verify_two_direction_four_point_wrapper.py",
    )
    algebra = envelope_algebra_audit()
    flip = one_flip_audit(g)
    four = four_point_envelope_audit(wrapper)
    covers = geometric_cover_audits(g)
    minimizers = minimizer_projection_audit(wrapper)
    scales = live_scale_audit()
    print(
        "PASS: weighted cap envelope, exponential one-flip transition, "
        "cap-triple cover, minimizer chambers, and live scale barrier; "
        f"algebra={algebra}; flip={flip}; four={four}; covers={covers}; "
        f"minimizers={minimizers}; scales={scales}"
    )


if __name__ == "__main__":
    main()
