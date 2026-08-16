#!/usr/bin/env python3
"""Exact checks for MASS_UNIFORM_CARRIER_FRAGMENTATION_GATE."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import runpy


# Abstract scalable parity code.
A = 5
q = 5
code = [w for w in product(range(A), repeat=q) if sum(w) % A == 0]
assert len(code) == A ** (q - 1)

branch_ratios = []
prefixes = [()]
for depth in range(q):
    next_prefixes = []
    ratios = set()
    for pref in prefixes:
        members = [w for w in code if w[:depth] == pref]
        counts = Counter(w[depth] for w in members)
        assert len(set(counts.values())) == 1
        ratios.add(sum(counts.values()) // max(counts.values()))
        next_prefixes.extend(pref + (z,) for z in sorted(counts))
    assert len(ratios) == 1
    branch_ratios.append(ratios.pop())
    prefixes = next_prefixes

assert branch_ratios == [A] * (q - 1) + [1]
c_eff = 1
for r in branch_ratios:
    c_eff *= r
assert c_eff == len(code)
p0 = A**q
assert p0 // c_eff == A

# Removing any coordinate from a parity word determines the missing label:
# every literal carrier fibre has size one.
for i in range(q):
    seen = {}
    for w in code:
        carrier = w[:i] + w[i + 1 :]
        assert carrier not in seen
        seen[carrier] = w[i]
    assert len(seen) == len(code)

# Exact atom-floor calibration.  A cyclic N-regular graph has atom 1/N and
# unit mass on every source and every target.
N = q * (4 * A + 2)  # 2q carrier vertices plus q(A+3A) local labels.
C = len(code)
assert C >= N
source_mass = [Fraction(0) for _ in range(C)]
target_mass = [Fraction(0) for _ in range(C)]
atom = Fraction(1, N)
edge_count = 0
for s in range(C):
    for shift in range(N):
        t = (s + shift) % C
        source_mass[s] += atom
        target_mass[t] += atom
        edge_count += 1
assert edge_count == N * C
assert all(x == 1 for x in source_mass)
assert all(x == 1 for x in target_mass)
assert sum(source_mass) == C

# Exact exponent comparison for the scalable independent-ear realization.
selected_atoms = N * A ** (q - 1)
mixed_bank = A ** (2 * q)
rooted_bank = A ** (3 * q)
assert rooted_bank > mixed_bank > selected_atoms

# Reuse the exact rational q=2,A=3 ear instance.  run_path executes its
# independent assertions and exposes the verified geometry.
here = Path(__file__).resolve().parent
ns = runpy.run_path(
    str(here / "verify_high_transversal_common_pocket_endpoint_product.py")
)
roles = ns["roles"]
BASE = ns["BASE"]
is_face = ns["is_face"]

# Parity target words b0+b1=0 mod 3 are ordinary and uniform.
small_code = [(b, (-b) % 3) for b in range(3)]
for w in small_code:
    out = BASE[:]
    out.extend(roles[0]["tris"][w[0]])
    out.extend(roles[1]["tris"][w[1]])
    assert is_face(out)

# Deleting role 0 leaves the role-1 triangle, which determines the deleted
# role-0 label.  Thus literal carrier fibres have support one.
literal_fibres = defaultdict(set)
for b0, b1 in small_code:
    carrier = frozenset(BASE + list(roles[1]["tris"][b1]))
    literal_fibres[carrier].add(b0)
assert len(literal_fibres) == 3
assert all(len(vals) == 1 for vals in literal_fibres.values())

# After coarsening to BASE, every rooted ell-x-r module is ordinary.
coarsened = set()
for role_index in range(2):
    role = roles[role_index]
    for a, b, c in product(range(3), repeat=3):
        out = BASE + [
            role["tris"][b][0],
            role["sources"][a],
            role["tris"][c][2],
        ]
        assert is_face(out)
        coarsened.add(frozenset(out))
assert len(coarsened) == 2 * 3**3

print(
    "PASS: mass-uniform parity forest has singleton literal carrier "
    "fibres and exact atom floor; code=%d, ratios=%s, Qeff=%d, "
    "atoms=%d, coarsened_rooted=%d"
    % (C, branch_ratios, p0 // c_eff, edge_count, len(coarsened))
)
