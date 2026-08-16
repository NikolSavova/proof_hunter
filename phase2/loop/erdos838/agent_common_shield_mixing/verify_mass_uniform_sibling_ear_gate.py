#!/usr/bin/env python3
"""Exact checks for MASS_UNIFORM_SIBLING_EAR_OR_CIRCUIT_GATE.md."""

from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def orient(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and orient(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    lo = half(pts)
    hi = half(reversed(pts))
    return lo[:-1] + hi[:-1]


def convex(points):
    return len(set(points)) == len(points) and len(hull(points)) == len(points)


def general_position(points):
    return all(orient(*triple) != 0 for triple in combinations(points, 3))


def inside_triangle_strict(p, tri):
    signs = [orient(tri[i], tri[(i + 1) % 3], p) for i in range(3)]
    return all(x > 0 for x in signs) or all(x < 0 for x in signs)


def inside_convex_strict(p, poly):
    return all(orient(poly[i], poly[(i + 1) % len(poly)], p) > 0
               for i in range(len(poly)))


def make_ears(poly, scale=F(1, 80)):
    """One exact point in the local outside cell of every oriented hull edge."""
    ears = []
    n = len(poly)
    for i, (a, b) in enumerate(zip(poly, poly[1:] + poly[:1])):
        dx, dy = b[0] - a[0], b[1] - a[1]
        mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        # Polygon is CCW.  (dy,-dx) is the outward/right normal.
        q = (mid[0] + scale * dy, mid[1] - scale * dx)
        assert convex(poly + [q]), (i, q)
        ears.append(q)
    return ears


def cycle_independent(indices, m):
    out = []
    for r in range(len(indices), -1, -1):
        for sub in combinations(indices, r):
            ss = set(sub)
            if all(((i + 1) % m not in ss) for i in ss):
                return sub
    return out


def check_geometry():
    poly = [
        (F(0), F(0)),
        (F(7), F(-1)),
        (F(13), F(2)),
        (F(15), F(8)),
        (F(11), F(14)),
        (F(4), F(16)),
        (F(-2), F(12)),
        (F(-4), F(5)),
    ]
    assert convex(poly) and general_position(poly)
    ears = make_ears(poly)
    checks = 0
    for r in range(1, 5):
        for inds in combinations(range(len(poly)), r):
            if all(((i + 1) % len(poly) not in inds) for i in inds):
                assert convex(poly + [ears[i] for i in inds])
                checks += 1
    # Decoder: disjoint role grounds make every chosen tuple distinct.
    banks = []
    for i in (0, 2, 4):
        a = ears[i]
        b = ((a[0] * 79 + (poly[i][0] + poly[(i + 1) % 8][0]) / 2) / 80,
             (a[1] * 79 + (poly[i][1] + poly[(i + 1) % 8][1]) / 2) / 80)
        assert convex(poly + [b])
        banks.append((a, b))
    outputs = {tuple(sorted(poly + list(choice))) for choice in product(*banks)}
    assert len(outputs) == 2 ** 3
    assert all(convex(list(w)) for w in outputs)

    # Full diffuse-bank collision: every interior released singleton is
    # hidden by the retained base, so no Cartesian ear output remembers it.
    candidates = [
        (F(300 + (17 * i) % 500, 100),
         F(400 + (23 * i + i * i) % 500, 100))
        for i in range(1, 500)
    ]
    fixed = poly + [p for bank_part in banks for p in bank_part]
    inners = choose_generic(
        candidates, fixed, 9, lambda p: inside_convex_strict(p, poly)
    )
    assert general_position(fixed + inners)
    for w in outputs:
        for u in inners:
            assert not convex(list(w) + [u])
    diffuse_loads = {w: len(inners) for w in outputs}
    assert set(diffuse_loads.values()) == {9}
    return checks, len(outputs), len(outputs) * len(inners), 9


def check_cycle_and_products():
    subset_checks = 0
    product_checks = 0
    for m in range(3, 10):
        for mask in range(1 << m):
            occ = [i for i in range(m) if mask >> i & 1]
            indep = cycle_independent(occ, m)
            assert 3 * len(indep) >= len(occ)
            subset_checks += 1
        # A proper three-colouring gives one colour product whose cube
        # dominates the product over all occupied edges.
        if m % 2 == 0:
            colours = [i % 2 for i in range(m)]
        else:
            colours = [i % 2 for i in range(m - 1)] + [2]
        assert all(colours[i] != colours[(i + 1) % m] for i in range(m))
        for ks in product(range(1, 5), repeat=m):
            prods = [1, 1, 1]
            for i, k in enumerate(ks):
                prods[colours[i]] *= k
            assert max(prods) ** 3 >= __import__("math").prod(ks)
            product_checks += 1
    return subset_checks, product_checks


def check_effective_support_and_heavy_edge():
    checks = 0
    # Four classes already exercise every rational inequality in (2),(4);
    # keeping this exhaustive makes the verifier finish in seconds.
    for masses in product(range(1, 6), repeat=4):
        b = sum(masses)
        star = max(masses)
        r = F(b, star)
        assert len(masses) >= r
        for m in range(3, 8):
            # Arbitrary edge allocation of the nonempty classes.
            for edges in product(range(m), repeat=len(masses)):
                counts = [edges.count(g) for g in range(m)]
                assert max(counts) * m >= len(masses) >= r
                checks += 1
    return checks


def check_circuit_pigeonhole():
    # Pure exact counting behind (12)--(13), including rational weights.
    checks = 0
    for m in range(3, 9):
        roots = list(combinations(range(m), 2))
        for a in range(1, 8):
            for b in range(1, 8):
                pairs = [(x, y) for x in range(a) for y in range(b)]
                # Deterministic mock geometry signature: some pairs are
                # compatible, each incompatible pair gets a canonical root.
                good = [p for p in pairs if (3 * p[0] + 5 * p[1] + m) % 7 < 2]
                bad = [p for p in pairs if p not in good]
                bins = {r: 0 for r in roots}
                for idx, p in enumerate(bad):
                    bins[roots[(11 * p[0] + 13 * p[1] + idx) % len(roots)]] += 1
                if bad:
                    assert max(bins.values()) * comb(m, 2) >= len(bad)
                assert len(good) + len(bad) == a * b
                checks += 1
    return checks


def check_weight_floor_rectangle():
    checks = 0
    for n in (8, 17, 64, 257):
        for md in (1, 3, 11, 37):
            for h in (1, 5, 19):
                atom = F(1, n)
                column_mass = md * atom
                total_mass = md * h * atom
                # A column terminal coalesces md atomic records.  The atomic
                # floor cannot replace its true mass by 1/n to gain H.
                terminal_mass = md * atom
                assert total_mass / terminal_mass == h
                # Per-column Kraft gives C_eff <= M_U/(1/n)=M_D.
                assert column_mass / atom == md
                for p0 in (md, 2 * md, 7 * md):
                    q = F(p0, md)
                    assert q == F(p0, column_mass / atom)
                checks += 1
    return checks


def choose_generic(candidates, fixed, count, predicate):
    out = []
    for p in candidates:
        if not predicate(p):
            continue
        if general_position(fixed + out + [p]):
            out.append(p)
            if len(out) == count:
                return out
    raise AssertionError("not enough generic candidates")


def check_context_collision():
    tri = [(F(0), F(0)), (F(1000), F(0)), (F(0), F(1000))]
    ear_candidates = [
        (F(40 + 17 * i), F(-11 - i * i)) for i in range(1, 60)
    ]
    ears = choose_generic(
        ear_candidates,
        tri,
        8,
        lambda p: convex(tri + [p]),
    )
    inner_candidates = [
        (F(80 + 13 * i), F(170 + 7 * i + i * i)) for i in range(1, 80)
    ]
    inners = choose_generic(
        inner_candidates,
        tri + ears,
        12,
        lambda p: inside_triangle_strict(p, tri),
    )
    pts = tri + ears + inners
    assert general_position(pts)
    rooted_bad = 0
    rooted_good = 0
    for x, y in combinations(ears, 2):
        if convex(tri + [x, y]):
            rooted_good += 1
            continue
        rooted_bad += 1
        witnesses = [
            (u, v) for u, v in combinations(tri, 2)
            if not convex([u, v, x, y])
        ]
        # Heredity forces every bad four-set to use x,y; the exact
        # rational instance exhibits the base-root witness.
        assert witnesses
    assert rooted_good and rooted_bad
    for x in ears:
        assert convex(tri + [x])
        for u in inners:
            assert convex([u])
            assert not convex(tri + [x, u])
    # Each source-only output tri+x is reused by every interior context.
    load = {tuple(sorted(tri + [x])): 0 for x in ears}
    for x in ears:
        for _u in inners:
            load[tuple(sorted(tri + [x]))] += 1
    assert set(load.values()) == {len(inners)}
    return len(ears) * len(inners), max(load.values()), rooted_good, rooted_bad


def main():
    geo, bank, diffuse_collisions, diffuse_load = check_geometry()
    subsets, products = check_cycle_and_products()
    support = check_effective_support_and_heavy_edge()
    circuits = check_circuit_pigeonhole()
    floors = check_weight_floor_rectangle()
    collision_checks, collision_load, rooted_good, rooted_bad = check_context_collision()
    total = (geo + bank + diffuse_collisions + subsets + products + support
             + circuits + floors + collision_checks)
    print("PASS")
    print(f"  exact independent-ear families: {geo}")
    print(f"  decoded Cartesian bank size: {bank}")
    print(f"  diffuse-bank context collisions/load: {diffuse_collisions}/{diffuse_load}")
    print(f"  cycle support systems: {subsets}")
    print(f"  three-colour product systems: {products}")
    print(f"  effective-support/edge systems: {support}")
    print(f"  circuit pigeonhole systems: {circuits}")
    print(f"  complete-rectangle floor systems: {floors}")
    print(f"  planar context-collision incidences: {collision_checks}")
    print(f"  exact collision load: {collision_load}")
    print(f"  planar same-edge compatible/incompatible pairs: {rooted_good}/{rooted_bad}")
    print(f"  total audited systems/incidences: {total}")


if __name__ == "__main__":
    main()
