#!/usr/bin/env python3
"""Exact audit of endpoint-span, entropy, and alignment localization.

The theorem itself is elementary and is stated/proved in REPORT.md.  This
script independently reconstructs the unit once-per-positive-root matrices
for two adversarial tests:

* the saved 58-wire reflection-order record with H>2; and
* the 36-point depth-two central Pascal composition T_(4,2)[T_(4,2)]; and
* the long-span restriction of the scalable alternating reflection family.

All matrix evaluations are exact.  Activity 1/2 uses one common dyadic
scale, and every coordinate comparison in the Pascal construction uses
Fraction.  The entropy diagnostics use logarithms only after the underlying
cell masses and rank moments have been reconstructed exactly.
"""

from __future__ import annotations

import json
import math
import random
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
N58_CERTIFICATE = (
    ROOT / "agent_cyclic_stem_hw" / "reflection_counter" / "certificate.json"
)

Root = tuple[int, int]
Word = tuple[int, ...]
Point = tuple[Q, Q]


def root_sequence(n: int, word: Word) -> tuple[Root, ...]:
    """Validate a reduced word for w_0 and return its complete root order."""
    wires = list(range(n))
    roots: list[Root] = []
    for generator in word:
        assert 0 <= generator < n - 1
        left, right = wires[generator : generator + 2]
        assert left < right
        roots.append((left, right))
        wires[generator], wires[generator + 1] = right, left
    assert len(word) == n * (n - 1) // 2
    assert wires == list(reversed(range(n)))
    assert set(roots) == set(combinations(range(n), 2))
    return tuple(roots)


def reflection_betweenness(n: int, roots: tuple[Root, ...]) -> None:
    position = {root: rank for rank, root in enumerate(roots)}
    for i, j, k in combinations(range(n), 3):
        a, b, c = position[i, j], position[i, k], position[j, k]
        assert a < b < c or c < b < a


