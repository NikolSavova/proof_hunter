#!/usr/bin/env python3
"""NC-P4 (wp3-a2): the stitching threshold table (Theorem S) — every number
printed here is consumed verbatim by draft §5/§6.

Inputs (all certified elsewhere in this package or cited):
  clause ladder (NC-P2): (c, m_p): (1/4,30) (1/2,83) (7/10,300) (1,1581)
  s2 floor on k >= c m (T.5-final, cited PROVED): s2 >= v(c) m, v = c(1+c)/6
  tilt cap (P.8): lam(k) <= log(1+1/c) on k >= c m
  deficit floor (P.7, NC-P3b): deficit >= 6.85 w0^2 E(w0), E(4) >= 0.00248992
  operating point: w0 = 4 (region 3 = |w| <= 4 = wp2-b's K = 4 dictionary),
  delta = 0.02 (region-2 conclusion r-1 >= (1+delta)/lambda).
"""
from math import log, sqrt

E4 = 0.00248992           # certified lower decimal (NC-P3b)
rho4 = 1 - 6.85 * 16 * E4 # upper bound on s2/lambda at |w| >= 4
delta = 0.02
eps_star = 1 - (1 + delta) * rho4

def v(c): return c * (1 + c) / 6

print("== operating point ==")
print(f"  w0 = 4, E(4) >= {E4}, deficit floor {6.85*16*E4:.4f}, rho(4) <= {rho4:.4f}")
print(f"  delta = {delta}; region-2 eps budget eps* = 1 - (1+delta)rho(4) = {eps_star:.4f}")
print(f"  R3 w^2-coefficient condition: 6.85 E(4) = {6.85*E4:.5f} >= 1.08/m  <=>  m >= "
      f"{1.08/(6.85*E4):.1f}")

print("== clause ladder and per-range wp4 requirements ==")
print("  m-range        clause c   s2 floor at range start   tilt cap   C_0* max   C* max")
ranges = [ (401, 1581, 0.7), (1581, None, 1.0) ]
for m0, m1, c in ranges:
    floor0 = v(c) * m0
    cap = log(1 + 1 / c)
    c0max = int(floor0)
    cmax = int(eps_star * floor0)
    r = f"[{m0}, {m1})" if m1 else f"[{m0}, inf)"
    print(f"  {r:14s}   {c:.2f}     {v(c):.4f}*m >= {floor0:8.1f}       {cap:.4f}    "
          f"{c0max:6d}    {cmax:5d}")

print("== global single spec for all m >= 401 (worst over ranges) ==")
floor_glob = v(0.7) * 401
print(f"  C_0* <= {int(floor_glob)},  C* <= {int(eps_star*floor_glob)},  "
      f"Lambda* >= {log(1+1/0.7):.4f} (say 0.89);  truth (NC-P3d): eps <= 0.0385 at m = 30, "
      f"falling ~1.2/m — margin ~{eps_star/0.0385:.0f}x at m=30 and growing")

print("== legacy-constant rows (what the old arithmetic gave / gives now) ==")
# old: inner edge k ~ sqrt(m)/4, floor s2 >= sqrt(m)/24  -> s2 >= 2000 iff m >= (24*2000)^2
print(f"  OLD (T2 item 2): floor sqrt(m)/24 >= 2000  <=>  m >= {(24*2000)**2:.1e}")
# new with C_0 = 2000 intact: c = 1 clause, m/3 >= 2000
print(f"  NEW, C_0* = 2000 intact: c=1 clause (m >= 1581), m/3 >= 2000  <=>  m >= 6000")
print(f"  NEW, C_0* = 2000, c=0.7 clause: 0.1983 m >= 2000  <=>  m >= {2000/0.1983:.0f} "
      f"(c=1 clause is better)")
# improvement factor
print(f"  improvement factor on the C_0 = 2000 threshold: {(24*2000)**2/6000:.1e}x")

print("== R1 margin over sigma^-2 at the region-1' edge (k = c m) ==")
for m0, c in ((401, 0.7), (1581, 1.0)):
    lam = m0 * (m0 - 1) * (2 * m0 + 5) / 72.0
    s_half = (m0 - 1) / (2 * c * m0 * (1 + c) * m0)
    print(f"  m = {m0}, c = {c}: (signal/2)*lambda = {s_half*lam:.0f}x sigma^-2")

print("== harness note ==")
print("  m <= 400: all of Theorem A parts (a-finite)/(b)/(c-finite) exact "
      "(harness_m200_20260811.md, C1-C6); the analytic stitch is only needed for m >= 401.")
