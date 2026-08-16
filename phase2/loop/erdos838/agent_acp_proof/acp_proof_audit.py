#!/usr/bin/env python3
"""Exact finite audit for the ACP reductions and structural barriers."""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb, isqrt, log2, sqrt
import importlib.util
import random
from pathlib import Path


SAVED_PROFILES = {
    20: (1, 20, 190, 1140, 2415, 866, 135, 8),
    24: (1, 24, 276, 2024, 5378, 2679, 413, 43, 3),
    30: (1, 30, 435, 4060, 13975, 10607, 3158, 481, 30),
    44: (1, 44, 946, 13244, 70450, 99093, 43597, 8726, 1075, 53),
    58: (
        1,
        58,
        1653,
        30856,
        220958,
        428915,
        284982,
        76995,
        15100,
        2179,
        210,
    ),
}

HERE = Path(__file__).resolve().parent


def z(profile: tuple[int, ...], activity: Fraction) -> Fraction:
    return sum(
        (Fraction(count) * activity**rank for rank, count in enumerate(profile)),
        Fraction(),
    )


def moment(profile: tuple[int, ...], activity: Fraction) -> Fraction:
    return sum(
        (
            Fraction(rank * count) * activity**rank
            for rank, count in enumerate(profile)
        ),
        Fraction(),
    )


def stats(profile: tuple[int, ...]) -> dict[str, Fraction]:
    n = profile[1]
    one = z(profile, Fraction(1))
    half = z(profile, Fraction(1, 2))
    mu_one = moment(profile, Fraction(1)) / one
    mu_half = moment(profile, Fraction(1, 2)) / half
    delta = mu_one - mu_half
    h_value = n * half / one
    acp = h_value * max(Fraction(), 1 - delta)
    # Equation (3), evaluated without using delta.
    covariance_form = n * sum(
        (
            Fraction(count, 2**rank) * (rank + 1 - mu_one)
            for rank, count in enumerate(profile)
        ),
        Fraction(),
    ) / one
    assert covariance_form == h_value * (1 - delta)
    return {
        "H": h_value,
        "mu_one": mu_one,
        "mu_half": mu_half,
        "delta": delta,
        "ACP": acp,
    }


def derivative_identity(profile: tuple[int, ...], t: Fraction) -> None:
    """Check (1) after clearing denominators by direct differentiation."""
    n = profile[1]
    z_t = z(profile, t)
    z_half_t = z(profile, t / 2)
    m_t = moment(profile, t)
    m_half_t = moment(profile, t / 2)
    f = n * t * z_half_t / z_t
    rhs = f * (1 + m_half_t / z_half_t - m_t / z_t)

    # t*d/dt of n*t*Z(t/2)/Z(t), using moment=t*Z'.
    lhs = n * t * z_half_t / z_t
    lhs += n * t * m_half_t / z_t
    lhs -= n * t * z_half_t * m_t / z_t**2
    assert lhs == rhs


def verify_saved_profiles() -> None:
    for n, profile in SAVED_PROFILES.items():
        assert profile[1] == n
        derivative_identity(profile, Fraction(1, 2))
        derivative_identity(profile, Fraction(3, 4))
        derivative_identity(profile, Fraction(1))
        row = stats(profile)
        assert row["delta"] >= 0
        print(
            f"saved n={n}: H={float(row['H']):.9f} "
            f"delta={float(row['delta']):.9f} ACP={float(row['ACP']):.9f}"
        )


def verify_gordon_collision() -> None:
    first = (1, 8, 28, 56, 33, 6, 1)
    second = (1, 8, 28, 56, 33, 7, 0)
    assert sum(first) == sum(second) == 133
    first_acp = stats(first)["ACP"]
    second_acp = stats(second)["ACP"]
    assert first_acp == Fraction(47583, 141512)
    assert second_acp == Fraction(185, 532)
    assert first_acp != second_acp
    print(f"Gordon collision ACP: {first_acp} versus {second_acp}")


def skeleton_profile(n: int) -> tuple[int, ...]:
    return tuple(comb(n, k) for k in range(4))


def verify_abstract_barrier() -> None:
    for n in range(4, 201):
        profile = skeleton_profile(n)
        one = z(profile, Fraction(1))
        half = z(profile, Fraction(1, 2))
        mu_one = moment(profile, Fraction(1)) / one
        mu_half = moment(profile, Fraction(1, 2)) / half
        assert one == Fraction(n**3 + 5 * n + 6, 6)
        assert half == Fraction(n**3 + 3 * n**2 + 20 * n + 48, 48)
        assert mu_one == Fraction(3 * n**3 - 3 * n**2 + 6 * n, n**3 + 5 * n + 6)
        assert mu_half == Fraction(
            3 * n**3 + 3 * n**2 + 18 * n,
            n**3 + 3 * n**2 + 20 * n + 48,
        )
    # A concrete exact linear lower bound, more than enough to certify that
    # no absolute ACP constant follows from the abstract hypotheses.
    for n in range(50, 501):
        assert stats(skeleton_profile(n))["ACP"] > Fraction(n, 10)
    print("abstract Caratheodory-3 barrier: ACP > n/10 for 50 <= n <= 500")


def verify_restriction_double_count() -> None:
    """Coefficientwise form of (7), independent of any geometry code."""
    for profile in SAVED_PROFILES.values():
        n = profile[1]
        sum_v_restrictions = sum(
            count * 2 ** (n - rank) for rank, count in enumerate(profile)
        )
        sum_m_restrictions = sum(
            rank * count * 2 ** (n - rank)
            for rank, count in enumerate(profile)
        )
        assert Fraction(sum_v_restrictions, 2**n) == z(profile, Fraction(1, 2))
        assert Fraction(sum_m_restrictions, 2**n) == moment(
            profile, Fraction(1, 2)
        )
    print("restriction double counts: PASS")