def product_one(n: int, roots: tuple[Root, ...]) -> list[list[int]]:
    matrix = [[int(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        matrix[j] = [a + b for a, b in zip(matrix[j], matrix[i])]
    return matrix


def product_half_scaled(n: int, roots: tuple[Root, ...]) -> tuple[int, list[list[int]]]:
    """Return 2^n B(1/2), exactly as an integer matrix."""
    scale = 1 << n
    matrix = [[scale * int(i == j) for j in range(n)] for i in range(n)]
    for i, j in roots:
        # A path entering row i has at most i edges, so 2^n is ample.
        assert all(value % 2 == 0 for value in matrix[i])
        matrix[j] = [a + b // 2 for a, b in zip(matrix[j], matrix[i])]
    return scale, matrix


def product_half_dual_scaled(
    n: int, roots: tuple[Root, ...]
) -> tuple[int, list[list[int]], list[list[int]]]:
    """Return 2^n B(1/2) and 2^n B'(1/2), both integral."""
    scale = 1 << n
    values = [[scale * int(i == j) for j in range(n)] for i in range(n)]
    derivatives = [[0 for _ in range(n)] for _ in range(n)]
    for i, j in roots:
        assert all(value % 2 == 0 for value in values[i])
        assert all(value % 2 == 0 for value in derivatives[i])
        values[j] = [a + b // 2 for a, b in zip(values[j], values[i])]
        derivatives[j] = [
            a + b + c // 2
            for a, b, c in zip(derivatives[j], values[i], derivatives[i])
        ]
    return scale, values, derivatives


def short_half_mass_moment(
    n: int, roots: tuple[Root, ...], cutoff: int
) -> tuple[Q, Q]:
    """Exact off-diagonal mass and rank moment for spans at most cutoff."""
    scale, forward, d_forward = product_half_dual_scaled(n, roots)
    other_scale, backward, d_backward = product_half_dual_scaled(
        n, tuple(reversed(roots))
    )
    assert scale == other_scale
    denominator = scale * scale
    mass = Q(0)
    derivative = Q(0)
    for i, j in combinations(range(n), 2):
        if j - i > cutoff:
            continue
        mass += Q(forward[j][i] * backward[j][i], denominator)
        derivative += Q(
            d_forward[j][i] * backward[j][i]
            + forward[j][i] * d_backward[j][i],
            denominator,
        )
    return mass, Q(1, 2) * derivative


def half_span_entropy_audit(
    n: int, roots: tuple[Root, ...]
) -> dict[str, float]:
    """Numerically audit the exact entropy encoding using exact cell moments."""
    scale, forward, d_forward = product_half_dual_scaled(n, roots)
    _, backward, d_backward = product_half_dual_scaled(
        n, tuple(reversed(roots))
    )
    denominator = scale * scale
    mass = Q(0)
    moment = Q(0)
    moment_log_span = 0.0
    for i, j in combinations(range(n), 2):
        cell_mass = Q(forward[j][i] * backward[j][i], denominator)
        cell_moment = Q(1, 2) * Q(
            d_forward[j][i] * backward[j][i]
            + forward[j][i] * d_backward[j][i],
            denominator,
        )
        mass += cell_mass
        moment += cell_moment
        moment_log_span += float(cell_moment) * math.log2(j - i)
    mean = float(moment / mass)
    entropy = math.log2(float(mass)) + mean
    entropy_cap = (
        math.log2(n * (n - 1) // 2)
        + mean * math.log2(math.e)
        + moment_log_span / float(mass)
    )
    assert entropy <= entropy_cap + 1e-10
    return {
        "nontrivial_half_mean": mean,
        "entropy_bits": entropy,
        "entropy_cap_bits": entropy_cap,
        "size_biased_mean_log2_span": moment_log_span / float(moment),
    }


def endpoint_masses(
    n: int, roots: tuple[Root, ...], activity: Q
) -> tuple[list[Q], Q]:
    """Mass by endpoint span, excluding empty sets and singletons."""
    if activity == 1:
        forward = product_one(n, roots)
        backward = product_one(n, tuple(reversed(roots)))
        denominator = 1
    elif activity == Q(1, 2):
        scale, forward = product_half_scaled(n, roots)
        other_scale, backward = product_half_scaled(n, tuple(reversed(roots)))
        assert scale == other_scale
        denominator = scale * scale
    else:
        raise ValueError("audit only implements activities 1 and 1/2")

    by_span = [Q(0) for _ in range(n)]
    for i, j in combinations(range(n), 2):
        by_span[j - i] += Q(forward[j][i] * backward[j][i], denominator)
    total = Q(1) + n * activity + sum(by_span, Q(0))
    return by_span, total


def alignment_statistics(
    n: int, roots: tuple[Root, ...], activity: Q
) -> tuple[Q, Q, Q]:
    """Return off-diagonal pairing Q, and the separate A/B energies."""
    if activity == 1:
        forward = product_one(n, roots)
        backward = product_one(n, tuple(reversed(roots)))
        denominator = 1
    elif activity == Q(1, 2):
        scale, forward = product_half_scaled(n, roots)
        other_scale, backward = product_half_scaled(n, tuple(reversed(roots)))
        assert scale == other_scale
        denominator = scale * scale
    else:
        raise ValueError("audit only implements activities 1 and 1/2")
    pairing = sum(
        (Q(forward[j][i] * backward[j][i], denominator)
         for i, j in combinations(range(n), 2)),
        Q(0),
    )
    energy_forward = sum(
        (Q(forward[j][i] ** 2, denominator)
         for i, j in combinations(range(n), 2)),
        Q(0),
    )
    energy_backward = sum(
        (Q(backward[j][i] ** 2, denominator)
         for i, j in combinations(range(n), 2)),
        Q(0),
    )
    return pairing, energy_backward, energy_forward


def assert_hellinger_midpoint(
    n: int, roots: tuple[Root, ...], activity: Q
) -> None:
    """Check r_e^2=p_e q_e/kappa^2 for every endpoint, exactly."""
    if activity == 1:
        forward = product_one(n, roots)
        backward = product_one(n, tuple(reversed(roots)))
        scale = 1
    else:
        scale, forward = product_half_scaled(n, roots)
        _, backward = product_half_scaled(n, tuple(reversed(roots)))
    forward_values = [Q(forward[j][i], scale) for i, j in combinations(range(n), 2)]
    backward_values = [Q(backward[j][i], scale) for i, j in combinations(range(n), 2)]
    pairing = sum((a * b for a, b in zip(backward_values, forward_values)), Q(0))
    energy_a = sum((a * a for a in backward_values), Q(0))
    energy_b = sum((b * b for b in forward_values), Q(0))
    kappa_squared = pairing**2 / (energy_a * energy_b)
    for a, b in zip(backward_values, forward_values):
        midpoint = a * b / pairing
        p = a * a / energy_a
        q = b * b / energy_b
        assert midpoint**2 == p * q / kappa_squared


def one_sided_history_audit(n: int, roots: tuple[Root, ...]) -> dict[str, int]:
    """Check direct-only histories and their simultaneous root-record property."""
    position = {root: rank for rank, root in enumerate(roots)}
    forward_one = product_one(n, roots)
    backward_one = product_one(n, tuple(reversed(roots)))
    scale, forward_half = product_half_scaled(n, roots)
    _, backward_half = product_half_scaled(n, tuple(reversed(roots)))
    forward_direct = 0
    backward_direct = 0
    for i, j in combinations(range(n), 2):
        forward_two = sum(
            position[i, k] < position[k, j] for k in range(i + 1, j)
        )
        backward_two = (j - i - 1) - forward_two
        if forward_two == 0:
            assert forward_one[j][i] == 1
            assert forward_half[j][i] == scale // 2
            assert all(position[i, j] < position[i, k] for k in range(i + 1, j))
            assert all(position[k, j] < position[i, j] for k in range(i + 1, j))
            forward_direct += 1
        if backward_two == 0:
            assert backward_one[j][i] == 1
            assert backward_half[j][i] == scale // 2
            assert all(position[i, k] < position[i, j] for k in range(i + 1, j))
            assert all(position[i, j] < position[k, j] for k in range(i + 1, j))
            backward_direct += 1
    return {
        "forward_direct_only_cells": forward_direct,
        "backward_direct_only_cells": backward_direct,
    }


def binary_entropy(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def interval_face_totals(
    roots: tuple[Root, ...], left: int, right: int
) -> tuple[Q, Q]:
    """Return F_I(1/2),F_I(1) for the open endpoint interval I."""
    size = right - left - 1
    if size == 0:
        return Q(1), Q(1)
    inside = tuple(
        (i - left - 1, j - left - 1)
        for i, j in roots
        if left < i < j < right
    )
    _, half = endpoint_masses(size, inside, Q(1, 2))
    _, one = endpoint_masses(size, inside, Q(1))
    return half, one


def coupled_cell_audit(
    n: int, roots: tuple[Root, ...]
) -> dict[str, object]:
    """Audit the exact product-face/one-sided-trace cell dichotomy."""
    scale, forward, d_forward = product_half_dual_scaled(n, roots)
    _, backward, d_backward = product_half_dual_scaled(
        n, tuple(reversed(roots))
    )
    forward_one = product_one(n, roots)
    backward_one = product_one(n, tuple(reversed(roots)))
    direct_scaled = scale // 2
    denominator = scale * scale

    total_mass = Q(0)
    product_mass = Q(0)
    one_sided_mass = Q(0)
    one_sided_long_mass = Q(0)
    one_sided_cells = 0
    product_dominant_mass = Q(0)
    trace_capture_weight = 0.0
    trace_logloss_weight = 0.0
    trace_weight = 0.0
    full_capture_weight = 0.0
    full_logloss_weight = 0.0
    interval_cache: dict[tuple[int, int], tuple[Q, Q]] = {}

    for i, j in combinations(range(n), 2):
        forward_value = Q(forward[j][i], scale)
        backward_value = Q(backward[j][i], scale)
        forward_remainder = forward_value - Q(1, 2)
        backward_remainder = backward_value - Q(1, 2)
        cell_mass = forward_value * backward_value
        two_rich_mass = forward_remainder * backward_remainder
        assert cell_mass == (
            Q(1, 4)
            + Q(1, 2) * (forward_remainder + backward_remainder)
            + two_rich_mass
        )
        total_mass += cell_mass
        product_mass += two_rich_mass

        interior_half, interior_one = interval_cache.setdefault(
            (i, j), interval_face_totals(roots, i, j)
        )

        # The whole endpoint cell, divided by t^2, is a family of convex
        # traces on the open interval.  This is the universal cell Bellman
        # inequality, independent of the boundary-history split.
        full_trace_half = 4 * cell_mass
        assert full_trace_half <= interior_half
        assert forward_one[j][i] * backward_one[j][i] <= interior_one
        full_mean = (
            Q(1, 2) * Q(d_forward[j][i], scale) / forward_value
            + Q(1, 2) * Q(d_backward[j][i], scale) / backward_value
            - 2
        )
        width = j - i - 1
        assert 0 <= full_mean <= width
        full_entropy = math.log2(float(full_trace_half)) + float(full_mean)
        full_entropy_cap = width * binary_entropy(float(full_mean / width)) if width else 0.0
        assert full_entropy <= full_entropy_cap + 1e-10
        full_actual_dilation = Q(
            forward_one[j][i] * backward_one[j][i], 1
        ) / cell_mass
        assert float(full_actual_dilation) + 1e-10 >= 2 ** (2 + float(full_mean))
        full_capture = full_trace_half / interior_half
        full_weight = float(cell_mass)
        full_capture_weight += full_weight * float(full_capture)
        full_logloss_weight += full_weight * -math.log2(float(full_capture))

        # Deleting endpoints sends the two-non-direct subfamily injectively
        # into the convex faces of the open interval.
        assert 4 * two_rich_mass <= interior_half
        two_rich_one = (
            (forward_one[j][i] - 1) * (backward_one[j][i] - 1)
        )
        assert two_rich_one <= interior_one

        if cell_mass and two_rich_mass * 4 >= cell_mass:
            product_dominant_mass += cell_mass

        # At delta=1/4 the exact algebraic near-one-sided alternative is
        # theta<=delta => min(A/t,B/t)<=1.
        if 4 * two_rich_mass <= cell_mass:
            assert min(2 * forward_remainder, 2 * backward_remainder) <= 1

        forward_is_direct = forward[j][i] == direct_scaled
        backward_is_direct = backward[j][i] == direct_scaled
        if not (forward_is_direct or backward_is_direct):
            continue

        one_sided_cells += 1
        one_sided_mass += cell_mass
        if j - i >= 10:
            one_sided_long_mass += cell_mass
        if j - i == 1:
            assert forward_is_direct and backward_is_direct
            continue
        assert forward_is_direct != backward_is_direct
        if forward_is_direct:
            rich_value = backward_value
            rich_derivative = Q(d_backward[j][i], scale)
            rich_one = backward_one[j][i]
        else:
            rich_value = forward_value
            rich_derivative = Q(d_forward[j][i], scale)
            rich_one = forward_one[j][i]

        # C(t)=rich(t)/t is the 0--1 trace polynomial after deleting the
        # endpoints.  It is coefficientwise contained in the interior face
        # polynomial; the two evaluations below audit that injection.
        trace_half = 2 * rich_value
        assert trace_half <= interior_half
        assert rich_one <= interior_one
        trace_capture = trace_half / interior_half

        mean_edges = Q(1, 2) * rich_derivative / rich_value
        mean_interior = mean_edges - 1
        width = j - i - 1
        assert 0 <= mean_interior <= width
        entropy = math.log2(float(trace_half)) + float(mean_interior)
        entropy_cap = width * binary_entropy(float(mean_interior / width))
        assert entropy <= entropy_cap + 1e-10

        # Since G=t^2 C, Jensen gives G(1)/G(1/2)>=4*2^E|S|.
        actual_dilation = Q(4 * rich_one, 1) / trace_half
        jensen_dilation = 2 ** (2 + float(mean_interior))
        assert float(actual_dilation) + 1e-10 >= jensen_dilation

        weight = float(cell_mass)
        trace_weight += weight
        trace_capture_weight += weight * float(trace_capture)
        trace_logloss_weight += weight * -math.log2(float(trace_capture))

    assert total_mass == sum(
        (
            Q(forward[j][i] * backward[j][i], denominator)
            for i, j in combinations(range(n), 2)
        ),
        Q(0),
    )
    return {
        "one_sided_cells": one_sided_cells,
        "one_sided_half_mass_fraction": float(one_sided_mass / total_mass),
        "one_sided_span_at_least_10_fraction": float(
            one_sided_long_mass / total_mass
        ),
        "two_rich_product_fraction": float(product_mass / total_mass),
        "cells_with_product_fraction_at_least_quarter_mass_fraction": float(
            product_dominant_mass / total_mass
        ),
        "one_sided_trace_weighted_capture": trace_capture_weight / trace_weight,
        "one_sided_trace_weighted_log2_loss": trace_logloss_weight / trace_weight,
        "full_trace_weighted_capture": full_capture_weight / float(total_mass),
        "full_trace_weighted_log2_loss": full_logloss_weight / float(total_mass),
    }


def temporal_paths(
    n: int, roots: tuple[Root, ...]
) -> dict[Root, list[tuple[int, ...]]]:
    """Enumerate every increasing-time path, grouped by its endpoints."""
    paths: dict[Root, list[tuple[int, ...]]] = {
        (i, i): [(i,)] for i in range(n)
    }
    for middle, right in roots:
        for left in range(middle + 1):
            prefixes = paths.get((left, middle))
            if prefixes:
                paths.setdefault((left, right), []).extend(
                    prefix + (right,) for prefix in prefixes
                )
    return paths


def canonical_peeling_audit(
    n: int, roots: tuple[Root, ...]
) -> dict[str, object]:
    """Enumerate face chains and audit the exact capture-KL chain rule."""
    forward_paths = temporal_paths(n, roots)
    backward_paths = temporal_paths(n, tuple(reversed(roots)))
    scale, forward = product_half_scaled(n, roots)
    _, backward = product_half_scaled(n, tuple(reversed(roots)))
    denominator = scale * scale
    _, total_half = endpoint_masses(n, roots, Q(1, 2))
    _, total_one = endpoint_masses(n, roots, Q(1))

    whole_half: dict[tuple[int, int], Q] = {}
    interior_half: dict[tuple[int, int], Q] = {}
    capture: dict[tuple[int, int], Q] = {}
    capture_cost: dict[tuple[int, int], float] = {}
    for i, j in combinations(range(n), 2):
        cell = Q(forward[j][i] * backward[j][i], denominator)
        inside = interval_face_totals(roots, i, j)[0]
        lam = 4 * cell / inside
        assert 0 < lam <= 1
        whole_half[i, j] = cell
        interior_half[i, j] = inside
        capture[i, j] = lam
        capture_cost[i, j] = -math.log2(float(lam))

    enumerated_faces = 0
    enumerated_half_mass = Q(0)
    enumerated_rank_moment = Q(0)
    weighted_capture_loss = 0.0
    maximum_pointwise_entropy_margin = -math.inf

    for i, j in combinations(range(n), 2):
        seen: set[tuple[int, ...]] = set()
        for upper in forward_paths[i, j]:
            for lower in backward_paths[i, j]:
                assert set(upper[1:-1]).isdisjoint(lower[1:-1])
                face = tuple(sorted(set(upper + lower)))
                assert len(face) == len(upper) + len(lower) - 2
                assert face not in seen
                seen.add(face)
                enumerated_faces += 1
                rank = len(face)
                weight = Q(1, 1 << rank)
                enumerated_half_mass += weight
                enumerated_rank_moment += rank * weight

                product_capture = Q(1)
                reference_probability = Q(1)
                parent_total = total_half
                cumulative_loss = 0.0
                for depth in range(rank // 2):
                    edge = (face[depth], face[-1 - depth])
                    product_capture *= capture[edge]
                    cumulative_loss += capture_cost[edge]
                    reference_probability *= whole_half[edge] / parent_total
                    parent_total = interior_half[edge]
                if rank % 2:
                    reference_probability *= Q(1, 2) / parent_total
                else:
                    reference_probability /= parent_total

                face_probability = weight / total_half
                # The independent-interior Markov reference differs from
                # the true face probability by precisely the product of
                # the conditional capture probabilities along the chain.
                assert reference_probability == face_probability * product_capture
                weighted_capture_loss += float(weight) * cumulative_loss
                surprisal = -math.log2(float(face_probability))
                maximum_pointwise_entropy_margin = max(
                    maximum_pointwise_entropy_margin,
                    cumulative_loss - surprisal,
                )

        assert len(seen) == (
            len(forward_paths[i, j]) * len(backward_paths[i, j])
        )

    offdiagonal_half = total_half - 1 - Q(n, 2)
    assert enumerated_faces == total_one - 1 - n
    assert enumerated_half_mass == offdiagonal_half
    total_rank_moment = enumerated_rank_moment + Q(n, 2)
    mean_rank = total_rank_moment / total_half
    face_entropy = math.log2(float(total_half)) + float(mean_rank)
    expected_capture_loss = weighted_capture_loss / float(total_half)
    return {
        "enumerated_nontrivial_faces": enumerated_faces,
        "mean_face_rank": float(mean_rank),
        "face_entropy_bits": face_entropy,
        "expected_cumulative_capture_loss_bits": expected_capture_loss,
        "loss_over_face_entropy": expected_capture_loss / face_entropy,
        "maximum_cost_minus_face_surprisal_bits": maximum_pointwise_entropy_margin,
        "mean_one_step_radial_extension_degree": float(
            4 * offdiagonal_half / total_half
        ),
    }


def abstract_peeling_barrier() -> dict[str, object]:
    """Exact non-planar barrier to a purely hereditary pointwise proof.

    The complex contains every set of rank at most three, a full Boolean
    block W of size 19, and one four-set consisting of two nested endpoint
    pairs.  It is hereditary and has the universal triple property, but the
    product of the two capture probabilities is smaller than the true
    probability of that four-face.
    """
    block = 19
    n = block + 4

    def low_rank_mass(size: int) -> Q:
        return sum(
            (Q(math.comb(size, rank), 1 << rank) for rank in range(4)),
            Q(0),
        )

    boolean_block = Q(3, 2) ** block
    total = (
        low_rank_mass(n)
        + boolean_block
        - low_rank_mass(block)
        + Q(1, 16)
    )
    outer_interior = (
        low_rank_mass(block + 2)
        + boolean_block
        - low_rank_mass(block)
    )
    outer_link = Q(1) + Q(block + 2, 2) + Q(1, 4)
    inner_link = Q(1) + Q(block, 2)
    outer_capture = outer_link / outer_interior
    inner_capture = inner_link / boolean_block
    face_probability = Q(1, 16) / total
    capture_product = outer_capture * inner_capture
    assert capture_product < face_probability
    return {
        "n": n,
        "boolean_block_size": block,
        "capture_product": str(capture_product),
        "four_face_probability": str(face_probability),
        "cost_minus_surprisal_bits": math.log2(
            float(face_probability / capture_product)
        ),
    }


def reflection_class_representatives(n: int) -> dict[int, tuple[Root, ...]]:
    """Enumerate one reduced-word representative per packet-sign class."""
    wires = list(range(n))
    roots: list[Root] = []
    triples = tuple(combinations(range(n), 3))
    length = n * (n - 1) // 2
    representatives: dict[int, tuple[Root, ...]] = {}

    def recurse() -> None:
        if len(roots) == length:
            position = {root: rank for rank, root in enumerate(roots)}
            signature = 0
            for bit, (i, j, k) in enumerate(triples):
                if position[i, j] < position[j, k]:
                    signature |= 1 << bit
            representatives.setdefault(signature, tuple(roots))
            return
        for generator in range(n - 1):
            if wires[generator] < wires[generator + 1]:
                left, right = wires[generator : generator + 2]
                wires[generator], wires[generator + 1] = right, left
                roots.append((left, right))
                recurse()
                roots.pop()
                wires[generator], wires[generator + 1] = left, right

    recurse()
    return representatives


def finite_pointwise_capture_search() -> dict[str, object]:
    """Exhaust small reflection classes and sample larger planar orders."""
    class_counts: dict[int, int] = {}
    maximum_small_margin = -math.inf
    for n in range(3, 7):
        representatives = reflection_class_representatives(n)
        class_counts[n] = len(representatives)
        for roots in representatives.values():
            result = canonical_peeling_audit(n, roots)
            maximum_small_margin = max(
                maximum_small_margin,
                result["maximum_cost_minus_face_surprisal_bits"],
            )
    assert class_counts == {3: 2, 4: 8, 5: 62, 6: 908}
    assert maximum_small_margin < 0

    generator = random.Random(839)
    maximum_planar_margin = -math.inf
    samples = 100
    n = 14
    for _ in range(samples):
        heights = generator.sample(range(-10**9, 10**9), n)
        points = [(Q(i), Q(height)) for i, height in enumerate(heights)]
        result = canonical_peeling_audit(n, slope_roots(points))
        maximum_planar_margin = max(
            maximum_planar_margin,
            result["maximum_cost_minus_face_surprisal_bits"],
        )
    assert maximum_planar_margin < 0
    return {
        "reflection_class_counts": class_counts,
        "maximum_small_margin_bits": maximum_small_margin,
        "random_planar_samples": samples,
        "random_planar_n": n,
        "maximum_random_planar_margin_bits": maximum_planar_margin,
    }


def alternating_rich_value(distance: int, activity: Q) -> Q:
    return activity + activity * activity * sum(
        ((1 + activity) ** ((step - 1) // 2)
         for step in range(1, distance)),
        Q(0),
    )


def alternating_points(n: int) -> list[Point]:
    """Exact stretchable realization with chi(i,j,k)=(-1)^i."""
    multiplier = 4 * n + 1
    heights = [
        ((-1) ** i) * multiplier ** (n - i) for i in range(n - 2)
    ] + [0, 0]
    return [(Q(i), Q(y)) for i, y in enumerate(heights)]


def alternating_long_statistics(
    n: int, activity: Q, cutoff: int
) -> tuple[Q, Q, Q]:
    """Exact long-span Q,E_A,E_B for the stretchable alternating family."""
    pairing = Q(0)
    energy_a = Q(0)
    energy_b = Q(0)
    for i, j in combinations(range(n), 2):
        if j - i <= cutoff:
            continue
        rich = alternating_rich_value(j - i, activity)
        pairing += activity * rich
        if i % 2 == 0:
            energy_a += rich * rich
            energy_b += activity * activity
        else:
            energy_a += activity * activity
            energy_b += rich * rich
    return pairing, energy_a, energy_b


def alternating_long_barrier() -> list[dict[str, object]]:
    """Replay linear Renyi drift after deleting all O(log n) spans."""
    rows = []
    for n in (20, 40, 80, 160):
        cutoff = math.ceil(2 * math.log2(n))
        half = alternating_long_statistics(n, Q(1, 2), cutoff)
        one = alternating_long_statistics(n, Q(1), cutoff)
        q_half, ea_half, eb_half = half
        q_one, ea_one, eb_one = one
        kappa_half_squared = q_half**2 / (ea_half * eb_half)
        kappa_one_squared = q_one**2 / (ea_one * eb_one)
        angular_ratio_squared = kappa_one_squared / kappa_half_squared
        # The report proves this scaled quantity converges to a positive
        # constant.  These broad rational bounds are only a finite replay.
        scaled = angular_ratio_squared * Q(4, 3) ** n
        assert Q(1, 10) < scaled < Q(10)
        rows.append(
            {
                "n": n,
                "cutoff": cutoff,
                "scaled_kappa_ratio_squared": str(scaled),
                "renyi_drift_bits": -math.log2(float(angular_ratio_squared)),
                "renyi_drift_per_n": -math.log2(float(angular_ratio_squared)) / n,
            }
        )
    return rows


def orient(a: Point, b: Point, c: Point) -> Q:
    return ((b[0] - a[0]) * (c[1] - a[1])
            - (b[1] - a[1]) * (c[0] - a[0]))


def strong_glue(left: list[Point], right: list[Point], epsilon: Q) -> list[Point]:
    return [
        (epsilon * epsilon * x, epsilon * y) for x, y in left
    ] + [
        (1 + epsilon * epsilon * x, 1 + epsilon * y) for x, y in right
    ]


def pascal_cell(m: int, i: int, epsilon: Q) -> list[Point]:
    if i in (0, m):
        return [(Q(0), Q(0))]
    return strong_glue(
        pascal_cell(m - 1, i - 1, epsilon),
        pascal_cell(m - 1, i, epsilon),
        epsilon,
    )


def slope_roots(raw_points: list[Point]) -> tuple[Root, ...]:
    points = sorted(raw_points)
    for i, j, k in combinations(range(len(points)), 3):
        assert orient(points[i], points[j], points[k]) != 0
    slopes = sorted(
        (
            (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]),
            i,
            j,
        )
        for i, j in combinations(range(len(points)), 2)
    )
    # Equal slopes on disjoint edges are harmless commuting factors.
    for left, right in zip(slopes, slopes[1:]):
        if left[0] == right[0]:
            assert len({left[1], left[2], right[1], right[2]}) == 4
    return tuple((i, j) for _, i, j in slopes)


def pascal_composition() -> list[Point]:
    base = sorted(pascal_cell(4, 2, Q(1, 97)))
    epsilon = Q(1, 16384)
    return sorted(
        (
            outer_x + epsilon * epsilon * inner_x,
            outer_y + epsilon * inner_y,
        )
        for outer_x, outer_y in base
        for inner_x, inner_y in base
    )


def short_span_bound(n: int, cutoff: int) -> Q:
    """The convenient closed upper bound 1+n/2*(3/2)^D."""
    return Q(1) + Q(n, 2) * Q(3, 2) ** cutoff


def exact_short_span_cap(n: int, cutoff: int) -> Q:
    return Q(1) + Q(n, 2) + Q(1, 4) * sum(
        ((n - distance) * Q(3, 2) ** (distance - 1)
         for distance in range(1, cutoff + 1)),
        Q(0),
    )


def audit(name: str, n: int, roots: tuple[Root, ...], expected_half: Q, expected_one: Q) -> dict[str, object]:
    assert len(roots) == n * (n - 1) // 2
    assert set(roots) == set(combinations(range(n), 2))
    reflection_betweenness(n, roots)

    half_by_span, half = endpoint_masses(n, roots, Q(1, 2))
    one_by_span, one = endpoint_masses(n, roots, Q(1))
    assert half == expected_half
    assert one == expected_one

    q_half, ea_half, eb_half = alignment_statistics(n, roots, Q(1, 2))
    q_one, ea_one, eb_one = alignment_statistics(n, roots, Q(1))
    assert q_half == half - 1 - Q(n, 2)
    assert q_one == one - 1 - n
    kappa_half_squared = q_half**2 / (ea_half * eb_half)
    kappa_one_squared = q_one**2 / (ea_one * eb_one)
    # Exact Hellinger/Renyi decomposition of the cross-activity ratio.
    assert (q_one / q_half) ** 2 == (
        (ea_one * eb_one) / (ea_half * eb_half)
        * kappa_one_squared / kappa_half_squared
    )
    assert_hellinger_midpoint(n, roots, Q(1, 2))
    assert_hellinger_midpoint(n, roots, Q(1))
    span_entropy = half_span_entropy_audit(n, roots)
    one_sided = one_sided_history_audit(n, roots)
    coupled_cells = coupled_cell_audit(n, roots)
    peeling = canonical_peeling_audit(n, roots)

    # The coefficientwise endpoint-cell theorem specialized at 1/2.
    for distance in range(1, n):
        aggregate_cap = Q(n - distance, 4) * Q(3, 2) ** (distance - 1)
        assert half_by_span[distance] <= aggregate_cap

    logarithm = math.log2(n)
    quadratic_threshold = math.floor(
        logarithm * logarithm / (4 * math.log2(1.5))
    )
    cutoffs = sorted({
        1,
        min(n - 1, int(logarithm)),
        min(n - 1, 2 * int(logarithm)),
        min(n - 1, quadratic_threshold),
    })
    rows = []
    for cutoff in cutoffs:
        observed = Q(1) + Q(n, 2) + sum(half_by_span[1 : cutoff + 1], Q(0))
        exact_cap = exact_short_span_cap(n, cutoff)
        closed_cap = short_span_bound(n, cutoff)
        assert observed <= exact_cap <= closed_cap
        restricted_mass, restricted_moment = short_half_mass_moment(
            n, roots, cutoff
        )
        assert restricted_mass == sum(half_by_span[1 : cutoff + 1], Q(0))
        restricted_mean = restricted_moment / restricted_mass
        # Entropy identity plus the endpoint/subset encoding from the report.
        entropy = math.log2(float(restricted_mass)) + float(restricted_mean)
        entropy_cap = (
            math.log2(n * cutoff)
            + float(restricted_mean) * math.log2(math.e * max(1, cutoff))
        )
        assert entropy <= entropy_cap + 1e-10
        rows.append(
            {
                "cutoff": cutoff,
                "observed_short_half_mass": str(observed),
                "observed_fraction": float(observed / half),
                "exact_cap": str(exact_cap),
                "closed_cap": str(closed_cap),
                "restricted_mean": float(restricted_mean),
                "entropy_bits": entropy,
                "entropy_cap_bits": entropy_cap,
            }
        )
    return {
        "name": name,
        "n": n,
        "F_half": str(half),
        "F_one": str(one),
        "H": str(Q(n) * half / one),
        "alignment": {
            "kappa_half_squared": str(kappa_half_squared),
            "kappa_one_squared": str(kappa_one_squared),
            "renyi_half_bits": -math.log2(float(kappa_half_squared)),
            "renyi_one_bits": -math.log2(float(kappa_one_squared)),
            "energy_dilation_bits": 0.5 * math.log2(
                float(ea_one * eb_one / (ea_half * eb_half))
            ),
            "renyi_drift_cost_bits": 0.5 * (
                -math.log2(float(kappa_one_squared))
                + math.log2(float(kappa_half_squared))
            ),
            "offdiagonal_dilation_bits": math.log2(float(q_one / q_half)),
        },
        "span_entropy": span_entropy,
        "one_sided_history": one_sided,
        "coupled_cells": coupled_cells,
        "canonical_peeling": peeling,
        "rows": rows,
        "one_mass_checksum": str(Q(1) + n + sum(one_by_span, Q(0))),
    }


def main() -> None:
    saved = json.loads(N58_CERTIFICATE.read_text())["finite_braid_record"]
    n58_roots = root_sequence(saved["n"], tuple(saved["word_zero_based"]))
    n58 = audit(
        "saved unit reflection order n=58",
        saved["n"],
        n58_roots,
        Q(saved["F_half"]),
        Q(saved["F_one"]),
    )

    points = pascal_composition()
    assert len(points) == 36
    pascal_roots = slope_roots(points)
    pascal = audit(
        "central Pascal composition T_(4,2)[T_(4,2)]",
        36,
        pascal_roots,
        # These exact values are independently reconstructed by the matrices.
        Q(80351, 8),
        Q(441400),
    )
    alternating = alternating_long_barrier()
    alternating_peeling = canonical_peeling_audit(
        30, slope_roots(alternating_points(30))
    )
    abstract_barrier = abstract_peeling_barrier()
    finite_search = finite_pointwise_capture_search()

    print("endpoint-span localization audit: PASS")
    for record in (n58, pascal):
        print(
            record["name"],
            "H=", record["H"],
            "F(1/2)=", record["F_half"],
            "F(1)=", record["F_one"],
        )
        alignment = record["alignment"]
        print(
            "  energy dilation bits=", f'{alignment["energy_dilation_bits"]:.6f}',
            "Renyi drift cost=", f'{alignment["renyi_drift_cost_bits"]:.6f}',
            "net offdiag dilation=", f'{alignment["offdiagonal_dilation_bits"]:.6f}',
        )
        print(
            "  size-biased mean log2(span)=",
            f'{record["span_entropy"]["size_biased_mean_log2_span"]:.6f}',
        )
        cells = record["coupled_cells"]
        print(
            "  one-sided mass=",
            f'{cells["one_sided_half_mass_fraction"]:.6f}',
            "two-rich product mass=",
            f'{cells["two_rich_product_fraction"]:.6f}',
            "one-sided trace capture=",
            f'{cells["one_sided_trace_weighted_capture"]:.6f}',
            "full trace capture=",
            f'{cells["full_trace_weighted_capture"]:.6f}',
        )
        peeling = record["canonical_peeling"]
        print(
            "  canonical peeling KL bits=",
            f'{peeling["expected_cumulative_capture_loss_bits"]:.6f}',
            "face entropy bits=",
            f'{peeling["face_entropy_bits"]:.6f}',
            "mean extension degree=",
            f'{peeling["mean_one_step_radial_extension_degree"]:.6f}',
        )
        for row in record["rows"]:
            print(
                "  D=", row["cutoff"],
                "observed short fraction=", f'{row["observed_fraction"]:.6f}',
                "cap=", row["closed_cap"],
            )
    last = alternating[-1]
    print(
        "alternating long-span barrier: n=", last["n"],
        "D=", last["cutoff"],
        "Renyi drift/n=", f'{last["renyi_drift_per_n"]:.6f}',
        "PASS",
    )
    print(
        "alternating canonical peeling: n=30 KL bits=",
        f'{alternating_peeling["expected_cumulative_capture_loss_bits"]:.6f}',
        "face entropy bits=",
        f'{alternating_peeling["face_entropy_bits"]:.6f}',
        "PASS",
    )
    print(
        "abstract hereditary peeling barrier: n=",
        abstract_barrier["n"],
        "cost-surprisal bits=",
        f'{abstract_barrier["cost_minus_surprisal_bits"]:.6f}',
        "PASS",
    )
    print(
        "pointwise planar/reflection search: classes through n=6=",
        finite_search["reflection_class_counts"][6],
        "random n=14 samples=",
        finite_search["random_planar_samples"],
        "PASS",
    )


if __name__ == "__main__":
    main()
