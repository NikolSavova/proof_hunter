#!/usr/bin/env python3
"""Exact adjudicator for any point set a campaign lane proposes.

The campaign briefs promise every lane that "any point set you propose will be checked in exact
rational arithmetic against an independent verifier that counts caps, cups and convex subsets from
orientation determinants only". This is that verifier. It shares no code path with the paper's
substitution formulas: it reads coordinates, computes orientation determinants, and runs dynamic
programs over them.

It answers the two questions the campaign turns on, for a proposed N-point set P:

  (a) the CAP-CUP PRODUCT, log2 C(P) + log2 U(P), against the target (1/2)(log2 N)^2.
      A lane claiming to refute the general lemma must produce a set where this falls short by a
      margin that grows with N -- a single small deficit is not a refutation, since the target
      carries an o(1).
  (b) the CONVEX-SUBSET COUNT, log2 W(P), against (1/2)(log2 N)^2. A lane claiming to beat the
      upper coefficient 1/2 must drive this down.

Input: a file of coordinates, one point per line, "x y", each an integer or a rational "p/q".
Exact arithmetic throughout; general position is checked and a violation is fatal.

Usage:
  ./check_candidate.py points.txt
  ./check_candidate.py --selftest
"""
import sys
from fractions import Fraction as F
from math import log2


def orient(p, q, r):
    d = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    return (d > 0) - (d < 0)


def read_points(path):
    pts = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        a, b = line.replace(",", " ").split()[:2]
        pts.append((F(a), F(b)))
    return sorted(set(pts))


def general_position(P):
    n = len(P)
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                if orient(P[a], P[b], P[c]) == 0:
                    return (P[a], P[b], P[c])
    return None


def endpoint_chains(P, sign):
    """res[(i,j)] = number of chains with first point i, last point j, of the given orientation
    sign, counting the 2-point chain. One DP per starting point."""
    n = len(P)
    res = {}
    for s in range(n):
        f = {}
        for j in range(s + 1, n):
            f[(s, j)] = 1
        for i in range(s + 1, n):
            for j in range(i + 1, n):
                tot = f.get((i, j), 0)
                for h in range(s, i):
                    if (h, i) in f and orient(P[h], P[i], P[j]) == sign:
                        tot += f[(h, i)]
                if tot:
                    f[(i, j)] = tot
        for j in range(s + 1, n):
            v = sum(f.get((i, j), 0) for i in range(s, j))
            if v:
                res[(s, j)] = v
    return res


def measure(P):
    n = len(P)
    caps = endpoint_chains(P, -1)
    cups = endpoint_chains(P, +1)
    C = n + sum(caps.values())
    U = n + sum(cups.values())
    W = n + sum(caps.get(k, 0) * cups.get(k, 0) for k in set(caps) | set(cups))
    M = max([1] + [caps.get(k, 0) * cups.get(k, 0) for k in set(caps) & set(cups)])
    return C, U, W, M


def report(P, label=""):
    n = len(P)
    bad = general_position(P)
    if bad:
        print(f"FATAL: not in general position -- collinear triple {bad}")
        return False
    C, U, W, M = measure(P)
    L = log2(n)
    target = 0.5 * L * L
    prod = log2(C) + log2(U)
    print(f"{label}N = {n}   log2 N = {L:.4f}   target (1/2)(log2 N)^2 = {target:.4f}")
    print(f"  C = {C}   U = {U}   W = {W}   max_pq c*u = {M}")
    print(f"  [a] cap-cup product  log2 C + log2 U = {prod:.4f}"
          f"   deficit vs target = {target - prod:+.4f}")
    print(f"  [b] convex count     log2 W           = {log2(W):.4f}"
          f"   deficit vs target = {target - log2(W):+.4f}")
    print(f"      endpoint-localized log2 max c*u  = {log2(M):.4f}")
    print("  NOTE: the target carries an o(1); a deficit at one N proves nothing. A refutation")
    print("  needs the deficit to GROW with N along a family.")
    return True


def selftest():
    """Reproduce the audited 36-point composition, whose (C,U,W) is known to be
    (14136, 14136, 441399); see independent_check.py and paper section 'Verification artifact'."""
    def prec(A, B, e):
        return [(e * e * x, e * y) for (x, y) in A] + [(1 + e * e * x, 1 + e * y) for (x, y) in B]

    def T(m, i, e):
        return [(F(0), F(0))] if i in (0, m) else prec(T(m - 1, i - 1, e), T(m - 1, i, e), e)

    S = sorted(T(4, 2, F(1, 97)))
    e = F(1, 16384)
    B = sorted([(X + e * e * x, Y + e * y) for (X, Y) in S for (x, y) in S])
    C, U, W, _ = measure(B)
    ok = (C, U, W) == (14136, 14136, 441399)
    print(f"selftest on the 36-point composition: (C,U,W) = ({C}, {U}, {W})  expected "
          f"(14136, 14136, 441399)  -> {'PASS' if ok else 'FAIL'}")
    report(S, label="template T_(4,2): ")
    return ok


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        raise SystemExit(0 if selftest() else 1)
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    raise SystemExit(0 if report(read_points(sys.argv[1])) else 1)