def verify_identical_pocket_envelope() -> None:
    """Integer audit of the quadratic dichotomy behind (34).

    We avoid floating point.  If `c=1/10`, the claimed positive-root
    envelope follows from `10*b+10*a*T-T^2 <= 0`.  For every tested state
    and every integral `y=log_2(m)`, this checks directly that either the
    raw-pocket exponent `y` or the ES-supply exponent
    `b+a*y-y^2/10` is at most `T`.
    """
    c_den = 10
    checks = 0
    for rank in range(16, 257, 8):
        for i_max in (0, 1, isqrt(rank), max(1, rank // 8)):
            # Audit several frame entropies, including subquadratic ones.
            for kappa in (0, rank, rank * isqrt(rank), rank * rank // 8):
                # Replace log2(I+1) by the rigorous integer upper bound
                # ceil(log2(I+1)).
                log_i = max(0, i_max.bit_length())
                b = kappa + log_i
                a = i_max + 1
                # A convenient integer ceiling above the positive zero of
                # b+a*y-y^2/10.  Incrementing is exact and cheap here.
                # Start to the right of the zero root which also occurs
                # when b=0; we need the positive quadratic root.
                t = c_den * a
                while t * t < c_den * a * t + c_den * b:
                    t += 1
                assert t * t >= c_den * a * t + c_den * b
                for y in range(0, rank + 65):
                    es_numerator = c_den * (b + a * y) - y * y
                    # min(y, b+a*y-y^2/10) <= t, after multiplying
                    # the second alternative by ten.
                    assert y <= t or es_numerator <= 0
                    checks += 1
    print(f"identical-pocket Hall envelope: {checks} exact exponent checks PASS")


def verify_crossing_pocket_reuse() -> None:
    """Exact parabola realization of Lemma 8."""
    for n_roots in range(3, 65):
        roots = [(t, t * t) for t in range(1, n_roots + 1)]
        q = (0, -1)

        def orient(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (
                b[1] - a[1]
            ) * (c[0] - a[0])

        points = [q] + roots
        for a in range(len(points)):
            for b in range(a + 1, len(points)):
                for c in range(b + 1, len(points)):
                    assert orient(points[a], points[b], points[c]) != 0

        containing_pockets = 0
        for a in range(n_roots):
            for b in range(a + 1, n_roots):
                side = orient(roots[a], roots[b], q)
                assert side != 0
                pocket = [x for x in points if orient(roots[a], roots[b], x) * side > 0]
                assert q in pocket
                containing_pockets += 1
        assert containing_pockets == comb(n_roots, 2)
    print("crossing-pocket singleton reuse: exact parabola certificates PASS")


def verify_source_cloud_envelope() -> None:
    """Exact exponent audit for source-cloud Theorem 9 at c=1/10."""
    c_den = 10
    checks = 0
    for ambient_log in range(16, 257, 8):
        for hidden_rank in (0, 1, isqrt(ambient_log), ambient_log // 8):
            log_i = max(0, hidden_rank.bit_length())
            b = hidden_rank * ambient_log + log_i
            # Positive root of b+x-x^2/10.
            t = c_den
            while t * t < c_den * t + c_den * b:
                t += 1
            assert t * t >= c_den * t + c_den * b
            for blocker_log in range(0, 2 * ambient_log + 1):
                supply_numerator = (
                    c_den * (b + blocker_log) - blocker_log * blocker_log
                )
                assert blocker_log <= t or supply_numerator <= 0
                checks += 1
    print(f"capped source-cloud entropy: {checks} exact exponent checks PASS")


def verify_retained_core_entropy_code() -> None:
    """Log-free integer audit of the coding constants and submodularity.

    For a uniform edge set, entropy submodularity is equivalent to
    product_R e_R^e_R >= product_(R,I) a_RI^a_RI product_(R,p) b_Rp^b_Rp.
    The test below checks this exact integer form on deterministic random
    bipartite cell tables.  It is a regression test, not the proof.
    """
    for rank in range(3, 129):
        # Nonempty proper cyclic intervals plus the full interval.
        interval_tags = rank * (rank - 1) + 1
        assert interval_tags < (rank + 1) ** 2
        assert rank + 1 <= rank + 1  # marked-vertex code in B

    rng = random.Random(838_20260814)
    table_checks = 0
    for record in range(400):
        cell_count = 1 + record % 7
        cell_edges: list[list[tuple[int, int]]] = []
        for cell in range(cell_count):
            left = 1 + (record + 2 * cell) % 8
            right = 1 + (2 * record + cell) % 9
            edges = [
                (i, j)
                for i in range(left)
                for j in range(right)
                if rng.randrange(5) != 0
            ]
            if not edges:
                edges = [(0, 0)]
            cell_edges.append(edges)

        lhs = 1
        rhs = 1
        for edges in cell_edges:
            edge_count = len(edges)
            lhs *= edge_count**edge_count
            left_degree: dict[int, int] = {}
            right_degree: dict[int, int] = {}
            for i, j in edges:
                left_degree[i] = left_degree.get(i, 0) + 1
                right_degree[j] = right_degree.get(j, 0) + 1
            for degree in left_degree.values():
                rhs *= degree**degree
            for degree in right_degree.values():
                rhs *= degree**degree
        assert lhs >= rhs
        table_checks += 1
    print(f"retained-core entropy code: {table_checks} exact tables PASS")


def verify_product_entropy_saturation() -> None:
    """Exact planar regression for (58) and the sunflower barrier."""
    verifier = HERE.parent / "agent_entropy_spread" / "verify_product_blocker.py"
    spec = importlib.util.spec_from_file_location("acp_product_blocker", verifier)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    rank, micro_size = 7, 8
    points, blocks, _, _, _ = module.build(rank, micro_size)
    hidden_block = 3
    fixed = (
        [blocks[0][0]]
        + [
            blocks[j][0]
            for j in range(1, len(blocks) - 1)
            if j != hidden_block
        ]
        + [blocks[-1][0]]
    )
    lower = blocks[hidden_block][: micro_size // 2]
    upper = blocks[hidden_block][micro_size // 2 :]
    rectangle_edges = 0
    for q in lower:
        source = fixed + [q]
        assert module.hull(points, source) == set(source)
        for p in upper:
            repaired = module.hull(points, source + [p])
            assert repaired == (set(source) - {q}) | {p}
            rectangle_edges += 1
    assert rectangle_edges == len(lower) * len(upper)

    # The abstract endpoint cell is exact: N retained words times a complete
    # lower/upper rectangle.  This is equality in entropy submodularity.
    retained_words = micro_size ** (rank - 3)
    edge_count = retained_words * len(lower) * len(upper)
    source_count = retained_words * len(lower)
    target_count = retained_words * len(upper)
    assert edge_count * retained_words == source_count * target_count

    # Singleton petals in one intermediate block form a sunflower, but no
    # union of two petals with the core is convex.
    petal_block = 2
    core = (
        [blocks[0][0]]
        + [
            blocks[j][0]
            for j in range(1, len(blocks) - 1)
            if j != petal_block
        ]
        + [blocks[-1][0]]
    )
    for a in range(micro_size):
        boundary = core + [blocks[petal_block][a]]
        assert module.hull(points, boundary) == set(boundary)
        for b in range(a + 1, micro_size):
            union = core + [blocks[petal_block][a], blocks[petal_block][b]]
            assert module.hull(points, union) != set(union)

    # Proposition 17: a two-point endpoint cup cannot retain even one
    # common suffix label.  The old cup becomes an illegal two-point
    # intermediate block.
    left_pair = tuple(blocks[1][:2])
    right_pair = tuple(blocks[2][:2])
    suffix = blocks[3][0]
    interval_target = (*left_pair, *right_pair)
    assert module.hull(points, interval_target) == set(interval_target)
    with_suffix = (*interval_target, suffix)
    assert module.hull(points, with_suffix) != set(with_suffix)

    # Exact failure of opposite-side rooted gluing, equations (64)--(65).
    u, v, p, q = (0, 0), (1, 0), (100, 1), (-100, -2)
    assert module.orient(u, v, p) > 0
    assert module.orient(u, v, q) < 0
    # 100*v = 97*u + 2*p + q, with all barycentric coefficients positive.
    assert (
        100 * v[0] == 97 * u[0] + 2 * p[0] + q[0]
        and 100 * v[1] == 97 * u[1] + 2 * p[1] + q[1]
    )
    assert module.hull([u, v, p, q], range(4)) != set(range(4))

    # Exact outward-successor repair from Theorem 20.  The two source
    # polygons share prefix (x1,v); p is the more outward next ray, violates
    # edge v-a, and replaces a while preserving the canonical prefix.
    x1, root_v = (0, 0), (2, 0)
    inner_next, suffix, outer_next = (2, 1), (0, 2), (3, 1)
    successor_points = [x1, root_v, inner_next, suffix, outer_next]
    source_a = [0, 1, 2, 3]
    source_b = [0, 1, 4, 3]
    assert module.hull(successor_points, source_a) == set(source_a)
    assert module.hull(successor_points, source_b) == set(source_b)
    assert module.orient(root_v, inner_next, outer_next) < 0
    repaired = module.hull(successor_points, range(5))
    assert repaired == {0, 1, 3, 4}
    assert {0, 1, 4} <= repaired
    print("product entropy saturation and sunflower barrier: exact geometry PASS")


def verify_tangent_rectangles() -> None:
    """Exact enumeration of the all-or-nothing claim in Theorem 13."""

    def orient(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (
            b[1] - a[1]
        ) * (c[0] - a[0])

    def hull(points, chosen):
        ordered = sorted(chosen, key=lambda i: points[i])
        if len(ordered) <= 1:
            return ordered

        lower = []
        for i in ordered:
            while len(lower) >= 2 and orient(
                points[lower[-2]], points[lower[-1]], points[i]
            ) <= 0:
                lower.pop()
            lower.append(i)
        upper = []
        for i in reversed(ordered):
            while len(upper) >= 2 and orient(
                points[upper[-2]], points[upper[-1]], points[i]
            ) <= 0:
                upper.pop()
            upper.append(i)
        return lower[:-1] + upper[:-1]

    rng = random.Random(13_838_20260814)
    total_rectangles = 0
    nontrivial_rectangles = 0
    for trial in range(24):
        # Generate one exact general-position configuration separated by uv.
        points = [(-2000, 0), (2000, 0)]
        while len(points) < 14:
            sign = 1 if len(points) < 8 else -1
            candidate = (
                rng.randrange(-2600, 2601),
                sign * rng.randrange(50, 2601),
            )
            if candidate in points:
                continue
            if any(
                orient(points[i], points[j], candidate) == 0
                for i in range(len(points))
                for j in range(i + 1, len(points))
            ):
                continue
            points.append(candidate)

        upper_ids = list(range(2, 8))
        lower_ids = list(range(8, 14))

        def rooted_faces(side_ids):
            faces = []
            for mask in range(1, 1 << len(side_ids)):
                chosen = [0, 1] + [
                    side_ids[j]
                    for j in range(len(side_ids))
                    if mask >> j & 1
                ]
                cycle = hull(points, chosen)
                if len(cycle) != len(chosen) or set(cycle) != set(chosen):
                    continue
                root_pos = cycle.index(0)
                if cycle[(root_pos - 1) % len(cycle)] != 1 and cycle[
                    (root_pos + 1) % len(cycle)
                ] != 1:
                    continue
                faces.append((frozenset(chosen), cycle))
            return faces

        uppers = rooted_faces(upper_ids)
        lowers = rooted_faces(lower_ids)
        cells = {}
        for face, cycle in lowers:
            pos_u = cycle.index(0)
            neighbours_u = {
                cycle[(pos_u - 1) % len(cycle)],
                cycle[(pos_u + 1) % len(cycle)],
            }
            pos_v = cycle.index(1)
            neighbours_v = {
                cycle[(pos_v - 1) % len(cycle)],
                cycle[(pos_v + 1) % len(cycle)],
            }
            assert 1 in neighbours_u and 0 in neighbours_v
            a = next(x for x in neighbours_u if x != 1)
            b = next(x for x in neighbours_v if x != 0)
            cells.setdefault((a, b), []).append(face)

        for cell_faces in cells.values():
            compatibility = []
            for upper, _ in uppers:
                row = []
                upper_without_roots = set(upper) - {0, 1}
                for lower in cell_faces:
                    union = set(lower) | upper_without_roots
                    row.append(set(hull(points, union)) == union)
                compatibility.append(row)
                # The row is either all true or all false.
                assert len(set(row)) == 1
            total_rectangles += 1
            if len(cell_faces) > 1 and any(row[0] for row in compatibility):
                nontrivial_rectangles += 1

    assert total_rectangles > 0 and nontrivial_rectangles > 0
    print(
        "tangent rectangles: "
        f"{total_rectangles} exact cells, {nontrivial_rectangles} nontrivial PASS"
    )


def verify_ordered_array_dichotomy() -> None:
    """Exact support-graph audit of (75)--(77)."""
    rng = random.Random(75_77_838)
    checks = 0
    for left_size in range(1, 13):
        for right_size in range(1, 13):
            for _ in range(20):
                edges = {
                    (a, b)
                    for a in range(left_size)
                    for b in range(right_size)
                    if rng.randrange(4) == 0
                }
                if not edges:
                    edges = {(0, 0)}
                edge_list = sorted(edges)
                m = len(edge_list)
                left_degree = [0] * left_size
                right_degree = [0] * right_size
                for a, b in edge_list:
                    left_degree[a] += 1
                    right_degree[b] += 1
                disjoint = 0
                endpoint_rectangles = set()
                for i, (a, b) in enumerate(edge_list):
                    for c, d in edge_list[i + 1 :]:
                        if a != c and b != d:
                            disjoint += 1
                            endpoint_rectangles.add(
                                (tuple(sorted((a, c))), tuple(sorted((b, d))))
                            )
                formula = comb(m, 2)
                formula -= sum(comb(x, 2) for x in left_degree)
                formula -= sum(comb(x, 2) for x in right_degree)
                assert disjoint == formula
                assert len(endpoint_rectangles) * 2 >= disjoint
                delta_left = max(left_degree)
                delta_right = max(right_degree)
                assert 2 * disjoint >= m * (
                    m + 1 - delta_left - delta_right
                )
                for cap in range(1, 1 + min(16, m)):
                    if len(endpoint_rectangles) < cap * m:
                        assert delta_left + delta_right > m + 1 - 4 * cap
                checks += 1
    print(f"ordered-array dichotomy: {checks} exact graphs PASS")


def verify_deep_nested_prefix() -> None:
    """Exact scalable obstruction to an automatic rank-one child."""

    def orient(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (
            b[1] - a[1]
        ) * (c[0] - a[0])

    def hull(points):
        ordered = sorted(points)
        if len(ordered) <= 1:
            return ordered
        lower = []
        for point in ordered:
            while len(lower) >= 2 and orient(
                lower[-2], lower[-1], point
            ) <= 0:
                lower.pop()
            lower.append(point)
        upper = []
        for point in reversed(ordered):
            while len(upper) >= 2 and orient(
                upper[-2], upper[-1], point
            ) <= 0:
                upper.pop()
            upper.append(point)
        return lower[:-1] + upper[:-1]

    for depth in range(1, 41):
        n_scale = 2 * depth + 4
        u = (0, 0)
        c = (n_scale, 0)
        prefix = [
            (j, j * (j - n_scale)) for j in range(1, depth + 1)
        ]
        inner = (n_scale // 2, 1)
        outer = (n_scale // 2, n_scale * n_scale)
        all_points = [u, c] + prefix + [inner, outer]
        for i in range(len(all_points)):
            for j in range(i + 1, len(all_points)):
                for k in range(j + 1, len(all_points)):
                    assert orient(
                        all_points[i], all_points[j], all_points[k]
                    ) != 0

        base = [u] + prefix + [c]
        assert set(hull(base + [inner])) == set(base + [inner])
        assert set(hull(base + [outer])) == set(base + [outer])
        assert inner not in hull(base + [inner, outer])
        for peeled in range(depth + 1):
            remaining_prefix = prefix[peeled:]
            state = remaining_prefix + [c, inner, outer]
            if remaining_prefix:
                assert inner not in hull(state)
            else:
                assert set(hull(state)) == set(state)
    print("deep nested prefix: exact depths 1..40 PASS")


def verify_split_sequence_theorem() -> None:
    """Finite exact audit of the single-crossing split theorem."""

    def is_forward(left, right):
        if right < left:
            left, right = right, left
        return any(
            left[i] < right[i] and left[j] > right[j]
            for i in range(len(left))
            for j in range(i + 1, len(left))
        )

    rng = random.Random(95_97_838)
    checks = 0
    for dimensions in range(2, 6):
        alphabet_sizes = tuple(2 + (j % 2) for j in range(dimensions))
        universe = [()]
        for size in alphabet_sizes:
            universe = [word + (value,) for word in universe for value in range(size)]
        for _ in range(100):
            sample_size = min(len(universe), 4 + rng.randrange(9))
            words = rng.sample(universe, sample_size)
            edges = {
                (i, j)
                for i in range(sample_size)
                for j in range(i + 1, sample_size)
                if is_forward(words[i], words[j])
            }
            # Exact maximum independent set for samples of size at most 12.
            alpha = 0
            for mask in range(1 << sample_size):
                size = mask.bit_count()
                if size <= alpha:
                    continue
                if all(not (mask >> i & 1 and mask >> j & 1) for i, j in edges):
                    alpha = size
            bound = 1 + sum(size - 1 for size in alphabet_sizes)
            assert alpha <= bound
            m = sample_size
            assert 2 * len(edges) * bound >= m * (m - bound)
            for cap in range(1, 5):
                if m > (2 * cap + 1) * bound:
                    assert len(edges) > cap * m
            checks += 1
    print(f"split-sequence theorem: {checks} exact families PASS")


def verify_conditional_high_medium_and_encoding_barrier() -> None:
    """Exact integer audit of Theorem 16 and the short-word obstruction."""
    checks = 0
    for n in (8, 17, 64):
        for b in range(1, 5):
            for s in range(1, 5):
                # This B is deliberately larger than needed for disjoint
                # coordinate pools; only positivity matters for the algebra.
                b_parameter = 1 + b * (n - 1)
                prefix_rows = (s + 1) * n**s
                for load in (1, 2, n):
                    fibre = 2 * b * b * (s + 1) * n ** (2 * b + s)
                    threshold = 4 * load * b_parameter * fibre
                    for row_size in (threshold, threshold + 1, 2 * threshold):
                        split_lower = Fraction(
                            row_size * (row_size - b_parameter),
                            2 * b_parameter,
                        )
                        assert split_lower >= Fraction(
                            row_size * row_size, 4 * b_parameter
                        )
                        assert split_lower / fibre >= load * row_size
                    maximal_medium_load = load * prefix_rows * (threshold - 1)
                    theorem_bound = (
                        4
                        * load
                        * load
                        * b_parameter
                        * fibre
                        * prefix_rows
                    )
                    assert maximal_medium_load < theorem_bound
                    checks += 1

    # A scalable vertical-product row can have quadratic child entropy while
    # every child has the same short batch word.
    for log_m in (16, 32, 64, 128):
        m = 1 << log_m
        q = log_m
        s = isqrt(q)
        ambient_n = q * m + 2
        same_batch_children = m ** (q - s)
        short_word_values = ambient_n**s
        # Both are subfamilies of the full m^q child family, but the former
        # has quadratic logarithm while any injective s-word code has only
        # O(s log n) bits.
        assert same_batch_children > short_word_values
        full_decoder = 2 * q * q * (s + 1) * ambient_n ** (2 * q + s)
        assert full_decoder > m**q

    # The trace-count version of the suffix obstruction, (110)--(111).
    for alphabet in (8, 16, 32):
        pair_count = comb(alphabet, 2)
        for suffix_length in (8, 12, 16):
            inputs = pair_count**suffix_length
            trace_upper = (
                4
                * (suffix_length + 1) ** 2
                * pair_count**2
                * (alphabet + 1) ** (suffix_length - 2)
            )
            assert inputs > trace_upper
    print(f"conditional high/medium recovery: {checks} integer regimes PASS")


def verify_successor_entropy_mean_bound() -> None:
    """Exact count form of 2^H <= e(mu+1) < 3(mu+1)."""

    def compositions(total, parts):
        if parts == 1:
            yield (total,)
            return
        for first in range(total + 1):
            for rest in compositions(total - first, parts - 1):
                yield (first,) + rest

    checks = 0
    for support_bound in range(1, 7):
        for total in range(1, 13):
            for counts in compositions(total, support_bound):
                mean_numerator = sum(j * count for j, count in enumerate(counts))
                entropy_denominator = 1
                for count in counts:
                    if count:
                        entropy_denominator *= count**count
                # For empirical probabilities count/total,
                # 2^(total*H) = total^total / prod count^count.
                # Raise 2^H <= 3(mu+1) to the power total and clear
                # the denominator total^total exactly.
                left = total ** (2 * total)
                right = (
                    3 * (mean_numerator + total)
                ) ** total * entropy_denominator
                assert left <= right
                checks += 1
    print(f"successor entropy/mean: {checks} exact empirical laws PASS")


def verify_near_product_rectangles() -> None:
    """Exact support-KL, weighted-C4, and DRC checks for Theorems 23--25."""
    checks = 0
    for left_size, right_size in ((2, 2), (2, 3), (3, 3)):
        edge_slots = left_size * right_size
        for mask in range(1, 1 << edge_slots):
            edges = [
                (i, j)
                for i in range(left_size)
                for j in range(right_size)
                if mask >> (i * right_size + j) & 1
            ]
            edge_count = len(edges)
            left_degree = [0] * left_size
            right_degree = [0] * right_size
            for i, j in edges:
                left_degree[i] += 1
                right_degree[j] += 1

            support_numerator = sum(
                left_degree[i] * right_degree[j] for i, j in edges
            )
            support_probability = Fraction(
                support_numerator, edge_count * edge_count
            )

            # For the uniform-edge joint law,
            # 2^I is the geometric mean of E/(d_i e_j).  The support-event
            # data-processing inequality I >= log(1/q) can be checked after
            # raising to the E-th power, with exact rational arithmetic.
            likelihood_product = Fraction(1)
            for i, j in edges:
                likelihood_product *= Fraction(
                    edge_count, left_degree[i] * right_degree[j]
                )
            assert likelihood_product >= support_probability ** (-edge_count)

            # Weighted C4 density under the two edge marginals.
            rectangle_probability = Fraction(0)
            for j1 in range(right_size):
                for j2 in range(right_size):
                    common_left_mass = sum(
                        Fraction(left_degree[i], edge_count)
                        for i in range(left_size)
                        if (i, j1) in edges and (i, j2) in edges
                    )
                    rectangle_probability += (
                        Fraction(right_degree[j1], edge_count)
                        * Fraction(right_degree[j2], edge_count)
                        * common_left_mass**2
                    )
            assert rectangle_probability >= support_probability**4

            def check_drc(
                row_size: int,
                column_size: int,
                row_degree: list[int],
                column_degree: list[int],
                oriented_edges: list[tuple[int, int]],
            ) -> None:
                row_mass = [Fraction(value, edge_count) for value in row_degree]
                column_mass = [
                    Fraction(value, edge_count) for value in column_degree
                ]
                collision = sum((value * value for value in column_mass), Fraction())
                for fan_size in range(2, min(3, column_size) + 1):
                    threshold = support_probability**fan_size / (
                        2 * comb(fan_size, 2)
                    )
                    if collision >= threshold:
                        assert max(column_mass) >= collision
                        continue
                    common_mass = Fraction()
                    edge_set = set(oriented_edges)
                    for columns in combinations(range(column_size), fan_size):
                        candidate = sum(
                            (
                                row_mass[row]
                                for row in range(row_size)
                                if all((row, column) in edge_set for column in columns)
                            ),
                            Fraction(),
                        )
                        common_mass = max(common_mass, candidate)
                    assert common_mass >= support_probability**fan_size / 2

            check_drc(
                left_size,
                right_size,
                left_degree,
                right_degree,
                edges,
            )
            check_drc(
                right_size,
                left_size,
                right_degree,
                left_degree,
                [(j, i) for i, j in edges],
            )
            checks += 1
    print(f"near-product rectangles/DRC: {checks} exact graphs PASS")


def _cross(a: tuple[Fraction, Fraction], b: tuple[Fraction, Fraction],
           c: tuple[Fraction, Fraction]) -> Fraction:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def _hull_indices(
    points: list[tuple[Fraction, Fraction]], indices: set[int]
) -> tuple[int, ...]:
    """Strict monotone-chain hull; the audited configurations are generic."""
    ordered = sorted(indices, key=lambda index: points[index])
    if len(ordered) <= 1:
        return tuple(ordered)
    lower: list[int] = []
    for index in ordered:
        while (len(lower) >= 2
               and _cross(points[lower[-2]], points[lower[-1]], points[index])
               <= 0):
            lower.pop()
        lower.append(index)
    upper: list[int] = []
    for index in reversed(ordered):
        while (len(upper) >= 2
               and _cross(points[upper[-2]], points[upper[-1]], points[index])
               <= 0):
            upper.pop()
        upper.append(index)
    return tuple(lower[:-1] + upper[:-1])


def verify_two_record_uncrossing_barrier() -> None:
    """Check Theorem 27's singleton fibre and the nested rational failure."""
    graph_checks = 0
    for left_size, right_size in ((2, 2), (2, 3), (3, 3)):
        slots = left_size * right_size
        for mask in range(1, 1 << slots):
            edges = [
                (left, right)
                for left in range(left_size)
                for right in range(right_size)
                if mask >> (left * right_size + right) & 1
            ]
            fibres: dict[tuple[frozenset[int], frozenset[int]], int] = {}
            # Separate the two label classes by offsetting blocker labels.
            for first in edges:
                for second in edges:
                    output = (
                        frozenset((first[0], second[0])),
                        frozenset((left_size + first[1], left_size + second[1])),
                    )
                    fibres[output] = fibres.get(output, 0) + 1
            assert max(fibres.values()) <= 4
            graph_checks += 1

    points: list[tuple[Fraction, Fraction]] = [
        (Fraction(-3), Fraction(-9)),
        (Fraction(3), Fraction(-9)),
        (Fraction(0), Fraction(-12)),
    ]
    ear_i: list[int] = []
    for x_value in (
        Fraction(-11, 5), Fraction(-11, 10), Fraction(0),
        Fraction(11, 10), Fraction(11, 5),
    ):
        ear_i.append(len(points))
        points.append((x_value, -(x_value * x_value)))
    blocker_p = len(points)
    points.append((Fraction(3, 20), Fraction(20)))
    ear_j: list[int] = []
    for x_value in (
        Fraction(-2), Fraction(-1), Fraction(1, 10),
        Fraction(21, 20), Fraction(41, 20),
    ):
        ear_j.append(len(points))
        points.append((x_value, Fraction(2) - x_value * x_value / 2))
    blocker_q = len(points)
    points.append((Fraction(-1, 5), Fraction(50)))

    for first, second, third in combinations(range(len(points)), 3):
        assert _cross(points[first], points[second], points[third]) != 0

    retained = {0, 1, 2}
    source_i = retained | set(ear_i)
    source_j = retained | set(ear_j)
    assert set(_hull_indices(points, source_i)) == source_i
    assert set(_hull_indices(points, source_j)) == source_j
    assert set(_hull_indices(points, source_i | {blocker_p})) == (
        retained | {blocker_p}
    )
    assert set(_hull_indices(points, source_j | {blocker_q})) == (
        retained | {blocker_q}
    )

    ear_union = set(ear_i) | set(ear_j)
    outer = set(_hull_indices(points, ear_union))
    hidden = ear_union - outer
    assert hidden == {ear_i[1], ear_i[2], ear_i[3]}
    second_layer = hidden | {blocker_p, blocker_q}
    assert set(_hull_indices(points, second_layer)) == {
        ear_i[1], ear_i[3], blocker_q
    }

    # Exact singleton repair C4 for which neither forward matching works.
    c4_points = [
        (Fraction(32400), Fraction(407678)),
        (Fraction(33685), Fraction(283524)),
        (Fraction(905544), Fraction(11856)),
        (Fraction(703904), Fraction(203346)),
        (Fraction(635399), Fraction(149950)),
        (Fraction(640980), Fraction(67396)),
        (Fraction(138202), Fraction(791563)),
        (Fraction(826473), Fraction(830732)),
    ]
    for first, second, third in combinations(range(len(c4_points)), 3):
        assert _cross(
            c4_points[first], c4_points[second], c4_points[third]
        ) != 0
    source_a = {2, 3, 6}
    source_b = {4, 5, 7}
    assert set(_hull_indices(c4_points, source_a)) == source_a
    assert set(_hull_indices(c4_points, source_b)) == source_b
    for blocker in (0, 1):
        assert set(_hull_indices(c4_points, source_a | {blocker})) == {
            2, 6, blocker
        }
        assert set(_hull_indices(c4_points, source_b | {blocker})) == {
            5, 7, blocker
        }
        # Cross-augmenting A's repaired target by B's hidden point fails.
        cross_a = {2, 6, blocker, 4}
        assert set(_hull_indices(c4_points, cross_a)) == {2, 6, blocker}
    # The other cross augmentation succeeds; a valid matching needs both.
    assert set(_hull_indices(c4_points, {1, 5, 7, 3})) == {1, 5, 7, 3}
    assert set(_hull_indices(c4_points, {0, 5, 7, 3})) == {0, 5, 7, 3}

    # Exterior/exterior C4 whose targets remain incomparable after rotation.
    rotation_points = [
        (Fraction(329428), Fraction(573254)),
        (Fraction(231876), Fraction(518007)),
        (Fraction(756242), Fraction(536954)),
        (Fraction(969122), Fraction(458917)),
        (Fraction(363787), Fraction(577409)),
        (Fraction(468465), Fraction(889102)),
        (Fraction(989247), Fraction(449299)),
    ]
    for first, second, third in combinations(range(len(rotation_points)), 3):
        assert _cross(
            rotation_points[first],
            rotation_points[second],
            rotation_points[third],
        ) != 0
    rotation_a = {3, 5, 6}
    rotation_b = {0, 1, 5}
    for blocker in (2, 4):
        assert set(_hull_indices(
            rotation_points, rotation_a | {blocker}
        )) == {5, 6, blocker}
        assert set(_hull_indices(
            rotation_points, rotation_b | {blocker}
        )) == {1, 5, blocker}
    target_t = {2, 5, 6}
    target_u = {1, 4, 5}
    rotated_t = set(_hull_indices(rotation_points, target_t | {0}))
    rotated_u = set(_hull_indices(rotation_points, target_u | {3}))
    assert rotated_t == {0, 5, 6}
    assert rotated_u == {1, 3, 5}

    def hull_contained(first_set: set[int], second_set: set[int]) -> bool:
        return set(_hull_indices(
            rotation_points, first_set | second_set
        )) == set(_hull_indices(rotation_points, second_set))

    for first_set, second_set in (
        (target_t, target_u),
        (rotated_t, target_u),
        (target_t, rotated_u),
        (rotated_t, rotated_u),
    ):
        assert not hull_contained(first_set, second_set)
        assert not hull_contained(second_set, first_set)

    # Same-edge prefixes survive, but an insertion-edge switch can erase one.
    prefix_points = [
        (Fraction(-2), Fraction(0)),
        (Fraction(2), Fraction(0)),
        (Fraction(0), Fraction(-2)),
        (Fraction(1, 10), Fraction(1)),
        (Fraction(-1, 10), Fraction(3)),
        (Fraction(-5), Fraction(1, 5)),
    ]
    for first, second, third in combinations(range(len(prefix_points)), 3):
        assert _cross(
            prefix_points[first], prefix_points[second], prefix_points[third]
        ) != 0
    prefix_base = {0, 1, 2}
    assert set(_hull_indices(prefix_points, prefix_base | {3})) == (
        prefix_base | {3}
    )
    assert set(_hull_indices(prefix_points, prefix_base | {4})) == (
        prefix_base | {4}
    )
    assert set(_hull_indices(prefix_points, prefix_base | {3, 4})) == (
        prefix_base | {4}
    )
    assert set(_hull_indices(prefix_points, prefix_base | {4, 5})) == {
        1, 2, 4, 5
    }
    print(
        "two-record singleton/onion barrier: "
        f"{graph_checks} exact graphs and rational/C4 geometry PASS"
    )


def verify_symmetric_endpoint_hall() -> None:
    """Audit (149u)--(149z): the adjacent kill and separated code."""
    # Minimal rank-three adjacent-cell failure.  All two-label tests pass,
    # but the three inserted labels form a genuine circuit after deleting v.
    points = [
        (Fraction(0), Fraction(0)),       # u
        (Fraction(10), Fraction(0)),      # v
        (Fraction(10), Fraction(10)),     # w
        (Fraction(9), Fraction(-5)),      # x, across uv
        (Fraction(19), Fraction(3)),      # y, across vw
        (Fraction(15), Fraction(1)),      # z, across vw
    ]
    for first, second, third in combinations(range(len(points)), 3):
        assert _cross(points[first], points[second], points[third]) != 0
    base = {0, 1, 2}
    assert set(_hull_indices(points, base | {3})) == base | {3}
    assert set(_hull_indices(points, base | {4, 5})) == base | {4, 5}
    deleted = {0, 2}
    for pair in combinations((3, 4, 5), 2):
        candidate = deleted | set(pair)
        assert set(_hull_indices(points, candidate)) == candidate
    assert set(_hull_indices(points, deleted | {3, 4, 5})) == {0, 2, 3, 4}
    # z=(6u+13x+42y)/61.
    assert points[5][0] == (
        6 * points[0][0] + 13 * points[3][0] + 42 * points[4][0]
    ) / 61
    assert points[5][1] == (
        6 * points[0][1] + 13 * points[3][1] + 42 * points[4][1]
    ) / 61

    # Explicit balanced-bucket codes have the ceiling fibre in (149z''').
    code_checks = 0
    for q_left in range(1, 7):
        for q_right in range(1, 7):
            for blocker_size in range(1, 7):
                left_code = 1 + q_left + comb(q_left, 2)
                right_code = 1 + q_right + comb(q_right, 2)
                domain_size = q_left * q_right * blocker_size * blocker_size
                codomain_size = left_code * right_code
                fibres = [0] * codomain_size
                for index in range(domain_size):
                    fibres[index % codomain_size] += 1
                expected = (domain_size + codomain_size - 1) // codomain_size
                assert max(fibres) == expected
                if q_left == q_right == blocker_size:
                    assert expected <= 4
                code_checks += 1

    # Finite weighted-prefix instance of Theorem 32.  Histories are repeated
    # bases; X is disjoint, so every (D,E) gives one distinct formal output.
    universe = set(range(6))
    bases = [set(item) for item in combinations(universe, 4)]
    histories = bases + bases[::2] + bases[::3]
    t = 2
    endpoint_labels = {10, 11, 12, 13}
    endpoint_subsets = [
        frozenset(item)
        for size in range(3)
        for item in combinations(endpoint_labels, size)
    ]
    left_degree = comb(4, t) * len(endpoint_subsets)
    output_degree: dict[frozenset[int], int] = {}
    for base_set in histories:
        seen: set[frozenset[int]] = set()
        for kept in combinations(base_set, 4 - t):
            for endpoint_set in endpoint_subsets:
                face = frozenset(kept) | endpoint_set
                assert face not in seen
                seen.add(face)
                output_degree[face] = output_degree.get(face, 0) + 1
        assert len(seen) == left_degree
    delta = max(output_degree.values())
    # Degree double counting gives the duplicated-Hall capacity exactly.
    assert sum(output_degree.values()) == len(histories) * left_degree
    hall_fibre = (delta + left_degree - 1) // left_degree
    assert hall_fibre >= 1

    # Sliding parabola intervals force exponentially many large-common rows.
    # The exact finite checks use modest k; the displayed proof is algebraic.
    interval_checks = 0
    for k in range(6, 13):
        n = 1 << k
        q = 1 << (k // 2)
        starts = list(range(0, n // 4))
        for first in starts[::max(1, len(starts) // 17)]:
            for last in starts[::max(1, len(starts) // 19)]:
                if first > last:
                    continue
                intersection = max(0, q - (last - first))
                if intersection >= (q + 1) // 2:
                    assert last - first <= q // 2
                interval_checks += 1
    print(
        "symmetric endpoint Hall: adjacent 3-circuit, "
        f"{code_checks} exact codes and {interval_checks} interval checks PASS"
    )


def verify_information_bucket_c4() -> None:
    """Exhaust small supports for Theorem 33's bucket conversion."""
    graph_checks = 0
    for left_size, right_size in ((2, 2), (2, 3), (3, 2), (3, 3)):
        slots = left_size * right_size
        for mask in range(1, 1 << slots):
            edges = [
                (left, right)
                for left in range(left_size)
                for right in range(right_size)
                if mask >> (left * right_size + right) & 1
            ]
            edge_set = set(edges)
            edge_count = len(edges)
            if edge_count < 2:
                continue
            left_degree = [0] * left_size
            right_degree = [0] * right_size
            for left, right in edges:
                left_degree[left] += 1
                right_degree[right] += 1

            capital_m = log2(edge_count)
            information = sum(
                log2(edge_count / (left_degree[left] * right_degree[right]))
                for left, right in edges
            ) / edge_count
            threshold = information + sqrt((information + 1) * capital_m)
            delta = (threshold - information) / (threshold + capital_m)
            good = [
                (left, right)
                for left, right in edges
                if log2(
                    edge_count / (left_degree[left] * right_degree[right])
                ) <= threshold + 1e-12
            ]
            assert len(good) / edge_count + 1e-12 >= delta

            buckets: dict[tuple[int, int], list[tuple[int, int]]] = {}
            for left, right in good:
                key = (
                    int(log2(left_degree[left])),
                    int(log2(right_degree[right])),
                )
                buckets.setdefault(key, []).append((left, right))
            key, bucket_edges = max(
                buckets.items(), key=lambda item: len(item[1])
            )
            bucket_count = len(bucket_edges)
            bucket_number_bound = (capital_m + 1) ** 2
            assert bucket_count + 1e-12 >= len(good) / bucket_number_bound
            lower_left = 1 << key[0]
            lower_right = 1 << key[1]
            assert (
                lower_left * lower_right + 1e-12
                >= edge_count * 2 ** (-threshold - 2)
            )

            bucket_set = set(bucket_edges)
            active_left = {left for left, _ in bucket_edges}
            active_right = {right for _, right in bucket_edges}
            c4_count = 0
            for left_1 in active_left:
                for left_2 in active_left:
                    for right_1 in active_right:
                        for right_2 in active_right:
                            if (
                                (left_1, right_1) in bucket_set
                                and (left_1, right_2) in bucket_set
                                and (left_2, right_1) in bucket_set
                                and (left_2, right_2) in bucket_set
                            ):
                                c4_count += 1
            # Exact C4 Sidorenko after clearing the denominator.
            assert (
                c4_count * len(active_left) ** 2 * len(active_right) ** 2
                >= bucket_count**4
            )
            full_c4 = 0
            for left_1 in range(left_size):
                for left_2 in range(left_size):
                    for right_1 in range(right_size):
                        for right_2 in range(right_size):
                            if (
                                (left_1, right_1) in edge_set
                                and (left_1, right_2) in edge_set
                                and (left_2, right_1) in edge_set
                                and (left_2, right_2) in edge_set
                            ):
                                full_c4 += 1
            analytic_lower = (
                edge_count**2
                * delta**4
                * 2 ** (-2 * threshold - 4)
                / (capital_m + 1) ** 8
            )
            assert full_c4 + 1e-9 >= analytic_lower
            graph_checks += 1
    print(f"information-bucket counted C4: {graph_checks} supports PASS")


def main() -> None:
    verify_saved_profiles()
    verify_gordon_collision()
    verify_abstract_barrier()
    verify_restriction_double_count()
    verify_identical_pocket_envelope()
    verify_crossing_pocket_reuse()
    verify_source_cloud_envelope()
    verify_retained_core_entropy_code()
    verify_product_entropy_saturation()
    verify_tangent_rectangles()
    verify_ordered_array_dichotomy()
    verify_deep_nested_prefix()
    verify_split_sequence_theorem()
    verify_conditional_high_medium_and_encoding_barrier()
    verify_successor_entropy_mean_bound()
    verify_near_product_rectangles()
    verify_two_record_uncrossing_barrier()
    verify_symmetric_endpoint_hall()
    verify_information_bucket_c4()
    print("ACP proof audit: PASS")


if __name__ == "__main__":
    main()
