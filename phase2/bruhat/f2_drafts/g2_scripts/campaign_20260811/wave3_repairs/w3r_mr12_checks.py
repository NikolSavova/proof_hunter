#!/usr/bin/env python3
"""w3r_mr12_checks.py — wave-3 repairs application: MR-1/MR-2 transcription
checks (referee_maths_theoremA.md §6, fixes supplied there and verified in
referee_checks_theoremA.py sections 3/7), the MR-2/N-F2 polynomial
certificate UPGRADED to proof-grade (sympy Sturm/real-root count, same
class as g1_b Lemma B.0(ii)), the harness C5-erratum arithmetic
(varfit(4) = 91/108 < 187/216 <= varfit(5) = 7/8), and the N-F3
margin-pair arithmetic. All verdict arithmetic exact Fraction/integer;
sympy used only for the exact polynomial real-root certificate.
"""
from fractions import Fraction as F
import math

def S4(m):  return F(m*(m+1)*(2*m+1)*(3*m*m+3*m-1), 30)
def lam(m): return F(m*(m-1)*(2*m+5), 72)
def B(m):   return (S4(m) - m) / (240 * lam(m)**2)

C_KER4 = F(378100442, 10000)
GRID   = F(532, 100) + C_KER4          # C_A grid  = 37815.3642
CLOSED = F(1878, 10) + C_KER4          # C_A closed = 37997.8442
E4     = F(248992, 100000000)
TARGET = F(187, 216)

print("== (1) MR-1: B.0(ii)-based all-m>=401 positivity floor for the R3 w^2-bracket ==")
print("   bracket(m) := 6.85*E4*(1 - 17*B_m - C_A/m^2) - B_m ; floor g(m) uses B_m <= 1.080/m (B.0(ii), proof-grade):")
print("   g(m) = 6.85*E4*(1 - 18.36/m - C_A/m^2) - 1.080/m   [18.36 = 17*1.080]")
def bracket(m, C): return F(685,100)*E4*(1 - 17*B(m) - C/F(m*m)) - B(m)
def g(m, C): return F(685,100)*E4*(1 - F(1836,100)/m - C/F(m*m)) - F(1080,1000)/m
for tag, C in (("grid", GRID), ("closed", CLOSED)):
    print("   %-6s: bracket(401) = %.6f ; floor g(401) = %.6f > 0: %s" %
          (tag, float(bracket(401, C)), float(g(401, C)), g(401, C) > 0))
print("   g is term-by-term increasing in m (each of -1/m, -1/m^2 enters with negative sign),")
print("   spot-verified g(m+1) > g(m) at m in {401, 1000, 5000, 10^5}: %s" %
      all(g(m+1, C) > g(m, C) for C in (GRID, CLOSED) for m in (401, 1000, 5000, 10**5)))
print("   => bracket(m) >= g(m) >= g(401) > 0 for ALL m >= 401, no scan (MR-1 discharged).")

print("\n== (2) MR-2/N-F2: the 27/25-recentring certificate, PROOF-GRADE ==")
print("   claim: 0 <= (27/25)/m - B_m <= 0.55/m^2 for all m >= 30")
print("   lower side = B.0(ii) upper bound B_m <= 1.080/m = (27/25)/m (g1_b, proof-grade).")
print("   upper side: q(m) := (11/20)/m^2 - (27/25)/m + B_m >= 0 for m >= 30 — polynomial certificate:")
import sympy as sp
ms = sp.symbols('m', positive=True)
S4s = ms*(ms+1)*(2*ms+1)*(3*ms*ms+3*ms-1)/30
lams = ms*(ms-1)*(2*ms+5)/72
Bs = (S4s - ms) / (240 * lams**2)
qs = sp.together(sp.Rational(11,20)/ms**2 - sp.Rational(27,25)/ms + Bs)
num, den = sp.fraction(qs)
num = sp.expand(num); den = sp.expand(den)
P = sp.Poly(num, ms)
print("   q(m) = N(m)/D(m), D(m) = %s > 0 for m >= 2 (product of positive factors)" % sp.factor(den))
print("   N(m) = %s" % P.as_expr())
roots = sp.polys.polytools.count_roots(P, 30, sp.oo)
allroots = sp.polys.polytools.count_roots(P, -sp.oo, sp.oo)
q30 = F(11,20)/F(30*30) - F(27,25)/30 + B(30)
print("   real roots of N in [30, oo): %d (total real roots: %d)" % (roots, allroots))
print("   q(30) = %s = %.3e > 0: %s" % (q30, float(q30), q30 > 0))
print("   => N has no sign change on [30, oo) and is positive at 30: q(m) >= 0 for ALL m >= 30: %s"
      % (roots == 0 and q30 > 0))
print("   measured d(m) = ((27/25)/m - B_m)*m^2 (matches referee scans, safe direction):")
for m in (30, 100, 401, 2000, 10**5):
    print("     m=%6d  d = %.4f" % (m, float((F(27,25)/m - B(m))*m*m)))
dinf = sp.limit(sp.together((sp.Rational(27,25)/ms - Bs)*ms**2), ms, sp.oo)
print("   exact limit of d(m) as m -> oo: %s = %.4f  (< 0.55: certificate is honest, not padded)"
      % (dinf, float(dinf)))
print("   => two-sided O(m^-2) constant for the (27/25)-centered form: C_A + 0.55 (MR-2 flavor (b)).")

print("\n== (3) C5-erratum arithmetic (harness scope 5 <= m, not 4 <= m) ==")
row = [1]
vf = {}
for mm in range(2, 7):
    cum = [0]*(len(row)+1)
    for i, v in enumerate(row): cum[i+1] = cum[i] + v
    row = [cum[min(i+1, len(row))] - cum[max(0, i+1-mm)] for i in range(len(row)+mm-1)]
    if mm >= 4:
        N = mm*(mm-1)//2
        assert row == row[::-1]
        best = min(range(1, N), key=lambda k: F(row[k]*row[k], row[k-1]*row[k+1]))
        vf[mm] = lam(mm) * (F(row[best]**2, row[best-1]*row[best+1]) - 1)
print("   varfit(4) = %s ; == 91/108: %s ; < 187/216: %s" % (vf[4], vf[4] == F(91,108), vf[4] < TARGET))
print("   varfit(5) = %s ; == 7/8: %s ; >= 187/216: %s" % (vf[5], vf[5] == F(7,8), vf[5] >= TARGET))
print("   varfit(6) = %s ; == 187/216 (equality case): %s" % (vf[6], vf[6] == TARGET))
print("   => C5 as displayed ('4 <= m <= 400') is FALSE at m = 4 and true on 5 <= m <= 400;")
print("      run_m200.py line 106 exempts m = 4 by design — display erratum only.")

print("\n== (4) N-F3: the two spec-point margin ratios (both correct, mixed in the text) ==")
b1 = F(20,1)/F(795,10)      # 20/79.5 budget
eps = F(1291739, 5000000)   # eps* (repaired)
truth = F(385, 10000)       # measured 0.0385 at the spec point (wp3-a2 NC-P3d)
print("   20/79.5 = %.6f ; eps* = %.7f ; measured 0.0385" % (float(b1), float(eps)))
print("   budget ratio  (20/79.5)/0.0385 = %.2f  -> '6.5x'" % float(b1/truth))
print("   eps*  ratio   eps*/0.0385      = %.2f  -> '6.7x'" % float(eps/truth))
print("DONE")
