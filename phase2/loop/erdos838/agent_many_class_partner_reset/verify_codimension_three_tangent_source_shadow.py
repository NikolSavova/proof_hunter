#!/usr/bin/env python3
"""Exact audit of codimension-three source shadows in the tangent reset.

The script checks, using Fraction arithmetic only, that

* an almost-full word from each of three original 2m-cell classes is never
  ordinary (m >= 2);
* the canonical source thinning L_i, L_j, (L_k union R_k) is a cup for every
  ordered class triple in a range of exact tangent constructions;
* both statements survive the arbitrary-child substitution in the companion
  verifier; and
* the complete-product incidence, output, and history-load formulas are exact.

The finite parameter sweep is a regression check.  The uniform coordinate
proof is in CODIMENSION_THREE_TANGENT_SOURCE_SHADOW_AUDIT.md.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from pathlib import Path
import runpy


HERE = Path(__file__).resolve().parent
RESET = runpy.run_path(str(HERE / "verify_scalable_partner_reset.py"))
SUBSTITUTION = runpy.run_path(
    str(HERE / "verify_low_face_substitution_profile.py")
)

orient = RESET["orient"]
is_convex = RESET["is_convex"]
class_labels = RESET["class_labels"]


def cup(points, labels) -> bool:
    """Every ordered triple is positive; labels use distinct macro cells."""
    ordered = sorted(labels, key=lambda label: points[label][0])
    return all(orient(points[a], points[b], points[c]) > 0
               for a, b, c in combinations(ordered, 3))


def canonical_cells(i: int, j: int, k: int, m: int):
    assert i < j < k
    return ([(i, "L", a) for a in range(m)]
            + [(j, "L", a) for a in range(m)]
            + [(k, side, a) for side in ("L", "R") for a in range(m)])


def mixed_pair_obstruction(t: int, m: int, points) -> int:
    """Every lower mixed-side pair plus every higher pair is a bad circuit."""
    checks = 0
    for i, j in combinations(range(t), 2):
        for a, b in product(range(m), repeat=2):
            lower = ((i, "L", a), (i, "R", b))
            for higher in combinations(class_labels(t, m, j), 2):
                assert not is_convex([points[z] for z in lower + higher])
                checks += 1
    return checks


def almost_full_zero_audit(t: int, m: int, points) -> int:
    """All three-class codimension-(1,1,1) full-word supports are bad."""
    assert m >= 2
    checks = 0
    for i, j, k in combinations(range(t), 3):
        words = [class_labels(t, m, cls) for cls in (i, j, k)]
        for oi, oj, ok in product(*(range(2 * m) for _ in range(3))):
            support = ([z for r, z in enumerate(words[0]) if r != oi]
                       + [z for r, z in enumerate(words[1]) if r != oj]
                       + [z for r, z in enumerate(words[2]) if r != ok])
            # Exhibit the hereditary four-point obstruction instead of
            # recomputing the hull of the whole almost-full support.
            lower_l = next(z for z in support if z[0] == i and z[1] == "L")
            lower_r = next(z for z in support if z[0] == i and z[1] == "R")
            higher = [z for z in support if z[0] == j][:2]
            witness = [lower_l, lower_r] + higher
            assert len(set(witness)) == 4
            assert not is_convex([points[z] for z in witness])
            checks += 1
    return checks


def macro_sweep() -> dict[str, int]:
    cup_checks = all_lower_checks = mixed_checks = zero_checks = 0
    constructions = 0
    for t in range(3, 9):
        m = max(2, t - 1)
        points, _delta, _halvings = RESET["construct"](t, m)
        constructions += 1
        mixed_checks += mixed_pair_obstruction(t, m, points)
        zero_checks += almost_full_zero_audit(t, m, points)
        for i, j, k in combinations(range(t), 3):
            cells = canonical_cells(i, j, k, m)
            assert len(cells) == 4 * m
            assert cup(points, cells)
            cup_checks += comb(4 * m, 3)
        all_lower = ([(i, "L", a)
                      for i in range(t - 1) for a in range(m)]
                     + class_labels(t, m, t - 1))
        assert len(all_lower) == m * (t + 1)
        assert cup(points, all_lower)
        all_lower_checks += comb(m * (t + 1), 3)
    return {
        "exact_macro_constructions": constructions,
        "canonical_cup_triples": cup_checks,
        "all_lower_plus_top_cup_triples": all_lower_checks,
        "mixed_pair_bad_circuits": mixed_checks,
        "almost_full_bad_supports": zero_checks,
    }


def physical_substitution_audit() -> dict[str, object]:
    """Check the cup and obstruction through genuinely nonconvex children."""
    t, m = 3, 2
    _macro, points, _seeds, _delta, epsilon, _halvings = (
        SUBSTITUTION["substituted_points"](t, m)
    )
    cells = canonical_cells(0, 1, 2, m)

    # It is enough to test triples: a physical source word uses at most one
    # point in each macro cell.  Every possible child-label transversal of
    # every three-cell subword has positive orientation.
    cup_triples = 0
    for a, b, c in combinations(cells, 3):
        for ra, rb, rc in product(range(4), repeat=3):
            labels = ((a, ra), (b, rb), (c, rc))
            ordered = sorted(labels, key=lambda z: points[z][0])
            assert orient(*(points[z] for z in ordered)) > 0
            cup_triples += 1

    bad_circuits = 0
    for i, j in combinations(range(t), 2):
        for a, b in product(range(m), repeat=2):
            lower_cells = ((i, "L", a), (i, "R", b))
            for higher_cells in combinations(class_labels(t, m, j), 2):
                four_cells = lower_cells + higher_cells
                for ranks in product(range(4), repeat=4):
                    labels = tuple((cell, rank)
                                   for cell, rank in zip(four_cells, ranks))
                    assert not is_convex([points[z] for z in labels])
                    bad_circuits += 1

    profile = SUBSTITUTION["class_recurrence_audit"](t, m, points)
    ramp = SUBSTITUTION["max_plus_ramp_audit"]()
    return {
        "physical_points": len(points),
        "micro_epsilon": epsilon,
        "physical_canonical_cup_triples": cup_triples,
        "physical_mixed_pair_bad_circuits": bad_circuits,
        "heterogeneous_class_profile": profile["class_direct_(C,U,W)"],
        **ramp,
    }


def encode_output(values, omitted, lengths):
    """Occupancy mask plus all retained role values; roles are coloured."""
    out = []
    start = 0
    for colour, (length, missing) in enumerate(zip(lengths, omitted)):
        for role in range(length):
            if role != missing:
                out.append((colour, role, values[start + role]))
        start += length
    return tuple(out)


def complete_product_audit(m: int = 2, d: int = 3,
                           t: int = 3) -> dict[str, int]:
    """Exhaust the thinned cubic shadow and check both decoder loads."""
    assert t >= 3 and m >= t - 1
    lengths = (m, m, 2 * m)
    roles = sum(lengths)
    outputs: Counter[tuple] = Counter()
    records = d ** roles
    omission_triples = lengths[0] * lengths[1] * lengths[2]

    for values in product(range(d), repeat=roles):
        for omitted in product(*(range(length) for length in lengths)):
            outputs[encode_output(values, omitted, lengths)] += 1

    incidences = records * omission_triples
    distinct = omission_triples * d ** (roles - 3)
    assert sum(outputs.values()) == incidences
    assert len(outputs) == distinct
    assert set(outputs.values()) == {d ** 3}

    # Relative to the original three full 2m-role histories, the two erased
    # lower R-halves contribute D^(2m) additional completions.
    full_records = d ** (6 * m)
    original_history_load = d ** (2 * m) * d ** 3
    assert full_records * omission_triples == distinct * original_history_load
    assert records == d ** (4 * m)

    return {
        "alphabet": d,
        "thin_records": records,
        "omission_incidences": incidences,
        "distinct_cubic_outputs": distinct,
        "thin_decoder_load": d ** 3,
        "original_full_histories": full_records,
        "original_history_load": original_history_load,
        "canonical_full_word_faces": records,
        "disjoint_t_class_bank": comb(t, 3) * records,
        "all_lower_plus_top_bank": d ** (m * (t + 1)),
    }


def main() -> None:
    macro = macro_sweep()
    physical = physical_substitution_audit()
    counting = complete_product_audit()
    print("PASS")
    print(f"  macro: {macro}")
    print(f"  arbitrary-child/ramp: {physical}")
    print(f"  source-shadow counts: {counting}")


if __name__ == "__main__":
    main()
