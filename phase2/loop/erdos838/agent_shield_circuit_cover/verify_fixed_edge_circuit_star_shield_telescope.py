#!/usr/bin/env python3
"""Exact checks for FIXED_EDGE_CIRCUIT_STAR_SHIELD_TELESCOPE.md."""

from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (
        c[0] - a[0]
    )


def hull(points):
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def half(seq):
        out = []
        for p in seq:
            while len(out) >= 2 and cross(out[-2], out[-1], p) <= 0:
                out.pop()
            out.append(p)
        return out

    return half(pts)[:-1] + half(reversed(pts))[:-1]


def convex(points):
    return len(points) <= 2 or len(hull(points)) == len(points)


def powerset_nonempty(items):
    items = tuple(items)
    for mask in range(1, 1 << len(items)):
        yield frozenset(items[i] for i in range(len(items)) if mask >> i & 1)


def tangent_point(left, right):
    """u=(-1,0), v=(1,0), with left=y/(1+x), right=y/(1-x)."""
    return ((right - left) / (left + right), 2 * left * right / (left + right))


def inside_triangle_strict(p, a, b, c):
    signs = [cross(a, b, p), cross(b, c, p), cross(c, a, p)]
    return all(s > 0 for s in signs) or all(s < 0 for s in signs)


def longest_cyclic_run(mask, q):
    if not mask:
        return ()
    if len(mask) == q:
        return tuple(range(q))
    best = ()
    for start in range(q):
        if start in mask and (start - 1) % q not in mask:
            run = []
            j = start
            while j in mask:
                run.append(j)
                j = (j + 1) % q
            if len(run) > len(best) or (len(run) == len(best) and tuple(run) < best):
                best = tuple(run)
    return best


def check_geometry_and_telescope():
    u, v = (Q(-1), Q(0)), (Q(1), Q(0))
    b0, b1 = (Q(1), Q(-2)), (Q(-1), Q(-2))
    base = (u, v, b0, b1)

    roles = []
    params = {}
    labels = {}
    for i in range(4):
        role = []
        for t in range(4):
            left = Q(101 * (i + 1)) + Q((t + 1) ** 2, 19)
            right = Q(173 * (i + 1)) + Q((t + 1) ** 3, 103)
            p = tangent_point(left, right)
            lab = f"p{i}_{t}"
            role.append(lab)
            params[lab] = (left, right)
            labels[lab] = p
            assert convex(list(base) + [p])
        roles.append(role)

    ground = list(base) + [labels[z] for role in roles for z in role]
    assert all(cross(*triple) != 0 for triple in combinations(ground, 3))

    # Higher roles dominate lower roles in both tangent coordinates.  The
    # lower point is exactly the hidden member of {u,v,x,y}.
    directed = []
    for i in range(1, 4):
        for j in range(i):
            for x in roles[i]:
                for y in roles[j]:
                    lx, rx = params[x]
                    ly, ry = params[y]
                    assert lx > ly and rx > ry
                    assert inside_triangle_strict(labels[y], u, v, labels[x])
                    assert not convex([u, v, labels[x], labels[y]])
                    directed.append((x, y))

    # Three literal contexts on the opposite, nonadjacent edge.  They make
    # distinct actual carrier faces while reusing every detached star.
    contexts = {}
    for h in range(3):
        z = (Q(h - 1, 5), Q(-3) - Q((h + 1) ** 2, 97))
        contexts[h] = z
        assert all(cross(a, b, z) != 0 for a, b in combinations(ground, 2))

    stars = []
    for h, z in contexts.items():
        for i in range(1, 4):
            for x in roles[i]:
                neigh = tuple(y for j in range(i) for y in roles[j])
                carrier_pts = list(base) + [labels[x], z]
                assert convex(carrier_pts)
                carrier = frozenset({"u", "v", "b0", "b1", x, f"z{h}"})
                faces = set()
                for F in powerset_nonempty(neigh):
                    if convex([labels[y] for y in F]):
                        faces.add(F)
                        # No nonempty detached child face can be spliced
                        # back through the root carrier.
                        assert not convex(list(base) + [labels[x]] + [labels[y] for y in F])
                stars.append(
                    {
                        "weight": h + 1,
                        "carrier": carrier,
                        "faces": faces,
                        "degree": len(neigh),
                    }
                )

    carrier_load = defaultdict(int)
    shield_load = defaultdict(int)
    pair_load = defaultdict(int)
    total_weight = 0
    shield_incidence = 0
    circuit_mass = 0
    q2 = Q(0)
    bank_outputs = set()
    for g in stars:
        w = g["weight"]
        A = g["carrier"]
        h = len(g["faces"])
        d = g["degree"]
        assert h > 0
        total_weight += w
        shield_incidence += w * h
        circuit_mass += w * d
        q2 = max(q2, Q(d * d, h))
        carrier_load[A] += w
        bank_outputs.add(("A", A))
        for F in g["faces"]:
            shield_load[F] += w
            pair_load[(A, F)] += w
            bank_outputs.add(("F", F))

    kappa = max(carrier_load.values())
    lam = max(shield_load.values())
    mu = max(pair_load.values())
    vbank = len(bank_outputs)
    assert circuit_mass * circuit_mass <= q2 * total_weight * shield_incidence
    assert total_weight <= kappa * vbank
    assert shield_incidence <= lam * vbank
    assert circuit_mass * circuit_mass <= q2 * kappa * lam * vbank * vbank

    # A shield face of maximum load sees at least lambda/mu distinct actual
    # carrier outputs.
    Fmax = max(shield_load, key=shield_load.get)
    carriers = {g["carrier"] for g in stars if Fmax in g["faces"]}
    assert lam <= mu * len(carriers)

    return len(directed), len(stars), len(bank_outputs), kappa, lam, mu


