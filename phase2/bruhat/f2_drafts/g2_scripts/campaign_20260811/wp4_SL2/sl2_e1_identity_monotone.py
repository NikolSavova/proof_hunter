#!/usr/bin/env python3
"""SL2 / E1 -- exact verification of the closed-form variance identity
(Lemma SL2.0 of wp4_sl_SL2.md) and re-check of part (i) monotonicity,
plus the plan's W7 anchor.

Identity, in E = e^{lam} = 1/q (q = tilt weight ratio; P(U_j = i) prop q^i
on {0,...,j-1}):
    Var(U_j^lam) = E/(E-1)^2 - j^2 E^j/(E^j - 1)^2      (lam != 0)
                 = (j^2 - 1)/12                          (lam  = 0)
Equivalently  lam^2 Var(U_j^lam) = h(lam) - h(j lam),
h(x) = x^2 e^x/(e^x - 1)^2 = (x / (2 sinh(x/2)))^2.

Checks:
  E1.1  exact-Fraction identity over a q-grid (both signs of lam,
        including the untilted point q = 1) x j <= 60;
  E1.2  float monotonicity re-check on the plan's grid lam in
        {0.01,...,0.89} x j <= 60 (the PROOF is Lemma SL2.1; this
        mirrors NC-PL1's "0 violations" count);
  E1.3  the plan's W7 anchor Var(U_3^{0.89}) * 0.89^2 (NC-PL1: 0.3666);
  E1.4  spot-row of h (strictly decreasing; proof = sinh series).
"""
from fractions import Fraction
import math

def var_direct(q, j):
    """Exact Var of U_j with weights q^i, i = 0..j-1 (q a Fraction)."""
    ws = [q**i for i in range(j)]
    Z = sum(ws)
    m1 = sum(i * wt for i, wt in enumerate(ws)) / Z
    m2 = sum(i * i * wt for i, wt in enumerate(ws)) / Z
    return m2 - m1 * m1

def var_formula(q, j):
    if q == 1:
        return Fraction(j * j - 1, 12)
    E = 1 / q
    Ej = E**j
    return E / (E - 1)**2 - j * j * Ej / (Ej - 1)**2

qs = [Fraction(1, 10), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
      Fraction(9, 10), Fraction(99, 100), Fraction(1),
      Fraction(101, 100), Fraction(3, 2), Fraction(2), Fraction(10)]
n = bad = 0
for q in qs:
    for j in range(1, 61):
        n += 1
        if var_direct(q, j) != var_formula(q, j):
            bad += 1
            print("IDENTITY FAIL at q=%s j=%d" % (q, j))
print("E1.1 identity: %d (q, j) pairs compared in exact Fractions; "
      "mismatches = %d" % (n, bad))

viol = 0
for ilam in range(1, 90):
    lam = ilam / 100.0
    prev = None
    for j in range(1, 61):
        E = math.exp(lam)
        Ej = math.exp(lam * j)
        var = E / (E - 1)**2 - j * j * Ej / (Ej - 1)**2
        if prev is not None and var < prev - 1e-12:
            viol += 1
        prev = var
print("E1.2 variance-monotone-in-j violations, "
      "lam in {0.01..0.89} x j <= 60: %d" % viol)

lam = 0.89
E = math.exp(lam)
E3 = math.exp(3 * lam)
v3 = E / (E - 1)**2 - 9.0 * E3 / (E3 - 1)**2
print("E1.3 anchor Var(U_3^{0.89}) * 0.89^2 = %.4f   [NC-PL1 quotes 0.3666]"
      % (v3 * lam * lam))

def h(x):
    s = 2.0 * math.sinh(x / 2.0)
    return (x / s)**2
print("E1.4 h(x) spot-row, x = 0.5, 1, 2, 4, 6, 8, 10:")
print("      " + "  ".join("%.6f" % h(x) for x in (0.5, 1, 2, 4, 6, 8, 10)))
