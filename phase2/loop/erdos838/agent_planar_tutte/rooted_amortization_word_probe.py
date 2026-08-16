#!/usr/bin/env python3
"""Exact rooted-amortization audit on type-A reflection orders."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
GATE = ROOT / "agent_reflection_gate"
sys.path.insert(0, str(GATE))
import reflection_order_gate as gate  # noqa: E402


def chirotope_table(n, word):
    positions = {root: i for i, root in enumerate(gate.root_sequence(n, word))}
    table = {}
    for a, b, c in itertools.combinations(range(n), 3):
        table[(a, b, c)] = 1 if positions[(a, b)] < positions[(a, c)] < positions[(b, c)] else -1
    return table


def chi(table, a, b, c):
    values = [a, b, c]
    inversions = sum(values[i] > values[j] for i in range(3) for j in range(i + 1, 3))
    key = tuple(sorted(values))
    return table[key] * (-1 if inversions & 1 else 1)


def forbidden_circuits(n, table):
    out = []
    for four in itertools.combinations(range(n), 4):
        nonconvex = False
        for root in four:
            tri = [x for x in four if x != root]
            tri_sign = chi(table, *tri)
            side = [chi(table, tri[i], tri[(i + 1) % 3], root) for i in range(3)]
            if all(value * tri_sign > 0 for value in side):
                nonconvex = True
                break
        if nonconvex:
            out.append(sum(1 << x for x in four))
    return out


def face_table(n, table):
    bad = bytearray(1 << n)
    for circuit in forbidden_circuits(n, table):
        bad[circuit] = 1
    for bit in range(n):
        step = 1 << bit
        for base in range(0, 1 << n, step << 1):
            for offset in range(step):
                if bad[base + offset]:
                    bad[base + step + offset] = 1
    return bytearray(1 - value for value in bad)


def hull_vertices(n, table):
    hull = []
    for e in range(n):
        is_hull = False
        for q in range(n):
            if q == e:
                continue
            sides = {chi(table, e, q, x) for x in range(n) if x not in (e, q)}
            if len(sides) <= 1:
                is_hull = True
                break
        if is_hull:
            hull.append(e)
    return hull


def audit_word(n, word):
    table = chirotope_table(n, tuple(word))
    faces = face_table(n, table)
    hull = hull_vertices(n, table)
    records = []
    for e in hull:
        absent_scaled = 0
        link_scaled = 0
        link_count = 0
        for mask, good in enumerate(faces):
            if not good:
                continue
            if mask >> e & 1:
                link_scaled += 1 << (n - mask.bit_count() + 1)
                link_count += 1
            else:
                absent_scaled += 1 << (n - mask.bit_count())
        lhs = 2 * absent_scaled + n * link_scaled
        rhs = 4 * link_count * (1 << n)
        records.append((lhs <= rhs, lhs, rhs, e, link_count))
    return records, sum(faces)


def scaled_half(profile, n):
    # Profiles from Gate A omit the empty face.
    return (1 << n) + sum(coefficient << (n - degree) for degree, coefficient in enumerate(profile))


def delete_root_sequence(roots, deleted, n):
    keep = [i for i in range(n) if i != deleted]
    relabel = {old: new for new, old in enumerate(keep)}
    return tuple(
        (relabel[a], relabel[b])
        for a, b in roots
        if a != deleted and b != deleted
    )


def restrict_root_sequence(roots, deleted_set, n):
    keep = [i for i in range(n) if i not in deleted_set]
    relabel = {old: new for new, old in enumerate(keep)}
    return tuple(
        (relabel[a], relabel[b])
        for a, b in roots
        if a not in deleted_set and b not in deleted_set
    )


def audit_word_fast(n, word):
    roots = gate.root_sequence(n, tuple(word))
    table = chirotope_table(n, tuple(word))
    hull = hull_vertices(n, table)
    parent = gate.evaluate_roots(n, roots, graded=True)
    parent_profile = parent.graded
    assert parent_profile is not None
    parent_v = 1 + sum(parent_profile)
    parent_w_scaled = scaled_half(parent_profile, n)
    records = []
    for e in hull:
        child_roots = delete_root_sequence(roots, e, n)
        child = gate.evaluate_roots(n - 1, child_roots, graded=True)
        child_profile = child.graded
        assert child_profile is not None
        absent_v = 1 + sum(child_profile)
        absent_w_scaled = 2 * scaled_half(child_profile, n - 1)
        link_count = parent_v - absent_v
        link_scaled = 2 * (parent_w_scaled - absent_w_scaled)
        lhs = 2 * absent_w_scaled + n * link_scaled
        rhs = 4 * link_count * (1 << n)
        records.append((lhs <= rhs, lhs, rhs, e, link_count))
    return records, parent_v


def audit_onion_fast(n, word):
    roots = gate.root_sequence(n, tuple(word))
    table = chirotope_table(n, tuple(word))
    hull = hull_vertices(n, table)
    h = len(hull)
    parent = gate.evaluate_roots(n, roots, graded=True)
    assert parent.graded is not None
    parent_v = 1 + sum(parent.graded)
    parent_w_scaled = scaled_half(parent.graded, n)
    interior_roots = restrict_root_sequence(roots, set(hull), n)
    m = n - h
    if m:
        interior = gate.evaluate_roots(m, interior_roots, graded=True)
        assert interior.graded is not None
        interior_v = 1 + sum(interior.graded)
        interior_w_scaled = (1 << h) * scaled_half(interior.graded, m)
    else:
        interior_v = 1
        interior_w_scaled = 1 << n
    lhs = h * interior_w_scaled + n * (parent_w_scaled - interior_w_scaled)
    rhs = 2 * (parent_v - interior_v) * (1 << n)
    return lhs <= rhs, lhs, rhs, parent_v, interior_v, h


def saved_words():
    paths = [
        GATE / "classes_n7.json",
        GATE / "heuristic_trace_n16.json",
        GATE / "heuristic_trace_n20.json",
        ROOT / "agent_coxeter_half_weight" / "planar_seed_n20.json",
        ROOT / "agent_coxeter_half_weight" / "seeded_n20.json",
        ROOT / "agent_coxeter_half_weight" / "planar_seed_n24.json",
        ROOT / "agent_coxeter_half_weight" / "seeded_n24.json",
        ROOT / "agent_coxeter_half_weight" / "planar_seed_n30.json",
        ROOT / "agent_coxeter_half_weight" / "seeded_n30.json",
    ]
    for path in paths:
        data = json.loads(path.read_text())
        if "word_zero_based" in data:
            word = data["word_zero_based"]
            n = data["n"]
            yield n, word, path.name
        for key, value in data.items():
            if isinstance(value, dict) and "word_zero_based" in value:
                word = value["word_zero_based"]
                n = len(value.get("caps", [])) or data.get("n")
                if n:
                    yield n, word, f"{path.name}:{key}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=20)
    args = parser.parse_args()
    for n, word, label in saved_words():
        if n > args.max_n:
            continue
        records, count = audit_word_fast(n, word)
        onion = audit_onion_fast(n, word)
        best = min(records, key=lambda row: row[1] / row[2])
        print(
            f"{label}: n={n}, V={count}, hull={len(records)}, "
            f"best_ratio={best[1]/best[2]:.12g}, pass={any(row[0] for row in records)}, "
            f"onion_ratio={onion[1]/onion[2]:.12g}, onion_pass={onion[0]}"
        )
        if not any(row[0] for row in records) or not onion[0]:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