def check_dense_orientation_pruning():
    # Abstract directed tensor with unequal degrees.  Removing vertices of
    # outdegree below E/(2N) retains at least half of all directed edges.
    N = 13
    edges = {(i, j) for i in range(N) for j in range(i) if (3 * i + j) % 5 != 0}
    E = len(edges)
    deg = [sum(1 for a, _ in edges if a == i) for i in range(N)]
    heavy = {i for i in range(N) if Q(deg[i]) >= Q(E, 2 * N)}
    kept = sum(deg[i] for i in heavy)
    assert kept >= Q(E, 2)
    return E, len(heavy), kept


def check_mask_run_load():
    q = 8
    records = []
    for mask_bits in range(1, 1 << q):
        mask = {i for i in range(q) if mask_bits >> i & 1}
        run = longest_cyclic_run(mask, q)
        weight = 1 + (mask_bits % 3)
        records.append((mask, run, weight))

    output_load = defaultdict(int)
    incidence = 0
    for _, run, weight in records:
        for J in powerset_nonempty(run):
            output = frozenset({"fixed_pair"}) | J
            output_load[output] += weight
            incidence += weight
    Lambda = max(output_load.values())
    assert incidence <= Lambda * len(output_load)

    # Exact longest-run lower bound by number of cyclic runs.
    for mask, run, _ in records:
        starts = [i for i in mask if (i - 1) % q not in mask]
        nruns = 1 if len(mask) == q else len(starts)
        assert len(run) * nruns >= len(mask)
    return len(records), len(output_load), Lambda


def check_arbitrary_child_barrier():
    u, v = (Q(-1), Q(0)), (Q(1), Q(0))
    base = [u, v, (Q(1), Q(-2)), (Q(-1), Q(-2))]
    outer = tangent_point(Q(8), Q(11))
    child = [
        (Q(-1, 5), Q(1, 10)),
        (Q(1, 10), Q(3, 25)),
        (Q(1, 4), Q(9, 50)),
        (Q(-1, 10), Q(1, 4)),
        (Q(1, 20), Q(3, 10)),
    ]
    assert convex(base + [outer])
    assert all(convex(base + [y]) for y in child)
    assert all(inside_triangle_strict(y, u, v, outer) for y in child)
    ground = base + [outer] + child
    assert all(cross(*triple) != 0 for triple in combinations(ground, 3))
    local_faces = 0
    for F in powerset_nonempty(range(len(child))):
        pts = [child[i] for i in F]
        if convex(pts):
            local_faces += 1
            assert not convex(base + [outer] + pts)
    return local_faces


def main():
    geom = check_geometry_and_telescope()
    prune = check_dense_orientation_pruning()
    masks = check_mask_run_load()
    child_faces = check_arbitrary_child_barrier()
    print(
        "PASS: fixed-edge circuit stars are triangle-containment DAGs; "
        f"geometry={geom}, pruning={prune}, mask_run={masks}, "
        f"arbitrary_child_faces={child_faces}"
    )


if __name__ == "__main__":
    main()
